# Source: https://clickhouse.ferndocs.com/integrations/metabase.md

---
sidebar_label: Metabase
sidebar_position: 131
slug: /integrations/metabase
keywords:
  - Metabase
description: >-
  Metabase is an easy-to-use, open source UI tool for asking questions about
  your data.
title: Connecting Metabase to ClickHouse
show_related_blogs: true
doc_type: guide
integration:
  - support_level: core
  - category: data_visualization
  - website: 'https://github.com/clickhouse/metabase-clickhouse-driver'
---

import {PartnerBadge} from '../../../../../components/Badges/PartnerBadge'

<PartnerBadge/>

Metabase is an easy-to-use, open source UI tool for asking questions about your data. Metabase is a Java application that can be run by simply <a href="https://www.metabase.com/start/oss/jar" target="_blank">downloading the JAR file</a> and running it with `java -jar metabase.jar`. Metabase connects to ClickHouse using a JDBC driver that you download and put in the `plugins` folder:

## Goal [#goal]

In this guide you will ask some questions of your ClickHouse data with Metabase and visualize the answers.  One of the answers will look like this:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/618f8d5e6a9e2c0d1b1e70dc4f79d32ad8d941c7343405009f7cfb44197e1846/images/integrations/data-visualization/metabase_08.png" alt="Metabase pie chart visualization showing data from ClickHouse" />

<Tip title="Add some data">
If you do not have a dataset to work with you can add one of the examples.  This guide uses the [UK Price Paid](/getting-started/example-datasets/uk-price-paid.md) dataset, so you might choose that one.  There are several others to look at in the same documentation category.
</Tip>

## 1. Gather your connection details [#1-gather-your-connection-details]

To connect to ClickHouse with HTTP(S) you need this information:

| Parameter(s)            | Description                                                                                                   |
|-------------------------|---------------------------------------------------------------------------------------------------------------|
|`HOST` and `PORT`        | Typically, the port is 8443 when using TLS or 8123 when not using TLS.                                        |
|`DATABASE NAME`          | Out of the box, there is a database named `default`, use the name of the database that you want to connect to.|
|`USERNAME` and `PASSWORD`| Out of the box, the username is `default`. Use the username appropriate for your use case.                    |

The details for your ClickHouse Cloud service are available in the ClickHouse Cloud console.
Select a service and click **Connect**:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9de2a784fe6ef2c5c51be720b96cb4bb7ebd0838901449759f587e0df6d9034a/images/_snippets/cloud-connect-button.png" alt="ClickHouse Cloud service connect button" />

Choose **HTTPS**. Connection details are displayed in an example `curl` command.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/710d528cac4deb00e877550b033fe8d67e19e1a8f825c75889eb0573ab25f7b0/images/_snippets/connection-details-https.png" alt="ClickHouse Cloud HTTPS connection details" />

If you are using self-managed ClickHouse, the connection details are set by your ClickHouse administrator.


## 2.  Download the ClickHouse plugin for Metabase [#2--download-the-clickhouse-plugin-for-metabase]

1. If you do not have a `plugins` folder, create one as a subfolder of where you have `metabase.jar` saved.

2. The plugin is a JAR file named `clickhouse.metabase-driver.jar`. Download the latest version of the JAR file at <a href="https://github.com/clickhouse/metabase-clickhouse-driver/release" target="_blank">https://github.com/clickhouse/metabase-clickhouse-driver/releases/latest</a>

3. Save `clickhouse.metabase-driver.jar` in your `plugins` folder.

4. Start (or restart) Metabase so that the driver gets loaded properly.

5. Access Metabase at <a href="http://localhost:3000/" target="_blank">http://hostname:3000</a>. On the initial startup, you will see a welcome screen and have to work your way through a list of questions. If prompted to select a database, select "**I'll add my data later**":

## 3.  Connect Metabase to ClickHouse [#3--connect-metabase-to-clickhouse]

1. Click on the gear icon in the top-right corner and select **Admin Settings** to visit your <a href="http://localhost:3000/admin/settings/setup" target="_blank">Metabase admin page</a>.

2. Click on **Add a database**. Alternately, you can click on the **Databases** tab and select the **Add database** button.

3. If your driver installation worked, you will see **ClickHouse** in the dropdown menu for **Database type**:

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5fdbd5ce3aac418fbe23405d3b6cc8846eae580f042931957105ccfd7295c38e/images/integrations/data-visualization/metabase_01.png" alt="Metabase database selection showing ClickHouse as an option" />

4. Give your database a **Display name**, which is a Metabase setting - so use any name you like.

5. Enter the connection details of your ClickHouse database. Enable a secure connection if your ClickHouse server is configured to use SSL. For example:

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/faf1d40220401783636a7e4ab5927e0b9ddcb0360b6fd553f4f7a846a712afc5/images/integrations/data-visualization/metabase_02.png" alt="Metabase connection details form for ClickHouse database" />

6. Click the **Save** button and Metabase will scan your database for tables.

## 4. Run a SQL query [#4-run-a-sql-query]

1. Exit the **Admin settings** by clicking the **Exit admin** button in the top-right corner.

2. In the top-right corner, click the **+ New** menu and notice you can ask questions, run SQL queries, and build a dashboard:

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/cefe3210427f49684e7bb812e769564cb75edecd83289135df8f735802c8d032/images/integrations/data-visualization/metabase_03.png" alt="Metabase New menu showing options to create questions, SQL queries, and dashboards" />

3. For example, here is a SQL query run on a table named `uk_price_paid` that returns the average price paid by year from 1995 to 2022:

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/055839e676371695d8db5bb369688c80f08da928ce7ca007c7f256564498e707/images/integrations/data-visualization/metabase_04.png" alt="Metabase SQL editor showing a query on UK price paid data" />

## 5. Ask a question [#5-ask-a-question]

1. Click on **+ New** and select **Question**. Notice you can build a question by starting with a database and table. For example, the following question is being asked of a table named `uk_price_paid` in the `default` database. Here is a simple question that calculates the average price by town, within the county of Greater Manchester:

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/4ef80fb49d29b986e13cc5c0406e874b0d195e1aab951a12cedb1a8567bb096f/images/integrations/data-visualization/metabase_06.png" alt="Metabase question builder interface with UK price data" />

2. Click the **Visualize** button to see the results in a tabular view.

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/83e17cb8e4f0b6b1489236a4eee3854e6d219a6815d5e32f18dff3f542be5965/images/integrations/data-visualization/metabase_07.png" alt="Metabase visualization showing tabular results of average prices by town" />

3. Below the results, click the **Visualization** button to change the visualization to a bar chart (or any of the other options available):

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/618f8d5e6a9e2c0d1b1e70dc4f79d32ad8d941c7343405009f7cfb44197e1846/images/integrations/data-visualization/metabase_08.png" alt="Metabase pie chart visualization of average prices by town in Greater Manchester" />

## Learn more [#learn-more]

Find more information about Metabase and how to build dashboards by <a href="https://www.metabase.com/docs/latest/" target="_blank">visiting the Metabase documentation</a>.
