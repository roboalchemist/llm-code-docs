# Source: https://docs.snowflake.com/en/user-guide/tables-iceberg-configure-catalog-integration-rest.md

# Configure a catalog integration for Apache Iceberg™ REST catalogs

An Apache Iceberg™ REST [catalog integration](tables-iceberg.md) lets Snowflake access
[Apache Iceberg™ tables](tables-iceberg.md) managed in a remote catalog that complies with the
open source [Apache Iceberg REST OpenAPI specification](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml).

Snowflake supports the following additional features when you use an Iceberg REST catalog integration:

* [Catalog-linked databases and automatic table discovery](tables-iceberg-catalog-linked-database.md)
* [Write support for externally managed Iceberg tables](tables-iceberg-externally-managed-writes.md)

## Authentication methods

Snowflake supports the following authentication methods for Iceberg REST catalogs:

* OAuth
* Bearer token or personal access token (PAT)
* Signature Version 4 (SigV4)

Supported authentication methods vary by catalog source.

### Credential rotation

To rotate the credentials for a catalog integration, you can use the [ALTER CATALOG INTEGRATION](../sql-reference/sql/alter-catalog-integration.md)
command to update the credentials that Snowflake uses to authenticate with your remote catalog.

For example:

```sqlexample
ALTER CATALOG INTEGRATION my_cat_int SET
  REST_AUTHENTICATION (
    OAUTH_CLIENT_SECRET = 'myNewSecret'
  );
```

## Connection options

This section describes the connection options for Iceberg REST catalogs.

### Vended credentials

In addition to [External volumes](tables-iceberg-configure-external-volume.md),
Snowflake supports the following connection options for Iceberg REST catalogs:

* [Vended credentials](tables-iceberg-configure-catalog-integration-vended-credentials.md)

Supported connection options vary by catalog source.

### Private connectivity

Snowflake supports connecting to Iceberg REST catalogs through [private connectivity](tables-iceberg-configure-catalog-integration-rest-private.md).

However, when you connect to the catalog through private connectivity, you must use an external volume to connect to the catalog data.

Supported connection options vary by catalog source.

## Catalog sources

Snowflake supports any external catalog server that complies with the Iceberg REST specification.

The following topics provide examples for commonly used REST catalogs:

* [Snowflake Open Catalog](tables-iceberg-configure-catalog-integration-open-catalog.md). These instructions also apply to
  Apache Polaris™.
* [AWS Glue](tables-iceberg-configure-catalog-integration-rest-glue.md)
* [Amazon API Gateway](tables-iceberg-configure-catalog-integration-rest-api-gateway.md)
* [Tabular](tables-iceberg-configure-catalog-integration-rest-tabular.md)
* [Unity Catalog](tables-iceberg-configure-catalog-integration-rest-unity.md)
* [OneLake](tables-iceberg-configure-catalog-integration-rest-onelake.md)

## Browsing a remote catalog

After you create a catalog integration for Iceberg REST, you can use the following
Snowflake system functions to browse namespaces and tables in the catalog:

* [SYSTEM$LIST_ICEBERG_TABLES_FROM_CATALOG](../sql-reference/functions/system_list_iceberg_tables_from_catalog.md)
* [SYSTEM$LIST_NAMESPACES_FROM_CATALOG](../sql-reference/functions/system_list_namespaces_from_catalog.md)

## Migrate a table to a Iceberg REST catalog integration

After you create a catalog integration for Iceberg REST, if needed, you can
replace the catalog integration associated with an externally managed Iceberg table in a standard Snowflake database with the catalog
integration you created. For instructions, see [SYSTEM$SET_CATALOG_INTEGRATION](../sql-reference/functions/system_set_catalog_integration.md).
