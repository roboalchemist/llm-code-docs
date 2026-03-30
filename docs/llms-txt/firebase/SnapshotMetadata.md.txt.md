# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotMetadata.md.txt

# SnapshotMetadata

# SnapshotMetadata


```
public class SnapshotMetadata
```

<br />

*** ** * ** ***

Metadata about a snapshot, describing the state of the snapshot.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Public fields |
|---|---|
| `final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotMetadata#isFromCache()` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotMetadata#equals(java.lang.Object)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html obj)` |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotMetadata#hasPendingWrites()()` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotMetadata#hashCode()()` |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotMetadata#isFromCache()()` |
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotMetadata#toString()()` |

## Public fields

### isFromCache

```
public final boolean isFromCache
```

## Public methods

### equals

```
public boolean equals(@Nullable Object obj)
```

### hasPendingWrites

```
public boolean hasPendingWrites()
```

| Returns |
|---|---|
| `boolean` | true if the snapshot contains the result of local writes (for example, `set()` or `update()` calls) that have not yet been committed to the backend. If your listener has opted into metadata updates (via `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#INCLUDE`) you will receive another snapshot with `hasPendingWrites()` equal to false once the writes have been committed to the backend. |

### hashCode

```
public int hashCode()
```

### isFromCache

```
public boolean isFromCache()
```

| Returns |
|---|---|
| `boolean` | true if the snapshot was created from cached data rather than guaranteed up-to-date server data. If your listener has opted into metadata updates (via `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#INCLUDE`) you will receive another snapshot with `isFromCache()` equal to false once the client has received up-to-date data from the backend. |

### toString

```
public String toString()
```