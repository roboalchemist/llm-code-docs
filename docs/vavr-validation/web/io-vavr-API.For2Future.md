Package io.vavr

# Class API.For2Future<T1,T2>

java.lang.Object
io.vavr.API.For2Future<T1,T2>

Type Parameters:
`T1` - component type of `Future` number 1
`T2` - component type of `Future` number 2

Enclosing class:
`API`

---

public static class API.For2Future<T1,T2>
extends Object
For-comprehension with two Futures.

- 

## Method Summary

Modifier and Type
Method
Description
`<R> Future<R>`
`yield(@NonNull BiFunction<? super T1,? super T2,? extends R> f)`

Yields a result for elements of the cross-product of the underlying Futures.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### yield

public <R> Future<R> yield(@NonNull BiFunction<? super T1,? super T2,? extends R> f)
Yields a result for elements of the cross-product of the underlying Futures.

Type Parameters:
`R` - type of the resulting `Future` elements
Parameters:
`f` - a function that maps an element of the cross-product to a result
Returns:
an `Future` of mapped results