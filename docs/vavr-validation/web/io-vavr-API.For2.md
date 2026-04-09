Package io.vavr

# Class API.For2<T1,T2>

java.lang.Object
io.vavr.API.For2<T1,T2>

Type Parameters:
`T1` - component type of `Iterable` number 1
`T2` - component type of `Iterable` number 2

Enclosing class:
`API`

---

public static class API.For2<T1,T2>
extends Object
For-comprehension with two Iterables.

- 

## Method Summary

Modifier and Type
Method
Description
`<R> Iterator<R>`
`yield(@NonNull BiFunction<? super T1,? super T2,? extends R> f)`

Yields a result for elements of the cross-product of the underlying Iterables.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### yield

public <R> Iterator<R> yield(@NonNull BiFunction<? super T1,? super T2,? extends R> f)
Yields a result for elements of the cross-product of the underlying Iterables.

Type Parameters:
`R` - type of the resulting `Iterator` elements
Parameters:
`f` - a function that maps an element of the cross-product to a result
Returns:
an `Iterator` of mapped results