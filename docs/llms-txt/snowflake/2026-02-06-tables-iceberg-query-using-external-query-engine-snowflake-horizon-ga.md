# Source: https://docs.snowflake.com/en/release-notes/2026/other/2026-02-06-tables-iceberg-query-using-external-query-engine-snowflake-horizon-ga.md

# Feb 06, 2026: External query engine support for Apache Iceberg™ tables with Snowflake Horizon Catalog (*General availability*)

Support for querying Snowflake-managed Apache Iceberg™ tables by using any external query engine that supports the open Iceberg REST protocol,
such as Apache Spark™, is now generally available. To ensure this interoperability with external engines,
[Apache Polaris™ (incubating)](https://github.com/apache/polaris) is integrated into Horizon Catalog. You can query these tables in a
Snowflake account by using a single Horizon Catalog endpoint and you can use your existing users, roles, policies, and authentication
in Snowflake.

For more information, see [Query Apache Iceberg™ tables with an external engine through Snowflake Horizon Catalog](../../../user-guide/tables-iceberg-query-using-external-query-engine-snowflake-horizon.md).
