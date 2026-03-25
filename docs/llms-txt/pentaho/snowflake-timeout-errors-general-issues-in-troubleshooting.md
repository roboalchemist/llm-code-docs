# Source: https://docs.pentaho.com/pdia-data-integration/data-integration-issues/snowflake-timeout-errors-general-issues-in-troubleshooting.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-issues/snowflake-timeout-errors-general-issues-in-troubleshooting.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-issues/snowflake-timeout-errors-general-issues-in-troubleshooting.md

# Snowflake timeout errors

When you are pooling the Pentaho database connection, you may see errors. Snowflake JDBC connections use a default timeout of four hours which contributes to these errors because the same connection can be reused for more than four hours. See the [Snowflake documentation](https://docs.snowflake.net/manuals/index.html) for further details.

To resolve this issue, do one of the following actions:
