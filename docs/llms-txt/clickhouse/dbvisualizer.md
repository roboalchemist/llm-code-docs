# Source: https://clickhouse.ferndocs.com/integrations/dbvisualizer.md

---
sidebar_label: DbVisualizer
slug: /integrations/dbvisualizer
description: DbVisualizer is a database tool with extended support for ClickHouse.
title: Connecting DbVisualizer to ClickHouse
keywords:

- DbVisualizer
- database visualization
- SQL client
- JDBC driver
- database tool
doc_type: guide
integration:
- support_level: partner
- category: sql_client

---

import {CommunityMaintainedBadge} from '../../../../../components/Badges/CommunityMaintainedBadge'

<CommunityMaintainedBadge/>

## Start or download DbVisualizer [#start-or-download-dbvisualizer]

DbVisualizer is available at https://www.dbvis.com/download/

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

## 2. Built-in JDBC driver management [#2-built-in-jdbc-driver-management]

DbVisualizer has the most up-to-date JDBC drivers for ClickHouse included. It has full JDBC driver management built right in that points to the latest releases as well as historical versions for the drivers.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/d6603b5fbac30c972ae9b7e4aedb747250518bef1081dca322285ea2c0487c54/images/integrations/sql-clients/dbvisualizer-driver-manager.png" alt="DbVisualizer driver manager interface showing ClickHouse JDBC driver configuration"/>

## 3. Connect to ClickHouse [#3-connect-to-clickhouse]

To connect a database with DbVisualizer, you must first create and setup a Database Connection.

1. Create a new connection from **Database->Create Database Connection** and select a driver for your database from the popup menu.

2. An **Object View** tab for the new connection is opened.

3. Enter a name for the connection in the **Name** field, and optionally enter a description of the connection in the **Notes** field.

4. Leave the **Database Type** as **Auto Detect**.

5. If the selected driver in **Driver Type** is marked with a green check mark then it is ready to use. If it is not marked with a green check mark, you may have to configure the driver in the **Driver Manager**.

6. Enter information about the database server in the remaining fields.

7. Verify that a network connection can be established to the specified address and port by clicking the **Ping Server** button.

8. If the result from Ping Server shows that the server can be reached, click **Connect** to connect to the database server.

## Learn more [#learn-more]

See [Fixing Connection Issues](https://www.dbvis.com/docs/ug/troubleshooting/fixing-connection-issues/) for some tips if you have problems connecting to the database.

Find more information about DbVisualizer visit the [DbVisualizer documentation](https://www.dbvis.com/docs/ug/).
