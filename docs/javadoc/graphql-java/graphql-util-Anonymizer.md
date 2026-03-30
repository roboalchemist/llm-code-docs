JavaScript is disabled on your browser.

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

graphql.util

## Class Anonymizer

- java.lang.Object

- 

  - graphql.util.Anonymizer

- 

---

```
@PublicApi
public class Anonymizer
extends java.lang.Object
```

Util class which converts schemas and optionally queries
 into anonymized schemas and queries.

- 

  - 

### Nested Class Summary

Nested Classes 

Modifier and Type
Class and Description

`static class `
`Anonymizer.AnonymizeResult` 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`Anonymizer()` 

  - 

### Method Summary

All Methods Static Methods Concrete Methods 

Modifier and Type
Method and Description

`static GraphQLSchema`
`anonymizeSchema(GraphQLSchema schema)` 

`static GraphQLSchema`
`anonymizeSchema(java.lang.String sdl)` 

`static Anonymizer.AnonymizeResult`
`anonymizeSchemaAndQueries(GraphQLSchema schema,
                         java.util.List<java.lang.String> queries)` 

`static Anonymizer.AnonymizeResult`
`anonymizeSchemaAndQueries(GraphQLSchema schema,
                         java.util.List<java.lang.String> queries,
                         java.util.Map<java.lang.String,java.lang.Object> variables)` 

`static Anonymizer.AnonymizeResult`
`anonymizeSchemaAndQueries(java.lang.String sdl,
                         java.util.List<java.lang.String> queries)` 

`static Anonymizer.AnonymizeResult`
`anonymizeSchemaAndQueries(java.lang.String sdl,
                         java.util.List<java.lang.String> queries,
                         java.util.Map<java.lang.String,java.lang.Object> variables)` 

`static java.util.Map<GraphQLNamedSchemaElement,java.lang.String>`
`recordNewNames(GraphQLSchema schema)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### Anonymizer

```
public Anonymizer()
```

  - 

### Method Detail

    - 

#### anonymizeSchema

```
public static GraphQLSchema anonymizeSchema(java.lang.String sdl)
```

    - 

#### anonymizeSchema

```
public static GraphQLSchema anonymizeSchema(GraphQLSchema schema)
```

    - 

#### anonymizeSchemaAndQueries

```
public static Anonymizer.AnonymizeResult anonymizeSchemaAndQueries(java.lang.String sdl,
                                                                   java.util.List<java.lang.String> queries)
```

    - 

#### anonymizeSchemaAndQueries

```
public static Anonymizer.AnonymizeResult anonymizeSchemaAndQueries(GraphQLSchema schema,
                                                                   java.util.List<java.lang.String> queries)
```

    - 

#### anonymizeSchemaAndQueries

```
public static Anonymizer.AnonymizeResult anonymizeSchemaAndQueries(java.lang.String sdl,
                                                                   java.util.List<java.lang.String> queries,
                                                                   java.util.Map<java.lang.String,java.lang.Object> variables)
```

    - 

#### anonymizeSchemaAndQueries

```
public static Anonymizer.AnonymizeResult anonymizeSchemaAndQueries(GraphQLSchema schema,
                                                                   java.util.List<java.lang.String> queries,
                                                                   java.util.Map<java.lang.String,java.lang.Object> variables)
```

    - 

#### recordNewNames

```
public static java.util.Map<GraphQLNamedSchemaElement,java.lang.String> recordNewNames(GraphQLSchema schema)
```

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method