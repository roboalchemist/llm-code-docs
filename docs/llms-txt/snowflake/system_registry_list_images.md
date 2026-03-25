# Source: https://docs.snowflake.com/en/sql-reference/functions/system_registry_list_images.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$REGISTRY_LIST_IMAGES — *Deprecated*

Lists images in an [image repository](../../developer-guide/snowpark-container-services/working-with-registry-repository.md).

See also:
:   [Working with an Image Registry and Repository](../../developer-guide/snowpark-container-services/working-with-registry-repository.md)

## Syntax

```sqlsyntax
SYSTEM$REGISTRY_LIST_IMAGES( '/<dbName>/<schemaName>/<repositoryName>' )
```

## Arguments

**Required:**

`dbName`
:   Name of the database in which the repository is created.

`schemaName`
:   Name of the database in which the repository is created.

`repositoryName`
:   Name of the image repository.

## Returns

Returns a JSON object listing all the images.

## Usage notes

* You need the read permission on the repository to get a list of images.

## Examples

This function retrieves a list of images from the `/tutorial_db/data_schema/tutorial_repository` repository.

```sqlexample
SELECT SYSTEM$REGISTRY_LIST_IMAGES('/tutorial_db/data_schema/tutorial_repository');
```

Sample output showing a list of two images in the repository:

```output
+-----------------------------------------------------------------------------+
| SYSTEM$REGISTRY_LIST_IMAGES('/TUTORIAL_DB/DATA_SCHEMA/TUTORIAL_REPOSITORY') |
|-----------------------------------------------------------------------------|
| {"images":["my_echo_service_image","my_job_image"]}                         |
+-----------------------------------------------------------------------------+
```
