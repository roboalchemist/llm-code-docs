# Source: https://clickhouse.ferndocs.com/integrations/datagrip.md

---
sidebar_label: DataGrip
slug: /integrations/datagrip
description: DataGrip is a database IDE that supports ClickHouse out of the box.
title: Connecting DataGrip to ClickHouse
doc_type: guide
integration:
  - support_level: partner
  - category: sql_client
  - website: 'https://www.jetbrains.com/datagrip/'
keywords:
  - DataGrip
  - database IDE
  - JetBrains
  - SQL client
  - integrated development environment
---

import {CommunityMaintainedBadge} from '../../../../../components/Badges/CommunityMaintainedBadge'

<CommunityMaintainedBadge/>

## Start or download DataGrip [#start-or-download-datagrip]

DataGrip is available at https://www.jetbrains.com/datagrip/

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


## 2. Load the ClickHouse driver [#2-load-the-clickhouse-driver]

1. Launch DataGrip, and on the **Data Sources** tab in the **Data Sources and Drivers** dialog, click the **+** icon

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9bf89a420315ce803911cdd878d3fb7b76d9d70d5d55cc3bd3c67f397339427f/images/integrations/sql-clients/datagrip-5.png" alt="DataGrip Data Sources tab with + icon highlighted"/>

  Select **ClickHouse**

  :::tip
  As you establish connections the order changes, ClickHouse may not be at the top of your list yet.
  :::

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/bb14e5cf2c558ea253d4c54a0def08de680b9917ef3ac652dff9fa54af8e9505/images/integrations/sql-clients/datagrip-6.png" alt="DataGrip selecting ClickHouse from the data sources list"/>

- Switch to the **Drivers** tab and load the ClickHouse driver

  DataGrip does not ship with drivers in order to minimize the download size.  On the **Drivers** tab
  Select **ClickHouse** from the **Complete Support** list, and expand the **+** sign.  Choose the **Latest stable** driver from the **Provided Driver** option:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/8accbfe1ed69ae321d14ce19c727fa141017fd7b0b9c9a94d40f6b17a2ed1d27/images/integrations/sql-clients/datagrip-1.png" alt="DataGrip Drivers tab showing ClickHouse driver installation"/>

## 3. Connect to ClickHouse [#3-connect-to-clickhouse]

- Specify your database connection details, and click **Test Connection**:

  In step one you gathered your connection details, fill in the host URL, port, username, password, and database name, then test the connection.

  :::tip
  The **HOST** entry in the DataGrip dialog is actually a URL, see the image below.

  For more details on JDBC URL settings, please refer to the [ClickHouse JDBC driver](https://github.com/ClickHouse/clickhouse-java) repository.
  :::

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/4e317723667623f7f3012ebaae217f087cee843cd7e9dca6dffedc1f4ab601d0/images/integrations/sql-clients/datagrip-7.png" alt="DataGrip connection details form with ClickHouse settings"/>

## Learn more [#learn-more]

Find more information about DataGrip visit the DataGrip documentation.
