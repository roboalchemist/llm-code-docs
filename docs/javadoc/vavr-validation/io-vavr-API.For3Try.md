Package io.vavr

# Class API.For3Try<T1,T2,T3>

java.lang.Object
io.vavr.API.For3Try<T1,T2,T3>

Type Parameters:
`T1` - component type of `Try` number 1
`T2` - component type of `Try` number 2
`T3` - component type of `Try` number 3

Enclosing class:
`API`

---

public static class API.For3Try<T1,T2,T3>
extends Object
For-comprehension with three Trys.

- 

## Method Summary

Modifier and Type
Method
Description
`<R> Try<R>`
`yield(@NonNull Function3<? super T1,? super T2,? super T3,? extends R> f)`

Yields a result for elements of the cross-product of the underlying Trys.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### yield

public <R> Try<R> yield(@NonNull Function3<? super T1,? super T2,? super T3,? extends R> f)
Yields a result for elements of the cross-product of the underlying Trys.

Type Parameters:
`R` - type of the resulting `Try` elements
Parameters:
`f` - a function that maps an element of the cross-product to a result
Returns:
an `Try` of mapped results