# Source: https://code.kx.com/kdbai/latest/reference/python-client.html

Title: KDB.AI Python API Client - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/reference/python-client.html

Markdown Content:
_This page contains the references for KDB.AI's Python API. For example usage, see the [Quickstart Guide](https://code.kx.com/kdbai/latest/gettingStarted/quickstart.html)._

Note

Before you start, ensure you have the following installed on your machine:

*   [Python](https://www.python.org/downloads) (versions 3.9 to 3.13)
*   An active KDB.AI [Server](https://kx.com/kdb-ai-server-download/) license
*   `kdbai-client`
*   [PyKX dependencies](https://code.kx.com/pykx/3.1/getting-started/installing.html#dependencies).

Note: Index Options

The argument `index_option` of function `search()` is the index-specific option for similarity search. For example, you can specify `efSearch` for HNSW indexes and `clusters` for IVF/IVFPQ indexes.

For details of the usage of `index_option`, see the [How to use an Index in KDB.AI](https://code.kx.com/kdbai/latest/use/supported-indexes.html) page.

Session
-------

Session represents a connection to a KDB.AI instance. To interact with KDBAI Server, you first need to create a session. This section summarizes how to create and close a session.

### Create session

`kdbai_client.Session`

Session represents a connection to a KDB.AI instance.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| api_key | str | API Key to be used for authentication. | No | None |
| endpoint | str | Server endpoint to connect to. | No | 'http://localhost:8081' |
| host | str | Hostname of the KDB.AI server. | No | None |
| port | int | Port number on the server. | No | - 8081 if `mode='rest'` - 8082 if `mode='qipc'` |
| mode | str | Implementation method used for the session. Possible values: `rest` and `qipc` | No | None |

Important

1.   If you don't provide the `mode` parameter, a qIPC-based session is created.

2.   The REST-based implementation has worse performance due to payload serialization and deserialization.

Example:

```
import kdbai_client as kdbai
### local server
session = kdbai.Session(endpoint='http://localhost:8082')
session = kdbai.Session(endpoint='http://localhost:8082', mode='qipc')
### local server using REST
session = kdbai.Session(endpoint='http://localhost:8081', mode='rest')
### local server using TLS
session = kdbai.Session(endpoint='http://localhost:8082', options={'tls': True})
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Session is created and KDB.AI instance can be interacted with. | True | N/A |
| Fail: Incorrect API Key is provided when attempting to connect to a KDB.AI Cloud. | KDBAIException with appropriate error message: - qIPC: Error during creating connection, make sure KDB.AI server is running and accepts qIPC connection on port {port}: {e}“ where `e` is the original underlying error. - REST: Failed to open a session on {self.endpoint} using API key with prefix {tmp}. Please double check your `endpoint` and `api_key`. | Check endpoint (host/port), credentials, and `mode` parameter. Check port forwarding in your environment and what port rules are allowed/denied. |
| Fail: No API Key is provided when attempting to connect to a KDB.AI Cloud. | KDBAIException with appropriate error message: qIPC: “Error during creating connection, make sure KDB.AI server is running and accepts qIPC connection on port {port}: {e}“ where e is the original underlying error. REST: Failed to open a session on {self.endpoint} using API key with prefix {tmp}. Please double check your `endpoint` and `api_key`. | Check endpoint (host/port), credentials, and `mode` parameter. Check port forwarding in your environment and what port rules are allowed/denied. |
| Fail: Server and client versions are incompatible. | Your KDB.AI server is not compatible with this client (kdbai_client=={version}). Use kdbai_client >={versions['`clientMinVersion`']} and <={versions['`clientMaxVersion`']} | Upgrade/downgrade either Server or client. |
| Error: Session cannot be created because KDB.AI is not available. | RuntimeError('Error during request, make sure KDB.AI server running') | Check your connection and if your server is running. |

### Close session

`session.close()`

You cannot execute any client-server interaction after this call.

Example:

```
session.close()
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Session is closed and KDB.AI instance can no longer be interacted with. | True | N/A |

### Get version info

`session.version()`

Retrieve version info from server and compatible client min/max version.

Example:

```
session.version()
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success. version info is returned. | {'serverVersion': '1.4.0','clientMinVersion': '1.4.0' ,'clientMaxVersion': 'latest'} | N/A |
| Error: KDBAI is not available. | RuntimeError('Error during request, make sure KDB.AI server running') | Check your connection and if your server is running. |

Database
--------

Create, delete, and retrieve databases.

In KDB.AI, a [database](https://code.kx.com/kdbai/latest/reference/database.html) is a collection of tables which store related data.

Key principles for database management

To simplify database design/management and prevent naming conflicts, follow the principles below:

*   **Unique database names**: Each database must have a unique name and can contain multiple tables.
*   **Unique table names within a database**: Tables within a database must have unique names, but different databases can contain tables with the same name. This is similar to the concept of namespaces.
*   **Cascade deletion**: When deleting a database, all child entities (tables) will also be deleted.
*   **Default database**: You don't need to create a database to create tables. If you create a table without specifying a database, it will be placed in a default, undeletable database.

### Create database

`session.create_database`

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| database | str | Name of the database to create. | Yes | None |

Database name rules

*   Max length is 128 characters
*   Must contain only alphanumeric characters and underscore
*   Must start with an alpha character

Example:

```
session.create_database("myDatabase")
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Database is created and returned | database instance | N/A |
| Fail: Database name is not unique | Raise exception | A database with the given name already exists. Create a database with another name. |
| Fail: Database name is not a valid name | Raise exception | Provide a valid str for the database name. |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure KDB.AI server running') | Check your connection and if your server is running. |

### Get database

`session.database`

Retrieve database with a given name.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | str | Name of the database to be retrieved | Yes |

Example:

```
session.database("myDatabase")
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Database with given name is found | Database instance. | N/A |
| Fail: Database with given name is not found | KDB.AI Exception: database {name} does not exist | Check the name of the database you are searching for as it does not seem to exist. |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure KDB.AI server running') | Check your connection and if your server is running. |

### Refresh database

`database.refresh()`

This method ensures that the list of tables associated with the loaded database is current. If the list is not up-to-date, it updates it. This is particularly useful if tables have been added to the database after the `getDatabase` function was called.

Example:

```
database.refresh()
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Database is refreshed | None | N/A |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure KDB.AI server running') | Check your connection and if your server is running. |

### List databases

`session.databases`

Retrieve list of databases in ascending order.

Example:

```
session.databases()
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Returns list of database names and default database included | list of database names | N/A |
| Error: Databases cannot be listed because KDBAI is not available | RuntimeError('Error during request, make sure KDB.AI server running') | Check your connection and if your server is running. |

### Delete database

`database.drop`

Delete database with a given name and all associated tables.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | str | Name of the database to be deleted. | Yes |

Example:

```
db=session.database("myDatabase")
db.drop()
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Database with given name has been deleted | N/A | N/A |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure KDB.AI server running') | Check your connection and if your server is running. |

Table
-----

Create, delete, update, and retrieve tables.

### Create table

`database.create_table`

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | instance name | Name of the database. | Yes |
| table | str | Name of the table to create. | Yes |
| [external_data_references](https://code.kx.com/kdbai/latest/reference/python-client.html#external_data_references) | dict | Should contain the keys: - `path` (path to the existing kdb+ table mounted in our Docker container) - `provider` (set to `kx`) WARNING: the name of the table should match the name of the target table in the existing kdb+ database. | No |
| [schema](https://code.kx.com/kdbai/latest/reference/python-client.html#schema) | dict | Schema details for the table. | Yes - if external_data_references is not specified. |
| [indexes](https://code.kx.com/kdbai/latest/reference/python-client.html#indexes) | list of dict | List of index definitions | No |
| partitionColumn | str | Column name to partition on | No |
| embeddingConfigurations | dict | Should be keyed by embedding column name | No |

Table name rules

*   Max length is 128 characters
*   Must contain only alphanumeric characters and underscore
*   Must start with an alpha character

Example:

```
schema = [{'name': 'id', 'type': 'int16'},
{'name': 'tag', 'type': 'bool'},
{'name': 'author', 'type': 'str'},
{'name': 'length', 'type': 'int32'},
{'name': 'content', 'type': 'str'},
{'name': 'createdDate', 'type': 'datetime64[D]'},
{'name': 'embeddings', 'type': 'float64s'}]
indexes = [
  {'type': 'flat', 'name': 'flat', 'column': 'embeddings',  'params': {'dims': 1536}},
  {'type': 'hnsw', 'name': 'fast_hnsw', 'column': 'embeddings', 'params': {'dims': 1536,'M': 8, 'efConstruction': 8}},
  {'type': 'hnsw', 'name': 'accurate_hnsw','column': 'embeddings', 'params': {'dims': 1536,'M': 64, 'efConstruction':256}} 
]
db = session.database("default")
db.create_table(table="myTable", schema=schema, indexes=indexes)
# create partitioned table
db.create_table(table="myPartitionedTable", schema=schema, indexes=indexes, partition_column='createdDate')
```

#### `schema`

**Attributes:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| name | str | Column name | Yes |
| type | str | Column [type](https://code.kx.com/kdbai/latest/reference/supported-types.html) | Yes |

Column name rules

*   Max length is 128 characters
*   Must contain only alphanumeric characters and underscore
*   Must start with an alpha character

Example:

```
schema = [ { 'name': 'id', 'type': 'int32'}, { 'name': 'isValid', 'type': 'bool'},
{ 'name': 'embeddings', 'type': 'float32s' }, { 'name': 'sparse_col', 'type': 'general' } ]
```

#### `indexes`

**Attributes:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| name | str | Index name | Yes |
| type | str | Index type, for example: flat, qFlat, hsnw, ivf, ivfpq, qhsnw | Yes |
| column | str | kdb+ column name to apply index | Yes |
| params | dict | Index parameters containing index-specific attributes for [Flat](https://code.kx.com/kdbai/latest/reference/python-client.html#flat), [qFlat](https://code.kx.com/kdbai/latest/reference/python-client.html#qflat), [HNSW](https://code.kx.com/kdbai/latest/reference/python-client.html#hnsw), [ivf](https://code.kx.com/kdbai/latest/reference/python-client.html#ivf), [ivfpq](https://code.kx.com/kdbai/latest/reference/python-client.html#ivfpq), [qHNSW](https://code.kx.com/kdbai/latest/reference/python-client.html#qhnsw) | Yes |

Example:

```
indexes = [
  {'type': 'flat', 'name': 'flat', 'column': 'embeddings',  'params': {'dims': 1536}},
  {'type': 'hnsw', 'name': 'fast_hnsw', 'column': 'embeddings', 'params': {'dims': 1536, 'M': 8, 'efConstruction': 8}},
  {'type': 'hnsw', 'name': 'accurate_hnsw','column': 'embeddings', 'params': {'dims': 1536, 'M': 64, 'efConstruction':256}} 
]
```

##### `flat`

Index-specific attributes (`params`) for `type = flat`

| **Attribute** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| dims | Dimension of vector space | int | Yes | N/A |
| metric | Distance metric | str | No | L2 |

##### `qFlat`

Index-specific attributes (`params`) for `type = qFlat`

| **Attribute** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| dims | Dimension of vector space | int | Yes | N/A |
| metric | Distance metric | str | No | L2 |

##### `hnsw`

Index-specific attributes (`params`) for `type = hnsw`

| **Attribute** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| dims | Dimension of vector space | int | Yes | N/A |
| M | Graph valency | int | No | 8 |
| efConstruction | Search depth at construction | int | No | 8 |
| metric | Distance metric | str | No | L2 |

##### `qHnsw`

Index-specific attributes (`params`) for `type = qHnsw`

| **Attribute** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| dims | Dimension of vector space | int | Yes | N/A |
| M | Graph valency | int | No | 8 |
| efConstruction | Search depth at construction | int | No | 8 |
| metric | Distance metric | str | No | L2 |
| mmapLevel | Level of memory mapping. Accepted values: - 0 for both vectors and node connection in memory; - 1 for memory-mapped vectors and in-memory nodes ; - 2 for both vectors and node connections memory mapped. | int | No | 1 |

An index consists of vectors and nodes. Vectors represent the data points in the vector space, while nodes are part of the graph structure used to organize and search through these vectors efficiently. Nodes connect vectors based on their similarity, forming a graph that facilitates fast nearest-neighbor searches.

##### `ivf`

Index-specific attributes (`params`) for `type = ivf`

| **Attribute** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| nclusters | Number of clusters | long | No | 8 |
| metric | Distance metric | str | No | L2 |

##### `ivfpq`

Index-specific attributes (`params`) for `type = ivfpq`

| **Attribute** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| nclusters | Number of clusters | long | No | 8 |
| nbits | Number of bits to quantize | long | No | 8 |
| nsplits | Number of vectors to split | long | No | 8 |
| metric | Distance metric | str | No | L2 |

#### `external_data_references`

**Attributes:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| path | byte str | Path to external table, for instance the existing kdb+ table mounted in our Docker container. | Yes |
| provider | str | Provider of external table, for example `kx`. | Yes |

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
database.create_table("tq", external_data_references=[{'path': b'/tmp/kx/remote', 'provider': 'kx'}])
```

The name of the table (`tq`) should match the name of the target table in the existing kdb+ db.

How to set up threads and the number of workers

For optimal performance, make sure to read about setting up both [`NUM_WRK`](https://code.kx.com/kdbai/latest/reference/multithreading.html#multi-worker-setup) and [`THREADS`](https://code.kx.com/kdbai/latest/reference/multithreading.html#setting-the-threads) environment variables.

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Table is created and returned | `success`result`error!True;table_dictionary;" | N/A |
| Fail: Table name is not unique | Raise exception | Specify a different table name as it appears a table with this name already exists. |
| Fail: Table name is not valid | Raise exception | Use a valid string for the table name. |
| Fail: Any of the input parameters are of wrong type | ValueError: "invalid arguments types: " ... | Provide the correct type of input parameters required. |
| Fail: Any of the input parameters are missing | ValueError: "missing arguments: " ... | Provide required input parameters. |
| Fail: Any of the input parameters are invalid | ValueError: "invalid arguments: " ... | Provide known or valid input parameters. |
| Fail: Schema individual attributes are not valid | ValueError: "invalid table attributes: " ... | Provide valid attributes in the schema. |
| Fail: Schema individual types are not valid | ValueError: "invalid column types: " ... | Provide valid [column types](https://code.kx.com/kdbai/latest/reference/supported-types.html) in the schema. |
| Fail: Index individual parameters are not valid | ValueError: "invalid index parameters: " ... | Double check the parameters of one of the specified indexes. |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure KDB.AI server running') | Check your connection and if your server is running. |

### Get Table

`database.table`

Retrieve a table from a database with a given name.

Example:

```
db=session.database("default")
db.table("myTable")
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Table with given name is found | Table meta dictionary as Pandas DataFrame | N/A |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure KDB.AI server running') | Check your connection and if your server is running. |

### Refresh table

`table.refresh()`

This method ensures that the table index and schema information associated with the table is current and calls `getTable` function.

Example:

```
table.refresh()
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Table is refreshed | None | N/A |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure KDB.AI server running') | Check your connection and if your server is running. |

### List tables

`database.tables`

Retrieve a list of tables from a database with a given name.

Tables are cached on the database instance. As a result, the data might have changed since the last get or refresh.

Example:

```
db = session.database("myDatabase")
db.tables
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Tables found | List of table names | N/A |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure KDB.AI server running') | Check your connection and if your server is running. |

### Load external table

`table.load`

Load external/reference table.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | str | Name of the database to be loaded. | Yes |
| table | str | Name of the database to be loaded. | Yes |

Example:

```
db=session.database("myDatabase")
tbl = db.table("myTable")
tbl.load()
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Table is loaded | None | N/A |
| Fail: Table does not exist | `fail`"Table does not exist" | Table does not exist in database. Try get table/database endpoint to verify. |
| Error: KDBAI is not available | `Error during request.` "Make sure KDB.AI server is running." | Check your connection and if your server is running. |

### Delete Table

`table.drop()`

Delete a table with a given name and all associated indexes.

Example:

```
db = session.database("default")
table = db.table("myTable")
table.drop()
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Table with given name has been deleted | N/A | N/A |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure KDB.AI server running') | Check your connection and if your server is running. |

Index
-----

Retrieve and list indexes.

### Get index

`table.index`

Retrieve an index from a table.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| name | str | Name of the index to be retrieved | Yes |

Example:

```
table.index('trade_flat_index')
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Index with given name is found and returned | dictionary | N/A |
| Fail: Index name is not valid | ValueError: Index name is invalid | Provide a valid string for the index name. |
| Fail: Index with given name is not found | ValueError: Index name is not found | Provide correct index name. |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure KDB.AI server running') | Check your connection and if your server is running. |

### List indexes

`table.indexes`

List all indexes for a table.

Example:

```
db = session.database("default")
table = db.table("myTable")
table.indexes
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Indexes found and returned | list of dictionaries | N/A |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

### Update indexes (only for external kdb+ tables)

`table.update_indexes`

Build one or more indexes from scratch. Only allowed for kdb+ HDB tables.

Allows to build indexes from scratch. Only supported for kdb+ HDB tables.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| indexes | list | List of index names to build. | Yes |
| parts | list | Partitions list to build index in case of partition database. If not given, then indexes will be built on all partitions. | Yes |

Example:

```
db = session.database("default")
table = db.table("SEC")
table.update_indexes(indexes=["flat_index"], parts=[1,2,3]) #assuming we have a partition column with integer type
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Index(es) with given name(s) updated successfully | None | N/A |
| Fail: Operation called on a table managed by kdbai | KDBAIException: feature not supported: build index is only allowed on reference database | Use build index only on reference tables. |
| Fail: Index name is not valid | ValueError: Index name is invalid | Provide a valid string for the index name |
| Fail: Index with given name is not found | KDBAIException: index not found: invalid | Provide correct index name. |
| Fail: Update operation is not valid | ValueError: Update operation is not valid |  |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

Data
----

Insert, query, and search data.

### Insert data

`table.insert`

Add rows to a table.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| payload | dataframe | Data to insert. | No - not required when using external database. |

Example:

```
db = session.database("default")
table = db.table("myTable")
table.insert(data)
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Data inserted successfully. | dictionary | N/A |
| Fail: Data table does not match with table schema. | KDBAIException: "data has wrong types: cols provided - expecting " | Check data schema and expected table schema. |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure KDB.AI server running') | Check your connection and if your server is running. |

### Train data

`table.train`

Train data.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| payload | table | Data to insert. | Yes |

Example:

```
db = session.database("default")
table = db.table("myTable")
table.train(payload=data)
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Index(es) with given name(s) updated successfully | True | N/A |
| Fail: Index name is not valid | ValueError: Index name is invalid | Provide a valid string for the index name. |
| Fail: Index with given name is not found | ValueError: Index name is not found | Provide correct index name. |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure KDB.AI server running') | Check your connection and if your server is running. |

### Query data

`table.query`

Query data from a table.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| filter | list of tuples | List of filter conditions, parse tree style. | No |
| sort_columns | list of str | The columns by which to sort the results. | No |
| group_by | list of str | The column values by which to group the results. | No |
| aggs | dictionary | Aggregation rules. Dictionary structure: - `Key` → new column name - `Value` → old column name or parse tree style aggregation rule | No |
| limit | int | Number of rows to return. | No |

Example:

```
db = session.database("default")
table = db.table("myTable")
table.query()  #returns all rows in the table
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successful query | Pandas DataFrame | N/A |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure KDB.AI server running') | Check your connection and if your server is running. |

### Search data

`table.search`

Perform a similarity search.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | str | Database name. | Yes |
| table | str | Database name. | Yes |
| type | str | Refer to the Type ??? table below. | No |
| vectors | dictionary | Indexes to query with query vectors. If a temporal search is performed (refer to Type), provide the name of the column to search instead of the index name. | Yes |
| n | int | Number of neighbors to return. | No |
| range | float | Returns all neighbors with distance < range. | No |
| index_params | dictionary (key is index name and value is dictionary of parameters for that index) | Weights required for multi index search. | No |
| options | dictionary | Refer to the Options??? table below. | Yes |
| filter | list of tuples | List of filter conditions, parse-tree style. | No |
| search_by | str or list of str | The columns to search by. | No |
| group_by | list of str | The column values by which to group the results. | No |
| aggs | dictionary | Aggregation rules. | No |
| sort_columns | list of str | The columns by which to sort the results. | No |

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
| force | tss/dtw | Forces the search even if some searchBy ???? group or table partition is failing, for example, when a partition has less data points than the searched pattern. | bool | No | 0b |
| normalize | tss | Controls whether TSS applies Z-normalization to the data before performing similarity search. | bool | No | 0b |
| RR | dtw | Ratio of warping radius; Range: 0 ≤ RR ≤ 1 | float | No | 0.05 |
| cutOff | dtw | Cut-off threshold value; Range: 0 < cutOff ≤ ∞ | float | No | 0w |

#### `index_params`

`index_params` is a dictionary where key is index name and value is a dictionary with the arguments below .

| **Attribute** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| weight | Weight for each index. | float | Required for multi index input. | None |

Important

For multi index searches, you have to allocate a weight to each index. The sum of all weights must be equal to 1.

Example:

```
db = session.database('default')
table = db.table('myTable')
# search vectors are either list of vectors or list of dictionaries (for sparse search)
v = [[1.0, 2.3, 6.7, 2.3, 2.3], [1.0, 2.3, 6.7, 2.3, 2.3]]
s = [{1: 2.3, 43: 0.4, 324: 4.6}, {1: 2.3, 43: 0.4, 324: 4.6}]

# simple dense search
table.search(vectors={'indexName': v}, n=10)

# simple sparse search
table.search(vectors={'sparseIndexName': s}, n=10)

# filtered search
table.search(vectors={'indexName': v}, n=10, filter=[['in', 'sym', [['AA', 'ABC']], ['<', 'num', 250]])

# TSS
table.search(vectors={'columnToSearch': v}, n=10, type='tss')
table.search(vectors={'columnToSearch': v}, n=10, type='tss', options={'returnMatches': True, 'force': True})

# DTW
table.search(vectors={'columnToSearch': v}, n=10, type='dtw')
table.search(vectors={'columnToSearch': v}, n=10, type='dtw', options={'RR':0.05, 'cutOff':15.5})

# use index_params
table.search(vectors={'indexName': v}, n=10, index_params={'indexName': {'efSearch': 64}})

# hybrid search
index_params = {
'indexName': {'weight': 0.6},
'sparseIndexName': {'weight': 0.4},
}
table.search(vectors={'indexName': v, 'sparseIndexName': s}, n=10, index_params=index_params)

# override __nn_distance column name
table.search(vectors={'indexName': v}, n=10, options={"distanceColumn": 'myDist'})

# override sort columns
table.search(vectors={'indexName': v}, n=10, sort_columns=['price', 'quantity'])

# group by
table.search(vectors={'indexName': v}, n=10, group_by=['sym'])

# aggs
table.search(vectors={'indexName': v}, n=10, aggs={'max_price': ['max', 'price']})
table.search(vectors={'indexName': v}, n=10, group_by=['sym'], aggs={'max_price': ['max', 'price']})

# rename a column
table.search(vectors={'indexName': v}, n=10, aggs={'new_col_name': 'existing_col_name'})

# change the result type
table.search(vectors={'indexName': v}, n=10, result_type='pd')
table.search(vectors={'indexName': v}, n=10, result_type='q')
table.search(vectors={'indexName': v}, n=10, result_type='py')
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successful query | list of Pandas DataFrames | N/A |
| Fail: Database name is not valid | N/A | A database with the given name does not appear to exist. Check the specified value. |
| Fail: Database with given name is not found | N/A | Check the name of the database you are searching for as it does not seem to exist. |
| Fail: Table name is not valid | N/A | Provide a valid symbol for the table name. |
| Fail: Table with given name is not found | N/A | A table with the given name doesn't exist. Double check the supplied value. |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure KDB.AI server running') | Check your connection and if your server is running. |

### Update data

`table.update_data`

Update one or more rows of data in a table.

**Input parameters**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | The name of the database. | Yes |
| table | symbol | The name of the table. | Yes |
| filter | list of tuples | List of filter conditions parse-tree style. | No |
| columns | dictionary | Columns to update. Each key represents a column name, and the corresponding value can be either: • A single value (applied to all rows), or • A list of values (length must match number of rows being updated). | Yes |

Example:

```
db = session.database("default")
table = db.table("myTable")
table.update_data(columns={'sym':'Vod.l'}, filter=[['=','sym','AAC.l']])
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

`table.delete_data`

Delete data from a table.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | The name of the database. | Yes |
| table | symbol | The name of the table. | Yes |
| filter | list of tuples | List of filter conditions parse-tree style. | No |

Example:

```
db = session.database("default")
table = db.table("trade")
table.delete_data(filter=[["=", "Date", "2025.05.14"], ["=", "sym", "Vod.l"]]))
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

`table.info`

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | The name of the database. | Yes |
| table | symbol | The name of the table. | Yes |

Example:

```
db = session.database("default")
table = db.table("table1")
table.info()
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successfully returns table info | Dictionary of table info | N/A |
| Fail: Table name does not exist | `success`result`error!0b;();"table {name} does not exist" | Check the name of the table as it does not seem to exist. |
| Fail: Database does not exist | `success`result`error!0b;();"database {name} does not exist" | Check the name of the database as it does not seem to exist. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

### Get database info

`database.info`

Get database info, including table info of each table in the database.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | The name of the database. | Yes |

Example:

```
db = session.database("default")
db.info()
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successfully returns database info | List of dictionaries containing database info and table info within that database | N/A |
| Fail: Database does not exist | N/A | Check the name of the database as it does not seem to exist. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

### Get all databases info

`session.databases_info`

Get all databases info, including table info of all tables in all databases.

**Input parameters:**

N/A

Example:

```
session = kdbai.Session(endpoint='http://localhost:8082')
session.databases_info()
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successfully returns all databases info | List of dictionaries containing databases info, including info about each databases and the tables within each database | N/A |
| Fail: Databases don't exist | N/A | No databases exist. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

### Get session info

`session.session_info`

**Input parameters:**

N/A

Example:

```
session = kdbai.Session(endpoint='http://localhost:8082')
session.session_info()
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successfully returns the number of sessions and when they started | Dictionary of session info | N/A |
| Fail: No sessions have been created | `success`result`error!0b;();"sessions do not exist" | No sessions exist. |
| Error: KDBAI is not available | Cannot write to handle ... | Check your connection and if your server is running. |

* * *

### Get process info

`session.process_info`

**Input parameters:**

N/A

Example:

```
session = kdbai.Session(endpoint='http://localhost:8082')
session.process_info()
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successfully returns process info | List of dictionaries of process info | N/A |
| Fail: Cannot retrieve process information due to internal server issue | N/A |  |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure Home - KDB.AI server running' | Check your connection and if your server is running. |

* * *

### Get system info

`session.system_info`

**Input parameters:**

N/A

Example:

```
session = kdbai.Session(endpoint='http://localhost:8082')
session.system_info()
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successfully returns system info | List of dictionaries including system info, process info, sessions info, database and table info in the system | N/A |
| Fail: Cannot retrieve system information due to internal server issue | N/A |  |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure Home - KDB.AI server running') | Check your connection and if your server is running. |

ACL Grants
----------

Add, list, get, and delete ACL grants.

### Add grants

`session.admin.add_grants`

Add one or more ACL grants.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| resource | str | Grant resource name (database, table, admin) | Yes | None |
| databaseName | str | The name of the database | Yes | None |
| table | str | The name of the table (mandatory for table resource) | No | None |
| tenant | symbol | Tenant ID from IdP provider | Yes | None |
| groups | list of str | User group names from IdP provider | Yes | None |
| actions | list of str | Actions to set — read/write/delete/system_admin | Yes | None |

Example:

```
session = kdbai.Session(oauth=<oauth_config_details>)
session.admin.add_grants([{'resource':'database','tenant':'quants','groups':'quants_read','databaseName':'default','actions':'read'}]
```

Error handling:

| **Description** | **Message** | **Troubleshooting** |
| --- | --- | --- |
| Success: Successful update | None | N/A |
| Fail: Wrong values length | N/A | - If applying the same value to all rows, provide a **scalar value**, not a list. - If using a list of values, make sure its **length matches** the number of rows that meet the `filter` condition. - Verify that your `filter` expression returns the expected number of rows before updating. |
| Fail: Wrong values types | N/A | - Check the **table schema** to confirm the expected q types for each column. - Make sure the values in your `columns` dictionary use the correct types. - Remember that q distinguishes between types such as `symbol`, `char`, `int`, and `float`. |
| Fail: Invalid column name | N/A | A column with the given name does not appear to exist. Please, check the specified value. |
| Fail: Index is not supported | N/A | Ensure that you are performing updates only on tables with **no index** or the **supported index types** (`flat`, `qFlat`, `hnsw`, or `qHnsw`) |
| Fail: Database name is not valid | N/A | A database with the given name does not appear to exist. Check the specified value. |
| Fail: Database with given name is not found | N/A | A database with the given name does not appear to exist. Check the specified value. |
| Fail: Table name is not valid | N/A | The table name is invalid. Provide a valid symbol for the table name. |
| Fail: Table with given name is not found | N/A | A table with the given name was not found. Double check the supplied value. |
| Error: KDBAI is not available | RuntimeError('Error during request, make sure KDB.AI server running') | Check your connection and if your server is running. |

### Get all grants

`session.admin.get_all_grants`

Get all ACL grants.

Example:

```
session = kdbai.Session(oauth=<oauth_config_details>)
session.admin.get_all_grants()
```

### Get grant for id

`session.admin.get_grant_by_id`

Get ACL grant for given grant id.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| id | str | Grant id. | Yes | None |

Example:

```
session = kdbai.Session(oauth=<oauth_config_details>)
session.admin.get_grant_by_id("test")
```

### Delete grant

`session.admin.delete_grant`

Delete ACL grant for given id.

**Input parameters:**

| **Name** | **Type** | **Description** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| id | str | Grant id. | Yes | None |

Example:

```
session = kdbai.Session(oauth=<oauth_config_details>)
session.admin.delete_grant("test")
```
