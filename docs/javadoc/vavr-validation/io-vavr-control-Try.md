Package io.vavr.control

# Interface Try<T>

Type Parameters:
`T` - the type of the value in case of success

All Superinterfaces:
`Iterable<T>`, `Serializable`, `Value<T>`

All Known Implementing Classes:
`Try.Failure`, `Try.Success`

---

public interface Try<T>
extends Value<T>, Serializable
A control structure that allows writing safe code without explicitly managing try-catch blocks for exceptions.
 

 The following exceptions are considered fatal or non-recoverable:
 

     
- InterruptedException
     
- LinkageError
     
- ThreadDeath
     
- VirtualMachineError, including OutOfMemoryError and StackOverflowError
 

 

 **Note:** Methods such as `get()` may re-throw exceptions without declaring them. When used
 within a `InvocationHandler` of a dynamic proxy, such exceptions will be wrapped in
 `UndeclaredThrowableException`. See 
 
 Dynamic Proxy Classes for more details.

Author:
Daniel

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Interface
Description
`static final class `
`Try.Failure<T>`

Represents a failed `Try` containing a `Throwable` as the cause.

`static final class `
`Try.Success<T>`

Represents a successful `Try` containing a value.

`static final class `
`Try.WithResources1<T1 extends AutoCloseable>`

A `Try`-with-resources builder that operates on one `AutoCloseable` resource.

`static final class `
`Try.WithResources2<T1 extends AutoCloseable,T2 extends AutoCloseable>`

A `Try`-with-resources builder that operates on two `AutoCloseable` resources.

`static final class `
`Try.WithResources3<T1 extends AutoCloseable,T2 extends AutoCloseable,T3 extends AutoCloseable>`

A `Try`-with-resources builder that operates on three `AutoCloseable` resources.

`static final class `
`Try.WithResources4<T1 extends AutoCloseable,T2 extends AutoCloseable,T3 extends AutoCloseable,T4 extends AutoCloseable>`

A `Try`-with-resources builder that operates on four `AutoCloseable` resources.

`static final class `
`Try.WithResources5<T1 extends AutoCloseable,T2 extends AutoCloseable,T3 extends AutoCloseable,T4 extends AutoCloseable,T5 extends AutoCloseable>`

A `Try`-with-resources builder that operates on five `AutoCloseable` resources.

`static final class `
`Try.WithResources6<T1 extends AutoCloseable,T2 extends AutoCloseable,T3 extends AutoCloseable,T4 extends AutoCloseable,T5 extends AutoCloseable,T6 extends AutoCloseable>`

A `Try`-with-resources builder that operates on six `AutoCloseable` resources.

`static final class `
`Try.WithResources7<T1 extends AutoCloseable,T2 extends AutoCloseable,T3 extends AutoCloseable,T4 extends AutoCloseable,T5 extends AutoCloseable,T6 extends AutoCloseable,T7 extends AutoCloseable>`

A `Try`-with-resources builder that operates on seven `AutoCloseable` resources.

`static final class `
`Try.WithResources8<T1 extends AutoCloseable,T2 extends AutoCloseable,T3 extends AutoCloseable,T4 extends AutoCloseable,T5 extends AutoCloseable,T6 extends AutoCloseable,T7 extends AutoCloseable,T8 extends AutoCloseable>`

A `Try`-with-resources builder that operates on eight `AutoCloseable` resources.

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
`default Try<T>`
`andFinally(@NonNull Runnable runnable)`

Executes a given `Runnable` after this `Try`, regardless of whether it is a
 `Try.Success` or `Try.Failure`.

`default Try<T>`
`andFinallyTry(@NonNull CheckedRunnable runnable)`

Executes a given `CheckedRunnable` after this `Try`, regardless of whether it is a
 `Try.Success` or `Try.Failure`.

`default Try<T>`
`andThen(@NonNull Runnable runnable)`

Performs the given `Runnable` if this `Try` is a `Try.Success`.

`default Try<T>`
`andThen(@NonNull Consumer<? super T> consumer)`

Performs the given `Consumer` on the value of this `Try` if it is a `Try.Success`.

`default Try<T>`
`andThenTry(@NonNull CheckedConsumer<? super T> consumer)`

Passes the result of this `Try` to the given `CheckedConsumer` if this is a `Try.Success`.

`default Try<T>`
`andThenTry(@NonNull CheckedRunnable runnable)`

Executes the given `CheckedRunnable` if this `Try` is a `Try.Success`; 
 otherwise, returns this `Failure`.

`default <R> Try<R>`
`collect(@NonNull PartialFunction<? super T,? extends R> partialFunction)`

Transforms the value of this `Try` using the given `PartialFunction` if it is defined at the value.

`boolean`
`equals(Object o)`

Clarifies that values have a proper equals() method implemented.

`default Try<Throwable>`
`failed()`

Returns a `Success` containing the throwable if this `Try` is a `Try.Failure`.

`static <T> Try<T>`
`failure(Throwable exception)`

Creates a `Try.Failure` containing the given `exception`.

`default Try<T>`
`filter(@NonNull Predicate<? super T> predicate)`

Returns a `Try` if the given `Predicate` evaluates to `true`, otherwise returns a `Try.Failure`.

`default Try<T>`
`filter(@NonNull Predicate<? super T> predicate,
 Function<? super T,? extends Throwable> errorProvider)`

Returns a `Try` if the given `Predicate` evaluates to `true`, otherwise returns a `Try.Failure`
 created by applying the given function to the value.

`default Try<T>`
`filter(@NonNull Predicate<? super T> predicate,
 Supplier<? extends Throwable> throwableSupplier)`

Returns a `Try` if the given `Predicate` evaluates to `true`, otherwise returns a `Try.Failure`
 created by the given `Supplier` of `Throwable`.

`default Try<T>`
`filterTry(@NonNull CheckedPredicate<? super T> predicate)`

Returns `this` if this `Try` is a `Try.Failure` or if it is a `Try.Success` and the value
 satisfies the given checked predicate.

`default Try<T>`
`filterTry(@NonNull CheckedPredicate<? super T> predicate,
 CheckedFunction1<? super T,? extends Throwable> errorProvider)`

Returns `this` if this `Try` is a `Try.Failure` or if it is a `Try.Success` and the value
 satisfies the given checked predicate.

`default Try<T>`
`filterTry(@NonNull CheckedPredicate<? super T> predicate,
 Supplier<? extends Throwable> throwableSupplier)`

Returns `this` if this `Try` is a `Try.Failure` or if it is a `Try.Success` and the value
 satisfies the given checked predicate.

`default <U> Try<U>`
`flatMap(@NonNull Function<? super T,? extends Try<? extends U>> mapper)`

Transforms the value of this `Try` using the given `Function` if it is a `Try.Success`,
 or returns this `Try.Failure`.

`default <U> Try<U>`
`flatMapTry(@NonNull CheckedFunction1<? super T,? extends Try<? extends U>> mapper)`

Transforms the value of this `Try` using the given `CheckedFunction1` if it is a `Try.Success`,
 or returns this `Try.Failure`.

`default <X> X`
`fold(@NonNull Function<? super Throwable,? extends X> ifFail,
 @NonNull Function<? super T,? extends X> f)`

Folds this `Try` into a single value by applying one of two functions:
 one for the failure case and one for the success case.

`T`
`get()`

Returns the value of this `Try` if it is a `Try.Success`, or throws the underlying exception if it is a `Try.Failure`.

`Throwable`
`getCause()`

Returns the cause of failure if this `Try` is a `Try.Failure`.

`default T`
`getOrElseGet(@NonNull Function<? super Throwable,? extends T> other)`

Returns the value of this `Success`, or applies the given function to the cause if this is a `Try.Failure`.

`default <X extends Throwable>
T`
`getOrElseThrow(@NonNull Function<? super Throwable,X> exceptionProvider)`

Returns the value of this `Try.Success`, or throws a provided exception if this is a `Try.Failure`.

`int`
`hashCode()`

Clarifies that values have a proper hashCode() method implemented.

`default boolean`
`isAsync()`

Indicates whether this `Try` is computed asynchronously.

`boolean`
`isEmpty()`

Checks whether this `Try` contains no value, i.e., it is a `Try.Failure`.

`boolean`
`isFailure()`

Checks whether this `Try` is a `Try.Failure`.

`default boolean`
`isLazy()`

Indicates whether this `Try` is evaluated lazily.

`default boolean`
`isSingleValued()`

Indicates whether this `Try` represents a single value.

`boolean`
`isSuccess()`

Checks whether this `Try` is a `Try.Success`.

`default @NonNull Iterator<T>`
`iterator()`

Returns a rich `io.vavr.collection.Iterator`.

`default <U> Try<U>`
`map(@NonNull Function<? super T,? extends U> mapper)`

Shortcut for `mapTry(mapper::apply)`, see `mapTry(CheckedFunction1)`.

`default Try<T>`
`mapFailure(@NonNull API.Match.Case<? extends Throwable,? extends Throwable> @NonNull ... cases)`

Transforms the cause of this `Try.Failure` using the given sequence of match cases.

`default <U> Try<U>`
`mapTo(U value)`

Maps the underlying value to another fixed value.

`default Try<Void>`
`mapToVoid()`

Maps the underlying value to Void

`default <U> Try<U>`
`mapTry(@NonNull CheckedFunction1<? super T,? extends U> mapper)`

Applies the given checked function to the value of this `Try.Success`, or returns this `Try.Failure` unchanged.

`static <T> Try<T>`
`narrow(Try<? extends T> t)`

Narrows a `Try<? extends T>` to `Try<T>` using a type-safe cast.

`static <T> Try<T>`
`of(@NonNull CheckedFunction0<? extends T> supplier)`

Creates a `Try` instance from a `CheckedFunction0`.

`static <T> Try<T>`
`ofCallable(@NonNull Callable<? extends T> callable)`

Creates a `Try` instance from a `Callable`.

`static <T> Try<T>`
`ofSupplier(@NonNull Supplier<? extends T> supplier)`

Creates a `Try` instance from a `Supplier`.

`default <X extends Throwable>
Try<T>`
`onFailure(@NonNull Class<X> exceptionType,
 @NonNull Consumer<? super X> action)`

Performs the given action if this `Try` is a `Try.Failure` and the cause is an instance of the specified type.

`default Try<T>`
`onFailure(@NonNull Consumer<? super Throwable> action)`

Performs the given action if this `Try` is a `Try.Failure`.

`default Try<T>`
`onSuccess(@NonNull Consumer<? super T> action)`

Performs the given action if this `Try` is a `Try.Success`.

`default Try<T>`
`orElse(@NonNull Try<? extends T> other)`

Returns this `Try` if it is a `Try.Success`, or the given alternative `Try` if this is a `Try.Failure`.

`default Try<T>`
`orElse(@NonNull Supplier<? extends Try<? extends T>> supplier)`

Returns this `Try` if it is a `Try.Success`, or a `Try` supplied by the given `Supplier` if this is a `Try.Failure`.

`default void`
`orElseRun(@NonNull Consumer<? super Throwable> action)`

Executes the given action if this `Try` is a `Try.Failure`.

`default Try<T>`
`peek(@NonNull Consumer<? super T> action)`

Performs the given action if this `Try` is a `Try.Success`, otherwise does nothing.

`default <X extends Throwable>
Try<T>`
`recover(@NonNull Class<X> exceptionType,
 @NonNull Function<? super X,? extends T> f)`

Attempts to recover from a failure if the cause is an instance of the specified exception type.

`default <X extends Throwable>
Try<T>`
`recover(@NonNull Class<X> exceptionType,
 T value)`

Recovers this `Try` with the given `value` if this is a `Try.Failure`
 and the underlying cause matches the specified `exceptionType`.

`default Try<T>`
`recover(@NonNull Function<? super Throwable,? extends T> f)`

Recovers this `Try` if it is a `Try.Failure` by applying the given recovery function `f`
 to the underlying exception.

`default Try<T>`
`recoverAllAndTry(@NonNull CheckedFunction0<? extends T> recoveryAttempt)`

Recovers from any failure by evaluating the given `recoveryAttempt` if this `Try` is a `Try.Failure`.

`default <X extends Throwable>
Try<T>`
`recoverAndTry(@NonNull Class<X> exceptionType,
 @NonNull CheckedFunction0<? extends T> recoveryAttempt)`

Returns `this` if it is a `Try.Success`, or attempts to recover from a failure when the
 underlying cause is assignable to the specified `exceptionType` by evaluating the given
 `recoveryAttempt` (via `of(CheckedFunction0)`).

`default <X extends Throwable>
Try<T>`
`recoverWith(@NonNull Class<X> exceptionType,
 @NonNull Try<? extends T> recovered)`

Recovers this `Try` with the given `recovered` value if this is a `Try.Failure`
 and the underlying cause is assignable to the specified `exceptionType`.

`default <X extends Throwable>
Try<T>`
`recoverWith(@NonNull Class<X> exceptionType,
 @NonNull Function<? super X,Try<? extends T>> f)`

Attempts to recover from a failure by applying the given recovery function if the cause matches the specified exception type.

`default Try<T>`
`recoverWith(@NonNull Function<? super Throwable,? extends Try<? extends T>> f)`

Recovers this `Try` if it is a `Try.Failure` by applying the given recovery function `f`
 to the underlying exception.

`static Try<Void>`
`run(@NonNull CheckedRunnable runnable)`

Creates a `Try` instance from a `CheckedRunnable`.

`static Try<Void>`
`runRunnable(@NonNull Runnable runnable)`

Creates a `Try` instance from a `Runnable`.

`static <T> Try<Seq<T>>`
`sequence(@NonNull Iterable<? extends Try<? extends T>> values)`

Transforms an `Iterable` of `Try` instances into a single `Try` containing a `Seq`
 of all successful results.

`static <T> Try<T>`
`success(T value)`

Creates a `Try.Success` containing the given `value`.

`default Either<Throwable,T>`
`toEither()`

Converts this `Try` to an `Either`.

`default <L> Either<L,T>`
`toEither(@NonNull Function<? super Throwable,? extends L> throwableMapper)`

Converts this `Try` to an `Either`, mapping the failure cause to a left value using
 the provided `Function`.

`String`
`toString()`

Clarifies that values have a proper toString() method implemented.

`default Validation<Throwable,T>`
`toValidation()`

Converts this `Try` to a `Validation`.

`default <U> Validation<U,T>`
`toValidation(@NonNull Function<? super Throwable,? extends U> throwableMapper)`

Converts this `Try` to a `Validation`, mapping the failure cause to an invalid value
 using the provided `Function`.

`default <U> U`
`transform(@NonNull Function<? super Try<T>,? extends U> f)`

Transforms this `Try` into a value of another type using the provided function.

`static <T,
U> Try<Seq<U>>`
`traverse(@NonNull Iterable<? extends T> values,
 @NonNull Function<? super T,? extends Try<? extends U>> mapper)`

Transforms an `Iterable` of values into a single `Try` containing a `Seq` of mapped results.

`static <T1 extends AutoCloseable>
Try.WithResources1<T1>`
`withResources(@NonNull CheckedFunction0<? extends T1> t1Supplier)`

Creates a `Try`-with-resources builder that operates on one `AutoCloseable` resource.

`static <T1 extends AutoCloseable,
T2 extends AutoCloseable>
Try.WithResources2<T1,T2>`
`withResources(@NonNull CheckedFunction0<? extends T1> t1Supplier,
 @NonNull CheckedFunction0<? extends T2> t2Supplier)`

Creates a `Try`-with-resources builder that operates on two `AutoCloseable` resources.

`static <T1 extends AutoCloseable,
T2 extends AutoCloseable,
T3 extends AutoCloseable>
Try.WithResources3<T1,T2,T3>`
`withResources(@NonNull CheckedFunction0<? extends T1> t1Supplier,
 @NonNull CheckedFunction0<? extends T2> t2Supplier,
 @NonNull CheckedFunction0<? extends T3> t3Supplier)`

Creates a `Try`-with-resources builder that operates on three `AutoCloseable` resources.

`static <T1 extends AutoCloseable,
T2 extends AutoCloseable,
T3 extends AutoCloseable,
T4 extends AutoCloseable>
Try.WithResources4<T1,T2,T3,T4>`
`withResources(@NonNull CheckedFunction0<? extends T1> t1Supplier,
 @NonNull CheckedFunction0<? extends T2> t2Supplier,
 @NonNull CheckedFunction0<? extends T3> t3Supplier,
 @NonNull CheckedFunction0<? extends T4> t4Supplier)`

Creates a `Try`-with-resources builder that operates on four `AutoCloseable` resources.

`static <T1 extends AutoCloseable,
T2 extends AutoCloseable,
T3 extends AutoCloseable,
T4 extends AutoCloseable,
T5 extends AutoCloseable>
Try.WithResources5<T1,T2,T3,T4,T5>`
`withResources(@NonNull CheckedFunction0<? extends T1> t1Supplier,
 @NonNull CheckedFunction0<? extends T2> t2Supplier,
 @NonNull CheckedFunction0<? extends T3> t3Supplier,
 @NonNull CheckedFunction0<? extends T4> t4Supplier,
 @NonNull CheckedFunction0<? extends T5> t5Supplier)`

Creates a `Try`-with-resources builder that operates on five `AutoCloseable` resources.

`static <T1 extends AutoCloseable,
T2 extends AutoCloseable,
T3 extends AutoCloseable,
T4 extends AutoCloseable,
T5 extends AutoCloseable,
T6 extends AutoCloseable>
Try.WithResources6<T1,T2,T3,T4,T5,T6>`
`withResources(@NonNull CheckedFunction0<? extends T1> t1Supplier,
 @NonNull CheckedFunction0<? extends T2> t2Supplier,
 @NonNull CheckedFunction0<? extends T3> t3Supplier,
 @NonNull CheckedFunction0<? extends T4> t4Supplier,
 @NonNull CheckedFunction0<? extends T5> t5Supplier,
 @NonNull CheckedFunction0<? extends T6> t6Supplier)`

Creates a `Try`-with-resources builder that operates on six `AutoCloseable` resources.

`static <T1 extends AutoCloseable,
T2 extends AutoCloseable,
T3 extends AutoCloseable,
T4 extends AutoCloseable,
T5 extends AutoCloseable,
T6 extends AutoCloseable,
T7 extends AutoCloseable>
Try.WithResources7<T1,T2,T3,T4,T5,T6,T7>`
`withResources(@NonNull CheckedFunction0<? extends T1> t1Supplier,
 @NonNull CheckedFunction0<? extends T2> t2Supplier,
 @NonNull CheckedFunction0<? extends T3> t3Supplier,
 @NonNull CheckedFunction0<? extends T4> t4Supplier,
 @NonNull CheckedFunction0<? extends T5> t5Supplier,
 @NonNull CheckedFunction0<? extends T6> t6Supplier,
 @NonNull CheckedFunction0<? extends T7> t7Supplier)`

Creates a `Try`-with-resources builder that operates on seven `AutoCloseable` resources.

`static <T1 extends AutoCloseable,
T2 extends AutoCloseable,
T3 extends AutoCloseable,
T4 extends AutoCloseable,
T5 extends AutoCloseable,
T6 extends AutoCloseable,
T7 extends AutoCloseable,
T8 extends AutoCloseable>
Try.WithResources8<T1,T2,T3,T4,T5,T6,T7,T8>`
`withResources(@NonNull CheckedFunction0<? extends T1> t1Supplier,
 @NonNull CheckedFunction0<? extends T2> t2Supplier,
 @NonNull CheckedFunction0<? extends T3> t3Supplier,
 @NonNull CheckedFunction0<? extends T4> t4Supplier,
 @NonNull CheckedFunction0<? extends T5> t5Supplier,
 @NonNull CheckedFunction0<? extends T6> t6Supplier,
 @NonNull CheckedFunction0<? extends T7> t7Supplier,
 @NonNull CheckedFunction0<? extends T8> t8Supplier)`

Creates a `Try`-with-resources builder that operates on eight `AutoCloseable` resources.

### Methods inherited from interface io.vavr.Value

`collect, collect, contains, corresponds, eq, exists, forAll, forEach, getOrElse, getOrElse, getOrElseThrow, getOrElseTry, getOrNull, out, out, spliterator, stderr, stdout, stringPrefix, toArray, toCharSeq, toCompletableFuture, toEither, toEither, toInvalid, toInvalid, toJavaArray, toJavaArray, toJavaArray, toJavaCollection, toJavaList, toJavaList, toJavaMap, toJavaMap, toJavaMap, toJavaOptional, toJavaParallelStream, toJavaSet, toJavaSet, toJavaStream, toLeft, toLeft, toLinkedMap, toLinkedMap, toLinkedSet, toList, toMap, toMap, toOption, toPriorityQueue, toPriorityQueue, toQueue, toRight, toRight, toSet, toSortedMap, toSortedMap, toSortedMap, toSortedMap, toSortedSet, toSortedSet, toStream, toTree, toTree, toTry, toTry, toValid, toValid, toValidation, toValidation, toVector`

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

static <T> Try<T> of(@NonNull CheckedFunction0<? extends T> supplier)
Creates a `Try` instance from a `CheckedFunction0`.
 

 If the supplier executes without throwing an exception, a `Try.Success` containing the result is returned.
 If an exception occurs during execution, a `Try.Failure` wrapping the thrown exception is returned.

Type Parameters:
`T` - the type of the value returned by the supplier
Parameters:
`supplier` - the checked supplier to execute
Returns:
a `Try.Success` with the supplier's result, or a `Try.Failure` if an exception is thrown
Throws:
`NullPointerException` - if `supplier` is `null`

  - 

### ofSupplier

static <T> Try<T> ofSupplier(@NonNull Supplier<? extends T> supplier)
Creates a `Try` instance from a `Supplier`.
 

 If the supplier executes without throwing an exception, a `Try.Success` containing the result is returned.
 If an exception occurs during execution, a `Try.Failure` wrapping the thrown exception is returned.

Type Parameters:
`T` - the type of the value returned by the supplier
Parameters:
`supplier` - the supplier to execute
Returns:
a `Try.Success` with the supplier's result, or a `Try.Failure` if an exception is thrown
Throws:
`NullPointerException` - if `supplier` is `null`

  - 

### ofCallable

static <T> Try<T> ofCallable(@NonNull Callable<? extends T> callable)
Creates a `Try` instance from a `Callable`.
 

 If the callable executes without throwing an exception, a `Try.Success` containing the result is returned.
 If an exception occurs during execution, a `Try.Failure` wrapping the thrown exception is returned.

Type Parameters:
`T` - the type of the value returned by the callable
Parameters:
`callable` - the callable to execute
Returns:
a `Try.Success` with the callable's result, or a `Try.Failure` if an exception is thrown
Throws:
`NullPointerException` - if `callable` is `null`

  - 

### run

static Try<Void> run(@NonNull CheckedRunnable runnable)
Creates a `Try` instance from a `CheckedRunnable`.
 

 If the runnable executes without throwing an exception, a `Try.Success` containing `null` (representing
 the absence of a value) is returned. If an exception occurs during execution, a `Try.Failure` wrapping the
 thrown exception is returned.

Parameters:
`runnable` - the checked runnable to execute
Returns:
a `Try.Success` with `null` if the runnable completes successfully, or a `Try.Failure` if an exception is thrown
Throws:
`NullPointerException` - if `runnable` is `null`

  - 

### runRunnable

static Try<Void> runRunnable(@NonNull Runnable runnable)
Creates a `Try` instance from a `Runnable`.
 

 If the runnable executes without throwing an exception, a `Try.Success` containing `null` (representing
 the absence of a value) is returned. If an exception occurs during execution, a `Try.Failure` wrapping the
 thrown exception is returned.

Parameters:
`runnable` - the runnable to execute
Returns:
a `Try.Success` with `null` if the runnable completes successfully, or a `Try.Failure` if an exception is thrown
Throws:
`NullPointerException` - if `runnable` is `null`

  - 

### sequence

static <T> Try<Seq<T>> sequence(@NonNull Iterable<? extends Try<? extends T>> values)
Transforms an `Iterable` of `Try` instances into a single `Try` containing a `Seq`
 of all successful results. 
 

 If any element in the input iterable is a `Try.Failure`, the resulting `Try` will also be a
 `Try.Failure`, containing the first encountered failure's cause.

Type Parameters:
`T` - the type of values contained in the `Try`s
Parameters:
`values` - an `Iterable` of `Try` instances
Returns:
a `Try` containing a `Seq` of all successful results, or a `Try.Failure` if any input is a failure
Throws:
`NullPointerException` - if `values` is `null`

  - 

### traverse

static <T,
U> Try<Seq<U>> traverse(@NonNull Iterable<? extends T> values,
 @NonNull Function<? super T,? extends Try<? extends U>> mapper)
Transforms an `Iterable` of values into a single `Try` containing a `Seq` of mapped results.
 

 Each value in the input iterable is mapped using the provided `mapper` function, which produces a
 `Try`. If all mappings succeed, a `Try.Success` containing a `Seq` of results is returned.
 If any mapping results in a `Try.Failure`, the first encountered failure is returned.

Type Parameters:
`T` - the type of the input values
`U` - the type of the mapped results
Parameters:
`values` - an `Iterable` of input values
`mapper` - a function mapping each input value to a `Try` of the mapped result
Returns:
a `Try` containing a `Seq` of all mapped results, or a `Try.Failure` if any mapping fails
Throws:
`NullPointerException` - if `values` or `mapper` is `null`

  - 

### success

static <T> Try<T> success(T value)
Creates a `Try.Success` containing the given `value`.
 

 This is a convenience method equivalent to `new Success<>(value)`.

Type Parameters:
`T` - the type of the value
Parameters:
`value` - the value to wrap in a `Try.Success`
Returns:
a new `Try.Success` containing `value`

  - 

### failure

static <T> Try<T> failure(Throwable exception)
Creates a `Try.Failure` containing the given `exception`.
 

 This is a convenience method equivalent to `new Failure<>(exception)`.

Type Parameters:
`T` - the component type of the `Try`
Parameters:
`exception` - the exception to wrap in a `Try.Failure`
Returns:
a new `Try.Failure` containing `exception`

  - 

### narrow

static <T> Try<T> narrow(Try<? extends T> t)
Narrows a `Try<? extends T>` to `Try<T>` using a type-safe cast.
 

 This is safe because `Try` is immutable and its contents are read-only, allowing covariance.

Type Parameters:
`T` - the component type of the `Try`
Parameters:
`t` - the `Try` instance to narrow
Returns:
the given `Try` instance as `Try<T>`

  - 

### andThen

default Try<T> andThen(@NonNull Consumer<? super T> consumer)
Performs the given `Consumer` on the value of this `Try` if it is a `Try.Success`.
 

 This is a shortcut for `andThenTry(consumer::accept)`. If this `Try` is a `Try.Failure`, 
 it is returned unchanged. If the consumer throws an exception, a `Try.Failure` is returned.

Parameters:
`consumer` - the consumer to execute on the value
Returns:
this `Try` if it is a `Try.Failure` or the consumer succeeds, otherwise a `Try.Failure` of the consumer
Throws:
`NullPointerException` - if `consumer` is `null`
See Also:

    - `andThenTry(CheckedConsumer)`

  - 

### andThenTry

default Try<T> andThenTry(@NonNull CheckedConsumer<? super T> consumer)
Passes the result of this `Try` to the given `CheckedConsumer` if this is a `Try.Success`.
 

 This allows chaining of operations that may throw checked exceptions. If this `Try` is a `Try.Failure`, 
 it is returned unchanged. If the consumer throws an exception, a `Try.Failure` containing that exception is returned.
 

 Example usage:
 

```

 Try.of(() -> 100)
    .andThenTry(i -> System.out.println(i));
 
```

Parameters:
`consumer` - the checked consumer to execute on the value
Returns:
this `Try` if it is a `Try.Failure` or the consumer succeeds, otherwise a `Try.Failure` of the consumer
Throws:
`NullPointerException` - if `consumer` is `null`

  - 

### andThen

default Try<T> andThen(@NonNull Runnable runnable)
Performs the given `Runnable` if this `Try` is a `Try.Success`.
 

 This is a shortcut for `andThenTry(runnable::run)`. If this `Try` is a `Try.Failure`, it is returned unchanged.
 If the runnable throws an exception, a `Try.Failure` containing that exception is returned.

Parameters:
`runnable` - the runnable to execute
Returns:
this `Try` if it is a `Try.Failure` or the runnable succeeds, otherwise a `Try.Failure` of the runnable
Throws:
`NullPointerException` - if `runnable` is `null`
See Also:

    - `andThenTry(CheckedRunnable)`

  - 

### andThenTry

default Try<T> andThenTry(@NonNull CheckedRunnable runnable)
Executes the given `CheckedRunnable` if this `Try` is a `Try.Success`; 
 otherwise, returns this `Failure`.
 

 This allows chaining of runnables that may throw checked exceptions. If the runnable throws an exception,
 a `Try.Failure` containing that exception is returned.
 

 Example usage with method references:
 

```

 Try.run(A::methodRef)
    .andThen(B::methodRef)
    .andThen(C::methodRef);
 
```

 The following two forms are semantically equivalent:
 

```

 Try.run(this::doStuff)
    .andThen(this::doMoreStuff)
    .andThen(this::doEvenMoreStuff);

 Try.run(() -> {
     doStuff();
     doMoreStuff();
     doEvenMoreStuff();
 });
 
```

Parameters:
`runnable` - the checked runnable to execute
Returns:
this `Try` if it is a `Try.Failure` or the runnable succeeds, otherwise a `Try.Failure` of the runnable
Throws:
`NullPointerException` - if `runnable` is `null`

  - 

### collect

default <R> Try<R> collect(@NonNull PartialFunction<? super T,? extends R> partialFunction)
Transforms the value of this `Try` using the given `PartialFunction` if it is defined at the value.
 

 The `partialFunction` is first tested with `PartialFunction.isDefinedAt(Object)`. If it returns
 `true`, the value is mapped using `PartialFunction.apply(Object)` and wrapped in a new `Try`.
 If the function is not defined at the value or this `Try` is a `Try.Failure`, the result is a `Try.Failure`.
 

 Example:
 

```

 PartialFunction<Integer, String> pf = ...;
 Try.of(() -> 42)
    .collect(pf); // maps the value if pf.isDefinedAt(42) is true
 
```

Type Parameters:
`R` - the type of the mapped result
Parameters:
`partialFunction` - a function that may not be defined for all input values
Returns:
a new `Try` containing the mapped value if defined, or a `Try.Failure`
Throws:
`NullPointerException` - if `partialFunction` is `null`

  - 

### failed

default Try<Throwable> failed()
Returns a `Success` containing the throwable if this `Try` is a `Try.Failure`.
 

 If this `Try` is a `Try.Success`, a `Failure` containing a `NoSuchElementException` is returned.

Returns:
a `Try<Throwable>` representing the throwable of this `Try.Failure`, or a `Try.Failure` if this is a `Try.Success`

  - 

### filter

default Try<T> filter(@NonNull Predicate<? super T> predicate,
 Supplier<? extends Throwable> throwableSupplier)
Returns a `Try` if the given `Predicate` evaluates to `true`, otherwise returns a `Try.Failure`
 created by the given `Supplier` of `Throwable`.
 

 This is a shortcut for `filterTry(CheckedPredicate, Supplier)`.

Parameters:
`predicate` - the predicate to test the value
`throwableSupplier` - a supplier providing a throwable if the predicate fails
Returns:
this `Try` if the predicate passes, otherwise a `Try.Failure` from the throwable supplier
Throws:
`NullPointerException` - if `predicate` or `throwableSupplier` is `null`

  - 

### filter

default Try<T> filter(@NonNull Predicate<? super T> predicate,
 Function<? super T,? extends Throwable> errorProvider)
Returns a `Try` if the given `Predicate` evaluates to `true`, otherwise returns a `Try.Failure`
 created by applying the given function to the value.
 

 This is a shortcut for `filterTry(CheckedPredicate, CheckedFunction1)`.

Parameters:
`predicate` - the predicate to test the value
`errorProvider` - a function providing a throwable if the predicate fails
Returns:
this `Try` if the predicate passes, otherwise a `Try.Failure` from the error provider
Throws:
`NullPointerException` - if `predicate` or `errorProvider` is `null`

  - 

### filter

default Try<T> filter(@NonNull Predicate<? super T> predicate)
Returns a `Try` if the given `Predicate` evaluates to `true`, otherwise returns a `Try.Failure`.
 

 This is a shortcut for `filterTry(CheckedPredicate)`.

Parameters:
`predicate` - the predicate to test the value
Returns:
this `Try` if the predicate passes, otherwise a `Try.Failure`
Throws:
`NullPointerException` - if `predicate` is `null`

  - 

### filterTry

default Try<T> filterTry(@NonNull CheckedPredicate<? super T> predicate,
 Supplier<? extends Throwable> throwableSupplier)
Returns `this` if this `Try` is a `Try.Failure` or if it is a `Try.Success` and the value
 satisfies the given checked predicate.
 

 If this is a `Try.Success` and the predicate returns `false`, or if evaluating the predicate
 throws an exception, a new `Try.Failure` is returned. The returned failure wraps a `Throwable`
 provided by the given `throwableSupplier`.

Parameters:
`predicate` - the checked predicate to test the value
`throwableSupplier` - a supplier providing the `Throwable` for the failure if the predicate does not hold
Returns:
this `Try` if it is a `Try.Failure` or the predicate passes, otherwise a `Try.Failure` from the supplier
Throws:
`NullPointerException` - if `predicate` or `throwableSupplier` is `null`

  - 

### filterTry

default Try<T> filterTry(@NonNull CheckedPredicate<? super T> predicate,
 CheckedFunction1<? super T,? extends Throwable> errorProvider)
Returns `this` if this `Try` is a `Try.Failure` or if it is a `Try.Success` and the value
 satisfies the given checked predicate.
 

 If the predicate does not hold or throws an exception, a new `Try.Failure` is returned. The returned
 failure wraps a `Throwable` provided by the given `errorProvider` function.

Parameters:
`predicate` - the checked predicate to test the value
`errorProvider` - a function that provides a `Throwable` if the predicate fails
Returns:
this `Try` if it is a `Try.Failure` or the predicate passes, otherwise a `Try.Failure` from the error provider
Throws:
`NullPointerException` - if `predicate` or `errorProvider` is `null`

  - 

### filterTry

default Try<T> filterTry(@NonNull CheckedPredicate<? super T> predicate)
Returns `this` if this `Try` is a `Try.Failure` or if it is a `Try.Success` and the value
 satisfies the given checked predicate.
 

 If the predicate does not hold or throws an exception, a new `Try.Failure` wrapping a
 `NoSuchElementException` is returned.

Parameters:
`predicate` - the checked predicate to test the value
Returns:
this `Try` if it is a `Try.Failure` or the predicate passes, otherwise a `Try.Failure` with a `NoSuchElementException`
Throws:
`NullPointerException` - if `predicate` is `null`

  - 

### flatMap

default <U> Try<U> flatMap(@NonNull Function<? super T,? extends Try<? extends U>> mapper)
Transforms the value of this `Try` using the given `Function` if it is a `Try.Success`,
 or returns this `Try.Failure`.
 

 This is a shortcut for `flatMapTry(CheckedFunction1)`.

Type Parameters:
`U` - the type of the resulting `Try`
Parameters:
`mapper` - a function mapping the value to another `Try`
Returns:
a new `Try` resulting from applying the mapper, or this `Failure` if this is a failure
Throws:
`NullPointerException` - if `mapper` is `null`

  - 

### flatMapTry

default <U> Try<U> flatMapTry(@NonNull CheckedFunction1<? super T,? extends Try<? extends U>> mapper)
Transforms the value of this `Try` using the given `CheckedFunction1` if it is a `Try.Success`,
 or returns this `Try.Failure`.
 

 If applying the mapper throws an exception, a `Try.Failure` containing the exception is returned.

Type Parameters:
`U` - the type of the resulting `Try`
Parameters:
`mapper` - a checked function mapping the value to another `Try`
Returns:
a new `Try` resulting from applying the mapper, or this `Failure` if this is a failure
Throws:
`NullPointerException` - if `mapper` is `null`

  - 

### get

T get()
Returns the value of this `Try` if it is a `Try.Success`, or throws the underlying exception if it is a `Try.Failure`.
 

 **Important:** If this `Try` is a `Try.Failure`, the exception thrown is exactly the
 `getCause()` of this `Failure`. The underlying cause is thrown sneakily (without being declared
 in the method signature).

Specified by:
`get` in interface `Value<T>`
Returns:
the value contained in this `Success`

  - 

### getCause

Throwable getCause()
Returns the cause of failure if this `Try` is a `Try.Failure`.

Returns:
the throwable cause of this `Try.Failure`
Throws:
`UnsupportedOperationException` - if this `Try` is a `Try.Success`

  - 

### isAsync

default boolean isAsync()
Indicates whether this `Try` is computed asynchronously.

Specified by:
`isAsync` in interface `Value<T>`
Returns:
`false` for a regular `Try`, since the value is computed synchronously

  - 

### isEmpty

boolean isEmpty()
Checks whether this `Try` contains no value, i.e., it is a `Try.Failure`.

Specified by:
`isEmpty` in interface `Value<T>`
Returns:
`true` if this is a `Try.Failure`, `false` if this is a `Try.Success`

  - 

### isFailure

boolean isFailure()
Checks whether this `Try` is a `Try.Failure`.

Returns:
`true` if this is a `Try.Failure`, `false` if this is a `Try.Success`

  - 

### isLazy

default boolean isLazy()
Indicates whether this `Try` is evaluated lazily.

Specified by:
`isLazy` in interface `Value<T>`
Returns:
`false` for a standard `Try`, as its value is computed eagerly

  - 

### isSingleValued

default boolean isSingleValued()
Indicates whether this `Try` represents a single value.

Specified by:
`isSingleValued` in interface `Value<T>`
Returns:
`true`, since a `Try` always contains at most one value

  - 

### isSuccess

boolean isSuccess()
Checks whether this `Try` is a `Try.Success`.

Returns:
`true` if this is a `Try.Success`, `false` if this is a `Try.Failure`

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

### map

default <U> Try<U> map(@NonNull Function<? super T,? extends U> mapper)
Shortcut for `mapTry(mapper::apply)`, see `mapTry(CheckedFunction1)`.

Specified by:
`map` in interface `Value<T>`
Type Parameters:
`U` - The new component type
Parameters:
`mapper` - A checked function
Returns:
a `Try`
Throws:
`NullPointerException` - if `mapper` is null

  - 

### mapTo

default <U> Try<U> mapTo(U value)
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

default Try<Void> mapToVoid()
Description copied from interface: `Value`
Maps the underlying value to Void

Specified by:
`mapToVoid` in interface `Value<T>`
Returns:
A new value of type Void

  - 

### mapFailure

@GwtIncompatible
default Try<T> mapFailure(@NonNull API.Match.Case<? extends Throwable,? extends Throwable> @NonNull ... cases)
Transforms the cause of this `Try.Failure` using the given sequence of match cases.
 

 If this `Try` is a `Try.Success`, it is returned unchanged. If this is a `Try.Failure`, the
 cause is matched against the provided `cases`. If a match is found, a new `Try.Failure` containing
 the mapped exception is returned. If none of the cases match, the original `Try.Failure` is returned.

Parameters:
`cases` - a possibly non-exhaustive sequence of match cases to handle the cause
Returns:
a new `Try` with a mapped cause if a match is found, otherwise this `Try`

  - 

### mapTry

default <U> Try<U> mapTry(@NonNull CheckedFunction1<? super T,? extends U> mapper)
Applies the given checked function to the value of this `Try.Success`, or returns this `Try.Failure` unchanged.
 

 If the function throws an exception, a new `Try.Failure` containing the exception is returned.
 This allows chaining of computations that may throw checked exceptions.
 

 Example:
 

```

 Try.of(() -> 0)
    .mapTry(x -> 1 / x); // division by zero will result in a Failure
 
```

Type Parameters:
`U` - the type of the result
Parameters:
`mapper` - a checked function to apply to the value
Returns:
a new `Try` containing the mapped value if this is a `Try.Success`, otherwise this `Try.Failure`
Throws:
`NullPointerException` - if `mapper` is `null`

  - 

### onFailure

default Try<T> onFailure(@NonNull Consumer<? super Throwable> action)
Performs the given action if this `Try` is a `Try.Failure`.
 

 Example:
 

```

 // does not print anything
 Try.success(1).onFailure(System.out::println);

 // prints "java.lang.Error"
 Try.failure(new Error()).onFailure(System.out::println);
 
```

Parameters:
`action` - a consumer of the throwable cause
Returns:
this `Try` instance
Throws:
`NullPointerException` - if `action` is null

  - 

### onFailure

@GwtIncompatible
default <X extends Throwable> Try<T> onFailure(@NonNull Class<X> exceptionType,
 @NonNull Consumer<? super X> action)
Performs the given action if this `Try` is a `Try.Failure` and the cause is an instance of the specified type.
 

 Example:
 

```

 // does not print anything
 Try.success(1).onFailure(Error.class, System.out::println);

 // prints "Error"
 Try.failure(new Error())
    .onFailure(RuntimeException.class, x -> System.out.println("Runtime exception"))
    .onFailure(Error.class, x -> System.out.println("Error"));
 
```

Type Parameters:
`X` - the type of exception that should be handled
Parameters:
`exceptionType` - the type of exception to handle
`action` - a consumer for the exception
Returns:
this `Try` instance
Throws:
`NullPointerException` - if `exceptionType` or `action` is null

  - 

### onSuccess

default Try<T> onSuccess(@NonNull Consumer<? super T> action)
Performs the given action if this `Try` is a `Try.Success`.
 

 Example:
 

```

 // prints "1"
 Try.success(1).onSuccess(System.out::println);

 // does not print anything
 Try.failure(new Error()).onSuccess(System.out::println);
 
```

Parameters:
`action` - a consumer of the value
Returns:
this `Try` instance
Throws:
`NullPointerException` - if `action` is null

  - 

### orElse

default Try<T> orElse(@NonNull Try<? extends T> other)
Returns this `Try` if it is a `Try.Success`, or the given alternative `Try` if this is a `Try.Failure`.

Parameters:
`other` - the alternative `Try` to return if this is a `Try.Failure`
Returns:
this `Try` if success, otherwise `other`
Throws:
`NullPointerException` - if `other` is null

  - 

### orElse

default Try<T> orElse(@NonNull Supplier<? extends Try<? extends T>> supplier)
Returns this `Try` if it is a `Try.Success`, or a `Try` supplied by the given `Supplier` if this is a `Try.Failure`.
 

 The supplier is only invoked if this `Try` is a `Try.Failure`.

Parameters:
`supplier` - a supplier of an alternative `Try`
Returns:
this `Try` if success, otherwise the `Try` returned by `supplier`
Throws:
`NullPointerException` - if `supplier` is null

  - 

### getOrElseGet

default T getOrElseGet(@NonNull Function<? super Throwable,? extends T> other)
Returns the value of this `Success`, or applies the given function to the cause if this is a `Try.Failure`.

Parameters:
`other` - a function mapping the throwable cause to a replacement value
Returns:
the value of this `Try.Success`, or the result of applying `other` to the failure cause
Throws:
`NullPointerException` - if `other` is null

  - 

### orElseRun

default void orElseRun(@NonNull Consumer<? super Throwable> action)
Executes the given action if this `Try` is a `Try.Failure`.
 

 This method is typically used for side-effecting handling of failure cases.

Parameters:
`action` - a consumer of the throwable cause
Throws:
`NullPointerException` - if `action` is null

  - 

### getOrElseThrow

default <X extends Throwable> T getOrElseThrow(@NonNull Function<? super Throwable,X> exceptionProvider)
                                        throws X
Returns the value of this `Try.Success`, or throws a provided exception if this is a `Try.Failure`.
 

 The exception to throw is created by applying the given `exceptionProvider` function to the cause of the failure.

Type Parameters:
`X` - the type of the exception to throw
Parameters:
`exceptionProvider` - a function mapping the throwable cause to an exception to be thrown
Returns:
the value of this `Try.Success`
Throws:
`X` - the exception provided by `exceptionProvider` if this is a `Try.Failure`
`NullPointerException` - if `exceptionProvider` is null

  - 

### fold

default <X> X fold(@NonNull Function<? super Throwable,? extends X> ifFail,
 @NonNull Function<? super T,? extends X> f)
Folds this `Try` into a single value by applying one of two functions:
 one for the failure case and one for the success case.
 

 If this is a `Try.Failure`, the `ifFail` function is applied to the cause.
 If this is a `Try.Success`, the `f` function is applied to the value.

Type Parameters:
`X` - the type of the result
Parameters:
`ifFail` - maps the throwable cause if this is a `Try.Failure`
`f` - maps the value if this is a `Try.Success`
Returns:
the result of applying the corresponding function

  - 

### peek

default Try<T> peek(@NonNull Consumer<? super T> action)
Performs the given action if this `Try` is a `Try.Success`, otherwise does nothing.
 

 This method is useful for side-effecting operations without transforming the value.

Specified by:
`peek` in interface `Value<T>`
Parameters:
`action` - a consumer of the value
Returns:
this `Try` instance
Throws:
`NullPointerException` - if `action` is null

  - 

### recover

@GwtIncompatible
default <X extends Throwable> Try<T> recover(@NonNull Class<X> exceptionType,
 @NonNull Function<? super X,? extends T> f)
Attempts to recover from a failure if the cause is an instance of the specified exception type.
 

 If this `Try` is a `Try.Success`, it is returned unchanged. If this is a `Try.Failure` and the cause
 is assignable from `exceptionType`, the recovery function `f` is applied to the cause inside a new `Try`.
 Otherwise, the original `Failure` is returned.
 

 Example:
 

```

 // = Success(13)
 Try.of(() -> 27/2).recover(ArithmeticException.class, x -> Integer.MAX_VALUE);

 // = Success(2147483647)
 Try.of(() -> 1/0)
    .recover(Error.class, x -> -1)
    .recover(ArithmeticException.class, x -> Integer.MAX_VALUE);

 // = Failure(java.lang.ArithmeticException: / by zero)
 Try.of(() -> 1/0).recover(Error.class, x -> Integer.MAX_VALUE);
 
```

Type Parameters:
`X` - the type of exception to handle
Parameters:
`exceptionType` - the specific exception type that should be recovered
`f` - a recovery function taking an exception of type `X` and producing a value
Returns:
a `Success` with the recovered value if the exception matches, otherwise this `Try`
Throws:
`NullPointerException` - if `exceptionType` or `f` is null

  - 

### recoverWith

@GwtIncompatible
default <X extends Throwable> Try<T> recoverWith(@NonNull Class<X> exceptionType,
 @NonNull Function<? super X,Try<? extends T>> f)
Attempts to recover from a failure by applying the given recovery function if the cause matches the specified exception type.
 

 If this `Try` is a `Try.Success`, it is returned unchanged. If this is a `Try.Failure` and the cause
 is assignable from `exceptionType`, the recovery function `f` is applied to the cause and returns a new `Try`.
 If the returned `Try` is a `isFailure()`, the recovery is considered unsuccessful.
 Otherwise, the original `Failure` is returned.
 

 Example:
 

```

 // = Success(13)
 Try.of(() -> 27/2).recoverWith(ArithmeticException.class, x -> Try.success(Integer.MAX_VALUE));

 // = Success(2147483647)
 Try.of(() -> 1/0)
    .recoverWith(Error.class, x -> Try.success(-1))
    .recoverWith(ArithmeticException.class, x -> Try.success(Integer.MAX_VALUE));

 // = Failure(java.lang.ArithmeticException: / by zero)
 Try.of(() -> 1/0).recoverWith(Error.class, x -> Try.success(Integer.MAX_VALUE));
 
```

Type Parameters:
`X` - the type of exception to handle
Parameters:
`exceptionType` - the specific exception type that should trigger recovery
`f` - a recovery function that takes an exception of type `X` and returns a new `Try` instance
Returns:
a `Try` representing the recovered value if the exception matches, otherwise this `Try`
Throws:
`NullPointerException` - if `exceptionType` or `f` is null

  - 

### recoverWith

@GwtIncompatible
default <X extends Throwable> Try<T> recoverWith(@NonNull Class<X> exceptionType,
 @NonNull Try<? extends T> recovered)
Recovers this `Try` with the given `recovered` value if this is a `Try.Failure`
 and the underlying cause is assignable to the specified `exceptionType`.
 

 If this `Try` is a `Try.Success`, or if the cause does not match `exceptionType`,
 the original `Try` is returned unchanged.
 

 Example:
 

```

 // = Success(13)
 Try.of(() -> 27/2).recoverWith(ArithmeticException.class, Try.success(Integer.MAX_VALUE));

 // = Success(2147483647)
 Try.of(() -> 1/0)
    .recoverWith(Error.class, Try.success(-1))
    .recoverWith(ArithmeticException.class, Try.success(Integer.MAX_VALUE));

 // = Failure(java.lang.ArithmeticException: / by zero)
 Try.of(() -> 1/0).recoverWith(Error.class, Try.success(Integer.MAX_VALUE));
 
```

Type Parameters:
`X` - the type of exception to handle
Parameters:
`exceptionType` - the exception type that triggers recovery
`recovered` - a `Try` instance to return if the cause matches `exceptionType`
Returns:
the given `recovered` if the exception matches, otherwise this `Try`
Throws:
`NullPointerException` - if `exceptionType` or `recovered` is null

  - 

### recover

@GwtIncompatible
default <X extends Throwable> Try<T> recover(@NonNull Class<X> exceptionType,
 T value)
Recovers this `Try` with the given `value` if this is a `Try.Failure`
 and the underlying cause matches the specified `exceptionType`.
 

 If this `Try` is a `Try.Success`, or if the cause is not assignable from `exceptionType`,
 the original `Try` is returned unchanged.
 

 Example:
 

```

 // = Success(13)
 Try.of(() -> 27/2).recover(ArithmeticException.class, 13);

 // = Success(2147483647)
 Try.of(() -> 1/0)
    .recover(Error.class, -1)
    .recover(ArithmeticException.class, Integer.MAX_VALUE);

 // = Failure(java.lang.ArithmeticException: / by zero)
 Try.of(() -> 1/0).recover(Error.class, Integer.MAX_VALUE);
 
```

Type Parameters:
`X` - the type of exception to handle
Parameters:
`exceptionType` - the exception type that triggers recovery
`value` - the value to return in a `Try.Success` if the cause matches
Returns:
a `Try` containing the recovery value if the exception matches, otherwise this `Try`
Throws:
`NullPointerException` - if `exceptionType` is null

  - 

### recover

default Try<T> recover(@NonNull Function<? super Throwable,? extends T> f)
Recovers this `Try` if it is a `Try.Failure` by applying the given recovery function `f`
 to the underlying exception. The result of the function is wrapped in a `Try.Success`.
 

 If this `Try` is already a `Try.Success`, it is returned unchanged.
 

 Example:
 

```

 // = Success(13)
 Try.of(() -> 27/2).recover(x -> Integer.MAX_VALUE);

 // = Success(2147483647)
 Try.of(() -> 1/0).recover(x -> Integer.MAX_VALUE);
 
```

Parameters:
`f` - A recovery function that takes the underlying exception and returns a value
Returns:
a `Try` containing either the original success value or the recovered value
Throws:
`NullPointerException` - if `f` is null

  - 

### recoverWith

default Try<T> recoverWith(@NonNull Function<? super Throwable,? extends Try<? extends T>> f)
Recovers this `Try` if it is a `Try.Failure` by applying the given recovery function `f`
 to the underlying exception. The recovery function returns a new `Try` instance. 
 

 If this `Try` is already a `Try.Success`, it is returned unchanged. 
 If an exception occurs while executing the recovery function, a new `Try.Failure` is returned 
 wrapping that exception.
 

 Example:
 

```

 // = Success(13)
 Try.of(() -> 27/2).recoverWith(x -> Try.success(Integer.MAX_VALUE));

 // = Success(2147483647)
 Try.of(() -> 1/0).recoverWith(x -> Try.success(Integer.MAX_VALUE));
 
```

Parameters:
`f` - A recovery function that takes the underlying exception and returns a new `Try`
Returns:
a `Try` containing either the original success value or the recovered `Try`
Throws:
`NullPointerException` - if `f` is null

  - 

### recoverAllAndTry

default Try<T> recoverAllAndTry(@NonNull CheckedFunction0<? extends T> recoveryAttempt)
Recovers from any failure by evaluating the given `recoveryAttempt` if this `Try` is a `Try.Failure`.
 

 If this `Try` is already a `Try.Success`, it is returned unchanged. The `recoveryAttempt` is
 evaluated using `of(CheckedFunction0)`, and its result is wrapped in a new `Try`.
 

 Example:
 

```

 // = Success(5)
 Try.of(() -> 5)
    .recoverAllAndTry(() -> 10);

 // = Success(10)
 Try.of(() -> 1/0)
    .recoverAllAndTry(() -> 10);
 
```

Parameters:
`recoveryAttempt` - A checked supplier providing a fallback value in case of failure
Returns:
a `Try` containing either the original success value or the result of `recoveryAttempt`
Throws:
`NullPointerException` - if `recoveryAttempt` is null

  - 

### recoverAndTry

default <X extends Throwable> Try<T> recoverAndTry(@NonNull Class<X> exceptionType,
 @NonNull CheckedFunction0<? extends T> recoveryAttempt)
Returns `this` if it is a `Try.Success`, or attempts to recover from a failure when the
 underlying cause is assignable to the specified `exceptionType` by evaluating the given
 `recoveryAttempt` (via `of(CheckedFunction0)`).
 

 Example usage:
 

```

 // = Success(5)
 Try.of(() -> 5)
    .recoverAndTry(ArithmeticException.class, () -> 10);

 // = Success(10)
 Try.of(() -> 1/0)
    .recoverAndTry(ArithmeticException.class, () -> 10);

 // = Failure(java.lang.ArithmeticException: / by zero)
 Try.of(() -> 1/0)
    .recoverAndTry(NullPointerException.class, () -> 10);
 
```

Type Parameters:
`X` - The type of the exception that may be recovered
Parameters:
`exceptionType` - The specific exception type that triggers the recovery
`recoveryAttempt` - A checked function providing a fallback value if the exception matches
Returns:
a `Try` containing either the original success value or the result of `recoveryAttempt`
Throws:
`NullPointerException` - if `exceptionType` or `recoveryAttempt` is null

  - 

### toEither

default Either<Throwable,T> toEither()
Converts this `Try` to an `Either`.
 

 If this is a `Try.Success`, the value is wrapped as a `Either.right(Object)`.
 If this is a `Try.Failure`, the cause is wrapped as a `Either.left(Object)`.

Returns:
a new `Either` representing this `Try`

  - 

### toEither

default <L> Either<L,T> toEither(@NonNull Function<? super Throwable,? extends L> throwableMapper)
Converts this `Try` to an `Either`, mapping the failure cause to a left value using
 the provided `Function`.

Type Parameters:
`L` - the left type of the resulting `Either`
Parameters:
`throwableMapper` - a function to convert the failure `Throwable` to type `L`
Returns:
a new `Either` representing this `Try`
Throws:
`NullPointerException` - if `throwableMapper` is null

  - 

### toValidation

default Validation<Throwable,T> toValidation()
Converts this `Try` to a `Validation`.
 

 A `Try.Success` is converted to a `Validation.valid(Object)`, while
 a `Try.Failure` is converted to a `Validation.invalid(Object)` containing
 the cause.

Returns:
a new `Validation` representing this `Try`

  - 

### toValidation

default <U> Validation<U,T> toValidation(@NonNull Function<? super Throwable,? extends U> throwableMapper)
Converts this `Try` to a `Validation`, mapping the failure cause to an invalid value
 using the provided `Function`.

 

```

 Validation<String, Integer> validation = Try.of(() -> 1/0).toValidation(Throwable::getMessage);
 
```

Type Parameters:
`U` - the type of the invalid value
Parameters:
`throwableMapper` - a function to convert the failure `Throwable` to type `U`
Returns:
a `Validation` representing this `Try`
Throws:
`NullPointerException` - if `throwableMapper` is null

  - 

### transform

default <U> U transform(@NonNull Function<? super Try<T>,? extends U> f)
Transforms this `Try` into a value of another type using the provided function.

Type Parameters:
`U` - the result type of the transformation
Parameters:
`f` - a transformation function
Returns:
the result of applying `f` to this `Try`
Throws:
`NullPointerException` - if `f` is null

  - 

### andFinally

default Try<T> andFinally(@NonNull Runnable runnable)
Executes a given `Runnable` after this `Try`, regardless of whether it is a
 `Try.Success` or `Try.Failure`.

Parameters:
`runnable` - a final action to perform
Returns:
this `Try` unchanged if the runnable succeeds, or a new `Try.Failure` if it throws
Throws:
`NullPointerException` - if `runnable` is null

  - 

### andFinallyTry

default Try<T> andFinallyTry(@NonNull CheckedRunnable runnable)
Executes a given `CheckedRunnable` after this `Try`, regardless of whether it is a
 `Try.Success` or `Try.Failure`.

Parameters:
`runnable` - a checked final action to perform
Returns:
this `Try` unchanged if the runnable succeeds, or a new `Try.Failure` if it throws
Throws:
`NullPointerException` - if `runnable` is null

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

  - 

### withResources

static <T1 extends AutoCloseable>
Try.WithResources1<T1> withResources(@NonNull CheckedFunction0<? extends T1> t1Supplier)
Creates a `Try`-with-resources builder that operates on one `AutoCloseable` resource.

Type Parameters:
`T1` - Type of the 1st resource.
Parameters:
`t1Supplier` - The supplier of the first resource.
Returns:
a new `Try.WithResources1` instance.

  - 

### withResources

static <T1 extends AutoCloseable,
T2 extends AutoCloseable>
Try.WithResources2<T1,T2> withResources(@NonNull CheckedFunction0<? extends T1> t1Supplier,
 @NonNull CheckedFunction0<? extends T2> t2Supplier)
Creates a `Try`-with-resources builder that operates on two `AutoCloseable` resources.

Type Parameters:
`T1` - Type of the 1st resource.
`T2` - Type of the 2nd resource.
Parameters:
`t1Supplier` - The supplier of the 1st resource.
`t2Supplier` - The supplier of the 2nd resource.
Returns:
a new `Try.WithResources2` instance.

  - 

### withResources

static <T1 extends AutoCloseable,
T2 extends AutoCloseable,
T3 extends AutoCloseable>
Try.WithResources3<T1,T2,T3> withResources(@NonNull CheckedFunction0<? extends T1> t1Supplier,
 @NonNull CheckedFunction0<? extends T2> t2Supplier,
 @NonNull CheckedFunction0<? extends T3> t3Supplier)
Creates a `Try`-with-resources builder that operates on three `AutoCloseable` resources.

Type Parameters:
`T1` - Type of the 1st resource.
`T2` - Type of the 2nd resource.
`T3` - Type of the 3rd resource.
Parameters:
`t1Supplier` - The supplier of the 1st resource.
`t2Supplier` - The supplier of the 2nd resource.
`t3Supplier` - The supplier of the 3rd resource.
Returns:
a new `Try.WithResources3` instance.

  - 

### withResources

static <T1 extends AutoCloseable,
T2 extends AutoCloseable,
T3 extends AutoCloseable,
T4 extends AutoCloseable>
Try.WithResources4<T1,T2,T3,T4> withResources(@NonNull CheckedFunction0<? extends T1> t1Supplier,
 @NonNull CheckedFunction0<? extends T2> t2Supplier,
 @NonNull CheckedFunction0<? extends T3> t3Supplier,
 @NonNull CheckedFunction0<? extends T4> t4Supplier)
Creates a `Try`-with-resources builder that operates on four `AutoCloseable` resources.

Type Parameters:
`T1` - Type of the 1st resource.
`T2` - Type of the 2nd resource.
`T3` - Type of the 3rd resource.
`T4` - Type of the 4th resource.
Parameters:
`t1Supplier` - The supplier of the 1st resource.
`t2Supplier` - The supplier of the 2nd resource.
`t3Supplier` - The supplier of the 3rd resource.
`t4Supplier` - The supplier of the 4th resource.
Returns:
a new `Try.WithResources4` instance.

  - 

### withResources

static <T1 extends AutoCloseable,
T2 extends AutoCloseable,
T3 extends AutoCloseable,
T4 extends AutoCloseable,
T5 extends AutoCloseable>
Try.WithResources5<T1,T2,T3,T4,T5> withResources(@NonNull CheckedFunction0<? extends T1> t1Supplier,
 @NonNull CheckedFunction0<? extends T2> t2Supplier,
 @NonNull CheckedFunction0<? extends T3> t3Supplier,
 @NonNull CheckedFunction0<? extends T4> t4Supplier,
 @NonNull CheckedFunction0<? extends T5> t5Supplier)
Creates a `Try`-with-resources builder that operates on five `AutoCloseable` resources.

Type Parameters:
`T1` - Type of the 1st resource.
`T2` - Type of the 2nd resource.
`T3` - Type of the 3rd resource.
`T4` - Type of the 4th resource.
`T5` - Type of the 5th resource.
Parameters:
`t1Supplier` - The supplier of the 1st resource.
`t2Supplier` - The supplier of the 2nd resource.
`t3Supplier` - The supplier of the 3rd resource.
`t4Supplier` - The supplier of the 4th resource.
`t5Supplier` - The supplier of the 5th resource.
Returns:
a new `Try.WithResources5` instance.

  - 

### withResources

static <T1 extends AutoCloseable,
T2 extends AutoCloseable,
T3 extends AutoCloseable,
T4 extends AutoCloseable,
T5 extends AutoCloseable,
T6 extends AutoCloseable>
Try.WithResources6<T1,T2,T3,T4,T5,T6> withResources(@NonNull CheckedFunction0<? extends T1> t1Supplier,
 @NonNull CheckedFunction0<? extends T2> t2Supplier,
 @NonNull CheckedFunction0<? extends T3> t3Supplier,
 @NonNull CheckedFunction0<? extends T4> t4Supplier,
 @NonNull CheckedFunction0<? extends T5> t5Supplier,
 @NonNull CheckedFunction0<? extends T6> t6Supplier)
Creates a `Try`-with-resources builder that operates on six `AutoCloseable` resources.

Type Parameters:
`T1` - Type of the 1st resource.
`T2` - Type of the 2nd resource.
`T3` - Type of the 3rd resource.
`T4` - Type of the 4th resource.
`T5` - Type of the 5th resource.
`T6` - Type of the 6th resource.
Parameters:
`t1Supplier` - The supplier of the 1st resource.
`t2Supplier` - The supplier of the 2nd resource.
`t3Supplier` - The supplier of the 3rd resource.
`t4Supplier` - The supplier of the 4th resource.
`t5Supplier` - The supplier of the 5th resource.
`t6Supplier` - The supplier of the 6th resource.
Returns:
a new `Try.WithResources6` instance.

  - 

### withResources

static <T1 extends AutoCloseable,
T2 extends AutoCloseable,
T3 extends AutoCloseable,
T4 extends AutoCloseable,
T5 extends AutoCloseable,
T6 extends AutoCloseable,
T7 extends AutoCloseable>
Try.WithResources7<T1,T2,T3,T4,T5,T6,T7> withResources(@NonNull CheckedFunction0<? extends T1> t1Supplier,
 @NonNull CheckedFunction0<? extends T2> t2Supplier,
 @NonNull CheckedFunction0<? extends T3> t3Supplier,
 @NonNull CheckedFunction0<? extends T4> t4Supplier,
 @NonNull CheckedFunction0<? extends T5> t5Supplier,
 @NonNull CheckedFunction0<? extends T6> t6Supplier,
 @NonNull CheckedFunction0<? extends T7> t7Supplier)
Creates a `Try`-with-resources builder that operates on seven `AutoCloseable` resources.

Type Parameters:
`T1` - Type of the 1st resource.
`T2` - Type of the 2nd resource.
`T3` - Type of the 3rd resource.
`T4` - Type of the 4th resource.
`T5` - Type of the 5th resource.
`T6` - Type of the 6th resource.
`T7` - Type of the 7th resource.
Parameters:
`t1Supplier` - The supplier of the 1st resource.
`t2Supplier` - The supplier of the 2nd resource.
`t3Supplier` - The supplier of the 3rd resource.
`t4Supplier` - The supplier of the 4th resource.
`t5Supplier` - The supplier of the 5th resource.
`t6Supplier` - The supplier of the 6th resource.
`t7Supplier` - The supplier of the 7th resource.
Returns:
a new `Try.WithResources7` instance.

  - 

### withResources

static <T1 extends AutoCloseable,
T2 extends AutoCloseable,
T3 extends AutoCloseable,
T4 extends AutoCloseable,
T5 extends AutoCloseable,
T6 extends AutoCloseable,
T7 extends AutoCloseable,
T8 extends AutoCloseable>
Try.WithResources8<T1,T2,T3,T4,T5,T6,T7,T8> withResources(@NonNull CheckedFunction0<? extends T1> t1Supplier,
 @NonNull CheckedFunction0<? extends T2> t2Supplier,
 @NonNull CheckedFunction0<? extends T3> t3Supplier,
 @NonNull CheckedFunction0<? extends T4> t4Supplier,
 @NonNull CheckedFunction0<? extends T5> t5Supplier,
 @NonNull CheckedFunction0<? extends T6> t6Supplier,
 @NonNull CheckedFunction0<? extends T7> t7Supplier,
 @NonNull CheckedFunction0<? extends T8> t8Supplier)
Creates a `Try`-with-resources builder that operates on eight `AutoCloseable` resources.

Type Parameters:
`T1` - Type of the 1st resource.
`T2` - Type of the 2nd resource.
`T3` - Type of the 3rd resource.
`T4` - Type of the 4th resource.
`T5` - Type of the 5th resource.
`T6` - Type of the 6th resource.
`T7` - Type of the 7th resource.
`T8` - Type of the 8th resource.
Parameters:
`t1Supplier` - The supplier of the 1st resource.
`t2Supplier` - The supplier of the 2nd resource.
`t3Supplier` - The supplier of the 3rd resource.
`t4Supplier` - The supplier of the 4th resource.
`t5Supplier` - The supplier of the 5th resource.
`t6Supplier` - The supplier of the 6th resource.
`t7Supplier` - The supplier of the 7th resource.
`t8Supplier` - The supplier of the 8th resource.
Returns:
a new `Try.WithResources8` instance.