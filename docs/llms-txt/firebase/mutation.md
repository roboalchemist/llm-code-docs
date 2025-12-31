# Source: https://firebase.google.com/docs/reference/data-connect/gql/mutation.md.txt

This reference doc is generated based on this[example schema](https://firebase.google.com/docs/reference/data-connect#graphql_schema).

Mutations define the write operations for modifying data in a GraphQL schema.

All mutations are generated based on customer defined[`@table`](https://firebase.google.com/docs/reference/data-connect/gql/directive#table)types. Customer defined mutations are not supported.

## Data Connect Generated

### mainTable_delete:[`MainTable_KeyOutput`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#MainTable_KeyOutput)

â¨ Delete a single[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)based on`id`,`key`or`first`and return its key (or`null`if not found).

|  Field  |                                                        Type                                                         |                      Description                       |
|---------|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `id`    | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                   | The unique ID of the object.                           |
| `key`   | [`MainTable_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Key)           | The key used to identify the object.                   |
| `first` | [`MainTable_FirstRow`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_FirstRow) | Fetch the first row based on the filters and ordering. |

### mainTable_deleteMany:[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)

â¨ Delete[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)objects matching`where`conditions (or`all`, if true). Returns the number of rows deleted.

|  Field  |                                                      Type                                                       |                    Description                    |
|---------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| `where` | [`MainTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Filter) | Filter condition to specify which rows to delete. |
| `all`   | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                         | Set to true to delete all rows.                   |

### mainTable_insert:[`MainTable_KeyOutput!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#MainTable_KeyOutput)

â¨ Insert a single[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)into the table and return its key. Columns not specified in`data`will receive defaults (e.g.`null`).

| Field  |                                                     Type                                                     |              Description              |
|--------|--------------------------------------------------------------------------------------------------------------|---------------------------------------|
| `data` | [`MainTable_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Data) | Data object to insert into the table. |

### mainTable_insertMany:[`[MainTable_KeyOutput!]!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#MainTable_KeyOutput)

â¨ Insert[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)objects into the table and return their keys. Columns not specified in`data`will receive defaults (e.g.`null`).

| Field  |                                                      Type                                                       |                  Description                   |
|--------|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| `data` | [`[MainTable_Data!]!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Data) | List of data objects to insert into the table. |

### mainTable_update:[`MainTable_KeyOutput`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#MainTable_KeyOutput)

â¨ Update a single[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)based on`id`,`key`or`first`, setting columns specified in`data`. Returns the key of the updated[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)or`null`if not found.

|  Field  |                                                        Type                                                         |                      Description                       |
|---------|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `id`    | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                   | The unique ID of the object.                           |
| `key`   | [`MainTable_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Key)           | The key used to identify the object.                   |
| `first` | [`MainTable_FirstRow`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_FirstRow) | Fetch the first row based on the filters and ordering. |
| `data`  | [`MainTable_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Data)        | Data object containing fields to be updated.           |

### mainTable_updateMany:[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)

â¨ Update[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)objects matching`where`conditions (or`all`, if true) according to`data`. Returns the number of rows updated.

|  Field  |                                                      Type                                                       |                    Description                    |
|---------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| `where` | [`MainTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Filter) | Filter condition to specify which rows to update. |
| `all`   | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                         | Set to true to update all rows.                   |
| `data`  | [`MainTable_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Data)    | Data object containing fields to update.          |

### mainTable_upsert:[`MainTable_KeyOutput!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#MainTable_KeyOutput)

â¨ Insert or update a single[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)into the table, based on the primary key. Returns the key of the newly inserted or existing updated[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).

| Field  |                                                     Type                                                     |                      Description                      |
|--------|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `data` | [`MainTable_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Data) | Data object to insert or update if it already exists. |

### mainTable_upsertMany:[`[MainTable_KeyOutput!]!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#MainTable_KeyOutput)

â¨ Insert or update[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)objects into the table, based on the primary key. Returns the key of the newly inserted or existing updated[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).

| Field  |                                                      Type                                                       |                          Description                           |
|--------|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| `data` | [`[MainTable_Data!]!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Data) | List of data objects to insert or update if it already exists. |

### manyToManyJoinTable_delete:[`ManyToManyJoinTable_KeyOutput`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#ManyToManyJoinTable_KeyOutput)

â¨ Delete a single[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable)based on`id`,`key`or`first`and return its key (or`null`if not found).

|  Field  |                                                                  Type                                                                   |                      Description                       |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `key`   | [`ManyToManyJoinTable_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Key)           | The key used to identify the object.                   |
| `first` | [`ManyToManyJoinTable_FirstRow`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_FirstRow) | Fetch the first row based on the filters and ordering. |

### manyToManyJoinTable_deleteMany:[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)

â¨ Delete[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable)objects matching`where`conditions (or`all`, if true). Returns the number of rows deleted.

|  Field  |                                                                Type                                                                 |                    Description                    |
|---------|-------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| `where` | [`ManyToManyJoinTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Filter) | Filter condition to specify which rows to delete. |
| `all`   | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                                             | Set to true to delete all rows.                   |

### manyToManyJoinTable_insert:[`ManyToManyJoinTable_KeyOutput!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#ManyToManyJoinTable_KeyOutput)

â¨ Insert a single[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable)into the table and return its key. Columns not specified in`data`will receive defaults (e.g.`null`).

| Field  |                                                               Type                                                               |              Description              |
|--------|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| `data` | [`ManyToManyJoinTable_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Data) | Data object to insert into the table. |

### manyToManyJoinTable_insertMany:[`[ManyToManyJoinTable_KeyOutput!]!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#ManyToManyJoinTable_KeyOutput)

â¨ Insert[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable)objects into the table and return their keys. Columns not specified in`data`will receive defaults (e.g.`null`).

| Field  |                                                                Type                                                                 |                  Description                   |
|--------|-------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| `data` | [`[ManyToManyJoinTable_Data!]!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Data) | List of data objects to insert into the table. |

### manyToManyJoinTable_update:[`ManyToManyJoinTable_KeyOutput`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#ManyToManyJoinTable_KeyOutput)

â¨ Update a single[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable)based on`id`,`key`or`first`, setting columns specified in`data`. Returns the key of the updated[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable)or`null`if not found.

|  Field  |                                                                  Type                                                                   |                      Description                       |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `key`   | [`ManyToManyJoinTable_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Key)           | The key used to identify the object.                   |
| `first` | [`ManyToManyJoinTable_FirstRow`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_FirstRow) | Fetch the first row based on the filters and ordering. |
| `data`  | [`ManyToManyJoinTable_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Data)        | Data object containing fields to be updated.           |

### manyToManyJoinTable_updateMany:[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)

â¨ Update[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable)objects matching`where`conditions (or`all`, if true) according to`data`. Returns the number of rows updated.

|  Field  |                                                                Type                                                                 |                    Description                    |
|---------|-------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| `where` | [`ManyToManyJoinTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Filter) | Filter condition to specify which rows to update. |
| `all`   | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                                             | Set to true to update all rows.                   |
| `data`  | [`ManyToManyJoinTable_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Data)    | Data object containing fields to update.          |

### manyToManyJoinTable_upsert:[`ManyToManyJoinTable_KeyOutput!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#ManyToManyJoinTable_KeyOutput)

â¨ Insert or update a single[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable)into the table, based on the primary key. Returns the key of the newly inserted or existing updated[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).

| Field  |                                                               Type                                                               |                      Description                      |
|--------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `data` | [`ManyToManyJoinTable_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Data) | Data object to insert or update if it already exists. |

### manyToManyJoinTable_upsertMany:[`[ManyToManyJoinTable_KeyOutput!]!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#ManyToManyJoinTable_KeyOutput)

â¨ Insert or update[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable)objects into the table, based on the primary key. Returns the key of the newly inserted or existing updated[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).

| Field  |                                                                Type                                                                 |                          Description                           |
|--------|-------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| `data` | [`[ManyToManyJoinTable_Data!]!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Data) | List of data objects to insert or update if it already exists. |

### manyToOneExample_delete:[`ManyToOneExample_KeyOutput`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#ManyToOneExample_KeyOutput)

â¨ Delete a single[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample)based on`id`,`key`or`first`and return its key (or`null`if not found).

|  Field  |                                                               Type                                                                |                      Description                       |
|---------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `id`    | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                                 | The unique ID of the object.                           |
| `key`   | [`ManyToOneExample_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Key)           | The key used to identify the object.                   |
| `first` | [`ManyToOneExample_FirstRow`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_FirstRow) | Fetch the first row based on the filters and ordering. |

### manyToOneExample_deleteMany:[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)

â¨ Delete[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample)objects matching`where`conditions (or`all`, if true). Returns the number of rows deleted.

|  Field  |                                                             Type                                                              |                    Description                    |
|---------|-------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| `where` | [`ManyToOneExample_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Filter) | Filter condition to specify which rows to delete. |
| `all`   | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                                       | Set to true to delete all rows.                   |

### manyToOneExample_insert:[`ManyToOneExample_KeyOutput!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#ManyToOneExample_KeyOutput)

â¨ Insert a single[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample)into the table and return its key. Columns not specified in`data`will receive defaults (e.g.`null`).

| Field  |                                                            Type                                                            |              Description              |
|--------|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| `data` | [`ManyToOneExample_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Data) | Data object to insert into the table. |

### manyToOneExample_insertMany:[`[ManyToOneExample_KeyOutput!]!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#ManyToOneExample_KeyOutput)

â¨ Insert[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample)objects into the table and return their keys. Columns not specified in`data`will receive defaults (e.g.`null`).

| Field  |                                                             Type                                                              |                  Description                   |
|--------|-------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| `data` | [`[ManyToOneExample_Data!]!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Data) | List of data objects to insert into the table. |

### manyToOneExample_update:[`ManyToOneExample_KeyOutput`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#ManyToOneExample_KeyOutput)

â¨ Update a single[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample)based on`id`,`key`or`first`, setting columns specified in`data`. Returns the key of the updated[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample)or`null`if not found.

|  Field  |                                                               Type                                                                |                      Description                       |
|---------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `id`    | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                                 | The unique ID of the object.                           |
| `key`   | [`ManyToOneExample_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Key)           | The key used to identify the object.                   |
| `first` | [`ManyToOneExample_FirstRow`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_FirstRow) | Fetch the first row based on the filters and ordering. |
| `data`  | [`ManyToOneExample_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Data)        | Data object containing fields to be updated.           |

### manyToOneExample_updateMany:[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)

â¨ Update[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample)objects matching`where`conditions (or`all`, if true) according to`data`. Returns the number of rows updated.

|  Field  |                                                             Type                                                              |                    Description                    |
|---------|-------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| `where` | [`ManyToOneExample_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Filter) | Filter condition to specify which rows to update. |
| `all`   | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                                       | Set to true to update all rows.                   |
| `data`  | [`ManyToOneExample_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Data)    | Data object containing fields to update.          |

### manyToOneExample_upsert:[`ManyToOneExample_KeyOutput!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#ManyToOneExample_KeyOutput)

â¨ Insert or update a single[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample)into the table, based on the primary key. Returns the key of the newly inserted or existing updated[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).

| Field  |                                                            Type                                                            |                      Description                      |
|--------|----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `data` | [`ManyToOneExample_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Data) | Data object to insert or update if it already exists. |

### manyToOneExample_upsertMany:[`[ManyToOneExample_KeyOutput!]!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#ManyToOneExample_KeyOutput)

â¨ Insert or update[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample)objects into the table, based on the primary key. Returns the key of the newly inserted or existing updated[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).

| Field  |                                                             Type                                                              |                          Description                           |
|--------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| `data` | [`[ManyToOneExample_Data!]!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Data) | List of data objects to insert or update if it already exists. |

### oneToOneExample_delete:[`OneToOneExample_KeyOutput`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#OneToOneExample_KeyOutput)

â¨ Delete a single[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample)based on`id`,`key`or`first`and return its key (or`null`if not found).

|  Field  |                                                              Type                                                               |                      Description                       |
|---------|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `id`    | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                               | The unique ID of the object.                           |
| `key`   | [`OneToOneExample_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Key)           | The key used to identify the object.                   |
| `first` | [`OneToOneExample_FirstRow`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_FirstRow) | Fetch the first row based on the filters and ordering. |

### oneToOneExample_deleteMany:[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)

â¨ Delete[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample)objects matching`where`conditions (or`all`, if true). Returns the number of rows deleted.

|  Field  |                                                            Type                                                             |                    Description                    |
|---------|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| `where` | [`OneToOneExample_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Filter) | Filter condition to specify which rows to delete. |
| `all`   | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                                     | Set to true to delete all rows.                   |

### oneToOneExample_insert:[`OneToOneExample_KeyOutput!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#OneToOneExample_KeyOutput)

â¨ Insert a single[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample)into the table and return its key. Columns not specified in`data`will receive defaults (e.g.`null`).

| Field  |                                                           Type                                                           |              Description              |
|--------|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| `data` | [`OneToOneExample_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Data) | Data object to insert into the table. |

### oneToOneExample_insertMany:[`[OneToOneExample_KeyOutput!]!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#OneToOneExample_KeyOutput)

â¨ Insert[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample)objects into the table and return their keys. Columns not specified in`data`will receive defaults (e.g.`null`).

| Field  |                                                            Type                                                             |                  Description                   |
|--------|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| `data` | [`[OneToOneExample_Data!]!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Data) | List of data objects to insert into the table. |

### oneToOneExample_update:[`OneToOneExample_KeyOutput`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#OneToOneExample_KeyOutput)

â¨ Update a single[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample)based on`id`,`key`or`first`, setting columns specified in`data`. Returns the key of the updated[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample)or`null`if not found.

|  Field  |                                                              Type                                                               |                      Description                       |
|---------|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `id`    | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                               | The unique ID of the object.                           |
| `key`   | [`OneToOneExample_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Key)           | The key used to identify the object.                   |
| `first` | [`OneToOneExample_FirstRow`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_FirstRow) | Fetch the first row based on the filters and ordering. |
| `data`  | [`OneToOneExample_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Data)        | Data object containing fields to be updated.           |

### oneToOneExample_updateMany:[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)

â¨ Update[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample)objects matching`where`conditions (or`all`, if true) according to`data`. Returns the number of rows updated.

|  Field  |                                                            Type                                                             |                    Description                    |
|---------|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| `where` | [`OneToOneExample_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Filter) | Filter condition to specify which rows to update. |
| `all`   | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                                     | Set to true to update all rows.                   |
| `data`  | [`OneToOneExample_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Data)    | Data object containing fields to update.          |

### oneToOneExample_upsert:[`OneToOneExample_KeyOutput!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#OneToOneExample_KeyOutput)

â¨ Insert or update a single[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample)into the table, based on the primary key. Returns the key of the newly inserted or existing updated[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).

| Field  |                                                           Type                                                           |                      Description                      |
|--------|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `data` | [`OneToOneExample_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Data) | Data object to insert or update if it already exists. |

### oneToOneExample_upsertMany:[`[OneToOneExample_KeyOutput!]!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#OneToOneExample_KeyOutput)

â¨ Insert or update[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample)objects into the table, based on the primary key. Returns the key of the newly inserted or existing updated[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).

| Field  |                                                            Type                                                             |                          Description                           |
|--------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| `data` | [`[OneToOneExample_Data!]!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Data) | List of data objects to insert or update if it already exists. |

### stringTable_delete:[`StringTable_KeyOutput`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#StringTable_KeyOutput)

â¨ Delete a single[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable)based on`id`,`key`or`first`and return its key (or`null`if not found).

|  Field  |                                                          Type                                                           |                      Description                       |
|---------|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `id`    | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                       | The unique ID of the object.                           |
| `key`   | [`StringTable_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Key)           | The key used to identify the object.                   |
| `first` | [`StringTable_FirstRow`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_FirstRow) | Fetch the first row based on the filters and ordering. |

### stringTable_deleteMany:[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)

â¨ Delete[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable)objects matching`where`conditions (or`all`, if true). Returns the number of rows deleted.

|  Field  |                                                        Type                                                         |                    Description                    |
|---------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| `where` | [`StringTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Filter) | Filter condition to specify which rows to delete. |
| `all`   | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                             | Set to true to delete all rows.                   |

### stringTable_insert:[`StringTable_KeyOutput!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#StringTable_KeyOutput)

â¨ Insert a single[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable)into the table and return its key. Columns not specified in`data`will receive defaults (e.g.`null`).

| Field  |                                                       Type                                                       |              Description              |
|--------|------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| `data` | [`StringTable_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Data) | Data object to insert into the table. |

### stringTable_insertMany:[`[StringTable_KeyOutput!]!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#StringTable_KeyOutput)

â¨ Insert[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable)objects into the table and return their keys. Columns not specified in`data`will receive defaults (e.g.`null`).

| Field  |                                                        Type                                                         |                  Description                   |
|--------|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| `data` | [`[StringTable_Data!]!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Data) | List of data objects to insert into the table. |

### stringTable_update:[`StringTable_KeyOutput`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#StringTable_KeyOutput)

â¨ Update a single[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable)based on`id`,`key`or`first`, setting columns specified in`data`. Returns the key of the updated[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable)or`null`if not found.

|  Field  |                                                          Type                                                           |                      Description                       |
|---------|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `id`    | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                       | The unique ID of the object.                           |
| `key`   | [`StringTable_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Key)           | The key used to identify the object.                   |
| `first` | [`StringTable_FirstRow`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_FirstRow) | Fetch the first row based on the filters and ordering. |
| `data`  | [`StringTable_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Data)        | Data object containing fields to be updated.           |

### stringTable_updateMany:[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)

â¨ Update[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable)objects matching`where`conditions (or`all`, if true) according to`data`. Returns the number of rows updated.

|  Field  |                                                        Type                                                         |                    Description                    |
|---------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| `where` | [`StringTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Filter) | Filter condition to specify which rows to update. |
| `all`   | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                             | Set to true to update all rows.                   |
| `data`  | [`StringTable_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Data)    | Data object containing fields to update.          |

### stringTable_upsert:[`StringTable_KeyOutput!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#StringTable_KeyOutput)

â¨ Insert or update a single[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable)into the table, based on the primary key. Returns the key of the newly inserted or existing updated[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).

| Field  |                                                       Type                                                       |                      Description                      |
|--------|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `data` | [`StringTable_Data!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Data) | Data object to insert or update if it already exists. |

### stringTable_upsertMany:[`[StringTable_KeyOutput!]!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#StringTable_KeyOutput)

â¨ Insert or update[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable)objects into the table, based on the primary key. Returns the key of the newly inserted or existing updated[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).

| Field  |                                                        Type                                                         |                          Description                           |
|--------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| `data` | [`[StringTable_Data!]!`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Data) | List of data objects to insert or update if it already exists. |