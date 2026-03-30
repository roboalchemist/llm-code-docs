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

graphql.execution.preparsed.persisted

## Class ApolloPersistedQuerySupport

- java.lang.Object

- 

  - graphql.execution.preparsed.persisted.PersistedQuerySupport

  - 

    - graphql.execution.preparsed.persisted.ApolloPersistedQuerySupport

- 

All Implemented Interfaces:
PreparsedDocumentProvider

---

```
@PublicApi
public class ApolloPersistedQuerySupport
extends PersistedQuerySupport
```

This persisted query support class supports the Apollo scheme where the persisted
 query id is in `ExecutionInput.getExtensions()`.
 

 You need to provide a `PersistedQueryCache` cache implementation
 as the backing cache.
 

 See Apollo Persisted Queries
 

 The Apollo client sends a hash of the persisted query in the input extensions in the following form
 

```

     {
      "extensions":{
       "persistedQuery":{
        "version":1,
        "sha256Hash":"fcf31818e50ac3e818ca4bdbc433d6ab73176f0b9d5f9d5ad17e200cdab6fba4"
      }
    }
  }
 
```

See Also:
`ExecutionInput.getExtensions()`

- 

  - 

### Field Summary

    - 

### Fields inherited from class graphql.execution.preparsed.persisted.PersistedQuerySupport

`PERSISTED_QUERY_MARKER`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`ApolloPersistedQuerySupport(PersistedQueryCache persistedQueryCache)` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`protected java.util.Optional<java.lang.Object>`
`getPersistedQueryId(ExecutionInput executionInput)`
This method is required for concrete types to work out the query id (often a hash) that should be used to look
 up the persisted query in the cache.

    - 

### Methods inherited from class graphql.execution.preparsed.persisted.PersistedQuerySupport

`getDocument, mkMissingError`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### ApolloPersistedQuerySupport

```
public ApolloPersistedQuerySupport(PersistedQueryCache persistedQueryCache)
```

  - 

### Method Detail

    - 

#### getPersistedQueryId

```
protected java.util.Optional<java.lang.Object> getPersistedQueryId(ExecutionInput executionInput)
```

Description copied from class: `PersistedQuerySupport`
This method is required for concrete types to work out the query id (often a hash) that should be used to look
 up the persisted query in the cache.

Specified by:
`getPersistedQueryId` in class `PersistedQuerySupport`
Parameters:
`executionInput` - the execution input
Returns:
an optional id of the persisted query

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