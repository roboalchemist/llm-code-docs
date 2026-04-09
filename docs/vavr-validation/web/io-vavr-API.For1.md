Package io.vavr

# Class API.For1<T1>

java.lang.Object
io.vavr.API.For1<T1>

Type Parameters:
`T1` - component type of `Iterable` number 1

Enclosing class:
`API`

---

public static class API.For1<T1>
extends Object
For-comprehension with one Iterable.

- 

## Method Summary

Modifier and Type
Method
Description
`Iterator<T1>`
`yield()`

A shortcut for `yield(Function.identity())`.

`<R> Iterator<R>`
`yield(@NonNull Function<? super T1,? extends R> f)`

Yields a result for elements of the cross-product of the underlying Iterable.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### yield

public <R> Iterator<R> yield(@NonNull Function<? super T1,? extends R> f)
Yields a result for elements of the cross-product of the underlying Iterable.

Type Parameters:
`R` - type of the resulting `Iterator` elements
Parameters:
`f` - a function that maps an element of the cross-product to a result
Returns:
an `Iterator` of mapped results

  - 

### yield

public Iterator<T1> yield()
A shortcut for `yield(Function.identity())`.

Returns:
an `Iterator` of mapped results