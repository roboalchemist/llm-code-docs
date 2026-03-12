# Source: https://docs.snowflake.com/en/sql-reference/info-schema/cortex_search_service_scoring_profiles.md

# CORTEX_SEARCH_SERVICE_SCORING_PROFILES view

This Information Schema view displays a row for each Cortex Search Service named scoring profile in the current or specified database.

For more information about named scoring profiles, see [Named scoring profiles](../../user-guide/snowflake-cortex/cortex-search/cortex-search-customize-scoring.md).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| SERVICE_CATALOG | VARCHAR | The database in which the service is defined. |
| SERVICE_SCHEMA | VARCHAR | The schema in which the service is defined. |
| SERVICE_NAME | VARCHAR | The name of the search service to which the profile belongs. |
| PROFILE_NAME | VARCHAR | The name of the scoring profile. |
| SCORING_PROFILE | VARCHAR | The scoring profile configuration as a JSON-format string. |

## Example

The following statement lists the named scoring profiles that are in the current database.

```sqlexample
SELECT * FROM INFORMATION_SCHEMA.CORTEX_SEARCH_SERVICE_SCORING_PROFILES;
```
