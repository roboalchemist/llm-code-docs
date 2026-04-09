Package io.vavr

# Class API.For1List<T1>

java.lang.Object
io.vavr.API.For1List<T1>

Type Parameters:
`T1` - component type of `List` number 1

Enclosing class:
`API`

---

public static class API.For1List<T1>
extends Object
For-comprehension with one List.

- 

## Method Summary

Modifier and Type
Method
Description
`List<T1>`
`yield()`

A shortcut for `yield(Function.identity())`.

`<R> List<R>`
`yield(@NonNull Function<? super T1,? extends R> f)`

Yields a result for elements of the cross-product of the underlying List.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### yield

public <R> List<R> yield(@NonNull Function<? super T1,? extends R> f)
Yields a result for elements of the cross-product of the underlying List.

Type Parameters:
`R` - type of the resulting `List` elements
Parameters:
`f` - a function that maps an element of the cross-product to a result
Returns:
an `List` of mapped results

  - 

### yield

public List<T1> yield()
A shortcut for `yield(Function.identity())`.

Returns:
an `Iterator` of mapped results