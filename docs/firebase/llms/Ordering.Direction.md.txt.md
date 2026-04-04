# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Direction.md.txt

# Ordering.Direction

# Ordering.Direction


```
public enum Ordering.Direction extends Enum
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html) ||
|   | ↳ | [com.google.firebase.firestore.pipeline.Ordering.Direction](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Direction) |

*** ** * ** ***

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Direction#ASCENDING` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Direction#DESCENDING` |   |

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/[JVM root]/<Error class: unknown class>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Direction#proto()` |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Direction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Direction#valueOf(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Returns the enum constant of this type with the specified name. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Ordering.Direction[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Direction#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### ASCENDING

```
Ordering.Direction Ordering.Direction.ASCENDING
```

### DESCENDING

```
Ordering.Direction Ordering.Direction.DESCENDING
```

## Public fields

### proto

```
public final @NonNull <Error class: unknown class> proto
```

## Public methods

### valueOf

```
public final @NonNull Ordering.Direction valueOf(@NonNull String value)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Throws |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html kotlin.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
public final @NonNull Ordering.Direction[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.