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

graphql.execution.batched

## Class BatchedDataFetcherFactory

- java.lang.Object

- 

  - graphql.execution.batched.BatchedDataFetcherFactory

- 

---

Deprecated. 
This has been deprecated in favour of using `AsyncExecutionStrategy` and `DataLoaderDispatcherInstrumentation`

```
@Deprecated
 @PublicApi
public class BatchedDataFetcherFactory
extends java.lang.Object
```

Produces a BatchedDataFetcher for a given DataFetcher.
 If that fetcher is already a BatchedDataFetcher we return it.
 If that fetcher's get method is annotated @Batched then we delegate to it directly.
 Otherwise we wrap the fetcher in a BatchedDataFetcher that iterates over the sources and invokes the delegate
 on each source. Note that this forgoes any performance benefits of batching,
 so regular DataFetchers should normally only be used if they are in-memory.

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`BatchedDataFetcherFactory()`
Deprecated. 
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods Deprecated Methods 

Modifier and Type
Method and Description

`BatchedDataFetcher`
`create(DataFetcher supplied)`
Deprecated. 
 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BatchedDataFetcherFactory

```
public BatchedDataFetcherFactory()
```

Deprecated. 

  - 

### Method Detail

    - 

#### create

```
public BatchedDataFetcher create(DataFetcher supplied)
```

Deprecated. 

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