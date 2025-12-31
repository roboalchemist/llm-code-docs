# Source: https://firebase.google.com/docs/reference/data-connect/gql/enum.md.txt

This reference doc is generated based on this[example schema](https://firebase.google.com/docs/reference/data-connect#graphql_schema).

Enum types define a set of allowed values for a field in a GraphQL schema.

Data Connect defines a few Built in enum types, but doesn't support developer defined enum types yet.

## Data Connect Defined

### enum AccessLevel

AccessLevel specifies coarse access policies for common situations.

Possible Values:

|         Value         |                                                                                                               Description                                                                                                                |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PUBLIC`              | This operation is accessible to anyone, with or without authentication. Equivalent to:`@auth(expr: "true")`                                                                                                                              |
| `USER_ANON`           | This operation can be executed only with a valid Firebase Auth ID token.**Note:** This access level allows anonymous and unverified accounts, which may present security and abuse risks. Equivalent to:`@auth(expr: "auth.uid != nil")` |
| `USER`                | This operation is restricted to non-anonymous Firebase Auth accounts. Equivalent to:`@auth(expr: "auth.uid != nil && auth.token.firebase.sign_in_provider != 'anonymous'")`                                                              |
| `USER_EMAIL_VERIFIED` | This operation is restricted to Firebase Auth accounts with verified email addresses. Equivalent to:`@auth(expr: "auth.uid != nil && auth.token.email_verified")`                                                                        |
| `NO_ACCESS`           | This operation cannot be executed by anyone. The operation can only be performed by using the Admin SDK from a privileged environment. Equivalent to:`@auth(expr: "false")`                                                              |

### enum Date_Interval

Possible Values:

|  Value  |               Description                |
|---------|------------------------------------------|
| `WEEK`  | Represents a time interval of one week.  |
| `MONTH` | Represents a time interval of one month. |
| `YEAR`  | Represents a time interval of one year.  |

### enum IndexFieldOrder

Specifies the sorting order for database indexes.

Possible Values:

| Value  |                          Description                          |
|--------|---------------------------------------------------------------|
| `ASC`  | Sorts the field in ascending order (from lowest to highest).  |
| `DESC` | Sorts the field in descending order (from highest to lowest). |

### enum IndexType

Defines the type of index to be used in the database.

Possible Values:

|   Value   |                                          Description                                           |
|-----------|------------------------------------------------------------------------------------------------|
| `BTREE`   | A general-purpose index type commonly used for sorting and searching.                          |
| `GIN`     | Generalized Inverted Index, optimized for indexing composite values such as arrays.            |
| `HNSW`    | Hierarchical Navigable Small World graph, used for nearest-neighbor searches on vector fields. |
| `IVFFLAT` | Inverted File Index, optimized for approximate nearest-neighbor searches in vector databases.  |

### enum OrderDirection

Defines the orderBy direction in a query.

Possible Values:

| Value  |               Description                |
|--------|------------------------------------------|
| `ASC`  | Results are ordered in ascending order.  |
| `DESC` | Results are ordered in descending order. |

### enum Timestamp_Interval

Possible Values:

|  Value   |                Description                |
|----------|-------------------------------------------|
| `SECOND` | Represents a time interval of one second. |
| `MINUTE` | Represents a time interval of one minute. |
| `HOUR`   | Represents a time interval of one hour.   |
| `DAY`    | Represents a time interval of one day.    |
| `WEEK`   | Represents a time interval of one week.   |
| `MONTH`  | Represents a time interval of one month.  |
| `YEAR`   | Represents a time interval of one year.   |

### enum VectorSimilarityMethod

Defines the similarity function to use when comparing vectors in queries.

Defaults to`INNER_PRODUCT`.

View[all vector functions](https://github.com/pgvector/pgvector?tab=readme-ov-file#vector-functions).

Possible Values:

|      Value      |                         Description                          |
|-----------------|--------------------------------------------------------------|
| `L2`            | Measures the Euclidean (L2) distance between two vectors.    |
| `COSINE`        | Measures the cosine similarity between two vectors.          |
| `INNER_PRODUCT` | Measures the inner product(dot product) between two vectors. |

## Built In

### enum __DirectiveLocation

A Directive can be adjacent to many parts of the GraphQL language, a __DirectiveLocation describes one such possible adjacencies.

Possible Values:

|          Value           |                      Description                       |
|--------------------------|--------------------------------------------------------|
| `QUERY`                  | Location adjacent to a query operation.                |
| `MUTATION`               | Location adjacent to a mutation operation.             |
| `SUBSCRIPTION`           | Location adjacent to a subscription operation.         |
| `FIELD`                  | Location adjacent to a field.                          |
| `FRAGMENT_DEFINITION`    | Location adjacent to a fragment definition.            |
| `FRAGMENT_SPREAD`        | Location adjacent to a fragment spread.                |
| `INLINE_FRAGMENT`        | Location adjacent to an inline fragment.               |
| `VARIABLE_DEFINITION`    | Location adjacent to a variable definition.            |
| `SCHEMA`                 | Location adjacent to a schema definition.              |
| `SCALAR`                 | Location adjacent to a scalar definition.              |
| `OBJECT`                 | Location adjacent to an object type definition.        |
| `FIELD_DEFINITION`       | Location adjacent to a field definition.               |
| `ARGUMENT_DEFINITION`    | Location adjacent to an argument definition.           |
| `INTERFACE`              | Location adjacent to an interface definition.          |
| `UNION`                  | Location adjacent to a union definition.               |
| `ENUM`                   | Location adjacent to an enum definition.               |
| `ENUM_VALUE`             | Location adjacent to an enum value definition.         |
| `INPUT_OBJECT`           | Location adjacent to an input object type definition.  |
| `INPUT_FIELD_DEFINITION` | Location adjacent to an input object field definition. |

### enum __TypeKind

An enum describing what kind of type a given[`__Type`](https://firebase.google.com/docs/reference/data-connect/gql/object#__Type)is.

Possible Values:

|     Value      |                                          Description                                           |
|----------------|------------------------------------------------------------------------------------------------|
| `SCALAR`       | Indicates this type is a scalar.                                                               |
| `OBJECT`       | Indicates this type is an object.`fields`and`interfaces`are valid fields.                      |
| `INTERFACE`    | Indicates this type is an interface.`fields`,`interfaces`, and`possibleTypes`are valid fields. |
| `UNION`        | Indicates this type is a union.`possibleTypes`is a valid field.                                |
| `ENUM`         | Indicates this type is an enum.`enumValues`is a valid field.                                   |
| `INPUT_OBJECT` | Indicates this type is an input object.`inputFields`is a valid field.                          |
| `LIST`         | Indicates this type is a list.`ofType`is a valid field.                                        |
| `NON_NULL`     | Indicates this type is a non-null.`ofType`is a valid field.                                    |