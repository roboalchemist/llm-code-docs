Package io.vavr

# Class API.For7Option<T1,T2,T3,T4,T5,T6,T7>

java.lang.Object
io.vavr.API.For7Option<T1,T2,T3,T4,T5,T6,T7>

Type Parameters:
`T1` - component type of `Option` number 1
`T2` - component type of `Option` number 2
`T3` - component type of `Option` number 3
`T4` - component type of `Option` number 4
`T5` - component type of `Option` number 5
`T6` - component type of `Option` number 6
`T7` - component type of `Option` number 7

Enclosing class:
`API`

---

public static class API.For7Option<T1,T2,T3,T4,T5,T6,T7>
extends Object
For-comprehension with 7 Options.

- 

## Method Summary

Modifier and Type
Method
Description
`<R> Option<R>`
`yield(@NonNull Function7<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,? extends R> f)`

Yields a result for elements of the cross-product of the underlying Options.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### yield

public <R> Option<R> yield(@NonNull Function7<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,? extends R> f)
Yields a result for elements of the cross-product of the underlying Options.

Type Parameters:
`R` - type of the resulting `Option` elements
Parameters:
`f` - a function that maps an element of the cross-product to a result
Returns:
an `Option` of mapped results