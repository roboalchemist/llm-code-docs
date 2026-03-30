# Source: https://firebase.google.com/docs/reference/data-connect.md.txt

# Firebase Data Connect API Reference

Welcome to the API reference for Data Connect. This guide provides detailed
documentation on the unique features and functionality available through the
GraphQL API. You can explore various extensions, data types, and operations
supported by Data Connect below.

## REST API Reference

For a detailed guide on the REST API, which covers queries, mutations, schema
and connector management, and project management functions, visit the
[REST API reference](https://firebase.google.com/docs/reference/data-connect/rest).

## GraphQL Schema

Data Connect allows you to define your SQL Schema in [GraphQL schema](https://graphql.org/learn/schema/) and automatically extends the schema with query and mutation operations.

The GraphQL schema reference page assumes the following Data Connect Schema.

    type MainTable @table {
      uuidField: UUID
      stringField: String @searchable
      intField: Int
      int64Field: Int64
      floatField: Float
      booleanField: Boolean
      dateField: Date
      timestampField: Timestamp
      anyField: Any
      vectorField: Vector @col(size: 768)
      uuidArray: [UUID]
      stringArray: [String]
      intArray: [Int]
      int64Array: [Int64]
      floatArray: [Float]
      booleanArray: [Boolean]
      dateArray: [Date]
      timestampArray: [Timestamp]
      anyArray: [Any]
    }
    type StringTable @table {
      stringField: String
      nonNullStringField: String!
      stringArray: [String]
      nonNullStringArray: [String!]
      stringNonnullArray: [String]!
      nonNullStringNonnullArray: [String!]!
    }
    type ManyToOneExample @table {
      main: MainTable!
      someField: Any
    }
    type OneToOneExample @table {
      main: MainTable! @unique
      someField: Any
    }
    type ManyToManyJoinTable @table(key: ["left","right"]) {
      left: MainTable!
      right: MainTable!
    }

Below you will find detailed documentation for each extension type.
In each page, you can see builtin types, Data Connect Defined types as well as Built In Types from Open [GraphQL spec](https://spec.graphql.org/).

### *Directives*

Data Connect offers customized [GraphQL directives](https://graphql.org/learn/queries/#directives) to let you customize SQL mapping in the schema.

Explore the available directives in [GraphQL Directives Reference](https://firebase.google.com/docs/reference/data-connect/gql/directive).

### *Queries*

[Queries](https://graphql.org/learn/queries) are the core operations in GraphQL that allow you to fetch data from the server. Data Connect offers enhanced query functionality to retrieve data with powerful filters and ordering options.

See more about available queries in the [GraphQL Query Types Reference](https://firebase.google.com/docs/reference/data-connect/gql/query).

### *Mutations*

[Mutations](https://graphql.org/learn/queries/#mutations) allow you to modify data on the server. Data Connect supports a wide range of mutation operations, from inserting and updating data to handling complex upsert and delete operations.

Learn about the mutation operations in the [GraphQL Mutation Types Reference](https://firebase.google.com/docs/reference/data-connect/gql/mutation).

### *Objects*

Object types are the core building blocks of a GraphQL schema. They define the structure of the data you can query, with fields that map to specific data points or relationships between data. Users can define [objects](https://graphql.org/learn/schema/#object-types-and-fields) in schema that maps to SQL tables.

Learn more in the [GraphQL Object Types Reference](https://firebase.google.com/docs/reference/data-connect/gql/object).

### *Input Object*

Input Object types define structured data that can be passed into mutations and queries. Data Connect supports a variety of [input types](https://graphql.org/learn/schema/#input-types) to handle complex filtering, updating, and ordering scenarios.

View all input object types in the [GraphQL Input Object Types Reference](https://firebase.google.com/docs/reference/data-connect/gql/input_object).

### *Scalars*

Scalar types represent the fundamental data types in a GraphQL schema. Data Connect supports additional scalars beyond the builtin [GraphQL scalars](https://graphql.org/learn/schema/#scalar-types) to represent common SQL types like [Date](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date), [Timestamp](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp), [UUID](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID) and more.

For a full list of scalar types, visit the [GraphQL Scalar Types Reference](https://firebase.google.com/docs/reference/data-connect/gql/scalar).

### *Enums*

Enumerations (Enums) allow you to define a set of [allowed values](https://graphql.org/learn/schema/#enumeration-types) for a field in a schema.

Discover available enums in the [GraphQL Enum Types Reference](https://firebase.google.com/docs/reference/data-connect/gql/enum).