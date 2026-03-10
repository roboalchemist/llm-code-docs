# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.InProgress.md.txt

# TaskState.InProgress

# TaskState.InProgress


```
class TaskState.InProgress<T : Any?> : TaskState
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.storage.TaskState](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState) ||
|   | ↳ | [com.google.firebase.storage.TaskState.InProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.InProgress) |

*** ** * ** ***

Called periodically as data is transferred and can be used to populate an upload/download indicator.

## Summary

| ### Public constructors |
|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.InProgress#InProgress(kotlin.Any)(snapshot: T)` |

| ### Public properties |
|---|---|
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.InProgress#snapshot()` |

## Public constructors

### InProgress

```
<T : Any?> InProgress(snapshot: T)
```

## Public properties

### snapshot

```
val snapshot: T
```