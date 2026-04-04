# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.md.txt

# StorageTask

# StorageTask


```
public abstract class StorageTask<ResultT extends StorageTask.ProvideError> extends ControllableTask
```

<br />

|---|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||||
| ↳ | [com.google.android.gms.tasks.Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) ||||
|   | ↳ | [com.google.firebase.storage.CancellableTask](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/CancellableTask) |||
|   |   | ↳ | [com.google.firebase.storage.ControllableTask](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ControllableTask) ||
|   |   |   | ↳ | [com.google.firebase.storage.StorageTask](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask) |

Known direct subclasses [FileDownloadTask](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask), [StreamDownloadTask](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask), [UploadTask](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask` | A task that downloads bytes of a GCS blob to a specified File. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask` | A task that downloads bytes of a GCS blob. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` | An controllable task that uploads and fires events for success, progress and failure. |

*** ** * ** ***

A controllable Task that has a synchronized state machine.

## Summary

| ### Nested types |
|---|
| `protected interface https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.ProvideError` An object that returns an exception. |
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase implements https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.ProvideError` Base class for state. |

| ### Protected fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#syncObject()` |

| ### Protected constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#StorageTask()()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#addOnCanceledListener(com.google.android.gms.tasks.OnCanceledListener)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html listener)` Adds a listener that is called if the Task is canceled. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#addOnCanceledListener(android.app.Activity,com.google.android.gms.tasks.OnCanceledListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html listener )` Adds an Activity-scoped listener that is called if the Task is canceled. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#addOnCanceledListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnCanceledListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html listener )` Adds a listener that is called if the Task is canceled. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#addOnCompleteListener(com.google.android.gms.tasks.OnCompleteListener<ResultT>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html<ResultT> listener)` Adds a listener that is called when the Task succeeds or fails. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#addOnCompleteListener(android.app.Activity,com.google.android.gms.tasks.OnCompleteListener<ResultT>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html<ResultT> listener )` Adds a listener that is called when the Task succeeds or fails. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#addOnCompleteListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnCompleteListener<ResultT>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html<ResultT> listener )` Adds a listener that is called when the Task succeeds or fails. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#addOnFailureListener(com.google.android.gms.tasks.OnFailureListener)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html listener)` Adds a listener that is called if the Task fails. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#addOnFailureListener(android.app.Activity,com.google.android.gms.tasks.OnFailureListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html listener )` Adds a listener that is called if the Task fails. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#addOnFailureListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnFailureListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html listener )` Adds a listener that is called if the Task fails. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#addOnPausedListener(com.google.firebase.storage.OnPausedListener<? super ResultT>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/OnPausedListener<https://developer.android.com/reference/kotlin/java/lang/Object.html> listener)` Adds a listener that is called when the Task becomes paused. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#addOnPausedListener(android.app.Activity,com.google.firebase.storage.OnPausedListener<? super ResultT>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/OnPausedListener<https://developer.android.com/reference/kotlin/java/lang/Object.html> listener )` Adds a listener that is called when the Task becomes paused. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#addOnPausedListener(java.util.concurrent.Executor,com.google.firebase.storage.OnPausedListener<? super ResultT>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/OnPausedListener<https://developer.android.com/reference/kotlin/java/lang/Object.html> listener )` Adds a listener that is called when the Task becomes paused. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#addOnProgressListener(com.google.firebase.storage.OnProgressListener<? super ResultT>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/OnProgressListener<https://developer.android.com/reference/kotlin/java/lang/Object.html> listener)` Adds a listener that is called periodically while the ControllableTask executes. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#addOnProgressListener(android.app.Activity,com.google.firebase.storage.OnProgressListener<? super ResultT>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/OnProgressListener<https://developer.android.com/reference/kotlin/java/lang/Object.html> listener )` Adds a listener that is called periodically while the ControllableTask executes. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#addOnProgressListener(java.util.concurrent.Executor,com.google.firebase.storage.OnProgressListener<? super ResultT>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/OnProgressListener<https://developer.android.com/reference/kotlin/java/lang/Object.html> listener )` Adds a listener that is called periodically while the ControllableTask executes. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#addOnSuccessListener(com.google.android.gms.tasks.OnSuccessListener<? super ResultT>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html<https://developer.android.com/reference/kotlin/java/lang/Object.html> listener)` Adds a listener that is called if the Task completes successfully. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#addOnSuccessListener(android.app.Activity,com.google.android.gms.tasks.OnSuccessListener<? super ResultT>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html<https://developer.android.com/reference/kotlin/java/lang/Object.html> listener )` Adds a listener that is called if the Task completes successfully. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#addOnSuccessListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnSuccessListener<? super ResultT>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html<https://developer.android.com/reference/kotlin/java/lang/Object.html> listener )` Adds a listener that is called if the Task completes successfully. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#cancel()()` Attempts to cancel the task. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<ContinuationResultT>` | `<ContinuationResultT> https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#continueWith(com.google.android.gms.tasks.Continuation<ResultT,ContinuationResultT>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<ResultT, ContinuationResultT> continuation )` Returns a new Task that will be completed with the result of applying the specified Continuation to this Task. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<ContinuationResultT>` | `<ContinuationResultT> https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#continueWith(java.util.concurrent.Executor,com.google.android.gms.tasks.Continuation<ResultT,ContinuationResultT>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<ResultT, ContinuationResultT> continuation )` Returns a new Task that will be completed with the result of applying the specified Continuation to this Task. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<ContinuationResultT>` | `<ContinuationResultT> https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#continueWithTask(com.google.android.gms.tasks.Continuation<ResultT,com.google.android.gms.tasks.Task<ContinuationResultT>>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<ResultT, https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<ContinuationResultT>> continuation )` Returns a new Task that will be completed with the result of applying the specified Continuation to this Task. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<ContinuationResultT>` | `<ContinuationResultT> https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#continueWithTask(java.util.concurrent.Executor,com.google.android.gms.tasks.Continuation<ResultT,com.google.android.gms.tasks.Task<ContinuationResultT>>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<ResultT, https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<ContinuationResultT>> continuation )` Returns a new Task that will be completed with the result of applying the specified Continuation to this Task. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Exception.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#getException()()` Returns the exception that caused the Task to fail. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ResultT` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#getResult()()` Gets the result of the Task, if it has already completed. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ResultT` | `<X extends https://developer.android.com/reference/kotlin/java/lang/Throwable.html> https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#getResult(java.lang.Class<X>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<X> exceptionType)` Gets the result of the Task, if it has already completed. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ResultT` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#getSnapshot()()` Returns the current state of the task. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#isCanceled()()` Returns `true` if the task has been canceled. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#isComplete()()` Returns `true` if the Task is complete; `false` otherwise. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#isInProgress()()` Returns `true` if the task is currently running. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#isPaused()()` Returns `true` if the task has been paused. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#isSuccessful()()` Returns `true` if the Task has completed successfully; `false` otherwise. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<ContinuationResultT>` | `<ContinuationResultT> https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#onSuccessTask(com.google.android.gms.tasks.SuccessContinuation<ResultT,ContinuationResultT>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html<ResultT, ContinuationResultT> continuation )` Returns a new Task that will be completed with the result of applying the specified SuccessContinuation to this Task when this Task completes successfully. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<ContinuationResultT>` | `<ContinuationResultT> https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#onSuccessTask(java.util.concurrent.Executor,com.google.android.gms.tasks.SuccessContinuation<ResultT,ContinuationResultT>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html<ResultT, ContinuationResultT> continuation )` Returns a new Task that will be completed with the result of applying the specified SuccessContinuation to this Task when this Task completes successfully. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#pause()()` Attempts to pause the task. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#removeOnCanceledListener(com.google.android.gms.tasks.OnCanceledListener)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html listener)` Removes a listener. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#removeOnCompleteListener(com.google.android.gms.tasks.OnCompleteListener<ResultT>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html<ResultT> listener)` Removes a listener. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#removeOnFailureListener(com.google.android.gms.tasks.OnFailureListener)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html listener)` Removes a listener. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#removeOnPausedListener(com.google.firebase.storage.OnPausedListener<? super ResultT>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/OnPausedListener<https://developer.android.com/reference/kotlin/java/lang/Object.html> listener)` Removes a listener. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#removeOnProgressListener(com.google.firebase.storage.OnProgressListener<? super ResultT>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/OnProgressListener<https://developer.android.com/reference/kotlin/java/lang/Object.html> listener)` Removes a listener. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#removeOnSuccessListener(com.google.android.gms.tasks.OnSuccessListener<? super ResultT>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html<https://developer.android.com/reference/kotlin/java/lang/Object.html> listener)` Removes a listener. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#resume()()` Attempts to resume a paused task. |

| ### Protected methods |
|---|---|
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#onCanceled()()` |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#onFailure()()` |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#onPaused()()` |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#onProgress()()` |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#onQueued()()` |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#onSuccess()()` |

| ### Extension functions |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/TaskState<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#(com.google.firebase.storage.StorageTask).getTaskState()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> receiver)` |

| ### Inherited methods |
|---|
| From [com.google.android.gms.tasks.Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) |---|---| | `abstract boolean` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isCanceled--()` | |

## Protected fields

### syncObject

```
protected final Object syncObject
```

## Protected constructors

### StorageTask

```
protected StorageTask()
```

## Public methods

### addOnCanceledListener

```
public @NonNull StorageTask<ResultT> addOnCanceledListener(@NonNull OnCanceledListener listener)
```

Adds a listener that is called if the Task is canceled.

The listener will be called on main application thread. If the Task has already been canceled, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | this Task |

### addOnCanceledListener

```
public @NonNull StorageTask<ResultT> addOnCanceledListener(
    @NonNull Activity activity,
    @NonNull OnCanceledListener listener
)
```

Adds an Activity-scoped listener that is called if the Task is canceled.

The listener will be called on main application thread. If the Task has already been canceled, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

The listener will be automatically removed during `https://developer.android.com/reference/kotlin/android/app/Activity.html#onStop--`.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | this Task |

### addOnCanceledListener

```
public @NonNull StorageTask<ResultT> addOnCanceledListener(
    @NonNull Executor executor,
    @NonNull OnCanceledListener listener
)
```

Adds a listener that is called if the Task is canceled.

If the Task has already been canceled, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | the executor to use to call the listener |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | this Task |

### addOnCompleteListener

```
public @NonNull StorageTask<ResultT> addOnCompleteListener(@NonNull OnCompleteListener<ResultT> listener)
```

Adds a listener that is called when the Task succeeds or fails.

The listener will be called on main application thread. If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | this Task |

### addOnCompleteListener

```
public @NonNull StorageTask<ResultT> addOnCompleteListener(
    @NonNull Activity activity,
    @NonNull OnCompleteListener<ResultT> listener
)
```

Adds a listener that is called when the Task succeeds or fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity` | When the supplied `https://developer.android.com/reference/kotlin/android/app/Activity.html` stops, this listener will automatically be removed. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | this Task |

### addOnCompleteListener

```
public @NonNull StorageTask<ResultT> addOnCompleteListener(
    @NonNull Executor executor,
    @NonNull OnCompleteListener<ResultT> listener
)
```

Adds a listener that is called when the Task succeeds or fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | the executor to use to call the listener |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | this Task |

### addOnFailureListener

```
public @NonNull StorageTask<ResultT> addOnFailureListener(@NonNull OnFailureListener listener)
```

Adds a listener that is called if the Task fails.

The listener will be called on main application thread. If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | this Task |

### addOnFailureListener

```
public @NonNull StorageTask<ResultT> addOnFailureListener(
    @NonNull Activity activity,
    @NonNull OnFailureListener listener
)
```

Adds a listener that is called if the Task fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity` | When the supplied `https://developer.android.com/reference/kotlin/android/app/Activity.html` stops, this listener will automatically be removed. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | this Task |

### addOnFailureListener

```
public @NonNull StorageTask<ResultT> addOnFailureListener(
    @NonNull Executor executor,
    @NonNull OnFailureListener listener
)
```

Adds a listener that is called if the Task fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | the executor to use to call the listener |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | this Task |

### addOnPausedListener

```
public @NonNull StorageTask<ResultT> addOnPausedListener(@NonNull OnPausedListener<Object> listener)
```

Adds a listener that is called when the Task becomes paused.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | this Task |

### addOnPausedListener

```
public @NonNull StorageTask<ResultT> addOnPausedListener(
    @NonNull Activity activity,
    @NonNull OnPausedListener<Object> listener
)
```

Adds a listener that is called when the Task becomes paused.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity` | When the supplied `https://developer.android.com/reference/kotlin/android/app/Activity.html` stops, this listener will automatically be removed. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | this Task |

### addOnPausedListener

```
public @NonNull StorageTask<ResultT> addOnPausedListener(
    @NonNull Executor executor,
    @NonNull OnPausedListener<Object> listener
)
```

Adds a listener that is called when the Task becomes paused.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | the executor to use to call the listener |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | this Task |

### addOnProgressListener

```
public @NonNull StorageTask<ResultT> addOnProgressListener(@NonNull OnProgressListener<Object> listener)
```

Adds a listener that is called periodically while the ControllableTask executes.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | this Task |

### addOnProgressListener

```
public @NonNull StorageTask<ResultT> addOnProgressListener(
    @NonNull Activity activity,
    @NonNull OnProgressListener<Object> listener
)
```

Adds a listener that is called periodically while the ControllableTask executes.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity` | When the supplied `https://developer.android.com/reference/kotlin/android/app/Activity.html` stops, this listener will automatically be removed. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | this Task |

### addOnProgressListener

```
public @NonNull StorageTask<ResultT> addOnProgressListener(
    @NonNull Executor executor,
    @NonNull OnProgressListener<Object> listener
)
```

Adds a listener that is called periodically while the ControllableTask executes.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | the executor to use to call the listener |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | this Task |

### addOnSuccessListener

```
public @NonNull StorageTask<ResultT> addOnSuccessListener(@NonNull OnSuccessListener<Object> listener)
```

Adds a listener that is called if the Task completes successfully. The listener will be called on the main application thread. If the task has already completed successfully, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | this Task |

### addOnSuccessListener

```
public @NonNull StorageTask<ResultT> addOnSuccessListener(
    @NonNull Activity activity,
    @NonNull OnSuccessListener<Object> listener
)
```

Adds a listener that is called if the Task completes successfully.

If multiple listeners are added, they will be called in the order in which they were added. If the task has already completed successfully, a call to the listener will be immediately scheduled.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity` | When the supplied `https://developer.android.com/reference/kotlin/android/app/Activity.html` stops, this listener will automatically be removed. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | this Task |

### addOnSuccessListener

```
public @NonNull StorageTask<ResultT> addOnSuccessListener(
    @NonNull Executor executor,
    @NonNull OnSuccessListener<Object> listener
)
```

Adds a listener that is called if the Task completes successfully.

If multiple listeners are added, they will be called in the order in which they were added. If the task has already completed successfully, a call to the listener will be immediately scheduled.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | the executor to use to call the listener |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | this Task |

### cancel

```
public boolean cancel()
```

Attempts to cancel the task. A canceled task cannot be resumed later.

| Returns |
|---|---|
| `boolean` | `true` if this task is successfully being canceled. |

### continueWith

```
public @NonNull Task<ContinuationResultT> <ContinuationResultT> continueWith(
    @NonNull Continuation<ResultT, ContinuationResultT> continuation
)
```

Returns a new Task that will be completed with the result of applying the specified Continuation to this Task.

The Continuation will be called on the main application thread.

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-` |   |

### continueWith

```
public @NonNull Task<ContinuationResultT> <ContinuationResultT> continueWith(
    @NonNull Executor executor,
    @NonNull Continuation<ResultT, ContinuationResultT> continuation
)
```

Returns a new Task that will be completed with the result of applying the specified Continuation to this Task.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | the executor to use to call the Continuation |

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-` |   |

### continueWithTask

```
public @NonNull Task<ContinuationResultT> <ContinuationResultT> continueWithTask(
    @NonNull Continuation<ResultT, Task<ContinuationResultT>> continuation
)
```

Returns a new Task that will be completed with the result of applying the specified Continuation to this Task.

The Continuation will be called on the main application thread.

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-` |   |

### continueWithTask

```
public @NonNull Task<ContinuationResultT> <ContinuationResultT> continueWithTask(
    @NonNull Executor executor,
    @NonNull Continuation<ResultT, Task<ContinuationResultT>> continuation
)
```

Returns a new Task that will be completed with the result of applying the specified Continuation to this Task.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | the executor to use to call the Continuation |

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-` |   |

### getException

```
public @Nullable Exception getException()
```

Returns the exception that caused the Task to fail. Returns `null` if the Task is not yet complete, or completed successfully.

### getResult

```
public @NonNull ResultT getResult()
```

Gets the result of the Task, if it has already completed.

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html java.lang.IllegalStateException` | if the Task is not yet complete |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/RuntimeExecutionException.html com.google.android.gms.tasks.RuntimeExecutionException` | if the Task failed with an exception |

### getResult

```
public @NonNull ResultT <X extends Throwable> getResult(@NonNull Class<X> exceptionType)
```

Gets the result of the Task, if it has already completed.

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html java.lang.IllegalStateException` | if the Task is not yet complete |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#getResult(java.lang.Class<X>) X` | if the Task failed with an exception of type X |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/RuntimeExecutionException.html com.google.android.gms.tasks.RuntimeExecutionException` | if the Task failed with an exception that was not of type X |

### getSnapshot

```
public @NonNull ResultT getSnapshot()
```

Returns the current state of the task. This method will return state at any point of the tasks execution and may not be the final result.

### isCanceled

```
public boolean isCanceled()
```

Returns `true` if the task has been canceled.

### isComplete

```
public boolean isComplete()
```

Returns `true` if the Task is complete; `false` otherwise.

### isInProgress

```
public boolean isInProgress()
```

Returns `true` if the task is currently running.

### isPaused

```
public boolean isPaused()
```

Returns `true` if the task has been paused.

### isSuccessful

```
public boolean isSuccessful()
```

Returns `true` if the Task has completed successfully; `false` otherwise.

### onSuccessTask

```
public @NonNull Task<ContinuationResultT> <ContinuationResultT> onSuccessTask(
    @NonNull SuccessContinuation<ResultT, ContinuationResultT> continuation
)
```

Returns a new Task that will be completed with the result of applying the specified SuccessContinuation to this Task when this Task completes successfully. If the previous Task fails, the onSuccessTask completion will be skipped and failure listeners will be invoked.

The SuccessContinuation will be called on the main application thread.

If the previous Task is canceled, the returned Task will also be canceled and the SuccessContinuation would not execute.

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html` |   |

### onSuccessTask

```
public @NonNull Task<ContinuationResultT> <ContinuationResultT> onSuccessTask(
    @NonNull Executor executor,
    @NonNull SuccessContinuation<ResultT, ContinuationResultT> continuation
)
```

Returns a new Task that will be completed with the result of applying the specified SuccessContinuation to this Task when this Task completes successfully. If the previous Task fails, the onSuccessTask completion will be skipped and failure listeners will be invoked.

If the previous Task is canceled, the returned Task will also be canceled and the SuccessContinuation would not execute.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | the executor to use to call the SuccessContinuation |

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html` |   |

### pause

```
public boolean pause()
```

Attempts to pause the task. A paused task can later be resumed.

| Returns |
|---|---|
| `boolean` | `true` if this task is successfully being paused. Note that a task may not be immediately paused if it was executing another action and can still fail or complete. |

### removeOnCanceledListener

```
public @NonNull StorageTask<ResultT> removeOnCanceledListener(@NonNull OnCanceledListener listener)
```

Removes a listener.

### removeOnCompleteListener

```
public @NonNull StorageTask<ResultT> removeOnCompleteListener(@NonNull OnCompleteListener<ResultT> listener)
```

Removes a listener.

### removeOnFailureListener

```
public @NonNull StorageTask<ResultT> removeOnFailureListener(@NonNull OnFailureListener listener)
```

Removes a listener.

### removeOnPausedListener

```
public @NonNull StorageTask<ResultT> removeOnPausedListener(@NonNull OnPausedListener<Object> listener)
```

Removes a listener.

### removeOnProgressListener

```
public @NonNull StorageTask<ResultT> removeOnProgressListener(@NonNull OnProgressListener<Object> listener)
```

Removes a listener.

### removeOnSuccessListener

```
public @NonNull StorageTask<ResultT> removeOnSuccessListener(@NonNull OnSuccessListener<Object> listener)
```

Removes a listener.

### resume

```
public boolean resume()
```

Attempts to resume a paused task.

| Returns |
|---|---|
| `boolean` | `true` if the task is successfully resumed. `false` if the task has an unrecoverable error or has entered another state that precludes resume. |

## Protected methods

### onCanceled

```
protected void onCanceled()
```

### onFailure

```
protected void onFailure()
```

### onPaused

```
protected void onPaused()
```

### onProgress

```
protected void onProgress()
```

### onQueued

```
protected void onQueued()
```

### onSuccess

```
protected void onSuccess()
```

## Extension functions

### StorageKt.getTaskState

```
public final @NonNull Flow<@NonNull TaskState<@NonNull T>> StorageKt.getTaskState(@NonNull StorageTask<@NonNull T> receiver)
```