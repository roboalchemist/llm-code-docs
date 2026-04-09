Package io.vavr

# Class API.For3Either<L,T1,T2,T3>

java.lang.Object
io.vavr.API.For3Either<L,T1,T2,T3>

Type Parameters:
`L` - The left-hand type of all `Either`s
`T1` - component type of `Either` number 1
`T2` - component type of `Either` number 2
`T3` - component type of `Either` number 3

Enclosing class:
`API`

---

public static class API.For3Either<L,T1,T2,T3>
extends Object
For-comprehension with three Eithers.

- 

## Method Summary

Modifier and Type
Method
Description
`<R> Either<L,R>`
`yield(@NonNull Function3<? super T1,? super T2,? super T3,? extends R> f)`

Yields a result for elements of the cross-product of the underlying Eithers.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### yield

public <R> Either<L,R> yield(@NonNull Function3<? super T1,? super T2,? super T3,? extends R> f)
Yields a result for elements of the cross-product of the underlying Eithers.

Type Parameters:
`R` - type of the resulting `Either` elements
Parameters:
`f` - a function that maps an element of the cross-product to a result
Returns:
an `Either` of mapped results