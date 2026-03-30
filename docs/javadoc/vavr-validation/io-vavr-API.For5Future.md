Package io.vavr

# Class API.For5Future<T1,T2,T3,T4,T5>

java.lang.Object
io.vavr.API.For5Future<T1,T2,T3,T4,T5>

Type Parameters:
`T1` - component type of `Future` number 1
`T2` - component type of `Future` number 2
`T3` - component type of `Future` number 3
`T4` - component type of `Future` number 4
`T5` - component type of `Future` number 5

Enclosing class:
`API`

---

public static class API.For5Future<T1,T2,T3,T4,T5>
extends Object
For-comprehension with 5 Futures.

- 

## Method Summary

Modifier and Type
Method
Description
`<R> Future<R>`
`yield(@NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,? extends R> f)`

Yields a result for elements of the cross-product of the underlying Futures.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### yield

public <R> Future<R> yield(@NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,? extends R> f)
Yields a result for elements of the cross-product of the underlying Futures.

Type Parameters:
`R` - type of the resulting `Future` elements
Parameters:
`f` - a function that maps an element of the cross-product to a result
Returns:
an `Future` of mapped results