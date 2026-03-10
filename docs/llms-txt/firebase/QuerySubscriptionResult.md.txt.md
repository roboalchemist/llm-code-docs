# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscriptionResult.md.txt

# QuerySubscriptionResult

# QuerySubscriptionResult


```
interface QuerySubscriptionResult<Data : Any?, Variables : Any?>
```

<br />

*** ** * ** ***

The result of a query's execution, as notified to a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscription`.

### Safe for concurrent use

All methods and properties of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscriptionResult` are thread-safe and may be safely called and/or accessed concurrently from multiple threads and/or coroutines.

### Not stable for inheritance

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscriptionResult` interface is *not* stable for inheritance in third-party libraries, as new methods might be added to this interface or contracts of the existing methods can be changed.

## Summary

| ### Public functions |
|---|---|
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscriptionResult#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Compares this object with another object for equality. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscriptionResult#hashCode()()` Calculates and returns the hash code for this object. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscriptionResult#toString()()` Returns a string representation of this object, useful for debugging. |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef<Data, Variables>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscriptionResult#query()` The query that was executed, whose result is captured in this object. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-result/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryResult<Data, Variables>>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscriptionResult#result()` The result of the query execution: a successful result if the query was executed successfully, or a failure if the query's execution failed. |

## Public functions

### equals

```
operator fun equals(other: Any?): Boolean
```

Compares this object with another object for equality.

| Parameters |
|---|---|
| `other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The object to compare to this for equality. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true if, and only if, the other object is an instance of the same implementation of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscriptionResult` whose public properties compare equal using the `==` operator to the corresponding properties of this object. |

### hashCode

```
fun hashCode(): Int
```

Calculates and returns the hash code for this object.

The hash code is *not* guaranteed to be stable across application restarts.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | the hash code for this object, that incorporates the values of this object's public properties. |

### toString

```
fun toString(): String
```

Returns a string representation of this object, useful for debugging.

The string representation is *not* guaranteed to be stable and may change without notice at any time. Therefore, the only recommended usage of the returned string is debugging and/or logging. Namely, parsing the returned string or storing the returned string in non-volatile storage should generally be avoided in order to be robust in case that the string representation changes.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | a string representation of this object, which includes the class name and the values of all public properties. |

## Public properties

### query

```
val query: QueryRef<Data, Variables>
```

The query that was executed, whose result is captured in this object.

### result

```
val result: Result<QueryResult<Data, Variables>>
```

The result of the query execution: a successful result if the query was executed successfully, or a failure if the query's execution failed.