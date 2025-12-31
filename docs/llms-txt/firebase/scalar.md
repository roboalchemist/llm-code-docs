# Source: https://firebase.google.com/docs/reference/data-connect/gql/scalar.md.txt

This reference doc is generated based on this[example schema](https://firebase.google.com/docs/reference/data-connect#graphql_schema).

Scalar types define the basic data types used for individual fields or arguments in a GraphQL schema.

Data Connect supports GraphQL's built in scalar types and a few additional scalars. Customer defined scalar types are not supported.

## Data Connect Defined

### scalar Any

**Specification** :<https://www.json.org/json-en.html>

The[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)scalar type accommodates any valid[JSON value](https://www.json.org/json-en.html)(e.g., numbers, strings, booleans, arrays, objects). PostgreSQL efficiently stores this data as jsonb, providing flexibility for schemas with evolving structures.
| **Caution:** JSON doesn't distinguish Int and Float.

##### Example:

#### Schema

    type Movie @table {
      name: String!
      metadata: Any!
    }

#### Mutation

Insert a movie with name and metadata from JSON literal.  

    mutation InsertMovie {
      movie_insert(
        data: {
          name: "The Dark Knight"
          metadata: {
            release_year: 2008
            genre: ["Action", "Adventure", "Superhero"]
            cast: [
              { name: "Christopher Bale", age: 31 }
              { name: "Heath Ledger", age: 28 }
            ]
            director: "Christopher Nolan"
          }
        }
      )
    }

Insert a movie with name and metadata that's constructed from a few GQL variables.  

    mutation InsertMovie($name: String!, $releaseDate: Date!, $genre: [String], $cast: [Any], $director: String!, $boxOfficeInUSD: Int) {
      movie_insert(data: {
        name: $name,
        release_date: $releaseDate,
        genre: $genre,
        cast: $cast,
        director: $director,
        box_office: $boxOfficeInUSD
      })
    }

**Note**:

- A mix of non-null and nullable variables can be provided.

- [`Date!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)can be passed into scalar[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)as well! It's stored as string.

- `$cast`is a nested array.[`[Any]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)can represent an array of arbitrary types, but it won't enforce the input shape.

#### Query

Since`metadata`field has scalar[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)type, it would return the full JSON in the response.

**Note** : You can't define selection set to scalar based on[GraphQL spec](https://spec.graphql.org/October2021/#sec-Field-Selections).  

    query GetAllMovies {
      movies {
        name
        metadata
      }
    }

### scalar Any_Expr

**Specification** :<https://github.com/google/cel-spec>

A Common Expression Language (CEL) expression whose return type is valid JSON.

Examples: -`{'A' : 'B'}`(Evaluates to a JSON object.) -`['A', 'B']`(Evaluates to a JSON array.) -`{'A' 1, 'B': [1, 2, {'foo': 'bar'}]}`(Nested JSON objects and arrays.)

### scalar Any_SQL

**Specification** :<https://www.postgresql.org/docs/current/sql-expressions.html>

A PostgreSQL value expression whose return type is unspecified.

### scalar Boolean_Expr

**Specification** :<https://github.com/google/cel-spec>

A Common Expression Language (CEL) expression that returns a boolean at runtime.

This expression can reference the`auth`variable, which is null when Firebase Auth is not used. When Firebase Auth is used, the following fields are available:

- `auth.uid`: The current user ID.
- `auth.token`: A map containing all token fields (e.g., claims).

|    Example     |                  Description                   |
|----------------|------------------------------------------------|
| `auth != null` | Allow only if a Firebase Auth user is present. |

### scalar Date

**Specification** :<https://scalars.graphql.org/andimarek/local-date.html>

Date is a string in the YYYY-MM-DD format representing a local-only date.

See the description for Timestamp for range and limitations.

As a FDC-specific extension, inputs that includes time portions (as specified by the Timestamp scalar) are accepted but only the date portion is used. In other words, only the part before "T" is used and the rest discarded. This effectively truncates it to the local date in the specified time-zone.

Outputs will always be in the canonical YYYY-MM-DD format.

In the PostgreSQL table, it's stored as[`date`](https://www.postgresql.org/docs/current/datatype-datetime.html).

### scalar Date_Expr

**Specification** :<https://github.com/google/cel-spec>

A Common Expression Language (CEL) expression that returns a Timestamp at runtime, which is then truncated to UTC date only. The time-of-day parts are discarded.

Limitation: Right now, only a few expressions are supported.

|    Example     |                  Description                   |
|----------------|------------------------------------------------|
| `request.time` | The UTC date on which the request is received. |

### scalar Float_Expr

**Specification** :<https://github.com/google/cel-spec>

A Common Expression Language (CEL) expression that returns a Float at runtime.

|   Example   |    Description    |
|-------------|-------------------|
| `2.0 * 4.0` | Evaluates to 8.0. |

### scalar Int64

[`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)is a scalar that represents a 64-bit signed integer.

In the PostgreSQL table, it's stored as[`bigint`](https://www.postgresql.org/docs/current/datatype-numeric.html).

On the wire, it's encoded as string because 64-bit integer exceeds the range of JSON number.

### scalar Int64_Expr

**Specification** :<https://github.com/google/cel-spec>

A Common Expression Language (CEL) expression that returns a Int64 at runtime.

|     Example      |    Description    |
|------------------|-------------------|
| `5000*1000*1000` | Evaluates to 5e9. |

### scalar Int_Expr

**Specification** :<https://github.com/google/cel-spec>

A Common Expression Language (CEL) expression that returns a Int at runtime.

|      Example      |                                 Description                                  |
|-------------------|------------------------------------------------------------------------------|
| `2 * 4`           | Evaluates to 8.                                                              |
| `vars.foo.size()` | Assuming`vars.foo`is a string, it will evaluate to the length of the string. |

### scalar String_Expr

**Specification** :<https://github.com/google/cel-spec>

A Common Expression Language (CEL) expression that returns a string at runtime.

**Limitation**: Currently, only a limited set of expressions are supported.

|  Example   |                                                Description                                                |
|------------|-----------------------------------------------------------------------------------------------------------|
| `auth.uid` | The ID of the currently logged in user in Firebase Auth. (Errors if not logged in.)                       |
| `uuidV4()` | Generates a new random UUID (version 4) string, formatted as 32 lower-case hex digits without delimiters. |

### scalar Timestamp

**Specification** :<https://scalars.graphql.org/andimarek/date-time>

Timestamp is a RFC 3339 string that represents an exact point in time.

The serialization format follows https://scalars.graphql.org/andimarek/date-time except the "Non-optional exact milliseconds" Section. As a FDC-specific extension, inputs and outputs may contain 0, 3, 6, or 9 fractional digits.

Specifically, output precision varies by server-side factors such as data source support and clients must not rely on an exact number of digits. Clients may truncate extra digits as fit, with the caveat that there may be information loss if the truncated value is subsequently sent back to the server.

FDC only supports year 1583 to 9999 (inclusive) and uses the ISO-8601 calendar system for all date-time calculations. Notably, the expanded year representation (+/-YYYYY) is rejected and Year 1582 and before may either be rejected or cause undefined behavior.

In the PostgreSQL table, it's stored as[`timestamptz`](https://www.postgresql.org/docs/current/datatype-datetime.html).

### scalar Timestamp_Expr

**Specification** :<https://github.com/google/cel-spec>

A Common Expression Language (CEL) expression that returns a Timestamp at runtime.

Limitation: Right now, only a few expressions are supported.

|    Example     |                                Description                                |
|----------------|---------------------------------------------------------------------------|
| `request.time` | The timestamp when the request is received (with microseconds precision). |

### scalar True

The[`True`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#True)scalar type only accepts the boolean value`true`.

An optional field/argument typed as[`True`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#True)may either be set to`true`or omitted (not provided at all). The values`false`or`null`are not accepted.

| Example |       Description       |
|---------|-------------------------|
| `true`  | The only allowed value. |

### scalar UUID

**Specification** :<https://tools.ietf.org/html/rfc4122>

[`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)is a string of hexadecimal digits representing an RFC4122-compliant UUID.

UUIDs are always output as 32 lowercase hexadecimal digits without delimiters or curly braces. Inputs in the following formats are also accepted (case insensitive):

- `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
- `urn:uuid:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
- `{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}`

In the PostgreSQL table, it's stored as[`uuid`](https://www.postgresql.org/docs/current/datatype-uuid.html).

### scalar UUID_Expr

**Specification** :<https://github.com/google/cel-spec>

A Common Expression Language (CEL) expression that returns a UUID string at runtime.

**Limitation**: Currently, only a limited set of expressions are supported.

|  Example   |                     Description                     |
|------------|-----------------------------------------------------|
| `uuidV4()` | Generates a new random UUID (version 4) every time. |

### scalar Vector

Vector is an array of single-precision floating-point numbers, serialized as a JSON array. All elements must be finite (no NaN, Infinity or -Infinity).

Example: \[1.1, 2, 3.3\]

In the PostgreSQL table, it's stored as[`pgvector`](https://github.com/pgvector/pgvector).

See[`Vector_Embed`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Vector_Embed)for how to generate text embeddings in query and mutations.

### scalar Vector_Embed_Model

**Specification** :<https://cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versioning>

The Vertex AI model version that is required in input[`Vector_Embed`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Vector_Embed).

It is recommended to use the latest stable model version:`textembedding-gecko@003`.

View all supported[Vertex AI Text embeddings APIs](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api).

|          Example          |                    Description                    |
|---------------------------|---------------------------------------------------|
| `textembedding-gecko@003` | A stable version of the textembedding-gecko model |
| `textembedding-gecko@001` | An older version of the textembedding-gecko model |
| `text-embedding-004`      | Another text embedding model                      |

### scalar Void

The[`Void`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Void)scalar type represents the absence of any value. It is typically used in operations where no value is expected in return.

## Data Connect Generated

### scalar MainTable_KeyOutput

â¨[`MainTable_KeyOutput`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#MainTable_KeyOutput)returns the primary key fields of table type[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).

It has the same format as[`MainTable_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Key), but is only used as mutation return value.

### scalar ManyToManyJoinTable_KeyOutput

â¨[`ManyToManyJoinTable_KeyOutput`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#ManyToManyJoinTable_KeyOutput)returns the primary key fields of table type[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).

It has the same format as[`ManyToManyJoinTable_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Key), but is only used as mutation return value.

### scalar ManyToOneExample_KeyOutput

â¨[`ManyToOneExample_KeyOutput`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#ManyToOneExample_KeyOutput)returns the primary key fields of table type[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).

It has the same format as[`ManyToOneExample_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Key), but is only used as mutation return value.

### scalar OneToOneExample_KeyOutput

â¨[`OneToOneExample_KeyOutput`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#OneToOneExample_KeyOutput)returns the primary key fields of table type[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).

It has the same format as[`OneToOneExample_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Key), but is only used as mutation return value.

### scalar StringTable_KeyOutput

â¨[`StringTable_KeyOutput`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#StringTable_KeyOutput)returns the primary key fields of table type[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).

It has the same format as[`StringTable_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Key), but is only used as mutation return value.

## Built In

### scalar Boolean

The[`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)scalar type represents`true`or`false`.

### scalar Float

The[`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)scalar type represents signed double-precision fractional values as specified by[IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).

### scalar ID

The[`ID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#ID)scalar type represents a unique identifier, often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as`"4"`) or integer (such as`4`) input value will be accepted as an ID.

### scalar Int

The[`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2\^31) and 2\^31 - 1.

### scalar String

The[`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.