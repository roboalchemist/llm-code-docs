# Source: https://clickhouse.ferndocs.com/integrations/chartbrew-and-clickhouse.md

---
title: Connecting Chartbrew to ClickHouse
sidebar_label: Chartbrew
sidebar_position: 131
slug: /integrations/chartbrew-and-clickhouse
keywords:

- ClickHouse
- Chartbrew
- connect
- integrate
- visualization
description: >-
  Connect Chartbrew to ClickHouse to create real-time dashboards and client
  reports.
doc_type: guide

---

import {CommunityMaintainedBadge} from "@site/components/Badges/CommunityMaintainedBadge"

<CommunityMaintainedBadge/>

[Chartbrew](https://chartbrew.com) is a data visualization platform that allows users to create dashboards and monitor data in real time. It supports multiple data sources, including ClickHouse, and provides a no-code interface for building charts and reports.

## Goal [#goal]

In this guide, you will connect Chartbrew to ClickHouse, run a SQL query, and create a visualization. By the end, your dashboard may look something like this:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/dfcfabdd73b6cd4b553dcf7efcae825a1dde0b618ecc09049d5f6415ab4dcb5e/images/integrations/data-visualization/chartbrew_01.png" alt="Chartbrew dashboard"/>

<Tip title="Add some data">
If you do not have a dataset to work with, you can add one of the examples. This guide uses the [UK Price Paid](/getting-started/example-datasets/uk-price-paid.md) dataset.
</Tip>

## 1. Gather your connection details [#1-gather-your-connection-details]

<ConnectionDetails />

## 2. Connect Chartbrew to ClickHouse [#2-connect-chartbrew-to-clickhouse]

1. Log in to [Chartbrew](https://chartbrew.com/login) and go to the **Connections** tab.
2. Click **Create connection** and select **ClickHouse** from the available database options.

   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/24adcef7b9e3f6c2d247a099a589113623090258618649b4efe37a334fd1da0c/images/integrations/data-visualization/chartbrew_02.png" alt="Select ClickHouse connection in Chartbrew"/>

3. Enter the connection details for your ClickHouse database:

   - **Display Name**: A name to identify the connection in Chartbrew.
   - **Host**: The hostname or IP address of your ClickHouse server.
   - **Port**: Typically `8443` for HTTPS connections.
   - **Database Name**: The database you want to connect to.
   - **Username**: Your ClickHouse username.
   - **Password**: Your ClickHouse password.

   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/457752cdd6561fbc0479855e8abe59d7d3d52c8ea184ce446cd64eda1d96b696/images/integrations/data-visualization/chartbrew_03.png" alt="ClickHouse connection settings in Chartbrew"/>

4. Click **Test connection** to verify that Chartbrew can connect to ClickHouse.
5. If the test is successful, click **Save connection**. Chartbrew will automatically retrieve the schema from ClickHouse.

   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9aa92853190fe7af6b479844a553fe517f1fddc43a14f13be1fd0f387affba89/images/integrations/data-visualization/chartbrew_04.png" alt="ClickHouse JSON schema in Chartbrew"/>

## 3. Create a dataset and run a SQL query [#3-create-a-dataset-and-run-a-sql-query]

  1. Click on the **Create dataset** button or navigate to the **Datasets** tab to create one.
  2. Select the ClickHouse connection you created earlier.

  <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/bfa34c5a111d72f3b50f935b1602038f37634d02a62fdb7d45d04e7ebf2ad42e/images/integrations/data-visualization/chartbrew_05.png" alt="Select ClickHouse connection for dataset"/>

  Write a SQL query to retrieve the data you want to visualize. For example, this query calculates the average price paid per year from the `uk_price_paid` dataset:

  ```sql
  SELECT toYear(date) AS year, avg(price) AS avg_price
  FROM uk_price_paid
  GROUP BY year
  ORDER BY year;
  ```

  <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/6c0edbac3cdf4ae8d7197900781f22c28ff9cfc55c7d7b24f7ede2ee13214342/images/integrations/data-visualization/chartbrew_07.png" alt="ClickHouse SQL query in Chartbrew"/>

  Click **Run query** to fetch the data.

  If you're unsure how to write the query, you can use **Chartbrew's AI assistant** to generate SQL queries based on your database schema.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/32491d55926d2fc8ced3613850489fe37bd61c5d11e93e29f32da080b05810ea/images/integrations/data-visualization/chartbrew_06.png" alt="ClickHouse AI SQL assistant in Chartbrew"/>

Once the data is retrieved, click **Configure dataset** to set up the visualization parameters.

## 4. Create a visualization [#4-create-a-visualization]

  1. Define a metric (numerical value) and dimension (categorical value) for your visualization.
  2. Preview the dataset to ensure the query results are structured correctly.
  3. Choose a chart type (e.g., line chart, bar chart, pie chart) and add it to your dashboard.
  4. Click **Complete dataset** to finalize the setup.

  <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/ec0f405f2b6799ea13b38a73ccdca67d3c5e51852299f6e32881972ab82b69ed/images/integrations/data-visualization/chartbrew_08.png" alt="Chartbrew dashboard with ClickHouse data"/>

  You can create as many datasets as you want to visualize different aspects of your data. Using these datasets, you can create multiple dashboards to keep track of different metrics.

  <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/dfcfabdd73b6cd4b553dcf7efcae825a1dde0b618ecc09049d5f6415ab4dcb5e/images/integrations/data-visualization/chartbrew_01.png" alt="Chartbrew dashboard with ClickHouse data"/>

## 5. Automate data updates [#5-automate-data-updates]

  To keep your dashboard up-to-date, you can schedule automatic data updates:

  1. Click the Calendar icon next to the dataset refresh button.
  2. Configure the update interval (e.g., every hour, every day).
  3. Save the settings to enable automatic refresh.

  <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/905164327292426a44ff1605006afd3b17f026d97e12f72126e0f88d758e1f07/images/integrations/data-visualization/chartbrew_09.png" alt="Chartbrew dataset refresh settings"/>

## Learn more [#learn-more]

For more details, check out the blog post about [Chartbrew and ClickHouse](https://chartbrew.com/blog/visualizing-clickhouse-data-with-chartbrew-a-step-by-step-guide/).
