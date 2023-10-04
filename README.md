# Sales & Customer Insights Dashboard

![Dashboard Screenshot](insert_screenshot_url_here.png) <!-- Add a screenshot of your Tableau dashboard if available -->

## Table of Contents

- [Description](#description)
- [Dashboard Link](#dashboard-link)
- [Data Pipeline Overview](#data-pipeline-overview)
- [Contact Information](#contact-information)

## Description

The Sales & Customer Insights Dashboard provides insights into e-commerce data using Tableau. This README provides a brief overview of the dashboard and how to access it.

## Dashboard Link

You can access the Sales & Customer Insights Dashboard by clicking on the following link:

[View Sales & Customer Insights Dashboard](https://public.tableau.com/app/profile/kai.yin.chan/viz/SalesCustomerInsights/Dashboard1?publish=yes)

Feel free to explore the dashboard and interact with the data visualizations.

## Data Pipeline Overview

The Ecomminsight Dashboard is powered by a data pipeline that includes the following components:

- **Data Collection**: E-commerce data is collected and processed using custom scripts.

- **AWS Integration**: Processed data is uploaded to an AWS S3 bucket for storage.

- **Data Cataloging**: AWS Glue Crawler is used to catalog the data stored in the S3 bucket.

- **Data Querying**: AWS Athena is employed to query and access the cataloged data.

- **Visualization**: Tableau Desktop connects to AWS Athena as the data source to create interactive data visualizations.

## Contact Information

If you have any questions or feedback about the Sales & Customer Insights Dashboard, please contact me at [chankaiy@usc.edu].

