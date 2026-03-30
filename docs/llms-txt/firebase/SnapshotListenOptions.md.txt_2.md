# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.md.txt

# SnapshotListenOptions

# SnapshotListenOptions


```
class SnapshotListenOptions
```

<br />

*** ** * ** ***

An options object that configures the behavior of `addSnapshotListener()` calls. Instances of this class control settings such as whether metadata-only changes trigger events, the preferred data source (server or cache), and the executor for listener callbacks.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder` Builder for constructing `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions` instances. |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions#equals(java.lang.Object)(o: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions#hashCode()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions#toString()()` |

| ### Public properties |
|---|---|
| `https://developer.android.com/reference/kotlin/android/app/Activity.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions#activity()` The activity to scope the listener to. |
| `https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions#executor()` The executor to use to call the listener. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions#metadataChanges()` Indicates whether metadata-only changes should trigger snapshot events. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenSource!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions#source()` Specifies the data source for the listener. |

## Public functions

### equals

```
fun equals(o: Any!): Boolean
```

### hashCode

```
fun hashCode(): Int
```

### toString

```
fun toString(): String!
```

## Public properties

### activity

```
val activity: Activity!
```

The activity to scope the listener to.

### executor

```
val executor: Executor!
```

The executor to use to call the listener.

### metadataChanges

```
val metadataChanges: MetadataChanges!
```

Indicates whether metadata-only changes should trigger snapshot events.

### source

```
val source: ListenSource!
```

Specifies the data source for the listener.