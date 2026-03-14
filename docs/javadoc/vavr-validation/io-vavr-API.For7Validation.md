Package io.vavr

# Class API.For7Validation<L,T1,T2,T3,T4,T5,T6,T7>

java.lang.Object
io.vavr.API.For7Validation<L,T1,T2,T3,T4,T5,T6,T7>

Type Parameters:
`L` - The left-hand type of all `Validation`s
`T1` - component type of `Validation` number 1
`T2` - component type of `Validation` number 2
`T3` - component type of `Validation` number 3
`T4` - component type of `Validation` number 4
`T5` - component type of `Validation` number 5
`T6` - component type of `Validation` number 6
`T7` - component type of `Validation` number 7

Enclosing class:
`API`

---

public static class API.For7Validation<L,T1,T2,T3,T4,T5,T6,T7>
extends Object
For-comprehension with 7 Validations.

- 

## Method Summary

Modifier and Type
Method
Description
`<R> Validation<L,R>`
`yield(@NonNull Function7<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,? extends R> f)`

Yields a result for elements of the cross-product of the underlying Validations.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### yield

public <R> Validation<L,R> yield(@NonNull Function7<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,? extends R> f)
Yields a result for elements of the cross-product of the underlying Validations.

Type Parameters:
`R` - type of the resulting `Validation` elements
Parameters:
`f` - a function that maps an element of the cross-product to a result
Returns:
an `Validation` of mapped results