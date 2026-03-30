Package io.vavr

# Class API.For1Future<T1>

java.lang.Object
io.vavr.API.For1Future<T1>

Type Parameters:
`T1` - component type of `Future` number 1

Enclosing class:
`API`

---

public static class API.For1Future<T1>
extends Object
For-comprehension with one Future.

- 

## Method Summary

Modifier and Type
Method
Description
`Future<T1>`
`yield()`

A shortcut for `yield(Function.identity())`.

`<R> Future<R>`
`yield(@NonNull Function<? super T1,? extends R> f)`

Yields a result for elements of the cross-product of the underlying Future.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### yield

public <R> Future<R> yield(@NonNull Function<? super T1,? extends R> f)
Yields a result for elements of the cross-product of the underlying Future.

Type Parameters:
`R` - type of the resulting `Future` elements
Parameters:
`f` - a function that maps an element of the cross-product to a result
Returns:
an `Future` of mapped results

  - 

### yield

public Future<T1> yield()
A shortcut for `yield(Function.identity())`.

Returns:
an `Iterator` of mapped results