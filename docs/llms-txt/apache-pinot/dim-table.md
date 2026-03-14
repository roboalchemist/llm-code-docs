# Source: https://docs.pinot.apache.org/release-0.9.0/basics/data-import/batch-ingestion/dim-table.md

# Source: https://docs.pinot.apache.org/release-0.10.0/basics/data-import/batch-ingestion/dim-table.md

# Source: https://docs.pinot.apache.org/release-0.11.0/basics/data-import/batch-ingestion/dim-table.md

# Source: https://docs.pinot.apache.org/release-0.12.0/basics/data-import/batch-ingestion/dim-table.md

# Source: https://docs.pinot.apache.org/release-0.12.1/basics/data-import/batch-ingestion/dim-table.md

# Source: https://docs.pinot.apache.org/release-1.0.0/basics/data-import/batch-ingestion/dim-table.md

# Source: https://docs.pinot.apache.org/release-1.1.0/basics/data-import/batch-ingestion/dim-table.md

# Source: https://docs.pinot.apache.org/release-1.2.0/basics/data-import/batch-ingestion/dim-table.md

# Source: https://docs.pinot.apache.org/release-1.3.0/basics/data-import/batch-ingestion/dim-table.md

# Source: https://docs.pinot.apache.org/release-1.4.0/manage-data/data-import/batch-ingestion/dim-table.md

# Source: https://docs.pinot.apache.org/manage-data/data-import/batch-ingestion/dim-table.md

# Dimension table

Dimension tables are a special kind of offline tables from which data can be looked up via the [lookup UDF](https://docs.pinot.apache.org/users/user-guide-query/query-syntax/lookup-udf-join), providing join-like functionality.

Dimension tables are replicated on all the hosts for a given tenant to allow faster lookups. When a table is marked as a dimension table, it will be replicated on all the hosts, which means that these tables must be small in size.

A dimension table cannot be part of a [hybrid table](https://docs.pinot.apache.org/basics/concepts/components/table#hybrid-table).

Configure dimension tables using following properties in the table configuration:

* `isDimTable`: Set to `true.`
* `ingestionConfig.batchIngestionConfig.segmentIngestionType`: Set to `REFRESH`.
* `dimensionTableConfig.disablePreload`: By default, dimension tables are preloaded to allow for fast lookups. Set to `true` to trade off speed for memory by storing only the segment reference and docID. Otherwise, the whole row is stored in the Dimension table hash map.
* `controller.dimTable.maxSize`: Determines the maximum size quota for a dimension table in a cluster. Table creation will fail if the storage quota exceeds this maximum size.
* `dimensionFieldSpecs`: To look up dimension values, dimension tables need a primary key. For details, see [`dimensionFieldSpecs`](https://docs.pinot.apache.org/configuration-reference/schema#dimensionfieldspec).

### Example dimension table configuration

```json
{
  "OFFLINE": {
    "tableName": "dimBaseballTeams_OFFLINE",
    "tableType": "OFFLINE",
    "segmentsConfig": {
    },
    "ingestionConfig": {
      "batchIngestionConfig": {
        "segmentIngestionType": "REFRESH"
      }
    }
    "quota": {
      "storage": "200M"
    },
    "isDimTable": true,
    "dimensionTableConfig": {
      "disablePreload": true
    }
  }
}
```

### Example table schema configuration

```json
{
  "dimensionFieldSpecs": [
    {
      "dataType": "STRING",
      "name": "teamID"
    },
    {
      "dataType": "STRING",
      "name": "teamName"
    }
  ],
  "schemaName": "dimBaseballTeams",
  "primaryKeyColumns": ["teamID"]
}
```
