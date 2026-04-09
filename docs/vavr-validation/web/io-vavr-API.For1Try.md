Package io.vavr

# Class API.For1Try<T1>

java.lang.Object
io.vavr.API.For1Try<T1>

Type Parameters:
`T1` - component type of `Try` number 1

Enclosing class:
`API`

---

public static class API.For1Try<T1>
extends Object
For-comprehension with one Try.

- 

## Method Summary

Modifier and Type
Method
Description
`Try<T1>`
`yield()`

A shortcut for `yield(Function.identity())`.

`<R> Try<R>`
`yield(@NonNull Function<? super T1,? extends R> f)`

Yields a result for elements of the cross-product of the underlying Try.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### yield

public <R> Try<R> yield(@NonNull Function<? super T1,? extends R> f)
Yields a result for elements of the cross-product of the underlying Try.

Type Parameters:
`R` - type of the resulting `Try` elements
Parameters:
`f` - a function that maps an element of the cross-product to a result
Returns:
an `Try` of mapped results

  - 

### yield

public Try<T1> yield()
A shortcut for `yield(Function.identity())`.

Returns:
an `Iterator` of mapped results