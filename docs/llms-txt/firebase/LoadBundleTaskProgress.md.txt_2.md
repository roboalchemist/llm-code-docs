# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress.md.txt

# LoadBundleTaskProgress

# LoadBundleTaskProgress


```
class LoadBundleTaskProgress
```

<br />

*** ** * ** ***

Represents a progress update or a final state from loading bundles.

## Summary

| ### Nested types |
|---|
| `enum https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState` Represents the state of bundle loading tasks. |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress#equals(java.lang.Object)(o: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress#hashCode()()` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress#bytesLoaded()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress#documentsLoaded()` |
| `https://developer.android.com/reference/kotlin/java/lang/Exception.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress#exception()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress#taskState()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress#totalBytes()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress#totalDocuments()` |

## Public functions

### equals

```
fun equals(o: Any!): Boolean
```

### hashCode

```
fun hashCode(): Int
```

## Public properties

### bytesLoaded

```
val bytesLoaded: Long
```

### documentsLoaded

```
val documentsLoaded: Int
```

### exception

```
val exception: Exception?
```

### taskState

```
val taskState: LoadBundleTaskProgress.TaskState
```

### totalBytes

```
val totalBytes: Long
```

### totalDocuments

```
val totalDocuments: Int
```