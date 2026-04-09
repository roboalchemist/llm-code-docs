Package io.vavr

# Class API.For1Option<T1>

java.lang.Object
io.vavr.API.For1Option<T1>

Type Parameters:
`T1` - component type of `Option` number 1

Enclosing class:
`API`

---

public static class API.For1Option<T1>
extends Object
For-comprehension with one Option.

- 

## Method Summary

Modifier and Type
Method
Description
`Option<T1>`
`yield()`

A shortcut for `yield(Function.identity())`.

`<R> Option<R>`
`yield(@NonNull Function<? super T1,? extends R> f)`

Yields a result for elements of the cross-product of the underlying Option.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### yield

public <R> Option<R> yield(@NonNull Function<? super T1,? extends R> f)
Yields a result for elements of the cross-product of the underlying Option.

Type Parameters:
`R` - type of the resulting `Option` elements
Parameters:
`f` - a function that maps an element of the cross-product to a result
Returns:
an `Option` of mapped results

  - 

### yield

public Option<T1> yield()
A shortcut for `yield(Function.identity())`.

Returns:
an `Iterator` of mapped results