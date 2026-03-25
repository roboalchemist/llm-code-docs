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

graphql.cachecontrol

## Class CacheControl

- java.lang.Object

- 

  - graphql.cachecontrol.CacheControl

- 

---

```
@PublicApi
public class CacheControl
extends java.lang.Object
```

This class implements the graphql Cache Control specification as outlined in https://github.com/apollographql/apollo-cache-control
 

 To best use this class you need to pass a CacheControl object to each `DataFetcher` and have them decide on
 the caching hint values.
 

 The easiest way to do this is create a CacheControl object at query start and pass it in as a "context" object via `ExecutionInput.getContext()` and then have
 each `DataFetcher` that wants to make cache control hints use that.
 

 Then at the end of the query you would call `addTo(graphql.ExecutionResult)` to record the cache control hints into the `ExecutionResult`
 extensions map as per the specification.

- 

  - 

### Nested Class Summary

Nested Classes 

Modifier and Type
Class and Description

`static class `
`CacheControl.Scope`
If the scope is set to PRIVATE, this indicates anything under this path should only be cached per-user,
 unless the value is overridden on a sub path.

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`static java.lang.String`
`CACHE_CONTROL_EXTENSION_KEY` 

  - 

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`ExecutionResult`
`addTo(ExecutionResult executionResult)`
This will record the values in the cache control object into the provided execution result object which creates a new `ExecutionResult`
 object back out

`CacheControl`
`hint(DataFetchingEnvironment dataFetchingEnvironment,
    CacheControl.Scope scope)`
This creates a cache control hint for the specified field being fetched with a specified scope

`CacheControl`
`hint(DataFetchingEnvironment dataFetchingEnvironment,
    java.lang.Integer maxAge)`
This creates a cache control hint for the specified field being fetched with a PUBLIC scope

`CacheControl`
`hint(DataFetchingEnvironment dataFetchingEnvironment,
    java.lang.Integer maxAge,
    CacheControl.Scope scope)`
This creates a cache control hint for the specified field being fetched

`CacheControl`
`hint(ResultPath path,
    CacheControl.Scope scope)`
This creates a cache control hint for the specified path

`CacheControl`
`hint(ResultPath path,
    java.lang.Integer maxAge)`
This creates a cache control hint for the specified path

`CacheControl`
`hint(ResultPath path,
    java.lang.Integer maxAge,
    CacheControl.Scope scope)`
This creates a cache control hint for the specified path

`static CacheControl`
`newCacheControl()`
Creates a new CacheControl object that can be used to trick caching hints

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### CACHE_CONTROL_EXTENSION_KEY

```
public static final java.lang.String CACHE_CONTROL_EXTENSION_KEY
```

See Also:
Constant Field Values

  - 

### Method Detail

    - 

#### hint

```
public CacheControl hint(ResultPath path,
                         java.lang.Integer maxAge,
                         CacheControl.Scope scope)
```

This creates a cache control hint for the specified path

Parameters:
`path` - the path to the field that has the cache control hint
`maxAge` - the caching time in seconds
`scope` - the scope of the cache control hint
Returns:
this object builder style

    - 

#### hint

```
public CacheControl hint(ResultPath path,
                         CacheControl.Scope scope)
```

This creates a cache control hint for the specified path

Parameters:
`path` - the path to the field that has the cache control hint
`scope` - the scope of the cache control hint
Returns:
this object builder style

    - 

#### hint

```
public CacheControl hint(ResultPath path,
                         java.lang.Integer maxAge)
```

This creates a cache control hint for the specified path

Parameters:
`path` - the path to the field that has the cache control hint
`maxAge` - the caching time in seconds
Returns:
this object builder style

    - 

#### hint

```
public CacheControl hint(DataFetchingEnvironment dataFetchingEnvironment,
                         java.lang.Integer maxAge,
                         CacheControl.Scope scope)
```

This creates a cache control hint for the specified field being fetched

Parameters:
`dataFetchingEnvironment` - the path to the field that has the cache control hint
`maxAge` - the caching time in seconds
`scope` - the scope of the cache control hint
Returns:
this object builder style

    - 

#### hint

```
public CacheControl hint(DataFetchingEnvironment dataFetchingEnvironment,
                         java.lang.Integer maxAge)
```

This creates a cache control hint for the specified field being fetched with a PUBLIC scope

Parameters:
`dataFetchingEnvironment` - the path to the field that has the cache control hint
`maxAge` - the caching time in seconds
Returns:
this object builder style

    - 

#### hint

```
public CacheControl hint(DataFetchingEnvironment dataFetchingEnvironment,
                         CacheControl.Scope scope)
```

This creates a cache control hint for the specified field being fetched with a specified scope

Parameters:
`dataFetchingEnvironment` - the path to the field that has the cache control hint
`scope` - the scope of the cache control hint
Returns:
this object builder style

    - 

#### newCacheControl

```
public static CacheControl newCacheControl()
```

Creates a new CacheControl object that can be used to trick caching hints

Returns:
the new object

    - 

#### addTo

```
public ExecutionResult addTo(ExecutionResult executionResult)
```

This will record the values in the cache control object into the provided execution result object which creates a new `ExecutionResult`
 object back out

Parameters:
`executionResult` - the starting execution result object
Returns:
a new execution result with the hints in the extensions map.

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