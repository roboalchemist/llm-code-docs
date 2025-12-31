# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/TaskState.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ktx/TaskState.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ktx/TaskState.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ktx/TaskState.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.md.txt

# TaskState

# TaskState


```
abstract class TaskState<TÂ :Â Any?>
```

<br />

Known direct subclasses  
[TaskState.InProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.InProgress), [TaskState.Paused](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.Paused)  

|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [TaskState.InProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.InProgress) | Called periodically as data is transferred and can be used to populate an upload/download indicator. |
| [TaskState.Paused](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.Paused)         | Called any time the upload/download is paused.                                                       |

*** ** * ** ***

Used to emit events about the progress of storage tasks.

## Summary

|                                                                                                                                                                                                          ### Nested types                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `class `[TaskState.InProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.InProgress)`<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?> : `[TaskState](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState) Called periodically as data is transferred and can be used to populate an upload/download indicator. |
| `class `[TaskState.Paused](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.Paused)`<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?> : `[TaskState](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState) Called any time the upload/download is paused.                                                               |