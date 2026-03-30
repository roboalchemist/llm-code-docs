# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscription.md.txt

# QuerySubscription

# QuerySubscription


```
interface QuerySubscription<Data : Any?, Variables : Any?>
```

<br />

*** ** * ** ***

A facility to subscribe to a query to be notified of updates to the query's data when the query is executed.

### Notifications are *not* realtime

At this time the notifications are *not* realtime, and are *not* pushed from the server. Instead, the notifications are sent whenever the query is explicitly executed by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#execute()`.

### Safe for concurrent use

All methods and properties of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscription` are thread-safe and may be safely called and/or accessed concurrently from multiple threads and/or coroutines.

### Not stable for inheritance

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscription` interface is *not* stable for inheritance in third-party libraries, as new methods might be added to this interface or contracts of the existing methods can be changed.

## Summary

| ### Public functions |
|---|---|
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscription#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Compares this object with another object for equality, using the `===` operator. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscription#hashCode()()` Calculates and returns the hash code for this object. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscription#toString()()` Returns a string representation of this object, useful for debugging. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscriptionResult<Data, Variables>>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscription#flow()` A cold flow that collects the query results as they become available. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef<Data, Variables>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscription#query()` The query whose results this object subscribes. |

## Public functions

### equals

```
operator fun equals(other: Any?): Boolean
```

Compares this object with another object for equality, using the `===` operator.

The implementation of this method simply uses referential equality. That is, two instances of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscription` compare equal using this method if, and only if, they refer to the same object, as determined by the `===` operator.

| Parameters |
|---|---|
| `other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The object to compare to this for equality. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `other === this` |

### hashCode

```
fun hashCode(): Int
```

Calculates and returns the hash code for this object.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | the hash code for this object. |

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

### flow

```
val flow: Flow<QuerySubscriptionResult<Data, Variables>>
```

A cold flow that collects the query results as they become available.

At this time the updates are *not* realtime, and are *not* pushed from the server. Instead, updates are sent whenever the query is explicitly executed by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#execute()`.

### query

```
val query: QueryRef<Data, Variables>
```

The query whose results this object subscribes.