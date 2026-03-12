# Source: https://clickhouse.ferndocs.com/integrations/qstudio.md

---
slug: /integrations/qstudio
sidebar_label: QStudio
description: QStudio is a free SQL tool.
title: Connect QStudio to ClickHouse
doc_type: guide
keywords:

- qstudio
- sql client
- database tool
- query tool
- ide

---

import {CommunityMaintainedBadge} from '../../../../../components/Badges/CommunityMaintainedBadge'

<CommunityMaintainedBadge/>

QStudio is a free SQL GUI, it allows running SQL scripts, easy browsing of tables, charting and exporting of results. It works on every operating system, with every database.

QStudio connects to ClickHouse using JDBC.

## 1. Gather your ClickHouse details [#1-gather-your-clickhouse-details]

QStudio uses JDBC over HTTP(S) to connect to ClickHouse; you need:

- endpoint
- port number
- username
- password

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

## 2. Download QStudio [#2-download-qstudio]

QStudio is available at https://www.timestored.com/qstudio/download/

## 3. Add a database [#3-add-a-database]

- When you first open QStudio click on the menu options **Server->Add Server** or on the add server button on the toolbar.
- Then set the details:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c542cac288757f6aad16cdb67139792e3632c0d76724cb17315d4bc9b422b81b/images/integrations/sql-clients/qstudio-add-connection.png" alt="QStudio database connection configuration screen showing ClickHouse connection settings"/>

1. Server Type: Clickhouse.com
2. Note for Host you MUST include https://
    Host: https://abc.def.clickhouse.cloud
    Port: 8443
3. Username: default
    Password: `XXXXXXXXXXX`
4. Click Add

If QStudio detects that you do not have the ClickHouse JDBC driver installed, it will offer to download them for you:

## 4. Query ClickHouse [#4-query-clickhouse]

- Open a query editor and run a query. You can run queries by
- Ctrl + e - Runs highlighted text
- Ctrl + Enter - Runs the current line

- An example query:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/375a54daac19a3c9b39c6610b82c574126ad78c21bd8f8f9d29bfd9b3e1de8a7/images/integrations/sql-clients/qstudio-running-query.png" alt="QStudio interface showing sample SQL query execution against ClickHouse database"/>

## Next steps [#next-steps]

See [QStudio](https://www.timestored.com/qstudio) to learn about the capabilities of QStudio, and the [ClickHouse documentation](https://clickhouse.com/docs) to learn about the capabilities of ClickHouse.
