Package io.vavr.control

# Interface Option<T>

Type Parameters:
`T` - the type of the optional value

All Superinterfaces:
`Iterable<T>`, `Serializable`, `Value<T>`

All Known Implementing Classes:
`Option.None`, `Option.Some`

---

public interface Option<T>
extends Value<T>, Serializable
A replacement for `Optional`.
 

 `Option` is a monadic container type representing the presence or absence of a value.
 An instance is either a `Option.Some` holding a value or the singleton `Option.None`.
 

 The design is similar to `Optional` and related types in
 Haskell and
 Scala.

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Interface
Description
`static final class `
`Option.None<T>`

None is a singleton representation of the undefined `Option`.

`static final class `
`Option.Some<T>`

Some represents a defined `Option`.

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final long`
`serialVersionUID`

The serial version UID for serialization.

- 

## Method Summary

Modifier and Type
Method
Description
`default <R> Option<R>`
`collect(@NonNull PartialFunction<? super T,? extends R> partialFunction)`

Applies a `partialFunction` to the value of this `Option` if it is defined for that value,
 and wraps the result in a new `Option`.

`boolean`
`equals(Object o)`

Clarifies that values have a proper equals() method implemented.

`default Option<T>`
`filter(@NonNull Predicate<? super T> predicate)`

Returns `Some(value)` if this `Option` is a `Some` and the contained value satisfies the given predicate.

`default <U> Option<U>`
`flatMap(@NonNull Function<? super T,? extends Option<? extends U>> mapper)`

Transforms the value of this `Option` using the given mapper if it is a `Some`.

`default <U> U`
`fold(@NonNull Supplier<? extends U> ifNone,
 @NonNull Function<? super T,? extends U> f)`

Folds this `Option` into a single value by applying one of two functions:
 
     `ifNone` is applied if this is `None`
     `f` is applied to the contained value if this is `Some`
 

`T`
`get()`

Returns the value contained in this `Some`, or throws if this is `None`.

`default T`
`getOrElse(@NonNull Supplier<? extends T> supplier)`

Returns the value contained in this `Some`, or the value supplied by `supplier` if this is `None`.

`default T`
`getOrElse(T other)`

Returns the value contained in this `Some`, or the provided `other` value if this is `None`.

`default <X extends Throwable>
T`
`getOrElseThrow(@NonNull Supplier<X> exceptionSupplier)`

Returns the value contained in this `Some`, or throws an exception provided by `exceptionSupplier` if this is `None`.

`int`
`hashCode()`

Clarifies that values have a proper hashCode() method implemented.

`default boolean`
`isAsync()`

Indicates that an `Option`'s value is computed synchronously.

`default boolean`
`isDefined()`

Checks whether this `Option` contains a value.

`boolean`
`isEmpty()`

Checks whether this `Option` is empty.

`default boolean`
`isLazy()`

Indicates that an `Option`'s value is computed eagerly.

`default boolean`
`isSingleValued()`

Indicates that an `Option` contains exactly one value.

`default @NonNull Iterator<T>`
`iterator()`

Returns a rich `io.vavr.collection.Iterator`.

`default <U> Option<U>`
`map(@NonNull Function<? super T,? extends U> mapper)`

Transforms the value of this `Some` using the given mapper and wraps it in a new `Some`.

`default <U> Option<U>`
`mapTo(U value)`

Maps the underlying value to another fixed value.

`default Option<Void>`
`mapToVoid()`

Maps the underlying value to Void

`default <U> Try<U>`
`mapTry(@NonNull CheckedFunction1<? super T,? extends U> mapper)`

Converts this `Option` to a `Try`, then applies the given checked function if this is a `Try.Success`,
 passing the contained value to it.

`static <T> Option<T>`
`narrow(@NonNull Option<? extends T> option)`

Narrows a widened `Option<? extends T>` to `Option<T>` via a type-safe cast.

`static <T> Option<T>`
`none()`

Returns the singleton `None` instance.

`static <T> Option<T>`
`of(T value)`

Creates an `Option` from the given value.

`static <T> Option<T>`
`ofOptional(@NonNull Optional<? extends T> optional)`

Wraps a `Optional` in a new `Option`.

`default Option<T>`
`onEmpty(@NonNull Runnable action)`

Executes the given `Runnable` if this `Option` is empty (`None`).

`default Option<T>`
`orElse(@NonNull Option<? extends T> other)`

Returns this `Option` if it is non-empty, otherwise returns the provided alternative `Option`.

`default Option<T>`
`orElse(@NonNull Supplier<? extends Option<? extends T>> supplier)`

Returns this `Option` if it is non-empty; otherwise, returns the `Option` provided by the supplier.

`default Option<T>`
`peek(@NonNull Consumer<? super T> action)`

Executes the given action on the contained value if this `Option` is defined (`Some`),
 otherwise does nothing.

`static <T> Option<Seq<T>>`
`sequence(@NonNull Iterable<? extends Option<? extends T>> values)`

Reduces multiple `Option` values into a single `Option` by transforming
 an `Iterable<Option<? extends T>>` into an `Option<Seq<T>>`.

`static <T> Option<T>`
`some(T value)`

Creates a `Some` containing the given value.

`String`
`toString()`

Clarifies that values have a proper toString() method implemented.

`default <U> U`
`transform(@NonNull Function<? super Option<T>,? extends U> f)`

Transforms this `Option` into a value of type `U` using the given function.

`static <T,
U> Option<Seq<U>>`
`traverse(@NonNull Iterable<? extends T> values,
 @NonNull Function<? super T,? extends Option<? extends U>> mapper)`

Maps the elements of an iterable into `Option` values and collects the results
 into a single `Option`.

`static <T> Option<T>`
`when(boolean condition,
 @NonNull Supplier<? extends T> supplier)`

Returns `Some` of the value supplied by `supplier` if `condition` is true,
 or `None` if `condition` is false.

`static <T> Option<T>`
`when(boolean condition,
 T value)`

Returns `Some` of the given `value` if `condition` is true, or `None` otherwise.

### Methods inherited from interface io.vavr.Value

`collect, collect, contains, corresponds, eq, exists, forAll, forEach, getOrElseTry, getOrNull, out, out, spliterator, stderr, stdout, stringPrefix, toArray, toCharSeq, toCompletableFuture, toEither, toEither, toInvalid, toInvalid, toJavaArray, toJavaArray, toJavaArray, toJavaCollection, toJavaList, toJavaList, toJavaMap, toJavaMap, toJavaMap, toJavaOptional, toJavaParallelStream, toJavaSet, toJavaSet, toJavaStream, toLeft, toLeft, toLinkedMap, toLinkedMap, toLinkedSet, toList, toMap, toMap, toOption, toPriorityQueue, toPriorityQueue, toQueue, toRight, toRight, toSet, toSortedMap, toSortedMap, toSortedMap, toSortedMap, toSortedSet, toSortedSet, toStream, toTree, toTree, toTry, toTry, toValid, toValid, toValidation, toValidation, toVector`

- 

## Field Details

  - 

### serialVersionUID

static final long serialVersionUID
The serial version UID for serialization.

See Also:

    - Constant Field Values

- 

## Method Details

  - 

### of

static <T> Option<T> of(T value)
Creates an `Option` from the given value.

Type Parameters:
`T` - the value type
Parameters:
`value` - the value to wrap
Returns:
`Some(value)` if the value is non-null, otherwise `None`

  - 

### sequence

static <T> Option<Seq<T>> sequence(@NonNull Iterable<? extends Option<? extends T>> values)
Reduces multiple `Option` values into a single `Option` by transforming
 an `Iterable<Option<? extends T>>` into an `Option<Seq<T>>`.
 

 If any element is `Option.None`, the result is `None`.
 Otherwise, all contained values are collected into a `Seq` wrapped in `Some`.

Type Parameters:
`T` - the element type
Parameters:
`values` - an iterable of `Option` values
Returns:
an `Option` containing a `Seq` of all values, or `None` if any value is empty
Throws:
`NullPointerException` - if `values` is null

  - 

### traverse

static <T,
U> Option<Seq<U>> traverse(@NonNull Iterable<? extends T> values,
 @NonNull Function<? super T,? extends Option<? extends U>> mapper)
Maps the elements of an iterable into `Option` values and collects the results
 into a single `Option`.
 

 Each element is transformed using `mapper`.
 If any mapped value is `Option.None`, the result is `None`.
 Otherwise, all mapped values are accumulated into a `Seq` wrapped in `Some`.

Type Parameters:
`T` - the input element type
`U` - the mapped element type
Parameters:
`values` - an iterable of input values
`mapper` - a function mapping each value to an `Option`
Returns:
an `Option` containing a `Seq` of mapped values, or `None` if any mapping yields `None`
Throws:
`NullPointerException` - if `values` or `mapper` is null

  - 

### some

static <T> Option<T> some(T value)
Creates a `Some` containing the given value.
 

 Unlike `of(Object)`, this method preserves `null`:
 

```

 Option.of(null);   // yields None
 Option.some(null); // yields Some(null)
 
```

Type Parameters:
`T` - the value type
Parameters:
`value` - the value to wrap, possibly `null`
Returns:
a `Some` containing `value`

  - 

### none

static <T> Option<T> none()
Returns the singleton `None` instance.

Type Parameters:
`T` - the option's component type
Returns:
the singleton `None`

  - 

### narrow

static <T> Option<T> narrow(@NonNull Option<? extends T> option)
Narrows a widened `Option<? extends T>` to `Option<T>` via a type-safe cast.
 

 This is safe because immutable/read-only types are covariant.

Type Parameters:
`T` - the component type of the `Option`
Parameters:
`option` - the `Option` to narrow
Returns:
the same `Option` instance, cast to `Option<T>`

  - 

### when

static <T> Option<T> when(boolean condition,
 @NonNull Supplier<? extends T> supplier)
Returns `Some` of the value supplied by `supplier` if `condition` is true,
 or `None` if `condition` is false.

Type Parameters:
`T` - the type of the optional value
Parameters:
`condition` - the condition to test
`supplier` - a supplier of the value, may return `null`
Returns:
`Some` of the supplied value if `condition` is true, otherwise `None`
Throws:
`NullPointerException` - if `supplier` is null

  - 

### when

static <T> Option<T> when(boolean condition,
 T value)
Returns `Some` of the given `value` if `condition` is true, or `None` otherwise.

Type Parameters:
`T` - the type of the optional value
Parameters:
`condition` - the condition to test
`value` - the value to wrap, may be `null`
Returns:
`Some` of `value` if `condition` is true, otherwise `None`

  - 

### ofOptional

static <T> Option<T> ofOptional(@NonNull Optional<? extends T> optional)
Wraps a `Optional` in a new `Option`.

Type Parameters:
`T` - the type of the contained value
Parameters:
`optional` - the Java `Optional` to wrap
Returns:
`Some(optional.get())` if the `Optional` is present, otherwise `None`

  - 

### collect

default <R> Option<R> collect(@NonNull PartialFunction<? super T,? extends R> partialFunction)
Applies a `partialFunction` to the value of this `Option` if it is defined for that value,
 and wraps the result in a new `Option`.
 

 If the `partialFunction` is not defined for the value, `None` is returned.

 

```

 if (partialFunction.isDefinedAt(value)) {
     R newValue = partialFunction.apply(value);
     // wrapped in Some(newValue)
 }
 
```

Type Parameters:
`R` - the type of the mapped value
Parameters:
`partialFunction` - a function that may not be defined for all input values
Returns:
a new `Option` containing the mapped value if defined, otherwise `None`
Throws:
`NullPointerException` - if `partialFunction` is null

  - 

### isEmpty

boolean isEmpty()
Checks whether this `Option` is empty.

Specified by:
`isEmpty` in interface `Value<T>`
Returns:
`true` if this is `None`, `false` if this is `Some`

  - 

### onEmpty

default Option<T> onEmpty(@NonNull Runnable action)
Executes the given `Runnable` if this `Option` is empty (`None`).

Parameters:
`action` - a `Runnable` to execute
Returns:
this `Option`

  - 

### isAsync

default boolean isAsync()
Indicates that an `Option`'s value is computed synchronously.

Specified by:
`isAsync` in interface `Value<T>`
Returns:
`false`

  - 

### isDefined

default boolean isDefined()
Checks whether this `Option` contains a value.
 

 Note that `Some(null)` is considered defined.

Returns:
`true` if this is `Some`, `false` if this is `None`

  - 

### isLazy

default boolean isLazy()
Indicates that an `Option`'s value is computed eagerly.

Specified by:
`isLazy` in interface `Value<T>`
Returns:
`false`

  - 

### isSingleValued

default boolean isSingleValued()
Indicates that an `Option` contains exactly one value.

Specified by:
`isSingleValued` in interface `Value<T>`
Returns:
`true`

  - 

### get

T get()
Returns the value contained in this `Some`, or throws if this is `None`.

Specified by:
`get` in interface `Value<T>`
Returns:
the contained value
Throws:
`NoSuchElementException` - if this is `None`

  - 

### getOrElse

default T getOrElse(T other)
Returns the value contained in this `Some`, or the provided `other` value if this is `None`.
 

 Note that `other` is evaluated eagerly.

Specified by:
`getOrElse` in interface `Value<T>`
Parameters:
`other` - an alternative value to return if this is `None`
Returns:
the contained value if defined, otherwise `other`

  - 

### orElse

default Option<T> orElse(@NonNull Option<? extends T> other)
Returns this `Option` if it is non-empty, otherwise returns the provided alternative `Option`.

Parameters:
`other` - an alternative `Option` to return if this is `None`
Returns:
this `Option` if defined, otherwise `other`

  - 

### orElse

default Option<T> orElse(@NonNull Supplier<? extends Option<? extends T>> supplier)
Returns this `Option` if it is non-empty; otherwise, returns the `Option` provided by the supplier.

Parameters:
`supplier` - a supplier of an alternative `Option` if this is `None`
Returns:
this `Option` if defined, otherwise the result of `supplier.get()`
Throws:
`NullPointerException` - if `supplier` is null

  - 

### getOrElse

default T getOrElse(@NonNull Supplier<? extends T> supplier)
Returns the value contained in this `Some`, or the value supplied by `supplier` if this is `None`.
 

 The alternative value is evaluated lazily.

Specified by:
`getOrElse` in interface `Value<T>`
Parameters:
`supplier` - a supplier of an alternative value if this is `None`
Returns:
the contained value if defined, otherwise the value returned by `supplier`
Throws:
`NullPointerException` - if `supplier` is null

  - 

### getOrElseThrow

default <X extends Throwable> T getOrElseThrow(@NonNull Supplier<X> exceptionSupplier)
                                        throws X
Returns the value contained in this `Some`, or throws an exception provided by `exceptionSupplier` if this is `None`.

Specified by:
`getOrElseThrow` in interface `Value<T>`
Type Parameters:
`X` - the type of the exception
Parameters:
`exceptionSupplier` - a supplier of the exception to throw if this is `None`
Returns:
the contained value if defined
Throws:
`X` - if this `Option` is `None`
`NullPointerException` - if `exceptionSupplier` is null

  - 

### filter

default Option<T> filter(@NonNull Predicate<? super T> predicate)
Returns `Some(value)` if this `Option` is a `Some` and the contained value satisfies the given predicate.
 Otherwise, returns `None`.

Parameters:
`predicate` - a predicate to test the contained value
Returns:
`Some(value)` if the value satisfies the predicate, otherwise `None`
Throws:
`NullPointerException` - if `predicate` is null

  - 

### flatMap

default <U> Option<U> flatMap(@NonNull Function<? super T,? extends Option<? extends U>> mapper)
Transforms the value of this `Option` using the given mapper if it is a `Some`.
 Returns `None` if this is `None`.

Type Parameters:
`U` - the type of the resulting `Option`'s value
Parameters:
`mapper` - a function to transform the contained value
Returns:
a new `Option` containing the mapped value, or `None`
Throws:
`NullPointerException` - if `mapper` is null

  - 

### map

default <U> Option<U> map(@NonNull Function<? super T,? extends U> mapper)
Transforms the value of this `Some` using the given mapper and wraps it in a new `Some`.
 Returns `None` if this is `None`.

Specified by:
`map` in interface `Value<T>`
Type Parameters:
`U` - the type of the resulting `Some`'s value
Parameters:
`mapper` - a function to transform the contained value
Returns:
a new `Some` with the mapped value if this is defined, otherwise `None`
Throws:
`NullPointerException` - if `mapper` is null

  - 

### mapTo

default <U> Option<U> mapTo(U value)
Description copied from interface: `Value`
Maps the underlying value to another fixed value.

Specified by:
`mapTo` in interface `Value<T>`
Type Parameters:
`U` - The new component type
Parameters:
`value` - value to replace the contents with
Returns:
A new value

  - 

### mapToVoid

default Option<Void> mapToVoid()
Description copied from interface: `Value`
Maps the underlying value to Void

Specified by:
`mapToVoid` in interface `Value<T>`
Returns:
A new value of type Void

  - 

### mapTry

default <U> Try<U> mapTry(@NonNull CheckedFunction1<? super T,? extends U> mapper)
Converts this `Option` to a `Try`, then applies the given checked function if this is a `Try.Success`,
 passing the contained value to it.

Type Parameters:
`U` - the type of the resulting `Try`'s value
Parameters:
`mapper` - a checked function to transform the contained value
Returns:
a `Try` containing the mapped value if this `Option` is defined, otherwise a `Try.Failure`
Throws:
`NullPointerException` - if `mapper` is null

  - 

### fold

default <U> U fold(@NonNull Supplier<? extends U> ifNone,
 @NonNull Function<? super T,? extends U> f)
Folds this `Option` into a single value by applying one of two functions:
 

     
    - `ifNone` is applied if this is `None`
     
    - `f` is applied to the contained value if this is `Some`
 

Type Parameters:
`U` - the type of the folded result
Parameters:
`ifNone` - a function to produce a value if this is `None`
`f` - a function to transform the contained value if this is `Some`
Returns:
the result of applying `f` or `ifNone` depending on whether this is `Some` or `None`
Throws:
`NullPointerException` - if `ifNone` or `f` is null

  - 

### peek

default Option<T> peek(@NonNull Consumer<? super T> action)
Executes the given action on the contained value if this `Option` is defined (`Some`),
 otherwise does nothing.

Specified by:
`peek` in interface `Value<T>`
Parameters:
`action` - a consumer to apply to the contained value
Returns:
this `Option`
Throws:
`NullPointerException` - if `action` is null

  - 

### transform

default <U> U transform(@NonNull Function<? super Option<T>,? extends U> f)
Transforms this `Option` into a value of type `U` using the given function.

Type Parameters:
`U` - the type of the result
Parameters:
`f` - a function to transform this `Option`
Returns:
the result of applying `f` to this `Option`
Throws:
`NullPointerException` - if `f` is null

  - 

### iterator

default @NonNull Iterator<T> iterator()
Description copied from interface: `Value`
Returns a rich `io.vavr.collection.Iterator`.

Specified by:
`iterator` in interface `Iterable<T>`
Specified by:
`iterator` in interface `Value<T>`
Returns:
A new Iterator

  - 

### equals

boolean equals(Object o)
Description copied from interface: `Value`
Clarifies that values have a proper equals() method implemented.
 

 See Object.equals(Object).

Specified by:
`equals` in interface `Value<T>`
Overrides:
`equals` in class `Object`
Parameters:
`o` - An object
Returns:
true, if this equals o, false otherwise

  - 

### hashCode

int hashCode()
Description copied from interface: `Value`
Clarifies that values have a proper hashCode() method implemented.
 

 See Object.hashCode().

Specified by:
`hashCode` in interface `Value<T>`
Overrides:
`hashCode` in class `Object`
Returns:
The hashcode of this object

  - 

### toString

String toString()
Description copied from interface: `Value`
Clarifies that values have a proper toString() method implemented.
 

 See Object.toString().

Specified by:
`toString` in interface `Value<T>`
Overrides:
`toString` in class `Object`
Returns:
A String representation of this object