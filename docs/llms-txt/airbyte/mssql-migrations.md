# Source: https://docs.airbyte.com/integrations/sources/mssql-migrations.md

# Source: https://docs.airbyte.com/integrations/destinations/mssql-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/destination-mssql/latest/icon.svg)

# MS SQL Server Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [2.2.15](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-mssql)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-mssql)(last updated a month ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `d4353156-9217-4cad-8dd7-c108fd4f74cf`

## Upgrading to 2.0.0[​](#upgrading-to-200 "Direct link to Upgrading to 2.0.0")

This version removes the Airbyte "raw" tables introduced in version 1.0.0. As such, any attempt to upgrade an existing connection will fail unless a "truncate refresh" is first executed. It is recommended that you should create a new connection using this upgraded destination and delete the existing connection and generated "raw" tables in the destination after performing a successful sync via the new connection.

In addition to removing the Airbyte "raw" tables, this version also introduces a new insert mode: bulk insert via Azure Blob Storage. This mode is only supported with Microsoft SQL Server 2017 (14.x) and newer and in scenarios where the database instance has access to Azure Cloud. This is a net-new configuration option and may be opted in to at any point after upgrading to the new connection version.
