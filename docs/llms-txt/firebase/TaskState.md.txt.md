# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/TaskState.md.txt

# TaskState

# TaskState


```
public abstract class TaskState<T extends Object>
```

<br />

Known direct subclasses [TaskState.InProgress](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/TaskState.InProgress), [TaskState.Paused](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/TaskState.Paused)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/TaskState.InProgress` | Called periodically as data is transferred and can be used to populate an upload/download indicator. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/TaskState.Paused` | Called any time the upload/download is paused. |

*** ** * ** ***

Used to emit events about the progress of storage tasks.

## Summary

| ### Nested types |
|---|
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/storage/TaskState.InProgress<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> extends https://firebase.google.com/docs/reference/android/com/google/firebase/storage/TaskState` Called periodically as data is transferred and can be used to populate an upload/download indicator. |
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/storage/TaskState.Paused<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> extends https://firebase.google.com/docs/reference/android/com/google/firebase/storage/TaskState` Called any time the upload/download is paused. |