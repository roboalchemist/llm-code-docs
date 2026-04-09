Package io.vavr

# Class API

java.lang.Object
io.vavr.API

---

public final class API
extends Object
The most basic Vavr functionality is accessed through this API class.

 

```

 import static io.vavr.API.*;
 
```

 
## For-comprehension

 

 The `For`-comprehension is syntactic sugar for nested for-loops. We write

 

```

 // lazily evaluated
 Iterator<R> result = For(iterable1, iterable2, ..., iterableN).yield(f);
 
```

 or

 

```

 Iterator<R> result =
     For(iterable1, v1 ->
         For(iterable2, v2 ->
             ...
             For(iterableN).yield(vN -> f.apply(v1, v2, ..., vN))
         )
     );
 
```

 instead of

 

```

 for(T1 v1 : iterable1) {
     for (T2 v2 : iterable2) {
         ...
         for (TN vN : iterableN) {
             R result = f.apply(v1, v2, ..., VN);
             //
             // We are forced to perform side effects to do s.th. meaningful with the result.
             //
         }
     }
 }
 
```

 Please note that values like Option, Try, Future, etc. are also iterable.
 

 Given a suitable function
 f: `(v1, v2, ..., vN) -> ...` and `1 <= N <= 8` iterables, the result is a Stream of the
 mapped cross product elements.

 

```

 { f(v1, v2, ..., vN) | v1 â iterable1, ... vN â iterableN }
 
```

 As with all Vavr Values, the result of a For-comprehension can be converted
 to standard Java library and Vavr types.

Author:
Daniel Dietrich

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static class `
`API.For1<T1>`

For-comprehension with one Iterable.

`static class `
`API.For1Either<L,T1>`

For-comprehension with one Either.

`static class `
`API.For1Future<T1>`

For-comprehension with one Future.

`static class `
`API.For1List<T1>`

For-comprehension with one List.

`static class `
`API.For1Option<T1>`

For-comprehension with one Option.

`static class `
`API.For1Try<T1>`

For-comprehension with one Try.

`static class `
`API.For1Validation<L,T1>`

For-comprehension with one Validation.

`static class `
`API.For2<T1,T2>`

For-comprehension with two Iterables.

`static class `
`API.For2Either<L,T1,T2>`

For-comprehension with two Eithers.

`static class `
`API.For2Future<T1,T2>`

For-comprehension with two Futures.

`static class `
`API.For2List<T1,T2>`

For-comprehension with two Lists.

`static class `
`API.For2Option<T1,T2>`

For-comprehension with two Options.

`static class `
`API.For2Try<T1,T2>`

For-comprehension with two Trys.

`static class `
`API.For2Validation<L,T1,T2>`

For-comprehension with two Validations.

`static class `
`API.For3<T1,T2,T3>`

For-comprehension with three Iterables.

`static class `
`API.For3Either<L,T1,T2,T3>`

For-comprehension with three Eithers.

`static class `
`API.For3Future<T1,T2,T3>`

For-comprehension with three Futures.

`static class `
`API.For3List<T1,T2,T3>`

For-comprehension with three Lists.

`static class `
`API.For3Option<T1,T2,T3>`

For-comprehension with three Options.

`static class `
`API.For3Try<T1,T2,T3>`

For-comprehension with three Trys.

`static class `
`API.For3Validation<L,T1,T2,T3>`

For-comprehension with three Validations.

`static class `
`API.For4<T1,T2,T3,T4>`

For-comprehension with 4 Iterables.

`static class `
`API.For4Either<L,T1,T2,T3,T4>`

For-comprehension with 4 Eithers.

`static class `
`API.For4Future<T1,T2,T3,T4>`

For-comprehension with 4 Futures.

`static class `
`API.For4List<T1,T2,T3,T4>`

For-comprehension with 4 Lists.

`static class `
`API.For4Option<T1,T2,T3,T4>`

For-comprehension with 4 Options.

`static class `
`API.For4Try<T1,T2,T3,T4>`

For-comprehension with 4 Trys.

`static class `
`API.For4Validation<L,T1,T2,T3,T4>`

For-comprehension with 4 Validations.

`static class `
`API.For5<T1,T2,T3,T4,T5>`

For-comprehension with 5 Iterables.

`static class `
`API.For5Either<L,T1,T2,T3,T4,T5>`

For-comprehension with 5 Eithers.

`static class `
`API.For5Future<T1,T2,T3,T4,T5>`

For-comprehension with 5 Futures.

`static class `
`API.For5List<T1,T2,T3,T4,T5>`

For-comprehension with 5 Lists.

`static class `
`API.For5Option<T1,T2,T3,T4,T5>`

For-comprehension with 5 Options.

`static class `
`API.For5Try<T1,T2,T3,T4,T5>`

For-comprehension with 5 Trys.

`static class `
`API.For5Validation<L,T1,T2,T3,T4,T5>`

For-comprehension with 5 Validations.

`static class `
`API.For6<T1,T2,T3,T4,T5,T6>`

For-comprehension with 6 Iterables.

`static class `
`API.For6Either<L,T1,T2,T3,T4,T5,T6>`

For-comprehension with 6 Eithers.

`static class `
`API.For6Future<T1,T2,T3,T4,T5,T6>`

For-comprehension with 6 Futures.

`static class `
`API.For6List<T1,T2,T3,T4,T5,T6>`

For-comprehension with 6 Lists.

`static class `
`API.For6Option<T1,T2,T3,T4,T5,T6>`

For-comprehension with 6 Options.

`static class `
`API.For6Try<T1,T2,T3,T4,T5,T6>`

For-comprehension with 6 Trys.

`static class `
`API.For6Validation<L,T1,T2,T3,T4,T5,T6>`

For-comprehension with 6 Validations.

`static class `
`API.For7<T1,T2,T3,T4,T5,T6,T7>`

For-comprehension with 7 Iterables.

`static class `
`API.For7Either<L,T1,T2,T3,T4,T5,T6,T7>`

For-comprehension with 7 Eithers.

`static class `
`API.For7Future<T1,T2,T3,T4,T5,T6,T7>`

For-comprehension with 7 Futures.

`static class `
`API.For7List<T1,T2,T3,T4,T5,T6,T7>`

For-comprehension with 7 Lists.

`static class `
`API.For7Option<T1,T2,T3,T4,T5,T6,T7>`

For-comprehension with 7 Options.

`static class `
`API.For7Try<T1,T2,T3,T4,T5,T6,T7>`

For-comprehension with 7 Trys.

`static class `
`API.For7Validation<L,T1,T2,T3,T4,T5,T6,T7>`

For-comprehension with 7 Validations.

`static class `
`API.For8<T1,T2,T3,T4,T5,T6,T7,T8>`

For-comprehension with 8 Iterables.

`static class `
`API.For8Either<L,T1,T2,T3,T4,T5,T6,T7,T8>`

For-comprehension with 8 Eithers.

`static class `
`API.For8Future<T1,T2,T3,T4,T5,T6,T7,T8>`

For-comprehension with 8 Futures.

`static class `
`API.For8List<T1,T2,T3,T4,T5,T6,T7,T8>`

For-comprehension with 8 Lists.

`static class `
`API.For8Option<T1,T2,T3,T4,T5,T6,T7,T8>`

For-comprehension with 8 Options.

`static class `
`API.For8Try<T1,T2,T3,T4,T5,T6,T7,T8>`

For-comprehension with 8 Trys.

`static class `
`API.For8Validation<L,T1,T2,T3,T4,T5,T6,T7,T8>`

For-comprehension with 8 Validations.

`static class `
`API.ForLazy2Either<L,T1,T2>`

A lazily evaluated `For`-comprehension with two Eithers.

`static class `
`API.ForLazy2Future<T1,T2>`

A lazily evaluated `For`-comprehension with two Futures.

`static class `
`API.ForLazy2List<T1,T2>`

A lazily evaluated `For`-comprehension with two Lists.

`static class `
`API.ForLazy2Option<T1,T2>`

A lazily evaluated `For`-comprehension with two Options.

`static class `
`API.ForLazy2Try<T1,T2>`

A lazily evaluated `For`-comprehension with two Trys.

`static class `
`API.ForLazy2Validation<L,T1,T2>`

A lazily evaluated `For`-comprehension with two Validations.

`static class `
`API.ForLazy3Either<L,T1,T2,T3>`

A lazily evaluated `For`-comprehension with three Eithers.

`static class `
`API.ForLazy3Future<T1,T2,T3>`

A lazily evaluated `For`-comprehension with three Futures.

`static class `
`API.ForLazy3List<T1,T2,T3>`

A lazily evaluated `For`-comprehension with three Lists.

`static class `
`API.ForLazy3Option<T1,T2,T3>`

A lazily evaluated `For`-comprehension with three Options.

`static class `
`API.ForLazy3Try<T1,T2,T3>`

A lazily evaluated `For`-comprehension with three Trys.

`static class `
`API.ForLazy3Validation<L,T1,T2,T3>`

A lazily evaluated `For`-comprehension with three Validations.

`static class `
`API.ForLazy4Either<L,T1,T2,T3,T4>`

A lazily evaluated `For`-comprehension with 4 Eithers.

`static class `
`API.ForLazy4Future<T1,T2,T3,T4>`

A lazily evaluated `For`-comprehension with 4 Futures.

`static class `
`API.ForLazy4List<T1,T2,T3,T4>`

A lazily evaluated `For`-comprehension with 4 Lists.

`static class `
`API.ForLazy4Option<T1,T2,T3,T4>`

A lazily evaluated `For`-comprehension with 4 Options.

`static class `
`API.ForLazy4Try<T1,T2,T3,T4>`

A lazily evaluated `For`-comprehension with 4 Trys.

`static class `
`API.ForLazy4Validation<L,T1,T2,T3,T4>`

A lazily evaluated `For`-comprehension with 4 Validations.

`static class `
`API.ForLazy5Either<L,T1,T2,T3,T4,T5>`

A lazily evaluated `For`-comprehension with 5 Eithers.

`static class `
`API.ForLazy5Future<T1,T2,T3,T4,T5>`

A lazily evaluated `For`-comprehension with 5 Futures.

`static class `
`API.ForLazy5List<T1,T2,T3,T4,T5>`

A lazily evaluated `For`-comprehension with 5 Lists.

`static class `
`API.ForLazy5Option<T1,T2,T3,T4,T5>`

A lazily evaluated `For`-comprehension with 5 Options.

`static class `
`API.ForLazy5Try<T1,T2,T3,T4,T5>`

A lazily evaluated `For`-comprehension with 5 Trys.

`static class `
`API.ForLazy5Validation<L,T1,T2,T3,T4,T5>`

A lazily evaluated `For`-comprehension with 5 Validations.

`static class `
`API.ForLazy6Either<L,T1,T2,T3,T4,T5,T6>`

A lazily evaluated `For`-comprehension with 6 Eithers.

`static class `
`API.ForLazy6Future<T1,T2,T3,T4,T5,T6>`

A lazily evaluated `For`-comprehension with 6 Futures.

`static class `
`API.ForLazy6List<T1,T2,T3,T4,T5,T6>`

A lazily evaluated `For`-comprehension with 6 Lists.

`static class `
`API.ForLazy6Option<T1,T2,T3,T4,T5,T6>`

A lazily evaluated `For`-comprehension with 6 Options.

`static class `
`API.ForLazy6Try<T1,T2,T3,T4,T5,T6>`

A lazily evaluated `For`-comprehension with 6 Trys.

`static class `
`API.ForLazy6Validation<L,T1,T2,T3,T4,T5,T6>`

A lazily evaluated `For`-comprehension with 6 Validations.

`static class `
`API.ForLazy7Either<L,T1,T2,T3,T4,T5,T6,T7>`

A lazily evaluated `For`-comprehension with 7 Eithers.

`static class `
`API.ForLazy7Future<T1,T2,T3,T4,T5,T6,T7>`

A lazily evaluated `For`-comprehension with 7 Futures.

`static class `
`API.ForLazy7List<T1,T2,T3,T4,T5,T6,T7>`

A lazily evaluated `For`-comprehension with 7 Lists.

`static class `
`API.ForLazy7Option<T1,T2,T3,T4,T5,T6,T7>`

A lazily evaluated `For`-comprehension with 7 Options.

`static class `
`API.ForLazy7Try<T1,T2,T3,T4,T5,T6,T7>`

A lazily evaluated `For`-comprehension with 7 Trys.

`static class `
`API.ForLazy7Validation<L,T1,T2,T3,T4,T5,T6,T7>`

A lazily evaluated `For`-comprehension with 7 Validations.

`static class `
`API.ForLazy8Either<L,T1,T2,T3,T4,T5,T6,T7,T8>`

A lazily evaluated `For`-comprehension with 8 Eithers.

`static class `
`API.ForLazy8Future<T1,T2,T3,T4,T5,T6,T7,T8>`

A lazily evaluated `For`-comprehension with 8 Futures.

`static class `
`API.ForLazy8List<T1,T2,T3,T4,T5,T6,T7,T8>`

A lazily evaluated `For`-comprehension with 8 Lists.

`static class `
`API.ForLazy8Option<T1,T2,T3,T4,T5,T6,T7,T8>`

A lazily evaluated `For`-comprehension with 8 Options.

`static class `
`API.ForLazy8Try<T1,T2,T3,T4,T5,T6,T7,T8>`

A lazily evaluated `For`-comprehension with 8 Trys.

`static class `
`API.ForLazy8Validation<L,T1,T2,T3,T4,T5,T6,T7,T8>`

A lazily evaluated `For`-comprehension with 8 Validations.

`static final class `
`API.Match<T>`

Scala-like structural pattern matching for Java.

- 

## Method Summary

Modifier and Type
Method
Description
`static <T> API.Match.Pattern0<T>`
`$()`

Wildcard pattern, matches any value.

`static <T> API.Match.Pattern0<T>`
`$(@NonNull Predicate<? super T> predicate)`

Guard pattern, checks if a predicate is satisfied.

`static <T> API.Match.Pattern0<T>`
`$(T prototype)`

Value pattern, checks for equality.

`static <T> Array<T>`
`Array()`

Alias for `Array.empty()`

`static <T> Array<T>`
`Array(T element)`

Alias for `Array.of(Object)`

`static <T> Array<T>`
`Array(T @NonNull ... elements)`

Alias for `Array.of(Object...)`

`static <T,
R> API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern0<T> pattern,
 @NonNull Function<? super T,? extends R> f)`

Returns a `API.Match.Case0` instance for a specific `API.Match.Pattern0` and `Function`

`static <T,
R> API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern0<T> pattern,
 @NonNull Supplier<? extends R> supplier)`

Returns a `API.Match.Case0` instance for a specific `API.Match.Pattern0` and `Supplier`

`static <T,
R> API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern0<T> pattern,
 R retVal)`

Returns a `API.Match.Case0` instance for a specific `API.Match.Pattern0` and a constant value

`static <T,
T1,
R> API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern1<T,T1> pattern,
 @NonNull Function<? super T1,? extends R> f)`

Returns a `API.Match.Case1` instance for a specific `API.Match.Pattern1` and `Function`

`static <T,
T1,
R> API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern1<T,T1> pattern,
 @NonNull Supplier<? extends R> supplier)`

Returns a `API.Match.Case1` instance for a specific `API.Match.Pattern1` and `Supplier`

`static <T,
T1,
R> API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern1<T,T1> pattern,
 R retVal)`

Returns a `API.Match.Case1` instance for a specific `API.Match.Pattern1` and a constant value

`static <T,
T1,
T2,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern2<T,T1,T2> pattern,
 @NonNull BiFunction<? super T1,? super T2,? extends R> f)`

Returns a `API.Match.Case2` instance for a specific `API.Match.Pattern2` and `BiFunction`

`static <T,
T1,
T2,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern2<T,T1,T2> pattern,
 @NonNull Supplier<? extends R> supplier)`

Returns a `API.Match.Case2` instance for a specific `API.Match.Pattern2` and `Supplier`

`static <T,
T1,
T2,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern2<T,T1,T2> pattern,
 R retVal)`

Returns a `API.Match.Case2` instance for a specific `API.Match.Pattern2` and a constant value

`static <T,
T1,
T2,
T3,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern3<T,T1,T2,T3> pattern,
 @NonNull Function3<? super T1,? super T2,? super T3,? extends R> f)`

Returns a `API.Match.Case3` instance for a specific `API.Match.Pattern3` and `Function3`

`static <T,
T1,
T2,
T3,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern3<T,T1,T2,T3> pattern,
 @NonNull Supplier<? extends R> supplier)`

Returns a `API.Match.Case3` instance for a specific `API.Match.Pattern3` and `Supplier`

`static <T,
T1,
T2,
T3,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern3<T,T1,T2,T3> pattern,
 R retVal)`

Returns a `API.Match.Case3` instance for a specific `API.Match.Pattern3` and a constant value

`static <T,
T1,
T2,
T3,
T4,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern4<T,T1,T2,T3,T4> pattern,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,? extends R> f)`

Returns a `API.Match.Case4` instance for a specific `API.Match.Pattern4` and `Function4`

`static <T,
T1,
T2,
T3,
T4,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern4<T,T1,T2,T3,T4> pattern,
 @NonNull Supplier<? extends R> supplier)`

Returns a `API.Match.Case4` instance for a specific `API.Match.Pattern4` and `Supplier`

`static <T,
T1,
T2,
T3,
T4,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern4<T,T1,T2,T3,T4> pattern,
 R retVal)`

Returns a `API.Match.Case4` instance for a specific `API.Match.Pattern4` and a constant value

`static <T,
T1,
T2,
T3,
T4,
T5,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern5<T,T1,T2,T3,T4,T5> pattern,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,? extends R> f)`

Returns a `API.Match.Case5` instance for a specific `API.Match.Pattern5` and `Function5`

`static <T,
T1,
T2,
T3,
T4,
T5,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern5<T,T1,T2,T3,T4,T5> pattern,
 @NonNull Supplier<? extends R> supplier)`

Returns a `API.Match.Case5` instance for a specific `API.Match.Pattern5` and `Supplier`

`static <T,
T1,
T2,
T3,
T4,
T5,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern5<T,T1,T2,T3,T4,T5> pattern,
 R retVal)`

Returns a `API.Match.Case5` instance for a specific `API.Match.Pattern5` and a constant value

`static <T,
T1,
T2,
T3,
T4,
T5,
T6,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern6<T,T1,T2,T3,T4,T5,T6> pattern,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? extends R> f)`

Returns a `API.Match.Case6` instance for a specific `API.Match.Pattern6` and `Function6`

`static <T,
T1,
T2,
T3,
T4,
T5,
T6,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern6<T,T1,T2,T3,T4,T5,T6> pattern,
 @NonNull Supplier<? extends R> supplier)`

Returns a `API.Match.Case6` instance for a specific `API.Match.Pattern6` and `Supplier`

`static <T,
T1,
T2,
T3,
T4,
T5,
T6,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern6<T,T1,T2,T3,T4,T5,T6> pattern,
 R retVal)`

Returns a `API.Match.Case6` instance for a specific `API.Match.Pattern6` and a constant value

`static <T,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern7<T,T1,T2,T3,T4,T5,T6,T7> pattern,
 @NonNull Function7<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,? extends R> f)`

Returns a `API.Match.Case7` instance for a specific `API.Match.Pattern7` and `Function7`

`static <T,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern7<T,T1,T2,T3,T4,T5,T6,T7> pattern,
 @NonNull Supplier<? extends R> supplier)`

Returns a `API.Match.Case7` instance for a specific `API.Match.Pattern7` and `Supplier`

`static <T,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern7<T,T1,T2,T3,T4,T5,T6,T7> pattern,
 R retVal)`

Returns a `API.Match.Case7` instance for a specific `API.Match.Pattern7` and a constant value

`static <T,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern8<T,T1,T2,T3,T4,T5,T6,T7,T8> pattern,
 @NonNull Function8<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,? super T8,? extends R> f)`

Returns a `API.Match.Case8` instance for a specific `API.Match.Pattern8` and `Function8`

`static <T,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern8<T,T1,T2,T3,T4,T5,T6,T7,T8> pattern,
 @NonNull Supplier<? extends R> supplier)`

Returns a `API.Match.Case8` instance for a specific `API.Match.Pattern8` and `Supplier`

`static <T,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8,
R>
API.Match.Case<T,R>`
`Case(@NonNull API.Match.Pattern8<T,T1,T2,T3,T4,T5,T6,T7,T8> pattern,
 R retVal)`

Returns a `API.Match.Case8` instance for a specific `API.Match.Pattern8` and a constant value

`static CharSeq`
`CharSeq(char character)`

Alias for `CharSeq.of(char)`

`static CharSeq`
`CharSeq(char... characters)`

Alias for `CharSeq.of(char...)`

`static CharSeq`
`CharSeq(CharSequence sequence)`

Alias for `CharSeq.of(CharSequence)`

`static <R> CheckedFunction0<R>`
`CheckedFunction(CheckedFunction0<R> methodReference)`

Alias for `CheckedFunction0.of(CheckedFunction0)`

`static <T1,
R> CheckedFunction1<T1,R>`
`CheckedFunction(CheckedFunction1<T1,R> methodReference)`

Alias for `CheckedFunction1.of(CheckedFunction1)`

`static <T1,
T2,
R>
CheckedFunction2<T1,T2,R>`
`CheckedFunction(CheckedFunction2<T1,T2,R> methodReference)`

Alias for `CheckedFunction2.of(CheckedFunction2)`

`static <T1,
T2,
T3,
R>
CheckedFunction3<T1,T2,T3,R>`
`CheckedFunction(CheckedFunction3<T1,T2,T3,R> methodReference)`

Alias for `CheckedFunction3.of(CheckedFunction3)`

`static <T1,
T2,
T3,
T4,
R>
CheckedFunction4<T1,T2,T3,T4,R>`
`CheckedFunction(CheckedFunction4<T1,T2,T3,T4,R> methodReference)`

Alias for `CheckedFunction4.of(CheckedFunction4)`

`static <T1,
T2,
T3,
T4,
T5,
R>
CheckedFunction5<T1,T2,T3,T4,T5,R>`
`CheckedFunction(CheckedFunction5<T1,T2,T3,T4,T5,R> methodReference)`

Alias for `CheckedFunction5.of(CheckedFunction5)`

`static <T1,
T2,
T3,
T4,
T5,
T6,
R>
CheckedFunction6<T1,T2,T3,T4,T5,T6,R>`
`CheckedFunction(CheckedFunction6<T1,T2,T3,T4,T5,T6,R> methodReference)`

Alias for `CheckedFunction6.of(CheckedFunction6)`

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
R>
CheckedFunction7<T1,T2,T3,T4,T5,T6,T7,R>`
`CheckedFunction(CheckedFunction7<T1,T2,T3,T4,T5,T6,T7,R> methodReference)`

Alias for `CheckedFunction7.of(CheckedFunction7)`

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8,
R>
CheckedFunction8<T1,T2,T3,T4,T5,T6,T7,T8,R>`
`CheckedFunction(CheckedFunction8<T1,T2,T3,T4,T5,T6,T7,T8,R> methodReference)`

Alias for `CheckedFunction8.of(CheckedFunction8)`

`static <T> Try.Failure<T>`
`Failure(Throwable exception)`

Alias for `Try.failure(Throwable)`

`static <T1> API.For1List<T1>`
`For(@NonNull List<T1> ts1)`

Creates a `For`-comprehension of one List.

`static <T1,
T2> API.ForLazy2List<T1,T2>`
`For(@NonNull List<T1> ts1,
 @NonNull Function1<? super T1,List<T2>> ts2)`

Creates a lazy `For`-comprehension over two Lists.

`static <T1,
T2,
T3>
API.ForLazy3List<T1,T2,T3>`
`For(@NonNull List<T1> ts1,
 @NonNull Function1<? super T1,List<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,List<T3>> ts3)`

Creates a lazy `For`-comprehension over three Lists.

`static <T1,
T2,
T3,
T4>
API.ForLazy4List<T1,T2,T3,T4>`
`For(@NonNull List<T1> ts1,
 @NonNull Function1<? super T1,List<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,List<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,List<T4>> ts4)`

Creates a lazy `For`-comprehension over 4 Lists.

`static <T1,
T2,
T3,
T4,
T5>
API.ForLazy5List<T1,T2,T3,T4,T5>`
`For(@NonNull List<T1> ts1,
 @NonNull Function1<? super T1,List<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,List<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,List<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,List<T5>> ts5)`

Creates a lazy `For`-comprehension over 5 Lists.

`static <T1,
T2,
T3,
T4,
T5,
T6>
API.ForLazy6List<T1,T2,T3,T4,T5,T6>`
`For(@NonNull List<T1> ts1,
 @NonNull Function1<? super T1,List<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,List<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,List<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,List<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,List<T6>> ts6)`

Creates a lazy `For`-comprehension over 6 Lists.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.ForLazy7List<T1,T2,T3,T4,T5,T6,T7>`
`For(@NonNull List<T1> ts1,
 @NonNull Function1<? super T1,List<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,List<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,List<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,List<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,List<T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,List<T7>> ts7)`

Creates a lazy `For`-comprehension over 7 Lists.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.ForLazy8List<T1,T2,T3,T4,T5,T6,T7,T8>`
`For(@NonNull List<T1> ts1,
 @NonNull Function1<? super T1,List<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,List<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,List<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,List<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,List<T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,List<T7>> ts7,
 @NonNull Function7<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,List<T8>> ts8)`

Creates a lazy `For`-comprehension over 8 Lists.

`static <T1,
T2> API.For2List<T1,T2>`
`For(@NonNull List<T1> ts1,
 @NonNull List<T2> ts2)`

Creates a `For`-comprehension of two Lists.

`static <T1,
T2,
T3>
API.For3List<T1,T2,T3>`
`For(@NonNull List<T1> ts1,
 @NonNull List<T2> ts2,
 @NonNull List<T3> ts3)`

Creates a `For`-comprehension of three Lists.

`static <T1,
T2,
T3,
T4>
API.For4List<T1,T2,T3,T4>`
`For(@NonNull List<T1> ts1,
 @NonNull List<T2> ts2,
 @NonNull List<T3> ts3,
 @NonNull List<T4> ts4)`

Creates a `For`-comprehension of 4 Lists.

`static <T1,
T2,
T3,
T4,
T5>
API.For5List<T1,T2,T3,T4,T5>`
`For(@NonNull List<T1> ts1,
 @NonNull List<T2> ts2,
 @NonNull List<T3> ts3,
 @NonNull List<T4> ts4,
 @NonNull List<T5> ts5)`

Creates a `For`-comprehension of 5 Lists.

`static <T1,
T2,
T3,
T4,
T5,
T6>
API.For6List<T1,T2,T3,T4,T5,T6>`
`For(@NonNull List<T1> ts1,
 @NonNull List<T2> ts2,
 @NonNull List<T3> ts3,
 @NonNull List<T4> ts4,
 @NonNull List<T5> ts5,
 @NonNull List<T6> ts6)`

Creates a `For`-comprehension of 6 Lists.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.For7List<T1,T2,T3,T4,T5,T6,T7>`
`For(@NonNull List<T1> ts1,
 @NonNull List<T2> ts2,
 @NonNull List<T3> ts3,
 @NonNull List<T4> ts4,
 @NonNull List<T5> ts5,
 @NonNull List<T6> ts6,
 @NonNull List<T7> ts7)`

Creates a `For`-comprehension of 7 Lists.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.For8List<T1,T2,T3,T4,T5,T6,T7,T8>`
`For(@NonNull List<T1> ts1,
 @NonNull List<T2> ts2,
 @NonNull List<T3> ts3,
 @NonNull List<T4> ts4,
 @NonNull List<T5> ts5,
 @NonNull List<T6> ts6,
 @NonNull List<T7> ts7,
 @NonNull List<T8> ts8)`

Creates a `For`-comprehension of 8 Lists.

`static <T1> API.For1Future<T1>`
`For(@NonNull Future<T1> ts1)`

Creates a `For`-comprehension of one Future.

`static <T1,
T2> API.ForLazy2Future<T1,T2>`
`For(@NonNull Future<T1> ts1,
 @NonNull Function1<? super T1,Future<T2>> ts2)`

Creates a lazy `For`-comprehension over two Futures.

`static <T1,
T2,
T3>
API.ForLazy3Future<T1,T2,T3>`
`For(@NonNull Future<T1> ts1,
 @NonNull Function1<? super T1,Future<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Future<T3>> ts3)`

Creates a lazy `For`-comprehension over three Futures.

`static <T1,
T2,
T3,
T4>
API.ForLazy4Future<T1,T2,T3,T4>`
`For(@NonNull Future<T1> ts1,
 @NonNull Function1<? super T1,Future<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Future<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Future<T4>> ts4)`

Creates a lazy `For`-comprehension over 4 Futures.

`static <T1,
T2,
T3,
T4,
T5>
API.ForLazy5Future<T1,T2,T3,T4,T5>`
`For(@NonNull Future<T1> ts1,
 @NonNull Function1<? super T1,Future<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Future<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Future<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Future<T5>> ts5)`

Creates a lazy `For`-comprehension over 5 Futures.

`static <T1,
T2,
T3,
T4,
T5,
T6>
API.ForLazy6Future<T1,T2,T3,T4,T5,T6>`
`For(@NonNull Future<T1> ts1,
 @NonNull Function1<? super T1,Future<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Future<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Future<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Future<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Future<T6>> ts6)`

Creates a lazy `For`-comprehension over 6 Futures.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.ForLazy7Future<T1,T2,T3,T4,T5,T6,T7>`
`For(@NonNull Future<T1> ts1,
 @NonNull Function1<? super T1,Future<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Future<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Future<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Future<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Future<T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Future<T7>> ts7)`

Creates a lazy `For`-comprehension over 7 Futures.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.ForLazy8Future<T1,T2,T3,T4,T5,T6,T7,T8>`
`For(@NonNull Future<T1> ts1,
 @NonNull Function1<? super T1,Future<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Future<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Future<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Future<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Future<T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Future<T7>> ts7,
 @NonNull Function7<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,Future<T8>> ts8)`

Creates a lazy `For`-comprehension over 8 Futures.

`static <T1,
T2> API.For2Future<T1,T2>`
`For(@NonNull Future<T1> ts1,
 @NonNull Future<T2> ts2)`

Creates a `For`-comprehension of two Futures.

`static <T1,
T2,
T3>
API.For3Future<T1,T2,T3>`
`For(@NonNull Future<T1> ts1,
 @NonNull Future<T2> ts2,
 @NonNull Future<T3> ts3)`

Creates a `For`-comprehension of three Futures.

`static <T1,
T2,
T3,
T4>
API.For4Future<T1,T2,T3,T4>`
`For(@NonNull Future<T1> ts1,
 @NonNull Future<T2> ts2,
 @NonNull Future<T3> ts3,
 @NonNull Future<T4> ts4)`

Creates a `For`-comprehension of 4 Futures.

`static <T1,
T2,
T3,
T4,
T5>
API.For5Future<T1,T2,T3,T4,T5>`
`For(@NonNull Future<T1> ts1,
 @NonNull Future<T2> ts2,
 @NonNull Future<T3> ts3,
 @NonNull Future<T4> ts4,
 @NonNull Future<T5> ts5)`

Creates a `For`-comprehension of 5 Futures.

`static <T1,
T2,
T3,
T4,
T5,
T6>
API.For6Future<T1,T2,T3,T4,T5,T6>`
`For(@NonNull Future<T1> ts1,
 @NonNull Future<T2> ts2,
 @NonNull Future<T3> ts3,
 @NonNull Future<T4> ts4,
 @NonNull Future<T5> ts5,
 @NonNull Future<T6> ts6)`

Creates a `For`-comprehension of 6 Futures.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.For7Future<T1,T2,T3,T4,T5,T6,T7>`
`For(@NonNull Future<T1> ts1,
 @NonNull Future<T2> ts2,
 @NonNull Future<T3> ts3,
 @NonNull Future<T4> ts4,
 @NonNull Future<T5> ts5,
 @NonNull Future<T6> ts6,
 @NonNull Future<T7> ts7)`

Creates a `For`-comprehension of 7 Futures.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.For8Future<T1,T2,T3,T4,T5,T6,T7,T8>`
`For(@NonNull Future<T1> ts1,
 @NonNull Future<T2> ts2,
 @NonNull Future<T3> ts3,
 @NonNull Future<T4> ts4,
 @NonNull Future<T5> ts5,
 @NonNull Future<T6> ts6,
 @NonNull Future<T7> ts7,
 @NonNull Future<T8> ts8)`

Creates a `For`-comprehension of 8 Futures.

`static <L,
T1> API.For1Either<L,T1>`
`For(@NonNull Either<L,T1> ts1)`

Creates a `For`-comprehension of one Either.

`static <L,
T1,
T2>
API.ForLazy2Either<L,T1,T2>`
`For(@NonNull Either<L,T1> ts1,
 @NonNull Function1<? super T1,Either<L,T2>> ts2)`

Creates a lazy `For`-comprehension over two Eithers.

`static <L,
T1,
T2,
T3>
API.ForLazy3Either<L,T1,T2,T3>`
`For(@NonNull Either<L,T1> ts1,
 @NonNull Function1<? super T1,Either<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Either<L,T3>> ts3)`

Creates a lazy `For`-comprehension over three Eithers.

`static <L,
T1,
T2,
T3,
T4>
API.ForLazy4Either<L,T1,T2,T3,T4>`
`For(@NonNull Either<L,T1> ts1,
 @NonNull Function1<? super T1,Either<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Either<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Either<L,T4>> ts4)`

Creates a lazy `For`-comprehension over 4 Eithers.

`static <L,
T1,
T2,
T3,
T4,
T5>
API.ForLazy5Either<L,T1,T2,T3,T4,T5>`
`For(@NonNull Either<L,T1> ts1,
 @NonNull Function1<? super T1,Either<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Either<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Either<L,T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Either<L,T5>> ts5)`

Creates a lazy `For`-comprehension over 5 Eithers.

`static <L,
T1,
T2,
T3,
T4,
T5,
T6>
API.ForLazy6Either<L,T1,T2,T3,T4,T5,T6>`
`For(@NonNull Either<L,T1> ts1,
 @NonNull Function1<? super T1,Either<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Either<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Either<L,T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Either<L,T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Either<L,T6>> ts6)`

Creates a lazy `For`-comprehension over 6 Eithers.

`static <L,
T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.ForLazy7Either<L,T1,T2,T3,T4,T5,T6,T7>`
`For(@NonNull Either<L,T1> ts1,
 @NonNull Function1<? super T1,Either<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Either<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Either<L,T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Either<L,T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Either<L,T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Either<L,T7>> ts7)`

Creates a lazy `For`-comprehension over 7 Eithers.

`static <L,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.ForLazy8Either<L,T1,T2,T3,T4,T5,T6,T7,T8>`
`For(@NonNull Either<L,T1> ts1,
 @NonNull Function1<? super T1,Either<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Either<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Either<L,T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Either<L,T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Either<L,T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Either<L,T7>> ts7,
 @NonNull Function7<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,Either<L,T8>> ts8)`

Creates a lazy `For`-comprehension over 8 Eithers.

`static <L,
T1,
T2>
API.For2Either<L,T1,T2>`
`For(@NonNull Either<L,T1> ts1,
 @NonNull Either<L,T2> ts2)`

Creates a `For`-comprehension of two Eithers.

`static <L,
T1,
T2,
T3>
API.For3Either<L,T1,T2,T3>`
`For(@NonNull Either<L,T1> ts1,
 @NonNull Either<L,T2> ts2,
 @NonNull Either<L,T3> ts3)`

Creates a `For`-comprehension of three Eithers.

`static <L,
T1,
T2,
T3,
T4>
API.For4Either<L,T1,T2,T3,T4>`
`For(@NonNull Either<L,T1> ts1,
 @NonNull Either<L,T2> ts2,
 @NonNull Either<L,T3> ts3,
 @NonNull Either<L,T4> ts4)`

Creates a `For`-comprehension of 4 Eithers.

`static <L,
T1,
T2,
T3,
T4,
T5>
API.For5Either<L,T1,T2,T3,T4,T5>`
`For(@NonNull Either<L,T1> ts1,
 @NonNull Either<L,T2> ts2,
 @NonNull Either<L,T3> ts3,
 @NonNull Either<L,T4> ts4,
 @NonNull Either<L,T5> ts5)`

Creates a `For`-comprehension of 5 Eithers.

`static <L,
T1,
T2,
T3,
T4,
T5,
T6>
API.For6Either<L,T1,T2,T3,T4,T5,T6>`
`For(@NonNull Either<L,T1> ts1,
 @NonNull Either<L,T2> ts2,
 @NonNull Either<L,T3> ts3,
 @NonNull Either<L,T4> ts4,
 @NonNull Either<L,T5> ts5,
 @NonNull Either<L,T6> ts6)`

Creates a `For`-comprehension of 6 Eithers.

`static <L,
T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.For7Either<L,T1,T2,T3,T4,T5,T6,T7>`
`For(@NonNull Either<L,T1> ts1,
 @NonNull Either<L,T2> ts2,
 @NonNull Either<L,T3> ts3,
 @NonNull Either<L,T4> ts4,
 @NonNull Either<L,T5> ts5,
 @NonNull Either<L,T6> ts6,
 @NonNull Either<L,T7> ts7)`

Creates a `For`-comprehension of 7 Eithers.

`static <L,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.For8Either<L,T1,T2,T3,T4,T5,T6,T7,T8>`
`For(@NonNull Either<L,T1> ts1,
 @NonNull Either<L,T2> ts2,
 @NonNull Either<L,T3> ts3,
 @NonNull Either<L,T4> ts4,
 @NonNull Either<L,T5> ts5,
 @NonNull Either<L,T6> ts6,
 @NonNull Either<L,T7> ts7,
 @NonNull Either<L,T8> ts8)`

Creates a `For`-comprehension of 8 Eithers.

`static <T1> API.For1Option<T1>`
`For(@NonNull Option<T1> ts1)`

Creates a `For`-comprehension of one Option.

`static <T1,
T2> API.ForLazy2Option<T1,T2>`
`For(@NonNull Option<T1> ts1,
 @NonNull Function1<? super T1,Option<T2>> ts2)`

Creates a lazy `For`-comprehension over two Options.

`static <T1,
T2,
T3>
API.ForLazy3Option<T1,T2,T3>`
`For(@NonNull Option<T1> ts1,
 @NonNull Function1<? super T1,Option<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Option<T3>> ts3)`

Creates a lazy `For`-comprehension over three Options.

`static <T1,
T2,
T3,
T4>
API.ForLazy4Option<T1,T2,T3,T4>`
`For(@NonNull Option<T1> ts1,
 @NonNull Function1<? super T1,Option<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Option<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Option<T4>> ts4)`

Creates a lazy `For`-comprehension over 4 Options.

`static <T1,
T2,
T3,
T4,
T5>
API.ForLazy5Option<T1,T2,T3,T4,T5>`
`For(@NonNull Option<T1> ts1,
 @NonNull Function1<? super T1,Option<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Option<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Option<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Option<T5>> ts5)`

Creates a lazy `For`-comprehension over 5 Options.

`static <T1,
T2,
T3,
T4,
T5,
T6>
API.ForLazy6Option<T1,T2,T3,T4,T5,T6>`
`For(@NonNull Option<T1> ts1,
 @NonNull Function1<? super T1,Option<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Option<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Option<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Option<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Option<T6>> ts6)`

Creates a lazy `For`-comprehension over 6 Options.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.ForLazy7Option<T1,T2,T3,T4,T5,T6,T7>`
`For(@NonNull Option<T1> ts1,
 @NonNull Function1<? super T1,Option<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Option<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Option<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Option<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Option<T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Option<T7>> ts7)`

Creates a lazy `For`-comprehension over 7 Options.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.ForLazy8Option<T1,T2,T3,T4,T5,T6,T7,T8>`
`For(@NonNull Option<T1> ts1,
 @NonNull Function1<? super T1,Option<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Option<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Option<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Option<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Option<T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Option<T7>> ts7,
 @NonNull Function7<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,Option<T8>> ts8)`

Creates a lazy `For`-comprehension over 8 Options.

`static <T1,
T2> API.For2Option<T1,T2>`
`For(@NonNull Option<T1> ts1,
 @NonNull Option<T2> ts2)`

Creates a `For`-comprehension of two Options.

`static <T1,
T2,
T3>
API.For3Option<T1,T2,T3>`
`For(@NonNull Option<T1> ts1,
 @NonNull Option<T2> ts2,
 @NonNull Option<T3> ts3)`

Creates a `For`-comprehension of three Options.

`static <T1,
T2,
T3,
T4>
API.For4Option<T1,T2,T3,T4>`
`For(@NonNull Option<T1> ts1,
 @NonNull Option<T2> ts2,
 @NonNull Option<T3> ts3,
 @NonNull Option<T4> ts4)`

Creates a `For`-comprehension of 4 Options.

`static <T1,
T2,
T3,
T4,
T5>
API.For5Option<T1,T2,T3,T4,T5>`
`For(@NonNull Option<T1> ts1,
 @NonNull Option<T2> ts2,
 @NonNull Option<T3> ts3,
 @NonNull Option<T4> ts4,
 @NonNull Option<T5> ts5)`

Creates a `For`-comprehension of 5 Options.

`static <T1,
T2,
T3,
T4,
T5,
T6>
API.For6Option<T1,T2,T3,T4,T5,T6>`
`For(@NonNull Option<T1> ts1,
 @NonNull Option<T2> ts2,
 @NonNull Option<T3> ts3,
 @NonNull Option<T4> ts4,
 @NonNull Option<T5> ts5,
 @NonNull Option<T6> ts6)`

Creates a `For`-comprehension of 6 Options.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.For7Option<T1,T2,T3,T4,T5,T6,T7>`
`For(@NonNull Option<T1> ts1,
 @NonNull Option<T2> ts2,
 @NonNull Option<T3> ts3,
 @NonNull Option<T4> ts4,
 @NonNull Option<T5> ts5,
 @NonNull Option<T6> ts6,
 @NonNull Option<T7> ts7)`

Creates a `For`-comprehension of 7 Options.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.For8Option<T1,T2,T3,T4,T5,T6,T7,T8>`
`For(@NonNull Option<T1> ts1,
 @NonNull Option<T2> ts2,
 @NonNull Option<T3> ts3,
 @NonNull Option<T4> ts4,
 @NonNull Option<T5> ts5,
 @NonNull Option<T6> ts6,
 @NonNull Option<T7> ts7,
 @NonNull Option<T8> ts8)`

Creates a `For`-comprehension of 8 Options.

`static <T1> API.For1Try<T1>`
`For(@NonNull Try<T1> ts1)`

Creates a `For`-comprehension of one Try.

`static <T1,
T2> API.ForLazy2Try<T1,T2>`
`For(@NonNull Try<T1> ts1,
 @NonNull Function1<? super T1,Try<T2>> ts2)`

Creates a lazy `For`-comprehension over two Trys.

`static <T1,
T2,
T3>
API.ForLazy3Try<T1,T2,T3>`
`For(@NonNull Try<T1> ts1,
 @NonNull Function1<? super T1,Try<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Try<T3>> ts3)`

Creates a lazy `For`-comprehension over three Trys.

`static <T1,
T2,
T3,
T4>
API.ForLazy4Try<T1,T2,T3,T4>`
`For(@NonNull Try<T1> ts1,
 @NonNull Function1<? super T1,Try<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Try<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Try<T4>> ts4)`

Creates a lazy `For`-comprehension over 4 Trys.

`static <T1,
T2,
T3,
T4,
T5>
API.ForLazy5Try<T1,T2,T3,T4,T5>`
`For(@NonNull Try<T1> ts1,
 @NonNull Function1<? super T1,Try<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Try<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Try<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Try<T5>> ts5)`

Creates a lazy `For`-comprehension over 5 Trys.

`static <T1,
T2,
T3,
T4,
T5,
T6>
API.ForLazy6Try<T1,T2,T3,T4,T5,T6>`
`For(@NonNull Try<T1> ts1,
 @NonNull Function1<? super T1,Try<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Try<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Try<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Try<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Try<T6>> ts6)`

Creates a lazy `For`-comprehension over 6 Trys.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.ForLazy7Try<T1,T2,T3,T4,T5,T6,T7>`
`For(@NonNull Try<T1> ts1,
 @NonNull Function1<? super T1,Try<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Try<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Try<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Try<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Try<T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Try<T7>> ts7)`

Creates a lazy `For`-comprehension over 7 Trys.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.ForLazy8Try<T1,T2,T3,T4,T5,T6,T7,T8>`
`For(@NonNull Try<T1> ts1,
 @NonNull Function1<? super T1,Try<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Try<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Try<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Try<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Try<T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Try<T7>> ts7,
 @NonNull Function7<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,Try<T8>> ts8)`

Creates a lazy `For`-comprehension over 8 Trys.

`static <T1,
T2> API.For2Try<T1,T2>`
`For(@NonNull Try<T1> ts1,
 @NonNull Try<T2> ts2)`

Creates a `For`-comprehension of two Trys.

`static <T1,
T2,
T3>
API.For3Try<T1,T2,T3>`
`For(@NonNull Try<T1> ts1,
 @NonNull Try<T2> ts2,
 @NonNull Try<T3> ts3)`

Creates a `For`-comprehension of three Trys.

`static <T1,
T2,
T3,
T4>
API.For4Try<T1,T2,T3,T4>`
`For(@NonNull Try<T1> ts1,
 @NonNull Try<T2> ts2,
 @NonNull Try<T3> ts3,
 @NonNull Try<T4> ts4)`

Creates a `For`-comprehension of 4 Trys.

`static <T1,
T2,
T3,
T4,
T5>
API.For5Try<T1,T2,T3,T4,T5>`
`For(@NonNull Try<T1> ts1,
 @NonNull Try<T2> ts2,
 @NonNull Try<T3> ts3,
 @NonNull Try<T4> ts4,
 @NonNull Try<T5> ts5)`

Creates a `For`-comprehension of 5 Trys.

`static <T1,
T2,
T3,
T4,
T5,
T6>
API.For6Try<T1,T2,T3,T4,T5,T6>`
`For(@NonNull Try<T1> ts1,
 @NonNull Try<T2> ts2,
 @NonNull Try<T3> ts3,
 @NonNull Try<T4> ts4,
 @NonNull Try<T5> ts5,
 @NonNull Try<T6> ts6)`

Creates a `For`-comprehension of 6 Trys.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.For7Try<T1,T2,T3,T4,T5,T6,T7>`
`For(@NonNull Try<T1> ts1,
 @NonNull Try<T2> ts2,
 @NonNull Try<T3> ts3,
 @NonNull Try<T4> ts4,
 @NonNull Try<T5> ts5,
 @NonNull Try<T6> ts6,
 @NonNull Try<T7> ts7)`

Creates a `For`-comprehension of 7 Trys.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.For8Try<T1,T2,T3,T4,T5,T6,T7,T8>`
`For(@NonNull Try<T1> ts1,
 @NonNull Try<T2> ts2,
 @NonNull Try<T3> ts3,
 @NonNull Try<T4> ts4,
 @NonNull Try<T5> ts5,
 @NonNull Try<T6> ts6,
 @NonNull Try<T7> ts7,
 @NonNull Try<T8> ts8)`

Creates a `For`-comprehension of 8 Trys.

`static <L,
T1> API.For1Validation<L,T1>`
`For(@NonNull Validation<L,T1> ts1)`

Creates a `For`-comprehension of one Validation.

`static <L,
T1,
T2>
API.ForLazy2Validation<L,T1,T2>`
`For(@NonNull Validation<L,T1> ts1,
 @NonNull Function1<? super T1,Validation<L,T2>> ts2)`

Creates a lazy `For`-comprehension over two Validations.

`static <L,
T1,
T2,
T3>
API.ForLazy3Validation<L,T1,T2,T3>`
`For(@NonNull Validation<L,T1> ts1,
 @NonNull Function1<? super T1,Validation<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Validation<L,T3>> ts3)`

Creates a lazy `For`-comprehension over three Validations.

`static <L,
T1,
T2,
T3,
T4>
API.ForLazy4Validation<L,T1,T2,T3,T4>`
`For(@NonNull Validation<L,T1> ts1,
 @NonNull Function1<? super T1,Validation<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Validation<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Validation<L,T4>> ts4)`

Creates a lazy `For`-comprehension over 4 Validations.

`static <L,
T1,
T2,
T3,
T4,
T5>
API.ForLazy5Validation<L,T1,T2,T3,T4,T5>`
`For(@NonNull Validation<L,T1> ts1,
 @NonNull Function1<? super T1,Validation<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Validation<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Validation<L,T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Validation<L,T5>> ts5)`

Creates a lazy `For`-comprehension over 5 Validations.

`static <L,
T1,
T2,
T3,
T4,
T5,
T6>
API.ForLazy6Validation<L,T1,T2,T3,T4,T5,T6>`
`For(@NonNull Validation<L,T1> ts1,
 @NonNull Function1<? super T1,Validation<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Validation<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Validation<L,T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Validation<L,T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Validation<L,T6>> ts6)`

Creates a lazy `For`-comprehension over 6 Validations.

`static <L,
T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.ForLazy7Validation<L,T1,T2,T3,T4,T5,T6,T7>`
`For(@NonNull Validation<L,T1> ts1,
 @NonNull Function1<? super T1,Validation<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Validation<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Validation<L,T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Validation<L,T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Validation<L,T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Validation<L,T7>> ts7)`

Creates a lazy `For`-comprehension over 7 Validations.

`static <L,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.ForLazy8Validation<L,T1,T2,T3,T4,T5,T6,T7,T8>`
`For(@NonNull Validation<L,T1> ts1,
 @NonNull Function1<? super T1,Validation<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Validation<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Validation<L,T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Validation<L,T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Validation<L,T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Validation<L,T7>> ts7,
 @NonNull Function7<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,Validation<L,T8>> ts8)`

Creates a lazy `For`-comprehension over 8 Validations.

`static <L,
T1,
T2>
API.For2Validation<L,T1,T2>`
`For(@NonNull Validation<L,T1> ts1,
 @NonNull Validation<L,T2> ts2)`

Creates a `For`-comprehension of two Validations.

`static <L,
T1,
T2,
T3>
API.For3Validation<L,T1,T2,T3>`
`For(@NonNull Validation<L,T1> ts1,
 @NonNull Validation<L,T2> ts2,
 @NonNull Validation<L,T3> ts3)`

Creates a `For`-comprehension of three Validations.

`static <L,
T1,
T2,
T3,
T4>
API.For4Validation<L,T1,T2,T3,T4>`
`For(@NonNull Validation<L,T1> ts1,
 @NonNull Validation<L,T2> ts2,
 @NonNull Validation<L,T3> ts3,
 @NonNull Validation<L,T4> ts4)`

Creates a `For`-comprehension of 4 Validations.

`static <L,
T1,
T2,
T3,
T4,
T5>
API.For5Validation<L,T1,T2,T3,T4,T5>`
`For(@NonNull Validation<L,T1> ts1,
 @NonNull Validation<L,T2> ts2,
 @NonNull Validation<L,T3> ts3,
 @NonNull Validation<L,T4> ts4,
 @NonNull Validation<L,T5> ts5)`

Creates a `For`-comprehension of 5 Validations.

`static <L,
T1,
T2,
T3,
T4,
T5,
T6>
API.For6Validation<L,T1,T2,T3,T4,T5,T6>`
`For(@NonNull Validation<L,T1> ts1,
 @NonNull Validation<L,T2> ts2,
 @NonNull Validation<L,T3> ts3,
 @NonNull Validation<L,T4> ts4,
 @NonNull Validation<L,T5> ts5,
 @NonNull Validation<L,T6> ts6)`

Creates a `For`-comprehension of 6 Validations.

`static <L,
T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.For7Validation<L,T1,T2,T3,T4,T5,T6,T7>`
`For(@NonNull Validation<L,T1> ts1,
 @NonNull Validation<L,T2> ts2,
 @NonNull Validation<L,T3> ts3,
 @NonNull Validation<L,T4> ts4,
 @NonNull Validation<L,T5> ts5,
 @NonNull Validation<L,T6> ts6,
 @NonNull Validation<L,T7> ts7)`

Creates a `For`-comprehension of 7 Validations.

`static <L,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.For8Validation<L,T1,T2,T3,T4,T5,T6,T7,T8>`
`For(@NonNull Validation<L,T1> ts1,
 @NonNull Validation<L,T2> ts2,
 @NonNull Validation<L,T3> ts3,
 @NonNull Validation<L,T4> ts4,
 @NonNull Validation<L,T5> ts5,
 @NonNull Validation<L,T6> ts6,
 @NonNull Validation<L,T7> ts7,
 @NonNull Validation<L,T8> ts8)`

Creates a `For`-comprehension of 8 Validations.

`static <T1> API.For1<T1>`
`For(@NonNull Iterable<T1> ts1)`

Creates a `For`-comprehension of one Iterable.

`static <T1,
T2> API.For2<T1,T2>`
`For(@NonNull Iterable<T1> ts1,
 @NonNull Iterable<T2> ts2)`

Creates a `For`-comprehension of two Iterables.

`static <T1,
T2,
T3>
API.For3<T1,T2,T3>`
`For(@NonNull Iterable<T1> ts1,
 @NonNull Iterable<T2> ts2,
 @NonNull Iterable<T3> ts3)`

Creates a `For`-comprehension of three Iterables.

`static <T1,
T2,
T3,
T4>
API.For4<T1,T2,T3,T4>`
`For(@NonNull Iterable<T1> ts1,
 @NonNull Iterable<T2> ts2,
 @NonNull Iterable<T3> ts3,
 @NonNull Iterable<T4> ts4)`

Creates a `For`-comprehension of 4 Iterables.

`static <T1,
T2,
T3,
T4,
T5>
API.For5<T1,T2,T3,T4,T5>`
`For(@NonNull Iterable<T1> ts1,
 @NonNull Iterable<T2> ts2,
 @NonNull Iterable<T3> ts3,
 @NonNull Iterable<T4> ts4,
 @NonNull Iterable<T5> ts5)`

Creates a `For`-comprehension of 5 Iterables.

`static <T1,
T2,
T3,
T4,
T5,
T6>
API.For6<T1,T2,T3,T4,T5,T6>`
`For(@NonNull Iterable<T1> ts1,
 @NonNull Iterable<T2> ts2,
 @NonNull Iterable<T3> ts3,
 @NonNull Iterable<T4> ts4,
 @NonNull Iterable<T5> ts5,
 @NonNull Iterable<T6> ts6)`

Creates a `For`-comprehension of 6 Iterables.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.For7<T1,T2,T3,T4,T5,T6,T7>`
`For(@NonNull Iterable<T1> ts1,
 @NonNull Iterable<T2> ts2,
 @NonNull Iterable<T3> ts3,
 @NonNull Iterable<T4> ts4,
 @NonNull Iterable<T5> ts5,
 @NonNull Iterable<T6> ts6,
 @NonNull Iterable<T7> ts7)`

Creates a `For`-comprehension of 7 Iterables.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.For8<T1,T2,T3,T4,T5,T6,T7,T8>`
`For(@NonNull Iterable<T1> ts1,
 @NonNull Iterable<T2> ts2,
 @NonNull Iterable<T3> ts3,
 @NonNull Iterable<T4> ts4,
 @NonNull Iterable<T5> ts5,
 @NonNull Iterable<T6> ts6,
 @NonNull Iterable<T7> ts7,
 @NonNull Iterable<T8> ts8)`

Creates a `For`-comprehension of 8 Iterables.

`static <T,
U> Iterator<U>`
`For(Iterable<T> ts,
 Function<? super T,? extends Iterable<U>> f)`

A shortcut for `Iterator.ofAll(ts).flatMap(f)` which allows us to write real for-comprehensions using
 `For(...).yield(...)`.

`static <R> Function0<R>`
`Function(Function0<R> methodReference)`

Alias for `Function0.of(Function0)`

`static <T1,
R> Function1<T1,R>`
`Function(Function1<T1,R> methodReference)`

Alias for `Function1.of(Function1)`

`static <T1,
T2,
R>
Function2<T1,T2,R>`
`Function(Function2<T1,T2,R> methodReference)`

Alias for `Function2.of(Function2)`

`static <T1,
T2,
T3,
R>
Function3<T1,T2,T3,R>`
`Function(Function3<T1,T2,T3,R> methodReference)`

Alias for `Function3.of(Function3)`

`static <T1,
T2,
T3,
T4,
R>
Function4<T1,T2,T3,T4,R>`
`Function(Function4<T1,T2,T3,T4,R> methodReference)`

Alias for `Function4.of(Function4)`

`static <T1,
T2,
T3,
T4,
T5,
R>
Function5<T1,T2,T3,T4,T5,R>`
`Function(Function5<T1,T2,T3,T4,T5,R> methodReference)`

Alias for `Function5.of(Function5)`

`static <T1,
T2,
T3,
T4,
T5,
T6,
R>
Function6<T1,T2,T3,T4,T5,T6,R>`
`Function(Function6<T1,T2,T3,T4,T5,T6,R> methodReference)`

Alias for `Function6.of(Function6)`

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
R>
Function7<T1,T2,T3,T4,T5,T6,T7,R>`
`Function(Function7<T1,T2,T3,T4,T5,T6,T7,R> methodReference)`

Alias for `Function7.of(Function7)`

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8,
R>
Function8<T1,T2,T3,T4,T5,T6,T7,T8,R>`
`Function(Function8<T1,T2,T3,T4,T5,T6,T7,T8,R> methodReference)`

Alias for `Function8.of(Function8)`

`static <T> Future<T>`
`Future(CheckedFunction0<? extends T> computation)`

Alias for `Future.of(CheckedFunction0)`

`static <T> Future<T>`
`Future(Executor executorService,
 CheckedFunction0<? extends T> computation)`

Alias for `Future.of(Executor, CheckedFunction0)`

`static <T> Future<T>`
`Future(Executor executorService,
 T result)`

Alias for `Future.successful(Executor, Object)`

`static <T> Future<T>`
`Future(T result)`

Alias for `Future.successful(Object)`

`static <T> IndexedSeq<T>`
`IndexedSeq()`

Alias for `Vector.empty()`

`static <T> IndexedSeq<T>`
`IndexedSeq(T element)`

Alias for `Vector.of(Object)`

`static <T> IndexedSeq<T>`
`IndexedSeq(T @NonNull ... elements)`

Alias for `Vector.of(Object...)`

`static <E,
T> Validation.Invalid<E,T>`
`Invalid(E error)`

Alias for `Validation.invalid(Object)`

`static <T> Lazy<T>`
`Lazy(@NonNull Supplier<? extends T> supplier)`

Alias for `Lazy.of(Supplier)`

`static <L,
R> Either.Left<L,R>`
`Left(L left)`

Alias for `Either.left(Object)`

`static <K,
V> Map<K,V>`
`LinkedMap()`

Alias for `LinkedHashMap.empty()`

`static <K,
V> Map<K,V>`
`LinkedMap(Tuple2<? extends K,? extends V> @NonNull ... entries)`

Deprecated.
Will be removed in a future version.

`static <K,
V> Map<K,V>`
`LinkedMap(K k1,
 V v1)`

Alias for `LinkedHashMap.of(Object, Object)`

`static <K,
V> Map<K,V>`
`LinkedMap(K k1,
 V v1,
 K k2,
 V v2)`

Alias for `LinkedHashMap.of(Object, Object, Object, Object)`

`static <K,
V> Map<K,V>`
`LinkedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3)`

Alias for `LinkedHashMap.of(Object, Object, Object, Object, Object, Object)`

`static <K,
V> Map<K,V>`
`LinkedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4)`

Alias for `LinkedHashMap.of(Object, Object, Object, Object, Object, Object, Object, Object)`

`static <K,
V> Map<K,V>`
`LinkedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5)`

Alias for `LinkedHashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

`static <K,
V> Map<K,V>`
`LinkedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6)`

Alias for `LinkedHashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

`static <K,
V> Map<K,V>`
`LinkedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7)`

Alias for `LinkedHashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

`static <K,
V> Map<K,V>`
`LinkedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7,
 K k8,
 V v8)`

Alias for `LinkedHashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

`static <K,
V> Map<K,V>`
`LinkedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7,
 K k8,
 V v8,
 K k9,
 V v9)`

Alias for `LinkedHashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

`static <K,
V> Map<K,V>`
`LinkedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7,
 K k8,
 V v8,
 K k9,
 V v9,
 K k10,
 V v10)`

Alias for `LinkedHashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

`static <T> Set<T>`
`LinkedSet()`

Alias for `LinkedHashSet.empty()`

`static <T> Set<T>`
`LinkedSet(T element)`

Alias for `LinkedHashSet.of(Object)`

`static <T> Set<T>`
`LinkedSet(T @NonNull ... elements)`

Alias for `LinkedHashSet.of(Object...)`

`static <T> List<T>`
`List()`

Alias for `List.empty()`

`static <T> List<T>`
`List(T element)`

Alias for `List.of(Object)`

`static <T> List<T>`
`List(T @NonNull ... elements)`

Alias for `List.of(Object...)`

`static <K,
V> Map<K,V>`
`Map()`

Alias for `HashMap.empty()`

`static <K,
V> Map<K,V>`
`Map(Tuple2<? extends K,? extends V> @NonNull ... entries)`

Deprecated.
Will be removed in a future version.

`static <K,
V> Map<K,V>`
`Map(K k1,
 V v1)`

Alias for `HashMap.of(Object, Object)`

`static <K,
V> Map<K,V>`
`Map(K k1,
 V v1,
 K k2,
 V v2)`

Alias for `HashMap.of(Object, Object, Object, Object)`

`static <K,
V> Map<K,V>`
`Map(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3)`

Alias for `HashMap.of(Object, Object, Object, Object, Object, Object)`

`static <K,
V> Map<K,V>`
`Map(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4)`

Alias for `HashMap.of(Object, Object, Object, Object, Object, Object, Object, Object)`

`static <K,
V> Map<K,V>`
`Map(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5)`

Alias for `HashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

`static <K,
V> Map<K,V>`
`Map(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6)`

Alias for `HashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

`static <K,
V> Map<K,V>`
`Map(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7)`

Alias for `HashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

`static <K,
V> Map<K,V>`
`Map(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7,
 K k8,
 V v8)`

Alias for `HashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

`static <K,
V> Map<K,V>`
`Map(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7,
 K k8,
 V v8,
 K k9,
 V v9)`

Alias for `HashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

`static <K,
V> Map<K,V>`
`Map(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7,
 K k8,
 V v8,
 K k9,
 V v9,
 K k10,
 V v10)`

Alias for `HashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

`static <T> API.Match<T>`
`Match(T value)`

Entry point of the match API.

`static <T> Option.None<T>`
`None()`

Alias for `Option.none()`

`static <T> Option<T>`
`Option(T value)`

Alias for `Option.of(Object)`

`static void`
`print(Object obj)`

Shortcut for `System.out.print(obj)`.

`static void`
`printf(String format,
 Object... args)`

Shortcut for `System.out.printf(format, args)`.

`static void`
`println()`

Shortcut for `System.out.println()`.

`static void`
`println(Object obj)`

Shortcut for `System.out.println(obj)`.

`static <T extends Comparable<? super T>>
PriorityQueue<T>`
`PriorityQueue()`

Alias for `PriorityQueue.empty()`

`static <T extends Comparable<? super T>>
PriorityQueue<T>`
`PriorityQueue(@NonNull Comparator<? super T> comparator)`

Alias for `PriorityQueue.empty(Comparator)`

`static <T> PriorityQueue<T>`
`PriorityQueue(@NonNull Comparator<? super T> comparator,
 T @NonNull ... elements)`

Alias for `PriorityQueue.of(Comparator, Object...)`

`static <T> PriorityQueue<T>`
`PriorityQueue(Comparator<? super T> comparator,
 T element)`

Alias for `PriorityQueue.of(Comparator, Object)`

`static <T extends Comparable<? super T>>
PriorityQueue<T>`
`PriorityQueue(T element)`

Alias for `PriorityQueue.of(Comparable)`

`static <T extends Comparable<? super T>>
PriorityQueue<T>`
`PriorityQueue(T @NonNull ... elements)`

Alias for `PriorityQueue.of(Comparable...)`

`static <T> Queue<T>`
`Queue()`

Alias for `Queue.empty()`

`static <T> Queue<T>`
`Queue(T element)`

Alias for `Queue.of(Object)`

`static <T> Queue<T>`
`Queue(T @NonNull ... elements)`

Alias for `Queue.of(Object...)`

`static <L,
R> Either.Right<L,R>`
`Right(R right)`

Alias for `Either.right(Object)`

`static Void`
`run(Runnable unit)`

Runs a `unit` of work and returns `Void`.

`static <T> Seq<T>`
`Seq()`

Alias for `List.empty()`

`static <T> Seq<T>`
`Seq(T element)`

Alias for `List.of(Object)`

`static <T> Seq<T>`
`Seq(T @NonNull ... elements)`

Alias for `List.of(Object...)`

`static <T> Set<T>`
`Set()`

Alias for `HashSet.empty()`

`static <T> Set<T>`
`Set(T element)`

Alias for `HashSet.of(Object)`

`static <T> Set<T>`
`Set(T @NonNull ... elements)`

Alias for `HashSet.of(Object...)`

`static <T> Option.Some<T>`
`Some(T value)`

Alias for `Option.some(Object)`

`static <K extends Comparable<? super K>,
V>
SortedMap<K,V>`
`SortedMap()`

Alias for `TreeMap.empty()`

`static <K extends Comparable<? super K>,
V>
SortedMap<K,V>`
`SortedMap(Tuple2<? extends K,? extends V> @NonNull ... entries)`

Deprecated.
Will be removed in a future version.

`static <K,
V> SortedMap<K,V>`
`SortedMap(@NonNull Comparator<? super K> keyComparator)`

Alias for `TreeMap.empty(Comparator)`

`static <K,
V> SortedMap<K,V>`
`SortedMap(@NonNull Comparator<? super K> keyComparator,
 Tuple2<? extends K,? extends V> @NonNull ... entries)`

Deprecated.
Will be removed in a future version.

`static <K,
V> SortedMap<K,V>`
`SortedMap(@NonNull Comparator<? super K> keyComparator,
 K key,
 V value)`

Alias for `TreeMap.of(Comparator, Object, Object)`

`static <K extends Comparable<? super K>,
V>
SortedMap<K,V>`
`SortedMap(Map<? extends K,? extends V> map)`

Deprecated.
Will be removed in a future version.

`static <K extends Comparable<? super K>,
V>
SortedMap<K,V>`
`SortedMap(K k1,
 V v1)`

Alias for `TreeMap.of(Comparable, Object)`

`static <K extends Comparable<? super K>,
V>
SortedMap<K,V>`
`SortedMap(K k1,
 V v1,
 K k2,
 V v2)`

Alias for `TreeMap.of(Comparable, Object, Comparable, Object)`

`static <K extends Comparable<? super K>,
V>
SortedMap<K,V>`
`SortedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3)`

Alias for `TreeMap.of(Comparable, Object, Comparable, Object, Comparable, Object)`

`static <K extends Comparable<? super K>,
V>
SortedMap<K,V>`
`SortedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4)`

Alias for `TreeMap.of(Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object)`

`static <K extends Comparable<? super K>,
V>
SortedMap<K,V>`
`SortedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5)`

Alias for `TreeMap.of(Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object)`

`static <K extends Comparable<? super K>,
V>
SortedMap<K,V>`
`SortedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6)`

Alias for `TreeMap.of(Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object)`

`static <K extends Comparable<? super K>,
V>
SortedMap<K,V>`
`SortedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7)`

Alias for `TreeMap.of(Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object)`

`static <K extends Comparable<? super K>,
V>
SortedMap<K,V>`
`SortedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7,
 K k8,
 V v8)`

Alias for `TreeMap.of(Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object)`

`static <K extends Comparable<? super K>,
V>
SortedMap<K,V>`
`SortedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7,
 K k8,
 V v8,
 K k9,
 V v9)`

Alias for `TreeMap.of(Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object)`

`static <K extends Comparable<? super K>,
V>
SortedMap<K,V>`
`SortedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7,
 K k8,
 V v8,
 K k9,
 V v9,
 K k10,
 V v10)`

Alias for `TreeMap.of(Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object)`

`static <T extends Comparable<? super T>>
SortedSet<T>`
`SortedSet()`

Alias for `TreeSet.empty()`

`static <T extends Comparable<? super T>>
SortedSet<T>`
`SortedSet(@NonNull Comparator<? super T> comparator)`

Alias for `TreeSet.empty(Comparator)`

`static <T> SortedSet<T>`
`SortedSet(@NonNull Comparator<? super T> comparator,
 T @NonNull ... elements)`

Alias for `TreeSet.of(Comparator, Object...)`

`static <T> SortedSet<T>`
`SortedSet(Comparator<? super T> comparator,
 T element)`

Alias for `TreeSet.of(Comparator, Object)`

`static <T extends Comparable<? super T>>
SortedSet<T>`
`SortedSet(T element)`

Alias for `TreeSet.of(Comparable)`

`static <T extends Comparable<? super T>>
SortedSet<T>`
`SortedSet(T @NonNull ... elements)`

Alias for `TreeSet.of(Comparable...)`

`static <T> Stream<T>`
`Stream()`

Alias for `Stream.empty()`

`static <T> Stream<T>`
`Stream(T element)`

Alias for `Stream.of(Object)`

`static <T> Stream<T>`
`Stream(T @NonNull ... elements)`

Alias for `Stream.of(Object...)`

`static <T> Try.Success<T>`
`Success(T value)`

Alias for `Try.success(Object)`

`static <T> T`
`TODO()`

A temporary replacement for an implementations used during prototyping.

`static <T> T`
`TODO(String msg)`

A temporary replacement for an implementations used during prototyping.

`static <T> Try<T>`
`Try(CheckedFunction0<? extends T> supplier)`

Alias for `Try.of(CheckedFunction0)`

`static Tuple0`
`Tuple()`

Alias for `Tuple.empty()`

`static <T1> Tuple1<T1>`
`Tuple(T1 t1)`

Alias for `Tuple.of(Object)`

 Creates a tuple of one element.

`static <T1,
T2> Tuple2<T1,T2>`
`Tuple(T1 t1,
 T2 t2)`

Alias for `Tuple.of(Object, Object)`

 Creates a tuple of two elements.

`static <T1,
T2,
T3>
Tuple3<T1,T2,T3>`
`Tuple(T1 t1,
 T2 t2,
 T3 t3)`

Alias for `Tuple.of(Object, Object, Object)`

 Creates a tuple of three elements.

`static <T1,
T2,
T3,
T4>
Tuple4<T1,T2,T3,T4>`
`Tuple(T1 t1,
 T2 t2,
 T3 t3,
 T4 t4)`

Alias for `Tuple.of(Object, Object, Object, Object)`

 Creates a tuple of 4 elements.

`static <T1,
T2,
T3,
T4,
T5>
Tuple5<T1,T2,T3,T4,T5>`
`Tuple(T1 t1,
 T2 t2,
 T3 t3,
 T4 t4,
 T5 t5)`

Alias for `Tuple.of(Object, Object, Object, Object, Object)`

 Creates a tuple of 5 elements.

`static <T1,
T2,
T3,
T4,
T5,
T6>
Tuple6<T1,T2,T3,T4,T5,T6>`
`Tuple(T1 t1,
 T2 t2,
 T3 t3,
 T4 t4,
 T5 t5,
 T6 t6)`

Alias for `Tuple.of(Object, Object, Object, Object, Object, Object)`

 Creates a tuple of 6 elements.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
Tuple7<T1,T2,T3,T4,T5,T6,T7>`
`Tuple(T1 t1,
 T2 t2,
 T3 t3,
 T4 t4,
 T5 t5,
 T6 t6,
 T7 t7)`

Alias for `Tuple.of(Object, Object, Object, Object, Object, Object, Object)`

 Creates a tuple of 7 elements.

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
Tuple8<T1,T2,T3,T4,T5,T6,T7,T8>`
`Tuple(T1 t1,
 T2 t2,
 T3 t3,
 T4 t4,
 T5 t5,
 T6 t6,
 T7 t7,
 T8 t8)`

Alias for `Tuple.of(Object, Object, Object, Object, Object, Object, Object, Object)`

 Creates a tuple of 8 elements.

`static <R> Function0<R>`
`unchecked(CheckedFunction0<R> f)`

Alias for `CheckedFunction0.unchecked()`

`static <T1,
R> Function1<T1,R>`
`unchecked(CheckedFunction1<T1,R> f)`

Alias for `CheckedFunction1.unchecked()`

`static <T1,
T2,
R>
Function2<T1,T2,R>`
`unchecked(CheckedFunction2<T1,T2,R> f)`

Alias for `CheckedFunction2.unchecked()`

`static <T1,
T2,
T3,
R>
Function3<T1,T2,T3,R>`
`unchecked(CheckedFunction3<T1,T2,T3,R> f)`

Alias for `CheckedFunction3.unchecked()`

`static <T1,
T2,
T3,
T4,
R>
Function4<T1,T2,T3,T4,R>`
`unchecked(CheckedFunction4<T1,T2,T3,T4,R> f)`

Alias for `CheckedFunction4.unchecked()`

`static <T1,
T2,
T3,
T4,
T5,
R>
Function5<T1,T2,T3,T4,T5,R>`
`unchecked(CheckedFunction5<T1,T2,T3,T4,T5,R> f)`

Alias for `CheckedFunction5.unchecked()`

`static <T1,
T2,
T3,
T4,
T5,
T6,
R>
Function6<T1,T2,T3,T4,T5,T6,R>`
`unchecked(CheckedFunction6<T1,T2,T3,T4,T5,T6,R> f)`

Alias for `CheckedFunction6.unchecked()`

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
R>
Function7<T1,T2,T3,T4,T5,T6,T7,R>`
`unchecked(CheckedFunction7<T1,T2,T3,T4,T5,T6,T7,R> f)`

Alias for `CheckedFunction7.unchecked()`

`static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8,
R>
Function8<T1,T2,T3,T4,T5,T6,T7,T8,R>`
`unchecked(CheckedFunction8<T1,T2,T3,T4,T5,T6,T7,T8,R> f)`

Alias for `CheckedFunction8.unchecked()`

`static <E,
T> Validation.Valid<E,T>`
`Valid(T value)`

Alias for `Validation.valid(Object)`

`static <T> Vector<T>`
`Vector()`

Alias for `Vector.empty()`

`static <T> Vector<T>`
`Vector(T element)`

Alias for `Vector.of(Object)`

`static <T> Vector<T>`
`Vector(T @NonNull ... elements)`

Alias for `Vector.of(Object...)`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### TODO

public static <T> T TODO()
A temporary replacement for an implementations used during prototyping.
 

 Example:

 

```

 public HttpResponse getResponse(HttpRequest request) {
     return TODO();
 }

 final HttpResponse response = getHttpResponse(TODO());
 
```

Type Parameters:
`T` - The result type of the missing implementation.
Returns:
Nothing - this methods always throws.
Throws:
`NotImplementedError` - when this methods is called
See Also:

    - `NotImplementedError()`

  - 

### TODO

public static <T> T TODO(String msg)
A temporary replacement for an implementations used during prototyping.
 

 Example:

 

```

 public HttpResponse getResponse(HttpRequest request) {
     return TODO("fake response");
 }

 final HttpResponse response = getHttpResponse(TODO("fake request"));
 
```

Type Parameters:
`T` - The result type of the missing implementation.
Parameters:
`msg` - An error message
Returns:
Nothing - this methods always throws.
Throws:
`NotImplementedError` - when this methods is called
See Also:

    - `NotImplementedError(String)`

  - 

### print

public static void print(Object obj)
Shortcut for `System.out.print(obj)`. See `PrintStream.print(Object)`.

Parameters:
`obj` - The `>Object` to be printed

  - 

### printf

@GwtIncompatible
public static void printf(String format,
 Object... args)
Shortcut for `System.out.printf(format, args)`. See `PrintStream.printf(String, Object...)`.

Parameters:
`format` - A format string as described in `Formatter`.
`args` - Arguments referenced by the format specifiers

  - 

### println

public static void println(Object obj)
Shortcut for `System.out.println(obj)`. See `PrintStream.println(Object)`.

Parameters:
`obj` - The `Object` to be printed

  - 

### println

public static void println()
Shortcut for `System.out.println()`. See `PrintStream.println()`.

  - 

### Function

public static <R> Function0<R> Function(Function0<R> methodReference)
Alias for `Function0.of(Function0)`

Type Parameters:
`R` - return type
Parameters:
`methodReference` - A method reference
Returns:
A `Function0`

  - 

### Function

public static <T1,
R> Function1<T1,R> Function(Function1<T1,R> methodReference)
Alias for `Function1.of(Function1)`

Type Parameters:
`T1` - type of the 1st argument
`R` - return type
Parameters:
`methodReference` - A method reference
Returns:
A `Function1`

  - 

### Function

public static <T1,
T2,
R> Function2<T1,T2,R> Function(Function2<T1,T2,R> methodReference)
Alias for `Function2.of(Function2)`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`R` - return type
Parameters:
`methodReference` - A method reference
Returns:
A `Function2`

  - 

### Function

public static <T1,
T2,
T3,
R> Function3<T1,T2,T3,R> Function(Function3<T1,T2,T3,R> methodReference)
Alias for `Function3.of(Function3)`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`T3` - type of the 3rd argument
`R` - return type
Parameters:
`methodReference` - A method reference
Returns:
A `Function3`

  - 

### Function

public static <T1,
T2,
T3,
T4,
R>
Function4<T1,T2,T3,T4,R> Function(Function4<T1,T2,T3,T4,R> methodReference)
Alias for `Function4.of(Function4)`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`T3` - type of the 3rd argument
`T4` - type of the 4th argument
`R` - return type
Parameters:
`methodReference` - A method reference
Returns:
A `Function4`

  - 

### Function

public static <T1,
T2,
T3,
T4,
T5,
R>
Function5<T1,T2,T3,T4,T5,R> Function(Function5<T1,T2,T3,T4,T5,R> methodReference)
Alias for `Function5.of(Function5)`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`T3` - type of the 3rd argument
`T4` - type of the 4th argument
`T5` - type of the 5th argument
`R` - return type
Parameters:
`methodReference` - A method reference
Returns:
A `Function5`

  - 

### Function

public static <T1,
T2,
T3,
T4,
T5,
T6,
R>
Function6<T1,T2,T3,T4,T5,T6,R> Function(Function6<T1,T2,T3,T4,T5,T6,R> methodReference)
Alias for `Function6.of(Function6)`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`T3` - type of the 3rd argument
`T4` - type of the 4th argument
`T5` - type of the 5th argument
`T6` - type of the 6th argument
`R` - return type
Parameters:
`methodReference` - A method reference
Returns:
A `Function6`

  - 

### Function

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
R>
Function7<T1,T2,T3,T4,T5,T6,T7,R> Function(Function7<T1,T2,T3,T4,T5,T6,T7,R> methodReference)
Alias for `Function7.of(Function7)`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`T3` - type of the 3rd argument
`T4` - type of the 4th argument
`T5` - type of the 5th argument
`T6` - type of the 6th argument
`T7` - type of the 7th argument
`R` - return type
Parameters:
`methodReference` - A method reference
Returns:
A `Function7`

  - 

### Function

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8,
R>
Function8<T1,T2,T3,T4,T5,T6,T7,T8,R> Function(Function8<T1,T2,T3,T4,T5,T6,T7,T8,R> methodReference)
Alias for `Function8.of(Function8)`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`T3` - type of the 3rd argument
`T4` - type of the 4th argument
`T5` - type of the 5th argument
`T6` - type of the 6th argument
`T7` - type of the 7th argument
`T8` - type of the 8th argument
`R` - return type
Parameters:
`methodReference` - A method reference
Returns:
A `Function8`

  - 

### CheckedFunction

public static <R> CheckedFunction0<R> CheckedFunction(CheckedFunction0<R> methodReference)
Alias for `CheckedFunction0.of(CheckedFunction0)`

Type Parameters:
`R` - return type
Parameters:
`methodReference` - A method reference
Returns:
A `CheckedFunction0`

  - 

### CheckedFunction

public static <T1,
R> CheckedFunction1<T1,R> CheckedFunction(CheckedFunction1<T1,R> methodReference)
Alias for `CheckedFunction1.of(CheckedFunction1)`

Type Parameters:
`T1` - type of the 1st argument
`R` - return type
Parameters:
`methodReference` - A method reference
Returns:
A `CheckedFunction1`

  - 

### CheckedFunction

public static <T1,
T2,
R> CheckedFunction2<T1,T2,R> CheckedFunction(CheckedFunction2<T1,T2,R> methodReference)
Alias for `CheckedFunction2.of(CheckedFunction2)`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`R` - return type
Parameters:
`methodReference` - A method reference
Returns:
A `CheckedFunction2`

  - 

### CheckedFunction

public static <T1,
T2,
T3,
R>
CheckedFunction3<T1,T2,T3,R> CheckedFunction(CheckedFunction3<T1,T2,T3,R> methodReference)
Alias for `CheckedFunction3.of(CheckedFunction3)`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`T3` - type of the 3rd argument
`R` - return type
Parameters:
`methodReference` - A method reference
Returns:
A `CheckedFunction3`

  - 

### CheckedFunction

public static <T1,
T2,
T3,
T4,
R>
CheckedFunction4<T1,T2,T3,T4,R> CheckedFunction(CheckedFunction4<T1,T2,T3,T4,R> methodReference)
Alias for `CheckedFunction4.of(CheckedFunction4)`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`T3` - type of the 3rd argument
`T4` - type of the 4th argument
`R` - return type
Parameters:
`methodReference` - A method reference
Returns:
A `CheckedFunction4`

  - 

### CheckedFunction

public static <T1,
T2,
T3,
T4,
T5,
R>
CheckedFunction5<T1,T2,T3,T4,T5,R> CheckedFunction(CheckedFunction5<T1,T2,T3,T4,T5,R> methodReference)
Alias for `CheckedFunction5.of(CheckedFunction5)`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`T3` - type of the 3rd argument
`T4` - type of the 4th argument
`T5` - type of the 5th argument
`R` - return type
Parameters:
`methodReference` - A method reference
Returns:
A `CheckedFunction5`

  - 

### CheckedFunction

public static <T1,
T2,
T3,
T4,
T5,
T6,
R>
CheckedFunction6<T1,T2,T3,T4,T5,T6,R> CheckedFunction(CheckedFunction6<T1,T2,T3,T4,T5,T6,R> methodReference)
Alias for `CheckedFunction6.of(CheckedFunction6)`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`T3` - type of the 3rd argument
`T4` - type of the 4th argument
`T5` - type of the 5th argument
`T6` - type of the 6th argument
`R` - return type
Parameters:
`methodReference` - A method reference
Returns:
A `CheckedFunction6`

  - 

### CheckedFunction

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
R>
CheckedFunction7<T1,T2,T3,T4,T5,T6,T7,R> CheckedFunction(CheckedFunction7<T1,T2,T3,T4,T5,T6,T7,R> methodReference)
Alias for `CheckedFunction7.of(CheckedFunction7)`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`T3` - type of the 3rd argument
`T4` - type of the 4th argument
`T5` - type of the 5th argument
`T6` - type of the 6th argument
`T7` - type of the 7th argument
`R` - return type
Parameters:
`methodReference` - A method reference
Returns:
A `CheckedFunction7`

  - 

### CheckedFunction

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8,
R>
CheckedFunction8<T1,T2,T3,T4,T5,T6,T7,T8,R> CheckedFunction(CheckedFunction8<T1,T2,T3,T4,T5,T6,T7,T8,R> methodReference)
Alias for `CheckedFunction8.of(CheckedFunction8)`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`T3` - type of the 3rd argument
`T4` - type of the 4th argument
`T5` - type of the 5th argument
`T6` - type of the 6th argument
`T7` - type of the 7th argument
`T8` - type of the 8th argument
`R` - return type
Parameters:
`methodReference` - A method reference
Returns:
A `CheckedFunction8`

  - 

### unchecked

public static <R> Function0<R> unchecked(CheckedFunction0<R> f)
Alias for `CheckedFunction0.unchecked()`

Type Parameters:
`R` - return type
Parameters:
`f` - A method reference
Returns:
An unchecked wrapper of supplied `CheckedFunction0`

  - 

### unchecked

public static <T1,
R> Function1<T1,R> unchecked(CheckedFunction1<T1,R> f)
Alias for `CheckedFunction1.unchecked()`

Type Parameters:
`T1` - type of the 1st argument
`R` - return type
Parameters:
`f` - A method reference
Returns:
An unchecked wrapper of supplied `CheckedFunction1`

  - 

### unchecked

public static <T1,
T2,
R> Function2<T1,T2,R> unchecked(CheckedFunction2<T1,T2,R> f)
Alias for `CheckedFunction2.unchecked()`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`R` - return type
Parameters:
`f` - A method reference
Returns:
An unchecked wrapper of supplied `CheckedFunction2`

  - 

### unchecked

public static <T1,
T2,
T3,
R> Function3<T1,T2,T3,R> unchecked(CheckedFunction3<T1,T2,T3,R> f)
Alias for `CheckedFunction3.unchecked()`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`T3` - type of the 3rd argument
`R` - return type
Parameters:
`f` - A method reference
Returns:
An unchecked wrapper of supplied `CheckedFunction3`

  - 

### unchecked

public static <T1,
T2,
T3,
T4,
R>
Function4<T1,T2,T3,T4,R> unchecked(CheckedFunction4<T1,T2,T3,T4,R> f)
Alias for `CheckedFunction4.unchecked()`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`T3` - type of the 3rd argument
`T4` - type of the 4th argument
`R` - return type
Parameters:
`f` - A method reference
Returns:
An unchecked wrapper of supplied `CheckedFunction4`

  - 

### unchecked

public static <T1,
T2,
T3,
T4,
T5,
R>
Function5<T1,T2,T3,T4,T5,R> unchecked(CheckedFunction5<T1,T2,T3,T4,T5,R> f)
Alias for `CheckedFunction5.unchecked()`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`T3` - type of the 3rd argument
`T4` - type of the 4th argument
`T5` - type of the 5th argument
`R` - return type
Parameters:
`f` - A method reference
Returns:
An unchecked wrapper of supplied `CheckedFunction5`

  - 

### unchecked

public static <T1,
T2,
T3,
T4,
T5,
T6,
R>
Function6<T1,T2,T3,T4,T5,T6,R> unchecked(CheckedFunction6<T1,T2,T3,T4,T5,T6,R> f)
Alias for `CheckedFunction6.unchecked()`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`T3` - type of the 3rd argument
`T4` - type of the 4th argument
`T5` - type of the 5th argument
`T6` - type of the 6th argument
`R` - return type
Parameters:
`f` - A method reference
Returns:
An unchecked wrapper of supplied `CheckedFunction6`

  - 

### unchecked

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
R>
Function7<T1,T2,T3,T4,T5,T6,T7,R> unchecked(CheckedFunction7<T1,T2,T3,T4,T5,T6,T7,R> f)
Alias for `CheckedFunction7.unchecked()`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`T3` - type of the 3rd argument
`T4` - type of the 4th argument
`T5` - type of the 5th argument
`T6` - type of the 6th argument
`T7` - type of the 7th argument
`R` - return type
Parameters:
`f` - A method reference
Returns:
An unchecked wrapper of supplied `CheckedFunction7`

  - 

### unchecked

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8,
R>
Function8<T1,T2,T3,T4,T5,T6,T7,T8,R> unchecked(CheckedFunction8<T1,T2,T3,T4,T5,T6,T7,T8,R> f)
Alias for `CheckedFunction8.unchecked()`

Type Parameters:
`T1` - type of the 1st argument
`T2` - type of the 2nd argument
`T3` - type of the 3rd argument
`T4` - type of the 4th argument
`T5` - type of the 5th argument
`T6` - type of the 6th argument
`T7` - type of the 7th argument
`T8` - type of the 8th argument
`R` - return type
Parameters:
`f` - A method reference
Returns:
An unchecked wrapper of supplied `CheckedFunction8`

  - 

### Tuple

public static Tuple0 Tuple()
Alias for `Tuple.empty()`

Returns:
the empty tuple.

  - 

### Tuple

public static <T1> Tuple1<T1> Tuple(T1 t1)
Alias for `Tuple.of(Object)`

 Creates a tuple of one element.

Type Parameters:
`T1` - type of the 1st element
Parameters:
`t1` - the 1st element
Returns:
a tuple of one element.

  - 

### Tuple

public static <T1,
T2> Tuple2<T1,T2> Tuple(T1 t1,
 T2 t2)
Alias for `Tuple.of(Object, Object)`

 Creates a tuple of two elements.

Type Parameters:
`T1` - type of the 1st element
`T2` - type of the 2nd element
Parameters:
`t1` - the 1st element
`t2` - the 2nd element
Returns:
a tuple of two elements.

  - 

### Tuple

public static <T1,
T2,
T3> Tuple3<T1,T2,T3> Tuple(T1 t1,
 T2 t2,
 T3 t3)
Alias for `Tuple.of(Object, Object, Object)`

 Creates a tuple of three elements.

Type Parameters:
`T1` - type of the 1st element
`T2` - type of the 2nd element
`T3` - type of the 3rd element
Parameters:
`t1` - the 1st element
`t2` - the 2nd element
`t3` - the 3rd element
Returns:
a tuple of three elements.

  - 

### Tuple

public static <T1,
T2,
T3,
T4> Tuple4<T1,T2,T3,T4> Tuple(T1 t1,
 T2 t2,
 T3 t3,
 T4 t4)
Alias for `Tuple.of(Object, Object, Object, Object)`

 Creates a tuple of 4 elements.

Type Parameters:
`T1` - type of the 1st element
`T2` - type of the 2nd element
`T3` - type of the 3rd element
`T4` - type of the 4th element
Parameters:
`t1` - the 1st element
`t2` - the 2nd element
`t3` - the 3rd element
`t4` - the 4th element
Returns:
a tuple of 4 elements.

  - 

### Tuple

public static <T1,
T2,
T3,
T4,
T5>
Tuple5<T1,T2,T3,T4,T5> Tuple(T1 t1,
 T2 t2,
 T3 t3,
 T4 t4,
 T5 t5)
Alias for `Tuple.of(Object, Object, Object, Object, Object)`

 Creates a tuple of 5 elements.

Type Parameters:
`T1` - type of the 1st element
`T2` - type of the 2nd element
`T3` - type of the 3rd element
`T4` - type of the 4th element
`T5` - type of the 5th element
Parameters:
`t1` - the 1st element
`t2` - the 2nd element
`t3` - the 3rd element
`t4` - the 4th element
`t5` - the 5th element
Returns:
a tuple of 5 elements.

  - 

### Tuple

public static <T1,
T2,
T3,
T4,
T5,
T6>
Tuple6<T1,T2,T3,T4,T5,T6> Tuple(T1 t1,
 T2 t2,
 T3 t3,
 T4 t4,
 T5 t5,
 T6 t6)
Alias for `Tuple.of(Object, Object, Object, Object, Object, Object)`

 Creates a tuple of 6 elements.

Type Parameters:
`T1` - type of the 1st element
`T2` - type of the 2nd element
`T3` - type of the 3rd element
`T4` - type of the 4th element
`T5` - type of the 5th element
`T6` - type of the 6th element
Parameters:
`t1` - the 1st element
`t2` - the 2nd element
`t3` - the 3rd element
`t4` - the 4th element
`t5` - the 5th element
`t6` - the 6th element
Returns:
a tuple of 6 elements.

  - 

### Tuple

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
Tuple7<T1,T2,T3,T4,T5,T6,T7> Tuple(T1 t1,
 T2 t2,
 T3 t3,
 T4 t4,
 T5 t5,
 T6 t6,
 T7 t7)
Alias for `Tuple.of(Object, Object, Object, Object, Object, Object, Object)`

 Creates a tuple of 7 elements.

Type Parameters:
`T1` - type of the 1st element
`T2` - type of the 2nd element
`T3` - type of the 3rd element
`T4` - type of the 4th element
`T5` - type of the 5th element
`T6` - type of the 6th element
`T7` - type of the 7th element
Parameters:
`t1` - the 1st element
`t2` - the 2nd element
`t3` - the 3rd element
`t4` - the 4th element
`t5` - the 5th element
`t6` - the 6th element
`t7` - the 7th element
Returns:
a tuple of 7 elements.

  - 

### Tuple

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
Tuple8<T1,T2,T3,T4,T5,T6,T7,T8> Tuple(T1 t1,
 T2 t2,
 T3 t3,
 T4 t4,
 T5 t5,
 T6 t6,
 T7 t7,
 T8 t8)
Alias for `Tuple.of(Object, Object, Object, Object, Object, Object, Object, Object)`

 Creates a tuple of 8 elements.

Type Parameters:
`T1` - type of the 1st element
`T2` - type of the 2nd element
`T3` - type of the 3rd element
`T4` - type of the 4th element
`T5` - type of the 5th element
`T6` - type of the 6th element
`T7` - type of the 7th element
`T8` - type of the 8th element
Parameters:
`t1` - the 1st element
`t2` - the 2nd element
`t3` - the 3rd element
`t4` - the 4th element
`t5` - the 5th element
`t6` - the 6th element
`t7` - the 7th element
`t8` - the 8th element
Returns:
a tuple of 8 elements.

  - 

### Right

public static <L,
R> Either.Right<L,R> Right(R right)
Alias for `Either.right(Object)`

Type Parameters:
`L` - Type of left value.
`R` - Type of right value.
Parameters:
`right` - The value.
Returns:
A new `Either.Right` instance.

  - 

### Left

public static <L,
R> Either.Left<L,R> Left(L left)
Alias for `Either.left(Object)`

Type Parameters:
`L` - Type of left value.
`R` - Type of right value.
Parameters:
`left` - The value.
Returns:
A new `Either.Left` instance.

  - 

### Future

public static <T> Future<T> Future(CheckedFunction0<? extends T> computation)
Alias for `Future.of(CheckedFunction0)`

Type Parameters:
`T` - Type of the computation result.
Parameters:
`computation` - A computation.
Returns:
A new `Future` instance.
Throws:
`NullPointerException` - if computation is null.

  - 

### Future

public static <T> Future<T> Future(Executor executorService,
 CheckedFunction0<? extends T> computation)
Alias for `Future.of(Executor, CheckedFunction0)`

Type Parameters:
`T` - Type of the computation result.
Parameters:
`executorService` - An executor service.
`computation` - A computation.
Returns:
A new `Future` instance.
Throws:
`NullPointerException` - if one of executorService or computation is null.

  - 

### Future

public static <T> Future<T> Future(T result)
Alias for `Future.successful(Object)`

Type Parameters:
`T` - The value type of a successful result.
Parameters:
`result` - The result.
Returns:
A succeeded `Future`.

  - 

### Future

public static <T> Future<T> Future(Executor executorService,
 T result)
Alias for `Future.successful(Executor, Object)`

Type Parameters:
`T` - The value type of a successful result.
Parameters:
`executorService` - An `ExecutorService`.
`result` - The result.
Returns:
A succeeded `Future`.
Throws:
`NullPointerException` - if executorService is null

  - 

### Lazy

public static <T> Lazy<T> Lazy(@NonNull Supplier<? extends T> supplier)
Alias for `Lazy.of(Supplier)`

Type Parameters:
`T` - type of the lazy value
Parameters:
`supplier` - A supplier
Returns:
A new instance of `Lazy`

  - 

### Option

public static <T> Option<T> Option(T value)
Alias for `Option.of(Object)`

Type Parameters:
`T` - type of the value
Parameters:
`value` - A value
Returns:
`Option.Some` if value is not `null`, `Option.None` otherwise

  - 

### Some

public static <T> Option.Some<T> Some(T value)
Alias for `Option.some(Object)`

Type Parameters:
`T` - type of the value
Parameters:
`value` - A value
Returns:
`Option.Some`

  - 

### None

public static <T> Option.None<T> None()
Alias for `Option.none()`

Type Parameters:
`T` - component type
Returns:
the singleton instance of `Option.None`

  - 

### Try

public static <T> Try<T> Try(CheckedFunction0<? extends T> supplier)
Alias for `Try.of(CheckedFunction0)`

Type Parameters:
`T` - Component type
Parameters:
`supplier` - A checked supplier
Returns:
`Try.Success` if no exception occurs, otherwise `Try.Failure` if an
 exception occurs calling `supplier.get()`.

  - 

### Success

public static <T> Try.Success<T> Success(T value)
Alias for `Try.success(Object)`

Type Parameters:
`T` - Type of the given `value`.
Parameters:
`value` - A value.
Returns:
A new `Try.Success`.

  - 

### Failure

public static <T> Try.Failure<T> Failure(Throwable exception)
Alias for `Try.failure(Throwable)`

Type Parameters:
`T` - Component type of the `Try`.
Parameters:
`exception` - An exception.
Returns:
A new `Try.Failure`.

  - 

### Valid

public static <E,
T> Validation.Valid<E,T> Valid(T value)
Alias for `Validation.valid(Object)`

Type Parameters:
`E` - type of the error
`T` - type of the given `value`
Parameters:
`value` - A value
Returns:
`Validation.Valid`
Throws:
`NullPointerException` - if value is null

  - 

### Invalid

public static <E,
T> Validation.Invalid<E,T> Invalid(E error)
Alias for `Validation.invalid(Object)`

Type Parameters:
`E` - type of the given `error`
`T` - type of the value
Parameters:
`error` - An error
Returns:
`Validation.Invalid`
Throws:
`NullPointerException` - if error is null

  - 

### CharSeq

public static CharSeq CharSeq(char character)
Alias for `CharSeq.of(char)`

Parameters:
`character` - A character.
Returns:
A new `CharSeq` instance containing the given element

  - 

### CharSeq

public static CharSeq CharSeq(char... characters)
Alias for `CharSeq.of(char...)`

Parameters:
`characters` - Zero or more characters.
Returns:
A new `CharSeq` instance containing the given characters in the same order.
Throws:
`NullPointerException` - if `elements` is null

  - 

### CharSeq

public static CharSeq CharSeq(CharSequence sequence)
Alias for `CharSeq.of(CharSequence)`

Parameters:
`sequence` - `CharSequence` instance.
Returns:
A new `CharSeq` instance

  - 

### PriorityQueue

public static <T extends Comparable<? super T>>
PriorityQueue<T> PriorityQueue()
Alias for `PriorityQueue.empty()`

Type Parameters:
`T` - Component type of element.
Returns:
A new `PriorityQueue` empty instance

  - 

### PriorityQueue

public static <T extends Comparable<? super T>>
PriorityQueue<T> PriorityQueue(@NonNull Comparator<? super T> comparator)
Alias for `PriorityQueue.empty(Comparator)`

Type Parameters:
`T` - Component type of element.
Parameters:
`comparator` - The comparator used to sort the elements
Returns:
A new `PriorityQueue` empty instance

  - 

### PriorityQueue

public static <T extends Comparable<? super T>>
PriorityQueue<T> PriorityQueue(T element)
Alias for `PriorityQueue.of(Comparable)`

Type Parameters:
`T` - Component type of element.
Parameters:
`element` - An element.
Returns:
A new `PriorityQueue` instance containing the given element

  - 

### PriorityQueue

public static <T> PriorityQueue<T> PriorityQueue(Comparator<? super T> comparator,
 T element)
Alias for `PriorityQueue.of(Comparator, Object)`

Type Parameters:
`T` - Component type of element.
Parameters:
`comparator` - The comparator used to sort the elements
`element` - An element.
Returns:
A new `PriorityQueue` instance containing the given element

  - 

### PriorityQueue

@SafeVarargs
public static <T extends Comparable<? super T>>
PriorityQueue<T> PriorityQueue(T @NonNull ... elements)
Alias for `PriorityQueue.of(Comparable...)`

Type Parameters:
`T` - Component type of element.
Parameters:
`elements` - Zero or more elements.
Returns:
A new `PriorityQueue` instance containing the given elements

  - 

### PriorityQueue

@SafeVarargs
public static <T> PriorityQueue<T> PriorityQueue(@NonNull Comparator<? super T> comparator,
 T @NonNull ... elements)
Alias for `PriorityQueue.of(Comparator, Object...)`

Type Parameters:
`T` - Component type of element.
Parameters:
`comparator` - The comparator used to sort the elements
`elements` - Zero or more elements.
Returns:
A new `PriorityQueue` instance containing the given elements

  - 

### Seq

public static <T> Seq<T> Seq()
Alias for `List.empty()`

Type Parameters:
`T` - Component type of element.
Returns:
A singleton instance of empty `List`

  - 

### Seq

public static <T> Seq<T> Seq(T element)
Alias for `List.of(Object)`

Type Parameters:
`T` - Component type of element.
Parameters:
`element` - An element.
Returns:
A new `List` instance containing the given element

  - 

### Seq

@SafeVarargs
public static <T> Seq<T> Seq(T @NonNull ... elements)
Alias for `List.of(Object...)`

Type Parameters:
`T` - Component type of elements.
Parameters:
`elements` - Zero or more elements.
Returns:
A new `List` instance containing the given elements
Throws:
`NullPointerException` - if `elements` is null

  - 

### IndexedSeq

public static <T> IndexedSeq<T> IndexedSeq()
Alias for `Vector.empty()`

Type Parameters:
`T` - Component type of element.
Returns:
A singleton instance of empty `Vector`

  - 

### IndexedSeq

public static <T> IndexedSeq<T> IndexedSeq(T element)
Alias for `Vector.of(Object)`

Type Parameters:
`T` - Component type of element.
Parameters:
`element` - An element.
Returns:
A new `Vector` instance containing the given element

  - 

### IndexedSeq

@SafeVarargs
public static <T> IndexedSeq<T> IndexedSeq(T @NonNull ... elements)
Alias for `Vector.of(Object...)`

Type Parameters:
`T` - Component type of elements.
Parameters:
`elements` - Zero or more elements.
Returns:
A new `Vector` instance containing the given elements
Throws:
`NullPointerException` - if `elements` is null

  - 

### Array

public static <T> Array<T> Array()
Alias for `Array.empty()`

Type Parameters:
`T` - Component type of element.
Returns:
A singleton instance of empty `Array`

  - 

### Array

public static <T> Array<T> Array(T element)
Alias for `Array.of(Object)`

Type Parameters:
`T` - Component type of element.
Parameters:
`element` - An element.
Returns:
A new `Array` instance containing the given element

  - 

### Array

@SafeVarargs
public static <T> Array<T> Array(T @NonNull ... elements)
Alias for `Array.of(Object...)`

Type Parameters:
`T` - Component type of elements.
Parameters:
`elements` - Zero or more elements.
Returns:
A new `Array` instance containing the given elements
Throws:
`NullPointerException` - if `elements` is null

  - 

### List

public static <T> List<T> List()
Alias for `List.empty()`

Type Parameters:
`T` - Component type of element.
Returns:
A singleton instance of empty `List`

  - 

### List

public static <T> List<T> List(T element)
Alias for `List.of(Object)`

Type Parameters:
`T` - Component type of element.
Parameters:
`element` - An element.
Returns:
A new `List` instance containing the given element

  - 

### List

@SafeVarargs
public static <T> List<T> List(T @NonNull ... elements)
Alias for `List.of(Object...)`

Type Parameters:
`T` - Component type of elements.
Parameters:
`elements` - Zero or more elements.
Returns:
A new `List` instance containing the given elements
Throws:
`NullPointerException` - if `elements` is null

  - 

### Queue

public static <T> Queue<T> Queue()
Alias for `Queue.empty()`

Type Parameters:
`T` - Component type of element.
Returns:
A singleton instance of empty `Queue`

  - 

### Queue

public static <T> Queue<T> Queue(T element)
Alias for `Queue.of(Object)`

Type Parameters:
`T` - Component type of element.
Parameters:
`element` - An element.
Returns:
A new `Queue` instance containing the given element

  - 

### Queue

@SafeVarargs
public static <T> Queue<T> Queue(T @NonNull ... elements)
Alias for `Queue.of(Object...)`

Type Parameters:
`T` - Component type of elements.
Parameters:
`elements` - Zero or more elements.
Returns:
A new `Queue` instance containing the given elements
Throws:
`NullPointerException` - if `elements` is null

  - 

### Stream

public static <T> Stream<T> Stream()
Alias for `Stream.empty()`

Type Parameters:
`T` - Component type of element.
Returns:
A singleton instance of empty `Stream`

  - 

### Stream

public static <T> Stream<T> Stream(T element)
Alias for `Stream.of(Object)`

Type Parameters:
`T` - Component type of element.
Parameters:
`element` - An element.
Returns:
A new `Stream` instance containing the given element

  - 

### Stream

@SafeVarargs
public static <T> Stream<T> Stream(T @NonNull ... elements)
Alias for `Stream.of(Object...)`

Type Parameters:
`T` - Component type of elements.
Parameters:
`elements` - Zero or more elements.
Returns:
A new `Stream` instance containing the given elements
Throws:
`NullPointerException` - if `elements` is null

  - 

### Vector

public static <T> Vector<T> Vector()
Alias for `Vector.empty()`

Type Parameters:
`T` - Component type of element.
Returns:
A singleton instance of empty `Vector`

  - 

### Vector

public static <T> Vector<T> Vector(T element)
Alias for `Vector.of(Object)`

Type Parameters:
`T` - Component type of element.
Parameters:
`element` - An element.
Returns:
A new `Vector` instance containing the given element

  - 

### Vector

@SafeVarargs
public static <T> Vector<T> Vector(T @NonNull ... elements)
Alias for `Vector.of(Object...)`

Type Parameters:
`T` - Component type of elements.
Parameters:
`elements` - Zero or more elements.
Returns:
A new `Vector` instance containing the given elements
Throws:
`NullPointerException` - if `elements` is null

  - 

### Set

public static <T> Set<T> Set()
Alias for `HashSet.empty()`

Type Parameters:
`T` - Component type of element.
Returns:
A singleton instance of empty `HashSet`

  - 

### Set

public static <T> Set<T> Set(T element)
Alias for `HashSet.of(Object)`

Type Parameters:
`T` - Component type of element.
Parameters:
`element` - An element.
Returns:
A new `HashSet` instance containing the given element

  - 

### Set

@SafeVarargs
public static <T> Set<T> Set(T @NonNull ... elements)
Alias for `HashSet.of(Object...)`

Type Parameters:
`T` - Component type of elements.
Parameters:
`elements` - Zero or more elements.
Returns:
A new `HashSet` instance containing the given elements
Throws:
`NullPointerException` - if `elements` is null

  - 

### LinkedSet

public static <T> Set<T> LinkedSet()
Alias for `LinkedHashSet.empty()`

Type Parameters:
`T` - Component type of element.
Returns:
A singleton instance of empty `LinkedHashSet`

  - 

### LinkedSet

public static <T> Set<T> LinkedSet(T element)
Alias for `LinkedHashSet.of(Object)`

Type Parameters:
`T` - Component type of element.
Parameters:
`element` - An element.
Returns:
A new `LinkedHashSet` instance containing the given element

  - 

### LinkedSet

@SafeVarargs
public static <T> Set<T> LinkedSet(T @NonNull ... elements)
Alias for `LinkedHashSet.of(Object...)`

Type Parameters:
`T` - Component type of elements.
Parameters:
`elements` - Zero or more elements.
Returns:
A new `LinkedHashSet` instance containing the given elements
Throws:
`NullPointerException` - if `elements` is null

  - 

### SortedSet

public static <T extends Comparable<? super T>>
SortedSet<T> SortedSet()
Alias for `TreeSet.empty()`

Type Parameters:
`T` - Component type of element.
Returns:
A new `TreeSet` empty instance

  - 

### SortedSet

public static <T extends Comparable<? super T>>
SortedSet<T> SortedSet(@NonNull Comparator<? super T> comparator)
Alias for `TreeSet.empty(Comparator)`

Type Parameters:
`T` - Component type of element.
Parameters:
`comparator` - The comparator used to sort the elements
Returns:
A new `TreeSet` empty instance

  - 

### SortedSet

public static <T extends Comparable<? super T>>
SortedSet<T> SortedSet(T element)
Alias for `TreeSet.of(Comparable)`

Type Parameters:
`T` - Component type of element.
Parameters:
`element` - An element.
Returns:
A new `TreeSet` instance containing the given element

  - 

### SortedSet

public static <T> SortedSet<T> SortedSet(Comparator<? super T> comparator,
 T element)
Alias for `TreeSet.of(Comparator, Object)`

Type Parameters:
`T` - Component type of element.
Parameters:
`comparator` - The comparator used to sort the elements
`element` - An element.
Returns:
A new `TreeSet` instance containing the given element

  - 

### SortedSet

@SafeVarargs
public static <T extends Comparable<? super T>>
SortedSet<T> SortedSet(T @NonNull ... elements)
Alias for `TreeSet.of(Comparable...)`

Type Parameters:
`T` - Component type of element.
Parameters:
`elements` - Zero or more elements.
Returns:
A new `TreeSet` instance containing the given elements

  - 

### SortedSet

@SafeVarargs
public static <T> SortedSet<T> SortedSet(@NonNull Comparator<? super T> comparator,
 T @NonNull ... elements)
Alias for `TreeSet.of(Comparator, Object...)`

Type Parameters:
`T` - Component type of element.
Parameters:
`comparator` - The comparator used to sort the elements
`elements` - Zero or more elements.
Returns:
A new `TreeSet` instance containing the given elements

  - 

### Map

public static <K,
V> Map<K,V> Map()
Alias for `HashMap.empty()`

Type Parameters:
`K` - The key type.
`V` - The value type.
Returns:
A singleton instance of empty `HashMap`

  - 

### Map

@Deprecated
@SafeVarargs
public static <K,
V> Map<K,V> Map(Tuple2<? extends K,? extends V> @NonNull ... entries)
Deprecated.
Will be removed in a future version.

Alias for `HashMap.ofEntries(Tuple2...)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`entries` - Map entries.
Returns:
A new `HashMap` instance containing the given entries

  - 

### Map

public static <K,
V> Map<K,V> Map(K k1,
 V v1)
Alias for `HashMap.of(Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key
`v1` - The value
Returns:
A new `HashMap` instance containing the given entries

  - 

### Map

public static <K,
V> Map<K,V> Map(K k1,
 V v1,
 K k2,
 V v2)
Alias for `HashMap.of(Object, Object, Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
Returns:
A new `HashMap` instance containing the given entries

  - 

### Map

public static <K,
V> Map<K,V> Map(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3)
Alias for `HashMap.of(Object, Object, Object, Object, Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
Returns:
A new `HashMap` instance containing the given entries

  - 

### Map

public static <K,
V> Map<K,V> Map(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4)
Alias for `HashMap.of(Object, Object, Object, Object, Object, Object, Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
Returns:
A new `HashMap` instance containing the given entries

  - 

### Map

public static <K,
V> Map<K,V> Map(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5)
Alias for `HashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
`k5` - The key of the 5th pair
`v5` - The value of the 5th pair
Returns:
A new `HashMap` instance containing the given entries

  - 

### Map

public static <K,
V> Map<K,V> Map(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6)
Alias for `HashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
`k5` - The key of the 5th pair
`v5` - The value of the 5th pair
`k6` - The key of the 6th pair
`v6` - The value of the 6th pair
Returns:
A new `HashMap` instance containing the given entries

  - 

### Map

public static <K,
V> Map<K,V> Map(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7)
Alias for `HashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
`k5` - The key of the 5th pair
`v5` - The value of the 5th pair
`k6` - The key of the 6th pair
`v6` - The value of the 6th pair
`k7` - The key of the 7th pair
`v7` - The value of the 7th pair
Returns:
A new `HashMap` instance containing the given entries

  - 

### Map

public static <K,
V> Map<K,V> Map(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7,
 K k8,
 V v8)
Alias for `HashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
`k5` - The key of the 5th pair
`v5` - The value of the 5th pair
`k6` - The key of the 6th pair
`v6` - The value of the 6th pair
`k7` - The key of the 7th pair
`v7` - The value of the 7th pair
`k8` - The key of the 8th pair
`v8` - The value of the 8th pair
Returns:
A new `HashMap` instance containing the given entries

  - 

### Map

public static <K,
V> Map<K,V> Map(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7,
 K k8,
 V v8,
 K k9,
 V v9)
Alias for `HashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
`k5` - The key of the 5th pair
`v5` - The value of the 5th pair
`k6` - The key of the 6th pair
`v6` - The value of the 6th pair
`k7` - The key of the 7th pair
`v7` - The value of the 7th pair
`k8` - The key of the 8th pair
`v8` - The value of the 8th pair
`k9` - The key of the 9th pair
`v9` - The value of the 9th pair
Returns:
A new `HashMap` instance containing the given entries

  - 

### Map

public static <K,
V> Map<K,V> Map(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7,
 K k8,
 V v8,
 K k9,
 V v9,
 K k10,
 V v10)
Alias for `HashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
`k5` - The key of the 5th pair
`v5` - The value of the 5th pair
`k6` - The key of the 6th pair
`v6` - The value of the 6th pair
`k7` - The key of the 7th pair
`v7` - The value of the 7th pair
`k8` - The key of the 8th pair
`v8` - The value of the 8th pair
`k9` - The key of the 9th pair
`v9` - The value of the 9th pair
`k10` - The key of the 10th pair
`v10` - The value of the 10th pair
Returns:
A new `HashMap` instance containing the given entries

  - 

### LinkedMap

public static <K,
V> Map<K,V> LinkedMap()
Alias for `LinkedHashMap.empty()`

Type Parameters:
`K` - The key type.
`V` - The value type.
Returns:
A singleton instance of empty `LinkedHashMap`

  - 

### LinkedMap

@Deprecated
@SafeVarargs
public static <K,
V> Map<K,V> LinkedMap(Tuple2<? extends K,? extends V> @NonNull ... entries)
Deprecated.
Will be removed in a future version.

Alias for `LinkedHashMap.ofEntries(Tuple2...)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`entries` - Map entries.
Returns:
A new `LinkedHashMap` instance containing the given entries

  - 

### LinkedMap

public static <K,
V> Map<K,V> LinkedMap(K k1,
 V v1)
Alias for `LinkedHashMap.of(Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key
`v1` - The value
Returns:
A new `LinkedHashMap` instance containing the given entries

  - 

### LinkedMap

public static <K,
V> Map<K,V> LinkedMap(K k1,
 V v1,
 K k2,
 V v2)
Alias for `LinkedHashMap.of(Object, Object, Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
Returns:
A new `LinkedHashMap` instance containing the given entries

  - 

### LinkedMap

public static <K,
V> Map<K,V> LinkedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3)
Alias for `LinkedHashMap.of(Object, Object, Object, Object, Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
Returns:
A new `LinkedHashMap` instance containing the given entries

  - 

### LinkedMap

public static <K,
V> Map<K,V> LinkedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4)
Alias for `LinkedHashMap.of(Object, Object, Object, Object, Object, Object, Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
Returns:
A new `LinkedHashMap` instance containing the given entries

  - 

### LinkedMap

public static <K,
V> Map<K,V> LinkedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5)
Alias for `LinkedHashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
`k5` - The key of the 5th pair
`v5` - The value of the 5th pair
Returns:
A new `LinkedHashMap` instance containing the given entries

  - 

### LinkedMap

public static <K,
V> Map<K,V> LinkedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6)
Alias for `LinkedHashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
`k5` - The key of the 5th pair
`v5` - The value of the 5th pair
`k6` - The key of the 6th pair
`v6` - The value of the 6th pair
Returns:
A new `LinkedHashMap` instance containing the given entries

  - 

### LinkedMap

public static <K,
V> Map<K,V> LinkedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7)
Alias for `LinkedHashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
`k5` - The key of the 5th pair
`v5` - The value of the 5th pair
`k6` - The key of the 6th pair
`v6` - The value of the 6th pair
`k7` - The key of the 7th pair
`v7` - The value of the 7th pair
Returns:
A new `LinkedHashMap` instance containing the given entries

  - 

### LinkedMap

public static <K,
V> Map<K,V> LinkedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7,
 K k8,
 V v8)
Alias for `LinkedHashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
`k5` - The key of the 5th pair
`v5` - The value of the 5th pair
`k6` - The key of the 6th pair
`v6` - The value of the 6th pair
`k7` - The key of the 7th pair
`v7` - The value of the 7th pair
`k8` - The key of the 8th pair
`v8` - The value of the 8th pair
Returns:
A new `LinkedHashMap` instance containing the given entries

  - 

### LinkedMap

public static <K,
V> Map<K,V> LinkedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7,
 K k8,
 V v8,
 K k9,
 V v9)
Alias for `LinkedHashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
`k5` - The key of the 5th pair
`v5` - The value of the 5th pair
`k6` - The key of the 6th pair
`v6` - The value of the 6th pair
`k7` - The key of the 7th pair
`v7` - The value of the 7th pair
`k8` - The key of the 8th pair
`v8` - The value of the 8th pair
`k9` - The key of the 9th pair
`v9` - The value of the 9th pair
Returns:
A new `LinkedHashMap` instance containing the given entries

  - 

### LinkedMap

public static <K,
V> Map<K,V> LinkedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7,
 K k8,
 V v8,
 K k9,
 V v9,
 K k10,
 V v10)
Alias for `LinkedHashMap.of(Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
`k5` - The key of the 5th pair
`v5` - The value of the 5th pair
`k6` - The key of the 6th pair
`v6` - The value of the 6th pair
`k7` - The key of the 7th pair
`v7` - The value of the 7th pair
`k8` - The key of the 8th pair
`v8` - The value of the 8th pair
`k9` - The key of the 9th pair
`v9` - The value of the 9th pair
`k10` - The key of the 10th pair
`v10` - The value of the 10th pair
Returns:
A new `LinkedHashMap` instance containing the given entries

  - 

### SortedMap

public static <K extends Comparable<? super K>,
V>
SortedMap<K,V> SortedMap()
Alias for `TreeMap.empty()`

Type Parameters:
`K` - The key type.
`V` - The value type.
Returns:
A new empty `TreeMap` instance

  - 

### SortedMap

public static <K,
V> SortedMap<K,V> SortedMap(@NonNull Comparator<? super K> keyComparator)
Alias for `TreeMap.empty(Comparator)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`keyComparator` - The comparator used to sort the entries by their key
Returns:
A new empty `TreeMap` instance

  - 

### SortedMap

public static <K,
V> SortedMap<K,V> SortedMap(@NonNull Comparator<? super K> keyComparator,
 K key,
 V value)
Alias for `TreeMap.of(Comparator, Object, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`keyComparator` - The comparator used to sort the entries by their key
`key` - A singleton map key.
`value` - A singleton map value.
Returns:
A new `TreeMap` instance containing the given entry

  - 

### SortedMap

@Deprecated
@SafeVarargs
public static <K extends Comparable<? super K>,
V>
SortedMap<K,V> SortedMap(Tuple2<? extends K,? extends V> @NonNull ... entries)
Deprecated.
Will be removed in a future version.

Alias for `TreeMap.ofEntries(Tuple2...)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`entries` - Map entries.
Returns:
A new `TreeMap` instance containing the given entries

  - 

### SortedMap

@Deprecated
@SafeVarargs
public static <K,
V> SortedMap<K,V> SortedMap(@NonNull Comparator<? super K> keyComparator,
 Tuple2<? extends K,? extends V> @NonNull ... entries)
Deprecated.
Will be removed in a future version.

Alias for `TreeMap.ofEntries(Comparator, Tuple2...)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`keyComparator` - The comparator used to sort the entries by their key
`entries` - Map entries.
Returns:
A new `TreeMap` instance containing the given entry

  - 

### SortedMap

@Deprecated
public static <K extends Comparable<? super K>,
V>
SortedMap<K,V> SortedMap(Map<? extends K,? extends V> map)
Deprecated.
Will be removed in a future version.

Alias for `TreeMap.ofAll(java.util.Map)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`map` - A map entry.
Returns:
A new `TreeMap` instance containing the given map

  - 

### SortedMap

public static <K extends Comparable<? super K>,
V>
SortedMap<K,V> SortedMap(K k1,
 V v1)
Alias for `TreeMap.of(Comparable, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key
`v1` - The value
Returns:
A new `TreeMap` instance containing the given entries

  - 

### SortedMap

public static <K extends Comparable<? super K>,
V>
SortedMap<K,V> SortedMap(K k1,
 V v1,
 K k2,
 V v2)
Alias for `TreeMap.of(Comparable, Object, Comparable, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
Returns:
A new `TreeMap` instance containing the given entries

  - 

### SortedMap

public static <K extends Comparable<? super K>,
V>
SortedMap<K,V> SortedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3)
Alias for `TreeMap.of(Comparable, Object, Comparable, Object, Comparable, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
Returns:
A new `TreeMap` instance containing the given entries

  - 

### SortedMap

public static <K extends Comparable<? super K>,
V>
SortedMap<K,V> SortedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4)
Alias for `TreeMap.of(Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
Returns:
A new `TreeMap` instance containing the given entries

  - 

### SortedMap

public static <K extends Comparable<? super K>,
V>
SortedMap<K,V> SortedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5)
Alias for `TreeMap.of(Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
`k5` - The key of the 5th pair
`v5` - The value of the 5th pair
Returns:
A new `TreeMap` instance containing the given entries

  - 

### SortedMap

public static <K extends Comparable<? super K>,
V>
SortedMap<K,V> SortedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6)
Alias for `TreeMap.of(Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
`k5` - The key of the 5th pair
`v5` - The value of the 5th pair
`k6` - The key of the 6th pair
`v6` - The value of the 6th pair
Returns:
A new `TreeMap` instance containing the given entries

  - 

### SortedMap

public static <K extends Comparable<? super K>,
V>
SortedMap<K,V> SortedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7)
Alias for `TreeMap.of(Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
`k5` - The key of the 5th pair
`v5` - The value of the 5th pair
`k6` - The key of the 6th pair
`v6` - The value of the 6th pair
`k7` - The key of the 7th pair
`v7` - The value of the 7th pair
Returns:
A new `TreeMap` instance containing the given entries

  - 

### SortedMap

public static <K extends Comparable<? super K>,
V>
SortedMap<K,V> SortedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7,
 K k8,
 V v8)
Alias for `TreeMap.of(Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
`k5` - The key of the 5th pair
`v5` - The value of the 5th pair
`k6` - The key of the 6th pair
`v6` - The value of the 6th pair
`k7` - The key of the 7th pair
`v7` - The value of the 7th pair
`k8` - The key of the 8th pair
`v8` - The value of the 8th pair
Returns:
A new `TreeMap` instance containing the given entries

  - 

### SortedMap

public static <K extends Comparable<? super K>,
V>
SortedMap<K,V> SortedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7,
 K k8,
 V v8,
 K k9,
 V v9)
Alias for `TreeMap.of(Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
`k5` - The key of the 5th pair
`v5` - The value of the 5th pair
`k6` - The key of the 6th pair
`v6` - The value of the 6th pair
`k7` - The key of the 7th pair
`v7` - The value of the 7th pair
`k8` - The key of the 8th pair
`v8` - The value of the 8th pair
`k9` - The key of the 9th pair
`v9` - The value of the 9th pair
Returns:
A new `TreeMap` instance containing the given entries

  - 

### SortedMap

public static <K extends Comparable<? super K>,
V>
SortedMap<K,V> SortedMap(K k1,
 V v1,
 K k2,
 V v2,
 K k3,
 V v3,
 K k4,
 V v4,
 K k5,
 V v5,
 K k6,
 V v6,
 K k7,
 V v7,
 K k8,
 V v8,
 K k9,
 V v9,
 K k10,
 V v10)
Alias for `TreeMap.of(Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object, Comparable, Object)`

Type Parameters:
`K` - The key type.
`V` - The value type.
Parameters:
`k1` - The key of the 1st pair
`v1` - The value of the 1st pair
`k2` - The key of the 2nd pair
`v2` - The value of the 2nd pair
`k3` - The key of the 3rd pair
`v3` - The value of the 3rd pair
`k4` - The key of the 4th pair
`v4` - The value of the 4th pair
`k5` - The key of the 5th pair
`v5` - The value of the 5th pair
`k6` - The key of the 6th pair
`v6` - The value of the 6th pair
`k7` - The key of the 7th pair
`v7` - The value of the 7th pair
`k8` - The key of the 8th pair
`v8` - The value of the 8th pair
`k9` - The key of the 9th pair
`v9` - The value of the 9th pair
`k10` - The key of the 10th pair
`v10` - The value of the 10th pair
Returns:
A new `TreeMap` instance containing the given entries

  - 

### run

public static Void run(Runnable unit)
Runs a `unit` of work and returns `Void`. This is helpful when a return value is expected,
 e.g. by `Match`:

 

```
Match(i).of(
     Case($(is(0)), i -> run(() -> System.out.println("zero"))),
     Case($(is(1)), i -> run(() -> System.out.println("one"))),
     Case($(), o -> run(() -> System.out.println("many")))
 )
```

Parameters:
`unit` - A block of code to be run.
Returns:
the single instance of `Void`, namely `null`

  - 

### For

public static <T,
U> Iterator<U> For(Iterable<T> ts,
 Function<? super T,? extends Iterable<U>> f)
A shortcut for `Iterator.ofAll(ts).flatMap(f)` which allows us to write real for-comprehensions using
 `For(...).yield(...)`.
 

 Example:
 

```

 For(getPersons(), person ->
     For(person.getTweets(), tweet ->
         For(tweet.getReplies())
             .yield(reply -> person + ", " + tweet + ", " + reply)));
 
```

Type Parameters:
`T` - element type of `ts`
`U` - component type of the resulting `Iterator`
Parameters:
`ts` - An iterable
`f` - A function `T -> Iterable<U>`
Returns:
A new Iterator

  - 

### For

public static <T1> API.For1<T1> For(@NonNull Iterable<T1> ts1)
Creates a `For`-comprehension of one Iterable.

Type Parameters:
`T1` - component type of the 1st Iterable
Parameters:
`ts1` - the 1st Iterable
Returns:
a new `For`-comprehension of arity 1

  - 

### For

public static <T1,
T2> API.For2<T1,T2> For(@NonNull Iterable<T1> ts1,
 @NonNull Iterable<T2> ts2)
Creates a `For`-comprehension of two Iterables.

Type Parameters:
`T1` - component type of the 1st Iterable
`T2` - component type of the 2nd Iterable
Parameters:
`ts1` - the 1st Iterable
`ts2` - the 2nd Iterable
Returns:
a new `For`-comprehension of arity 2

  - 

### For

public static <T1,
T2,
T3> API.For3<T1,T2,T3> For(@NonNull Iterable<T1> ts1,
 @NonNull Iterable<T2> ts2,
 @NonNull Iterable<T3> ts3)
Creates a `For`-comprehension of three Iterables.

Type Parameters:
`T1` - component type of the 1st Iterable
`T2` - component type of the 2nd Iterable
`T3` - component type of the 3rd Iterable
Parameters:
`ts1` - the 1st Iterable
`ts2` - the 2nd Iterable
`ts3` - the 3rd Iterable
Returns:
a new `For`-comprehension of arity 3

  - 

### For

public static <T1,
T2,
T3,
T4>
API.For4<T1,T2,T3,T4> For(@NonNull Iterable<T1> ts1,
 @NonNull Iterable<T2> ts2,
 @NonNull Iterable<T3> ts3,
 @NonNull Iterable<T4> ts4)
Creates a `For`-comprehension of 4 Iterables.

Type Parameters:
`T1` - component type of the 1st Iterable
`T2` - component type of the 2nd Iterable
`T3` - component type of the 3rd Iterable
`T4` - component type of the 4th Iterable
Parameters:
`ts1` - the 1st Iterable
`ts2` - the 2nd Iterable
`ts3` - the 3rd Iterable
`ts4` - the 4th Iterable
Returns:
a new `For`-comprehension of arity 4

  - 

### For

public static <T1,
T2,
T3,
T4,
T5>
API.For5<T1,T2,T3,T4,T5> For(@NonNull Iterable<T1> ts1,
 @NonNull Iterable<T2> ts2,
 @NonNull Iterable<T3> ts3,
 @NonNull Iterable<T4> ts4,
 @NonNull Iterable<T5> ts5)
Creates a `For`-comprehension of 5 Iterables.

Type Parameters:
`T1` - component type of the 1st Iterable
`T2` - component type of the 2nd Iterable
`T3` - component type of the 3rd Iterable
`T4` - component type of the 4th Iterable
`T5` - component type of the 5th Iterable
Parameters:
`ts1` - the 1st Iterable
`ts2` - the 2nd Iterable
`ts3` - the 3rd Iterable
`ts4` - the 4th Iterable
`ts5` - the 5th Iterable
Returns:
a new `For`-comprehension of arity 5

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6>
API.For6<T1,T2,T3,T4,T5,T6> For(@NonNull Iterable<T1> ts1,
 @NonNull Iterable<T2> ts2,
 @NonNull Iterable<T3> ts3,
 @NonNull Iterable<T4> ts4,
 @NonNull Iterable<T5> ts5,
 @NonNull Iterable<T6> ts6)
Creates a `For`-comprehension of 6 Iterables.

Type Parameters:
`T1` - component type of the 1st Iterable
`T2` - component type of the 2nd Iterable
`T3` - component type of the 3rd Iterable
`T4` - component type of the 4th Iterable
`T5` - component type of the 5th Iterable
`T6` - component type of the 6th Iterable
Parameters:
`ts1` - the 1st Iterable
`ts2` - the 2nd Iterable
`ts3` - the 3rd Iterable
`ts4` - the 4th Iterable
`ts5` - the 5th Iterable
`ts6` - the 6th Iterable
Returns:
a new `For`-comprehension of arity 6

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.For7<T1,T2,T3,T4,T5,T6,T7> For(@NonNull Iterable<T1> ts1,
 @NonNull Iterable<T2> ts2,
 @NonNull Iterable<T3> ts3,
 @NonNull Iterable<T4> ts4,
 @NonNull Iterable<T5> ts5,
 @NonNull Iterable<T6> ts6,
 @NonNull Iterable<T7> ts7)
Creates a `For`-comprehension of 7 Iterables.

Type Parameters:
`T1` - component type of the 1st Iterable
`T2` - component type of the 2nd Iterable
`T3` - component type of the 3rd Iterable
`T4` - component type of the 4th Iterable
`T5` - component type of the 5th Iterable
`T6` - component type of the 6th Iterable
`T7` - component type of the 7th Iterable
Parameters:
`ts1` - the 1st Iterable
`ts2` - the 2nd Iterable
`ts3` - the 3rd Iterable
`ts4` - the 4th Iterable
`ts5` - the 5th Iterable
`ts6` - the 6th Iterable
`ts7` - the 7th Iterable
Returns:
a new `For`-comprehension of arity 7

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.For8<T1,T2,T3,T4,T5,T6,T7,T8> For(@NonNull Iterable<T1> ts1,
 @NonNull Iterable<T2> ts2,
 @NonNull Iterable<T3> ts3,
 @NonNull Iterable<T4> ts4,
 @NonNull Iterable<T5> ts5,
 @NonNull Iterable<T6> ts6,
 @NonNull Iterable<T7> ts7,
 @NonNull Iterable<T8> ts8)
Creates a `For`-comprehension of 8 Iterables.

Type Parameters:
`T1` - component type of the 1st Iterable
`T2` - component type of the 2nd Iterable
`T3` - component type of the 3rd Iterable
`T4` - component type of the 4th Iterable
`T5` - component type of the 5th Iterable
`T6` - component type of the 6th Iterable
`T7` - component type of the 7th Iterable
`T8` - component type of the 8th Iterable
Parameters:
`ts1` - the 1st Iterable
`ts2` - the 2nd Iterable
`ts3` - the 3rd Iterable
`ts4` - the 4th Iterable
`ts5` - the 5th Iterable
`ts6` - the 6th Iterable
`ts7` - the 7th Iterable
`ts8` - the 8th Iterable
Returns:
a new `For`-comprehension of arity 8

  - 

### For

public static <T1> API.For1Option<T1> For(@NonNull Option<T1> ts1)
Creates a `For`-comprehension of one Option.

Type Parameters:
`T1` - component type of the 1st Option
Parameters:
`ts1` - the 1st Option
Returns:
a new `For`-comprehension of arity 1

  - 

### For

public static <T1,
T2> API.For2Option<T1,T2> For(@NonNull Option<T1> ts1,
 @NonNull Option<T2> ts2)
Creates a `For`-comprehension of two Options.

Type Parameters:
`T1` - component type of the 1st Option
`T2` - component type of the 2nd Option
Parameters:
`ts1` - the 1st Option
`ts2` - the 2nd Option
Returns:
a new `For`-comprehension of arity 2

  - 

### For

public static <T1,
T2,
T3> API.For3Option<T1,T2,T3> For(@NonNull Option<T1> ts1,
 @NonNull Option<T2> ts2,
 @NonNull Option<T3> ts3)
Creates a `For`-comprehension of three Options.

Type Parameters:
`T1` - component type of the 1st Option
`T2` - component type of the 2nd Option
`T3` - component type of the 3rd Option
Parameters:
`ts1` - the 1st Option
`ts2` - the 2nd Option
`ts3` - the 3rd Option
Returns:
a new `For`-comprehension of arity 3

  - 

### For

public static <T1,
T2,
T3,
T4>
API.For4Option<T1,T2,T3,T4> For(@NonNull Option<T1> ts1,
 @NonNull Option<T2> ts2,
 @NonNull Option<T3> ts3,
 @NonNull Option<T4> ts4)
Creates a `For`-comprehension of 4 Options.

Type Parameters:
`T1` - component type of the 1st Option
`T2` - component type of the 2nd Option
`T3` - component type of the 3rd Option
`T4` - component type of the 4th Option
Parameters:
`ts1` - the 1st Option
`ts2` - the 2nd Option
`ts3` - the 3rd Option
`ts4` - the 4th Option
Returns:
a new `For`-comprehension of arity 4

  - 

### For

public static <T1,
T2,
T3,
T4,
T5>
API.For5Option<T1,T2,T3,T4,T5> For(@NonNull Option<T1> ts1,
 @NonNull Option<T2> ts2,
 @NonNull Option<T3> ts3,
 @NonNull Option<T4> ts4,
 @NonNull Option<T5> ts5)
Creates a `For`-comprehension of 5 Options.

Type Parameters:
`T1` - component type of the 1st Option
`T2` - component type of the 2nd Option
`T3` - component type of the 3rd Option
`T4` - component type of the 4th Option
`T5` - component type of the 5th Option
Parameters:
`ts1` - the 1st Option
`ts2` - the 2nd Option
`ts3` - the 3rd Option
`ts4` - the 4th Option
`ts5` - the 5th Option
Returns:
a new `For`-comprehension of arity 5

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6>
API.For6Option<T1,T2,T3,T4,T5,T6> For(@NonNull Option<T1> ts1,
 @NonNull Option<T2> ts2,
 @NonNull Option<T3> ts3,
 @NonNull Option<T4> ts4,
 @NonNull Option<T5> ts5,
 @NonNull Option<T6> ts6)
Creates a `For`-comprehension of 6 Options.

Type Parameters:
`T1` - component type of the 1st Option
`T2` - component type of the 2nd Option
`T3` - component type of the 3rd Option
`T4` - component type of the 4th Option
`T5` - component type of the 5th Option
`T6` - component type of the 6th Option
Parameters:
`ts1` - the 1st Option
`ts2` - the 2nd Option
`ts3` - the 3rd Option
`ts4` - the 4th Option
`ts5` - the 5th Option
`ts6` - the 6th Option
Returns:
a new `For`-comprehension of arity 6

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.For7Option<T1,T2,T3,T4,T5,T6,T7> For(@NonNull Option<T1> ts1,
 @NonNull Option<T2> ts2,
 @NonNull Option<T3> ts3,
 @NonNull Option<T4> ts4,
 @NonNull Option<T5> ts5,
 @NonNull Option<T6> ts6,
 @NonNull Option<T7> ts7)
Creates a `For`-comprehension of 7 Options.

Type Parameters:
`T1` - component type of the 1st Option
`T2` - component type of the 2nd Option
`T3` - component type of the 3rd Option
`T4` - component type of the 4th Option
`T5` - component type of the 5th Option
`T6` - component type of the 6th Option
`T7` - component type of the 7th Option
Parameters:
`ts1` - the 1st Option
`ts2` - the 2nd Option
`ts3` - the 3rd Option
`ts4` - the 4th Option
`ts5` - the 5th Option
`ts6` - the 6th Option
`ts7` - the 7th Option
Returns:
a new `For`-comprehension of arity 7

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.For8Option<T1,T2,T3,T4,T5,T6,T7,T8> For(@NonNull Option<T1> ts1,
 @NonNull Option<T2> ts2,
 @NonNull Option<T3> ts3,
 @NonNull Option<T4> ts4,
 @NonNull Option<T5> ts5,
 @NonNull Option<T6> ts6,
 @NonNull Option<T7> ts7,
 @NonNull Option<T8> ts8)
Creates a `For`-comprehension of 8 Options.

Type Parameters:
`T1` - component type of the 1st Option
`T2` - component type of the 2nd Option
`T3` - component type of the 3rd Option
`T4` - component type of the 4th Option
`T5` - component type of the 5th Option
`T6` - component type of the 6th Option
`T7` - component type of the 7th Option
`T8` - component type of the 8th Option
Parameters:
`ts1` - the 1st Option
`ts2` - the 2nd Option
`ts3` - the 3rd Option
`ts4` - the 4th Option
`ts5` - the 5th Option
`ts6` - the 6th Option
`ts7` - the 7th Option
`ts8` - the 8th Option
Returns:
a new `For`-comprehension of arity 8

  - 

### For

public static <T1> API.For1Future<T1> For(@NonNull Future<T1> ts1)
Creates a `For`-comprehension of one Future.

Type Parameters:
`T1` - component type of the 1st Future
Parameters:
`ts1` - the 1st Future
Returns:
a new `For`-comprehension of arity 1

  - 

### For

public static <T1,
T2> API.For2Future<T1,T2> For(@NonNull Future<T1> ts1,
 @NonNull Future<T2> ts2)
Creates a `For`-comprehension of two Futures.

Type Parameters:
`T1` - component type of the 1st Future
`T2` - component type of the 2nd Future
Parameters:
`ts1` - the 1st Future
`ts2` - the 2nd Future
Returns:
a new `For`-comprehension of arity 2

  - 

### For

public static <T1,
T2,
T3> API.For3Future<T1,T2,T3> For(@NonNull Future<T1> ts1,
 @NonNull Future<T2> ts2,
 @NonNull Future<T3> ts3)
Creates a `For`-comprehension of three Futures.

Type Parameters:
`T1` - component type of the 1st Future
`T2` - component type of the 2nd Future
`T3` - component type of the 3rd Future
Parameters:
`ts1` - the 1st Future
`ts2` - the 2nd Future
`ts3` - the 3rd Future
Returns:
a new `For`-comprehension of arity 3

  - 

### For

public static <T1,
T2,
T3,
T4>
API.For4Future<T1,T2,T3,T4> For(@NonNull Future<T1> ts1,
 @NonNull Future<T2> ts2,
 @NonNull Future<T3> ts3,
 @NonNull Future<T4> ts4)
Creates a `For`-comprehension of 4 Futures.

Type Parameters:
`T1` - component type of the 1st Future
`T2` - component type of the 2nd Future
`T3` - component type of the 3rd Future
`T4` - component type of the 4th Future
Parameters:
`ts1` - the 1st Future
`ts2` - the 2nd Future
`ts3` - the 3rd Future
`ts4` - the 4th Future
Returns:
a new `For`-comprehension of arity 4

  - 

### For

public static <T1,
T2,
T3,
T4,
T5>
API.For5Future<T1,T2,T3,T4,T5> For(@NonNull Future<T1> ts1,
 @NonNull Future<T2> ts2,
 @NonNull Future<T3> ts3,
 @NonNull Future<T4> ts4,
 @NonNull Future<T5> ts5)
Creates a `For`-comprehension of 5 Futures.

Type Parameters:
`T1` - component type of the 1st Future
`T2` - component type of the 2nd Future
`T3` - component type of the 3rd Future
`T4` - component type of the 4th Future
`T5` - component type of the 5th Future
Parameters:
`ts1` - the 1st Future
`ts2` - the 2nd Future
`ts3` - the 3rd Future
`ts4` - the 4th Future
`ts5` - the 5th Future
Returns:
a new `For`-comprehension of arity 5

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6>
API.For6Future<T1,T2,T3,T4,T5,T6> For(@NonNull Future<T1> ts1,
 @NonNull Future<T2> ts2,
 @NonNull Future<T3> ts3,
 @NonNull Future<T4> ts4,
 @NonNull Future<T5> ts5,
 @NonNull Future<T6> ts6)
Creates a `For`-comprehension of 6 Futures.

Type Parameters:
`T1` - component type of the 1st Future
`T2` - component type of the 2nd Future
`T3` - component type of the 3rd Future
`T4` - component type of the 4th Future
`T5` - component type of the 5th Future
`T6` - component type of the 6th Future
Parameters:
`ts1` - the 1st Future
`ts2` - the 2nd Future
`ts3` - the 3rd Future
`ts4` - the 4th Future
`ts5` - the 5th Future
`ts6` - the 6th Future
Returns:
a new `For`-comprehension of arity 6

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.For7Future<T1,T2,T3,T4,T5,T6,T7> For(@NonNull Future<T1> ts1,
 @NonNull Future<T2> ts2,
 @NonNull Future<T3> ts3,
 @NonNull Future<T4> ts4,
 @NonNull Future<T5> ts5,
 @NonNull Future<T6> ts6,
 @NonNull Future<T7> ts7)
Creates a `For`-comprehension of 7 Futures.

Type Parameters:
`T1` - component type of the 1st Future
`T2` - component type of the 2nd Future
`T3` - component type of the 3rd Future
`T4` - component type of the 4th Future
`T5` - component type of the 5th Future
`T6` - component type of the 6th Future
`T7` - component type of the 7th Future
Parameters:
`ts1` - the 1st Future
`ts2` - the 2nd Future
`ts3` - the 3rd Future
`ts4` - the 4th Future
`ts5` - the 5th Future
`ts6` - the 6th Future
`ts7` - the 7th Future
Returns:
a new `For`-comprehension of arity 7

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.For8Future<T1,T2,T3,T4,T5,T6,T7,T8> For(@NonNull Future<T1> ts1,
 @NonNull Future<T2> ts2,
 @NonNull Future<T3> ts3,
 @NonNull Future<T4> ts4,
 @NonNull Future<T5> ts5,
 @NonNull Future<T6> ts6,
 @NonNull Future<T7> ts7,
 @NonNull Future<T8> ts8)
Creates a `For`-comprehension of 8 Futures.

Type Parameters:
`T1` - component type of the 1st Future
`T2` - component type of the 2nd Future
`T3` - component type of the 3rd Future
`T4` - component type of the 4th Future
`T5` - component type of the 5th Future
`T6` - component type of the 6th Future
`T7` - component type of the 7th Future
`T8` - component type of the 8th Future
Parameters:
`ts1` - the 1st Future
`ts2` - the 2nd Future
`ts3` - the 3rd Future
`ts4` - the 4th Future
`ts5` - the 5th Future
`ts6` - the 6th Future
`ts7` - the 7th Future
`ts8` - the 8th Future
Returns:
a new `For`-comprehension of arity 8

  - 

### For

public static <T1> API.For1Try<T1> For(@NonNull Try<T1> ts1)
Creates a `For`-comprehension of one Try.

Type Parameters:
`T1` - component type of the 1st Try
Parameters:
`ts1` - the 1st Try
Returns:
a new `For`-comprehension of arity 1

  - 

### For

public static <T1,
T2> API.For2Try<T1,T2> For(@NonNull Try<T1> ts1,
 @NonNull Try<T2> ts2)
Creates a `For`-comprehension of two Trys.

Type Parameters:
`T1` - component type of the 1st Try
`T2` - component type of the 2nd Try
Parameters:
`ts1` - the 1st Try
`ts2` - the 2nd Try
Returns:
a new `For`-comprehension of arity 2

  - 

### For

public static <T1,
T2,
T3> API.For3Try<T1,T2,T3> For(@NonNull Try<T1> ts1,
 @NonNull Try<T2> ts2,
 @NonNull Try<T3> ts3)
Creates a `For`-comprehension of three Trys.

Type Parameters:
`T1` - component type of the 1st Try
`T2` - component type of the 2nd Try
`T3` - component type of the 3rd Try
Parameters:
`ts1` - the 1st Try
`ts2` - the 2nd Try
`ts3` - the 3rd Try
Returns:
a new `For`-comprehension of arity 3

  - 

### For

public static <T1,
T2,
T3,
T4>
API.For4Try<T1,T2,T3,T4> For(@NonNull Try<T1> ts1,
 @NonNull Try<T2> ts2,
 @NonNull Try<T3> ts3,
 @NonNull Try<T4> ts4)
Creates a `For`-comprehension of 4 Trys.

Type Parameters:
`T1` - component type of the 1st Try
`T2` - component type of the 2nd Try
`T3` - component type of the 3rd Try
`T4` - component type of the 4th Try
Parameters:
`ts1` - the 1st Try
`ts2` - the 2nd Try
`ts3` - the 3rd Try
`ts4` - the 4th Try
Returns:
a new `For`-comprehension of arity 4

  - 

### For

public static <T1,
T2,
T3,
T4,
T5>
API.For5Try<T1,T2,T3,T4,T5> For(@NonNull Try<T1> ts1,
 @NonNull Try<T2> ts2,
 @NonNull Try<T3> ts3,
 @NonNull Try<T4> ts4,
 @NonNull Try<T5> ts5)
Creates a `For`-comprehension of 5 Trys.

Type Parameters:
`T1` - component type of the 1st Try
`T2` - component type of the 2nd Try
`T3` - component type of the 3rd Try
`T4` - component type of the 4th Try
`T5` - component type of the 5th Try
Parameters:
`ts1` - the 1st Try
`ts2` - the 2nd Try
`ts3` - the 3rd Try
`ts4` - the 4th Try
`ts5` - the 5th Try
Returns:
a new `For`-comprehension of arity 5

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6>
API.For6Try<T1,T2,T3,T4,T5,T6> For(@NonNull Try<T1> ts1,
 @NonNull Try<T2> ts2,
 @NonNull Try<T3> ts3,
 @NonNull Try<T4> ts4,
 @NonNull Try<T5> ts5,
 @NonNull Try<T6> ts6)
Creates a `For`-comprehension of 6 Trys.

Type Parameters:
`T1` - component type of the 1st Try
`T2` - component type of the 2nd Try
`T3` - component type of the 3rd Try
`T4` - component type of the 4th Try
`T5` - component type of the 5th Try
`T6` - component type of the 6th Try
Parameters:
`ts1` - the 1st Try
`ts2` - the 2nd Try
`ts3` - the 3rd Try
`ts4` - the 4th Try
`ts5` - the 5th Try
`ts6` - the 6th Try
Returns:
a new `For`-comprehension of arity 6

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.For7Try<T1,T2,T3,T4,T5,T6,T7> For(@NonNull Try<T1> ts1,
 @NonNull Try<T2> ts2,
 @NonNull Try<T3> ts3,
 @NonNull Try<T4> ts4,
 @NonNull Try<T5> ts5,
 @NonNull Try<T6> ts6,
 @NonNull Try<T7> ts7)
Creates a `For`-comprehension of 7 Trys.

Type Parameters:
`T1` - component type of the 1st Try
`T2` - component type of the 2nd Try
`T3` - component type of the 3rd Try
`T4` - component type of the 4th Try
`T5` - component type of the 5th Try
`T6` - component type of the 6th Try
`T7` - component type of the 7th Try
Parameters:
`ts1` - the 1st Try
`ts2` - the 2nd Try
`ts3` - the 3rd Try
`ts4` - the 4th Try
`ts5` - the 5th Try
`ts6` - the 6th Try
`ts7` - the 7th Try
Returns:
a new `For`-comprehension of arity 7

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.For8Try<T1,T2,T3,T4,T5,T6,T7,T8> For(@NonNull Try<T1> ts1,
 @NonNull Try<T2> ts2,
 @NonNull Try<T3> ts3,
 @NonNull Try<T4> ts4,
 @NonNull Try<T5> ts5,
 @NonNull Try<T6> ts6,
 @NonNull Try<T7> ts7,
 @NonNull Try<T8> ts8)
Creates a `For`-comprehension of 8 Trys.

Type Parameters:
`T1` - component type of the 1st Try
`T2` - component type of the 2nd Try
`T3` - component type of the 3rd Try
`T4` - component type of the 4th Try
`T5` - component type of the 5th Try
`T6` - component type of the 6th Try
`T7` - component type of the 7th Try
`T8` - component type of the 8th Try
Parameters:
`ts1` - the 1st Try
`ts2` - the 2nd Try
`ts3` - the 3rd Try
`ts4` - the 4th Try
`ts5` - the 5th Try
`ts6` - the 6th Try
`ts7` - the 7th Try
`ts8` - the 8th Try
Returns:
a new `For`-comprehension of arity 8

  - 

### For

public static <T1> API.For1List<T1> For(@NonNull List<T1> ts1)
Creates a `For`-comprehension of one List.

Type Parameters:
`T1` - component type of the 1st List
Parameters:
`ts1` - the 1st List
Returns:
a new `For`-comprehension of arity 1

  - 

### For

public static <T1,
T2> API.For2List<T1,T2> For(@NonNull List<T1> ts1,
 @NonNull List<T2> ts2)
Creates a `For`-comprehension of two Lists.

Type Parameters:
`T1` - component type of the 1st List
`T2` - component type of the 2nd List
Parameters:
`ts1` - the 1st List
`ts2` - the 2nd List
Returns:
a new `For`-comprehension of arity 2

  - 

### For

public static <T1,
T2,
T3> API.For3List<T1,T2,T3> For(@NonNull List<T1> ts1,
 @NonNull List<T2> ts2,
 @NonNull List<T3> ts3)
Creates a `For`-comprehension of three Lists.

Type Parameters:
`T1` - component type of the 1st List
`T2` - component type of the 2nd List
`T3` - component type of the 3rd List
Parameters:
`ts1` - the 1st List
`ts2` - the 2nd List
`ts3` - the 3rd List
Returns:
a new `For`-comprehension of arity 3

  - 

### For

public static <T1,
T2,
T3,
T4>
API.For4List<T1,T2,T3,T4> For(@NonNull List<T1> ts1,
 @NonNull List<T2> ts2,
 @NonNull List<T3> ts3,
 @NonNull List<T4> ts4)
Creates a `For`-comprehension of 4 Lists.

Type Parameters:
`T1` - component type of the 1st List
`T2` - component type of the 2nd List
`T3` - component type of the 3rd List
`T4` - component type of the 4th List
Parameters:
`ts1` - the 1st List
`ts2` - the 2nd List
`ts3` - the 3rd List
`ts4` - the 4th List
Returns:
a new `For`-comprehension of arity 4

  - 

### For

public static <T1,
T2,
T3,
T4,
T5>
API.For5List<T1,T2,T3,T4,T5> For(@NonNull List<T1> ts1,
 @NonNull List<T2> ts2,
 @NonNull List<T3> ts3,
 @NonNull List<T4> ts4,
 @NonNull List<T5> ts5)
Creates a `For`-comprehension of 5 Lists.

Type Parameters:
`T1` - component type of the 1st List
`T2` - component type of the 2nd List
`T3` - component type of the 3rd List
`T4` - component type of the 4th List
`T5` - component type of the 5th List
Parameters:
`ts1` - the 1st List
`ts2` - the 2nd List
`ts3` - the 3rd List
`ts4` - the 4th List
`ts5` - the 5th List
Returns:
a new `For`-comprehension of arity 5

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6>
API.For6List<T1,T2,T3,T4,T5,T6> For(@NonNull List<T1> ts1,
 @NonNull List<T2> ts2,
 @NonNull List<T3> ts3,
 @NonNull List<T4> ts4,
 @NonNull List<T5> ts5,
 @NonNull List<T6> ts6)
Creates a `For`-comprehension of 6 Lists.

Type Parameters:
`T1` - component type of the 1st List
`T2` - component type of the 2nd List
`T3` - component type of the 3rd List
`T4` - component type of the 4th List
`T5` - component type of the 5th List
`T6` - component type of the 6th List
Parameters:
`ts1` - the 1st List
`ts2` - the 2nd List
`ts3` - the 3rd List
`ts4` - the 4th List
`ts5` - the 5th List
`ts6` - the 6th List
Returns:
a new `For`-comprehension of arity 6

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.For7List<T1,T2,T3,T4,T5,T6,T7> For(@NonNull List<T1> ts1,
 @NonNull List<T2> ts2,
 @NonNull List<T3> ts3,
 @NonNull List<T4> ts4,
 @NonNull List<T5> ts5,
 @NonNull List<T6> ts6,
 @NonNull List<T7> ts7)
Creates a `For`-comprehension of 7 Lists.

Type Parameters:
`T1` - component type of the 1st List
`T2` - component type of the 2nd List
`T3` - component type of the 3rd List
`T4` - component type of the 4th List
`T5` - component type of the 5th List
`T6` - component type of the 6th List
`T7` - component type of the 7th List
Parameters:
`ts1` - the 1st List
`ts2` - the 2nd List
`ts3` - the 3rd List
`ts4` - the 4th List
`ts5` - the 5th List
`ts6` - the 6th List
`ts7` - the 7th List
Returns:
a new `For`-comprehension of arity 7

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.For8List<T1,T2,T3,T4,T5,T6,T7,T8> For(@NonNull List<T1> ts1,
 @NonNull List<T2> ts2,
 @NonNull List<T3> ts3,
 @NonNull List<T4> ts4,
 @NonNull List<T5> ts5,
 @NonNull List<T6> ts6,
 @NonNull List<T7> ts7,
 @NonNull List<T8> ts8)
Creates a `For`-comprehension of 8 Lists.

Type Parameters:
`T1` - component type of the 1st List
`T2` - component type of the 2nd List
`T3` - component type of the 3rd List
`T4` - component type of the 4th List
`T5` - component type of the 5th List
`T6` - component type of the 6th List
`T7` - component type of the 7th List
`T8` - component type of the 8th List
Parameters:
`ts1` - the 1st List
`ts2` - the 2nd List
`ts3` - the 3rd List
`ts4` - the 4th List
`ts5` - the 5th List
`ts6` - the 6th List
`ts7` - the 7th List
`ts8` - the 8th List
Returns:
a new `For`-comprehension of arity 8

  - 

### For

public static <L,
T1> API.For1Either<L,T1> For(@NonNull Either<L,T1> ts1)
Creates a `For`-comprehension of one Either.

Type Parameters:
`L` - left-hand type of all Eithers
`T1` - component type of the 1st Either
Parameters:
`ts1` - the 1st Either
Returns:
a new `For`-comprehension of arity 1

  - 

### For

public static <L,
T1,
T2> API.For2Either<L,T1,T2> For(@NonNull Either<L,T1> ts1,
 @NonNull Either<L,T2> ts2)
Creates a `For`-comprehension of two Eithers.

Type Parameters:
`L` - left-hand type of all Eithers
`T1` - component type of the 1st Either
`T2` - component type of the 2nd Either
Parameters:
`ts1` - the 1st Either
`ts2` - the 2nd Either
Returns:
a new `For`-comprehension of arity 2

  - 

### For

public static <L,
T1,
T2,
T3>
API.For3Either<L,T1,T2,T3> For(@NonNull Either<L,T1> ts1,
 @NonNull Either<L,T2> ts2,
 @NonNull Either<L,T3> ts3)
Creates a `For`-comprehension of three Eithers.

Type Parameters:
`L` - left-hand type of all Eithers
`T1` - component type of the 1st Either
`T2` - component type of the 2nd Either
`T3` - component type of the 3rd Either
Parameters:
`ts1` - the 1st Either
`ts2` - the 2nd Either
`ts3` - the 3rd Either
Returns:
a new `For`-comprehension of arity 3

  - 

### For

public static <L,
T1,
T2,
T3,
T4>
API.For4Either<L,T1,T2,T3,T4> For(@NonNull Either<L,T1> ts1,
 @NonNull Either<L,T2> ts2,
 @NonNull Either<L,T3> ts3,
 @NonNull Either<L,T4> ts4)
Creates a `For`-comprehension of 4 Eithers.

Type Parameters:
`L` - left-hand type of all Eithers
`T1` - component type of the 1st Either
`T2` - component type of the 2nd Either
`T3` - component type of the 3rd Either
`T4` - component type of the 4th Either
Parameters:
`ts1` - the 1st Either
`ts2` - the 2nd Either
`ts3` - the 3rd Either
`ts4` - the 4th Either
Returns:
a new `For`-comprehension of arity 4

  - 

### For

public static <L,
T1,
T2,
T3,
T4,
T5>
API.For5Either<L,T1,T2,T3,T4,T5> For(@NonNull Either<L,T1> ts1,
 @NonNull Either<L,T2> ts2,
 @NonNull Either<L,T3> ts3,
 @NonNull Either<L,T4> ts4,
 @NonNull Either<L,T5> ts5)
Creates a `For`-comprehension of 5 Eithers.

Type Parameters:
`L` - left-hand type of all Eithers
`T1` - component type of the 1st Either
`T2` - component type of the 2nd Either
`T3` - component type of the 3rd Either
`T4` - component type of the 4th Either
`T5` - component type of the 5th Either
Parameters:
`ts1` - the 1st Either
`ts2` - the 2nd Either
`ts3` - the 3rd Either
`ts4` - the 4th Either
`ts5` - the 5th Either
Returns:
a new `For`-comprehension of arity 5

  - 

### For

public static <L,
T1,
T2,
T3,
T4,
T5,
T6>
API.For6Either<L,T1,T2,T3,T4,T5,T6> For(@NonNull Either<L,T1> ts1,
 @NonNull Either<L,T2> ts2,
 @NonNull Either<L,T3> ts3,
 @NonNull Either<L,T4> ts4,
 @NonNull Either<L,T5> ts5,
 @NonNull Either<L,T6> ts6)
Creates a `For`-comprehension of 6 Eithers.

Type Parameters:
`L` - left-hand type of all Eithers
`T1` - component type of the 1st Either
`T2` - component type of the 2nd Either
`T3` - component type of the 3rd Either
`T4` - component type of the 4th Either
`T5` - component type of the 5th Either
`T6` - component type of the 6th Either
Parameters:
`ts1` - the 1st Either
`ts2` - the 2nd Either
`ts3` - the 3rd Either
`ts4` - the 4th Either
`ts5` - the 5th Either
`ts6` - the 6th Either
Returns:
a new `For`-comprehension of arity 6

  - 

### For

public static <L,
T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.For7Either<L,T1,T2,T3,T4,T5,T6,T7> For(@NonNull Either<L,T1> ts1,
 @NonNull Either<L,T2> ts2,
 @NonNull Either<L,T3> ts3,
 @NonNull Either<L,T4> ts4,
 @NonNull Either<L,T5> ts5,
 @NonNull Either<L,T6> ts6,
 @NonNull Either<L,T7> ts7)
Creates a `For`-comprehension of 7 Eithers.

Type Parameters:
`L` - left-hand type of all Eithers
`T1` - component type of the 1st Either
`T2` - component type of the 2nd Either
`T3` - component type of the 3rd Either
`T4` - component type of the 4th Either
`T5` - component type of the 5th Either
`T6` - component type of the 6th Either
`T7` - component type of the 7th Either
Parameters:
`ts1` - the 1st Either
`ts2` - the 2nd Either
`ts3` - the 3rd Either
`ts4` - the 4th Either
`ts5` - the 5th Either
`ts6` - the 6th Either
`ts7` - the 7th Either
Returns:
a new `For`-comprehension of arity 7

  - 

### For

public static <L,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.For8Either<L,T1,T2,T3,T4,T5,T6,T7,T8> For(@NonNull Either<L,T1> ts1,
 @NonNull Either<L,T2> ts2,
 @NonNull Either<L,T3> ts3,
 @NonNull Either<L,T4> ts4,
 @NonNull Either<L,T5> ts5,
 @NonNull Either<L,T6> ts6,
 @NonNull Either<L,T7> ts7,
 @NonNull Either<L,T8> ts8)
Creates a `For`-comprehension of 8 Eithers.

Type Parameters:
`L` - left-hand type of all Eithers
`T1` - component type of the 1st Either
`T2` - component type of the 2nd Either
`T3` - component type of the 3rd Either
`T4` - component type of the 4th Either
`T5` - component type of the 5th Either
`T6` - component type of the 6th Either
`T7` - component type of the 7th Either
`T8` - component type of the 8th Either
Parameters:
`ts1` - the 1st Either
`ts2` - the 2nd Either
`ts3` - the 3rd Either
`ts4` - the 4th Either
`ts5` - the 5th Either
`ts6` - the 6th Either
`ts7` - the 7th Either
`ts8` - the 8th Either
Returns:
a new `For`-comprehension of arity 8

  - 

### For

public static <L,
T1> API.For1Validation<L,T1> For(@NonNull Validation<L,T1> ts1)
Creates a `For`-comprehension of one Validation.

Type Parameters:
`L` - left-hand type of all Validations
`T1` - component type of the 1st Validation
Parameters:
`ts1` - the 1st Validation
Returns:
a new `For`-comprehension of arity 1

  - 

### For

public static <L,
T1,
T2>
API.For2Validation<L,T1,T2> For(@NonNull Validation<L,T1> ts1,
 @NonNull Validation<L,T2> ts2)
Creates a `For`-comprehension of two Validations.

Type Parameters:
`L` - left-hand type of all Validations
`T1` - component type of the 1st Validation
`T2` - component type of the 2nd Validation
Parameters:
`ts1` - the 1st Validation
`ts2` - the 2nd Validation
Returns:
a new `For`-comprehension of arity 2

  - 

### For

public static <L,
T1,
T2,
T3>
API.For3Validation<L,T1,T2,T3> For(@NonNull Validation<L,T1> ts1,
 @NonNull Validation<L,T2> ts2,
 @NonNull Validation<L,T3> ts3)
Creates a `For`-comprehension of three Validations.

Type Parameters:
`L` - left-hand type of all Validations
`T1` - component type of the 1st Validation
`T2` - component type of the 2nd Validation
`T3` - component type of the 3rd Validation
Parameters:
`ts1` - the 1st Validation
`ts2` - the 2nd Validation
`ts3` - the 3rd Validation
Returns:
a new `For`-comprehension of arity 3

  - 

### For

public static <L,
T1,
T2,
T3,
T4>
API.For4Validation<L,T1,T2,T3,T4> For(@NonNull Validation<L,T1> ts1,
 @NonNull Validation<L,T2> ts2,
 @NonNull Validation<L,T3> ts3,
 @NonNull Validation<L,T4> ts4)
Creates a `For`-comprehension of 4 Validations.

Type Parameters:
`L` - left-hand type of all Validations
`T1` - component type of the 1st Validation
`T2` - component type of the 2nd Validation
`T3` - component type of the 3rd Validation
`T4` - component type of the 4th Validation
Parameters:
`ts1` - the 1st Validation
`ts2` - the 2nd Validation
`ts3` - the 3rd Validation
`ts4` - the 4th Validation
Returns:
a new `For`-comprehension of arity 4

  - 

### For

public static <L,
T1,
T2,
T3,
T4,
T5>
API.For5Validation<L,T1,T2,T3,T4,T5> For(@NonNull Validation<L,T1> ts1,
 @NonNull Validation<L,T2> ts2,
 @NonNull Validation<L,T3> ts3,
 @NonNull Validation<L,T4> ts4,
 @NonNull Validation<L,T5> ts5)
Creates a `For`-comprehension of 5 Validations.

Type Parameters:
`L` - left-hand type of all Validations
`T1` - component type of the 1st Validation
`T2` - component type of the 2nd Validation
`T3` - component type of the 3rd Validation
`T4` - component type of the 4th Validation
`T5` - component type of the 5th Validation
Parameters:
`ts1` - the 1st Validation
`ts2` - the 2nd Validation
`ts3` - the 3rd Validation
`ts4` - the 4th Validation
`ts5` - the 5th Validation
Returns:
a new `For`-comprehension of arity 5

  - 

### For

public static <L,
T1,
T2,
T3,
T4,
T5,
T6>
API.For6Validation<L,T1,T2,T3,T4,T5,T6> For(@NonNull Validation<L,T1> ts1,
 @NonNull Validation<L,T2> ts2,
 @NonNull Validation<L,T3> ts3,
 @NonNull Validation<L,T4> ts4,
 @NonNull Validation<L,T5> ts5,
 @NonNull Validation<L,T6> ts6)
Creates a `For`-comprehension of 6 Validations.

Type Parameters:
`L` - left-hand type of all Validations
`T1` - component type of the 1st Validation
`T2` - component type of the 2nd Validation
`T3` - component type of the 3rd Validation
`T4` - component type of the 4th Validation
`T5` - component type of the 5th Validation
`T6` - component type of the 6th Validation
Parameters:
`ts1` - the 1st Validation
`ts2` - the 2nd Validation
`ts3` - the 3rd Validation
`ts4` - the 4th Validation
`ts5` - the 5th Validation
`ts6` - the 6th Validation
Returns:
a new `For`-comprehension of arity 6

  - 

### For

public static <L,
T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.For7Validation<L,T1,T2,T3,T4,T5,T6,T7> For(@NonNull Validation<L,T1> ts1,
 @NonNull Validation<L,T2> ts2,
 @NonNull Validation<L,T3> ts3,
 @NonNull Validation<L,T4> ts4,
 @NonNull Validation<L,T5> ts5,
 @NonNull Validation<L,T6> ts6,
 @NonNull Validation<L,T7> ts7)
Creates a `For`-comprehension of 7 Validations.

Type Parameters:
`L` - left-hand type of all Validations
`T1` - component type of the 1st Validation
`T2` - component type of the 2nd Validation
`T3` - component type of the 3rd Validation
`T4` - component type of the 4th Validation
`T5` - component type of the 5th Validation
`T6` - component type of the 6th Validation
`T7` - component type of the 7th Validation
Parameters:
`ts1` - the 1st Validation
`ts2` - the 2nd Validation
`ts3` - the 3rd Validation
`ts4` - the 4th Validation
`ts5` - the 5th Validation
`ts6` - the 6th Validation
`ts7` - the 7th Validation
Returns:
a new `For`-comprehension of arity 7

  - 

### For

public static <L,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.For8Validation<L,T1,T2,T3,T4,T5,T6,T7,T8> For(@NonNull Validation<L,T1> ts1,
 @NonNull Validation<L,T2> ts2,
 @NonNull Validation<L,T3> ts3,
 @NonNull Validation<L,T4> ts4,
 @NonNull Validation<L,T5> ts5,
 @NonNull Validation<L,T6> ts6,
 @NonNull Validation<L,T7> ts7,
 @NonNull Validation<L,T8> ts8)
Creates a `For`-comprehension of 8 Validations.

Type Parameters:
`L` - left-hand type of all Validations
`T1` - component type of the 1st Validation
`T2` - component type of the 2nd Validation
`T3` - component type of the 3rd Validation
`T4` - component type of the 4th Validation
`T5` - component type of the 5th Validation
`T6` - component type of the 6th Validation
`T7` - component type of the 7th Validation
`T8` - component type of the 8th Validation
Parameters:
`ts1` - the 1st Validation
`ts2` - the 2nd Validation
`ts3` - the 3rd Validation
`ts4` - the 4th Validation
`ts5` - the 5th Validation
`ts6` - the 6th Validation
`ts7` - the 7th Validation
`ts8` - the 8th Validation
Returns:
a new `For`-comprehension of arity 8

  - 

### For

public static <T1,
T2> API.ForLazy2Option<T1,T2> For(@NonNull Option<T1> ts1,
 @NonNull Function1<? super T1,Option<T2>> ts2)
Creates a lazy `For`-comprehension over two Options.

 

The first argument (`ts1`) is the initial Option. Each subsequent
 argument (`ts2` .. `ts2`) is a function that receives all values
 bound so far and returns the next Option. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Option
`T2` - the component type of the 2nd Option
Parameters:
`ts1` - the 1st Option
`ts2` - the 2nd Option
Returns:
a new `ForLazy2Option` builder of arity 2
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3>
API.ForLazy3Option<T1,T2,T3> For(@NonNull Option<T1> ts1,
 @NonNull Function1<? super T1,Option<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Option<T3>> ts3)
Creates a lazy `For`-comprehension over three Options.

 

The first argument (`ts1`) is the initial Option. Each subsequent
 argument (`ts2` .. `ts3`) is a function that receives all values
 bound so far and returns the next Option. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Option
`T2` - the component type of the 2nd Option
`T3` - the component type of the 3rd Option
Parameters:
`ts1` - the 1st Option
`ts2` - the 2nd Option
`ts3` - the 3rd Option
Returns:
a new `ForLazy3Option` builder of arity 3
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4>
API.ForLazy4Option<T1,T2,T3,T4> For(@NonNull Option<T1> ts1,
 @NonNull Function1<? super T1,Option<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Option<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Option<T4>> ts4)
Creates a lazy `For`-comprehension over 4 Options.

 

The first argument (`ts1`) is the initial Option. Each subsequent
 argument (`ts2` .. `ts4`) is a function that receives all values
 bound so far and returns the next Option. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Option
`T2` - the component type of the 2nd Option
`T3` - the component type of the 3rd Option
`T4` - the component type of the 4th Option
Parameters:
`ts1` - the 1st Option
`ts2` - the 2nd Option
`ts3` - the 3rd Option
`ts4` - the 4th Option
Returns:
a new `ForLazy4Option` builder of arity 4
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4,
T5>
API.ForLazy5Option<T1,T2,T3,T4,T5> For(@NonNull Option<T1> ts1,
 @NonNull Function1<? super T1,Option<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Option<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Option<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Option<T5>> ts5)
Creates a lazy `For`-comprehension over 5 Options.

 

The first argument (`ts1`) is the initial Option. Each subsequent
 argument (`ts2` .. `ts5`) is a function that receives all values
 bound so far and returns the next Option. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Option
`T2` - the component type of the 2nd Option
`T3` - the component type of the 3rd Option
`T4` - the component type of the 4th Option
`T5` - the component type of the 5th Option
Parameters:
`ts1` - the 1st Option
`ts2` - the 2nd Option
`ts3` - the 3rd Option
`ts4` - the 4th Option
`ts5` - the 5th Option
Returns:
a new `ForLazy5Option` builder of arity 5
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6>
API.ForLazy6Option<T1,T2,T3,T4,T5,T6> For(@NonNull Option<T1> ts1,
 @NonNull Function1<? super T1,Option<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Option<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Option<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Option<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Option<T6>> ts6)
Creates a lazy `For`-comprehension over 6 Options.

 

The first argument (`ts1`) is the initial Option. Each subsequent
 argument (`ts2` .. `ts6`) is a function that receives all values
 bound so far and returns the next Option. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Option
`T2` - the component type of the 2nd Option
`T3` - the component type of the 3rd Option
`T4` - the component type of the 4th Option
`T5` - the component type of the 5th Option
`T6` - the component type of the 6th Option
Parameters:
`ts1` - the 1st Option
`ts2` - the 2nd Option
`ts3` - the 3rd Option
`ts4` - the 4th Option
`ts5` - the 5th Option
`ts6` - the 6th Option
Returns:
a new `ForLazy6Option` builder of arity 6
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.ForLazy7Option<T1,T2,T3,T4,T5,T6,T7> For(@NonNull Option<T1> ts1,
 @NonNull Function1<? super T1,Option<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Option<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Option<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Option<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Option<T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Option<T7>> ts7)
Creates a lazy `For`-comprehension over 7 Options.

 

The first argument (`ts1`) is the initial Option. Each subsequent
 argument (`ts2` .. `ts7`) is a function that receives all values
 bound so far and returns the next Option. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Option
`T2` - the component type of the 2nd Option
`T3` - the component type of the 3rd Option
`T4` - the component type of the 4th Option
`T5` - the component type of the 5th Option
`T6` - the component type of the 6th Option
`T7` - the component type of the 7th Option
Parameters:
`ts1` - the 1st Option
`ts2` - the 2nd Option
`ts3` - the 3rd Option
`ts4` - the 4th Option
`ts5` - the 5th Option
`ts6` - the 6th Option
`ts7` - the 7th Option
Returns:
a new `ForLazy7Option` builder of arity 7
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.ForLazy8Option<T1,T2,T3,T4,T5,T6,T7,T8> For(@NonNull Option<T1> ts1,
 @NonNull Function1<? super T1,Option<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Option<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Option<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Option<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Option<T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Option<T7>> ts7,
 @NonNull Function7<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,Option<T8>> ts8)
Creates a lazy `For`-comprehension over 8 Options.

 

The first argument (`ts1`) is the initial Option. Each subsequent
 argument (`ts2` .. `ts8`) is a function that receives all values
 bound so far and returns the next Option. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Option
`T2` - the component type of the 2nd Option
`T3` - the component type of the 3rd Option
`T4` - the component type of the 4th Option
`T5` - the component type of the 5th Option
`T6` - the component type of the 6th Option
`T7` - the component type of the 7th Option
`T8` - the component type of the 8th Option
Parameters:
`ts1` - the 1st Option
`ts2` - the 2nd Option
`ts3` - the 3rd Option
`ts4` - the 4th Option
`ts5` - the 5th Option
`ts6` - the 6th Option
`ts7` - the 7th Option
`ts8` - the 8th Option
Returns:
a new `ForLazy8Option` builder of arity 8
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2> API.ForLazy2Future<T1,T2> For(@NonNull Future<T1> ts1,
 @NonNull Function1<? super T1,Future<T2>> ts2)
Creates a lazy `For`-comprehension over two Futures.

 

The first argument (`ts1`) is the initial Future. Each subsequent
 argument (`ts2` .. `ts2`) is a function that receives all values
 bound so far and returns the next Future. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Future
`T2` - the component type of the 2nd Future
Parameters:
`ts1` - the 1st Future
`ts2` - the 2nd Future
Returns:
a new `ForLazy2Future` builder of arity 2
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3>
API.ForLazy3Future<T1,T2,T3> For(@NonNull Future<T1> ts1,
 @NonNull Function1<? super T1,Future<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Future<T3>> ts3)
Creates a lazy `For`-comprehension over three Futures.

 

The first argument (`ts1`) is the initial Future. Each subsequent
 argument (`ts2` .. `ts3`) is a function that receives all values
 bound so far and returns the next Future. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Future
`T2` - the component type of the 2nd Future
`T3` - the component type of the 3rd Future
Parameters:
`ts1` - the 1st Future
`ts2` - the 2nd Future
`ts3` - the 3rd Future
Returns:
a new `ForLazy3Future` builder of arity 3
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4>
API.ForLazy4Future<T1,T2,T3,T4> For(@NonNull Future<T1> ts1,
 @NonNull Function1<? super T1,Future<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Future<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Future<T4>> ts4)
Creates a lazy `For`-comprehension over 4 Futures.

 

The first argument (`ts1`) is the initial Future. Each subsequent
 argument (`ts2` .. `ts4`) is a function that receives all values
 bound so far and returns the next Future. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Future
`T2` - the component type of the 2nd Future
`T3` - the component type of the 3rd Future
`T4` - the component type of the 4th Future
Parameters:
`ts1` - the 1st Future
`ts2` - the 2nd Future
`ts3` - the 3rd Future
`ts4` - the 4th Future
Returns:
a new `ForLazy4Future` builder of arity 4
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4,
T5>
API.ForLazy5Future<T1,T2,T3,T4,T5> For(@NonNull Future<T1> ts1,
 @NonNull Function1<? super T1,Future<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Future<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Future<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Future<T5>> ts5)
Creates a lazy `For`-comprehension over 5 Futures.

 

The first argument (`ts1`) is the initial Future. Each subsequent
 argument (`ts2` .. `ts5`) is a function that receives all values
 bound so far and returns the next Future. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Future
`T2` - the component type of the 2nd Future
`T3` - the component type of the 3rd Future
`T4` - the component type of the 4th Future
`T5` - the component type of the 5th Future
Parameters:
`ts1` - the 1st Future
`ts2` - the 2nd Future
`ts3` - the 3rd Future
`ts4` - the 4th Future
`ts5` - the 5th Future
Returns:
a new `ForLazy5Future` builder of arity 5
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6>
API.ForLazy6Future<T1,T2,T3,T4,T5,T6> For(@NonNull Future<T1> ts1,
 @NonNull Function1<? super T1,Future<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Future<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Future<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Future<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Future<T6>> ts6)
Creates a lazy `For`-comprehension over 6 Futures.

 

The first argument (`ts1`) is the initial Future. Each subsequent
 argument (`ts2` .. `ts6`) is a function that receives all values
 bound so far and returns the next Future. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Future
`T2` - the component type of the 2nd Future
`T3` - the component type of the 3rd Future
`T4` - the component type of the 4th Future
`T5` - the component type of the 5th Future
`T6` - the component type of the 6th Future
Parameters:
`ts1` - the 1st Future
`ts2` - the 2nd Future
`ts3` - the 3rd Future
`ts4` - the 4th Future
`ts5` - the 5th Future
`ts6` - the 6th Future
Returns:
a new `ForLazy6Future` builder of arity 6
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.ForLazy7Future<T1,T2,T3,T4,T5,T6,T7> For(@NonNull Future<T1> ts1,
 @NonNull Function1<? super T1,Future<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Future<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Future<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Future<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Future<T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Future<T7>> ts7)
Creates a lazy `For`-comprehension over 7 Futures.

 

The first argument (`ts1`) is the initial Future. Each subsequent
 argument (`ts2` .. `ts7`) is a function that receives all values
 bound so far and returns the next Future. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Future
`T2` - the component type of the 2nd Future
`T3` - the component type of the 3rd Future
`T4` - the component type of the 4th Future
`T5` - the component type of the 5th Future
`T6` - the component type of the 6th Future
`T7` - the component type of the 7th Future
Parameters:
`ts1` - the 1st Future
`ts2` - the 2nd Future
`ts3` - the 3rd Future
`ts4` - the 4th Future
`ts5` - the 5th Future
`ts6` - the 6th Future
`ts7` - the 7th Future
Returns:
a new `ForLazy7Future` builder of arity 7
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.ForLazy8Future<T1,T2,T3,T4,T5,T6,T7,T8> For(@NonNull Future<T1> ts1,
 @NonNull Function1<? super T1,Future<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Future<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Future<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Future<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Future<T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Future<T7>> ts7,
 @NonNull Function7<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,Future<T8>> ts8)
Creates a lazy `For`-comprehension over 8 Futures.

 

The first argument (`ts1`) is the initial Future. Each subsequent
 argument (`ts2` .. `ts8`) is a function that receives all values
 bound so far and returns the next Future. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Future
`T2` - the component type of the 2nd Future
`T3` - the component type of the 3rd Future
`T4` - the component type of the 4th Future
`T5` - the component type of the 5th Future
`T6` - the component type of the 6th Future
`T7` - the component type of the 7th Future
`T8` - the component type of the 8th Future
Parameters:
`ts1` - the 1st Future
`ts2` - the 2nd Future
`ts3` - the 3rd Future
`ts4` - the 4th Future
`ts5` - the 5th Future
`ts6` - the 6th Future
`ts7` - the 7th Future
`ts8` - the 8th Future
Returns:
a new `ForLazy8Future` builder of arity 8
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2> API.ForLazy2Try<T1,T2> For(@NonNull Try<T1> ts1,
 @NonNull Function1<? super T1,Try<T2>> ts2)
Creates a lazy `For`-comprehension over two Trys.

 

The first argument (`ts1`) is the initial Try. Each subsequent
 argument (`ts2` .. `ts2`) is a function that receives all values
 bound so far and returns the next Try. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Try
`T2` - the component type of the 2nd Try
Parameters:
`ts1` - the 1st Try
`ts2` - the 2nd Try
Returns:
a new `ForLazy2Try` builder of arity 2
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3>
API.ForLazy3Try<T1,T2,T3> For(@NonNull Try<T1> ts1,
 @NonNull Function1<? super T1,Try<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Try<T3>> ts3)
Creates a lazy `For`-comprehension over three Trys.

 

The first argument (`ts1`) is the initial Try. Each subsequent
 argument (`ts2` .. `ts3`) is a function that receives all values
 bound so far and returns the next Try. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Try
`T2` - the component type of the 2nd Try
`T3` - the component type of the 3rd Try
Parameters:
`ts1` - the 1st Try
`ts2` - the 2nd Try
`ts3` - the 3rd Try
Returns:
a new `ForLazy3Try` builder of arity 3
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4>
API.ForLazy4Try<T1,T2,T3,T4> For(@NonNull Try<T1> ts1,
 @NonNull Function1<? super T1,Try<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Try<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Try<T4>> ts4)
Creates a lazy `For`-comprehension over 4 Trys.

 

The first argument (`ts1`) is the initial Try. Each subsequent
 argument (`ts2` .. `ts4`) is a function that receives all values
 bound so far and returns the next Try. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Try
`T2` - the component type of the 2nd Try
`T3` - the component type of the 3rd Try
`T4` - the component type of the 4th Try
Parameters:
`ts1` - the 1st Try
`ts2` - the 2nd Try
`ts3` - the 3rd Try
`ts4` - the 4th Try
Returns:
a new `ForLazy4Try` builder of arity 4
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4,
T5>
API.ForLazy5Try<T1,T2,T3,T4,T5> For(@NonNull Try<T1> ts1,
 @NonNull Function1<? super T1,Try<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Try<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Try<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Try<T5>> ts5)
Creates a lazy `For`-comprehension over 5 Trys.

 

The first argument (`ts1`) is the initial Try. Each subsequent
 argument (`ts2` .. `ts5`) is a function that receives all values
 bound so far and returns the next Try. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Try
`T2` - the component type of the 2nd Try
`T3` - the component type of the 3rd Try
`T4` - the component type of the 4th Try
`T5` - the component type of the 5th Try
Parameters:
`ts1` - the 1st Try
`ts2` - the 2nd Try
`ts3` - the 3rd Try
`ts4` - the 4th Try
`ts5` - the 5th Try
Returns:
a new `ForLazy5Try` builder of arity 5
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6>
API.ForLazy6Try<T1,T2,T3,T4,T5,T6> For(@NonNull Try<T1> ts1,
 @NonNull Function1<? super T1,Try<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Try<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Try<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Try<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Try<T6>> ts6)
Creates a lazy `For`-comprehension over 6 Trys.

 

The first argument (`ts1`) is the initial Try. Each subsequent
 argument (`ts2` .. `ts6`) is a function that receives all values
 bound so far and returns the next Try. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Try
`T2` - the component type of the 2nd Try
`T3` - the component type of the 3rd Try
`T4` - the component type of the 4th Try
`T5` - the component type of the 5th Try
`T6` - the component type of the 6th Try
Parameters:
`ts1` - the 1st Try
`ts2` - the 2nd Try
`ts3` - the 3rd Try
`ts4` - the 4th Try
`ts5` - the 5th Try
`ts6` - the 6th Try
Returns:
a new `ForLazy6Try` builder of arity 6
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.ForLazy7Try<T1,T2,T3,T4,T5,T6,T7> For(@NonNull Try<T1> ts1,
 @NonNull Function1<? super T1,Try<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Try<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Try<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Try<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Try<T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Try<T7>> ts7)
Creates a lazy `For`-comprehension over 7 Trys.

 

The first argument (`ts1`) is the initial Try. Each subsequent
 argument (`ts2` .. `ts7`) is a function that receives all values
 bound so far and returns the next Try. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Try
`T2` - the component type of the 2nd Try
`T3` - the component type of the 3rd Try
`T4` - the component type of the 4th Try
`T5` - the component type of the 5th Try
`T6` - the component type of the 6th Try
`T7` - the component type of the 7th Try
Parameters:
`ts1` - the 1st Try
`ts2` - the 2nd Try
`ts3` - the 3rd Try
`ts4` - the 4th Try
`ts5` - the 5th Try
`ts6` - the 6th Try
`ts7` - the 7th Try
Returns:
a new `ForLazy7Try` builder of arity 7
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.ForLazy8Try<T1,T2,T3,T4,T5,T6,T7,T8> For(@NonNull Try<T1> ts1,
 @NonNull Function1<? super T1,Try<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Try<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Try<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Try<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Try<T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Try<T7>> ts7,
 @NonNull Function7<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,Try<T8>> ts8)
Creates a lazy `For`-comprehension over 8 Trys.

 

The first argument (`ts1`) is the initial Try. Each subsequent
 argument (`ts2` .. `ts8`) is a function that receives all values
 bound so far and returns the next Try. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st Try
`T2` - the component type of the 2nd Try
`T3` - the component type of the 3rd Try
`T4` - the component type of the 4th Try
`T5` - the component type of the 5th Try
`T6` - the component type of the 6th Try
`T7` - the component type of the 7th Try
`T8` - the component type of the 8th Try
Parameters:
`ts1` - the 1st Try
`ts2` - the 2nd Try
`ts3` - the 3rd Try
`ts4` - the 4th Try
`ts5` - the 5th Try
`ts6` - the 6th Try
`ts7` - the 7th Try
`ts8` - the 8th Try
Returns:
a new `ForLazy8Try` builder of arity 8
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2> API.ForLazy2List<T1,T2> For(@NonNull List<T1> ts1,
 @NonNull Function1<? super T1,List<T2>> ts2)
Creates a lazy `For`-comprehension over two Lists.

 

The first argument (`ts1`) is the initial List. Each subsequent
 argument (`ts2` .. `ts2`) is a function that receives all values
 bound so far and returns the next List. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st List
`T2` - the component type of the 2nd List
Parameters:
`ts1` - the 1st List
`ts2` - the 2nd List
Returns:
a new `ForLazy2List` builder of arity 2
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3>
API.ForLazy3List<T1,T2,T3> For(@NonNull List<T1> ts1,
 @NonNull Function1<? super T1,List<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,List<T3>> ts3)
Creates a lazy `For`-comprehension over three Lists.

 

The first argument (`ts1`) is the initial List. Each subsequent
 argument (`ts2` .. `ts3`) is a function that receives all values
 bound so far and returns the next List. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st List
`T2` - the component type of the 2nd List
`T3` - the component type of the 3rd List
Parameters:
`ts1` - the 1st List
`ts2` - the 2nd List
`ts3` - the 3rd List
Returns:
a new `ForLazy3List` builder of arity 3
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4>
API.ForLazy4List<T1,T2,T3,T4> For(@NonNull List<T1> ts1,
 @NonNull Function1<? super T1,List<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,List<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,List<T4>> ts4)
Creates a lazy `For`-comprehension over 4 Lists.

 

The first argument (`ts1`) is the initial List. Each subsequent
 argument (`ts2` .. `ts4`) is a function that receives all values
 bound so far and returns the next List. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st List
`T2` - the component type of the 2nd List
`T3` - the component type of the 3rd List
`T4` - the component type of the 4th List
Parameters:
`ts1` - the 1st List
`ts2` - the 2nd List
`ts3` - the 3rd List
`ts4` - the 4th List
Returns:
a new `ForLazy4List` builder of arity 4
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4,
T5>
API.ForLazy5List<T1,T2,T3,T4,T5> For(@NonNull List<T1> ts1,
 @NonNull Function1<? super T1,List<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,List<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,List<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,List<T5>> ts5)
Creates a lazy `For`-comprehension over 5 Lists.

 

The first argument (`ts1`) is the initial List. Each subsequent
 argument (`ts2` .. `ts5`) is a function that receives all values
 bound so far and returns the next List. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st List
`T2` - the component type of the 2nd List
`T3` - the component type of the 3rd List
`T4` - the component type of the 4th List
`T5` - the component type of the 5th List
Parameters:
`ts1` - the 1st List
`ts2` - the 2nd List
`ts3` - the 3rd List
`ts4` - the 4th List
`ts5` - the 5th List
Returns:
a new `ForLazy5List` builder of arity 5
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6>
API.ForLazy6List<T1,T2,T3,T4,T5,T6> For(@NonNull List<T1> ts1,
 @NonNull Function1<? super T1,List<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,List<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,List<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,List<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,List<T6>> ts6)
Creates a lazy `For`-comprehension over 6 Lists.

 

The first argument (`ts1`) is the initial List. Each subsequent
 argument (`ts2` .. `ts6`) is a function that receives all values
 bound so far and returns the next List. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st List
`T2` - the component type of the 2nd List
`T3` - the component type of the 3rd List
`T4` - the component type of the 4th List
`T5` - the component type of the 5th List
`T6` - the component type of the 6th List
Parameters:
`ts1` - the 1st List
`ts2` - the 2nd List
`ts3` - the 3rd List
`ts4` - the 4th List
`ts5` - the 5th List
`ts6` - the 6th List
Returns:
a new `ForLazy6List` builder of arity 6
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.ForLazy7List<T1,T2,T3,T4,T5,T6,T7> For(@NonNull List<T1> ts1,
 @NonNull Function1<? super T1,List<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,List<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,List<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,List<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,List<T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,List<T7>> ts7)
Creates a lazy `For`-comprehension over 7 Lists.

 

The first argument (`ts1`) is the initial List. Each subsequent
 argument (`ts2` .. `ts7`) is a function that receives all values
 bound so far and returns the next List. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st List
`T2` - the component type of the 2nd List
`T3` - the component type of the 3rd List
`T4` - the component type of the 4th List
`T5` - the component type of the 5th List
`T6` - the component type of the 6th List
`T7` - the component type of the 7th List
Parameters:
`ts1` - the 1st List
`ts2` - the 2nd List
`ts3` - the 3rd List
`ts4` - the 4th List
`ts5` - the 5th List
`ts6` - the 6th List
`ts7` - the 7th List
Returns:
a new `ForLazy7List` builder of arity 7
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.ForLazy8List<T1,T2,T3,T4,T5,T6,T7,T8> For(@NonNull List<T1> ts1,
 @NonNull Function1<? super T1,List<T2>> ts2,
 @NonNull Function2<? super T1,? super T2,List<T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,List<T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,List<T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,List<T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,List<T7>> ts7,
 @NonNull Function7<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,List<T8>> ts8)
Creates a lazy `For`-comprehension over 8 Lists.

 

The first argument (`ts1`) is the initial List. Each subsequent
 argument (`ts2` .. `ts8`) is a function that receives all values
 bound so far and returns the next List. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`T1` - the component type of the 1st List
`T2` - the component type of the 2nd List
`T3` - the component type of the 3rd List
`T4` - the component type of the 4th List
`T5` - the component type of the 5th List
`T6` - the component type of the 6th List
`T7` - the component type of the 7th List
`T8` - the component type of the 8th List
Parameters:
`ts1` - the 1st List
`ts2` - the 2nd List
`ts3` - the 3rd List
`ts4` - the 4th List
`ts5` - the 5th List
`ts6` - the 6th List
`ts7` - the 7th List
`ts8` - the 8th List
Returns:
a new `ForLazy8List` builder of arity 8
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <L,
T1,
T2>
API.ForLazy2Either<L,T1,T2> For(@NonNull Either<L,T1> ts1,
 @NonNull Function1<? super T1,Either<L,T2>> ts2)
Creates a lazy `For`-comprehension over two Eithers.

 

The first argument (`ts1`) is the initial Either. Each subsequent
 argument (`ts2` .. `ts2`) is a function that receives all values
 bound so far and returns the next Either. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`L` - the common left-hand type of all Eithers
`T1` - the component type of the 1st Either
`T2` - the component type of the 2nd Either
Parameters:
`ts1` - the 1st Either
`ts2` - the 2nd Either
Returns:
a new `ForLazy2Either` builder of arity 2
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <L,
T1,
T2,
T3>
API.ForLazy3Either<L,T1,T2,T3> For(@NonNull Either<L,T1> ts1,
 @NonNull Function1<? super T1,Either<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Either<L,T3>> ts3)
Creates a lazy `For`-comprehension over three Eithers.

 

The first argument (`ts1`) is the initial Either. Each subsequent
 argument (`ts2` .. `ts3`) is a function that receives all values
 bound so far and returns the next Either. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`L` - the common left-hand type of all Eithers
`T1` - the component type of the 1st Either
`T2` - the component type of the 2nd Either
`T3` - the component type of the 3rd Either
Parameters:
`ts1` - the 1st Either
`ts2` - the 2nd Either
`ts3` - the 3rd Either
Returns:
a new `ForLazy3Either` builder of arity 3
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <L,
T1,
T2,
T3,
T4>
API.ForLazy4Either<L,T1,T2,T3,T4> For(@NonNull Either<L,T1> ts1,
 @NonNull Function1<? super T1,Either<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Either<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Either<L,T4>> ts4)
Creates a lazy `For`-comprehension over 4 Eithers.

 

The first argument (`ts1`) is the initial Either. Each subsequent
 argument (`ts2` .. `ts4`) is a function that receives all values
 bound so far and returns the next Either. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`L` - the common left-hand type of all Eithers
`T1` - the component type of the 1st Either
`T2` - the component type of the 2nd Either
`T3` - the component type of the 3rd Either
`T4` - the component type of the 4th Either
Parameters:
`ts1` - the 1st Either
`ts2` - the 2nd Either
`ts3` - the 3rd Either
`ts4` - the 4th Either
Returns:
a new `ForLazy4Either` builder of arity 4
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <L,
T1,
T2,
T3,
T4,
T5>
API.ForLazy5Either<L,T1,T2,T3,T4,T5> For(@NonNull Either<L,T1> ts1,
 @NonNull Function1<? super T1,Either<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Either<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Either<L,T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Either<L,T5>> ts5)
Creates a lazy `For`-comprehension over 5 Eithers.

 

The first argument (`ts1`) is the initial Either. Each subsequent
 argument (`ts2` .. `ts5`) is a function that receives all values
 bound so far and returns the next Either. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`L` - the common left-hand type of all Eithers
`T1` - the component type of the 1st Either
`T2` - the component type of the 2nd Either
`T3` - the component type of the 3rd Either
`T4` - the component type of the 4th Either
`T5` - the component type of the 5th Either
Parameters:
`ts1` - the 1st Either
`ts2` - the 2nd Either
`ts3` - the 3rd Either
`ts4` - the 4th Either
`ts5` - the 5th Either
Returns:
a new `ForLazy5Either` builder of arity 5
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <L,
T1,
T2,
T3,
T4,
T5,
T6>
API.ForLazy6Either<L,T1,T2,T3,T4,T5,T6> For(@NonNull Either<L,T1> ts1,
 @NonNull Function1<? super T1,Either<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Either<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Either<L,T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Either<L,T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Either<L,T6>> ts6)
Creates a lazy `For`-comprehension over 6 Eithers.

 

The first argument (`ts1`) is the initial Either. Each subsequent
 argument (`ts2` .. `ts6`) is a function that receives all values
 bound so far and returns the next Either. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`L` - the common left-hand type of all Eithers
`T1` - the component type of the 1st Either
`T2` - the component type of the 2nd Either
`T3` - the component type of the 3rd Either
`T4` - the component type of the 4th Either
`T5` - the component type of the 5th Either
`T6` - the component type of the 6th Either
Parameters:
`ts1` - the 1st Either
`ts2` - the 2nd Either
`ts3` - the 3rd Either
`ts4` - the 4th Either
`ts5` - the 5th Either
`ts6` - the 6th Either
Returns:
a new `ForLazy6Either` builder of arity 6
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <L,
T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.ForLazy7Either<L,T1,T2,T3,T4,T5,T6,T7> For(@NonNull Either<L,T1> ts1,
 @NonNull Function1<? super T1,Either<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Either<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Either<L,T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Either<L,T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Either<L,T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Either<L,T7>> ts7)
Creates a lazy `For`-comprehension over 7 Eithers.

 

The first argument (`ts1`) is the initial Either. Each subsequent
 argument (`ts2` .. `ts7`) is a function that receives all values
 bound so far and returns the next Either. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`L` - the common left-hand type of all Eithers
`T1` - the component type of the 1st Either
`T2` - the component type of the 2nd Either
`T3` - the component type of the 3rd Either
`T4` - the component type of the 4th Either
`T5` - the component type of the 5th Either
`T6` - the component type of the 6th Either
`T7` - the component type of the 7th Either
Parameters:
`ts1` - the 1st Either
`ts2` - the 2nd Either
`ts3` - the 3rd Either
`ts4` - the 4th Either
`ts5` - the 5th Either
`ts6` - the 6th Either
`ts7` - the 7th Either
Returns:
a new `ForLazy7Either` builder of arity 7
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <L,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.ForLazy8Either<L,T1,T2,T3,T4,T5,T6,T7,T8> For(@NonNull Either<L,T1> ts1,
 @NonNull Function1<? super T1,Either<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Either<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Either<L,T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Either<L,T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Either<L,T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Either<L,T7>> ts7,
 @NonNull Function7<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,Either<L,T8>> ts8)
Creates a lazy `For`-comprehension over 8 Eithers.

 

The first argument (`ts1`) is the initial Either. Each subsequent
 argument (`ts2` .. `ts8`) is a function that receives all values
 bound so far and returns the next Either. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`L` - the common left-hand type of all Eithers
`T1` - the component type of the 1st Either
`T2` - the component type of the 2nd Either
`T3` - the component type of the 3rd Either
`T4` - the component type of the 4th Either
`T5` - the component type of the 5th Either
`T6` - the component type of the 6th Either
`T7` - the component type of the 7th Either
`T8` - the component type of the 8th Either
Parameters:
`ts1` - the 1st Either
`ts2` - the 2nd Either
`ts3` - the 3rd Either
`ts4` - the 4th Either
`ts5` - the 5th Either
`ts6` - the 6th Either
`ts7` - the 7th Either
`ts8` - the 8th Either
Returns:
a new `ForLazy8Either` builder of arity 8
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <L,
T1,
T2>
API.ForLazy2Validation<L,T1,T2> For(@NonNull Validation<L,T1> ts1,
 @NonNull Function1<? super T1,Validation<L,T2>> ts2)
Creates a lazy `For`-comprehension over two Validations.

 

The first argument (`ts1`) is the initial Validation. Each subsequent
 argument (`ts2` .. `ts2`) is a function that receives all values
 bound so far and returns the next Validation. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`L` - the common left-hand type of all Validations
`T1` - the component type of the 1st Validation
`T2` - the component type of the 2nd Validation
Parameters:
`ts1` - the 1st Validation
`ts2` - the 2nd Validation
Returns:
a new `ForLazy2Validation` builder of arity 2
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <L,
T1,
T2,
T3>
API.ForLazy3Validation<L,T1,T2,T3> For(@NonNull Validation<L,T1> ts1,
 @NonNull Function1<? super T1,Validation<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Validation<L,T3>> ts3)
Creates a lazy `For`-comprehension over three Validations.

 

The first argument (`ts1`) is the initial Validation. Each subsequent
 argument (`ts2` .. `ts3`) is a function that receives all values
 bound so far and returns the next Validation. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`L` - the common left-hand type of all Validations
`T1` - the component type of the 1st Validation
`T2` - the component type of the 2nd Validation
`T3` - the component type of the 3rd Validation
Parameters:
`ts1` - the 1st Validation
`ts2` - the 2nd Validation
`ts3` - the 3rd Validation
Returns:
a new `ForLazy3Validation` builder of arity 3
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <L,
T1,
T2,
T3,
T4>
API.ForLazy4Validation<L,T1,T2,T3,T4> For(@NonNull Validation<L,T1> ts1,
 @NonNull Function1<? super T1,Validation<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Validation<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Validation<L,T4>> ts4)
Creates a lazy `For`-comprehension over 4 Validations.

 

The first argument (`ts1`) is the initial Validation. Each subsequent
 argument (`ts2` .. `ts4`) is a function that receives all values
 bound so far and returns the next Validation. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`L` - the common left-hand type of all Validations
`T1` - the component type of the 1st Validation
`T2` - the component type of the 2nd Validation
`T3` - the component type of the 3rd Validation
`T4` - the component type of the 4th Validation
Parameters:
`ts1` - the 1st Validation
`ts2` - the 2nd Validation
`ts3` - the 3rd Validation
`ts4` - the 4th Validation
Returns:
a new `ForLazy4Validation` builder of arity 4
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <L,
T1,
T2,
T3,
T4,
T5>
API.ForLazy5Validation<L,T1,T2,T3,T4,T5> For(@NonNull Validation<L,T1> ts1,
 @NonNull Function1<? super T1,Validation<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Validation<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Validation<L,T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Validation<L,T5>> ts5)
Creates a lazy `For`-comprehension over 5 Validations.

 

The first argument (`ts1`) is the initial Validation. Each subsequent
 argument (`ts2` .. `ts5`) is a function that receives all values
 bound so far and returns the next Validation. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`L` - the common left-hand type of all Validations
`T1` - the component type of the 1st Validation
`T2` - the component type of the 2nd Validation
`T3` - the component type of the 3rd Validation
`T4` - the component type of the 4th Validation
`T5` - the component type of the 5th Validation
Parameters:
`ts1` - the 1st Validation
`ts2` - the 2nd Validation
`ts3` - the 3rd Validation
`ts4` - the 4th Validation
`ts5` - the 5th Validation
Returns:
a new `ForLazy5Validation` builder of arity 5
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <L,
T1,
T2,
T3,
T4,
T5,
T6>
API.ForLazy6Validation<L,T1,T2,T3,T4,T5,T6> For(@NonNull Validation<L,T1> ts1,
 @NonNull Function1<? super T1,Validation<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Validation<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Validation<L,T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Validation<L,T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Validation<L,T6>> ts6)
Creates a lazy `For`-comprehension over 6 Validations.

 

The first argument (`ts1`) is the initial Validation. Each subsequent
 argument (`ts2` .. `ts6`) is a function that receives all values
 bound so far and returns the next Validation. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`L` - the common left-hand type of all Validations
`T1` - the component type of the 1st Validation
`T2` - the component type of the 2nd Validation
`T3` - the component type of the 3rd Validation
`T4` - the component type of the 4th Validation
`T5` - the component type of the 5th Validation
`T6` - the component type of the 6th Validation
Parameters:
`ts1` - the 1st Validation
`ts2` - the 2nd Validation
`ts3` - the 3rd Validation
`ts4` - the 4th Validation
`ts5` - the 5th Validation
`ts6` - the 6th Validation
Returns:
a new `ForLazy6Validation` builder of arity 6
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <L,
T1,
T2,
T3,
T4,
T5,
T6,
T7>
API.ForLazy7Validation<L,T1,T2,T3,T4,T5,T6,T7> For(@NonNull Validation<L,T1> ts1,
 @NonNull Function1<? super T1,Validation<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Validation<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Validation<L,T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Validation<L,T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Validation<L,T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Validation<L,T7>> ts7)
Creates a lazy `For`-comprehension over 7 Validations.

 

The first argument (`ts1`) is the initial Validation. Each subsequent
 argument (`ts2` .. `ts7`) is a function that receives all values
 bound so far and returns the next Validation. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`L` - the common left-hand type of all Validations
`T1` - the component type of the 1st Validation
`T2` - the component type of the 2nd Validation
`T3` - the component type of the 3rd Validation
`T4` - the component type of the 4th Validation
`T5` - the component type of the 5th Validation
`T6` - the component type of the 6th Validation
`T7` - the component type of the 7th Validation
Parameters:
`ts1` - the 1st Validation
`ts2` - the 2nd Validation
`ts3` - the 3rd Validation
`ts4` - the 4th Validation
`ts5` - the 5th Validation
`ts6` - the 6th Validation
`ts7` - the 7th Validation
Returns:
a new `ForLazy7Validation` builder of arity 7
Throws:
`NullPointerException` - if any argument is `null`

  - 

### For

public static <L,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8>
API.ForLazy8Validation<L,T1,T2,T3,T4,T5,T6,T7,T8> For(@NonNull Validation<L,T1> ts1,
 @NonNull Function1<? super T1,Validation<L,T2>> ts2,
 @NonNull Function2<? super T1,? super T2,Validation<L,T3>> ts3,
 @NonNull Function3<? super T1,? super T2,? super T3,Validation<L,T4>> ts4,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,Validation<L,T5>> ts5,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,Validation<L,T6>> ts6,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,Validation<L,T7>> ts7,
 @NonNull Function7<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,Validation<L,T8>> ts8)
Creates a lazy `For`-comprehension over 8 Validations.

 

The first argument (`ts1`) is the initial Validation. Each subsequent
 argument (`ts2` .. `ts8`) is a function that receives all values
 bound so far and returns the next Validation. This method only constructs the
 lazy comprehension; underlying effects are evaluated when `yield(...)`
 is invoked.

Type Parameters:
`L` - the common left-hand type of all Validations
`T1` - the component type of the 1st Validation
`T2` - the component type of the 2nd Validation
`T3` - the component type of the 3rd Validation
`T4` - the component type of the 4th Validation
`T5` - the component type of the 5th Validation
`T6` - the component type of the 6th Validation
`T7` - the component type of the 7th Validation
`T8` - the component type of the 8th Validation
Parameters:
`ts1` - the 1st Validation
`ts2` - the 2nd Validation
`ts3` - the 3rd Validation
`ts4` - the 4th Validation
`ts5` - the 5th Validation
`ts6` - the 6th Validation
`ts7` - the 7th Validation
`ts8` - the 8th Validation
Returns:
a new `ForLazy8Validation` builder of arity 8
Throws:
`NullPointerException` - if any argument is `null`

  - 

### Match

@GwtIncompatible
public static <T> API.Match<T> Match(T value)
Entry point of the match API.

Type Parameters:
`T` - type of the value
Parameters:
`value` - a value to be matched
Returns:
a new `Match` instance

  - 

### Case

@GwtIncompatible
public static <T,
R> API.Match.Case<T,R> Case(@NonNull API.Match.Pattern0<T> pattern,
 @NonNull Function<? super T,? extends R> f)
Returns a `API.Match.Case0` instance for a specific `API.Match.Pattern0` and `Function`

Type Parameters:
`T` - Type of the value being matched
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`f` - Matched value consumer
Returns:
new Case0

  - 

### Case

@GwtIncompatible
public static <T,
R> API.Match.Case<T,R> Case(@NonNull API.Match.Pattern0<T> pattern,
 @NonNull Supplier<? extends R> supplier)
Returns a `API.Match.Case0` instance for a specific `API.Match.Pattern0` and `Supplier`

Type Parameters:
`T` - Type of the value being matched
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`supplier` - Matched value supplier
Returns:
new Case0

  - 

### Case

@GwtIncompatible
public static <T,
R> API.Match.Case<T,R> Case(@NonNull API.Match.Pattern0<T> pattern,
 R retVal)
Returns a `API.Match.Case0` instance for a specific `API.Match.Pattern0` and a constant value

Type Parameters:
`T` - Type of the value being matched
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`retVal` - Constant value to return
Returns:
new Case0

  - 

### Case

@GwtIncompatible
public static <T,
T1,
R> API.Match.Case<T,R> Case(@NonNull API.Match.Pattern1<T,T1> pattern,
 @NonNull Function<? super T1,? extends R> f)
Returns a `API.Match.Case1` instance for a specific `API.Match.Pattern1` and `Function`

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`f` - Matched value consumer
Returns:
new Case1

  - 

### Case

@GwtIncompatible
public static <T,
T1,
R> API.Match.Case<T,R> Case(@NonNull API.Match.Pattern1<T,T1> pattern,
 @NonNull Supplier<? extends R> supplier)
Returns a `API.Match.Case1` instance for a specific `API.Match.Pattern1` and `Supplier`

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`supplier` - Matched value supplier
Returns:
new Case1

  - 

### Case

@GwtIncompatible
public static <T,
T1,
R> API.Match.Case<T,R> Case(@NonNull API.Match.Pattern1<T,T1> pattern,
 R retVal)
Returns a `API.Match.Case1` instance for a specific `API.Match.Pattern1` and a constant value

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`retVal` - Constant value to return
Returns:
new Case1

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
R> API.Match.Case<T,R> Case(@NonNull API.Match.Pattern2<T,T1,T2> pattern,
 @NonNull BiFunction<? super T1,? super T2,? extends R> f)
Returns a `API.Match.Case2` instance for a specific `API.Match.Pattern2` and `BiFunction`

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`f` - Matched value consumer
Returns:
new Case2

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
R> API.Match.Case<T,R> Case(@NonNull API.Match.Pattern2<T,T1,T2> pattern,
 @NonNull Supplier<? extends R> supplier)
Returns a `API.Match.Case2` instance for a specific `API.Match.Pattern2` and `Supplier`

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`supplier` - Matched value supplier
Returns:
new Case2

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
R> API.Match.Case<T,R> Case(@NonNull API.Match.Pattern2<T,T1,T2> pattern,
 R retVal)
Returns a `API.Match.Case2` instance for a specific `API.Match.Pattern2` and a constant value

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`retVal` - Constant value to return
Returns:
new Case2

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
T3,
R>
API.Match.Case<T,R> Case(@NonNull API.Match.Pattern3<T,T1,T2,T3> pattern,
 @NonNull Function3<? super T1,? super T2,? super T3,? extends R> f)
Returns a `API.Match.Case3` instance for a specific `API.Match.Pattern3` and `Function3`

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`T3` - Intermediate type 3 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`f` - Matched value consumer
Returns:
new Case3

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
T3,
R>
API.Match.Case<T,R> Case(@NonNull API.Match.Pattern3<T,T1,T2,T3> pattern,
 @NonNull Supplier<? extends R> supplier)
Returns a `API.Match.Case3` instance for a specific `API.Match.Pattern3` and `Supplier`

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`T3` - Intermediate type 3 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`supplier` - Matched value supplier
Returns:
new Case3

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
T3,
R>
API.Match.Case<T,R> Case(@NonNull API.Match.Pattern3<T,T1,T2,T3> pattern,
 R retVal)
Returns a `API.Match.Case3` instance for a specific `API.Match.Pattern3` and a constant value

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`T3` - Intermediate type 3 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`retVal` - Constant value to return
Returns:
new Case3

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
T3,
T4,
R>
API.Match.Case<T,R> Case(@NonNull API.Match.Pattern4<T,T1,T2,T3,T4> pattern,
 @NonNull Function4<? super T1,? super T2,? super T3,? super T4,? extends R> f)
Returns a `API.Match.Case4` instance for a specific `API.Match.Pattern4` and `Function4`

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`T3` - Intermediate type 3 for the pattern
`T4` - Intermediate type 4 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`f` - Matched value consumer
Returns:
new Case4

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
T3,
T4,
R>
API.Match.Case<T,R> Case(@NonNull API.Match.Pattern4<T,T1,T2,T3,T4> pattern,
 @NonNull Supplier<? extends R> supplier)
Returns a `API.Match.Case4` instance for a specific `API.Match.Pattern4` and `Supplier`

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`T3` - Intermediate type 3 for the pattern
`T4` - Intermediate type 4 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`supplier` - Matched value supplier
Returns:
new Case4

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
T3,
T4,
R>
API.Match.Case<T,R> Case(@NonNull API.Match.Pattern4<T,T1,T2,T3,T4> pattern,
 R retVal)
Returns a `API.Match.Case4` instance for a specific `API.Match.Pattern4` and a constant value

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`T3` - Intermediate type 3 for the pattern
`T4` - Intermediate type 4 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`retVal` - Constant value to return
Returns:
new Case4

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
T3,
T4,
T5,
R>
API.Match.Case<T,R> Case(@NonNull API.Match.Pattern5<T,T1,T2,T3,T4,T5> pattern,
 @NonNull Function5<? super T1,? super T2,? super T3,? super T4,? super T5,? extends R> f)
Returns a `API.Match.Case5` instance for a specific `API.Match.Pattern5` and `Function5`

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`T3` - Intermediate type 3 for the pattern
`T4` - Intermediate type 4 for the pattern
`T5` - Intermediate type 5 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`f` - Matched value consumer
Returns:
new Case5

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
T3,
T4,
T5,
R>
API.Match.Case<T,R> Case(@NonNull API.Match.Pattern5<T,T1,T2,T3,T4,T5> pattern,
 @NonNull Supplier<? extends R> supplier)
Returns a `API.Match.Case5` instance for a specific `API.Match.Pattern5` and `Supplier`

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`T3` - Intermediate type 3 for the pattern
`T4` - Intermediate type 4 for the pattern
`T5` - Intermediate type 5 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`supplier` - Matched value supplier
Returns:
new Case5

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
T3,
T4,
T5,
R>
API.Match.Case<T,R> Case(@NonNull API.Match.Pattern5<T,T1,T2,T3,T4,T5> pattern,
 R retVal)
Returns a `API.Match.Case5` instance for a specific `API.Match.Pattern5` and a constant value

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`T3` - Intermediate type 3 for the pattern
`T4` - Intermediate type 4 for the pattern
`T5` - Intermediate type 5 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`retVal` - Constant value to return
Returns:
new Case5

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
T3,
T4,
T5,
T6,
R>
API.Match.Case<T,R> Case(@NonNull API.Match.Pattern6<T,T1,T2,T3,T4,T5,T6> pattern,
 @NonNull Function6<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? extends R> f)
Returns a `API.Match.Case6` instance for a specific `API.Match.Pattern6` and `Function6`

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`T3` - Intermediate type 3 for the pattern
`T4` - Intermediate type 4 for the pattern
`T5` - Intermediate type 5 for the pattern
`T6` - Intermediate type 6 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`f` - Matched value consumer
Returns:
new Case6

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
T3,
T4,
T5,
T6,
R>
API.Match.Case<T,R> Case(@NonNull API.Match.Pattern6<T,T1,T2,T3,T4,T5,T6> pattern,
 @NonNull Supplier<? extends R> supplier)
Returns a `API.Match.Case6` instance for a specific `API.Match.Pattern6` and `Supplier`

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`T3` - Intermediate type 3 for the pattern
`T4` - Intermediate type 4 for the pattern
`T5` - Intermediate type 5 for the pattern
`T6` - Intermediate type 6 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`supplier` - Matched value supplier
Returns:
new Case6

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
T3,
T4,
T5,
T6,
R>
API.Match.Case<T,R> Case(@NonNull API.Match.Pattern6<T,T1,T2,T3,T4,T5,T6> pattern,
 R retVal)
Returns a `API.Match.Case6` instance for a specific `API.Match.Pattern6` and a constant value

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`T3` - Intermediate type 3 for the pattern
`T4` - Intermediate type 4 for the pattern
`T5` - Intermediate type 5 for the pattern
`T6` - Intermediate type 6 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`retVal` - Constant value to return
Returns:
new Case6

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
R>
API.Match.Case<T,R> Case(@NonNull API.Match.Pattern7<T,T1,T2,T3,T4,T5,T6,T7> pattern,
 @NonNull Function7<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,? extends R> f)
Returns a `API.Match.Case7` instance for a specific `API.Match.Pattern7` and `Function7`

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`T3` - Intermediate type 3 for the pattern
`T4` - Intermediate type 4 for the pattern
`T5` - Intermediate type 5 for the pattern
`T6` - Intermediate type 6 for the pattern
`T7` - Intermediate type 7 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`f` - Matched value consumer
Returns:
new Case7

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
R>
API.Match.Case<T,R> Case(@NonNull API.Match.Pattern7<T,T1,T2,T3,T4,T5,T6,T7> pattern,
 @NonNull Supplier<? extends R> supplier)
Returns a `API.Match.Case7` instance for a specific `API.Match.Pattern7` and `Supplier`

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`T3` - Intermediate type 3 for the pattern
`T4` - Intermediate type 4 for the pattern
`T5` - Intermediate type 5 for the pattern
`T6` - Intermediate type 6 for the pattern
`T7` - Intermediate type 7 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`supplier` - Matched value supplier
Returns:
new Case7

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
R>
API.Match.Case<T,R> Case(@NonNull API.Match.Pattern7<T,T1,T2,T3,T4,T5,T6,T7> pattern,
 R retVal)
Returns a `API.Match.Case7` instance for a specific `API.Match.Pattern7` and a constant value

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`T3` - Intermediate type 3 for the pattern
`T4` - Intermediate type 4 for the pattern
`T5` - Intermediate type 5 for the pattern
`T6` - Intermediate type 6 for the pattern
`T7` - Intermediate type 7 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`retVal` - Constant value to return
Returns:
new Case7

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8,
R>
API.Match.Case<T,R> Case(@NonNull API.Match.Pattern8<T,T1,T2,T3,T4,T5,T6,T7,T8> pattern,
 @NonNull Function8<? super T1,? super T2,? super T3,? super T4,? super T5,? super T6,? super T7,? super T8,? extends R> f)
Returns a `API.Match.Case8` instance for a specific `API.Match.Pattern8` and `Function8`

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`T3` - Intermediate type 3 for the pattern
`T4` - Intermediate type 4 for the pattern
`T5` - Intermediate type 5 for the pattern
`T6` - Intermediate type 6 for the pattern
`T7` - Intermediate type 7 for the pattern
`T8` - Intermediate type 8 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`f` - Matched value consumer
Returns:
new Case8

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8,
R>
API.Match.Case<T,R> Case(@NonNull API.Match.Pattern8<T,T1,T2,T3,T4,T5,T6,T7,T8> pattern,
 @NonNull Supplier<? extends R> supplier)
Returns a `API.Match.Case8` instance for a specific `API.Match.Pattern8` and `Supplier`

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`T3` - Intermediate type 3 for the pattern
`T4` - Intermediate type 4 for the pattern
`T5` - Intermediate type 5 for the pattern
`T6` - Intermediate type 6 for the pattern
`T7` - Intermediate type 7 for the pattern
`T8` - Intermediate type 8 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`supplier` - Matched value supplier
Returns:
new Case8

  - 

### Case

@GwtIncompatible
public static <T,
T1,
T2,
T3,
T4,
T5,
T6,
T7,
T8,
R>
API.Match.Case<T,R> Case(@NonNull API.Match.Pattern8<T,T1,T2,T3,T4,T5,T6,T7,T8> pattern,
 R retVal)
Returns a `API.Match.Case8` instance for a specific `API.Match.Pattern8` and a constant value

Type Parameters:
`T` - Type of the value being matched
`T1` - Intermediate type 1 for the pattern
`T2` - Intermediate type 2 for the pattern
`T3` - Intermediate type 3 for the pattern
`T4` - Intermediate type 4 for the pattern
`T5` - Intermediate type 5 for the pattern
`T6` - Intermediate type 6 for the pattern
`T7` - Intermediate type 7 for the pattern
`T8` - Intermediate type 8 for the pattern
`R` - Return value type
Parameters:
`pattern` - Pattern to match
`retVal` - Constant value to return
Returns:
new Case8

  - 

### $

@GwtIncompatible
public static <T> API.Match.Pattern0<T> $()
Wildcard pattern, matches any value.

Type Parameters:
`T` - injected type of the underlying value
Returns:
a new `Pattern0` instance

  - 

### $

@GwtIncompatible
public static <T> API.Match.Pattern0<T> $(T prototype)
Value pattern, checks for equality.

Type Parameters:
`T` - type of the prototype
Parameters:
`prototype` - the value that should be equal to the underlying object
Returns:
a new `Pattern0` instance

  - 

### $

@GwtIncompatible
public static <T> API.Match.Pattern0<T> $(@NonNull Predicate<? super T> predicate)
Guard pattern, checks if a predicate is satisfied.
 

 This method is intended to be used with lambdas and method references, for example:

 

```

 String evenOrOdd(int num) {
     return Match(num).of(
             Case($(i -> i % 2 == 0), "even"),
             Case($(this::isOdd), "odd")
     );
 }

 boolean isOdd(int i) {
     return i % 2 == 1;
 }
 
```

 It is also valid to pass `Predicate` instances:

 

```

 Predicate<Integer> isOdd = i -> i % 2 == 1;

 Match(num).of(
         Case($(i -> i % 2 == 0), "even"),
         Case($(isOdd), "odd")
 );
 
```

 **Note:** Please take care when matching `Predicate` instances. In general,
 function equality
 is an undecidable problem in computer science. In Vavr we are only able to check,
 if two functions are the same instance.
 

 However, this code will fail:

 

```

 Predicate<Integer> p = i -> true;
 Match(p).of(
     Case($(p), 1) // WRONG! It calls $(Predicate)
 );
 
```

 Instead we have to use `Predicates.is(Object)`:

 

```

 Predicate<Integer> p = i -> true;
 Match(p).of(
     Case($(is(p)), 1) // CORRECT! It calls $(T)
 );
 
```

Type Parameters:
`T` - type of the prototype
Parameters:
`predicate` - the predicate that tests a given value
Returns:
a new `Pattern0` instance