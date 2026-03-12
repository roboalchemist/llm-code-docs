# Source: https://code.kx.com/kdbai/latest/reference/qAPI.html

Title: KDB.AI q API - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/reference/qAPI.html

Markdown Content:
_This page contains the references for KDB.AI's q API. For example usage, see the [Quickstart Guide](https://code.kx.com/kdbai/latest/gettingStarted/quickstart.html)._

Introduction
------------

KDB.AI q API allows KDB.AI Server users to achieve the following:

*   Load and use existing kdb+ datasets in KDB.AI.
*   Apply KDB.AI functionalities to external kdb+ datasets. 

KDB.AI kdb+/q

KDB.AI is a high-performance vector database designed to manage real-time, unstructured data and power AI applications with advanced search, recommendation, and personalization features.

*   [Quickstart Guide](https://code.kx.com/kdbai/latest/gettingStarted/quickstart.html)

Kdb+ is a high-performance time-series database widely used in industries like finance for managing large datasets, particularly time-sensitive data. It is built to handle vast amounts of structured data efficiently. The q programming language is an integral part of kdb+ as its query language, designed for working with complex, high-speed analytics on large datasets. Q provides a concise syntax and is optimized for the operations typical in kdb+, such as querying and manipulating time-series data.

*   [Get started with q and kdb+](https://code.kx.com/q/learn/)
*   [Install kdb+](https://code.kx.com/q/learn/install/)

Prerequisites
-------------

Before you start, make sure you have the following:

*   Access to [KDB.AI Server](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html).
*   Knowledge of writing q code using an environment of choice (command line, IDE, notebooks).

Version
-------

### Get version info

`getVersion`

Retrieve version info from server and compatible client min/max version.

Example:

```
gw(`getVersion;`)
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success. version info is returned. | `serverVersion`clientMinVersion`clientMaxVersion!("1.4.0";"1.4.0";"latest") | N/A |
| Error: KDBAI is not available. | Cannot write to handle ... | Check your connection and if your server is running. |

Database
--------

Create, delete, and retrieve databases.

In KDB.AI, a [database](https://code.kx.com/kdbai/latest/reference/database.html) is a collection of tables which stores related data.

Key principles for database management

To simplify database design/management and prevent naming conflicts, follow the principles below:

*   **Unique database names**: Each database must have a unique name and can contain multiple tables.
*   **Unique table names within a database**: Tables within a database must have unique names, but different databases can contain tables with the same name. This is similar to the concept of namespaces.
*   **Cascade deletion**: When deleting a database, all child entities (tables) will also be deleted.
*   **Default database**: You don't need to create a database to create tables. If you create a table without specifying a database, it will be placed in a default, undeletable database.

### Create database

`createDatabase`

Create a database.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | Name of the database to create. | Yes |

Database name rules

*   Max length is 128 characters
*   Must contain only alphanumeric characters and underscore
*   Must start with an alpha character

Example:

```
`gw set hopen 8082;
gw(`createDatabase;enlist[`database]!enlist `myDatabaseName)
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Database is created and returned | `success`result`error!(1b;(`name!`tableName);()) | N/A |
| Fail: Database name is not unique | `success`result`error!0b;();"database {name} already exists" | A database with the given name already exists. Create a database with another name. |
| Fail: Database name is not a valid name | `success`result`error!0b;();"database name is invalid" | Provide a valid symbol for the database name. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

### Get database

`getDatabase`

Retrieve database with a given name.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | Name of the database to be retrieved | Yes |

Example:

```
`gw set hopen 8082;
gw(`getDatabase;enlist[`database]!enlist `myDatabaseName)
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Database with given name is found | `success`result`error!1b;`database`tables!{databasename};{list of table metadata (see at get table)};() | N/A |
| Fail: Database with given name is not found | `success`result`error!0b;();"database {name} does not exist" | Check the name of the database you are searching for as it does not seem to exist. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

### List databases

`listDatabases`

Retrieve list of databases in ascending order.

Example:

```
`gw set hopen 8082;
gw(`listDatabases;`)
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Returns list of database names and default db included | `success`result`error!1b;[get database names];() | N/A |
| Error: Databases cannot be listed because KDBAI is not available | Cannot write to handle... | Check your connection and if your server is running. |

### Delete database

`deleteDatabase`

Delete database with a given name and all associated tables.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | Name of the database to be deleted. | Yes |

Example:

```
`gw set hopen 8082;
gw(`deleteDatabase;enlist[`database]!enlist `myDatabaseName)
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Database with given name has been deleted | `success`result`error!1b;();() | N/A |
| Fail: Database name is not valid | `success`result`error!0b;();"database {name} does not exist" | Check the name of the database you are searching for as it does not seem to exist. |
| Fail: Database with given name is not found | `success`result`error!0b;();"database {name} does not exist" | Check the name of the database you are searching for as it does not seem to exist. |
| Fail: Default database cannot be deleted, (see database API section intro) | `success`result`error!0b;();"Default database cannot be deleted" | Remove the tables from the database individually as required. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

Table
-----

Create, delete, update, and retrieve tables.

### Create table

`createTable`

Create a table.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | Name of the database. | Yes |
| table | symbol | Name of the table to create. | Yes |
| [externalDataReferences](https://code.kx.com/kdbai/latest/reference/qAPI.html#externaldatareferences) | string list | Should contain the keys: - `path` (path to the existing kdb+ table mounted in our Docker container) - `provider` (set to `kx`) WARNING: the name of the table should match the name of the target table in the existing kdb+ database. | No |
| [schema](https://code.kx.com/kdbai/latest/reference/qAPI.html#schema) | list of dictionary | Schema details for the table. | Yes - if externalDataReferences is not specified |
| [indexes](https://code.kx.com/kdbai/latest/reference/qAPI.html#indexes) | list of dictionary | List of index definitions | No |
| partitionColumn | symbol | Column name to partition on | No |
| embeddingConfigurations | dictionary | Should be keyed by embedding column name | No |

Table name rules

*   Max length is 128 characters
*   Must contain only alphanumeric characters and underscore
*   Must start with an alpha character

Example:

```
// Open connection
`gw set hopen 8082;

// Create table partitioned on date with flat index on the embeddings column
indexes:(enlist `flat;enlist `embeddings;enlist `flat;enlist `dims`metric!(25;`CS));
p:(!). flip ((`database;`default);
        (`table;`myTable);
        (`schema;flip `name`type!(`date`tag`val`embeddings;`d`s`j`E));
        (`partitionColumn;`date);
        (`indexes;flip `name`column`type`params!indexes));
gw(`createTable;p);

// Create table from external table partitioned on date with flat index on the embeddings column
ref:enlist `path`provider`type!("/tmp/kx/remote";`kx);
indexes:enlist `name`column`type`params!(`flat_index;`embeddings;`flat;enlist[`dims]!enlist 384);
p:`database`table`externalDataReferences`indexes`partitionColumn!(`default;`myTableExternal;ref;indexes;`date);
gw(`createTable;p);
```

#### `schema`

**Attributes:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| name | symbol | Column name | Yes |
| type | symbol | Column [type](https://code.kx.com/kdbai/latest/reference/supported-types.html) using kdb type symbols. Small for atoms and caps for vectors, Example: ‘i' for integer and 'I’ for integer list. | Yes |

Column name rules

*   Max length is 128 characters
*   Must contain only alphanumeric characters and underscore
*   Must start with an alpha character

Example:

```
schema: (`name`type!(`id;`i);`name`type!(`isValid;`b);`name`type!(`embeddings;`E);`name`type!(`sparse_col;`)
```

#### `indexes`

**Attributes:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| name | symbol | Index name | Yes |
| type | symbol | Index type, for example: Flat, qFlat, HNSW, ivf, ivfpq, qHNSW | Yes |
| column | symbol | kdb+ column name to apply index | Yes |
| params | dictionary | Index parameters containing index-specific attributes for [Flat](https://code.kx.com/kdbai/latest/reference/qAPI.html#flat), [qFlat](https://code.kx.com/kdbai/latest/reference/qAPI.html#qflat), [HNSW](https://code.kx.com/kdbai/latest/reference/qAPI.html#hnsw), [ivf](https://code.kx.com/kdbai/latest/reference/qAPI.html#ivf), [ivfpq](https://code.kx.com/kdbai/latest/reference/qAPI.html#ivfpq), [qHNSW](https://code.kx.com/kdbai/latest/reference/qAPI.html#qhnsw) | Yes |

Example:

```
flatIndex: `name`column`type`params!(`flat_index;`embeddings;`flat;enlist[`dims]!enlist 25)
hnswFast: `name`column`type`params!(`hnsw_fast;`embeddings;`hnsw;`dims`M`efConstruction!(25;8;8))
sparseIndex: `name`column`type`params!(`sparse_index;`sparse_column;`bm25;`k`b!(1.25;0.75))
indexes: (flat_index;hnsw_fast;sparse_index)
```

##### `flat`

Index-specific attributes (`params`) for `type = flat`

| **Attribute** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| dims | Dimension of vector space | int | Yes | N/A |
| metric | Distance metric | symbol | No | `L2 |

##### `qFlat`

Index-specific attributes (`params`) for `type = qFlat`

| **Attribute** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| dims | Dimension of vector space | int | Yes | N/A |
| metric | Distance metric | symbol | No | `L2 |

##### `hnsw`

Index-specific attributes (`params`) for `type = hnsw`

| **Attribute** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| dims | Dimension of vector space | int | Yes | N/A |
| M | Graph valency | int | No | 8 |
| efConstruction | Search depth at construction | int | No | 8 |
| metric | Distance metric | symbol | No | `L2 |

##### `qHnsw`

Index-specific attributes (`params`) for `type = qHnsw`

| **Attribute** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| dims | Dimension of vector space | int | Yes | N/A |
| M | Graph valency | int | No | 8 |
| efConstruction | Search depth at construction | int | No | 8 |
| metric | Distance metric | symbol | No | `L2 |
| mmapLevel | Level of memory mapping. Accepted values: - 0 for both vectors and node connection in memory; - 1 for memory-mapped vectors and in-memory nodes ; - 2 for both vectors and node connections memory mapped. | int | No | 1 |

##### `ivf`

Index-specific attributes (`params`) for `type = ivf`

| **Attribute** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| nclusters | Number of clusters | long | No | 8 |
| metric | Distance metric | symbol | No | `L2 |

##### `ivfpq`

Index-specific attributes (`params`) for `type = ivfpq`

| **Attribute** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| nclusters | Number of clusters | long | No | 8 |
| nbits | Number of bits to quantize | long | No | 8 |
| nsplits | Number of vectors to split | long | No | 8 |
| metric | Distance metric | symbol | No | `L2 |

#### `externalDataReferences`

**Attributes:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| path | string | Path to external table, for instance the existing kdb+ table mounted in our Docker container. | Yes |
| provider | symbol | Provider of external table, for example `kx`. | Yes |

Example:

Launch the KDB.AI Server container with the `-v` flag to mount an existing kdb+ DB in the container, for example:

```
docker run -it --rm -e NUM_WRK=1                        \
                    -e THREADS=16                       \
                    -e KDB_LICENSE_B64                  \
                    -v $PWD/vecdb/data:/tmp/kx/data/vdb \
                    -v $PWD/taq/db:/tmp/kx/remote:ro    \   <= mount a local ./taq/db under /tmp/kx/remote in the container as read-only
                    -p 8082:8082                        \
                    kdbai-db:local
```

 Then: 

```
gw(`createTable;`database`table`externalDataReferences!(`;`tq;enlist `path`provider!("/tmp/kx/remote";`kx)))
```

The name of the table (`tq`) should match the name of the target table in the external kdb+ database.

How to set up threads and the number of workers

For optimal performance, make sure to read about setting up both [`NUM_WRK`](https://code.kx.com/kdbai/latest/reference/multithreading.html#multi-worker-setup) and [`THREADS`](https://code.kx.com/kdbai/latest/reference/multithreading.html#setting-the-threads) environment variables.

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Table is created and returned | `success`result`error!1b;table_dictionary;" | N/A |
| Fail: Table name is not unique | `success`result`error!0b;();"Table with given name already exists" | Specify a different table name as it appears a table with this name already exists. |
| Fail: Table name is not valid | `success`result`error!0b;();"Table name is invalid" | Use a valid symbol for the table name. |
| Fail: Any of the input parameters are of wrong type | `success`result`error!0b;();"invalid arguments types: " ... | Provide the correct type of input parameters required. |
| Fail: Any of the input parameters are missing | `success`result`error!0b;();"missing arguments: " ... | Provide required input parameters. |
| Fail: Any of the input parameters are invalid | `success`result`error!0b;();"invalid arguments: " ... | Provide known or valid input parameters. |
| Fail: Schema individual attributes are not valid | `success`result`error!0b;();"invalid table attributes: " ... | Provide valid attributes in the schema. |
| Fail: Schema individual types are not valid | `success`result`error!0b;();"invalid column types: " ... | Provide valid [column types](https://code.kx.com/kdbai/latest/reference/supported-types.html) in the schema. |
| Fail: Index individual parameters are not valid | `success`result`error!0b;();"invalid index parameters:" ... | Double check the parameters of one of the specified indexes. |
| Fail: Database does not exist | `success`result`error!0b;();"Database does not exist" | Double check the database name. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

### Get table

`getTable`

Retrieve a table from a database with a given name.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | Name of the database where the table is. | Yes |
| table | symbol | Name of the table to be retrieved | Yes |

Example:

```
// Open connection
`gw set hopen 8082;
// Get table details
gw(`getTable;`database`table!`default`myTable);
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Table with given name is found | `success`result`error!(1b;table meta dictionary;"") | N/A |
| Fail; Database name is not valid | `success`result`error!0b;();"Database name is invalid" | A database with the given name does not appear to exist. Check the specified value. |
| Fail: Database with given name is not found | `success`result`error!0b;();"database {name} does not exist" | Check the name of the database you are searching for as it does not seem to exist. |
| Fail: Table name is not valid | `success`result`error!0b;();"Table name is invalid" | Provide a valid symbol for the table name. |
| Fail: Table with given name is not found | `success`result`error!0b;();"Table name is not found". | A table with the given name doens't exist. Double check the supplied value. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

### List tables

`listTables`

Retrieve a list of tables from a database with a given name.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | Name of the database where the table is. If you don't provide a database name, the default database is used. | Yes |

Example:

```
// Open connection
`gw set hopen 8082;
// Get tables details
gw(`listTables;enlist[`database]!enlist`default)
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Tables found | `success`result`error!(1b;`database`tables!(dbname;tables name list);"") | N/A |
| Fail: Database name is not valid | `success`result`error!0b;();"database {name} does not exist" | A database with the given name does not appear to exist. Check the specified value. |
| Fail: Database with given name is not found | `success`result`error!0b;();"database {name} does not exist" | Check the name of the database you are searching for as it does not seem to exist. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

### Load external table

`loadTable`

Load external/reference table.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | Name of the database to be loaded. | Yes |
| table | symbol | Name of the database to be loaded. | Yes |

Example:

```
`gw set hopen 8082;
gw(`loadTable;`database`table!`myDatabase`myTable)
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Table is loaded | `success` | N/A |
| Fail: Table does not exist | error!"table:trade does not exist in database:default" | Table does not exist in database. Try the get table/database endpoint to verify. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

### Delete table

`deleteTable`

Delete a table with a given name and all associated indexes.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | Name of the database where the table is. | Yes |
| table | symbol | Name of the table to be deleted. | Yes |

Example:

```
// Open connection
`gw set hopen 8082;
// Get table details
gw(`deleteTable;`database`table!`default`myTable);
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Table with given name has been deleted | `success`result`error!(1b;`database`tables!(dbname;tables name list);"") | N/A |
| Fail: Database name is not valid | `success`result`error!0b;();"database {name} does not exist" | A database with the given name does not appear to exist. Check the specified value. |
| Fail: Database with given name is not found | `success`result`error!0b;();"database {name} does not exist" | Check the name of the database you are searching for as it does not seem to exist. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

Index
-----

Retrieve and list indexes.

### Get index

`getIndex`

Retrieve an index from a table.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | Name of the database where the table is. If not provided, the default database is used. | Yes |
| table | symbol | Name of the table where the index to be retrieved is. | Yes |
| name | symbol | Name of the index to be retrieved | Yes |

Example:

```
`gw set hopen 8082;
gw(`getIndex;`database`table`name!`default`test`trade_flat_index)
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Index with given name is found and returned | `success`result`error!1b;dictionary of details;() | N/A |
| Fail: Table name is not valid | `success`result`error!0b;();"Table name is invalid" | Provide a valid symbol for the table name. |
| Fail: Table with given name is not found | `success`result`error!0b;();"Table name is not found". | A table with the given name doens't exist. Double check the supplied value. |
| Fail: Index name is not valid | `success`result`error!0b;();"Index name is invalid" | Provide a valid symbol for the index name. |
| Fail: Index with given name is not found | `success`result`error!0b;();"Index name is not found" | Double check the supplied value for the index. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

### List indexes

`listIndexes`

List all indexes for a table.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | Name of the database where the table is. If not provided, the default database is used. | No |
| table | symbol | Name of the table where the indexes to be retrieved are. | No |

Example:

```
`gw set hopen 8082
gw(`listIndexes;`database`table!`default`myTable)
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Indexes found and returned | `success`result`error!1b;dictionary of details;() | N/A |
| Fail: Database name is not valid | `success`result`error!0b;();"database {name} does not exist" | A database with the given name does not appear to exist. Check the specified value. |
| Fail: Database with given name is not found | `success`result`error!0b;();"database {name} does not exist" | Check the name of the database you are searching for as it does not seem to exist. |
| Fail: Table name is not valid | `success`result`error!0b;();"Table name is invalid" | Provide a valid symbol for the table name. |
| Fail: Table with given name is not found | `success`result`error!0b;();"Table name is not found". | A table with the given name doens't exist. Double check the supplied value. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

### Update indexes

`updateIndexes` (only for external kdb+ tables)

Build one or more indexes from scratch. Only allowed for kdb+ HDB tables.

Allows to build and attach indexes to external kdb+ tables.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | The name of the database. If a database name is not provided, the default database is used. | Yes |
| table | symbol | The name of the table. | Yes |
| indexes | symbol list | List of index names to build. | Yes |
| parts | symbol list | Partitions list to build index in case of partition database. If not given, then indexes will be built on all partitions. | Yes |

Example:

```
ref:enlist `path`provider!("/tmp/kx/remote";`kx);
indexes:enlist `name`column`type`params!(`flat_index;`embeddings;`flat;enlist[`dims]!enlist 384);

p:`database`table`externalDataReferences`indexes`partitionColumn!(`default;`SEC;ref;indexes;`date);
gw(`createTable;p);
gw(`updateIndexes;`database`table`indexes!(`default;`SEC;enlist `flat_index))
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Index(es) with given name(s) updated successfully | None | N/A |
| Fail: Database name is not valid | `success`result`error!0b;();"database {name} does not exist" | A database with the given name does not appear to exist. Check the specified value. |
| Fail: Database with given name is not found | `success`result`error!0b;();"database {name} does not exist" | Check the name of the database you are searching for as it does not seem to exist. |
| Fail: Table name is not valid | `success`result`error!0b;();"Table name is invalid" | Provide a valid symbol for the table name. |
| Fail: Table with given name is not found | `success`result`error!0b;();"Table name is not found". | A table with the given name doens't exist. Double check the supplied value. |
| Fail: Operation called on a table managed by kdbai | KDBAIException: feature not supported: build index is only allowed on reference database |  |
| Fail: Index name is not valid | ValueError: Index name is invalid |  |
| Fail: Index with given name is not found | KDBAIException: index not found: invalid |  |
| Fail: Update Operation is not valid | ValueError: Update Operation is not valid |  |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

Data
----

Insert, query, and search data.

### Insert data

`insertData`

Add rows to a table.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | The name of the database where the table is located. If a database name is not provided, the default database is used. | Yes |
| table | symbol | The name of the table where the data will be inserted. | Yes |
| payload | table | Data to insert. | No - not required when using external database. |

Example:

```
// Open connection
`gw set hopen 8082;

// Insert Data
gw(`insertData;`database`table`payload!(`default;`myTable;data));
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success. Data inserted successfully. | {`success`result`èrrorMsg!(1b;`rows_inserted!10;"")}) | N/A |
| Fail: Database name is not valid | `success`result`error!0b;();"database {name} does not exist" | A database with the given name does not appear to exist. Check the specified value. |
| Fail: Database with given name is not found | `success`result`error!0b;();"database {name} does not exist" | Check the name of the database you are searching for as it does not seem to exist. |
| Fail: Table name is not valid | `success`result`error!0b;();"Table name is invalid" | Provide a valid symbol for the table name. |
| Fail: Table with given name is not found | `success`result`error!0b;();"Table name is not found". | A table with the given name doens't exist. Double check the supplied value. |
| Fail: Index name is not valid | `success`result`error!0b;();"Index name is invalid" | Provide a valid symbol for the index name. |
| Fail: Index with given name is not found | `success`result`error!0b;();"Index name is not found" | Double check the supplied value for the index. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

### Train data

`trainData`

Train data.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | The name of the database where the table is located. | Yes |
| table | symbol | The name of the table. | Yes |
| payload | table | Data to insert. | Yes |

Example:

```
// Open connection
`gw set hopen 8082;

// Train
gw(`trainData;`database`table`payload!(`default;`myTable;data));
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Index(es) with given name(s) updated successfully | 1b | N/A |
| Fail: Database name is not valid | `success`result`error!0b;();"database {name} does not exist" | A database with the given name does not appear to exist. Check the specified value. |
| Fail: Database with given name is not found | `success`result`error!0b;();"database {name} does not exist" | Check the name of the database you are searching for as it does not seem to exist. |
| Fail: Table name is not valid | `success`result`error!0b;();"Table name is invalid" | Provide a valid symbol for the table name. |
| Fail: Table with given name is not found | `success`result`error!0b;();"Table name is not found". | A table with the given name doens't exist. Double check the supplied value. |
| Fail: Index name is not valid | `success`result`error!0b;();"Index name is invalid" | Provide a valid symbol for the index name. |
| Fail: Index with given name is not found | `success`result`error!0b;();"Index name is not found" | Double check the supplied value for the index. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

### Query data

`query`

Query data from a table.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | The name of the database where the table you are querying data from is located. | Yes |
| table | symbol | The name of the table you are querying data from. | Yes |
| filter | list of tuples | List of filter conditions, parse tree style. | No |
| sortColumns | list of symbols | The columns by which to sort the results. | No |
| groupBy | list of symbols | The column values by which to group the results. | No |
| aggs | dictionary | Aggregation rules. Dictionary structure: - `Key` → new column name - `Value` → old column name or parse tree style aggregation rule | No |
| limit | integer | Number of rows to return. | No |

Example:

```
// Open connection
`gw set hopen 8082;

// Query
gw(`query;args:`database`table!`default`myTable)
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successful query | table | N/A |
| Fail: Database name is not valid | `success`result`error!0b;();"database {name} does not exist" | A database with the given name does not appear to exist. Check the specified value. |
| Fail: Database with given name is not found | `success`result`error!0b;();"database {name} does not exist" | Check the name of the database you are searching for as it does not seem to exist. |
| Fail: Table name is not valid | `success`result`error!0b;();"Table name is invalid" | Provide a valid symbol for the table name. |
| Fail: Table with given name is not found | `success`result`error!0b;();"Table name is not found". | A table with the given name doens't exist. Double check the supplied value. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

### Search data

`search`

Perform a similarity search.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | Database name | Yes |
| table | symbol | Table name. | Yes |
| type | symbol | Refer to the [Type](https://code.kx.com/kdbai/latest/reference/qAPI.html#python-type) table below. | No |
| vectors | dictionary | Indexes to query with query vectors. If a temporal search is performed (see Type), then the name of the column to search should be provided instead of the index name. | Yes |
| n | long | Number of neighbors to return. | No |
| range | float | Returns all neighbors with distance < range. | No |
| indexParams | dictionary | Weights required for multi index search. | No |
| options | dictionary | Refer to Options table below. | Yes |
| filter | list of tuples | List of filter conditions, parse tree style. | No |
| searchBy | symbol atom or list of symbols | The columns to search by. | No |
| groupBy | list of symbols | The column values by which to group the results. | No |
| aggs | dictionary | Aggregation rules. | No |
| sortColumns | list of symbols | The columns by which to sort the results. | No |

#### `type`

| **Value** | **Notes** |
| --- | --- |
| If not provided | A standard similarity search (with or without tsc) is performed. |
| tss | A temporal similarity search is performed on the raw data - no indexes are required, instead column name is used in place of index name in vectors dictionary. |
| dtw | A temporal similarity search is performed using dynamic time warping on the raw data - no indexes are required, instead column name is used in place of index name in vectors dictionary. |

#### `options`

| **Attribute** | **For Type** | **Description** | Python type | Required | Default |
| --- | --- | --- | --- | --- | --- |
| distanceColumn | N/A | Rename distance column to this. | str | No | None |
| indexOnly | N/A | Return only index information. | bool | No | 0b |
| returnMatches | tss/dtw | (Non Transformed TSS only) Return the full detected pattern for each match. | bool | No | 0b |
| force | tss/dtw | Forces the search even if some searchBy group or table partition is failing, for example, when a partition has less data points than the searched pattern. | bool | No | 0b |
| normalize | tss | Controls whether TSS applies Z-normalization to the data before performing similarity search. | bool | No | 0b |
| RR | dtw | Ratio of warping radius; Range: 0 ≤ RR ≤ 1 | float | No | 0.05 |
| cutOff | dtw | Cut-off threshold value; Range: 0 < cutOff ≤ ∞ | float | No | 0w |

#### `indexParams`

`index_params` is a dictionary where key is index name and value is a dictionary with the arguments below .

| **Attribute** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| weight | Weight for each index. | float | Required for multi index input. | None |

Important

For multi index searches, you have to allocate a weight to each index. The sum of all weights must be equal to 1.

Example:

```
// Open connection
`gw set hopen 8082;

// Query
gw(`search;args:`database`table`vectors`n!(`default;`myTable;enlist[`indexName]!enlist enlist 384?1e;25))

// TSS Search
gw(`search;`database`table`type`vectors`n!(`default;`table;`tss;enlist[`columnToSearch]!enlist enlist 64?1f;10))
gw(`search;`database`table`type`vectors`n`options!(`default;`table;`tss;enlist[`columnToSearch]!enlist enlist 64?1f;10;`returnMatches`force!11b))

// DTW Search
gw(`search;`database`table`type`vectors`n!(`default;`table;`dtw;enlist[`columnToSearch]!enlist enlist 64?1f;10))
gw(`search;`database`table`type`vectors`n`options!(`default;`table;`dtw;enlist[`columnToSearch]!enlist enlist 64?1f;10;(`RR`cutOff)!(0.05;0w)))
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successful query | list of tables | N/A |
| Fail: Database name is not valid | `success`result`error!0b;();"database {name} does not exist" | A database with the given name does not appear to exist. Check the specified value. |
| Fail: Database with given name is not found | `success`result`error!0b;();"database {name} does not exist" | Check the name of the database you are searching for as it does not seem to exist. |
| Fail: Table name is not valid | `success`result`error!0b;();"Table name is invalid" | Provide a valid symbol for the table name. |
| Fail: Table with given name is not found | `success`result`error!0b;();"Table name is not found". | A table with the given name doens't exist. Double check the supplied value. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

### Update data

`updateData`

Update one or more rows of data in a table.

**Input parameters**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | The name of the database. | Yes |
| table | symbol | The name of the table. | Yes |
| filter | list of list | List of filter conditions parse-tree style. | No |
| columns | dictionary | Columns to update. Each key represents a column name, and the corresponding value can be either: • A single value (applied to all rows), or • A list of values (length must match number of rows being updated). | Yes |

Example:

```
// Open connection
`gw set hopen 8082;
// Query
gw(`updateData;args:`database`table`columns`filter!(`default;`myTable;enlist[`sym]!enlist[`Vod.l];enlist(=;`sym;`AAC.l)))
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successful update | `success`result`error!(1b;`rowsUpdated!2;"") | Success |
| Fail: Wrong values length | `success`result`error!(0b;();"Value count mismatch: expected 3 items ") | - If applying the same value to all rows, provide a scalar value, not a list. - If using a list of values, make sure its length matches the number of rows that meet the filter condition. - Verify that your filter expression returns the expected number of rows before updating. |
| Fail: Wrong values types | `success`result`error!(0b;();"Wrong value types: sym, size ") | - Check the table schema to confirm the expected q types for each column. - Make sure the values in your columns dictionary use the correct types. - Remember that q distinguishes between types such as symbol, char, int, and float. |
| Fail: Invalid column name | `success`result`error!(0b;();"Column does not exist: size ") | A column with the given name does not appear to exist. Please, check the specified value. |
| Fail: Index is not supported | `success`result error!(0b;();"Update operation is not supported on this table's index type") | Ensure that you are performing updates only on tables with no index or the supported index types (`flat`, `qFlat`, `hnsw`, or `qHnsw`). |
| Fail: Database name is not valid | `success`result`error!0b;();"database {name} does not exist" | Use a valid symbol for the database name. |
| Fail: Database with given name is not found | `success`result`error!0b;();"database {name} does not exist" | Check the name of the database as it does not seem to exist. |
| Fail: Table name is not valid | `success`result`error!0b;();"Table name is invalid" | Use a valid symbol for the table name. |
| Fail: Table with given name is not found | `success`result`error!0b;();"Table name is not found" | Check the name of the table as it does not seem to exist. |
| Error: KDBAI is not available | Cannot write to handle ... | The server is not available. Please, check your connection and if your server is running. |

### Delete data

`deleteData`

Delete data from a table.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | The name of the database. | Yes |
| table | symbol | The name of the table. | Yes |
| filter | list of tuples | List of filter conditions parse-tree style. | No |

Example:

```
// Open connection
`gw set hopen 8082;

// Delete data
gw(`deleteData;args:`database`table`filter!(`default;`trade;(("=";"date";"2025.05.14");("=";"sym";"Vod.l")))
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successful delete for splayed table | Pandas DataFrame | Success |
| Success: Partial delete for partition table | Pandas DataFrame | Success |
| Fail: Delete failed because of disk issue | N/A |  |
| Fail: Delete failed because of internal error | N/A |  |
| Fail: Database name is not valid | N/A | Use a valid symbol for the database name. |
| Fail: Database with given name is not found | N/A | Check the name of the database as it does not seem to exist. |
| Fail: Table name is not valid | N/A | Use a valid symbol for the table name. |
| Fail: Table with given name is not found | N/A | Check the name of the table as it does not seem to exist. |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure Home - KDB.AI server running') | Check your connection and if your server is running. |

Info
----

Get information on tables, databases, sessions, processes or system.

### Get table info

`getTableInfo`

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | The name of the database. | Yes |
| table | symbol | The name of the table. | Yes |

Example:

```
// Open connection
`gw set hopen 8082;

// Get table info
gw(`getTableInfo;args:`database`table!(`default;`table1))
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successfully returns table info | Dictionary of table info | N/A |
| Fail: Table name does not exist | `success`result`error!0b;();"table {name} does not exist" | Check the name of the table as it does not seem to exist. |
| Fail: Database does not exist | `success`result`error!0b;();"database {name} does not exist" | Check the name of the database as it does not seem to exist. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

### Get database info

`getDatabaseInfo`

Get database info, including table info of each table in the database.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | The name of the database. | Yes |

Example:

```
// Open connection
`gw set hopen 8082;

// Get Database Info
gw(`getDatabaseInfo;args:enlist[`database]!enlist `default)
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successfully returns database info | List of dictionaries containing database info and table info within that database | N/A |
| Fail: Database does not exist | N/A | Check the name of the database as it does not seem to exist. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

### Get all databases info

`getDatabasesInfo`

Get all databases info, including table info of all tables in all databases.

**Input parameters:**

N/A

Example:

```
// Open connection
`gw set hopen 8082;

// Get databases info
gw(`getAllDatabasesInfo;`)
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successfully returns all databases info | List of dictionaries containing databases info, including info about each databases and the tables within each database | N/A |
| Fail: Databases don't exist | `success`result`error!0b;();"databases do not exist" | No databases exist. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

### Get session info

`getSessionInfo`

**Input parameters:**

N/A

Example:

```
// Open connection
`gw set hopen 8082;

// Get session info
gw(`getSessionInfo;`)
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successfully returns the number of sessions and when they started | Dictionary of session info | N/A |
| Fail: No sessions have been created | `success`result`error!0b;();"sessions do not exist" | No sessions exist. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

* * *

### Get process info

`getProcessInfo`

**Input parameters:**

N/A

Example:

```
// Open connection
`gw set hopen 8082;

// Get processes info
gw(`getProcessInfo;`)
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successfully returns process info | List of dictionaries of process info | N/A |
| Fail: Cannot retrieve process information due to internal server issue | `success`result`error!0b;();"internal server error" | N/A |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure Home - KDB.AI server running' | Check your connection and if your server is running. |

### Get system info

`getSystemInfo`

**Input parameters:**

N/A

Example:

```
// Open connection
`gw set hopen 8082;

// Get system info
gw(`getSystemInfo;`)
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successfully returns system info | List of dictionaries including system info, process info, sessions info, database and table info in the system | N/A |
| Fail: Cannot retrieve system information due to internal server issue | `success`result`error!0b;();"internal server error" | N/A |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure Home - KDB.AI server running') | Check your connection and if your server is running. |

ACL Grants
----------

Add, list, get, and delete ACL grants.

### Add grants

`addGrants`

Add one or more ACL grants.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| resource | symbol | Grant resource name (database, table, admin) | Yes | None |
| databaseName | symbol | The name of the database | Yes | None |
| table | symbol | The name of the table (mandatory for table resource) | No | None |
| tenant | symbol | Tenant ID from IdP provider | Yes | None |
| groups | list of symbols | User group names from IdP provider | Yes | None |
| actions | list of symbols | Actions to set — read/write/delete/system_admin | Yes | None |

Example:

```
// Open connection
`gw set hopen `::8082:<username>:<oauth_token>;
// Query
gw(`addGrants;args:enlist `resource`tenant`groups`databaseName`actions!(`database;`quants;`quants_read;`default;`read))
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successful update | `success`result`error!(1b;`rowsUpdated!2;"") | N/A |
| Fail: Wrong values length | `success`result`error!(0b;();"Value count mismatch: expected 3 items ")|- If applying the same value to all rows, provide a **scalar value**, not a list.<br> - If using a list of values, make sure its **length matches** the number of rows that meet the`filter`condition.<br> - Verify that your`filter` expression returns the expected number of rows before updating. |  |
| Fail: Wrong values types | `success`result`error!(0b;();"Wrong value types: sym, size ")|- Check the **table schema** to confirm the expected q types for each column.<br> - Make sure the values in your`columns`dictionary use the correct types.<br> - Remember that q distinguishes between types such as`symbol`,`char`,`int`, and`float`. |  |
| Fail: Invalid column name | `success`result`error!(0b;();"Column does not exist: size ") | A column with the given name does not appear to exist. Please, check the specified value. |
| Fail: Index is not supported | `success`result`error!(0b;();"Update operation is not supported on this table's index type")|Ensure that you are performing updates only on tables with **no index** or the **supported index types** (`flat`,`qFlat`,`hnsw`, or`qHnsw`) |  |
| Fail: Database name is not valid | `success`result`error!0b;();"database {name} does not exist" | A database with the given name does not appear to exist. Check the specified value. |
| Fail: Database with given name is not found | `success`result`error!0b;();"database {name} does not exist" | A database with the given name does not appear to exist. Check the specified value. |
| Fail: Table name is not valid | `success`result`error!0b;();"Table name is invalid" | The table name is invalid. Provide a valid symbol for the table name. |
| Fail: Table with given name is not found | `success`result`error!0b;();"Table name is not found" | A table with the given name was not found. Double check the supplied value. |
| Error: KDBAI is not available | Cannot write to handle... | Check your connection and if your server is running. |

### Get all grants

`getAllGrants`

Get all ACL grants.

Example:

```
`gw set hopen `::8082:<username>:<oauth_token>;
gw(`getAllGrants;`)
```

### Get grant for id

`getGrantById`

Get ACL grant for given grant id.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| id | dictionary → enlist[`id]!enlist | Grant id. | Yes | None |

Example:

```
`gw set hopen `::8082:<username>:<oauth_token>;
gw(`getGrantById;enlist[`id]!enlist `test)
```

### Delete grant

`deleteGrant`

Delete ACL grant for given id.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| id | dictionary → enlist[`id]!enlist | Grant id. | Yes | None |

Example:

```
`gw set hopen `::8082:<username>:<oauth_token>;
gw(`deleteGrant;enlist[`id]!enlist `test)
```
