Package io.vavr

# Class API.For1Either<L,T1>

java.lang.Object
io.vavr.API.For1Either<L,T1>

Type Parameters:
`L` - The left-hand type of all `Either`s
`T1` - component type of `Either` number 1

Enclosing class:
`API`

---

public static class API.For1Either<L,T1>
extends Object
For-comprehension with one Either.

- 

## Method Summary

Modifier and Type
Method
Description
`Either<L,T1>`
`yield()`

A shortcut for `yield(Function.identity())`.

`<R> Either<L,R>`
`yield(@NonNull Function<? super T1,? extends R> f)`

Yields a result for elements of the cross-product of the underlying Either.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### yield

public <R> Either<L,R> yield(@NonNull Function<? super T1,? extends R> f)
Yields a result for elements of the cross-product of the underlying Either.

Type Parameters:
`R` - type of the resulting `Either` elements
Parameters:
`f` - a function that maps an element of the cross-product to a result
Returns:
an `Either` of mapped results

  - 

### yield

public Either<L,T1> yield()
A shortcut for `yield(Function.identity())`.

Returns:
an `Iterator` of mapped results