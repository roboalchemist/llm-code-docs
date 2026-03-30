# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.md.txt

# TaskState

# TaskState


```
abstract class TaskState<T : Any?>
```

<br />

Known direct subclasses [TaskState.InProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.InProgress), [TaskState.Paused](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.Paused)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.InProgress` | Called periodically as data is transferred and can be used to populate an upload/download indicator. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.Paused` | Called any time the upload/download is paused. |

*** ** * ** ***

Used to emit events about the progress of storage tasks.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.InProgress<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState` Called periodically as data is transferred and can be used to populate an upload/download indicator. |
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.Paused<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState` Called any time the upload/download is paused. |