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

graphql.schema

## Class AsyncDataFetcher<T>

- java.lang.Object

- 

  - graphql.schema.AsyncDataFetcher<T>

- 

All Implemented Interfaces:
DataFetcher<java.util.concurrent.CompletableFuture<T>>

---

```
@PublicApi
public class AsyncDataFetcher<T>
extends java.lang.Object
implements DataFetcher<java.util.concurrent.CompletableFuture<T>>
```

A modifier type that indicates the underlying data fetcher is run asynchronously

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AsyncDataFetcher(DataFetcher<T> wrappedDataFetcher)` 

`AsyncDataFetcher(DataFetcher<T> wrappedDataFetcher,
                java.util.concurrent.Executor executor)` 

  - 

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`static <T> AsyncDataFetcher<T>`
`async(DataFetcher<T> wrappedDataFetcher)`
A factory method for creating asynchronous data fetchers so that when used with
 static imports allows more readable code such as:

`static <T> AsyncDataFetcher<T>`
`async(DataFetcher<T> wrappedDataFetcher,
     java.util.concurrent.Executor executor)`
A factory method for creating asynchronous data fetchers and setting the
 `Executor` they run in so that when used with static imports allows
 more readable code such as:

`java.util.concurrent.CompletableFuture<T>`
`get(DataFetchingEnvironment environment)`
This is called by the graphql engine to fetch the value.

`java.util.concurrent.Executor`
`getExecutor()` 

`DataFetcher<T>`
`getWrappedDataFetcher()` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AsyncDataFetcher

```
public AsyncDataFetcher(DataFetcher<T> wrappedDataFetcher)
```

    - 

#### AsyncDataFetcher

```
public AsyncDataFetcher(DataFetcher<T> wrappedDataFetcher,
                        java.util.concurrent.Executor executor)
```

  - 

### Method Detail

    - 

#### async

```
public static <T> AsyncDataFetcher<T> async(DataFetcher<T> wrappedDataFetcher)
```

A factory method for creating asynchronous data fetchers so that when used with
 static imports allows more readable code such as:
 

 `.dataFetcher(async(fooDataFetcher))`
 

 By default this will run in the `ForkJoinPool.commonPool()`. You can set
 your own `Executor` with `async(DataFetcher, Executor)`

Type Parameters:
`T` - the type of data
Parameters:
`wrappedDataFetcher` - the data fetcher to run asynchronously
Returns:
a `DataFetcher` that will run the wrappedDataFetcher asynchronously

    - 

#### async

```
public static <T> AsyncDataFetcher<T> async(DataFetcher<T> wrappedDataFetcher,
                                            java.util.concurrent.Executor executor)
```

A factory method for creating asynchronous data fetchers and setting the
 `Executor` they run in so that when used with static imports allows
 more readable code such as:
 

 `.dataFetcher(async(fooDataFetcher, fooExecutor))`

Type Parameters:
`T` - the type of data
Parameters:
`wrappedDataFetcher` - the data fetcher to run asynchronously
`executor` - the executor to run the asynchronous data fetcher in
Returns:
a `DataFetcher` that will run the wrappedDataFetcher asynchronously in
 the given `Executor`

    - 

#### getWrappedDataFetcher

```
public DataFetcher<T> getWrappedDataFetcher()
```

    - 

#### getExecutor

```
public java.util.concurrent.Executor getExecutor()
```

    - 

#### get

```
public java.util.concurrent.CompletableFuture<T> get(DataFetchingEnvironment environment)
```

Description copied from interface: `DataFetcher`
This is called by the graphql engine to fetch the value.  The `DataFetchingEnvironment` is a composite
 context object that tells you all you need to know about how to fetch a data value in graphql type terms.

Specified by:
`get` in interface `DataFetcher<java.util.concurrent.CompletableFuture<T>>`
Parameters:
`environment` - this is the data fetching environment which contains all the context you need to fetch a value
Returns:
a value of type T. May be wrapped in a `DataFetcherResult`

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