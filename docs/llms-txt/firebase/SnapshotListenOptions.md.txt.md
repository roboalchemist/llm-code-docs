# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.md.txt

# SnapshotListenOptions

# SnapshotListenOptions


```
public final class SnapshotListenOptions
```

<br />

*** ** * ** ***

An options object that configures the behavior of `addSnapshotListener()` calls. Instances of this class control settings such as whether metadata-only changes trigger events, the preferred data source (server or cache), and the executor for listener callbacks.

## Summary

| ### Nested types |
|---|
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.Builder` Builder for constructing `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions` instances. |

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/android/app/Activity.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#activity()` The activity to scope the listener to. |
| `final https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#executor()` The executor to use to call the listener. |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#metadataChanges()` Indicates whether metadata-only changes should trigger snapshot events. |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenSource` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#source()` Specifies the data source for the listener. |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html o)` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/app/Activity.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#getActivity()()` Returns the optional Activity that scopes this snapshot listener's lifespan. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#getExecutor()()` Returns the executor that will be used to execute the snapshot listener's callback. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#getMetadataChanges()()` Returns the setting for whether metadata-only changes should trigger snapshot events. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenSource` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#getSource()()` Returns the preferred source for retrieving data in snapshot listeners. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#hashCode()()` |
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions#toString()()` |

## Public fields

### activity

```
public final Activity activity
```

The activity to scope the listener to.

### executor

```
public final Executor executor
```

The executor to use to call the listener.

### metadataChanges

```
public final MetadataChanges metadataChanges
```

Indicates whether metadata-only changes should trigger snapshot events.

### source

```
public final ListenSource source
```

Specifies the data source for the listener.

## Public methods

### equals

```
public boolean equals(Object o)
```

### getActivity

```
public @Nullable Activity getActivity()
```

Returns the optional Activity that scopes this snapshot listener's lifespan. If provided, the listener will automatically stop receiving events when the activity is destroyed.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/app/Activity.html` | The Activity associated with this listener, or null if no activity is set. |

### getExecutor

```
public @NonNull Executor getExecutor()
```

Returns the executor that will be used to execute the snapshot listener's callback.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | The executor for snapshot listener callbacks. |

### getMetadataChanges

```
public @NonNull MetadataChanges getMetadataChanges()
```

Returns the setting for whether metadata-only changes should trigger snapshot events.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges` | The setting object for metadata-only changes. |

### getSource

```
public @NonNull ListenSource getSource()
```

Returns the preferred source for retrieving data in snapshot listeners.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenSource` | The listen source for retrieving data. |

### hashCode

```
public int hashCode()
```

### toString

```
public String toString()
```