# Source: https://clickhouse.ferndocs.com/integrations/draxlr.md

---
sidebar_label: Draxlr
sidebar_position: 131
slug: /integrations/draxlr
keywords:

- clickhouse
- Draxlr
- connect
- integrate
- ui
description: Draxlr is a Business intelligence tool with data visualization and analytics.
title: Connecting Draxlr to ClickHouse
doc_type: guide
integration:
- support_level: partner
- category: data_visualization

---

import {CommunityMaintainedBadge} from "@site/components/Badges/CommunityMaintainedBadge"

<CommunityMaintainedBadge/>

Draxlr offers an intuitive interface for connecting to your ClickHouse database, enabling your team to explore, visualize, and publish insights within minutes. This guide will walk you through the steps to establish a successful connection.

## 1. Get your ClickHouse credentials [#1-get-your-clickhouse-credentials]

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

## 2.  Connect Draxlr to ClickHouse [#2--connect-draxlr-to-clickhouse]

1. Click on the **Connect a Database** button on the navbar.

2. Select **ClickHouse** from the list of available databases and click next.

3. Choose one of the hosting services and click next.

4. Use any name in the **Connection Name** field.

5. Add the connection details in the form.

  <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/82890d47bd445ddaac8be3e6dfe4dc60dd0d5d44495452f06ed6ca1abd3f60b3/images/integrations/data-visualization/draxlr_01.png" alt="Draxlr connection form showing ClickHouse database configuration options" />

1. Click on the **Next** button and wait for the connection to be established. You will see the tables page if the connection is successful.

## 4. Explore your data [#4-explore-your-data]

1. Click on one of the tables in the list.

2. It will take you to the explore page to see the data in the table.

3. You can start adding the filters, make joins and add sort to your data.

  <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f789e44e24db9c2d33ba65ec9b085d4a8de0a8807ebb202db62c8830bcde919b/images/integrations/data-visualization/draxlr_02.png" alt="Draxlr data exploration interface showing filters and sorting options" />

1. You can also use the **Graph** button and select the graph type to visualize the data.

  <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9dc85faa953cf742f2bc153ff02171e754aa9d2e1a0386e0ea1a0f865c11c84f/images/integrations/data-visualization/draxlr_05.png" alt="Draxlr graph visualization options for ClickHouse data" />

## 4. Using SQL queries [#4-using-sql-queries]

1. Click on the Explore button on the navbar.

2. Click the **Raw Query** button and enter your query in the text area.

  <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/4f58397ed86bc20658951d7839052b915d695d1f66af539acb6ebfb11a34d835/images/integrations/data-visualization/draxlr_03.png" alt="Draxlr SQL query interface for ClickHouse" />

1. Click on the **Execute Query** button to see the results.

## 4. Saving you query [#4-saving-you-query]

1. After executing your query, click on the **Save Query** button.

  <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/decda3d893d976496600318ad29167c41e30d8b0c1fa4cd140abec2adfc98404/images/integrations/data-visualization/draxlr_04.png" alt="Draxlr save query dialog with dashboard options" />

1. You can name to query in **Query Name** text box and select a folder to categories it.

2. You can also use **Add to dashboard** option to add the result to dashboard.

3. Click on the **Save** button to save the query.

## 5. Building dashboards [#5-building-dashboards]

1. Click on the **Dashboards** button on the navbar.

  <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5b4c5a12f4ce7000deb468eb327962e84a16fba1f09543798d2d1d9f003560b9/images/integrations/data-visualization/draxlr_06.png" alt="Draxlr dashboard management interface" />

1. You can add a new dashboard by clicking on the **Add +** button on the left sidebar.

2. To add a new widget, click on the **Add** button on the top right corner.

3. You can select a query from the list of saved queries and choose the visualization type then click on the **Add Dashboard Item** button.

## Learn more [#learn-more]

To know more about Draxlr you can visit [Draxlr documentation](https://draxlr.notion.site/draxlr/Draxlr-Docs-d228b23383f64d00a70836ff9643a928) site.
