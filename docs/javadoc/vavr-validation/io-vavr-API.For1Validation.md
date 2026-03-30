Package io.vavr

# Class API.For1Validation<L,T1>

java.lang.Object
io.vavr.API.For1Validation<L,T1>

Type Parameters:
`L` - The left-hand type of all `Validation`s
`T1` - component type of `Validation` number 1

Enclosing class:
`API`

---

public static class API.For1Validation<L,T1>
extends Object
For-comprehension with one Validation.

- 

## Method Summary

Modifier and Type
Method
Description
`Validation<L,T1>`
`yield()`

A shortcut for `yield(Function.identity())`.

`<R> Validation<L,R>`
`yield(@NonNull Function<? super T1,? extends R> f)`

Yields a result for elements of the cross-product of the underlying Validation.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### yield

public <R> Validation<L,R> yield(@NonNull Function<? super T1,? extends R> f)
Yields a result for elements of the cross-product of the underlying Validation.

Type Parameters:
`R` - type of the resulting `Validation` elements
Parameters:
`f` - a function that maps an element of the cross-product to a result
Returns:
an `Validation` of mapped results

  - 

### yield

public Validation<L,T1> yield()
A shortcut for `yield(Function.identity())`.

Returns:
an `Iterator` of mapped results