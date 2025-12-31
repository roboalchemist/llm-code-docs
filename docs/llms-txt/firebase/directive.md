# Source: https://firebase.google.com/docs/reference/data-connect/gql/directive.md.txt

This reference doc is generated based on this[example schema](https://firebase.google.com/docs/reference/data-connect#graphql_schema).

Directives define specific behaviors that can be applied to fields or types within Data Connect schema and connectors.

Data Connect defines GraphQL directives to map schema to SQL tables and customize behavior of queries and mutations.

## Data Connect Defined

### @auth on`QUERY`\|`MUTATION`

The[`@auth`](https://firebase.google.com/docs/reference/data-connect/gql/directive#auth)directive defines the authentication policy for a query or mutation.

It must be added to any operation that you wish to be accessible from a client application. If not specified, the operation defaults to`@auth(level: NO_ACCESS)`.

Refer to[Data Connect Auth Guide](https://firebase.google.com/docs/data-connect/authorization-and-security)for the best practices.

|     Argument     |                                               Type                                                |                                                                                                                                                                                                                                                              Description                                                                                                                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `level`          | [`AccessLevel`](https://firebase.google.com/docs/reference/data-connect/gql/enum#AccessLevel)     | The minimal level of access required to perform this operation. Exactly one of`level`and`expr`should be specified.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `expr`           | [`Boolean_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean_Expr) | A CEL expression that grants access to this operation if the expression evaluates to`true`. Exactly one of`level`and`expr`should be specified.                                                                                                                                                                                                                                                                                                                                                                                         |
| `insecureReason` | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)             | If the[`@auth`](https://firebase.google.com/docs/reference/data-connect/gql/directive#auth)on this operation is considered insecure, then developer acknowledgement is required to deploy this operation, for new operations.[`@auth`](https://firebase.google.com/docs/reference/data-connect/gql/directive#auth)is considered insecure if`level: PUBLIC`, or if`level: USER/USER_ANON/USER_EMAIL_VERIFIED`and`auth.uid`is not referenced in the operation. If`insecureReason`is set, no further developer acknowledgement is needed. |

### @check on`QUERY`\|`MUTATION`\|`FIELD`\|`FRAGMENT_DEFINITION`\|`FRAGMENT_SPREAD`\|`INLINE_FRAGMENT`

Ensure this field is present and is not null or`[]`, or abort the request / transaction.

A CEL expression,`expr`is used to test the field value. It defaults to rejecting null and`[]`but a custom expression can be provided instead.

If the field occurs multiple times (i.e. directly or indirectly nested under a list),`expr`will be executed once for each occurrence and[`@check`](https://firebase.google.com/docs/reference/data-connect/gql/directive#check)succeeds if all values succeed.[`@check`](https://firebase.google.com/docs/reference/data-connect/gql/directive#check)fails when the field is not present at all (i.e. all ancestor paths contain`null`or`[]`), unless`optional`is true.

If a[`@check`](https://firebase.google.com/docs/reference/data-connect/gql/directive#check)fails in a mutation, the top-level field containing it will be replaced with a partial error, whose message can be customzied via the`message`argument. Each subsequent top-level fields will return an aborted error (i.e. not executed). To rollback previous steps, see[`@transaction`](https://firebase.google.com/docs/reference/data-connect/gql/directive#transaction).

|  Argument  |                                                Type                                                |                                                                                                                                                                                                                                                                                                                                                             Description                                                                                                                                                                                                                                                                                                                                                             |
|------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `expr`     | [`Boolean_Expr!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean_Expr) | The CEL expression to test the field value (or values if nested under a list). Within the CEL expression, a special value`this`evaluates to the field that this directive is attached to. If this field occurs multiple times because any ancestor is a list, each occurrence is tested with`this`bound to each value. When the field itself is a list or object,`this`follows the same structure (including all descendants selected in case of objects). For any given path, if an ancestor is`null`or`[]`, the field will not be reached and the CEL evaluation will be skipped for that path. In other words, evaluation only takes place when`this`is`null`or non-null, but never undefined. (See also the`optional`argument.) |
| `message`  | [`String!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)             | The error message to return to the client if the check fails. Defaults to "permission denied" if not specified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `optional` | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)            | Whether the check should pass or fail (default) when the field is not present. A field will not be reached at a given path if its parent or any ancestor is`[]`or`null`. When this happens to all paths, the field will not be present anywhere in the response tree. In other words,`expr`is evaluated 0 times. By default, @check will automatically fail in this case. Set this argument to`true`to make it pass even if no tests are run (a.k.a. "vacuously true").                                                                                                                                                                                                                                                             |

### @col on`FIELD_DEFINITION`

Customizes a field that represents a SQL database table column.

Data Connect maps scalar Fields on[`@table`](https://firebase.google.com/docs/reference/data-connect/gql/directive#table)type to a SQL column of corresponding data type.

- scalar[`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)maps to[`uuid`](https://www.postgresql.org/docs/current/datatype-uuid.html).
- scalar[`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)maps to[`text`](https://www.postgresql.org/docs/current/datatype-character.html).
- scalar[`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)maps to[`int`](https://www.postgresql.org/docs/current/datatype-numeric.html).
- scalar[`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)maps to[`bigint`](https://www.postgresql.org/docs/current/datatype-numeric.html).
- scalar[`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)maps to[`double precision`](https://www.postgresql.org/docs/current/datatype-numeric.html).
- scalar[`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)maps to[`boolean`](https://www.postgresql.org/docs/current/datatype-boolean.html).
- scalar[`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)maps to[`date`](https://www.postgresql.org/docs/current/datatype-datetime.html).
- scalar[`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)maps to[`timestamptz`](https://www.postgresql.org/docs/current/datatype-datetime.html).
- scalar[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)maps to[`jsonb`](https://www.postgresql.org/docs/current/datatype-json.html).
- scalar[`Vector`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector)maps to[`pgvector`](https://github.com/pgvector/pgvector).

Array scalar fields are mapped to[Postgres arrays](https://www.postgresql.org/docs/current/arrays.html).

###### Example: Serial Primary Key

For example, you can define auto-increment primary key.  

    type Post @table {
      id: Int! @col(name: "post_id", dataType: "serial")
    }

Data Connect converts it to the following SQL table schema.  

    CREATE TABLE "public"."post" (
      "post_id" serial NOT NULL,
      PRIMARY KEY ("id")
    )

###### Example: Vector

    type Post @table {
      content: String! @col(name: "post_content")
      contentEmbedding: Vector! @col(size:768)
    }

|  Argument  |                                         Type                                          |                                                                                                                                           Description                                                                                                                                           |
|------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`     | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | The SQL database column name. Defaults to snake_case of the field name.                                                                                                                                                                                                                         |
| `dataType` | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | Configures the custom SQL data type. Each GraphQL type can map to multiple SQL data types. Refer to[Postgres supported data types](https://www.postgresql.org/docs/current/datatype.html). Incompatible SQL data type will lead to undefined behavior.                                          |
| `size`     | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)       | Required on[`Vector`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector)columns. It specifies the length of the Vector.`textembedding-gecko@003`model generates[`Vector`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector)of`@col(size:768)`. |

### @default on`FIELD_DEFINITION`

Specifies the default value for a column field.

For example:  

    type User @table(key: "uid") {
      uid: String! @default(expr: "auth.uid")
      number: Int! @col(dataType: "serial")
      createdAt: Date! @default(expr: "request.time")
      role: String! @default(value: "Member")
      credit: Int! @default(value: 100)
    }

The supported arguments vary based on the field type.

| Argument |                                           Type                                            |                                                                                                                                                                                       Description                                                                                                                                                                                       |
|----------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `value`  | [`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)           | A constant value validated against the field's GraphQL type during compilation.                                                                                                                                                                                                                                                                                                         |
| `expr`   | [`Any_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any_Expr) | A CEL expression whose return value must match the field's data type.                                                                                                                                                                                                                                                                                                                   |
| `sql`    | [`Any_SQL`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any_SQL)   | A raw SQL expression, whose SQL data type must match the underlying column. The value is any variable-free expression (in particular, cross-references to other columns in the current table are not allowed). Subqueries are not allowed either. See[PostgreSQL defaults](https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-PARMS-DEFAULT)for more details. |

### @index on`FIELD_DEFINITION`\|`OBJECT`

Defines a database index to optimize query performance.  

    type User @table @index(fields: ["name", "phoneNumber"], order: [ASC, DESC]) {
        name: String @index
        phoneNumber: Int64 @index
        tags: [String] @index # GIN Index
    }

##### Single Field Index

You can put[`@index`](https://firebase.google.com/docs/reference/data-connect/gql/directive#index)on a[`@col`](https://firebase.google.com/docs/reference/data-connect/gql/directive#col)field to create a SQL index.

`@index(order)`matters little for single field indexes, as they can be scanned in both directions.

##### Composite Index

You can put`@index(fields: [...])`on[`@table`](https://firebase.google.com/docs/reference/data-connect/gql/directive#table)type to define composite indexes.

`@index(order: [...])`can customize the index order to satisfy particular filter and order requirement.

|    Argument     |                                                        Type                                                         |                                                                                                                                                                  Description                                                                                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`          | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                               | Configure the SQL database index id. If not overridden, Data Connect generates the index name: -`{table_name}_{first_field}_{second_field}_aa_idx`-`{table_name}_{field_name}_idx`                                                                                                                                                             |
| `fields`        | [`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                            | Only allowed and required when used on a[`@table`](https://firebase.google.com/docs/reference/data-connect/gql/directive#table)type. Specifies the fields to create the index on.                                                                                                                                                              |
| `order`         | [`[IndexFieldOrder!]`](https://firebase.google.com/docs/reference/data-connect/gql/enum#IndexFieldOrder)            | Only allowed for`BTREE`[`@index`](https://firebase.google.com/docs/reference/data-connect/gql/directive#index)on[`@table`](https://firebase.google.com/docs/reference/data-connect/gql/directive#table)type. Specifies the order for each indexed column. Defaults to all`ASC`.                                                                |
| `type`          | [`IndexType`](https://firebase.google.com/docs/reference/data-connect/gql/enum#IndexType)                           | Customize the index type. For most index, it defaults to`BTREE`. For array fields, only allowed[`IndexType`](https://firebase.google.com/docs/reference/data-connect/gql/enum#IndexType)is`GIN`. For[`Vector`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector)fields, defaults to`HNSW`, may configure to`IVFFLAT`. |
| `vector_method` | [`VectorSimilarityMethod`](https://firebase.google.com/docs/reference/data-connect/gql/enum#VectorSimilarityMethod) | Only allowed when used on vector field. Defines the vector similarity method. Defaults to`INNER_PRODUCT`.                                                                                                                                                                                                                                      |

### @redact on`FIELD`\|`FRAGMENT_SPREAD`\|`INLINE_FRAGMENT`

Redact a part of the response from the client.

Redacted fields are still evaluated for side effects (including data changes and[`@check`](https://firebase.google.com/docs/reference/data-connect/gql/directive#check)) and the results are still available to later steps in CEL expressions (via`response.fieldName`).

### @ref on`FIELD_DEFINITION`

Defines a foreign key reference to another table.

For example, we can define a many-to-one relation.  

    type ManyTable @table {
      refField: OneTable!
    }
    type OneTable @table {
      someField: String!
    }

Data Connect adds implicit foreign key column and relation query field. So the above schema is equivalent to the following schema.  

    type ManyTable @table {
      id: UUID! @default(expr: "uuidV4()")
      refField: OneTable! @ref(fields: "refFieldId", references: "id")
      refFieldId: UUID!
    }
    type OneTable @table {
      id: UUID! @default(expr: "uuidV4()")
      someField: UUID!
      # Generated Fields:
      # manyTables_on_refField: [ManyTable!]!
    }

Data Connect generates the necessary foreign key constraint.  

    CREATE TABLE "public"."many_table" (
      "id" uuid NOT NULL DEFAULT uuid_generate_v4(),
      "ref_field_id" uuid NOT NULL,
      PRIMARY KEY ("id"),
      CONSTRAINT "many_table_ref_field_id_fkey" FOREIGN KEY ("ref_field_id") REFERENCES "public"."one_table" ("id") ON DELETE CASCADE
    )

###### Example: Traverse the Reference Field

    query ($id: UUID!) {
      manyTable(id: $id) {
        refField { id }
      }
    }

###### Example: Reverse Traverse the Reference field

    query ($id: UUID!) {
      oneTable(id: $id) {
        manyTables_on_refField { id }
      }
    }

##### Optional Many-to-One Relation

An optional foreign key reference will be set to null if the referenced row is deleted.

In this example, if a`User`is deleted, the`assignee`and`reporter`references will be set to null.  

    type Bug @table {
      title: String!
      assignee: User
      reproter: User
    }

    type User @table { name: String!  }

##### Required Many-to-One Relation

A required foreign key reference will cascade delete if the referenced row is deleted.

In this example, if a`Post`is deleted, associated comments will also be deleted.  

    type Comment @table {
      post: Post!
      content: String!
    }

    type Post @table { title: String!  }

##### Many To Many Relation

You can define a many-to-many relation with a join table.  

    type Membership @table(key: ["group", "user"]) {
      group: Group!
      user: User!
      role: String! @default(value: "member")
    }

    type Group @table { name: String! }
    type User @table { name: String! }

When Data Connect sees a table with two reference field as its primary key, it knows this is a join table, so expands the many-to-many query field.  

    type Group @table {
      name: String!
      # Generated Fields:
      # users_via_Membership: [User!]!
      # memberships_on_group: [Membership!]!
    }
    type User @table {
      name: String!
      # Generated Fields:
      # groups_via_Membership: [Group!]!
      # memberships_on_user: [Membership!]!
    }

###### Example: Traverse the Many-To-Many Relation

    query ($id: UUID!) {
      group(id: $id) {
        users: users_via_Membership {
          name
        }
      }
    }

###### Example: Traverse to the Join Table

    query ($id: UUID!) {
      group(id: $id) {
        memberships: memberships_on_group {
          user { name }
          role
        }
      }
    }

##### One To One Relation

You can even define a one-to-one relation with the help of[`@unique`](https://firebase.google.com/docs/reference/data-connect/gql/directive#unique)or`@table(key)`.  

    type User @table {
      name: String
    }
    type Account @table {
      user: User! @unique
    }
    # Alternatively, use primary key constraint.
    # type Account @table(key: "user") {
    #   user: User!
    # }

###### Example: Transerse the Reference Field

    query ($id: UUID!) {
      account(id: $id) {
        user { id }
      }
    }

###### Example: Reverse Traverse the Reference field

    query ($id: UUID!) {
      user(id: $id) {
        account_on_user { id }
      }
    }

##### Customizations

- `@ref(constraintName)`can customize the SQL foreign key constraint name (`table_name_ref_field_fkey`above).
- `@ref(fields)`can customize the foreign key field names.
- `@ref(references)`can customize the constraint to reference other columns. By default,`@ref(references)`is the primary key of the[`@ref`](https://firebase.google.com/docs/reference/data-connect/gql/directive#ref)table. Other fields with[`@unique`](https://firebase.google.com/docs/reference/data-connect/gql/directive#unique)may also be referred in the foreign key constraint.

|     Argument     |                                           Type                                           |                                              Description                                              |
|------------------|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| `constraintName` | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)    | The SQL database foreign key constraint name. Defaults to snake_case`{table_name}_{field_name}_fkey`. |
| `fields`         | [`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | Foreign key fields. Defaults to`{tableName}{PrimaryIdName}`.                                          |
| `references`     | [`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | The fields that the foreign key references in the other table. Defaults to its primary key.           |

### @retired on`QUERY`\|`MUTATION`\|`FIELD`\|`VARIABLE_DEFINITION`

Marks an element of a GraphQL operation as no longer supported for client use. The Firebase Data Connect backend will continue supporting this element, but it will no longer be visible in the generated SDKs.

| Argument |                                         Type                                          |             Description             |
|----------|---------------------------------------------------------------------------------------|-------------------------------------|
| `reason` | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | Provides the reason for retirement. |

### @table on`OBJECT`

Defines a relational database table.

In this example, we defined one table with a field named`myField`.  

    type TableName @table {
      myField: String
    }

Data Connect adds an implicit`id`primary key column. So the above schema is equivalent to:  

    type TableName @table(key: "id") {
      id: String @default(expr: "uuidV4()")
      myField: String
    }

Data Connect generates the following SQL table and CRUD operations to use it.  

    CREATE TABLE "public"."table_name" (
      "id" uuid NOT NULL DEFAULT uuid_generate_v4(),
      "my_field" text NULL,
      PRIMARY KEY ("id")
    )

- You can lookup a row:`query ($id: UUID!) { tableName(id: $id) { myField } }`
- You can find rows using:`query tableNames(limit: 20) { myField }`
- You can insert a row:`mutation { tableName_insert(data: {myField: "foo"}) }`
- You can update a row:`mutation ($id: UUID!) { tableName_update(id: $id, data: {myField: "bar"}) }`
- You can delete a row:`mutation ($id: UUID!) { tableName_delete(id: $id) }`

##### Customizations

- `@table(singular)`and`@table(plural)`can customize the singular and plural name.
- `@table(name)`can customize the Postgres table name.
- `@table(key)`can customize the primary key field name and type.

For example, the`User`table often has a`uid`as its primary key.  

    type User @table(key: "uid") {
      uid: String!
      name: String
    }

- You can securely lookup a row:`query { user(key: {uid_expr: "auth.uid"}) { name } }`
- You can securely insert a row:`mutation { user_insert(data: {uid_expr: "auth.uid" name: "Fred"}) }`
- You can securely update a row:`mutation { user_update(key: {uid_expr: "auth.uid"}, data: {name: "New Name"}) }`
- You can securely delete a row:`mutation { user_delete(key: {uid_expr: "auth.uid"}) }`

[`@table`](https://firebase.google.com/docs/reference/data-connect/gql/directive#table)type can be configured further with:

- Custom SQL data types for columns. See[`@col`](https://firebase.google.com/docs/reference/data-connect/gql/directive#col).
- Add SQL indexes. See[`@index`](https://firebase.google.com/docs/reference/data-connect/gql/directive#index).
- Add SQL unique constraints. See[`@unique`](https://firebase.google.com/docs/reference/data-connect/gql/directive#unique).
- Add foreign key constraints to define relations. See[`@ref`](https://firebase.google.com/docs/reference/data-connect/gql/directive#ref).

|  Argument  |                                           Type                                           |                                                                                  Description                                                                                   |
|------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`     | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)    | Configures the SQL database table name. Defaults to snake_case like`table_name`.                                                                                               |
| `singular` | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)    | Configures the singular name. Defaults to the camelCase like`tableName`.                                                                                                       |
| `plural`   | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)    | Configures the plural name. Defaults to infer based on English plural pattern like`tableNames`.                                                                                |
| `key`      | [`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | Defines the primary key of the table. Defaults to a single field named`id`. If not present already, Data Connect adds an implicit field`id: UUID! @default(expr: "uuidV4()")`. |

### @transaction on`MUTATION`

Require that this mutation always run in a DB transaction.

Mutations with[`@transaction`](https://firebase.google.com/docs/reference/data-connect/gql/directive#transaction)are guaranteed to either fully succeed or fully fail. Upon the first error in a transaction (either an execution error or failed[`@check`](https://firebase.google.com/docs/reference/data-connect/gql/directive#check)), the transaction will be rolled back. In the GraphQL response, all fields within the transaction will be`null`, each with an error raised.

- Fields that have been already evaluated will be nullified due to the rollback and a "(rolled back)" error will be reported on each of them.
- The execution error or failed[`@check`](https://firebase.google.com/docs/reference/data-connect/gql/directive#check)will be reported on the current field.
- Subsequent fields will not be executed. An`(aborted)`error will be reported on each subsequent field.

Mutations without[`@transaction`](https://firebase.google.com/docs/reference/data-connect/gql/directive#transaction)would execute each root field one after another in sequence. They surface any errors as partial[field errors](https://spec.graphql.org/October2021/#sec-Errors.Field-errors), but does not impact the execution of subsequent fields. However, failed[`@check`](https://firebase.google.com/docs/reference/data-connect/gql/directive#check)s still terminate the entire operation.

The[`@transaction`](https://firebase.google.com/docs/reference/data-connect/gql/directive#transaction)directive cannot be added to queries for now. Currently, queries cannot fail partially, the response data is not guaranteed to be a consistent snapshot.

### @unique on`FIELD_DEFINITION`\|`OBJECT`

Defines unique constraints on[`@table`](https://firebase.google.com/docs/reference/data-connect/gql/directive#table).

For example,  

    type User @table {
        phoneNumber: Int64 @unique
    }
    type UserProfile @table {
        user: User! @unique
        address: String @unique
    }

- [`@unique`](https://firebase.google.com/docs/reference/data-connect/gql/directive#unique)on a[`@col`](https://firebase.google.com/docs/reference/data-connect/gql/directive#col)field adds a single-column unique constraint.
- [`@unique`](https://firebase.google.com/docs/reference/data-connect/gql/directive#unique)on a[`@table`](https://firebase.google.com/docs/reference/data-connect/gql/directive#table)type adds a composite unique constraint.
- [`@unique`](https://firebase.google.com/docs/reference/data-connect/gql/directive#unique)on a[`@ref`](https://firebase.google.com/docs/reference/data-connect/gql/directive#ref)defines a one-to-one relation. It adds unique constraint on`@ref(fields)`.

[`@unique`](https://firebase.google.com/docs/reference/data-connect/gql/directive#unique)ensures those fields can uniquely identify a row, so other[`@table`](https://firebase.google.com/docs/reference/data-connect/gql/directive#table)type may define`@ref(references)`to refer to fields that has a unique constraint.

|  Argument   |                                           Type                                           |                                                                                               Description                                                                                               |
|-------------|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `indexName` | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)    | Configures the SQL database unique constraint name. If not overridden, Data Connect generates the unique constraint name: -`table_name_first_field_second_field_uidx`-`table_name_only_field_name_uidx` |
| `fields`    | [`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | Only allowed and required when used on OBJECT, this specifies the fields to create a unique constraint on.                                                                                              |

### @view on`OBJECT`

Defines a relational database Raw SQLview.

Data Connect generates GraphQL queries with WHERE and ORDER BY clauses. However, not all SQL features has native GraphQL equivalent.

You can write**an arbitrary SQL SELECT statement** . Data Connect would map Graphql fields on[`@view`](https://firebase.google.com/docs/reference/data-connect/gql/directive#view)type to columns in your SELECT statement.

- Scalar GQL fields (camelCase) should match a SQL column (snake_case) in the SQL SELECT statement.
- Reference GQL field can point to another[`@table`](https://firebase.google.com/docs/reference/data-connect/gql/directive#table)type. Similar to foreign key defined with[`@ref`](https://firebase.google.com/docs/reference/data-connect/gql/directive#ref)on a[`@table`](https://firebase.google.com/docs/reference/data-connect/gql/directive#table)type, a[`@view`](https://firebase.google.com/docs/reference/data-connect/gql/directive#view)type establishes a relation when`@ref(fields)`match`@ref(references)`on the target table.

In this example, you can use`@view(sql)`to define an aggregation view on existing table.  

    type User @table {
      name: String
      score: Int
    }
    type UserAggregation @view(sql: """
      SELECT
        COUNT(*) as count,
        SUM(score) as sum,
        AVG(score) as average,
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY score) AS median,
        (SELECT id FROM "user" LIMIT 1) as example_id
      FROM "user"
    """) {
      count: Int
      sum: Int
      average: Float
      median: Float
      example: User
      exampleId: UUID
    }

###### Example: Query Raw SQL View

    query {
      userAggregations {
        count sum average median
        exampleId example { id }
      }
    }

##### One-to-One View

An one-to-one companion[`@view`](https://firebase.google.com/docs/reference/data-connect/gql/directive#view)can be handy if you want to argument a[`@table`](https://firebase.google.com/docs/reference/data-connect/gql/directive#table)with additional implied content.  

    type Restaurant @table {
      name: String!
    }
    type Review @table {
      restaurant: Restaurant!
      rating: Int!
    }
    type RestaurantStats @view(sql: """
      SELECT
        restaurant_id,
        COUNT(*) AS review_count,
        AVG(rating) AS average_rating
      FROM review
      GROUP BY restaurant_id
    """) {
      restaurant: Restaurant @unique
      reviewCount: Int
      averageRating: Float
    }

In this example,[`@unique`](https://firebase.google.com/docs/reference/data-connect/gql/directive#unique)convey the assumption that each`Restaurant`should have only one`RestaurantStats`object.

###### Example: Query One-to-One View

    query ListRestaurants {
      restaurants {
        name
        stats: restaurantStats_on_restaurant {
          reviewCount
          averageRating
        }
      }
    }

###### Example: Filter based on One-to-One View

    query BestRestaurants($minAvgRating: Float, $minReviewCount: Int) {
      restaurants(where: {
        restaurantStats_on_restaurant: {
          averageRating: {ge: $minAvgRating}
          reviewCount: {ge: $minReviewCount}
        }
      }) { name }
    }

##### Customizations

- One of`@view(sql)`or`@view(name)`should be defined.`@view(name)`can refer to a persisted SQL view in the Postgres schema.
- `@view(singular)`and`@view(plural)`can customize the singular and plural name.

[`@view`](https://firebase.google.com/docs/reference/data-connect/gql/directive#view)type can be configured further:

- [`@unique`](https://firebase.google.com/docs/reference/data-connect/gql/directive#unique)lets you define one-to-one relation.
- [`@col`](https://firebase.google.com/docs/reference/data-connect/gql/directive#col)lets you customize SQL column mapping. For example,`@col(name: "column_in_select")`.

##### Limitations

Raw SQL view doesn't have a primary key, so it doesn't support lookup. Other[`@table`](https://firebase.google.com/docs/reference/data-connect/gql/directive#table)or[`@view`](https://firebase.google.com/docs/reference/data-connect/gql/directive#view)cannot have[`@ref`](https://firebase.google.com/docs/reference/data-connect/gql/directive#ref)to a view either.

View cannot be mutated. You can perform CRUD operations on the underlying table to alter its content.

**Important: Data Connect doesn't parse and validate SQL**

- If the SQL view is invalid or undefined, related requests may fail.
- If the SQL view return incompatible types. Firebase Data Connect may surface errors.
- If a field doesn't have a corresponding column in the SQL SELECT statement, it will always be`null`.
- There is no way to ensure VIEW to TABLE[`@ref`](https://firebase.google.com/docs/reference/data-connect/gql/directive#ref)constraint.
- All fields must be nullable in case they aren't found in the SELECT statement or in the referenced table.

**Important: You should always test[`@view`](https://firebase.google.com/docs/reference/data-connect/gql/directive#view)!**

|  Argument  |                                         Type                                          |                                                                                       Description                                                                                       |
|------------|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`     | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | The SQL view name. If neither`name`nor`sql`are provided, defaults to the snake_case of the singular type name.`name`and`sql`cannot be specified at the same time.                       |
| `sql`      | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | SQL`SELECT`statement used as the basis for this type. SQL SELECT columns should use snake_case. GraphQL fields should use camelCase.`name`and`sql`cannot be specified at the same time. |
| `singular` | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | Configures the singular name. Defaults to the camelCase like`viewName`.                                                                                                                 |
| `plural`   | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | Configures the plural name. Defaults to infer based on English plural pattern like`viewNames`.                                                                                          |

## Built In

### @deprecated on`FIELD_DEFINITION`\|`ARGUMENT_DEFINITION`\|`INPUT_FIELD_DEFINITION`\|`ENUM_VALUE`

Marks an element of a GraphQL schema as no longer supported.

| Argument |                                         Type                                          |                                                                                                    Description                                                                                                     |
|----------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `reason` | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | Explains why this element was deprecated, usually also including a suggestion for how to access supported similar data. Formatted using the Markdown syntax, as specified by[CommonMark](https://commonmark.org/). |

### @include on`FIELD`\|`FRAGMENT_SPREAD`\|`INLINE_FRAGMENT`

Directs the executor to include this field or fragment only when the`if`argument is true.

| Argument |                                           Type                                           |     Description     |
|----------|------------------------------------------------------------------------------------------|---------------------|
| `if`     | [`Boolean!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean) | Included when true. |

### @skip on`FIELD`\|`FRAGMENT_SPREAD`\|`INLINE_FRAGMENT`

Directs the executor to skip this field or fragment when the`if`argument is true.

| Argument |                                           Type                                           |    Description     |
|----------|------------------------------------------------------------------------------------------|--------------------|
| `if`     | [`Boolean!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean) | Skipped when true. |

### @specifiedBy on`SCALAR`

Exposes a URL that specifies the behavior of this scalar.

| Argument |                                          Type                                          |                     Description                     |
|----------|----------------------------------------------------------------------------------------|-----------------------------------------------------|
| `url`    | [`String!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | The URL that specifies the behavior of this scalar. |