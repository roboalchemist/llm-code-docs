# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/CancellableTask.md.txt

# CancellableTask

# CancellableTask


```
public abstract class CancellableTask<StateT> extends Task
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.android.gms.tasks.Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) ||
|   | ↳ | [com.google.firebase.storage.CancellableTask](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/CancellableTask) |

Known direct subclasses [ControllableTask](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ControllableTask)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ControllableTask` | Represents an asynchronous operation that can be paused, resumed and canceled. |

Known indirect subclasses [FileDownloadTask](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask), [StorageTask](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask), [StreamDownloadTask](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask), [UploadTask](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask` | A task that downloads bytes of a GCS blob to a specified File. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask` | A controllable Task that has a synchronized state machine. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask` | A task that downloads bytes of a GCS blob. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` | An controllable task that uploads and fires events for success, progress and failure. |

*** ** * ** ***

Represents an asynchronous operation that can be canceled.

| Parameters |
|---|---|
| `<StateT>` | the type of state this operation returns in events. |

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/CancellableTask#CancellableTask()()` |

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/CancellableTask<StateT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/CancellableTask#addOnProgressListener(com.google.firebase.storage.OnProgressListener<? super StateT>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/OnProgressListener<https://developer.android.com/reference/kotlin/java/lang/Object.html> listener)` Adds a listener that is called periodically while the ControllableTask executes. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/CancellableTask<StateT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/CancellableTask#addOnProgressListener(android.app.Activity,com.google.firebase.storage.OnProgressListener<? super StateT>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/OnProgressListener<https://developer.android.com/reference/kotlin/java/lang/Object.html> listener )` Adds a listener that is called periodically while the ControllableTask executes. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/CancellableTask<StateT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/CancellableTask#addOnProgressListener(java.util.concurrent.Executor,com.google.firebase.storage.OnProgressListener<? super StateT>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/OnProgressListener<https://developer.android.com/reference/kotlin/java/lang/Object.html> listener )` Adds a listener that is called periodically while the ControllableTask executes. |
| `abstract boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/CancellableTask#cancel()()` Attempts to cancel the task. |
| `abstract boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/CancellableTask#isCanceled()()` |
| `abstract boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/CancellableTask#isInProgress()()` |

| ### Inherited methods |
|---|
| From [com.google.android.gms.tasks.Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) |---|---| | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnCanceledListener-com.google.android.gms.tasks.OnCanceledListener-(https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html p)` | | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnCompleteListener-com.google.android.gms.tasks.OnCompleteListener&lt;TResult&gt;-(https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html<TResult> p)` | | `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnFailureListener-com.google.android.gms.tasks.OnFailureListener-(https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html p)` | | `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnSuccessListener-com.google.android.gms.tasks.OnSuccessListener&lt;? super TResult&gt;-(https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html<https://developer.android.com/reference/kotlin/java/lang/Object.html> p)` | | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult>` | `<TContinuationResult> https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#continueWith-com.google.android.gms.tasks.Continuation&lt;TResult,TContinuationResult&gt;-( https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<TResult, TContinuationResult> p )` | | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult>` | `<TContinuationResult> https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#continueWithTask-com.google.android.gms.tasks.Continuation&lt;TResult,com.google.android.gms.tasks.Task&lt;TContinuationResult&gt;&gt;-( https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<TResult, https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult>> p )` | | `abstract https://developer.android.com/reference/kotlin/java/lang/Exception.html` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#getException--()` | | `abstract TResult` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#getResult--()` | | `abstract boolean` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isComplete--()` | | `abstract boolean` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isSuccessful--()` | | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult>` | `<TContinuationResult> https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#onSuccessTask-com.google.android.gms.tasks.SuccessContinuation&lt;TResult,TContinuationResult&gt;-( https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html<TResult, TContinuationResult> p )` | |

## Public constructors

### CancellableTask

```
public CancellableTask()
```

## Public methods

### addOnProgressListener

```
public abstract @NonNull CancellableTask<StateT> addOnProgressListener(@NonNull OnProgressListener<Object> listener)
```

Adds a listener that is called periodically while the ControllableTask executes.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/CancellableTask<StateT>` | this Task |

### addOnProgressListener

```
public abstract @NonNull CancellableTask<StateT> addOnProgressListener(
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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/CancellableTask<StateT>` | this Task |

### addOnProgressListener

```
public abstract @NonNull CancellableTask<StateT> addOnProgressListener(
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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/CancellableTask<StateT>` | this Task |

### cancel

```
public abstract boolean cancel()
```

Attempts to cancel the task. A canceled task cannot be resumed later. A canceled task calls back on listeners subscribed to `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnFailureListener-com.google.android.gms.tasks.OnFailureListener-` with an exception that indicates the task was canceled.

| Returns |
|---|---|
| `boolean` | true if this task was successfully canceled or is in the process of being canceled. Returns false if the task is already completed or in a state that cannot be canceled. |

### isCanceled

```
public abstract boolean isCanceled()
```

| Returns |
|---|---|
| `boolean` | true if the task has been canceled. |

### isInProgress

```
public abstract boolean isInProgress()
```

| Returns |
|---|---|
| `boolean` | true if the task is currently running. |