Package io.vavr

# Class API.For2List<T1,T2>

java.lang.Object
io.vavr.API.For2List<T1,T2>

Type Parameters:
`T1` - component type of `List` number 1
`T2` - component type of `List` number 2

Enclosing class:
`API`

---

public static class API.For2List<T1,T2>
extends Object
For-comprehension with two Lists.

- 

## Method Summary

Modifier and Type
Method
Description
`<R> List<R>`
`yield(@NonNull BiFunction<? super T1,? super T2,? extends R> f)`

Yields a result for elements of the cross-product of the underlying Lists.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### yield

public <R> List<R> yield(@NonNull BiFunction<? super T1,? super T2,? extends R> f)
Yields a result for elements of the cross-product of the underlying Lists.

Type Parameters:
`R` - type of the resulting `List` elements
Parameters:
`f` - a function that maps an element of the cross-product to a result
Returns:
an `List` of mapped results