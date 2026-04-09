Package io.vavr

# Class API.For6Try<T1,T2,T3,T4,T5,T6>

java.lang.Object
io.vavr.API.For6Try<T1,T2,T3,T4,T5,T6>

Type Parameters:
`T1` - component type of `Try` number 1
`T2` - component type of `Try` number 2
`T3` - component type of `Try` number 3
`T4` - component type of `Try` number 4
`T5` - component type of `Try` number 5
`T6` - component type of `Try` number 6

Enclosing class:
`API`

---

public static class API.For6Try<T1,T2,T3,T4,T5,T6>
extends Object
For-comprehension with 6 Trys.

- 

## Method Summary

Modifier and Type
Method
Description
`<R> Try<R>`
`yield(@NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? extends R> f)`

Yields a result for elements of the cross-product of the underlying Trys.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### yield

public <R> Try<R> yield(@NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? extends R> f)
Yields a result for elements of the cross-product of the underlying Trys.

Type Parameters:
`R` - type of the resulting `Try` elements
Parameters:
`f` - a function that maps an element of the cross-product to a result
Returns:
an `Try` of mapped results