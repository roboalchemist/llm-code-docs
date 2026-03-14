# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-04-30-programmatic-access-tokens.md

# Apr 30, 2025: Programmatic access tokens

You can now generate and use programmatic access tokens to authenticate to the following Snowflake endpoints:

* [Snowflake REST APIs](../../../developer-guide/snowflake-rest-api/snowflake-rest-api.md).
* [The Snowflake SQL API](../../../developer-guide/sql-api/index.md).
* [The Snowflake Catalog SDK](../../../user-guide/tables-iceberg-catalog.md).

> **Note:**
>
> Using programmatic access tokens to authenticate to
> [Snowpark Container Services](../../../developer-guide/snowpark-container-services/working-with-services.md) endpoints is not yet
> supported.

You can also use a programmatic access token as a replacement for a password in:

* [Snowflake drivers](../../../developer-guide/drivers.md).
* [Third-party applications that connect to Snowflake](../../../user-guide/ecosystem.md) (such as Tableau and PowerBI).
* Snowflake APIs and libraries (such as the [Snowpark API](../../../developer-guide/snowpark/index.md) and the
  [Snowflake Python API](../../../developer-guide/snowflake-python-api/snowflake-python-overview.md).
* Snowflake command-line clients (such as the [Snowflake CLI](../../../developer-guide/snowflake-cli/index.md) and
  [SnowSQL](../../../user-guide/snowsql.md).

You can generate programmatic access tokens for human users (users with TYPE=PERSON) as well as for service users (users with
TYPE=SERVICE).

For more information, see [Using programmatic access tokens for authentication](../../../user-guide/programmatic-access-tokens.md).
