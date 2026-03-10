# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress.md.txt

# LoadBundleTaskProgress

# LoadBundleTaskProgress


```
public final class LoadBundleTaskProgress
```

<br />

*** ** * ** ***

Represents a progress update or a final state from loading bundles.

## Summary

| ### Nested types |
|---|
| `public enum https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState` Represents the state of bundle loading tasks. |

| ### Public fields |
|---|---|
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#bytesLoaded()` |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#documentsLoaded()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Exception.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#exception()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#taskState()` |
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#totalBytes()` |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#totalDocuments()` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html o)` |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#getBytesLoaded()()` Returns how many bytes have been loaded. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#getDocumentsLoaded()()` Returns how many documents have been loaded. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Exception.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#getException()()` If the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask` failed, returns the exception. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#getTaskState()()` Returns the current state of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask`. |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#getTotalBytes()()` Returns the total number of bytes in the bundle. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#getTotalDocuments()()` Returns the total number of documents in the bundle. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress#hashCode()()` |

## Public fields

### bytesLoaded

```
public final long bytesLoaded
```

### documentsLoaded

```
public final int documentsLoaded
```

### exception

```
public final @Nullable Exception exception
```

### taskState

```
public final @NonNull LoadBundleTaskProgress.TaskState taskState
```

### totalBytes

```
public final long totalBytes
```

### totalDocuments

```
public final int totalDocuments
```

## Public methods

### equals

```
public boolean equals(Object o)
```

### getBytesLoaded

```
public long getBytesLoaded()
```

Returns how many bytes have been loaded.

### getDocumentsLoaded

```
public int getDocumentsLoaded()
```

Returns how many documents have been loaded.

### getException

```
public @Nullable Exception getException()
```

If the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask` failed, returns the exception. Otherwise, returns `null`.

### getTaskState

```
public @NonNull LoadBundleTaskProgress.TaskState getTaskState()
```

Returns the current state of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask`.

### getTotalBytes

```
public long getTotalBytes()
```

Returns the total number of bytes in the bundle. Returns 0 if the bundle failed to parse.

### getTotalDocuments

```
public int getTotalDocuments()
```

Returns the total number of documents in the bundle. Returns 0 if the bundle failed to parse.

### hashCode

```
public int hashCode()
```