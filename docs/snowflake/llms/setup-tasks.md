# Source: https://docs.snowflake.com/en/connectors/kafkahp/setup-tasks.md

# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/connectors/sap-sql/setup-tasks.md

# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/connectors/oracle/setup-tasks.md

# Set up tasks for the Openflow Connector for Oracle

> **Note:**
>
> This connector is subject to the [Snowflake Connector Terms](https://www.snowflake.com/legal/snowflake-connector-terms/).

> **Note:**
>
> The Openflow Connector for Oracle is also subject to additional terms of service beyond the standard
> connector terms of service. For more information, see the
> [Openflow Connector for Oracle Addendum](https://www.snowflake.com/en/legal/optional-offerings/offering-specific-terms/openflow-oracle-terms/).

This topic describes the overall tasks required to set up, configure, and run the Openflow Connector for Oracle.

## Prerequisites

Before you set up the Openflow Connector for Oracle, verify that the following prerequisites are met:

1. Ensure that you have reviewed [About Openflow Connector for Oracle](about.md).
2. Ensure that you have set up an Openflow deployment:

   * [Set up Openflow - BYOC](../../setup-openflow-byoc.md)
   * [Set up Openflow - Snowflake Deployment](../../setup-openflow-spcs.md)
3. Ensure that you add only one connector instance per runtime.

## Tasks

Perform the following tasks to set up, configure, and run the Openflow Connector for Oracle.

| Order | Task | Description | Persona |
| --- | --- | --- | --- |
| 1 | Review Prerequisites | Review and confirm all required prerequisites. | **Snowflake account administrator** |
| 2 | [Enable the connector](manage-commercial-terms.md) | Accept the Oracle XStream terms to make the connector visible in the list of available connectors. | **Organization administrator (ORGADMIN)** |
| 3 | [Configure the Oracle database](setup-oracledb.md) | Configure the Oracle database for Openflow Connector for Oracle including replication settings and credentials. | **Oracle database administrator** |
| 4 | [Set up Snowflake](setup-snowflake.md) | Create the destination database, service user, role, warehouse, and key pair authentication for the Openflow Connector for Oracle. | **Snowflake account administrator** |
| 5 | [Configure the connector](setup-connector.md) | Install, configure, and run the Openflow Connector for Oracle connector. | **Snowflake account administrator** |
| 6 | [Set up licensing](manage-commercial-terms.md) | Configure your licensing model after the connector detects your source database inventory. | **Organization administrator (ORGADMIN)** |

## Next steps

* [Monitor the flow](../../monitor.md).
* [Maintenance](maintenance.md) for reinstalling the connector or changing the XStream position.
