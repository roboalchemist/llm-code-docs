# Source: https://docs.snowflake.com/en/release-notes/2026/other/2026-01-27-iceberg-enforce-access-policies-on-tables-queried-from-apache-spark.md

# Jan 27, 2026: Enforce data protection policies when querying Apache Iceberg™ tables from Apache Spark™

You can now enforce the following policies on Apache Iceberg tables that you query from Apache Spark™ through Snowflake
Horizon Catalog:

* [Masking policies](../../../user-guide/security-column-intro.md)
* [Tag-based masking policies](../../../user-guide/tag-based-masking-policies.md)
* [Row access policies](../../../user-guide/security-row-intro.md)

To enforce these policies, you first define the policy in Snowflake as you normally would, and then you configure Spark to enforce the
policy. This configuration uses version 3.1.6 of the Snowflake Connector for Spark to connect to Snowflake and evaluate policies.

For more information, see [Enforce data protection policies when querying Apache Iceberg™ tables from Apache Spark™](../../../user-guide/tables-iceberg-query-using-external-query-engine-snowflake-horizon-enforce-access-policies.md).
