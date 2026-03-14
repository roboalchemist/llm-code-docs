# Source: https://docs.snowflake.com/en/user-guide/tables-iceberg-configure-catalog-integration-object-storage.md

# Configure a catalog integration for files in object storage

Create a catalog integration for Apache Iceberg™ table files or Delta table files in object storage.

After you create a catalog integration, you can [create an Iceberg table](tables-iceberg-create.md).

## Iceberg files

Create a catalog integration for Iceberg metadata that’s in an external cloud storage location
by setting `OBJECT_STORE` as the `CATALOG_SOURCE` value and `ICEBERG` as the `TABLE_FORMAT`.

```sqlexample
CREATE OR REPLACE CATALOG INTEGRATION icebergCatalogInt
  CATALOG_SOURCE = OBJECT_STORE
  TABLE_FORMAT = ICEBERG
  ENABLED = TRUE;
```

## Delta table files

Create a catalog integration for Iceberg tables based on
Delta table files by setting `OBJECT_STORE` as the `CATALOG_SOURCE` value and `DELTA` as the `TABLE_FORMAT`.

* `CATALOG_SOURCE = OBJECT_STORE`
* `TABLE_FORMAT = DELTA`

```sqlexample
CREATE OR REPLACE CATALOG INTEGRATION delta_catalog_integration
  CATALOG_SOURCE = OBJECT_STORE
  TABLE_FORMAT = DELTA
  ENABLED = TRUE;
```

> **Note:**
>
> Snowflake doesn’t support creating Iceberg tables from Delta table definitions in the AWS Glue Data Catalog.
