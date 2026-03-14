Package io.vavr

# Class API.For2Validation<L,T1,T2>

java.lang.Object
io.vavr.API.For2Validation<L,T1,T2>

Type Parameters:
`L` - The left-hand type of all `Validation`s
`T1` - component type of `Validation` number 1
`T2` - component type of `Validation` number 2

Enclosing class:
`API`

---

public static class API.For2Validation<L,T1,T2>
extends Object
For-comprehension with two Validations.

- 

## Method Summary

Modifier and Type
Method
Description
`<R> Validation<L,R>`
`yield(@NonNull BiFunction<? super T1,? super T2,? extends R> f)`

Yields a result for elements of the cross-product of the underlying Validations.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### yield

public <R> Validation<L,R> yield(@NonNull BiFunction<? super T1,? super T2,? extends R> f)
Yields a result for elements of the cross-product of the underlying Validations.

Type Parameters:
`R` - type of the resulting `Validation` elements
Parameters:
`f` - a function that maps an element of the cross-product to a result
Returns:
an `Validation` of mapped results