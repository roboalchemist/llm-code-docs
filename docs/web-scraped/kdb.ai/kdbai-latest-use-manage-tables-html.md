# Source: https://code.kx.com/kdbai/latest/use/manage-tables.html

Title: Manage KDB.AI Tables - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/use/manage-tables.html

Markdown Content:
How to Create and Manage Tables in KDB.AI
-----------------------------------------

_This page provides details on creating and managing tables within the KDB.AI vector database._

In KDB.AI, the table is the fundamental structure for storing and organizing your data. Each table not only holds the actual vector data, but also includes crucial metadata that defines how the data is indexed and organized.

To create a table object, use the `create_table` function, which allows you to specify various attributes and settings for your table. Alternatively, you can retrieve an existing table using `table` function, which provides access to previously defined tables within your session.

Create tables
-------------

### Define schema

Before creating a new table, you need to design its schema. This schema is a list of dictionaries, each dictionary refers to one column. For every column, you must specify the `name`and its `type`. Refer to the [list of supported data types](https://code.kx.com/kdbai/latest/reference/supported-types.html).

Naming reminder

When creating a table, column, or database in KDB.AI, make sure to follow our [Naming Convention and Reserved Words](https://code.kx.com/kdbai/latest/reference/naming-convention-reserved-words.html) guidelines. A quick check now can save hours of troubleshooting later.

The vector embeddings column must be type of `float32s`.

| **Parameter** | **Description** |
| --- | --- |
| `metric` | The choice metric depends on the specific context and nature of your data. See available metrics in KDB.AI [here](https://code.kx.com/kdbai/latest/reference/metrics.html). |
| `type` | Like metrics, the one you choose depends on your data and your overall performance requirements. See available indexes in KDB.AI [here](https://code.kx.com/kdbai/latest/use/supported-indexes.html). |

Depending on the choice of an index, there are additional parameters specific to that index that require configuration. For more information about these parameters and their default values, please refer to the dedicated [index](https://code.kx.com/kdbai/latest/use/supported-indexes.html) section.

Python JSON q

```
schema = [
     {'name': 'id', 'type': 'int16'},
     {'name': 'tag', 'type': 'bool'},
     {'name': 'author', 'type': 'str'},
     {'name': 'length', 'type': 'int32'},
     {'name': 'content', 'type': 'bytes'},
     {'name': 'createdTime', 'type': 'datetime64[ns]'},
     {'name': 'embeddings', 'type': 'float32s'}
]
```

```
{
    "table": "documents",
    "schema": [
        {"name": "id", "type": "short"},
        {"name": "tag", "type": "boolean"},
        {"name": "author", "type": "char"},
        {"name": "length", "type": "int"},
        {"name": "content", "type": "char"},
        {"name": "createdTime", "type": "timestamp"},
        {"name": "embeddings", "type": "reals"}
    ]
}
```

```
schema: flip `name`type!(`id`tag`author`length`content`createdTime`embeddings;`h`b`s`i`C`p`E)
```

This helps you create a Sparse Index or conduct a [Hybrid Search](https://code.kx.com/kdbai/latest/use/hybrid-search.html), a [Transformed Temporal Similarity Search](https://code.kx.com/kdbai/latest/use/non-transformed-tss.html), and a [Non-Transformed Temporal Similarity Search](https://code.kx.com/kdbai/latest/use/transformed-tss.html).

### Define indexes

To be able to run similarity search you need to create at least one index. A table can have multiple indexes even on the same column, but index names must be unique per table. Read more details about [supported indexes](https://code.kx.com/kdbai/latest/use/supported-indexes.html).

Python JSON q

```
indexes = [
    {'name': 'flat_index', 'column': 'embeddings', 'type': 'flat', 'params': {'dims': 25}},
    {'name': 'hnsw_fast', 'column': 'embeddings', 'type': 'hnsw', 'params': {'dims': 25, 'M': 8, 'efConstruction': 8}}
]
```

```
{
    "indexes": [
        {"name": "flat_index", "column": "embeddings", "type": "flat", "params": {"dims": 25}},
        {"name": "hnsw_fast", "column": "embeddings", "type": "hnsw", "params": {"dims": 25, "M": 8, "efConstruction": 8}}
    ]
}
```

```
flatIndex: `name`column`type`params!(`flat_index;`embeddings;`flat;enlist[`dims]!enlist 25);
hnswFast: `name`column`type`params!(`hnsw_fast;`embeddings;`hnsw;`dims`M`efConstruction!(25;8;8));
indexes: (flatIndex;hnswFast);
```

### Create table

You can create multiple tables to suit your data organization needs.

When creating a new table, the associated index is also automatically generated based on the configuration provided in the `indexes` parameter. To set up a table after defining its schema, provide the desired table name along with the schema details specified above. For example, to create a table titled `documents`, run this command:

Python REST q

```
session = kdbai.Session("http://localhost:8082")
db=session.database('default')
documents = db.create_table("documents", schema=schema, indexes=indexes)
```

```
curl -X POST -H "Content-Type: application/json" -d @table.json localhost:8081/api/v2/databases/default/tables
```

```
gw:hopen 8082;
gw(`createTable;`database`table`schema`indexes!(`default;`documents;schema;indexes))
```

Advanced table creation
-----------------------

### Partition column

You can partition a table by providing a valid column name in `partition_column` parameter.

### Embedding configurations

To reduce the embeddings' size, TSC configurations can be provided with `embedding_configurations` dictionary, where keys are the column names.

Python JSON q

```
embedding_configurations = {'embeddings': {'dims': 4, 'type': 'tsc', 'on_insert_error': 'reject_all'}}
```

```
{
   "embeddingConfigurations": {
        "embeddings": {
            "dims": 4,
            "type": "tsc",
            "on_insert_error": "reject_all"
        }
   } 
}
```

```
embeddingConfigurations: enlist[`embeddings]!enlist `dims`type`on_insert_error!(4;`tsc;`reject_all)
```

### Reference tables

Since KDB.AI 1.4.0 you can use existing kdb+ tables by providing path on disk.

Python JSON q

```
external_data_references = [{'path': b'/tmp/kx/remote', 'provider': 'kx'}]
```

```
{
   "externalDataReferences": [
        {
            "path": "/tmp/kx/remote",
            "provider": "kx"
        }
   ]
}
```

```
externalDataReferences: enlist `path`provider!("/tmp/kx/remote";`kx)
```

### Retrieve table configuration

To fetch the table configuration, including details about the table structure and indexes, use the following commands:

Python REST q

```
documents.schema
documents.indexes
```

```
curl -s http://localhost:8081/api/v2/databases/default/tables/documents
```

```
// gw is a handler to the gateway
gw(`getTable;`database`table!(`default;`documents`))
```

This will provide you with the schema and index parameters that were explicitly chosen during the table creation.

### Retrieve information on available tables

After you have connected with your KDB.AI session and fetched a database, you can retrieve information about the existing tables.

In python client `tables` property is cached on the database instance. If the tables are used by multiple users/sessions `data.refresh()` method updates the database's state

Python REST q

```
database = session.database('default')
database.tables
```

```
curl -s localhost:8081/api/v2/databases/default/tables
```

```
// gw is a handler to the gateway
gw(`listTables;enlist[`database]!enlist `default)
```

### Delete table

Deleting a table deletes all the data together with the associated index. In the command line, run:

Python REST q

```
documents.drop()
```

```
curl -s -X DELETE localhost:8081/api/v2/databases/default/tables/documents
```

```
// gw is a handler to the gateway
gw(`deleteTable;`database`table!(`default;`documents`))
```

Do not perform this action on a production database or in any environment where data deletion is not intended, because this action cannot be reverted.

Next steps
----------

Once you have some tables created and your schema ready, you can do the following:

*   Watch our videos to learn more about [Managing tables in vector databases](https://kdb.ai/learning-hub/video-lessons/managing-tables-in-vector-databases/).
*   [Ingest some data](https://code.kx.com/kdbai/latest/use/ingestion.html).
*   Try creating tables in any of our [sample projects](https://kdb.ai/learning-hub/samples/).
*   Perform a [Hybrid search](https://code.kx.com/kdbai/latest/use/hybrid-search.html) or a [Transformed Temporal Similarity Search](https://code.kx.com/kdbai/latest/reference/transformed-tss.html).
