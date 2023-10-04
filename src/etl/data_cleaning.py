import os
import pandas as pd
import boto3
from io import BytesIO


s3 = boto3.client('s3')


script_dir = os.path.dirname(os.path.abspath(__file__))
# data = pd.read_csv("../../data/data.csv", encoding='ISO-8859-1')
data_csv_path = os.path.join(script_dir, '../../data/data.csv')
data = pd.read_csv(data_csv_path, encoding='ISO-8859-1')
data.InvoiceDate = pd.to_datetime(data.InvoiceDate)
# missing_values = data.isnull().sum()
# print(missing_values)


data['Year'] = data['InvoiceDate'].dt.year
data['Month'] = data['InvoiceDate'].dt.month
data['DayOfWeek'] = data['InvoiceDate'].dt.dayofweek
data['Description'] = data['Description'].str.lower().str.strip().replace(r'\s+', ' ', regex=True)

# Generate a mapping of StockCode to Description
stockcode_to_description = data.dropna(
    subset=['Description']).groupby('StockCode')['Description'].first()

# For rows with missing descriptions, look up the StockCode in the mapping and fill the description accordingly
data['Description'] = data.apply(lambda row: stockcode_to_description.get(row['StockCode'],
                                                                          'Unknown') if pd.isnull(row['Description']) else row['Description'], axis = 1)
data['Description'] = data['Description'].str.replace(',', ';')
data['TotalValue'] = data['Quantity'] * data['UnitPrice']
data['RefundFlag'] = data['Quantity'].apply(lambda x: 1 if x < 0 else 0)


processed_data_bytes = data.to_csv(index=False).encode('utf-8')
bucket_name = 'ecomminsight-data-bucket'
s3_object_key = 'data/processed_data.csv'
s3.upload_fileobj(BytesIO(processed_data_bytes), bucket_name, s3_object_key)

