# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask.md.txt

# ControllableTask

# ControllableTask


```
abstract class ControllableTask<StateT> : CancellableTask
```

<br />

|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) ||||
| ↳ | [com.google.android.gms.tasks.Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) |||
|   | ↳ | [com.google.firebase.storage.CancellableTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/CancellableTask) ||
|   |   | ↳ | [com.google.firebase.storage.ControllableTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask) |

Known direct subclasses [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask` | A controllable Task that has a synchronized state machine. |

Known indirect subclasses [FileDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask), [StreamDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask), [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask` | A task that downloads bytes of a GCS blob to a specified File. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask` | A task that downloads bytes of a GCS blob. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` | An controllable task that uploads and fires events for success, progress and failure. |

*** ** * ** ***

Represents an asynchronous operation that can be paused, resumed and canceled. This task also receives progress and other state change notifications.

| Parameters |
|---|---|
| `<StateT>` | the type of state this operation returns in events. |

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask#ControllableTask()()` |

| ### Public functions |
|---|---|
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask<StateT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask#addOnPausedListener(com.google.firebase.storage.OnPausedListener<? super StateT>)(listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnPausedListener<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Adds a listener that is called when the Task becomes paused. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask<StateT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask#addOnPausedListener(android.app.Activity,com.google.firebase.storage.OnPausedListener<? super StateT>)(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnPausedListener<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Adds a listener that is called when the Task becomes paused. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask<StateT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask#addOnPausedListener(java.util.concurrent.Executor,com.google.firebase.storage.OnPausedListener<? super StateT>)(executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnPausedListener<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Adds a listener that is called when the Task becomes paused. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask#isPaused()()` |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask#pause()()` Attempts to pause the task. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask#resume()()` Attempts to resume this task. |

| ### Inherited functions |
|---|
| From [com.google.firebase.storage.CancellableTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/CancellableTask) |---|---| | `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/CancellableTask<StateT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/CancellableTask#addOnProgressListener(com.google.firebase.storage.OnProgressListener<? super StateT>)(listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnProgressListener<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Adds a listener that is called periodically while the ControllableTask executes. | | `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/CancellableTask<StateT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/CancellableTask#addOnProgressListener(android.app.Activity,com.google.firebase.storage.OnProgressListener<? super StateT>)( activity: https://developer.android.com/reference/kotlin/android/app/Activity.html, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnProgressListener<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!> )` Adds a listener that is called periodically while the ControllableTask executes. | | `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/CancellableTask<StateT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/CancellableTask#addOnProgressListener(java.util.concurrent.Executor,com.google.firebase.storage.OnProgressListener<? super StateT>)( executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnProgressListener<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!> )` Adds a listener that is called periodically while the ControllableTask executes. | | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/CancellableTask#cancel()()` Attempts to cancel the task. | | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/CancellableTask#isCanceled()()` | | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/CancellableTask#isInProgress()()` | |
| From [com.google.android.gms.tasks.Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) |---|---| | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult!>!` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnCanceledListener-com.google.android.gms.tasks.OnCanceledListener-(p: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html!)` | | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult!>!` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnCompleteListener-com.google.android.gms.tasks.OnCompleteListener&lt;TResult&gt;-(p: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html<TResult!>!)` | | `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult!>!` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnFailureListener-com.google.android.gms.tasks.OnFailureListener-(p: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html!)` | | `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult!>!` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnSuccessListener-com.google.android.gms.tasks.OnSuccessListener&lt;? super TResult&gt;-(p: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>!)` | | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult!>!` | `<TContinuationResult> https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#continueWith-com.google.android.gms.tasks.Continuation&lt;TResult,TContinuationResult&gt;-( p: https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<TResult!, TContinuationResult!>! )` | | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult!>!` | `<TContinuationResult> https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#continueWithTask-com.google.android.gms.tasks.Continuation&lt;TResult,com.google.android.gms.tasks.Task&lt;TContinuationResult&gt;&gt;-( p: https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<TResult!, https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult!>!>! )` | | `abstract https://developer.android.com/reference/kotlin/java/lang/Exception.html!` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#getException--()` | | `abstract TResult!` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#getResult--()` | | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isCanceled--()` | | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isComplete--()` | | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isSuccessful--()` | | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult!>!` | `<TContinuationResult> https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#onSuccessTask-com.google.android.gms.tasks.SuccessContinuation&lt;TResult,TContinuationResult&gt;-( p: https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html<TResult!, TContinuationResult!>! )` | |

## Public constructors

### ControllableTask

```
ControllableTask()
```

## Public functions

### addOnPausedListener

```
abstract fun addOnPausedListener(listener: OnPausedListener<Any!>): ControllableTask<StateT!>
```

Adds a listener that is called when the Task becomes paused.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask<StateT!>` | this Task |

### addOnPausedListener

```
abstract fun addOnPausedListener(activity: Activity, listener: OnPausedListener<Any!>): ControllableTask<StateT!>
```

Adds a listener that is called when the Task becomes paused.

| Parameters |
|---|---|
| `activity: https://developer.android.com/reference/kotlin/android/app/Activity.html` | When the supplied `https://developer.android.com/reference/kotlin/android/app/Activity.html` stops, this listener will automatically be removed. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask<StateT!>` | this Task |

### addOnPausedListener

```
abstract fun addOnPausedListener(executor: Executor, listener: OnPausedListener<Any!>): ControllableTask<StateT!>
```

Adds a listener that is called when the Task becomes paused.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | the executor to use to call the listener |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask<StateT!>` | this Task |

### isPaused

```
abstract fun isPaused(): Boolean
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true if the task has been paused. |

### pause

```
abstract fun pause(): Boolean
```

Attempts to pause the task. A paused task can later be resumed.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true if this task was successfully paused or is in the process of being paused. Returns false if the task is already completed or in a state that cannot be paused. |

### resume

```
abstract fun resume(): Boolean
```

Attempts to resume this task.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true if the task is successfully resumed or is in the process of being resumed. Returns false if the task is already completed or in a state that cannot be resumed. |