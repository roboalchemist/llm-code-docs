Package io.vavr

# Class API.For2Either<L,T1,T2>

java.lang.Object
io.vavr.API.For2Either<L,T1,T2>

Type Parameters:
`L` - The left-hand type of all `Either`s
`T1` - component type of `Either` number 1
`T2` - component type of `Either` number 2

Enclosing class:
`API`

---

public static class API.For2Either<L,T1,T2>
extends Object
For-comprehension with two Eithers.

- 

## Method Summary

Modifier and Type
Method
Description
`<R> Either<L,R>`
`yield(@NonNull BiFunction<? super T1,? super T2,? extends R> f)`

Yields a result for elements of the cross-product of the underlying Eithers.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### yield

public <R> Either<L,R> yield(@NonNull BiFunction<? super T1,? super T2,? extends R> f)
Yields a result for elements of the cross-product of the underlying Eithers.

Type Parameters:
`R` - type of the resulting `Either` elements
Parameters:
`f` - a function that maps an element of the cross-product to a result
Returns:
an `Either` of mapped results