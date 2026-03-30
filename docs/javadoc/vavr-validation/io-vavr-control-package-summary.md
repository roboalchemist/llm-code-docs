# Package io.vavr.control

---

package io.vavr.control

Control structures like the disjoint union type Either, the optional value type
 Option and Try for exception handling.
 

 **Either**
 

 The control package contains an implementation of the Either control which is either Left or Right.
 A given Either is projected to a Left or a Right.
 Both cases can be further processed with control operations map, flatMap, filter.
 If a Right is projected to a Left, the Left control operations have no effect on the Right value.
 If a Left is projected to a Right, the Right control operations have no effect on the Left value.
 

 **Option**
 

 The Option control is a replacement for Optional. An Option is either
 Option.Some value or Option.None.
 In contrast to Optional, Option supports null values, i.e. it is possible to call `new Some(null)`.
 However, `Option.of(null)` results in None.
 

 **Try**
 

 Exceptions are handled with the Try control which is either a
 Try.Success, containing a result, or a Try.Failure,
 containing an Exception.

- 

Related Packages

Package
Description
io.vavr

Beside `API` the io.vavr package contains core types like (Checked)Functions and Tuples.

io.vavr.collection

Purely functional collections based on Traversable.

io.vavr.concurrent

This package contains basic building blocks for creating fast, asynchronous, non-blocking parallel code.

- 

Class
Description
Either<L,R>

Represents a value of one of two possible types: `Either.Left` or `Either.Right`.

Either.Failure

An exception wrapper used to propagate values through exception handling mechanisms.

Either.Left<L,R>

The `Left` version of an `Either`.

Either.LeftProjection<L,R>
Deprecated.
Either is right-biased.

Either.Right<L,R>

The `Right` version of an `Either`.

Either.RightProjection<L,R>
Deprecated.
Either is right-biased.

HashCodes
Deprecated.
Will be removed from public API

Option<T>

A replacement for `Optional`.

Option.None<T>

None is a singleton representation of the undefined `Option`.

Option.Some<T>

Some represents a defined `Option`.

Try<T>

A control structure that allows writing safe code without explicitly managing try-catch blocks for exceptions.

Try.Failure<T>

Represents a failed `Try` containing a `Throwable` as the cause.

Try.Success<T>

Represents a successful `Try` containing a value.

Try.WithResources1<T1 extends AutoCloseable>

A `Try`-with-resources builder that operates on one `AutoCloseable` resource.

Try.WithResources2<T1 extends AutoCloseable,T2 extends AutoCloseable>

A `Try`-with-resources builder that operates on two `AutoCloseable` resources.

Try.WithResources3<T1 extends AutoCloseable,T2 extends AutoCloseable,T3 extends AutoCloseable>

A `Try`-with-resources builder that operates on three `AutoCloseable` resources.

Try.WithResources4<T1 extends AutoCloseable,T2 extends AutoCloseable,T3 extends AutoCloseable,T4 extends AutoCloseable>

A `Try`-with-resources builder that operates on four `AutoCloseable` resources.

Try.WithResources5<T1 extends AutoCloseable,T2 extends AutoCloseable,T3 extends AutoCloseable,T4 extends AutoCloseable,T5 extends AutoCloseable>

A `Try`-with-resources builder that operates on five `AutoCloseable` resources.

Try.WithResources6<T1 extends AutoCloseable,T2 extends AutoCloseable,T3 extends AutoCloseable,T4 extends AutoCloseable,T5 extends AutoCloseable,T6 extends AutoCloseable>

A `Try`-with-resources builder that operates on six `AutoCloseable` resources.

Try.WithResources7<T1 extends AutoCloseable,T2 extends AutoCloseable,T3 extends AutoCloseable,T4 extends AutoCloseable,T5 extends AutoCloseable,T6 extends AutoCloseable,T7 extends AutoCloseable>

A `Try`-with-resources builder that operates on seven `AutoCloseable` resources.

Try.WithResources8<T1 extends AutoCloseable,T2 extends AutoCloseable,T3 extends AutoCloseable,T4 extends AutoCloseable,T5 extends AutoCloseable,T6 extends AutoCloseable,T7 extends AutoCloseable,T8 extends AutoCloseable>

A `Try`-with-resources builder that operates on eight `AutoCloseable` resources.

Validation<E,T>

An implementation similar to Scalaz's 
 Validation control.

Validation.Builder<E,T1,T2>

A builder that holds two Validation instances, used for combining validations
 and applying functions that take two arguments.

Validation.Builder3<E,T1,T2,T3>

A builder that holds three Validation instances, used for combining validations
 and applying functions that take three arguments.

Validation.Builder4<E,T1,T2,T3,T4>

A builder that holds four Validation instances, used for combining validations
 and applying functions that take four arguments.

Validation.Builder5<E,T1,T2,T3,T4,T5>

A builder that holds five Validation instances, used for combining validations
 and applying functions that take five arguments.

Validation.Builder6<E,T1,T2,T3,T4,T5,T6>

A builder that holds six Validation instances, used for combining validations
 and applying functions that take six arguments.

Validation.Builder7<E,T1,T2,T3,T4,T5,T6,T7>

A builder that holds seven Validation instances, used for combining validations
 and applying functions that take seven arguments.

Validation.Builder8<E,T1,T2,T3,T4,T5,T6,T7,T8>

A builder that holds eight Validation instances, used for combining validations
 and applying functions that take eight arguments.

Validation.Invalid<E,T>

An invalid Validation

Validation.Valid<E,T>

A valid Validation