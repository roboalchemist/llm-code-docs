# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTask.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.md.txt

# StorageTask

# StorageTask


```
abstract class StorageTask<ResultTÂ :Â StorageTask.ProvideError?> : ControllableTask
```

<br />

|---|---|---|---|--------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                |||||
| â³ | [com.google.android.gms.tasks.Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)                   ||||
|   | â³ | [com.google.firebase.storage.CancellableTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/CancellableTask) |||
|   |   | â³ | [com.google.firebase.storage.ControllableTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask) ||
|   |   |   | â³ | [com.google.firebase.storage.StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask) |

Known direct subclasses  
[FileDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask), [StreamDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask), [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask)  

|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [FileDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask)     | A task that downloads bytes of a GCS blob to a specified File.                        |
| [StreamDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask) | A task that downloads bytes of a GCS blob.                                            |
| [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask)                 | An controllable task that uploads and fires events for success, progress and failure. |

*** ** * ** ***

A controllable Task that has a synchronized state machine.

## Summary

|                                                                                                                                            ### Nested types                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `protected interface `[StorageTask.ProvideError](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.ProvideError) An object that returns an exception.                                                                                                           |
| `class `[StorageTask.SnapshotBase](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase)` : `[StorageTask.ProvideError](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.ProvideError) Base class for state. |

|                                                 ### Protected constructors                                                 |
|----------------------------------------------------------------------------------------------------------------------------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#StorageTask())`()` |

|                                                  ### Public functions                                                  |
|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [addOnCanceledListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnCanceledListener(com.google.android.gms.tasks.OnCanceledListener))`(listener: `[OnCanceledListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html)`)` Adds a listener that is called if the Task is canceled.                                                                                                                                                                                                                                                                                                                                                                                                              |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [addOnCanceledListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnCanceledListener(android.app.Activity,com.google.android.gms.tasks.OnCanceledListener))`(activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html)`, listener: `[OnCanceledListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html)`)` Adds an Activity-scoped listener that is called if the Task is canceled.                                                                                                                                                                                                                                                                      |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [addOnCanceledListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnCanceledListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnCanceledListener))`(executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)`, listener: `[OnCanceledListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html)`)` Adds a listener that is called if the Task is canceled.                                                                                                                                                                                                                                                                     |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [addOnCompleteListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnCompleteListener(com.google.android.gms.tasks.OnCompleteListener<ResultT>))`(listener: `[OnCompleteListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html)`<ResultT!>)` Adds a listener that is called when the Task succeeds or fails.                                                                                                                                                                                                                                                                                                                                                                                   |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [addOnCompleteListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnCompleteListener(android.app.Activity,com.google.android.gms.tasks.OnCompleteListener<ResultT>))`(` ` activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html)`,` ` listener: `[OnCompleteListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html)`<ResultT!>` `)` Adds a listener that is called when the Task succeeds or fails.                                                                                                                                                                                                                                                  |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [addOnCompleteListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnCompleteListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnCompleteListener<ResultT>))`(` ` executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)`,` ` listener: `[OnCompleteListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html)`<ResultT!>` `)` Adds a listener that is called when the Task succeeds or fails.                                                                                                                                                                                                                                |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [addOnFailureListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnFailureListener(com.google.android.gms.tasks.OnFailureListener))`(listener: `[OnFailureListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html)`)` Adds a listener that is called if the Task fails.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [addOnFailureListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnFailureListener(android.app.Activity,com.google.android.gms.tasks.OnFailureListener))`(activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html)`, listener: `[OnFailureListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html)`)` Adds a listener that is called if the Task fails.                                                                                                                                                                                                                                                                                                  |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [addOnFailureListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnFailureListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnFailureListener))`(executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)`, listener: `[OnFailureListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html)`)` Adds a listener that is called if the Task fails.                                                                                                                                                                                                                                                                                |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [addOnPausedListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnPausedListener(com.google.firebase.storage.OnPausedListener<? super ResultT>))`(listener: `[OnPausedListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnPausedListener)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>)` Adds a listener that is called when the Task becomes paused.                                                                                                                                                                                                                                                                                                                        |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [addOnPausedListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnPausedListener(android.app.Activity,com.google.firebase.storage.OnPausedListener<? super ResultT>))`(activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html)`, listener: `[OnPausedListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnPausedListener)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>)` Adds a listener that is called when the Task becomes paused.                                                                                                                                                                                                 |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [addOnPausedListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnPausedListener(java.util.concurrent.Executor,com.google.firebase.storage.OnPausedListener<? super ResultT>))`(executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)`, listener: `[OnPausedListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnPausedListener)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>)` Adds a listener that is called when the Task becomes paused.                                                                                                                                                                               |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [addOnProgressListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnProgressListener(com.google.firebase.storage.OnProgressListener<? super ResultT>))`(listener: `[OnProgressListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnProgressListener)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>)` Adds a listener that is called periodically while the ControllableTask executes.                                                                                                                                                                                                                                                                                          |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [addOnProgressListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnProgressListener(android.app.Activity,com.google.firebase.storage.OnProgressListener<? super ResultT>))`(` ` activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html)`,` ` listener: `[OnProgressListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnProgressListener)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>` `)` Adds a listener that is called periodically while the ControllableTask executes.                                                                                                                                                         |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [addOnProgressListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnProgressListener(java.util.concurrent.Executor,com.google.firebase.storage.OnProgressListener<? super ResultT>))`(` ` executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)`,` ` listener: `[OnProgressListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnProgressListener)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>` `)` Adds a listener that is called periodically while the ControllableTask executes.                                                                                                                                       |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [addOnSuccessListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnSuccessListener(com.google.android.gms.tasks.OnSuccessListener<? super ResultT>))`(listener: `[OnSuccessListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>)` Adds a listener that is called if the Task completes successfully.                                                                                                                                                                                                                                                                                                        |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [addOnSuccessListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnSuccessListener(android.app.Activity,com.google.android.gms.tasks.OnSuccessListener<? super ResultT>))`(` ` activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html)`,` ` listener: `[OnSuccessListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>` `)` Adds a listener that is called if the Task completes successfully.                                                                                                                                                                       |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [addOnSuccessListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnSuccessListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnSuccessListener<? super ResultT>))`(` ` executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)`,` ` listener: `[OnSuccessListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>` `)` Adds a listener that is called if the Task completes successfully.                                                                                                                                                     |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                     | [cancel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#cancel())`()` Attempts to cancel the task.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<ContinuationResultT!>` | `<ContinuationResultT> `[continueWith](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#continueWith(com.google.android.gms.tasks.Continuation<ResultT,ContinuationResultT>))`(` ` continuation: `[Continuation](https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html)`<ResultT!, ContinuationResultT!>` `)` Returns a new Task that will be completed with the result of applying the specified Continuation to this Task.                                                                                                                                                                                                                                                                                           |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<ContinuationResultT!>` | `<ContinuationResultT> `[continueWith](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#continueWith(java.util.concurrent.Executor,com.google.android.gms.tasks.Continuation<ResultT,ContinuationResultT>))`(` ` executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)`,` ` continuation: `[Continuation](https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html)`<ResultT!, ContinuationResultT!>` `)` Returns a new Task that will be completed with the result of applying the specified Continuation to this Task.                                                                                                                                               |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<ContinuationResultT!>` | `<ContinuationResultT> `[continueWithTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#continueWithTask(com.google.android.gms.tasks.Continuation<ResultT,com.google.android.gms.tasks.Task<ContinuationResultT>>))`(` ` continuation: `[Continuation](https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html)`<ResultT!, `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<ContinuationResultT!>!>` `)` Returns a new Task that will be completed with the result of applying the specified Continuation to this Task.                                                                                                                                             |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<ContinuationResultT!>` | `<ContinuationResultT> `[continueWithTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#continueWithTask(java.util.concurrent.Executor,com.google.android.gms.tasks.Continuation<ResultT,com.google.android.gms.tasks.Task<ContinuationResultT>>))`(` ` executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)`,` ` continuation: `[Continuation](https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html)`<ResultT!, `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<ContinuationResultT!>!>` `)` Returns a new Task that will be completed with the result of applying the specified Continuation to this Task. |
| [Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html)`?`                                | [getException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#getException())`()` Returns the exception that caused the Task to fail.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `ResultT`                                                                                                              | [getResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#getResult())`()` Gets the result of the Task, if it has already completed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `ResultT`                                                                                                              | `<X : `[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`?> `[getResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#getResult(java.lang.Class<X>))`(exceptionType: `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<X!>)` Gets the result of the Task, if it has already completed.                                                                                                                                                                                                                                                                                                                                                                                                    |
| `ResultT`                                                                                                              | [getSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#getSnapshot())`()` Returns the current state of the task.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                     | [isCanceled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#isCanceled())`()` Returns `true` if the task has been canceled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                     | [isComplete](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#isComplete())`()` Returns `true` if the Task is complete; `false` otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                     | [isInProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#isInProgress())`()` Returns `true` if the task is currently running.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                     | [isPaused](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#isPaused())`()` Returns `true` if the task has been paused.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                     | [isSuccessful](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#isSuccessful())`()` Returns `true` if the Task has completed successfully; `false` otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<ContinuationResultT!>` | `<ContinuationResultT> `[onSuccessTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#onSuccessTask(com.google.android.gms.tasks.SuccessContinuation<ResultT,ContinuationResultT>))`(` ` continuation: `[SuccessContinuation](https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html)`<ResultT!, ContinuationResultT!>` `)` Returns a new Task that will be completed with the result of applying the specified SuccessContinuation to this Task when this Task completes successfully.                                                                                                                                                                                                                       |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<ContinuationResultT!>` | `<ContinuationResultT> `[onSuccessTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#onSuccessTask(java.util.concurrent.Executor,com.google.android.gms.tasks.SuccessContinuation<ResultT,ContinuationResultT>))`(` ` executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)`,` ` continuation: `[SuccessContinuation](https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html)`<ResultT!, ContinuationResultT!>` `)` Returns a new Task that will be completed with the result of applying the specified SuccessContinuation to this Task when this Task completes successfully.                                                                           |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                     | [pause](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#pause())`()` Attempts to pause the task.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [removeOnCanceledListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#removeOnCanceledListener(com.google.android.gms.tasks.OnCanceledListener))`(listener: `[OnCanceledListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html)`)` Removes a listener.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [removeOnCompleteListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#removeOnCompleteListener(com.google.android.gms.tasks.OnCompleteListener<ResultT>))`(listener: `[OnCompleteListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html)`<ResultT!>)` Removes a listener.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [removeOnFailureListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#removeOnFailureListener(com.google.android.gms.tasks.OnFailureListener))`(listener: `[OnFailureListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html)`)` Removes a listener.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [removeOnPausedListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#removeOnPausedListener(com.google.firebase.storage.OnPausedListener<? super ResultT>))`(listener: `[OnPausedListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnPausedListener)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>)` Removes a listener.                                                                                                                                                                                                                                                                                                                                                           |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [removeOnProgressListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#removeOnProgressListener(com.google.firebase.storage.OnProgressListener<? super ResultT>))`(listener: `[OnProgressListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnProgressListener)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>)` Removes a listener.                                                                                                                                                                                                                                                                                                                                                 |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>`   | [removeOnSuccessListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#removeOnSuccessListener(com.google.android.gms.tasks.OnSuccessListener<? super ResultT>))`(listener: `[OnSuccessListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>)` Removes a listener.                                                                                                                                                                                                                                                                                                                                                 |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                     | [resume](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#resume())`()` Attempts to resume a paused task.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

|                           ### Protected functions                            |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [onCanceled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#onCanceled())`()` |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [onFailure](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#onFailure())`()`   |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [onPaused](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#onPaused())`()`     |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [onProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#onProgress())`()` |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [onQueued](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#onQueued())`()`     |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [onSuccess](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#onSuccess())`()`   |

|                           ### Protected properties                            |
|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!` | [syncObject](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#syncObject()) |

|                                                                                                      ### Extension properties                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)`<`[TaskState](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState)`<T>>` | [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<T>.`[taskState](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#(com.google.firebase.storage.StorageTask).taskState()) Starts listening to this task's progress and emits its values via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html). |

|                                                                                                                                                                                                                                                                               ### Inherited functions                                                                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [com.google.android.gms.tasks.Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) |-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------| | `abstract `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | [isCanceled](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isCanceled--)`()` | |

## Protected constructors

### StorageTask

```
protectedÂ StorageTask()
```  

## Public functions

### addOnCanceledListener

```
funÂ addOnCanceledListener(listener:Â OnCanceledListener):Â StorageTask<ResultT!>
```

Adds a listener that is called if the Task is canceled.

The listener will be called on main application thread. If the Task has already been canceled, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.  

|                                                       Returns                                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | this Task |

### addOnCanceledListener

```
funÂ addOnCanceledListener(activity:Â Activity,Â listener:Â OnCanceledListener):Â StorageTask<ResultT!>
```

Adds an Activity-scoped listener that is called if the Task is canceled.

The listener will be called on main application thread. If the Task has already been canceled, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

The listener will be automatically removed during [onStop](https://developer.android.com/reference/kotlin/android/app/Activity.html#onStop--).  

|                                                       Returns                                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | this Task |

### addOnCanceledListener

```
funÂ addOnCanceledListener(executor:Â Executor,Â listener:Â OnCanceledListener):Â StorageTask<ResultT!>
```

Adds a listener that is called if the Task is canceled.

If the Task has already been canceled, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------|
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) | the executor to use to call the listener |

|                                                       Returns                                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | this Task |

### addOnCompleteListener

```
funÂ addOnCompleteListener(listener:Â OnCompleteListener<ResultT!>):Â StorageTask<ResultT!>
```

Adds a listener that is called when the Task succeeds or fails.

The listener will be called on main application thread. If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.  

|                                                       Returns                                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | this Task |

### addOnCompleteListener

```
funÂ addOnCompleteListener(
Â Â Â Â activity:Â Activity,
Â Â Â Â listener:Â OnCompleteListener<ResultT!>
):Â StorageTask<ResultT!>
```

Adds a listener that is called when the Task succeeds or fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.  

|                                            Parameters                                            |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) | When the supplied [Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) stops, this listener will automatically be removed. |

|                                                       Returns                                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | this Task |

### addOnCompleteListener

```
funÂ addOnCompleteListener(
Â Â Â Â executor:Â Executor,
Â Â Â Â listener:Â OnCompleteListener<ResultT!>
):Â StorageTask<ResultT!>
```

Adds a listener that is called when the Task succeeds or fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------|
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) | the executor to use to call the listener |

|                                                       Returns                                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | this Task |

### addOnFailureListener

```
funÂ addOnFailureListener(listener:Â OnFailureListener):Â StorageTask<ResultT!>
```

Adds a listener that is called if the Task fails.

The listener will be called on main application thread. If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.  

|                                                       Returns                                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | this Task |

### addOnFailureListener

```
funÂ addOnFailureListener(activity:Â Activity,Â listener:Â OnFailureListener):Â StorageTask<ResultT!>
```

Adds a listener that is called if the Task fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.  

|                                            Parameters                                            |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) | When the supplied [Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) stops, this listener will automatically be removed. |

|                                                       Returns                                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | this Task |

### addOnFailureListener

```
funÂ addOnFailureListener(executor:Â Executor,Â listener:Â OnFailureListener):Â StorageTask<ResultT!>
```

Adds a listener that is called if the Task fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------|
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) | the executor to use to call the listener |

|                                                       Returns                                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | this Task |

### addOnPausedListener

```
funÂ addOnPausedListener(listener:Â OnPausedListener<Any!>):Â StorageTask<ResultT!>
```

Adds a listener that is called when the Task becomes paused.  

|                                                       Returns                                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | this Task |

### addOnPausedListener

```
funÂ addOnPausedListener(activity:Â Activity,Â listener:Â OnPausedListener<Any!>):Â StorageTask<ResultT!>
```

Adds a listener that is called when the Task becomes paused.  

|                                            Parameters                                            |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) | When the supplied [Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) stops, this listener will automatically be removed. |

|                                                       Returns                                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | this Task |

### addOnPausedListener

```
funÂ addOnPausedListener(executor:Â Executor,Â listener:Â OnPausedListener<Any!>):Â StorageTask<ResultT!>
```

Adds a listener that is called when the Task becomes paused.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------|
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) | the executor to use to call the listener |

|                                                       Returns                                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | this Task |

### addOnProgressListener

```
funÂ addOnProgressListener(listener:Â OnProgressListener<Any!>):Â StorageTask<ResultT!>
```

Adds a listener that is called periodically while the ControllableTask executes.  

|                                                       Returns                                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | this Task |

### addOnProgressListener

```
funÂ addOnProgressListener(
Â Â Â Â activity:Â Activity,
Â Â Â Â listener:Â OnProgressListener<Any!>
):Â StorageTask<ResultT!>
```

Adds a listener that is called periodically while the ControllableTask executes.  

|                                            Parameters                                            |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) | When the supplied [Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) stops, this listener will automatically be removed. |

|                                                       Returns                                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | this Task |

### addOnProgressListener

```
funÂ addOnProgressListener(
Â Â Â Â executor:Â Executor,
Â Â Â Â listener:Â OnProgressListener<Any!>
):Â StorageTask<ResultT!>
```

Adds a listener that is called periodically while the ControllableTask executes.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------|
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) | the executor to use to call the listener |

|                                                       Returns                                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | this Task |

### addOnSuccessListener

```
funÂ addOnSuccessListener(listener:Â OnSuccessListener<Any!>):Â StorageTask<ResultT!>
```

Adds a listener that is called if the Task completes successfully. The listener will be called on the main application thread. If the task has already completed successfully, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.  

|                                                       Returns                                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | this Task |

### addOnSuccessListener

```
funÂ addOnSuccessListener(
Â Â Â Â activity:Â Activity,
Â Â Â Â listener:Â OnSuccessListener<Any!>
):Â StorageTask<ResultT!>
```

Adds a listener that is called if the Task completes successfully.

If multiple listeners are added, they will be called in the order in which they were added. If the task has already completed successfully, a call to the listener will be immediately scheduled.  

|                                            Parameters                                            |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) | When the supplied [Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) stops, this listener will automatically be removed. |

|                                                       Returns                                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | this Task |

### addOnSuccessListener

```
funÂ addOnSuccessListener(
Â Â Â Â executor:Â Executor,
Â Â Â Â listener:Â OnSuccessListener<Any!>
):Â StorageTask<ResultT!>
```

Adds a listener that is called if the Task completes successfully.

If multiple listeners are added, they will be called in the order in which they were added. If the task has already completed successfully, a call to the listener will be immediately scheduled.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------|
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) | the executor to use to call the listener |

|                                                       Returns                                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------|
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | this Task |

### cancel

```
funÂ cancel():Â Boolean
```

Attempts to cancel the task. A canceled task cannot be resumed later.  

|                                      Returns                                       |
|------------------------------------------------------------------------------------|-----------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `true` if this task is successfully being canceled. |

### continueWith

```
funÂ <ContinuationResultT> continueWith(
Â Â Â Â continuation:Â Continuation<ResultT!,Â ContinuationResultT!>
):Â Task<ContinuationResultT!>
```

Returns a new Task that will be completed with the result of applying the specified Continuation to this Task.

The Continuation will be called on the main application thread.  

|                                                                           See also                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [then](https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-) |   |

### continueWith

```
funÂ <ContinuationResultT> continueWith(
Â Â Â Â executor:Â Executor,
Â Â Â Â continuation:Â Continuation<ResultT!,Â ContinuationResultT!>
):Â Task<ContinuationResultT!>
```

Returns a new Task that will be completed with the result of applying the specified Continuation to this Task.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------|
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) | the executor to use to call the Continuation |

|                                                                           See also                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [then](https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-) |   |

### continueWithTask

```
funÂ <ContinuationResultT> continueWithTask(
Â Â Â Â continuation:Â Continuation<ResultT!,Â Task<ContinuationResultT!>!>
):Â Task<ContinuationResultT!>
```

Returns a new Task that will be completed with the result of applying the specified Continuation to this Task.

The Continuation will be called on the main application thread.  

|                                                                           See also                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [then](https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-) |   |

### continueWithTask

```
funÂ <ContinuationResultT> continueWithTask(
Â Â Â Â executor:Â Executor,
Â Â Â Â continuation:Â Continuation<ResultT!,Â Task<ContinuationResultT!>!>
):Â Task<ContinuationResultT!>
```

Returns a new Task that will be completed with the result of applying the specified Continuation to this Task.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------|
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) | the executor to use to call the Continuation |

|                                                                           See also                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [then](https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-) |   |

### getException

```
funÂ getException():Â Exception?
```

Returns the exception that caused the Task to fail. Returns `null` if the Task is not yet complete, or completed successfully.  

### getResult

```
funÂ getResult():Â ResultT
```

Gets the result of the Task, if it has already completed.  

|                                                                                                             Throws                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| `java.lang.IllegalStateException: `[java.lang.IllegalStateException](https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html)                                                                       | if the Task is not yet complete      |
| `com.google.android.gms.tasks.RuntimeExecutionException: `[com.google.android.gms.tasks.RuntimeExecutionException](https://developers.google.com/android/reference/com/google/android/gms/tasks/RuntimeExecutionException.html) | if the Task failed with an exception |

### getResult

```
funÂ <XÂ :Â Throwable?> getResult(exceptionType:Â Class<X!>):Â ResultT
```

Gets the result of the Task, if it has already completed.  

|                                                                                                             Throws                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| `java.lang.IllegalStateException: `[java.lang.IllegalStateException](https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html)                                                                       | if the Task is not yet complete                             |
| `X: `[X](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#getResult(java.lang.Class<X>))                                                                                               | if the Task failed with an exception of type X              |
| `com.google.android.gms.tasks.RuntimeExecutionException: `[com.google.android.gms.tasks.RuntimeExecutionException](https://developers.google.com/android/reference/com/google/android/gms/tasks/RuntimeExecutionException.html) | if the Task failed with an exception that was not of type X |

### getSnapshot

```
funÂ getSnapshot():Â ResultT
```

Returns the current state of the task. This method will return state at any point of the tasks execution and may not be the final result.  

### isCanceled

```
funÂ isCanceled():Â Boolean
```

Returns `true` if the task has been canceled.  

### isComplete

```
funÂ isComplete():Â Boolean
```

Returns `true` if the Task is complete; `false` otherwise.  

### isInProgress

```
funÂ isInProgress():Â Boolean
```

Returns `true` if the task is currently running.  

### isPaused

```
funÂ isPaused():Â Boolean
```

Returns `true` if the task has been paused.  

### isSuccessful

```
funÂ isSuccessful():Â Boolean
```

Returns `true` if the Task has completed successfully; `false` otherwise.  

### onSuccessTask

```
funÂ <ContinuationResultT> onSuccessTask(
Â Â Â Â continuation:Â SuccessContinuation<ResultT!,Â ContinuationResultT!>
):Â Task<ContinuationResultT!>
```

Returns a new Task that will be completed with the result of applying the specified SuccessContinuation to this Task when this Task completes successfully. If the previous Task fails, the onSuccessTask completion will be skipped and failure listeners will be invoked.

The SuccessContinuation will be called on the main application thread.

If the previous Task is canceled, the returned Task will also be canceled and the SuccessContinuation would not execute.  

|                                                           See also                                                           |
|------------------------------------------------------------------------------------------------------------------------------|---|
| [SuccessContinuation](https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html) |   |

### onSuccessTask

```
funÂ <ContinuationResultT> onSuccessTask(
Â Â Â Â executor:Â Executor,
Â Â Â Â continuation:Â SuccessContinuation<ResultT!,Â ContinuationResultT!>
):Â Task<ContinuationResultT!>
```

Returns a new Task that will be completed with the result of applying the specified SuccessContinuation to this Task when this Task completes successfully. If the previous Task fails, the onSuccessTask completion will be skipped and failure listeners will be invoked.

If the previous Task is canceled, the returned Task will also be canceled and the SuccessContinuation would not execute.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) | the executor to use to call the SuccessContinuation |

|                                                           See also                                                           |
|------------------------------------------------------------------------------------------------------------------------------|---|
| [SuccessContinuation](https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html) |   |

### pause

```
funÂ pause():Â Boolean
```

Attempts to pause the task. A paused task can later be resumed.  

|                                      Returns                                       |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `true` if this task is successfully being paused. Note that a task may not be immediately paused if it was executing another action and can still fail or complete. |

### removeOnCanceledListener

```
funÂ removeOnCanceledListener(listener:Â OnCanceledListener):Â StorageTask<ResultT!>
```

Removes a listener.  

### removeOnCompleteListener

```
funÂ removeOnCompleteListener(listener:Â OnCompleteListener<ResultT!>):Â StorageTask<ResultT!>
```

Removes a listener.  

### removeOnFailureListener

```
funÂ removeOnFailureListener(listener:Â OnFailureListener):Â StorageTask<ResultT!>
```

Removes a listener.  

### removeOnPausedListener

```
funÂ removeOnPausedListener(listener:Â OnPausedListener<Any!>):Â StorageTask<ResultT!>
```

Removes a listener.  

### removeOnProgressListener

```
funÂ removeOnProgressListener(listener:Â OnProgressListener<Any!>):Â StorageTask<ResultT!>
```

Removes a listener.  

### removeOnSuccessListener

```
funÂ removeOnSuccessListener(listener:Â OnSuccessListener<Any!>):Â StorageTask<ResultT!>
```

Removes a listener.  

### resume

```
funÂ resume():Â Boolean
```

Attempts to resume a paused task.  

|                                      Returns                                       |
|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `true` if the task is successfully resumed. `false` if the task has an unrecoverable error or has entered another state that precludes resume. |

## Protected functions

### onCanceled

```
protectedÂ funÂ onCanceled():Â Unit
```  

### onFailure

```
protectedÂ funÂ onFailure():Â Unit
```  

### onPaused

```
protectedÂ funÂ onPaused():Â Unit
```  

### onProgress

```
protectedÂ funÂ onProgress():Â Unit
```  

### onQueued

```
protectedÂ funÂ onQueued():Â Unit
```  

### onSuccess

```
protectedÂ funÂ onSuccess():Â Unit
```  

## Protected properties

### syncObject

```
protectedÂ valÂ syncObject:Â Any!
```  

## Extension properties

### taskState

```
valÂ StorageTask<T>.taskState:Â Flow<TaskState<T>>
```

Starts listening to this task's progress and emits its values via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).

- When the returned flow starts being collected, it attaches the following listeners: [OnProgressListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnProgressListener), [OnPausedListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnPausedListener), [OnCompleteListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html).

- When the flow completes the listeners will be removed.