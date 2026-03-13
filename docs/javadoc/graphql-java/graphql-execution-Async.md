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

graphql.execution

## Class Async

- java.lang.Object

- 

  - graphql.execution.Async

- 

---

```
public class Async
extends java.lang.Object
```

- 

  - 

### Nested Class Summary

Nested Classes 

Modifier and Type
Class and Description

`static interface `
`Async.CFFactory<T,U>` 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`Async()` 

  - 

### Method Summary

All Methods Static Methods Concrete Methods 

Modifier and Type
Method and Description

`static <T,U> java.util.concurrent.CompletableFuture<java.util.List<U>>`
`each(java.util.Collection<T> list,
    java.util.function.BiFunction<T,java.lang.Integer,java.util.concurrent.CompletableFuture<U>> cfFactory)` 

`static <U> java.util.concurrent.CompletableFuture<java.util.List<U>>`
`each(java.util.List<java.util.concurrent.CompletableFuture<U>> futures)` 

`static <T,U> java.util.concurrent.CompletableFuture<java.util.List<U>>`
`eachSequentially(java.lang.Iterable<T> list,
                Async.CFFactory<T,U> cfFactory)` 

`static <T> java.util.concurrent.CompletableFuture<T>`
`exceptionallyCompletedFuture(java.lang.Throwable exception)` 

`static <U,T> java.util.concurrent.CompletableFuture<java.util.List<U>>`
`flatMap(java.util.List<T> inputs,
       java.util.function.Function<T,java.util.concurrent.CompletableFuture<U>> mapper)` 

`static <U,T> java.util.concurrent.CompletableFuture<java.util.List<U>>`
`map(java.util.concurrent.CompletableFuture<java.util.List<T>> values,
   java.util.function.Function<T,U> mapper)` 

`static <U,T> java.util.List<java.util.concurrent.CompletableFuture<U>>`
`map(java.util.List<java.util.concurrent.CompletableFuture<T>> values,
   java.util.function.Function<T,U> mapper)` 

`static <U,T> java.util.List<java.util.concurrent.CompletableFuture<U>>`
`mapCompose(java.util.List<java.util.concurrent.CompletableFuture<T>> values,
          java.util.function.Function<T,java.util.concurrent.CompletableFuture<U>> mapper)` 

`static <T> java.util.concurrent.CompletableFuture<T>`
`toCompletableFuture(T t)`
Turns an object T into a CompletableFuture if its not already

`static <T> java.util.concurrent.CompletableFuture<T>`
`tryCatch(java.util.function.Supplier<java.util.concurrent.CompletableFuture<T>> supplier)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### Async

```
public Async()
```

  - 

### Method Detail

    - 

#### each

```
public static <U> java.util.concurrent.CompletableFuture<java.util.List<U>> each(java.util.List<java.util.concurrent.CompletableFuture<U>> futures)
```

    - 

#### each

```
public static <T,U> java.util.concurrent.CompletableFuture<java.util.List<U>> each(java.util.Collection<T> list,
                                                                                   java.util.function.BiFunction<T,java.lang.Integer,java.util.concurrent.CompletableFuture<U>> cfFactory)
```

    - 

#### eachSequentially

```
public static <T,U> java.util.concurrent.CompletableFuture<java.util.List<U>> eachSequentially(java.lang.Iterable<T> list,
                                                                                               Async.CFFactory<T,U> cfFactory)
```

    - 

#### toCompletableFuture

```
public static <T> java.util.concurrent.CompletableFuture<T> toCompletableFuture(T t)
```

Turns an object T into a CompletableFuture if its not already

Type Parameters:
`T` - for two
Parameters:
`t` - - the object to check
Returns:
a CompletableFuture

    - 

#### tryCatch

```
public static <T> java.util.concurrent.CompletableFuture<T> tryCatch(java.util.function.Supplier<java.util.concurrent.CompletableFuture<T>> supplier)
```

    - 

#### exceptionallyCompletedFuture

```
public static <T> java.util.concurrent.CompletableFuture<T> exceptionallyCompletedFuture(java.lang.Throwable exception)
```

    - 

#### flatMap

```
public static <U,T> java.util.concurrent.CompletableFuture<java.util.List<U>> flatMap(java.util.List<T> inputs,
                                                                                      java.util.function.Function<T,java.util.concurrent.CompletableFuture<U>> mapper)
```

    - 

#### map

```
public static <U,T> java.util.concurrent.CompletableFuture<java.util.List<U>> map(java.util.concurrent.CompletableFuture<java.util.List<T>> values,
                                                                                  java.util.function.Function<T,U> mapper)
```

    - 

#### map

```
public static <U,T> java.util.List<java.util.concurrent.CompletableFuture<U>> map(java.util.List<java.util.concurrent.CompletableFuture<T>> values,
                                                                                  java.util.function.Function<T,U> mapper)
```

    - 

#### mapCompose

```
public static <U,T> java.util.List<java.util.concurrent.CompletableFuture<U>> mapCompose(java.util.List<java.util.concurrent.CompletableFuture<T>> values,
                                                                                         java.util.function.Function<T,java.util.concurrent.CompletableFuture<U>> mapper)
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