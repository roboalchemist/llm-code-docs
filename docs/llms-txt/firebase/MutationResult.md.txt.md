# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/MutationResult.md.txt

# MutationResult

# MutationResult


```
interface MutationResult<Data : Any?, Variables : Any?> : OperationResult
```

<br />

*** ** * ** ***

A specialization of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationResult` for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/MutationRef`.

### Safe for concurrent use

All methods and properties of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/MutationResult` are thread-safe and may be safely called and/or accessed concurrently from multiple threads and/or coroutines.

### Not stable for inheritance

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/MutationResult` interface is *not* stable for inheritance in third-party libraries, as new methods might be added to this interface or contracts of the existing methods can be changed.

## Summary

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/MutationRef<Data, Variables>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/MutationResult#ref()` The operation that produced this result. |

| ### Inherited functions |
|---|
| From [com.google.firebase.dataconnect.OperationResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationResult) |---|---| | `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationResult#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Compares this object with another object for equality. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationResult#hashCode()()` Calculates and returns the hash code for this object. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationResult#toString()()` Returns a string representation of this object, useful for debugging. | |

| ### Inherited properties |
|---|
| From [com.google.firebase.dataconnect.OperationResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationResult) |---|---| | `Data` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationResult#data()` The response data for the operation. | |

## Public properties

### ref

```
val ref: MutationRef<Data, Variables>
```

The operation that produced this result.