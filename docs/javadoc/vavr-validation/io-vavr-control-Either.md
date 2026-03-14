Package io.vavr.control

# Interface Either<L,R>

Type Parameters:
`L` - The type of the Left value.
`R` - The type of the Right value.

All Superinterfaces:
`Iterable<R>`, `Serializable`, `Value<R>`

All Known Implementing Classes:
`Either.Left`, `Either.Right`

---

public interface Either<L,R>
extends Value<R>, Serializable
Represents a value of one of two possible types: `Either.Left` or `Either.Right`.
 

 An `Either<L, R>` is typically used to model a computation that may result in either
 a success (represented by `Right`) or a failure (represented by `Left`).
 

 This implementation is **right-biased**, meaning that most operations such as
 `map`, `flatMap`, `filter`, etc., are defined for the `Right` projection.
 This makes `Either` behave like a monad over its `Right` type, and enables fluent
 chaining of computations in the successful case.

 
## Example

 

 Suppose we have a `compute()` function that returns an `Either<String, Integer>`,
 where `Right` represents a successful result and `Left` holds an error message.

 

```

 Either<String, Integer> result = compute().map(i -> i * 2);
 
```

 

 If `compute()` returns `Right(1)`, the result will be `Right(2)`.

 If `compute()` returns `Left("error")`, the result will remain `Left("error")`.

 
## Projection Semantics

 

   
- If an `Either` is a `Right` and projected to `Left`, operations on `Left` are no-ops.
   
- If an `Either` is a `Left` and projected to `Right`, operations on `Right` are no-ops.
   
- Operations on the matching projection are applied as expected.
 

Author:
Daniel Dietrich, Grzegorz Piwowarek, Adam KopeÄ

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Interface
Description
`static class `
`Either.Failure`

An exception wrapper used to propagate values through exception handling mechanisms.

`static final class `
`Either.Left<L,R>`

The `Left` version of an `Either`.

`static final class `
`Either.LeftProjection<L,R>`

Deprecated.
Either is right-biased.

`static final class `
`Either.Right<L,R>`

The `Right` version of an `Either`.

`static final class `
`Either.RightProjection<L,R>`

Deprecated.
Either is right-biased.

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
`default <X,
Y> Either<X,Y>`
`bimap(@NonNull Function<? super L,? extends X> leftMapper,
 @NonNull Function<? super R,? extends Y> rightMapper)`

Transforms the value of this `Either` by applying one of the given mapping functions.

`static <L,
R> Either<L,R>`
`cond(boolean test,
 @NonNull R right,
 @NonNull L left)`

Returns an `Either<L, R>` based on the given test condition.

`static <L,
R> Either<L,R>`
`cond(boolean test,
 @NonNull Supplier<? extends R> right,
 @NonNull Supplier<? extends L> left)`

Returns an `Either<L, R>` based on the given test condition.

`boolean`
`equals(Object o)`

Clarifies that values have a proper equals() method implemented.

`default Option<Either<L,R>>`
`filter(@NonNull Predicate<? super R> predicate)`

Returns an `Option` describing the right value of this right-biased `Either`
 if it satisfies the given predicate.

`default Either<L,R>`
`filterOrElse(@NonNull Predicate<? super R> predicate,
 @NonNull Function<? super R,? extends L> zero)`

Filters this right-biased `Either` using the given predicate.

`default <U> Either<L,U>`
`flatMap(@NonNull Function<? super R,? extends Either<L,? extends U>> mapper)`

Applies a flat-mapping function to the right value of this right-biased `Either`.

`default <U> U`
`fold(@NonNull Function<? super L,? extends U> leftMapper,
 @NonNull Function<? super R,? extends U> rightMapper)`

Reduces this `Either` to a single value by applying one of the given functions.

`R`
`get()`

Returns the right value if this is a `Right`; otherwise throws.

`L`
`getLeft()`

Returns the left value of this `Either`.

`default R`
`getOrElseGet(@NonNull Function<? super L,? extends R> other)`

Returns the right value of this `Either`, or an alternative value if this is a `Either.Left`.

`default <X extends Throwable>
R`
`getOrElseThrow(@NonNull Function<? super L,X> exceptionFunction)`

Returns the right value of this `Either`, or throws an exception if it is a `Either.Left`.

`int`
`hashCode()`

Clarifies that values have a proper hashCode() method implemented.

`default boolean`
`isAsync()`

Indicates that a right-biased `Either` computes its value synchronously.

`default boolean`
`isEmpty()`

Checks, this `Value` is empty, i.e. if the underlying value is absent.

`default boolean`
`isLazy()`

Indicates that a right-biased `Either` computes its value eagerly.

`boolean`
`isLeft()`

Checks whether this `Either` is a `Either.Left`.

`boolean`
`isRight()`

Checks whether this `Either` is a `Either.Right`.

`default boolean`
`isSingleValued()`

Indicates that a right-biased `Either` contains exactly one value.

`default @NonNull Iterator<R>`
`iterator()`

Returns a rich `io.vavr.collection.Iterator`.

`default Either.LeftProjection<L,R>`
`left()`

Deprecated.
Either is right-biased.

`static <L,
R> Either<L,R>`
`left(L left)`

Constructs a new `Either.Left` instance containing the given value.

`default <U> Either<L,U>`
`map(@NonNull Function<? super R,? extends U> mapper)`

Transforms the right value of this `Either` using the given mapping function.

`default <U> Either<U,R>`
`mapLeft(@NonNull Function<? super L,? extends U> leftMapper)`

Transforms the left value of this `Either` using the given mapping function.

`default <U> Either<L,U>`
`mapTo(U value)`

Maps the underlying value to another fixed value.

`default Either<L,Void>`
`mapToVoid()`

Maps the underlying value to Void

`static <L,
R> Either<L,R>`
`narrow(Either<? extends L,? extends R> either)`

Narrows a `Either<? extends L, ? extends R>` to `Either<L, R>` via a type-safe cast.

`default Either<L,R>`
`orElse(@NonNull Either<? extends L,? extends R> other)`

Returns this `Either` if it is a `Either.Right`, otherwise returns the given `other` Either.

`default Either<L,R>`
`orElse(@NonNull Supplier<? extends Either<? extends L,? extends R>> supplier)`

Returns this `Either` if it is a `Either.Right`, otherwise returns the result of evaluating the given `supplier`.

`default void`
`orElseRun(@NonNull Consumer<? super L> action)`

Executes the given action if this projection represents a `Either.Left` value.

`default Either<L,R>`
`peek(@NonNull Consumer<? super R> action)`

Performs the given `action` on the first element if this is an *eager* implementation.

`default Either<L,R>`
`peekLeft(@NonNull Consumer<? super L> action)`

Performs the given action on the left value if this is a `Either.Left`.

`default Either.RightProjection<L,R>`
`right()`

Deprecated.
Either is right-biased.

`static <L,
R> Either<L,R>`
`right(R right)`

Constructs a new `Either.Right` instance containing the given value.

`static <L,
R> Either<Seq<L>,Seq<R>>`
`sequence(@NonNull Iterable<? extends Either<? extends L,? extends R>> eithers)`

Transforms an `Iterable` of `Either<L, R>` into a single `Either<Seq<L>, Seq<R>>`.

`static <L,
R> Either<L,Seq<R>>`
`sequenceRight(@NonNull Iterable<? extends Either<? extends L,? extends R>> eithers)`

Transforms an `Iterable` of `Either<L, R>` into a single `Either<L, Seq<R>>`.

`default Either<R,L>`
`swap()`

Swaps the sides of this `Either`, converting a `Either.Left` to a `Either.Right`
 and vice versa.

`String`
`toString()`

Clarifies that values have a proper toString() method implemented.

`default Try<R>`
`toTry()`

Converts this to a `Try`.

`default Validation<L,R>`
`toValidation()`

Returns this as `Validation`.

`static <L,
R,
T> Either<Seq<L>,Seq<R>>`
`traverse(@NonNull Iterable<? extends T> values,
 @NonNull Function<? super T,? extends Either<? extends L,? extends R>> mapper)`

Transforms an `Iterable` of values into a single `Either<Seq<L>, Seq<R>>` by applying a mapping function 
 that returns an `Either` for each value.

`static <L,
R,
T> Either<L,Seq<R>>`
`traverseRight(@NonNull Iterable<? extends T> values,
 @NonNull Function<? super T,? extends Either<? extends L,? extends R>> mapper)`

Transforms an `Iterable` of values into a single `Either<Seq<L>, Seq<R>>` by applying a mapping 
 function that returns an `Either` for each element.

### Methods inherited from interface io.vavr.Value

`collect, collect, contains, corresponds, eq, exists, forAll, forEach, getOrElse, getOrElse, getOrElseThrow, getOrElseTry, getOrNull, out, out, spliterator, stderr, stdout, stringPrefix, toArray, toCharSeq, toCompletableFuture, toEither, toEither, toInvalid, toInvalid, toJavaArray, toJavaArray, toJavaArray, toJavaCollection, toJavaList, toJavaList, toJavaMap, toJavaMap, toJavaMap, toJavaOptional, toJavaParallelStream, toJavaSet, toJavaSet, toJavaStream, toLeft, toLeft, toLinkedMap, toLinkedMap, toLinkedSet, toList, toMap, toMap, toOption, toPriorityQueue, toPriorityQueue, toQueue, toRight, toRight, toSet, toSortedMap, toSortedMap, toSortedMap, toSortedMap, toSortedSet, toSortedSet, toStream, toTree, toTree, toTry, toValid, toValid, toValidation, toValidation, toVector`

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

### right

static <L,
R> Either<L,R> right(R right)
Constructs a new `Either.Right` instance containing the given value.

Type Parameters:
`L` - the type of the left value
`R` - the type of the right value
Parameters:
`right` - the value to store in the `Right`
Returns:
a new `Right` instance

  - 

### left

static <L,
R> Either<L,R> left(L left)
Constructs a new `Either.Left` instance containing the given value.

Type Parameters:
`L` - the type of the left value
`R` - the type of the right value
Parameters:
`left` - the value to store in the `Left`
Returns:
a new `Left` instance

  - 

### narrow

static <L,
R> Either<L,R> narrow(Either<? extends L,? extends R> either)
Narrows a `Either<? extends L, ? extends R>` to `Either<L, R>` via a type-safe cast.
 This is safe because immutable or read-only collections are covariant.

Type Parameters:
`L` - the type of the left value
`R` - the type of the right value
Parameters:
`either` - the `Either` to narrow
Returns:
the same `either` instance cast to `Either<L, R>`

  - 

### cond

static <L,
R> Either<L,R> cond(boolean test,
 @NonNull Supplier<? extends R> right,
 @NonNull Supplier<? extends L> left)
Returns an `Either<L, R>` based on the given test condition.
 

   
    - If `test` is `true`, the result is a `Either.Right` created from `right`.
   
    - If `test` is `false`, the result is a `Either.Left` created from `left`.
 

Type Parameters:
`L` - the type of the left value
`R` - the type of the right value
Parameters:
`test` - the boolean condition to evaluate
`right` - a `Supplier<? extends R>` providing the right value if `test` is true
`left` - a `Supplier<? extends L>` providing the left value if `test` is false
Returns:
an `Either<L, R>` containing the left or right value depending on `test`
Throws:
`NullPointerException` - if any argument is null

  - 

### cond

static <L,
R> Either<L,R> cond(boolean test,
 @NonNull R right,
 @NonNull L left)
Returns an `Either<L, R>` based on the given test condition.
 

   
    - If `test` is `true`, the result is a `Either.Right` containing `right`.
   
    - If `test` is `false`, the result is a `Either.Left` containing `left`.
 

Type Parameters:
`L` - the type of the left value
`R` - the type of the right value
Parameters:
`test` - the boolean condition to evaluate
`right` - the `R` value to return if `test` is true
`left` - the `L` value to return if `test` is false
Returns:
an `Either<L, R>` containing either the left or right value depending on `test`
Throws:
`NullPointerException` - if any argument is null

  - 

### getLeft

L getLeft()
Returns the left value of this `Either`.

Returns:
the left value
Throws:
`NoSuchElementException` - if this `Either` is a `Either.Right`

  - 

### isLeft

boolean isLeft()
Checks whether this `Either` is a `Either.Left`.

Returns:
`true` if this is a `Left`, `false` otherwise

  - 

### isRight

boolean isRight()
Checks whether this `Either` is a `Either.Right`.

Returns:
`true` if this is a `Right`, `false` otherwise

  - 

### left

@Deprecated
default Either.LeftProjection<L,R> left()
Deprecated.
Either is right-biased. Use `swap()` instead of projections.

Returns a LeftProjection of this Either.

Returns:
a new LeftProjection of this

  - 

### right

@Deprecated
default Either.RightProjection<L,R> right()
Deprecated.
Either is right-biased. Use `swap()` instead of projections.

Returns a RightProjection of this Either.

Returns:
a new RightProjection of this

  - 

### bimap

default <X,
Y> Either<X,Y> bimap(@NonNull Function<? super L,? extends X> leftMapper,
 @NonNull Function<? super R,? extends Y> rightMapper)
Transforms the value of this `Either` by applying one of the given mapping functions.
 

   
    - If this is a `Either.Left`, `leftMapper` is applied to the left value.
   
    - If this is a `Either.Right`, `rightMapper` is applied to the right value.
 

Type Parameters:
`X` - the type of the left value in the resulting `Either`
`Y` - the type of the right value in the resulting `Either`
Parameters:
`leftMapper` - function to transform the left value if this is a `Left`
`rightMapper` - function to transform the right value if this is a `Right`
Returns:
a new `Either` instance with the transformed value

  - 

### fold

default <U> U fold(@NonNull Function<? super L,? extends U> leftMapper,
 @NonNull Function<? super R,? extends U> rightMapper)
Reduces this `Either` to a single value by applying one of the given functions.
 

   
    - If this is a `Either.Left`, `leftMapper` is applied to the left value.
   
    - If this is a `Either.Right`, `rightMapper` is applied to the right value.
 

Type Parameters:
`U` - the type of the resulting value
Parameters:
`leftMapper` - function to transform the left value if this is a `Left`
`rightMapper` - function to transform the right value if this is a `Right`
Returns:
a value of type `U` obtained by applying the appropriate function

  - 

### sequence

static <L,
R> Either<Seq<L>,Seq<R>> sequence(@NonNull Iterable<? extends Either<? extends L,? extends R>> eithers)
Transforms an `Iterable` of `Either<L, R>` into a single `Either<Seq<L>, Seq<R>>`.
 

 If any of the given `Either`s is a `Either.Left`, the result is a `Either.Left`
 containing a non-empty `Seq` of all left values.
 

 If all of the given `Either`s are `Either.Right`, the result is a `Either.Right`
 containing a (possibly empty) `Seq` of all right values.

 

```

 // = Right(Seq())
 Either.sequence(List.empty())

 // = Right(Seq(1, 2))
 Either.sequence(List.of(Either.right(1), Either.right(2)))

 // = Left(Seq("x"))
 Either.sequence(List.of(Either.right(1), Either.left("x")))
 
```

Type Parameters:
`L` - the common type of left values
`R` - the common type of right values
Parameters:
`eithers` - an `Iterable` of `Either` instances
Returns:
an `Either` containing a `Seq` of left values if any `Either` was a `Either.Left`, 
         otherwise a `Seq` of right values
Throws:
`NullPointerException` - if `eithers` is null

  - 

### traverse

static <L,
R,
T> Either<Seq<L>,Seq<R>> traverse(@NonNull Iterable<? extends T> values,
 @NonNull Function<? super T,? extends Either<? extends L,? extends R>> mapper)
Transforms an `Iterable` of values into a single `Either<Seq<L>, Seq<R>>` by applying a mapping function 
 that returns an `Either` for each value.
 

 If the mapper returns any `Either.Left`, the resulting `Either` is a `Either.Left`
 containing a `Seq` of all left values. Otherwise, the result is a `Either.Right` containing 
 a `Seq` of all right values.

Type Parameters:
`L` - the type of left values
`R` - the type of right values
`T` - the type of the input values
Parameters:
`values` - an `Iterable` of values to map
`mapper` - a function mapping each value to an `Either<L, R>`
Returns:
a single `Either` containing a `Seq` of left or right results
Throws:
`NullPointerException` - if `values` or `mapper` is null

  - 

### sequenceRight

static <L,
R> Either<L,Seq<R>> sequenceRight(@NonNull Iterable<? extends Either<? extends L,? extends R>> eithers)
Transforms an `Iterable` of `Either<L, R>` into a single `Either<L, Seq<R>>`.
 

 If any of the given `Either`s is a `Either.Left`, the result is a `Either.Left`
 containing the first left value encountered in iteration order.
 

 If all of the given `Either`s are `Either.Right`, the result is a `Either.Right`
 containing a (possibly empty) `Seq` of all right values.

 

```

 // = Right(Seq())
 Either.sequenceRight(List.empty())

 // = Right(Seq(1, 2))
 Either.sequenceRight(List.of(Either.right(1), Either.right(2)))

 // = Left("x1")
 Either.sequenceRight(List.of(Either.right(1), Either.left("x1"), Either.left("x2")))
 
```

Type Parameters:
`L` - the type of left values
`R` - the type of right values
Parameters:
`eithers` - an `Iterable` of `Either` instances
Returns:
an `Either` containing either the first left value if present, or a `Seq` of all right values
Throws:
`NullPointerException` - if `eithers` is null

  - 

### traverseRight

static <L,
R,
T> Either<L,Seq<R>> traverseRight(@NonNull Iterable<? extends T> values,
 @NonNull Function<? super T,? extends Either<? extends L,? extends R>> mapper)
Transforms an `Iterable` of values into a single `Either<Seq<L>, Seq<R>>` by applying a mapping 
 function that returns an `Either` for each element.
 

 If the mapper returns any `Either.Left`, the resulting `Either` is a `Either.Left`
 containing a `Seq` of all left values. Otherwise, the result is a `Either.Right` containing 
 a `Seq` of all right values.

Type Parameters:
`L` - the type of left values
`R` - the type of right values
`T` - the type of input values
Parameters:
`values` - an `Iterable` of values to map
`mapper` - a function mapping each value to an `Either<L, R>`
Returns:
a single `Either` containing a `Seq` of left or right results
Throws:
`NullPointerException` - if `values` or `mapper` is null

  - 

### getOrElseGet

default R getOrElseGet(@NonNull Function<? super L,? extends R> other)
Returns the right value of this `Either`, or an alternative value if this is a `Either.Left`.

Parameters:
`other` - a function that converts a left value to an alternative right value
Returns:
the right value if present, otherwise the alternative value produced by applying `other` to the left value

  - 

### orElseRun

default void orElseRun(@NonNull Consumer<? super L> action)
Executes the given action if this projection represents a `Either.Left` value.

Parameters:
`action` - a consumer that processes the left value

  - 

### getOrElseThrow

default <X extends Throwable> R getOrElseThrow(@NonNull Function<? super L,X> exceptionFunction)
                                        throws X
Returns the right value of this `Either`, or throws an exception if it is a `Either.Left`.

Type Parameters:
`X` - the type of exception to be thrown
Parameters:
`exceptionFunction` - a function that produces an exception from the left value
Returns:
the right value if present
Throws:
`X` - if this `Either` is a `Either.Left`, using the exception produced by `exceptionFunction`

  - 

### swap

default Either<R,L> swap()
Swaps the sides of this `Either`, converting a `Either.Left` to a `Either.Right`
 and vice versa.

Returns:
a new `Either` with the left and right values swapped

  - 

### flatMap

default <U> Either<L,U> flatMap(@NonNull Function<? super R,? extends Either<L,? extends U>> mapper)
Applies a flat-mapping function to the right value of this right-biased `Either`.
 

 If this `Either` is a `Either.Left`, it is returned unchanged. 
 Otherwise, the `mapper` function is applied to the right value, and its result is returned.

Type Parameters:
`U` - the type of the right value in the resulting `Either`
Parameters:
`mapper` - a function that maps the right value to another `Either<L, U>`
Returns:
this `Either` unchanged if it is a `Either.Left`, or the result of applying `mapper` if it is a `Either.Right`
Throws:
`NullPointerException` - if `mapper` is null

  - 

### map

default <U> Either<L,U> map(@NonNull Function<? super R,? extends U> mapper)
Transforms the right value of this `Either` using the given mapping function.
 

 If this `Either` is a `Either.Left`, no operation is performed and it is returned unchanged.

 

```

 import static io.vavr.API.*;

 // = Right("A")
 Right("a").map(String::toUpperCase);

 // = Left(1)
 Left(1).map(String::toUpperCase);
 
```

Specified by:
`map` in interface `Value<L>`
Type Parameters:
`U` - the type of the right value in the resulting `Either`
Parameters:
`mapper` - a function to transform the right value
Returns:
a new `Either` with the right value transformed, or the original left value
Throws:
`NullPointerException` - if `mapper` is null

  - 

### mapLeft

default <U> Either<U,R> mapLeft(@NonNull Function<? super L,? extends U> leftMapper)
Transforms the left value of this `Either` using the given mapping function.
 

 If this `Either` is a `Either.Right`, no operation is performed and it is returned unchanged.

 

```

 import static io.vavr.API.*;

 // = Left(2)
 Left(1).mapLeft(i -> i + 1);

 // = Right("a")
 Right("a").mapLeft(i -> i + 1);
 
```

Type Parameters:
`U` - the type of the left value in the resulting `Either`
Parameters:
`leftMapper` - a function to transform the left value
Returns:
a new `Either` with the left value transformed, or the original right value
Throws:
`NullPointerException` - if `leftMapper` is null

  - 

### filter

default Option<Either<L,R>> filter(@NonNull Predicate<? super R> predicate)
Returns an `Option` describing the right value of this right-biased `Either`
 if it satisfies the given predicate.
 

 If this `Either` is a `Either.Left` or the predicate does not match, `Option.none()` is returned.

Parameters:
`predicate` - a predicate to test the right value
Returns:
an `Option` containing the right value if it satisfies the predicate, or `Option.none()` otherwise
Throws:
`NullPointerException` - if `predicate` is null

  - 

### filterOrElse

default Either<L,R> filterOrElse(@NonNull Predicate<? super R> predicate,
 @NonNull Function<? super R,? extends L> zero)
Filters this right-biased `Either` using the given predicate. 
 

 If this `Either` is a `Either.Right` and the predicate evaluates to `false`, 
 the result is a `Either.Left` obtained by applying the `zero` function to the right value.
 If the predicate evaluates to `true`, the `Either.Right` is returned unchanged.

 

```

 import static io.vavr.API.*;

 // = Left("bad: a")
 Right("a").filterOrElse(i -> false, val -> "bad: " + val);

 // = Right("a")
 Right("a").filterOrElse(i -> true, val -> "bad: " + val);
 
```

Parameters:
`predicate` - a predicate to test the right value
`zero` - a function that converts a right value to a left value if the predicate fails
Returns:
an `Either` containing the right value if the predicate matches, or a left value otherwise
Throws:
`NullPointerException` - if `predicate` or `zero` is null

  - 

### get

R get()
Returns the right value if this is a `Right`; otherwise throws.

Specified by:
`get` in interface `Value<L>`
Returns:
the right value
Throws:
`NoSuchElementException` - if this is a `Left`

  - 

### isEmpty

default boolean isEmpty()
Description copied from interface: `Value`
Checks, this `Value` is empty, i.e. if the underlying value is absent.

Specified by:
`isEmpty` in interface `Value<L>`
Returns:
false, if no underlying value is present, true otherwise.

  - 

### orElse

default Either<L,R> orElse(@NonNull Either<? extends L,? extends R> other)
Returns this `Either` if it is a `Either.Right`, otherwise returns the given `other` Either.

Parameters:
`other` - an alternative `Either`
Returns:
this `Either` if it is a `Right`, otherwise `other`

  - 

### orElse

default Either<L,R> orElse(@NonNull Supplier<? extends Either<? extends L,? extends R>> supplier)
Returns this `Either` if it is a `Either.Right`, otherwise returns the result of evaluating the given `supplier`.

Parameters:
`supplier` - a supplier of an alternative `Either`
Returns:
this `Either` if it is a `Right`, otherwise the result of `supplier`

  - 

### mapTo

default <U> Either<L,U> mapTo(U value)
Description copied from interface: `Value`
Maps the underlying value to another fixed value.

Specified by:
`mapTo` in interface `Value<L>`
Type Parameters:
`U` - The new component type
Parameters:
`value` - value to replace the contents with
Returns:
A new value

  - 

### mapToVoid

default Either<L,Void> mapToVoid()
Description copied from interface: `Value`
Maps the underlying value to Void

Specified by:
`mapToVoid` in interface `Value<L>`
Returns:
A new value of type Void

  - 

### isAsync

default boolean isAsync()
Indicates that a right-biased `Either` computes its value synchronously.

Specified by:
`isAsync` in interface `Value<L>`
Returns:
`false`

  - 

### isLazy

default boolean isLazy()
Indicates that a right-biased `Either` computes its value eagerly.

Specified by:
`isLazy` in interface `Value<L>`
Returns:
`false`

  - 

### isSingleValued

default boolean isSingleValued()
Indicates that a right-biased `Either` contains exactly one value.

Specified by:
`isSingleValued` in interface `Value<L>`
Returns:
`true`

  - 

### iterator

default @NonNull Iterator<R> iterator()
Description copied from interface: `Value`
Returns a rich `io.vavr.collection.Iterator`.

Specified by:
`iterator` in interface `Iterable<L>`
Specified by:
`iterator` in interface `Value<L>`
Returns:
A new Iterator

  - 

### peek

default Either<L,R> peek(@NonNull Consumer<? super R> action)
Description copied from interface: `Value`
Performs the given `action` on the first element if this is an *eager* implementation.
 Performs the given `action` on all elements (the first immediately, successive deferred),
 if this is a *lazy* implementation.

Specified by:
`peek` in interface `Value<L>`
Parameters:
`action` - The action that will be performed on the element(s).
Returns:
this instance

  - 

### peekLeft

default Either<L,R> peekLeft(@NonNull Consumer<? super L> action)
Performs the given action on the left value if this is a `Either.Left`.
 

 If this is a `Either.Right`, no action is performed.

Parameters:
`action` - a consumer that processes the left value
Returns:
this `Either`

  - 

### toValidation

default Validation<L,R> toValidation()
Returns this as `Validation`.

Returns:
`Validation.valid(get())` if this is right, otherwise `Validation.invalid(getLeft())`.

  - 

### toTry

default Try<R> toTry()
Description copied from interface: `Value`
Converts this to a `Try`.
 

 If this value is undefined, i.e. empty, then a new `Failure(NoSuchElementException)` is returned,
 otherwise a new `Success(value)` is returned.

Specified by:
`toTry` in interface `Value<L>`
Returns:
A new `Try`.

  - 

### equals

boolean equals(Object o)
Description copied from interface: `Value`
Clarifies that values have a proper equals() method implemented.
 

 See Object.equals(Object).

Specified by:
`equals` in interface `Value<L>`
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
`hashCode` in interface `Value<L>`
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
`toString` in interface `Value<L>`
Overrides:
`toString` in class `Object`
Returns:
A String representation of this object