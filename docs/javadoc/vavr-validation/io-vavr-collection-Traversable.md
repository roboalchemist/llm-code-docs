Package io.vavr.collection

# Interface Traversable<T>

Type Parameters:
`T` - the type of elements contained in this Traversable

All Superinterfaces:
`Foldable<T>`, `Iterable<T>`, `Value<T>`

All Known Subinterfaces:
`BitSet<T>`, `IndexedSeq<T>`, `Iterator<T>`, `LinearSeq<T>`, `List<T>`, `Map<K,V>`, `Multimap<K,V>`, `Seq<T>`, `Set<T>`, `SortedMap<K,V>`, `SortedMultimap<K,V>`, `SortedSet<T>`, `Stream<T>`, `Tree<T>`

All Known Implementing Classes:
`Array`, `CharSeq`, `HashMap`, `HashMultimap`, `HashSet`, `LinkedHashMap`, `LinkedHashMultimap`, `LinkedHashSet`, `List.Cons`, `List.Nil`, `PriorityQueue`, `Queue`, `Stream.Cons`, `Stream.Empty`, `Tree.Empty`, `Tree.Node`, `TreeMap`, `TreeMultimap`, `TreeSet`, `Vector`

---

public interface Traversable<T>
extends Foldable<T>, Value<T>
Represents a recursive, multi-valued data structure whose elements can be traversed in order.
 The iteration order is determined by `Iterable.iterator()` and may vary across calls.

 

This interface provides operations for:
 

   
- **Basic access:** querying elements, length, head/tail, and emptiness.
   
- **Iteration:** indexed traversal, sliding windows, and grouping.
   
- **Numeric computations:** sum, product, min/max, and averages.
   
- **Reduction and folding:** folding, reducing, and string representation.
   
- **Selection and slicing:** take/drop, filtering, partitioning, and sub-sequencing.
   
- **Testing:** uniqueness, order, distinctness, and sequence properties.
   
- **Transformation:** mapping, flat-mapping, scanning, zipping, and deduplication.
 

 

Implementations may be lazy or strict and may support infinite sequences.

Author:
Daniel Dietrich, Grzegorz Piwowarek

- 

## Method Summary

Modifier and Type
Method
Description
`default <K> Option<Map<K,T>>`
`arrangeBy(@NonNull Function<? super T,? extends K> getKey)`

Groups elements by a unique key extracted from each element.

`default Option<Double>`
`average()`

Computes the average of the elements, assuming they are of type `Number`.

`<R> Traversable<R>`
`collect(@NonNull PartialFunction<? super T,? extends R> partialFunction)`

Applies a `PartialFunction` to all elements that are defined for it and collects the results.

`default boolean`
`containsAll(@NonNull Iterable<? extends T> elements)`

Checks whether this `Traversable` contains all elements from the given iterable.

`default int`
`count(@NonNull Predicate<? super T> predicate)`

Counts the number of elements that satisfy the given predicate.

`Traversable<T>`
`distinct()`

Returns a new `Traversable` containing the elements of this instance
 with all duplicates removed.

`Traversable<T>`
`distinctBy(@NonNull Comparator<? super T> comparator)`

Returns a new `Traversable` containing the elements of this instance
 without duplicates, as determined by the given `comparator`.

`<U> Traversable<T>`
`distinctBy(@NonNull Function<? super T,? extends U> keyExtractor)`

Returns a new `Traversable` containing the elements of this instance
 without duplicates, based on keys extracted from elements using `keyExtractor`.

`Traversable<T>`
`drop(int n)`

Returns a new `Traversable` without the first `n` elements,
 or an empty instance if this contains fewer than `n` elements.

`Traversable<T>`
`dropRight(int n)`

Returns a new `Traversable` without the last `n` elements,
 or an empty instance if this contains fewer than `n` elements.

`Traversable<T>`
`dropUntil(@NonNull Predicate<? super T> predicate)`

Returns a new `Traversable` starting from the first element
 that satisfies the given `predicate`, dropping all preceding elements.

`Traversable<T>`
`dropWhile(@NonNull Predicate<? super T> predicate)`

Returns a new `Traversable` starting from the first element
 that does not satisfy the given `predicate`, dropping all preceding elements.

`boolean`
`equals(Object obj)`

Determines whether this collection is equal to the given object.

`default boolean`
`existsUnique(@NonNull Predicate<? super T> predicate)`

Checks whether there is exactly one element in this traversable for which the given predicate holds.

`Traversable<T>`
`filter(@NonNull Predicate<? super T> predicate)`

Returns a new traversable containing only the elements that satisfy the given predicate.

`default Option<T>`
`find(@NonNull Predicate<? super T> predicate)`

Returns the first element that satisfies the given predicate.

`default Option<T>`
`findLast(@NonNull Predicate<? super T> predicate)`

Returns the last element that satisfies the given predicate.

`<U> Traversable<U>`
`flatMap(@NonNull Function<? super T,? extends Iterable<? extends U>> mapper)`

Transforms each element of this Traversable into an `Iterable` of elements and
 flattens the resulting iterables into a single Traversable.

`default <U> U`
`foldLeft(U zero,
 @NonNull BiFunction<? super U,? super T,? extends U> f)`

Folds the elements of this structure from the left, starting with the given `zero` value
 and successively applying the `combine` function to each element.

`<U> U`
`foldRight(U zero,
 @NonNull BiFunction<? super T,? super U,? extends U> f)`

Folds the elements of this structure from the right, starting with the given `zero` value
 and successively applying the `combine` function to each element.

`default void`
`forEachWithIndex(@NonNull ObjIntConsumer<? super T> action)`

Performs the given action on each element of this Traversable along with its index.

`default T`
`get()`

Returns the first element of this `Traversable` in iteration order.

`<C> Map<C,? extends Traversable<T>>`
`groupBy(@NonNull Function<? super T,? extends C> classifier)`

Groups elements of this `Traversable` based on a classifier function.

`Iterator<? extends Traversable<T>>`
`grouped(int size)`

Splits this `Traversable` into consecutive blocks of the given size.

`boolean`
`hasDefiniteSize()`

Indicates whether this `Traversable` has a known finite size.

`int`
`hashCode()`

Returns the hash code of this collection.

`T`
`head()`

Returns the first element of this non-empty `Traversable`.

`default Option<T>`
`headOption()`

Returns the first element of this `Traversable` as an `Option`.

`Traversable<T>`
`init()`

Returns all elements of this Traversable except the last one.

`default Option<? extends Traversable<T>>`
`initOption()`

Returns all elements of this Traversable except the last one, wrapped in an `Option`.

`default boolean`
`isDistinct()`

Indicates whether this Traversable may contain only distinct elements.

`default boolean`
`isEmpty()`

Checks if this Traversable contains no elements.

`default boolean`
`isOrdered()`

Indicates whether this Traversable is ordered according to its natural or specified order.

`default boolean`
`isSequential()`

Indicates whether the elements of this Traversable appear in encounter (insertion) order.

`default boolean`
`isSingleValued()`

Indicates that this Traversable may contain multiple elements.

`boolean`
`isTraversableAgain()`

Checks if this Traversable can be traversed multiple times without side effects.

`default @NonNull Iterator<T>`
`iterator()`

Returns an iterator over the elements of this Traversable, implemented via `head()` and `tail()`.

`T`
`last()`

Returns the last element of this Traversable.

`default Option<T>`
`lastOption()`

Returns the last element of this Traversable as an `Option`.

`int`
`length()`

Returns the number of elements in this Traversable.

`<U> Traversable<U>`
`map(@NonNull Function<? super T,? extends U> mapper)`

Transforms the elements of this Traversable to a new type, preserving order if defined.

`default <U> Traversable<U>`
`mapTo(U value)`

Maps the underlying value to another fixed value.

`default Traversable<Void>`
`mapToVoid()`

Maps the underlying value to Void

`default Option<T>`
`max()`

Returns the maximum element of this Traversable according to the natural order of its elements.

`default Option<T>`
`maxBy(@NonNull Comparator<? super T> comparator)`

Returns the maximum element of this Traversable according to the given comparator.

`default <U extends Comparable<? super U>>
Option<T>`
`maxBy(@NonNull Function<? super T,? extends U> f)`

Returns the element of this Traversable whose mapped value, according to the given function, is maximal.

`default Option<T>`
`min()`

Returns the minimum element of this Traversable according to its natural order in O(n).

`default Option<T>`
`minBy(@NonNull Comparator<? super T> comparator)`

Returns the minimum element of this Traversable according to a given comparator.

`default <U extends Comparable<? super U>>
Option<T>`
`minBy(@NonNull Function<? super T,? extends U> f)`

Returns the element of this Traversable whose mapped value is minimal according to natural order.

`default CharSeq`
`mkCharSeq()`

Concatenates the string representations of all elements in this Traversable.

`default CharSeq`
`mkCharSeq(CharSequence delimiter)`

Concatenates the string representations of all elements in this Traversable, separated by a delimiter.

`default CharSeq`
`mkCharSeq(CharSequence prefix,
 CharSequence delimiter,
 CharSequence suffix)`

Concatenates the string representations of all elements in this Traversable with a prefix, delimiter, and suffix.

`default String`
`mkString()`

Concatenates the string representations of all elements in this Traversable.

`default String`
`mkString(CharSequence delimiter)`

Concatenates the string representations of all elements in this Traversable, separated by a delimiter.

`default String`
`mkString(CharSequence prefix,
 CharSequence delimiter,
 CharSequence suffix)`

Concatenates the string representations of all elements in this Traversable with a prefix, delimiter, and suffix.

`static <T> Traversable<T>`
`narrow(Traversable<? extends T> traversable)`

Narrows a `Traversable<? extends T>` to `Traversable<T>` with a type-safe cast.

`default boolean`
`nonEmpty()`

Checks if this `Traversable` contains at least one element.

`Traversable<T>`
`orElse(Iterable<? extends T> other)`

Returns this `Traversable` if it is non-empty; otherwise, returns the given alternative.

`Traversable<T>`
`orElse(@NonNull Supplier<? extends Iterable<? extends T>> supplier)`

Returns this `Traversable` if it is non-empty; otherwise, returns the result of evaluating the given supplier.

`Tuple2<? extends Traversable<T>,? extends Traversable<T>>`
`partition(@NonNull Predicate<? super T> predicate)`

Splits this `Traversable` into two partitions according to a predicate.

`Traversable<T>`
`peek(@NonNull Consumer<? super T> action)`

Performs the given `action` on the first element if this is an *eager* implementation.

`default Number`
`product()`

Calculates the product of the elements in this `Traversable`.

`default T`
`reduceLeft(@NonNull BiFunction<? super T,? super T,? extends T> op)`

Reduces the elements of this Traversable from the left using the given binary operation.

`default Option<T>`
`reduceLeftOption(@NonNull BiFunction<? super T,? super T,? extends T> op)`

Reduces the elements of this Traversable from the left using the given binary operation,
 returning the result wrapped in an `Option`.

`default T`
`reduceRight(@NonNull BiFunction<? super T,? super T,? extends T> op)`

Reduces the elements of this Traversable from the right using the given binary operation.

`default Option<T>`
`reduceRightOption(@NonNull BiFunction<? super T,? super T,? extends T> op)`

Reduces the elements of this Traversable from the right using the given binary operation,
 returning the result wrapped in an `Option`.

`default Traversable<T>`
`reject(@NonNull Predicate<? super T> predicate)`

Returns a new traversable containing only the elements that do not satisfy the given predicate.

`Traversable<T>`
`replace(T currentElement,
 T newElement)`

Replaces the first occurrence of `currentElement` with `newElement`, if it exists.

`Traversable<T>`
`replaceAll(T currentElement,
 T newElement)`

Replaces all occurrences of `currentElement` with `newElement`.

`Traversable<T>`
`retainAll(@NonNull Iterable<? extends T> elements)`

Retains only the elements from this Traversable that are contained in the given `elements`.

`Traversable<T>`
`scan(T zero,
 @NonNull BiFunction<? super T,? super T,? extends T> operation)`

Computes a prefix scan of the elements of this Traversable.

`<U> Traversable<U>`
`scanLeft(U zero,
 @NonNull BiFunction<? super U,? super T,? extends U> operation)`

Produces a collection containing cumulative results of applying the operator from left to right.

`<U> Traversable<U>`
`scanRight(U zero,
 @NonNull BiFunction<? super T,? super U,? extends U> operation)`

Produces a collection containing cumulative results of applying the operator from right to left.

`default T`
`single()`

Returns the single element of this Traversable.

`default Option<T>`
`singleOption()`

Returns the single element of this Traversable as an `Option`.

`default int`
`size()`

Returns the number of elements in this Traversable.

`Iterator<? extends Traversable<T>>`
`slideBy(@NonNull Function<? super T,?> classifier)`

Partitions this `Traversable` into consecutive non-overlapping windows
 according to a classification function.

`Iterator<? extends Traversable<T>>`
`sliding(int size)`

Slides a window of a given `size` over this `Traversable` with a step size of 1.

`Iterator<? extends Traversable<T>>`
`sliding(int size,
 int step)`

Slides a window of a specific `size` with a given `step` over this `Traversable`.

`Tuple2<? extends Traversable<T>,? extends Traversable<T>>`
`span(@NonNull Predicate<? super T> predicate)`

Splits this `Traversable` into a prefix and remainder according to the given `predicate`.

`default Spliterator<T>`
`spliterator()`
 
`default Number`
`sum()`

Calculates the sum of the elements in this `Traversable`.

`Traversable<T>`
`tail()`

Returns a new `Traversable` without its first element.

`default Option<? extends Traversable<T>>`
`tailOption()`

Returns a new `Traversable` without its first element as an `Option`.

`Traversable<T>`
`take(int n)`

Returns the first `n` elements of this `Traversable`, or all elements if `n` exceeds the length.

`Traversable<T>`
`takeRight(int n)`

Returns the last `n` elements of this `Traversable`, or all elements if `n` exceeds the length.

`Traversable<T>`
`takeUntil(@NonNull Predicate<? super T> predicate)`

Takes elements from this `Traversable` until the given predicate holds for an element.

`Traversable<T>`
`takeWhile(@NonNull Predicate<? super T> predicate)`

Takes elements from this `Traversable` while the given predicate holds.

`<T1,
T2> Tuple2<? extends Traversable<T1>,? extends Traversable<T2>>`
`unzip(@NonNull Function<? super T,Tuple2<? extends T1,? extends T2>> unzipper)`

Unzips the elements of this `Traversable` by mapping each element to a pair
 and splitting them into two separate `Traversable` collections.

`<T1,
T2,
T3>
Tuple3<? extends Traversable<T1>,? extends Traversable<T2>,? extends Traversable<T3>>`
`unzip3(@NonNull Function<? super T,Tuple3<? extends T1,? extends T2,? extends T3>> unzipper)`

Unzips the elements of this `Traversable` by mapping each element to a triple
 and splitting them into three separate `Traversable` collections.

`<U> Traversable<Tuple2<T,U>>`
`zip(@NonNull Iterable<? extends U> that)`

Returns a `Traversable` formed by pairing elements of this `Traversable` with elements of another
 `Iterable`.

`<U> Traversable<Tuple2<T,U>>`
`zipAll(@NonNull Iterable<? extends U> that,
 T thisElem,
 U thatElem)`

Returns a `Traversable` formed by pairing elements of this `Traversable` with elements of another
 `Iterable`, filling in placeholder elements when one collection is shorter than the other.

`<U,
R> Traversable<R>`
`zipWith(@NonNull Iterable<? extends U> that,
 BiFunction<? super T,? super U,? extends R> mapper)`

Returns a `Traversable` by combining elements of this `Traversable` with elements of another
 `Iterable` using a mapping function.

`Traversable<Tuple2<T,Integer>>`
`zipWithIndex()`

Zips this `Traversable` with its indices, starting at 0.

`<U> Traversable<U>`
`zipWithIndex(@NonNull BiFunction<? super T,? super Integer,? extends U> mapper)`

Zips this `Traversable` with its indices and maps the resulting pairs using the provided mapper.

### Methods inherited from interface io.vavr.collection.Foldable

`fold, reduce, reduceOption`

### Methods inherited from interface io.vavr.Value

`collect, collect, contains, corresponds, eq, exists, forAll, forEach, getOrElse, getOrElse, getOrElseThrow, getOrElseTry, getOrNull, isAsync, isLazy, out, out, stderr, stdout, stringPrefix, toArray, toCharSeq, toCompletableFuture, toEither, toEither, toInvalid, toInvalid, toJavaArray, toJavaArray, toJavaArray, toJavaCollection, toJavaList, toJavaList, toJavaMap, toJavaMap, toJavaMap, toJavaOptional, toJavaParallelStream, toJavaSet, toJavaSet, toJavaStream, toLeft, toLeft, toLinkedMap, toLinkedMap, toLinkedSet, toList, toMap, toMap, toOption, toPriorityQueue, toPriorityQueue, toQueue, toRight, toRight, toSet, toSortedMap, toSortedMap, toSortedMap, toSortedMap, toSortedSet, toSortedSet, toStream, toString, toTree, toTree, toTry, toTry, toValid, toValid, toValidation, toValidation, toVector`

- 

## Method Details

  - 

### narrow

static <T> Traversable<T> narrow(Traversable<? extends T> traversable)
Narrows a `Traversable<? extends T>` to `Traversable<T>` with a type-safe cast.
 

 This is safe because immutable or read-only collections are covariant in their element type.

Type Parameters:
`T` - the element type of the resulting `Traversable`
Parameters:
`traversable` - the `Traversable` instance to narrow
Returns:
the same `traversable` instance with type `Traversable<T>`

  - 

### arrangeBy

default <K> Option<Map<K,T>> arrangeBy(@NonNull Function<? super T,? extends K> getKey)
Groups elements by a unique key extracted from each element.
 

 Returns `None` if any key occurs more than once; otherwise, returns a `Map`
 where each key is associated with its corresponding element.

Type Parameters:
`K` - the type of keys
Parameters:
`getKey` - a function to extract a key from each element
Returns:
an `Option` containing the `Map` of elements by key, or `None` if keys are not unique
Throws:
`NullPointerException` - if `getKey` is null
See Also:

    - `groupBy(Function)`

  - 

### average

default Option<Double> average()
Computes the average of the elements, assuming they are of type `Number`.
 

 If the elements are not numeric, an `UnsupportedOperationException` is thrown.
 

 Examples:

 

```

 List.empty().average()                       // = None
 List.of(1, 2, 3).average()                   // = Some(2.0)
 List.of(1.0, 1e100, 2.0, -1e100).average()  // = Some(0.75)
 List.of(1.0, Double.NaN).average()           // = NaN
 List.of("apple", "pear").average()           // throws
 
```

 

 Unlike Java's `DoubleStream.average()` which uses the Kahan summation algorithm,
 Vavr uses Neumaier's modification of Kahan's algorithm for improved numerical accuracy.

Returns:
`Some(average)` if the sequence has elements, otherwise `None`
Throws:
`UnsupportedOperationException` - if any element is not numeric

  - 

### collect

<R> Traversable<R> collect(@NonNull PartialFunction<? super T,? extends R> partialFunction)
Applies a `PartialFunction` to all elements that are defined for it and collects the results.
 

 For each element in iteration order, the function is first tested:

 

```

 partialFunction.isDefinedAt(element)
 
```

 If `true`, the element is mapped to type `R`:

 

```

 R newElement = partialFunction.apply(element)
 
```

 

**Note:** If this `Traversable` is ordered (i.e., extends `Ordered`),
 the caller must ensure that the resulting elements are comparable (i.e., implement `Comparable`).

Type Parameters:
`R` - the type of elements in the resulting `Traversable`
Parameters:
`partialFunction` - a function that may not be defined for all elements of this traversable
Returns:
a new `Traversable` containing the results of applying the partial function
Throws:
`NullPointerException` - if `partialFunction` is null

  - 

### containsAll

default boolean containsAll(@NonNull Iterable<? extends T> elements)
Checks whether this `Traversable` contains all elements from the given iterable.
 

 Equivalent to testing each element individually:
 

```

 elements.isEmpty() ? true : contains(elements.head()) && containsAll(elements.tail())
 
```

 but implemented efficiently without recursion.

Parameters:
`elements` - an `Iterable` of elements to check for containment
Returns:
`true` if all elements are present, `false` otherwise
Throws:
`NullPointerException` - if `elements` is null

  - 

### count

default int count(@NonNull Predicate<? super T> predicate)
Counts the number of elements that satisfy the given predicate.

Parameters:
`predicate` - a condition to test each element
Returns:
the number of elements matching the predicate (always >= 0)
Throws:
`NullPointerException` - if `predicate` is null

  - 

### distinct

Traversable<T> distinct()
Returns a new `Traversable` containing the elements of this instance
 with all duplicates removed. Element equality is determined using `equals`.

Returns:
a new `Traversable` without duplicate elements

  - 

### distinctBy

Traversable<T> distinctBy(@NonNull Comparator<? super T> comparator)
Returns a new `Traversable` containing the elements of this instance
 without duplicates, as determined by the given `comparator`.

Parameters:
`comparator` - a comparator used to determine equality of elements
Returns:
a new `Traversable` with duplicates removed
Throws:
`NullPointerException` - if `comparator` is null

  - 

### distinctBy

<U> Traversable<T> distinctBy(@NonNull Function<? super T,? extends U> keyExtractor)
Returns a new `Traversable` containing the elements of this instance
 without duplicates, based on keys extracted from elements using `keyExtractor`.
 

 The first occurrence of each key is retained in the resulting sequence.

Type Parameters:
`U` - the type of key
Parameters:
`keyExtractor` - a function to extract keys for determining uniqueness
Returns:
a new `Traversable` with duplicates removed based on keys
Throws:
`NullPointerException` - if `keyExtractor` is null

  - 

### drop

Traversable<T> drop(int n)
Returns a new `Traversable` without the first `n` elements,
 or an empty instance if this contains fewer than `n` elements.

Parameters:
`n` - the number of elements to drop
Returns:
a new instance excluding the first `n` elements

  - 

### dropRight

Traversable<T> dropRight(int n)
Returns a new `Traversable` without the last `n` elements,
 or an empty instance if this contains fewer than `n` elements.

Parameters:
`n` - the number of elements to drop from the end
Returns:
a new instance excluding the last `n` elements

  - 

### dropUntil

Traversable<T> dropUntil(@NonNull Predicate<? super T> predicate)
Returns a new `Traversable` starting from the first element
 that satisfies the given `predicate`, dropping all preceding elements.

Parameters:
`predicate` - a condition tested on each element
Returns:
a new instance starting from the first element matching the predicate
Throws:
`NullPointerException` - if `predicate` is null

  - 

### dropWhile

Traversable<T> dropWhile(@NonNull Predicate<? super T> predicate)
Returns a new `Traversable` starting from the first element
 that does not satisfy the given `predicate`, dropping all preceding elements.
 

 This is equivalent to `dropUntil(predicate.negate())`, which is useful
 for method references that cannot be negated directly.

Parameters:
`predicate` - a condition tested on each element
Returns:
a new instance starting from the first element not matching the predicate
Throws:
`NullPointerException` - if `predicate` is null

  - 

### equals

boolean equals(Object obj)
Determines whether this collection is equal to the given object.
 

 In Vavr, there are four basic collection types:
 

     
    - `Seq` â sequential elements
     
    - `Set` â distinct elements
     
    - `Map` â key-value pairs
     
    - `Multimap` â keys mapped to multiple values
 

 Two collections are considered equal if and only if:
 

     
    - They are of the same collection type (Seq, Set, Map, Multimap)
     
    - They contain the same elements
     
    - For `Seq`, the element order is the same
 

 

 For `Map` and `Multimap`, two entries `(key1, value1)` and `(key2, value2)`
 are equal if both their keys and values are equal.
 

 **Additional notes:**
 

     
    - No collection equals `null` (e.g., `Queue(1) != null`)
     
    - Null elements are allowed and treated as expected
         (e.g., `List(null, 1) == Stream(null, 1)`, `HashMap((null,1)) == LinkedHashMap((null,1))`)
     
    - Element order matters only for `Seq`
     
    - Other collection classes are equal if their types and elements (in iteration order) are equal
     
    - Iterators are compared by reference only
 

Specified by:
`equals` in interface `Value<T>`
Overrides:
`equals` in class `Object`
Parameters:
`obj` - the object to compare with, may be `null`
Returns:
`true` if the collections are equal according to the rules above, `false` otherwise

  - 

### existsUnique

default boolean existsUnique(@NonNull Predicate<? super T> predicate)
Checks whether there is exactly one element in this traversable for which the given predicate holds.

Parameters:
`predicate` - the condition to test elements
Returns:
`true` if exactly one element satisfies the predicate, `false` otherwise
Throws:
`NullPointerException` - if `predicate` is `null`

  - 

### filter

Traversable<T> filter(@NonNull Predicate<? super T> predicate)
Returns a new traversable containing only the elements that satisfy the given predicate.

Parameters:
`predicate` - the condition to test elements
Returns:
a traversable with elements matching the predicate
Throws:
`NullPointerException` - if `predicate` is null

  - 

### reject

default Traversable<T> reject(@NonNull Predicate<? super T> predicate)
Returns a new traversable containing only the elements that do not satisfy the given predicate.
 

 This is equivalent to `filter(predicate.negate())`.

Parameters:
`predicate` - the condition to test elements
Returns:
a traversable with elements not matching the predicate
Throws:
`NullPointerException` - if `predicate` is null

  - 

### find

default Option<T> find(@NonNull Predicate<? super T> predicate)
Returns the first element that satisfies the given predicate.

Parameters:
`predicate` - the condition to test elements
Returns:
`Some(element)` if a matching element is found, otherwise `None`;
         the element may be `null`
Throws:
`NullPointerException` - if `predicate` is null

  - 

### findLast

default Option<T> findLast(@NonNull Predicate<? super T> predicate)
Returns the last element that satisfies the given predicate.
 

 Equivalent to `reverse().find(predicate)` but potentially more efficient.

Parameters:
`predicate` - the condition to test elements
Returns:
`Some(element)` if a matching element is found, otherwise `None`;
         the element may be `null`
Throws:
`NullPointerException` - if `predicate` is null

  - 

### flatMap

<U> Traversable<U> flatMap(@NonNull Function<? super T,? extends Iterable<? extends U>> mapper)
Transforms each element of this Traversable into an `Iterable` of elements and
 flattens the resulting iterables into a single Traversable.

Type Parameters:
`U` - the type of elements in the resulting Traversable
Parameters:
`mapper` - a function mapping elements to iterables
Returns:
a new Traversable containing all elements produced by applying `mapper` and flattening
Throws:
`NullPointerException` - if `mapper` is null

  - 

### foldLeft

default <U> U foldLeft(U zero,
 @NonNull BiFunction<? super U,? super T,? extends U> f)
Description copied from interface: `Foldable`
Folds the elements of this structure from the left, starting with the given `zero` value
 and successively applying the `combine` function to each element.
 

 Folding from the left means that elements are combined in the order they are encountered,
 associating each step with the accumulated result so far.
 

 **Example:**
 

```

 // Result: "cba!"
 List.of("a", "b", "c").foldLeft("!", (acc, x) -> x + acc);
 
```

Specified by:
`foldLeft` in interface `Foldable<T>`
Type Parameters:
`U` - the type of the accumulated result
Parameters:
`zero` - the initial value to start folding with
`f` - a function that combines the accumulated value and the next element
Returns:
the folded result

  - 

### foldRight

<U> U foldRight(U zero,
 @NonNull BiFunction<? super T,? super U,? extends U> f)
Description copied from interface: `Foldable`
Folds the elements of this structure from the right, starting with the given `zero` value
 and successively applying the `combine` function to each element.
 

 Folding from the right means that elements are combined starting from the last element
 and associating each step with the accumulated result so far.
 

 **Example:**
 

```

 // Result: "!cba"
 List.of("a", "b", "c").foldRight("!", (x, acc) -> acc + x);
 
```

Specified by:
`foldRight` in interface `Foldable<T>`
Type Parameters:
`U` - the type of the accumulated result
Parameters:
`zero` - the initial value to start folding with
`f` - a function that combines the next element and the accumulated value
Returns:
the folded result

  - 

### forEachWithIndex

default void forEachWithIndex(@NonNull ObjIntConsumer<? super T> action)
Performs the given action on each element of this Traversable along with its index.

 

This method is more efficient than `iterator().zipWithIndex().forEach()` because
 it avoids creating intermediate `Tuple2` objects and boxing integers.

 

Note that the iteration order may vary between calls depending on the underlying
 Traversable implementation. Also, if this Traversable is lazily evaluated (e.g., a `Stream`),
 the method may loop indefinitely.

Parameters:
`action` - an action to perform on each element and its index
Throws:
`NullPointerException` - if `action` is null

  - 

### get

default T get()
Returns the first element of this `Traversable` in iteration order.

Specified by:
`get` in interface `Value<T>`
Returns:
the first element
Throws:
`NoSuchElementException` - if this `Traversable` is empty

  - 

### groupBy

<C> Map<C,? extends Traversable<T>> groupBy(@NonNull Function<? super T,? extends C> classifier)
Groups elements of this `Traversable` based on a classifier function.

Type Parameters:
`C` - The type of the group keys
Parameters:
`classifier` - A function that assigns each element to a group
Returns:
A map where each key corresponds to a group of elements
Throws:
`NullPointerException` - if `classifier` is null
See Also:

    - `arrangeBy(Function)`

  - 

### grouped

Iterator<? extends Traversable<T>> grouped(int size)
Splits this `Traversable` into consecutive blocks of the given size.
 

 Let `length` be the number of elements in this `Traversable`:
 

     
    - If empty, the resulting `Iterator` is empty.
     
    - If `size <= length`, the resulting `Iterator` contains
         `length / size` blocks of size `size` and possibly a final smaller block of size `length % size`.
     
    - If `size > length`, the resulting `Iterator` contains a single block of size `length`.
 

 

Examples:
 

```

 
 [].grouped(1) = []
 [].grouped(0) throws
 [].grouped(-1) throws
 [1,2,3,4].grouped(2) = [[1,2],[3,4]]
 [1,2,3,4,5].grouped(2) = [[1,2],[3,4],[5]]
 [1,2,3,4].grouped(5) = [[1,2,3,4]]
 
 
```

 

Note: `grouped(size)` is equivalent to `sliding(size, size)`.

Parameters:
`size` - the block size; must be positive
Returns:
an `Iterator` over blocks of elements
Throws:
`IllegalArgumentException` - if `size` is zero or negative

  - 

### hasDefiniteSize

boolean hasDefiniteSize()
Indicates whether this `Traversable` has a known finite size.
 

 This should typically be implemented by concrete classes, not interfaces.

Returns:
`true` if the number of elements is finite and known, `false` otherwise.

  - 

### head

T head()
Returns the first element of this non-empty `Traversable`.

Returns:
the first element
Throws:
`NoSuchElementException` - if this `Traversable` is empty

  - 

### headOption

default Option<T> headOption()
Returns the first element of this `Traversable` as an `Option`.

Returns:
`Some(element)` if non-empty, otherwise `None`

  - 

### hashCode

int hashCode()
Returns the hash code of this collection.

 

Vavr distinguishes between collections with predictable iteration order (like `Seq`) and
 collections with arbitrary iteration order (like `Set`, `Map`, and `Multimap`).
 In all cases, the hash of an empty collection is defined as `1`.

 

For collections with predictable iteration order, the hash is computed as:
 

```

 int hash = 1;
 for (T t : this) {
     hash = hash * 31 + Objects.hashCode(t);
 }
 
```

 

For collections with arbitrary iteration order, the hash is computed to be independent of element order:
 

```

 int hash = 1;
 for (T t : this) {
     hash += Objects.hashCode(t);
 }
 
```

 

Note that these algorithms may change in future Vavr versions. Hash codes are generally *not* cached,
 unlike size/length, because caching would increase memory usage due to persistent tree-based structures.
 Computing the hash code is linear in time, O(n). For frequently re-used collections (e.g., as `HashMap` keys),
 caching can be done externally using a wrapper, for example:

 

```

 public final class Hashed<K> {
     private final K key;
     private final Lazy<Integer> hashCode;

     public Hashed(K key) {
         this.key = key;
         this.hashCode = Lazy.of(() -> Objects.hashCode(key));
     }

     public K key() { return key; }

     @Override
     public boolean equals(Object o) {
         if (o == key) return true;
         if (key != null && o instanceof Hashed) return key.equals(((Hashed<?>) o).key);
         return false;
     }

     @Override
     public int hashCode() { return hashCode.get(); }

     @Override
     public String toString() { return "Hashed(" + key + ")"; }
 }
 
```

Specified by:
`hashCode` in interface `Value<T>`
Overrides:
`hashCode` in class `Object`
Returns:
the hash code of this collection

  - 

### init

Traversable<T> init()
Returns all elements of this Traversable except the last one.
 

 This is the dual of `tail()`.

Returns:
a new instance containing all elements except the last
Throws:
`UnsupportedOperationException` - if this Traversable is empty

  - 

### initOption

default Option<? extends Traversable<T>> initOption()
Returns all elements of this Traversable except the last one, wrapped in an `Option`.
 

 This is the dual of `tailOption()`.

Returns:
`Some(traversable)` if non-empty, or `None` if this Traversable is empty

  - 

### isDistinct

default boolean isDistinct()
Indicates whether this Traversable may contain only distinct elements.

Returns:
`true` if this Traversable may contain only distinct elements, `false` otherwise

  - 

### isEmpty

default boolean isEmpty()
Checks if this Traversable contains no elements.

Specified by:
`isEmpty` in interface `Value<T>`
Returns:
`true` if empty, `false` otherwise

  - 

### isOrdered

default boolean isOrdered()
Indicates whether this Traversable is ordered according to its natural or specified order.

Returns:
`true` if this Traversable is ordered, `false` otherwise

  - 

### isSequential

default boolean isSequential()
Indicates whether the elements of this Traversable appear in encounter (insertion) order.

Returns:
`true` if insertion order is preserved, `false` otherwise

  - 

### isSingleValued

default boolean isSingleValued()
Indicates that this Traversable may contain multiple elements.

Specified by:
`isSingleValued` in interface `Value<T>`
Returns:
`false` since Traversable is multi-valued by design

  - 

### isTraversableAgain

boolean isTraversableAgain()
Checks if this Traversable can be traversed multiple times without side effects.
 

 Implementations should provide the correct behavior; this is not meant for interfaces alone.

Returns:
`true` if this Traversable is guaranteed to be repeatably traversable, `false` otherwise

  - 

### iterator

default @NonNull Iterator<T> iterator()
Returns an iterator over the elements of this Traversable, implemented via `head()` and `tail()`.
 Subclasses may override for a more efficient implementation.

Specified by:
`iterator` in interface `Iterable<T>`
Specified by:
`iterator` in interface `Value<T>`
Returns:
a new `Iterator` over the elements of this Traversable

  - 

### last

T last()
Returns the last element of this Traversable.

Returns:
the last element
Throws:
`NoSuchElementException` - if this Traversable is empty

  - 

### lastOption

default Option<T> lastOption()
Returns the last element of this Traversable as an `Option`.

Returns:
`Some(element)` if not empty, otherwise `None`

  - 

### length

int length()
Returns the number of elements in this Traversable.
 

 Equivalent to `size()`.

Returns:
the number of elements

  - 

### map

<U> Traversable<U> map(@NonNull Function<? super T,? extends U> mapper)
Transforms the elements of this Traversable to a new type, preserving order if defined.

Specified by:
`map` in interface `Value<T>`
Type Parameters:
`U` - the target element type
Parameters:
`mapper` - a mapping function
Returns:
a new Traversable containing the mapped elements
Throws:
`NullPointerException` - if `mapper` is null

  - 

### mapTo

default <U> Traversable<U> mapTo(U value)
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

default Traversable<Void> mapToVoid()
Description copied from interface: `Value`
Maps the underlying value to Void

Specified by:
`mapToVoid` in interface `Value<T>`
Returns:
A new value of type Void

  - 

### max

default Option<T> max()
Returns the maximum element of this Traversable according to the natural order of its elements.
 

 Note that the underlying order of sorted collections is not consideredâonly the natural ordering of elements matters.
 

 Examples:
 

```

 List.empty().max()             // = None
 List.of(1, 2, 3).max()         // = Some(3)
 List.of("a", "b", "c").max()   // = Some("c")
 List.of(1.0, Double.NaN).max() // = NaN
 List.of(1, "a").max()          // throws ClassCastException
 
```

Returns:
`Some(maximum)` if this Traversable is not empty, otherwise `None`
Throws:
`NullPointerException` - if any element is null
`ClassCastException` - if elements do not implement `Comparable`

  - 

### maxBy

default Option<T> maxBy(@NonNull Comparator<? super T> comparator)
Returns the maximum element of this Traversable according to the given comparator.
 

 If the Traversable is empty, `None` is returned.

Parameters:
`comparator` - a non-null `Comparator` to determine element ordering
Returns:
`Some(maximum)` if this Traversable is not empty, otherwise `None`
Throws:
`NullPointerException` - if `comparator` is null

  - 

### maxBy

default <U extends Comparable<? super U>> Option<T> maxBy(@NonNull Function<? super T,? extends U> f)
Returns the element of this Traversable whose mapped value, according to the given function, is maximal.
 

 The mapping function `f` transforms elements of type `T` to a comparable type `U`,
 and the element with the largest `U` value is returned.

Type Parameters:
`U` - the type used for comparison, must implement `Comparable`
Parameters:
`f` - a non-null function mapping elements to a comparable type
Returns:
`Some(element)` whose mapped value is maximal, or `None` if this Traversable is empty
Throws:
`NullPointerException` - if `f` is null

  - 

### min

default Option<T> min()
Returns the minimum element of this Traversable according to its natural order in O(n).
 

 The underlying order of sorted collections is not considered. For numeric types `Double` and `Float`,
 if any element is `NaN`, the result is `NaN` instead of following the natural order.
 

 Examples:
 

```

 
 List.empty().min()             // = None
 List.of(1, 2, 3).min()         // = Some(1)
 List.of("a", "b", "c").min()   // = Some("a")
 List.of(1.0, Double.NaN).min() // = NaN
 List.of(1, "a").min()          // throws
 
 
```

Returns:
`Some(minimum)` of this elements, or `None` if this Traversable is empty
Throws:
`NullPointerException` - if an element is null
`ClassCastException` - if the elements do not have a natural order, i.e., do not implement `Comparable`

  - 

### minBy

default Option<T> minBy(@NonNull Comparator<? super T> comparator)
Returns the minimum element of this Traversable according to a given comparator.

Parameters:
`comparator` - a non-null comparator used to determine ordering
Returns:
`Some(minimum)` of this elements, or `None` if this Traversable is empty
Throws:
`NullPointerException` - if `comparator` is null

  - 

### minBy

default <U extends Comparable<? super U>> Option<T> minBy(@NonNull Function<? super T,? extends U> f)
Returns the element of this Traversable whose mapped value is minimal according to natural order.

Type Parameters:
`U` - the type of the comparable value
Parameters:
`f` - a function mapping elements to a comparable value
Returns:
the element of type T whose mapped value is minimal, wrapped in `Some`, or `None` if empty
Throws:
`NullPointerException` - if `f` is null

  - 

### mkCharSeq

default CharSeq mkCharSeq()
Concatenates the string representations of all elements in this Traversable.
 

 Equivalent to `mkCharSeq("", "", "")`.

Returns:
a new `CharSeq` containing all elements concatenated

  - 

### mkCharSeq

default CharSeq mkCharSeq(CharSequence delimiter)
Concatenates the string representations of all elements in this Traversable, separated by a delimiter.
 

 Equivalent to `mkCharSeq("", delimiter, "")`.

Parameters:
`delimiter` - a string placed between elements
Returns:
a new `CharSeq` with elements separated by the delimiter

  - 

### mkCharSeq

default CharSeq mkCharSeq(CharSequence prefix,
 CharSequence delimiter,
 CharSequence suffix)
Concatenates the string representations of all elements in this Traversable with a prefix, delimiter, and suffix.
 

 Example: `List.of("a", "b", "c").mkCharSeq("Chars(", ", ", ")") = CharSeq.of("Chars(a, b, c)")`

Parameters:
`prefix` - a string prepended to the result
`delimiter` - a string placed between elements
`suffix` - a string appended to the result
Returns:
a new `CharSeq` containing the formatted concatenation of elements

  - 

### mkString

default String mkString()
Concatenates the string representations of all elements in this Traversable.
 

 Equivalent to `mkString("", "", "")`.

Returns:
a new `String` containing all elements concatenated

  - 

### mkString

default String mkString(CharSequence delimiter)
Concatenates the string representations of all elements in this Traversable, separated by a delimiter.
 

 Equivalent to `mkString("", delimiter, "")`.

Parameters:
`delimiter` - a string placed between elements
Returns:
a new `String` containing the concatenated elements

  - 

### mkString

default String mkString(CharSequence prefix,
 CharSequence delimiter,
 CharSequence suffix)
Concatenates the string representations of all elements in this Traversable with a prefix, delimiter, and suffix.
 

 Example: `List.of("a", "b", "c").mkString("Chars(", ", ", ")") = "Chars(a, b, c)"`

Parameters:
`prefix` - a string prepended to the result
`delimiter` - a string placed between elements
`suffix` - a string appended to the result
Returns:
a new `String` containing the formatted concatenation of elements

  - 

### nonEmpty

default boolean nonEmpty()
Checks if this `Traversable` contains at least one element.
 

 Equivalent to `!isEmpty()`.

Returns:
`true` if this Traversable is not empty, `false` otherwise

  - 

### orElse

Traversable<T> orElse(Iterable<? extends T> other)
Returns this `Traversable` if it is non-empty; otherwise, returns the given alternative.

Parameters:
`other` - an alternative `Traversable` to return if this is empty
Returns:
this `Traversable` if non-empty, otherwise `other`

  - 

### orElse

Traversable<T> orElse(@NonNull Supplier<? extends Iterable<? extends T>> supplier)
Returns this `Traversable` if it is non-empty; otherwise, returns the result of evaluating the given supplier.

Parameters:
`supplier` - a supplier of an alternative `Traversable` if this is empty
Returns:
this `Traversable` if non-empty, otherwise the result of `supplier.get()`
Throws:
`NullPointerException` - if `supplier` is null

  - 

### partition

Tuple2<? extends Traversable<T>,? extends Traversable<T>> partition(@NonNull Predicate<? super T> predicate)
Splits this `Traversable` into two partitions according to a predicate.
 

 The first partition contains all elements that satisfy the predicate, and the second contains all elements that do not.
 The original iteration order is preserved.

Parameters:
`predicate` - a predicate used to classify elements
Returns:
a `Tuple2` containing the two resulting `Traversable` instances
Throws:
`NullPointerException` - if `predicate` is null

  - 

### peek

Traversable<T> peek(@NonNull Consumer<? super T> action)
Description copied from interface: `Value`
Performs the given `action` on the first element if this is an *eager* implementation.
 Performs the given `action` on all elements (the first immediately, successive deferred),
 if this is a *lazy* implementation.

Specified by:
`peek` in interface `Value<T>`
Parameters:
`action` - The action that will be performed on the element(s).
Returns:
this instance

  - 

### product

default Number product()
Calculates the product of the elements in this `Traversable`.
 

 Supported element types are `Byte`, `Double`, `Float`, `Integer`, `Long`,
 `Short`, `BigInteger`, and `BigDecimal`.
 

 Examples:
 

```

 List.empty().product()              // = 1
 List.of(1, 2, 3).product()          // = 6L
 List.of(0.1, 0.2, 0.3).product()    // = 0.006
 List.of("apple", "pear").product()  // throws
 
```

 

 For type-safe multiplication of elements, consider using `Foldable.fold(Object, BiFunction)`.

Returns:
a `Number` representing the product of the elements
Throws:
`UnsupportedOperationException` - if the elements are not numeric

  - 

### reduceLeft

default T reduceLeft(@NonNull BiFunction<? super T,? super T,? extends T> op)
Reduces the elements of this Traversable from the left using the given binary operation.

Specified by:
`reduceLeft` in interface `Foldable<T>`
Parameters:
`op` - A binary operation combining two elements of type T
Returns:
the result of the reduction
Throws:
`NoSuchElementException` - if this Traversable is empty
`NullPointerException` - if `op` is null

  - 

### reduceLeftOption

default Option<T> reduceLeftOption(@NonNull BiFunction<? super T,? super T,? extends T> op)
Reduces the elements of this Traversable from the left using the given binary operation,
 returning the result wrapped in an `Option`.

Specified by:
`reduceLeftOption` in interface `Foldable<T>`
Parameters:
`op` - A binary operation combining two elements of type T
Returns:
`Some(reduced value)` or `None` if this Traversable is empty
Throws:
`NullPointerException` - if `op` is null

  - 

### reduceRight

default T reduceRight(@NonNull BiFunction<? super T,? super T,? extends T> op)
Reduces the elements of this Traversable from the right using the given binary operation.

Specified by:
`reduceRight` in interface `Foldable<T>`
Parameters:
`op` - A binary operation combining two elements of type T
Returns:
the result of the reduction
Throws:
`NoSuchElementException` - if this Traversable is empty
`NullPointerException` - if `op` is null

  - 

### reduceRightOption

default Option<T> reduceRightOption(@NonNull BiFunction<? super T,? super T,? extends T> op)
Reduces the elements of this Traversable from the right using the given binary operation,
 returning the result wrapped in an `Option`.

Specified by:
`reduceRightOption` in interface `Foldable<T>`
Parameters:
`op` - A binary operation combining two elements of type T
Returns:
`Some(reduced value)` or `None` if this Traversable is empty
Throws:
`NullPointerException` - if `op` is null

  - 

### replace

Traversable<T> replace(T currentElement,
 T newElement)
Replaces the first occurrence of `currentElement` with `newElement`, if it exists.

Parameters:
`currentElement` - the element to be replaced
`newElement` - the replacement element
Returns:
a new Traversable with the first occurrence of `currentElement` replaced by `newElement`

  - 

### replaceAll

Traversable<T> replaceAll(T currentElement,
 T newElement)
Replaces all occurrences of `currentElement` with `newElement`.

Parameters:
`currentElement` - the element to be replaced
`newElement` - the replacement element
Returns:
a new Traversable with all occurrences of `currentElement` replaced by `newElement`

  - 

### retainAll

Traversable<T> retainAll(@NonNull Iterable<? extends T> elements)
Retains only the elements from this Traversable that are contained in the given `elements`.

Parameters:
`elements` - the elements to keep
Returns:
a new Traversable containing only the elements present in `elements`, in their original order
Throws:
`NullPointerException` - if `elements` is null

  - 

### scan

Traversable<T> scan(T zero,
 @NonNull BiFunction<? super T,? super T,? extends T> operation)
Computes a prefix scan of the elements of this Traversable.
 

 The neutral element `zero` may be applied more than once.

Parameters:
`zero` - the neutral element for the operator
`operation` - an associative binary operator
Returns:
a new Traversable containing the prefix scan of the elements
Throws:
`NullPointerException` - if `operation` is null

  - 

### scanLeft

<U> Traversable<U> scanLeft(U zero,
 @NonNull BiFunction<? super U,? super T,? extends U> operation)
Produces a collection containing cumulative results of applying the operator from left to right.
 

 Will not terminate for infinite collections. The results may vary across runs unless the collection is ordered.

Type Parameters:
`U` - the type of the resulting elements
Parameters:
`zero` - the initial value
`operation` - a binary operator applied to the intermediate result and each element
Returns:
a new Traversable containing the cumulative results
Throws:
`NullPointerException` - if `operation` is null

  - 

### scanRight

<U> Traversable<U> scanRight(U zero,
 @NonNull BiFunction<? super T,? super U,? extends U> operation)
Produces a collection containing cumulative results of applying the operator from right to left.
 

 The head of the resulting collection is the last cumulative result. Will not terminate for infinite collections.
 Results may vary across runs unless the collection is ordered.

Type Parameters:
`U` - the type of the resulting elements
Parameters:
`zero` - the initial value
`operation` - a binary operator applied to each element and the intermediate result
Returns:
a new Traversable containing the cumulative results
Throws:
`NullPointerException` - if `operation` is null

  - 

### single

default T single()
Returns the single element of this Traversable.

Returns:
the single element
Throws:
`NoSuchElementException` - if the Traversable is empty or contains more than one element

  - 

### singleOption

default Option<T> singleOption()
Returns the single element of this Traversable as an `Option`.

Returns:
`Some(element)` if the Traversable contains exactly one element,
         or `None` otherwise.

  - 

### size

default int size()
Returns the number of elements in this Traversable.
 

 Alias for `length()`.

Returns:
the number of elements

  - 

### slideBy

Iterator<? extends Traversable<T>> slideBy(@NonNull Function<? super T,?> classifier)
Partitions this `Traversable` into consecutive non-overlapping windows
 according to a classification function.
 

 Each window contains elements with the same class, as determined by `classifier`.
 Two consecutive elements belong to the same window only if `classifier` returns equal values
 for both. Otherwise, the current window ends and a new window begins with the next element.
 

 Examples:
 

```

 [].slideBy(Function.identity()) = []
 [1,2,3,4,4,5].slideBy(Function.identity()) = [[1],[2],[3],[4,4],[5]]
 [1,2,3,10,12,5,7,20,29].slideBy(x -> x / 10) = [[1,2,3],[10,12],[5,7],[20,29]]
 
```

Parameters:
`classifier` - A function classifying elements into groups
Returns:
An `Iterator` of windows (grouped elements)
Throws:
`NullPointerException` - if `classifier` is null

  - 

### sliding

Iterator<? extends Traversable<T>> sliding(int size)
Slides a window of a given `size` over this `Traversable` with a step size of 1.
 

 This is equivalent to calling `sliding(int, int)` with a step size of 1.

Parameters:
`size` - a positive window size
Returns:
An `Iterator` of windows, each containing up to `size` elements
Throws:
`IllegalArgumentException` - if `size` is zero or negative

  - 

### sliding

Iterator<? extends Traversable<T>> sliding(int size,
 int step)
Slides a window of a specific `size` with a given `step` over this `Traversable`.
 

 Examples:
 

```

 [].sliding(1, 1) = []
 [1,2,3,4,5].sliding(2, 3) = [[1,2],[4,5]]
 [1,2,3,4,5].sliding(2, 4) = [[1,2],[5]]
 [1,2,3,4,5].sliding(2, 5) = [[1,2]]
 [1,2,3,4].sliding(5, 3) = [[1,2,3,4],[4]]
 
```

Parameters:
`size` - a positive window size
`step` - a positive step size
Returns:
an `Iterator` of windows with the given size and step
Throws:
`IllegalArgumentException` - if `size` or `step` are zero or negative

  - 

### span

Tuple2<? extends Traversable<T>,? extends Traversable<T>> span(@NonNull Predicate<? super T> predicate)
Splits this `Traversable` into a prefix and remainder according to the given `predicate`.
 

 The first element of the returned `Tuple` is the longest prefix of elements satisfying `predicate`,
 and the second element is the remaining elements.

Parameters:
`predicate` - a predicate used to determine the prefix
Returns:
a `Tuple` containing the prefix and remainder
Throws:
`NullPointerException` - if `predicate` is null

  - 

### spliterator

default Spliterator<T> spliterator()

Specified by:
`spliterator` in interface `Iterable<T>`
Specified by:
`spliterator` in interface `Value<T>`

  - 

### sum

default Number sum()
Calculates the sum of the elements in this `Traversable`. Supported numeric types are
 `Byte`, `Double`, `Float`, `Integer`, `Long`, `Short`,
 `BigInteger`, and `BigDecimal`.
 

 Examples:
 

```

 List.empty().sum()              // = 0
 List.of(1, 2, 3).sum()          // = 6L
 List.of(0.1, 0.2, 0.3).sum()    // = 0.6
 List.of("apple", "pear").sum()  // throws
 
```

 

 See also `Foldable.fold(Object, BiFunction)` for type-safe summation of elements.

Returns:
a `Number` representing the sum of the elements
Throws:
`UnsupportedOperationException` - if elements are not numeric

  - 

### tail

Traversable<T> tail()
Returns a new `Traversable` without its first element.

Returns:
a new `Traversable` containing all elements except the first
Throws:
`UnsupportedOperationException` - if this `Traversable` is empty

  - 

### tailOption

default Option<? extends Traversable<T>> tailOption()
Returns a new `Traversable` without its first element as an `Option`.

Returns:
`Some(traversable)` if non-empty, otherwise `None`

  - 

### take

Traversable<T> take(int n)
Returns the first `n` elements of this `Traversable`, or all elements if `n` exceeds the length.
 

 Equivalent to `sublist(0, max(0, min(length(), n)))`, but safe for `n < 0` or `n > length()`.
 

 If `n < 0`, an empty instance is returned. If `n > length()`, the full instance is returned.

Parameters:
`n` - the number of elements to take
Returns:
a new `Traversable` containing the first `n` elements

  - 

### takeRight

Traversable<T> takeRight(int n)
Returns the last `n` elements of this `Traversable`, or all elements if `n` exceeds the length.
 

 Equivalent to `sublist(max(0, length() - n), length())`, but safe for `n < 0` or `n > length()`.
 

 If `n < 0`, an empty instance is returned. If `n > length()`, the full instance is returned.

Parameters:
`n` - the number of elements to take from the end
Returns:
a new `Traversable` containing the last `n` elements

  - 

### takeUntil

Traversable<T> takeUntil(@NonNull Predicate<? super T> predicate)
Takes elements from this `Traversable` until the given predicate holds for an element.
 

 Equivalent to `takeWhile(predicate.negate())`, but useful when using method references
 that cannot be negated directly.

Parameters:
`predicate` - a condition tested sequentially on the elements
Returns:
a new `Traversable` containing all elements before the first one that satisfies the predicate
Throws:
`NullPointerException` - if `predicate` is null

  - 

### takeWhile

Traversable<T> takeWhile(@NonNull Predicate<? super T> predicate)
Takes elements from this `Traversable` while the given predicate holds.

Parameters:
`predicate` - a condition tested sequentially on the elements
Returns:
a new `Traversable` containing all elements up to (but not including) the first one
         that does not satisfy the predicate
Throws:
`NullPointerException` - if `predicate` is null

  - 

### unzip

<T1,
T2>
Tuple2<? extends Traversable<T1>,? extends Traversable<T2>> unzip(@NonNull Function<? super T,Tuple2<? extends T1,? extends T2>> unzipper)
Unzips the elements of this `Traversable` by mapping each element to a pair
 and splitting them into two separate `Traversable` collections.

Type Parameters:
`T1` - type of the first element in the resulting pairs
`T2` - type of the second element in the resulting pairs
Parameters:
`unzipper` - a function that maps elements of this `Traversable` to pairs
Returns:
a `Tuple2` containing two `Traversable` collections with the split elements
Throws:
`NullPointerException` - if `unzipper` is null

  - 

### unzip3

<T1,
T2,
T3>
Tuple3<? extends Traversable<T1>,? extends Traversable<T2>,? extends Traversable<T3>> unzip3(@NonNull Function<? super T,Tuple3<? extends T1,? extends T2,? extends T3>> unzipper)
Unzips the elements of this `Traversable` by mapping each element to a triple
 and splitting them into three separate `Traversable` collections.

Type Parameters:
`T1` - type of the first element in the resulting triples
`T2` - type of the second element in the resulting triples
`T3` - type of the third element in the resulting triples
Parameters:
`unzipper` - a function that maps elements of this `Traversable` to triples
Returns:
a `Tuple3` containing three `Traversable` collections with the split elements
Throws:
`NullPointerException` - if `unzipper` is null

  - 

### zip

<U> Traversable<Tuple2<T,U>> zip(@NonNull Iterable<? extends U> that)
Returns a `Traversable` formed by pairing elements of this `Traversable` with elements of another
 `Iterable`. Pairing stops when either collection runs out of elements; any remaining elements in the longer
 collection are ignored.
 

 The length of the resulting `Traversable` is the minimum of the lengths of this `Traversable` and
 `that`.

Type Parameters:
`U` - the type of elements in the second half of each pair
Parameters:
`that` - an `Iterable` providing the second element of each pair
Returns:
a new `Traversable` containing pairs of corresponding elements
Throws:
`NullPointerException` - if `that` is null

  - 

### zipAll

<U> Traversable<Tuple2<T,U>> zipAll(@NonNull Iterable<? extends U> that,
 T thisElem,
 U thatElem)
Returns a `Traversable` formed by pairing elements of this `Traversable` with elements of another
 `Iterable`, filling in placeholder elements when one collection is shorter than the other.
 

 The length of the resulting `Traversable` is the maximum of the lengths of this `Traversable` and
 `that`.
 

 If this `Traversable` is shorter than `that`, `thisElem` is used as a filler. Conversely, if
 `that` is shorter, `thatElem` is used.

Type Parameters:
`U` - the type of elements in the second half of each pair
Parameters:
`that` - an `Iterable` providing the second element of each pair
`thisElem` - the element used to fill missing values if this `Traversable` is shorter than `that`
`thatElem` - the element used to fill missing values if `that` is shorter than this `Traversable`
Returns:
a new `Traversable` containing pairs of elements, including fillers as needed
Throws:
`NullPointerException` - if `that` is null

  - 

### zipWith

<U,
R> Traversable<R> zipWith(@NonNull Iterable<? extends U> that,
 BiFunction<? super T,? super U,? extends R> mapper)
Returns a `Traversable` by combining elements of this `Traversable` with elements of another
 `Iterable` using a mapping function. Pairing stops when either collection runs out of elements.
 

 The length of the resulting `Traversable` is the minimum of the lengths of this `Traversable` and
 `that`.

Type Parameters:
`U` - the type of elements in the second parameter of the mapper
`R` - the type of elements in the resulting `Traversable`
Parameters:
`that` - an `Iterable` providing the second parameter of the mapper
`mapper` - a function that combines elements from this and `that` into a new element
Returns:
a new `Traversable` containing mapped elements
Throws:
`NullPointerException` - if `that` or `mapper` is null

  - 

### zipWithIndex

Traversable<Tuple2<T,Integer>> zipWithIndex()
Zips this `Traversable` with its indices, starting at 0.

Returns:
a new `Traversable` containing each element paired with its index

  - 

### zipWithIndex

<U> Traversable<U> zipWithIndex(@NonNull BiFunction<? super T,? super Integer,? extends U> mapper)
Zips this `Traversable` with its indices and maps the resulting pairs using the provided mapper.

Type Parameters:
`U` - the type of elements in the resulting `Traversable`
Parameters:
`mapper` - a function mapping an element and its index to a new element
Returns:
a new `Traversable` containing the mapped elements
Throws:
`NullPointerException` - if `mapper` is null