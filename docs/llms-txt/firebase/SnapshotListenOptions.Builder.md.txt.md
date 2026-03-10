# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.Builder.md.txt

# SnapshotListenOptions.Builder

# SnapshotListenOptions.Builder


```
public class SnapshotListenOptions.Builder
```

<br />

*** ** * ** ***

Builder for constructing `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions` instances.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.Builder#Builder()()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.Builder#build()()` Constructs a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions` instance using the current settings in this Builder. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.Builder#setActivity(android.app.Activity)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity)` Associates an Activity with this snapshot listener's lifecycle. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.Builder#setExecutor(java.util.concurrent.Executor)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor)` Sets the executor to be used for snapshot listener callbacks. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.Builder#setMetadataChanges(com.google.firebase.firestore.MetadataChanges)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges)` Sets whether metadata-only changes should trigger snapshot events. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.Builder#setSource(com.google.firebase.firestore.ListenSource)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenSource source)` Sets the preferred source for retrieving data in snapshot listeners. |

## Public constructors

### Builder

```
public Builder()
```

## Public methods

### build

```
public @NonNull SnapshotListenOptions build()
```

Constructs a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions` instance using the current settings in this Builder.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions` | The constructed SnapshotListenOptions instance. |

### setActivity

```
public @NonNull SnapshotListenOptions.Builder setActivity(@NonNull Activity activity)
```

Associates an Activity with this snapshot listener's lifecycle. If set, the listener will automatically stop when the Activity is destroyed.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity` | The Activity to associate with the listener. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.Builder` | This Builder instance to allow chaining of method calls. |

### setExecutor

```
public @NonNull SnapshotListenOptions.Builder setExecutor(@NonNull Executor executor)
```

Sets the executor to be used for snapshot listener callbacks.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | The executor to be used. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.Builder` | This Builder instance to allow chaining of method calls. |

### setMetadataChanges

```
public @NonNull SnapshotListenOptions.Builder setMetadataChanges(@NonNull MetadataChanges metadataChanges)
```

Sets whether metadata-only changes should trigger snapshot events.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges` | The setting for metadata-only changes. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.Builder` | This Builder instance to allow chaining of method calls. |

### setSource

```
public @NonNull SnapshotListenOptions.Builder setSource(@NonNull ListenSource source)
```

Sets the preferred source for retrieving data in snapshot listeners.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenSource source` | The preferred source for data retrieval. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.Builder` | This Builder instance to allow chaining of method calls. |