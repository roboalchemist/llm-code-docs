# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.md.txt

# StorageTask

# StorageTask


```
abstract class StorageTask<ResultT : StorageTask.ProvideError?> : ControllableTask
```

<br />

|---|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||||
| ↳ | [com.google.android.gms.tasks.Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) ||||
|   | ↳ | [com.google.firebase.storage.CancellableTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/CancellableTask) |||
|   |   | ↳ | [com.google.firebase.storage.ControllableTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask) ||
|   |   |   | ↳ | [com.google.firebase.storage.StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask) |

Known direct subclasses [FileDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask), [StreamDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask), [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask` | A task that downloads bytes of a GCS blob to a specified File. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask` | A task that downloads bytes of a GCS blob. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` | An controllable task that uploads and fires events for success, progress and failure. |

*** ** * ** ***

A controllable Task that has a synchronized state machine.

## Summary

| ### Nested types |
|---|
| `protected interface https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.ProvideError` An object that returns an exception. |
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.ProvideError` Base class for state. |

| ### Protected constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#StorageTask()()` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnCanceledListener(com.google.android.gms.tasks.OnCanceledListener)(listener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html)` Adds a listener that is called if the Task is canceled. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnCanceledListener(android.app.Activity,com.google.android.gms.tasks.OnCanceledListener)(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html, listener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html)` Adds an Activity-scoped listener that is called if the Task is canceled. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnCanceledListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnCanceledListener)(executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, listener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html)` Adds a listener that is called if the Task is canceled. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnCompleteListener(com.google.android.gms.tasks.OnCompleteListener<ResultT>)(listener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html<ResultT!>)` Adds a listener that is called when the Task succeeds or fails. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnCompleteListener(android.app.Activity,com.google.android.gms.tasks.OnCompleteListener<ResultT>)( activity: https://developer.android.com/reference/kotlin/android/app/Activity.html, listener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html<ResultT!> )` Adds a listener that is called when the Task succeeds or fails. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnCompleteListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnCompleteListener<ResultT>)( executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, listener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html<ResultT!> )` Adds a listener that is called when the Task succeeds or fails. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnFailureListener(com.google.android.gms.tasks.OnFailureListener)(listener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html)` Adds a listener that is called if the Task fails. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnFailureListener(android.app.Activity,com.google.android.gms.tasks.OnFailureListener)(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html, listener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html)` Adds a listener that is called if the Task fails. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnFailureListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnFailureListener)(executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, listener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html)` Adds a listener that is called if the Task fails. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnPausedListener(com.google.firebase.storage.OnPausedListener<? super ResultT>)(listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnPausedListener<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Adds a listener that is called when the Task becomes paused. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnPausedListener(android.app.Activity,com.google.firebase.storage.OnPausedListener<? super ResultT>)(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnPausedListener<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Adds a listener that is called when the Task becomes paused. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnPausedListener(java.util.concurrent.Executor,com.google.firebase.storage.OnPausedListener<? super ResultT>)(executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnPausedListener<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Adds a listener that is called when the Task becomes paused. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnProgressListener(com.google.firebase.storage.OnProgressListener<? super ResultT>)(listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnProgressListener<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Adds a listener that is called periodically while the ControllableTask executes. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnProgressListener(android.app.Activity,com.google.firebase.storage.OnProgressListener<? super ResultT>)( activity: https://developer.android.com/reference/kotlin/android/app/Activity.html, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnProgressListener<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!> )` Adds a listener that is called periodically while the ControllableTask executes. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnProgressListener(java.util.concurrent.Executor,com.google.firebase.storage.OnProgressListener<? super ResultT>)( executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnProgressListener<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!> )` Adds a listener that is called periodically while the ControllableTask executes. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnSuccessListener(com.google.android.gms.tasks.OnSuccessListener<? super ResultT>)(listener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Adds a listener that is called if the Task completes successfully. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnSuccessListener(android.app.Activity,com.google.android.gms.tasks.OnSuccessListener<? super ResultT>)( activity: https://developer.android.com/reference/kotlin/android/app/Activity.html, listener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!> )` Adds a listener that is called if the Task completes successfully. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnSuccessListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnSuccessListener<? super ResultT>)( executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, listener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!> )` Adds a listener that is called if the Task completes successfully. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#cancel()()` Attempts to cancel the task. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<ContinuationResultT!>` | `<ContinuationResultT> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#continueWith(com.google.android.gms.tasks.Continuation<ResultT,ContinuationResultT>)( continuation: https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<ResultT!, ContinuationResultT!> )` Returns a new Task that will be completed with the result of applying the specified Continuation to this Task. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<ContinuationResultT!>` | `<ContinuationResultT> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#continueWith(java.util.concurrent.Executor,com.google.android.gms.tasks.Continuation<ResultT,ContinuationResultT>)( executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, continuation: https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<ResultT!, ContinuationResultT!> )` Returns a new Task that will be completed with the result of applying the specified Continuation to this Task. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<ContinuationResultT!>` | `<ContinuationResultT> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#continueWithTask(com.google.android.gms.tasks.Continuation<ResultT,com.google.android.gms.tasks.Task<ContinuationResultT>>)( continuation: https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<ResultT!, https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<ContinuationResultT!>!> )` Returns a new Task that will be completed with the result of applying the specified Continuation to this Task. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<ContinuationResultT!>` | `<ContinuationResultT> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#continueWithTask(java.util.concurrent.Executor,com.google.android.gms.tasks.Continuation<ResultT,com.google.android.gms.tasks.Task<ContinuationResultT>>)( executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, continuation: https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<ResultT!, https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<ContinuationResultT!>!> )` Returns a new Task that will be completed with the result of applying the specified Continuation to this Task. |
| `https://developer.android.com/reference/kotlin/java/lang/Exception.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#getException()()` Returns the exception that caused the Task to fail. |
| `ResultT` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#getResult()()` Gets the result of the Task, if it has already completed. |
| `ResultT` | `<X : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#getResult(java.lang.Class<X>)(exceptionType: https://developer.android.com/reference/kotlin/java/lang/Class.html<X!>)` Gets the result of the Task, if it has already completed. |
| `ResultT` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#getSnapshot()()` Returns the current state of the task. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#isCanceled()()` Returns `true` if the task has been canceled. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#isComplete()()` Returns `true` if the Task is complete; `false` otherwise. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#isInProgress()()` Returns `true` if the task is currently running. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#isPaused()()` Returns `true` if the task has been paused. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#isSuccessful()()` Returns `true` if the Task has completed successfully; `false` otherwise. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<ContinuationResultT!>` | `<ContinuationResultT> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#onSuccessTask(com.google.android.gms.tasks.SuccessContinuation<ResultT,ContinuationResultT>)( continuation: https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html<ResultT!, ContinuationResultT!> )` Returns a new Task that will be completed with the result of applying the specified SuccessContinuation to this Task when this Task completes successfully. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<ContinuationResultT!>` | `<ContinuationResultT> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#onSuccessTask(java.util.concurrent.Executor,com.google.android.gms.tasks.SuccessContinuation<ResultT,ContinuationResultT>)( executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, continuation: https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html<ResultT!, ContinuationResultT!> )` Returns a new Task that will be completed with the result of applying the specified SuccessContinuation to this Task when this Task completes successfully. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#pause()()` Attempts to pause the task. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#removeOnCanceledListener(com.google.android.gms.tasks.OnCanceledListener)(listener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html)` Removes a listener. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#removeOnCompleteListener(com.google.android.gms.tasks.OnCompleteListener<ResultT>)(listener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html<ResultT!>)` Removes a listener. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#removeOnFailureListener(com.google.android.gms.tasks.OnFailureListener)(listener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html)` Removes a listener. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#removeOnPausedListener(com.google.firebase.storage.OnPausedListener<? super ResultT>)(listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnPausedListener<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Removes a listener. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#removeOnProgressListener(com.google.firebase.storage.OnProgressListener<? super ResultT>)(listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnProgressListener<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Removes a listener. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#removeOnSuccessListener(com.google.android.gms.tasks.OnSuccessListener<? super ResultT>)(listener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Removes a listener. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#resume()()` Attempts to resume a paused task. |

| ### Protected functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#onCanceled()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#onFailure()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#onPaused()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#onProgress()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#onQueued()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#onSuccess()()` |

| ### Protected properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#syncObject()` |

| ### Extension properties |
|---|---|
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState<T>>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<T>.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#(com.google.firebase.storage.StorageTask).taskState()` Starts listening to this task's progress and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |

| ### Inherited functions |
|---|
| From [com.google.android.gms.tasks.Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) |---|---| | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isCanceled--()` | |

## Protected constructors

### StorageTask

```
protected StorageTask()
```

## Public functions

### addOnCanceledListener

```
fun addOnCanceledListener(listener: OnCanceledListener): StorageTask<ResultT!>
```

Adds a listener that is called if the Task is canceled.

The listener will be called on main application thread. If the Task has already been canceled, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | this Task |

### addOnCanceledListener

```
fun addOnCanceledListener(activity: Activity, listener: OnCanceledListener): StorageTask<ResultT!>
```

Adds an Activity-scoped listener that is called if the Task is canceled.

The listener will be called on main application thread. If the Task has already been canceled, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

The listener will be automatically removed during `https://developer.android.com/reference/kotlin/android/app/Activity.html#onStop--`.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | this Task |

### addOnCanceledListener

```
fun addOnCanceledListener(executor: Executor, listener: OnCanceledListener): StorageTask<ResultT!>
```

Adds a listener that is called if the Task is canceled.

If the Task has already been canceled, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | the executor to use to call the listener |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | this Task |

### addOnCompleteListener

```
fun addOnCompleteListener(listener: OnCompleteListener<ResultT!>): StorageTask<ResultT!>
```

Adds a listener that is called when the Task succeeds or fails.

The listener will be called on main application thread. If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | this Task |

### addOnCompleteListener

```
fun addOnCompleteListener(
    activity: Activity,
    listener: OnCompleteListener<ResultT!>
): StorageTask<ResultT!>
```

Adds a listener that is called when the Task succeeds or fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `activity: https://developer.android.com/reference/kotlin/android/app/Activity.html` | When the supplied `https://developer.android.com/reference/kotlin/android/app/Activity.html` stops, this listener will automatically be removed. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | this Task |

### addOnCompleteListener

```
fun addOnCompleteListener(
    executor: Executor,
    listener: OnCompleteListener<ResultT!>
): StorageTask<ResultT!>
```

Adds a listener that is called when the Task succeeds or fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | the executor to use to call the listener |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | this Task |

### addOnFailureListener

```
fun addOnFailureListener(listener: OnFailureListener): StorageTask<ResultT!>
```

Adds a listener that is called if the Task fails.

The listener will be called on main application thread. If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | this Task |

### addOnFailureListener

```
fun addOnFailureListener(activity: Activity, listener: OnFailureListener): StorageTask<ResultT!>
```

Adds a listener that is called if the Task fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `activity: https://developer.android.com/reference/kotlin/android/app/Activity.html` | When the supplied `https://developer.android.com/reference/kotlin/android/app/Activity.html` stops, this listener will automatically be removed. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | this Task |

### addOnFailureListener

```
fun addOnFailureListener(executor: Executor, listener: OnFailureListener): StorageTask<ResultT!>
```

Adds a listener that is called if the Task fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | the executor to use to call the listener |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | this Task |

### addOnPausedListener

```
fun addOnPausedListener(listener: OnPausedListener<Any!>): StorageTask<ResultT!>
```

Adds a listener that is called when the Task becomes paused.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | this Task |

### addOnPausedListener

```
fun addOnPausedListener(activity: Activity, listener: OnPausedListener<Any!>): StorageTask<ResultT!>
```

Adds a listener that is called when the Task becomes paused.

| Parameters |
|---|---|
| `activity: https://developer.android.com/reference/kotlin/android/app/Activity.html` | When the supplied `https://developer.android.com/reference/kotlin/android/app/Activity.html` stops, this listener will automatically be removed. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | this Task |

### addOnPausedListener

```
fun addOnPausedListener(executor: Executor, listener: OnPausedListener<Any!>): StorageTask<ResultT!>
```

Adds a listener that is called when the Task becomes paused.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | the executor to use to call the listener |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | this Task |

### addOnProgressListener

```
fun addOnProgressListener(listener: OnProgressListener<Any!>): StorageTask<ResultT!>
```

Adds a listener that is called periodically while the ControllableTask executes.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | this Task |

### addOnProgressListener

```
fun addOnProgressListener(
    activity: Activity,
    listener: OnProgressListener<Any!>
): StorageTask<ResultT!>
```

Adds a listener that is called periodically while the ControllableTask executes.

| Parameters |
|---|---|
| `activity: https://developer.android.com/reference/kotlin/android/app/Activity.html` | When the supplied `https://developer.android.com/reference/kotlin/android/app/Activity.html` stops, this listener will automatically be removed. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | this Task |

### addOnProgressListener

```
fun addOnProgressListener(
    executor: Executor,
    listener: OnProgressListener<Any!>
): StorageTask<ResultT!>
```

Adds a listener that is called periodically while the ControllableTask executes.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | the executor to use to call the listener |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | this Task |

### addOnSuccessListener

```
fun addOnSuccessListener(listener: OnSuccessListener<Any!>): StorageTask<ResultT!>
```

Adds a listener that is called if the Task completes successfully. The listener will be called on the main application thread. If the task has already completed successfully, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | this Task |

### addOnSuccessListener

```
fun addOnSuccessListener(
    activity: Activity,
    listener: OnSuccessListener<Any!>
): StorageTask<ResultT!>
```

Adds a listener that is called if the Task completes successfully.

If multiple listeners are added, they will be called in the order in which they were added. If the task has already completed successfully, a call to the listener will be immediately scheduled.

| Parameters |
|---|---|
| `activity: https://developer.android.com/reference/kotlin/android/app/Activity.html` | When the supplied `https://developer.android.com/reference/kotlin/android/app/Activity.html` stops, this listener will automatically be removed. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | this Task |

### addOnSuccessListener

```
fun addOnSuccessListener(
    executor: Executor,
    listener: OnSuccessListener<Any!>
): StorageTask<ResultT!>
```

Adds a listener that is called if the Task completes successfully.

If multiple listeners are added, they will be called in the order in which they were added. If the task has already completed successfully, a call to the listener will be immediately scheduled.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | the executor to use to call the listener |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | this Task |

### cancel

```
fun cancel(): Boolean
```

Attempts to cancel the task. A canceled task cannot be resumed later.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `true` if this task is successfully being canceled. |

### continueWith

```
fun <ContinuationResultT> continueWith(
    continuation: Continuation<ResultT!, ContinuationResultT!>
): Task<ContinuationResultT!>
```

Returns a new Task that will be completed with the result of applying the specified Continuation to this Task.

The Continuation will be called on the main application thread.

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-` |   |

### continueWith

```
fun <ContinuationResultT> continueWith(
    executor: Executor,
    continuation: Continuation<ResultT!, ContinuationResultT!>
): Task<ContinuationResultT!>
```

Returns a new Task that will be completed with the result of applying the specified Continuation to this Task.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | the executor to use to call the Continuation |

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-` |   |

### continueWithTask

```
fun <ContinuationResultT> continueWithTask(
    continuation: Continuation<ResultT!, Task<ContinuationResultT!>!>
): Task<ContinuationResultT!>
```

Returns a new Task that will be completed with the result of applying the specified Continuation to this Task.

The Continuation will be called on the main application thread.

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-` |   |

### continueWithTask

```
fun <ContinuationResultT> continueWithTask(
    executor: Executor,
    continuation: Continuation<ResultT!, Task<ContinuationResultT!>!>
): Task<ContinuationResultT!>
```

Returns a new Task that will be completed with the result of applying the specified Continuation to this Task.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | the executor to use to call the Continuation |

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-` |   |

### getException

```
fun getException(): Exception?
```

Returns the exception that caused the Task to fail. Returns `null` if the Task is not yet complete, or completed successfully.

### getResult

```
fun getResult(): ResultT
```

Gets the result of the Task, if it has already completed.

| Throws |
|---|---|
| `java.lang.IllegalStateException: https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html` | if the Task is not yet complete |
| `com.google.android.gms.tasks.RuntimeExecutionException: https://developers.google.com/android/reference/com/google/android/gms/tasks/RuntimeExecutionException.html` | if the Task failed with an exception |

### getResult

```
fun <X : Throwable?> getResult(exceptionType: Class<X!>): ResultT
```

Gets the result of the Task, if it has already completed.

| Throws |
|---|---|
| `java.lang.IllegalStateException: https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html` | if the Task is not yet complete |
| `X: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#getResult(java.lang.Class<X>)` | if the Task failed with an exception of type X |
| `com.google.android.gms.tasks.RuntimeExecutionException: https://developers.google.com/android/reference/com/google/android/gms/tasks/RuntimeExecutionException.html` | if the Task failed with an exception that was not of type X |

### getSnapshot

```
fun getSnapshot(): ResultT
```

Returns the current state of the task. This method will return state at any point of the tasks execution and may not be the final result.

### isCanceled

```
fun isCanceled(): Boolean
```

Returns `true` if the task has been canceled.

### isComplete

```
fun isComplete(): Boolean
```

Returns `true` if the Task is complete; `false` otherwise.

### isInProgress

```
fun isInProgress(): Boolean
```

Returns `true` if the task is currently running.

### isPaused

```
fun isPaused(): Boolean
```

Returns `true` if the task has been paused.

### isSuccessful

```
fun isSuccessful(): Boolean
```

Returns `true` if the Task has completed successfully; `false` otherwise.

### onSuccessTask

```
fun <ContinuationResultT> onSuccessTask(
    continuation: SuccessContinuation<ResultT!, ContinuationResultT!>
): Task<ContinuationResultT!>
```

Returns a new Task that will be completed with the result of applying the specified SuccessContinuation to this Task when this Task completes successfully. If the previous Task fails, the onSuccessTask completion will be skipped and failure listeners will be invoked.

The SuccessContinuation will be called on the main application thread.

If the previous Task is canceled, the returned Task will also be canceled and the SuccessContinuation would not execute.

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html` |   |

### onSuccessTask

```
fun <ContinuationResultT> onSuccessTask(
    executor: Executor,
    continuation: SuccessContinuation<ResultT!, ContinuationResultT!>
): Task<ContinuationResultT!>
```

Returns a new Task that will be completed with the result of applying the specified SuccessContinuation to this Task when this Task completes successfully. If the previous Task fails, the onSuccessTask completion will be skipped and failure listeners will be invoked.

If the previous Task is canceled, the returned Task will also be canceled and the SuccessContinuation would not execute.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | the executor to use to call the SuccessContinuation |

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html` |   |

### pause

```
fun pause(): Boolean
```

Attempts to pause the task. A paused task can later be resumed.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `true` if this task is successfully being paused. Note that a task may not be immediately paused if it was executing another action and can still fail or complete. |

### removeOnCanceledListener

```
fun removeOnCanceledListener(listener: OnCanceledListener): StorageTask<ResultT!>
```

Removes a listener.

### removeOnCompleteListener

```
fun removeOnCompleteListener(listener: OnCompleteListener<ResultT!>): StorageTask<ResultT!>
```

Removes a listener.

### removeOnFailureListener

```
fun removeOnFailureListener(listener: OnFailureListener): StorageTask<ResultT!>
```

Removes a listener.

### removeOnPausedListener

```
fun removeOnPausedListener(listener: OnPausedListener<Any!>): StorageTask<ResultT!>
```

Removes a listener.

### removeOnProgressListener

```
fun removeOnProgressListener(listener: OnProgressListener<Any!>): StorageTask<ResultT!>
```

Removes a listener.

### removeOnSuccessListener

```
fun removeOnSuccessListener(listener: OnSuccessListener<Any!>): StorageTask<ResultT!>
```

Removes a listener.

### resume

```
fun resume(): Boolean
```

Attempts to resume a paused task.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `true` if the task is successfully resumed. `false` if the task has an unrecoverable error or has entered another state that precludes resume. |

## Protected functions

### onCanceled

```
protected fun onCanceled(): Unit
```

### onFailure

```
protected fun onFailure(): Unit
```

### onPaused

```
protected fun onPaused(): Unit
```

### onProgress

```
protected fun onProgress(): Unit
```

### onQueued

```
protected fun onQueued(): Unit
```

### onSuccess

```
protected fun onSuccess(): Unit
```

## Protected properties

### syncObject

```
protected val syncObject: Any!
```

## Extension properties

### taskState

```
val StorageTask<T>.taskState: Flow<TaskState<T>>
```

Starts listening to this task's progress and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, it attaches the following listeners: `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnProgressListener`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnPausedListener`, `https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html`.

- When the flow completes the listeners will be removed.