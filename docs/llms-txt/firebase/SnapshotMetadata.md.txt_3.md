# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotMetadata.md.txt

# SnapshotMetadata

# SnapshotMetadata


```
class SnapshotMetadata
```

<br />

*** ** * ** ***

Metadata about a snapshot, describing the state of the snapshot.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotMetadata#equals(java.lang.Object)(obj: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotMetadata#hasPendingWrites()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotMetadata#hashCode()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotMetadata#toString()()` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotMetadata#isFromCache()` |

## Public functions

### equals

```
fun equals(obj: Any?): Boolean
```

### hasPendingWrites

```
fun hasPendingWrites(): Boolean
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true if the snapshot contains the result of local writes (for example, `set()` or `update()` calls) that have not yet been committed to the backend. If your listener has opted into metadata updates (via `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges#INCLUDE`) you will receive another snapshot with `hasPendingWrites()` equal to false once the writes have been committed to the backend. |

### hashCode

```
fun hashCode(): Int
```

### toString

```
fun toString(): String!
```

## Public properties

### isFromCache

```
val isFromCache: Boolean
```