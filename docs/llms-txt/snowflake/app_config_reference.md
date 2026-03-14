# Source: https://docs.snowflake.com/en/developer-guide/native-apps/connector-sdk/reference/app_config_reference.md

# App config SQL reference

File: `configuration/app_config.sql`

## Database objects and procedures

### STATE.APP_CONFIG

An internal table to store all the connector configurations. This table follows the following structure:

| KEY | VALUE | UPDATED_AT |
| --- | --- | --- |
| connector_configuration | {warehouse: “wh”, destination_db: “db”, destination_schema: “s”} | TIMESTAMP_NTZ_1 |
| custom_configuration | {journal_table: “j_table_name”} | TIMESTAMP_NTZ_2 |
| connection_configuration | {secret_name: “secret_db.schema.the_secret”} | TIMESTAMP_NTZ_3 |
| … | {…} | … |

### PUBLIC.CONNECTOR_CONFIGURATION

A view that retrieves and maps the data from the `APP_CONFIG` internal table
The mapping is as follows:

1. KEY (col) → CONFIG_GROUP (col);
2. JSON keys from VALUE column (JSON key) → CONFIG_KEY (col)
3. JSON values from VALUE column (JSON value) → VALUE (col)
4. UPDATED_AT (col) → UPDATED_AT (col)

Example CONNECTOR_CONFIGURATION view created on example APP_CONFIG:

| CONFIG_GROUP | CONFIG_KEY | VALUE | UPDATED_AT |
| --- | --- | --- | --- |
| connector_configuration | warehouse | wh | <timestamp_ntz> |
| connector_configuration | destination_db | db | <timestamp_ntz> |
| custom_configuration | journal_table | j_table_name | <timestamp_ntz> |
| connection_configuration | secret_name | secret_db.schema.the_secret | <timestamp_ntz> |
| … | … | … | … |

## Related Java objects

The following Java objects are tightly connected with the `APP_STATE` table:

* `ConnectorConfigurationService`
* `ConfigurationRepository`
* `ConfigurationMap`
* `KeyValueTable`
