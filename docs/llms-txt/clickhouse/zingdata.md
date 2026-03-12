# Source: https://clickhouse.ferndocs.com/integrations/zingdata.md

---
sidebar_label: Zing Data
sidebar_position: 206
slug: /integrations/zingdata
keywords:
  - Zing Data
description: >-
  Zing Data is simple social business intelligence for ClickHouse, made for iOS,
  Android and the web.
title: Connect Zing Data to ClickHouse
show_related_blogs: true
doc_type: guide
---

import {CommunityMaintainedBadge} from "@site/components/Badges/CommunityMaintainedBadge"

<CommunityMaintainedBadge/>

<a href="https://www.zingdata.com/" target="_blank">Zing Data</a> is a data exploration and visualization platform. Zing Data connects to ClickHouse using the JS driver provided by ClickHouse.

## How to connect [#how-to-connect]
1. Gather your connection details.
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


2. Download or visit Zing Data

    * To use Clickhouse with Zing Data on mobile, download the Zing data app on [Google Play Store](https://play.google.com/store/apps/details?id=com.getzingdata.android) or the [Apple App Store](https://apps.apple.com/us/app/zing-data-collaborative-bi/id1563294091).

    * To use Clickhouse with Zing Data on the web, visit the [Zing web console](https://console.getzingdata.com/) and create an account.

3. Add a datasource

    * To interact with your ClickHouse data with Zing Data, you need to define a **_datasource_**. On the mobile app menu in Zing Data, select **Sources**, then click on **Add a Datasource**.

    * To add a datasource on web, click on **Data Sources** on the top menu, click on **New Datasource** and select **Clickhouse** from the dropdown menu

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/48c0f4933f2e72adb4d8d692de8bdefaefc556be7f6c07e5dad32175ab4aae3e/images/integrations/data-visualization/zing_01.png" alt="Zing Data interface showing New Datasource button and ClickHouse option in the dropdown menu" />
    <br/>

4. Fill out the connection details and click on **Check Connection**.

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/d79d85934cfcf3be5f2fb0acadf5a1770e71dea86d4ea501b67ebd26afbd1d4f/images/integrations/data-visualization/zing_02.png" alt="ClickHouse connection configuration form in Zing Data with fields for server, port, database, username and password" />
    <br/>

5. If the connection is successful, Zing will proceed you to table selection. Select the required tables and click on **Save**. If Zing cannot connect to your data source, you'll see a message asking your to check your credentials and retry. If even after checking your credentials and retrying you still experience issues, <a id="contact_link" href="mailto:hello@getzingdata.com">reach out to Zing support here.</a>

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/22abf4e7915d3380225015700b00fe203993e87dacce3d7742537329e23e6392/images/integrations/data-visualization/zing_03.png" alt="Zing Data table selection interface showing available ClickHouse tables with checkboxes" />
    <br/>

6. Once the Clickhouse datasource is added, it will be available to everyone in your Zing organization, under the **Data Sources** / **Sources** tab.

## Creating charts and dashboards in Zing Data [#creating-charts-and-dashboards-in-zing-data]

1. After your Clickhouse datasource is added, click on **Zing App** on the web, or click on the datasource on mobile to start creating charts.

2. Click on a table under the table's list to create a chart.

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/ecfc7f05172f9fbee4224b3c7d8cb8f75df024f5eab26d900c951868fc02c69d/images/integrations/data-visualization/zing_04.png" alt="Zing Data interface showing the table list with available ClickHouse tables" />
    <br/>

3. Use the visual query builder to pick the desired fields, aggregations, etc., and click on **Run Question**.

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/bbd95c05b4f5353b8168d3bf7ce27b6a2495d41ecd96073d6cd2674fdf3497c5/images/integrations/data-visualization/zing_05.png" alt="Zing Data visual query builder interface with field selection and aggregation options" />
    <br/>

4. If you familiar with SQL, you can also write custom SQL to run queries and create a chart.

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/373c8f25c62011933d416a79c59089beb9952be1a940cd98f7c1add2b3a41135/images/integrations/data-visualization/zing_06.png" alt="SQL editor mode in Zing Data showing SQL query writing interface" />
    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/2e89d994124c1730a4d2c5061370d6709d6fa9222d0b062090039703482c80a7/images/integrations/data-visualization/zing_07.png" alt="SQL query results in Zing Data with data displayed in tabular format" />

5. An example chart would look as follows. The question can be saved using the three-dot menu. You can comment on the chart, tag your team members, create real-time alerts, change the chart type, etc.

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/3af2ea38f54c1c390adbe252be18125276ce1818ced0d0519281f43bcd542bc1/images/integrations/data-visualization/zing_08.png" alt="Example chart visualization in Zing Data showing data from ClickHouse with options menu" />
    <br/>

6. Dashboards can be created using the "+" icon under **Dashboards** on the Home screen. Existing questions can be dragged in, to be displayed on the dashboard.

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5aa6810979288f6d140d8fc1b3377e2d0e09ef60bb2c777a0ee4a1fc63c764a7/images/integrations/data-visualization/zing_09.png" alt="Zing Data dashboard view showing multiple visualizations arranged in a dashboard layout" />
    <br/>

## Related content [#related-content]

- [Documentation](https://docs.getzingdata.com/docs/)
- [Quick Start](https://getzingdata.com/quickstart/)
- Guide to [Create Dashboards](https://getzingdata.com/blog/new-feature-create-multi-question-dashboards/)
