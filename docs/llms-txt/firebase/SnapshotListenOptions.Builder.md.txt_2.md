# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder.md.txt

# SnapshotListenOptions.Builder

# SnapshotListenOptions.Builder


```
class SnapshotListenOptions.Builder
```

<br />

*** ** * ** ***

Builder for constructing `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions` instances.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder#Builder()()` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder#build()()` Constructs a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions` instance using the current settings in this Builder. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder#setActivity(android.app.Activity)(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html)` Associates an Activity with this snapshot listener's lifecycle. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder#setExecutor(java.util.concurrent.Executor)(executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)` Sets the executor to be used for snapshot listener callbacks. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder#setMetadataChanges(com.google.firebase.firestore.MetadataChanges)(metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges)` Sets whether metadata-only changes should trigger snapshot events. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder#setSource(com.google.firebase.firestore.ListenSource)(source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenSource)` Sets the preferred source for retrieving data in snapshot listeners. |

## Public constructors

### Builder

```
Builder()
```

## Public functions

### build

```
fun build(): SnapshotListenOptions
```

Constructs a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions` instance using the current settings in this Builder.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions` | The constructed SnapshotListenOptions instance. |

### setActivity

```
fun setActivity(activity: Activity): SnapshotListenOptions.Builder
```

Associates an Activity with this snapshot listener's lifecycle. If set, the listener will automatically stop when the Activity is destroyed.

| Parameters |
|---|---|
| `activity: https://developer.android.com/reference/kotlin/android/app/Activity.html` | The Activity to associate with the listener. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder` | This Builder instance to allow chaining of method calls. |

### setExecutor

```
fun setExecutor(executor: Executor): SnapshotListenOptions.Builder
```

Sets the executor to be used for snapshot listener callbacks.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | The executor to be used. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder` | This Builder instance to allow chaining of method calls. |

### setMetadataChanges

```
fun setMetadataChanges(metadataChanges: MetadataChanges): SnapshotListenOptions.Builder
```

Sets whether metadata-only changes should trigger snapshot events.

| Parameters |
|---|---|
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges` | The setting for metadata-only changes. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder` | This Builder instance to allow chaining of method calls. |

### setSource

```
fun setSource(source: ListenSource): SnapshotListenOptions.Builder
```

Sets the preferred source for retrieving data in snapshot listeners.

| Parameters |
|---|---|
| `source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenSource` | The preferred source for data retrieval. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder` | This Builder instance to allow chaining of method calls. |