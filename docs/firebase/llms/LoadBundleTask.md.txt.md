# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask.md.txt

# LoadBundleTask

# LoadBundleTask


```
public class LoadBundleTask extends Task
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.android.gms.tasks.Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) ||
|   | ↳ | [com.google.firebase.firestore.LoadBundleTask](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask) |

*** ** * ** ***

Represents the task of loading a Firestore bundle. It provides progress of bundle loading, as well as task completion and error events.

## Summary

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#addOnCanceledListener(com.google.android.gms.tasks.OnCanceledListener)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html onCanceledListener)` Adds a listener that is called if the `Task` is canceled. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#addOnCanceledListener(android.app.Activity,com.google.android.gms.tasks.OnCanceledListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html onCanceledListener )` Adds an Activity-scoped listener that is called if the `Task` is canceled. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#addOnCanceledListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnCanceledListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html onCanceledListener )` Adds a listener that is called if the `Task` is canceled. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#addOnCompleteListener(com.google.android.gms.tasks.OnCompleteListener<com.google.firebase.firestore.LoadBundleTaskProgress>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress> onCompleteListener )` Adds a listener that is called when the `Task` succeeds or fails. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#addOnCompleteListener(android.app.Activity,com.google.android.gms.tasks.OnCompleteListener<com.google.firebase.firestore.LoadBundleTaskProgress>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress> onCompleteListener )` Adds a listener that is called when the `Task` succeeds or fails. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#addOnCompleteListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnCompleteListener<com.google.firebase.firestore.LoadBundleTaskProgress>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress> onCompleteListener )` Adds a listener that is called when the `Task` succeeds or fails. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#addOnFailureListener(com.google.android.gms.tasks.OnFailureListener)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html onFailureListener)` Adds a listener that is called if the `Task` fails. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#addOnFailureListener(android.app.Activity,com.google.android.gms.tasks.OnFailureListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html onFailureListener )` Adds a listener that is called if the `Task` fails. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#addOnFailureListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnFailureListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html onFailureListener )` Adds a listener that is called if the `Task` fails. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#addOnProgressListener(com.google.firebase.firestore.OnProgressListener<com.google.firebase.firestore.LoadBundleTaskProgress>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/OnProgressListener<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress> listener )` Adds a listener that is called periodically while the `LoadBundleTask` executes. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#addOnProgressListener(android.app.Activity,com.google.firebase.firestore.OnProgressListener<com.google.firebase.firestore.LoadBundleTaskProgress>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/OnProgressListener<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress> listener )` Adds a listener that is called periodically while the `LoadBundleTask` executes. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#addOnProgressListener(java.util.concurrent.Executor,com.google.firebase.firestore.OnProgressListener<com.google.firebase.firestore.LoadBundleTaskProgress>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/OnProgressListener<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress> listener )` Adds a listener that is called periodically while the `LoadBundleTask` executes. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#addOnSuccessListener(com.google.android.gms.tasks.OnSuccessListener<? super com.google.firebase.firestore.LoadBundleTaskProgress>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html<https://developer.android.com/reference/kotlin/java/lang/Object.html> onSuccessListener )` Adds a listener that is called if the `Task` completes successfully. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#addOnSuccessListener(android.app.Activity,com.google.android.gms.tasks.OnSuccessListener<? super com.google.firebase.firestore.LoadBundleTaskProgress>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html<https://developer.android.com/reference/kotlin/java/lang/Object.html> onSuccessListener )` Adds a listener that is called if the `Task` completes successfully. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#addOnSuccessListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnSuccessListener<? super com.google.firebase.firestore.LoadBundleTaskProgress>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html<https://developer.android.com/reference/kotlin/java/lang/Object.html> onSuccessListener )` Adds a listener that is called if the `Task` completes successfully. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult>` | `<TContinuationResult> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#continueWith(com.google.android.gms.tasks.Continuation<com.google.firebase.firestore.LoadBundleTaskProgress,TContinuationResult>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress, TContinuationResult> continuation )` Returns a new `Task` that will be completed with the result of applying the specified Continuation to this Task. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult>` | `<TContinuationResult> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#continueWith(java.util.concurrent.Executor,com.google.android.gms.tasks.Continuation<com.google.firebase.firestore.LoadBundleTaskProgress,TContinuationResult>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress, TContinuationResult> continuation )` Returns a new `Task` that will be completed with the result of applying the specified `Continuation` to this Task. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult>` | `<TContinuationResult> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#continueWithTask(com.google.android.gms.tasks.Continuation<com.google.firebase.firestore.LoadBundleTaskProgress,com.google.android.gms.tasks.Task<TContinuationResult>>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress, https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult>> continuation )` Returns a new `Task` that will be completed with the result of applying the specified `Continuation` to this Task. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult>` | `<TContinuationResult> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#continueWithTask(java.util.concurrent.Executor,com.google.android.gms.tasks.Continuation<com.google.firebase.firestore.LoadBundleTaskProgress,com.google.android.gms.tasks.Task<TContinuationResult>>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress, https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult>> continuation )` Returns a new `Task` that will be completed with the result of applying the specified `Continuation` to this Task. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Exception.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#getException()()` Returns the exception that caused the `Task` to fail. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#getResult()()` Gets the result of the `Task`, if it has already completed. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress` | `<X extends https://developer.android.com/reference/kotlin/java/lang/Throwable.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#getResult(java.lang.Class<X>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<X> exceptionType)` Gets the result of the `Task`, if it has already completed. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#isCanceled()()` Returns `true` if the task has been canceled. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#isComplete()()` Returns `true` if the `Task` is complete; `false` otherwise. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#isSuccessful()()` Returns `true` if the `Task` has completed successfully; `false` otherwise. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult>` | `<TContinuationResult> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#onSuccessTask(com.google.android.gms.tasks.SuccessContinuation<com.google.firebase.firestore.LoadBundleTaskProgress,TContinuationResult>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress, TContinuationResult> successContinuation )` Returns a new `Task` that will be completed with the result of applying the specified `SuccessContinuation` to this `Task` when this `Task` completes successfully. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult>` | `<TContinuationResult> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#onSuccessTask(java.util.concurrent.Executor,com.google.android.gms.tasks.SuccessContinuation<com.google.firebase.firestore.LoadBundleTaskProgress,TContinuationResult>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress, TContinuationResult> successContinuation )` Returns a new `Task` that will be completed with the result of applying the specified `SuccessContinuation` to this `Task` when this `Task` completes successfully. |

## Public methods

### addOnCanceledListener

```
public @NonNull Task<LoadBundleTaskProgress> addOnCanceledListener(@NonNull OnCanceledListener onCanceledListener)
```

Adds a listener that is called if the `Task` is canceled.

The listener will be called on main application thread. If the `Task` has already been canceled, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | this `Task` |

### addOnCanceledListener

```
public @NonNull Task<LoadBundleTaskProgress> addOnCanceledListener(
    @NonNull Activity activity,
    @NonNull OnCanceledListener onCanceledListener
)
```

Adds an Activity-scoped listener that is called if the `Task` is canceled.

The listener will be called on main application thread. If the task has already been canceled, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

The listener will be automatically removed during `https://developer.android.com/reference/kotlin/android/app/Activity.html#onStop--`.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | this Task |

### addOnCanceledListener

```
public @NonNull Task<LoadBundleTaskProgress> addOnCanceledListener(
    @NonNull Executor executor,
    @NonNull OnCanceledListener onCanceledListener
)
```

Adds a listener that is called if the `Task` is canceled.

If the task has already been canceled, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | the executor to use to call the listener |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | this Task |

### addOnCompleteListener

```
public @NonNull Task<LoadBundleTaskProgress> addOnCompleteListener(
    @NonNull OnCompleteListener<LoadBundleTaskProgress> onCompleteListener
)
```

Adds a listener that is called when the `Task` succeeds or fails.

The listener will be called on main application thread. If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | this `Task` |

### addOnCompleteListener

```
public @NonNull Task<LoadBundleTaskProgress> addOnCompleteListener(
    @NonNull Activity activity,
    @NonNull OnCompleteListener<LoadBundleTaskProgress> onCompleteListener
)
```

Adds a listener that is called when the `Task` succeeds or fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity` | When the supplied `https://developer.android.com/reference/kotlin/android/app/Activity.html` stops, this listener will automatically be removed. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | this `Task` |

### addOnCompleteListener

```
public @NonNull Task<LoadBundleTaskProgress> addOnCompleteListener(
    @NonNull Executor executor,
    @NonNull OnCompleteListener<LoadBundleTaskProgress> onCompleteListener
)
```

Adds a listener that is called when the `Task` succeeds or fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | the executor to use to call the listener |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | this `Task` |

### addOnFailureListener

```
public @NonNull Task<LoadBundleTaskProgress> addOnFailureListener(@NonNull OnFailureListener onFailureListener)
```

Adds a listener that is called if the `Task` fails.

The listener will be called on main application thread. If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | this `Task` |

### addOnFailureListener

```
public @NonNull Task<LoadBundleTaskProgress> addOnFailureListener(
    @NonNull Activity activity,
    @NonNull OnFailureListener onFailureListener
)
```

Adds a listener that is called if the `Task` fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity` | When the supplied `https://developer.android.com/reference/kotlin/android/app/Activity.html` stops, this listener will automatically be removed. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | this `Task` |

### addOnFailureListener

```
public @NonNull Task<LoadBundleTaskProgress> addOnFailureListener(
    @NonNull Executor executor,
    @NonNull OnFailureListener onFailureListener
)
```

Adds a listener that is called if the `Task` fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | the executor to use to call the listener |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | this `Task` |

### addOnProgressListener

```
public @NonNull LoadBundleTask addOnProgressListener(
    @NonNull OnProgressListener<LoadBundleTaskProgress> listener
)
```

Adds a listener that is called periodically while the `LoadBundleTask` executes.

The listener will be called on main application thread. If multiple listeners are added, they will be called in the order in which they were added.

The listener will be automatically removed during `https://developer.android.com/reference/kotlin/android/app/Activity.html#onStop--`.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask` | this `Task` |

### addOnProgressListener

```
public @NonNull LoadBundleTask addOnProgressListener(
    @NonNull Activity activity,
    @NonNull OnProgressListener<LoadBundleTaskProgress> listener
)
```

Adds a listener that is called periodically while the `LoadBundleTask` executes.

The listener will be called on main application thread. If multiple listeners are added, they will be called in the order in which they were added.

The listener will be automatically removed during `https://developer.android.com/reference/kotlin/android/app/Activity.html#onStop--`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity` | When the supplied `https://developer.android.com/reference/kotlin/android/app/Activity.html` stops, this listener will automatically be removed. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask` | this `Task` |

### addOnProgressListener

```
public @NonNull LoadBundleTask addOnProgressListener(
    @NonNull Executor executor,
    @NonNull OnProgressListener<LoadBundleTaskProgress> listener
)
```

Adds a listener that is called periodically while the `LoadBundleTask` executes.

If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | the executor to use to call the listener |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask` | this `Task` |

### addOnSuccessListener

```
public @NonNull Task<LoadBundleTaskProgress> addOnSuccessListener(
    @NonNull OnSuccessListener<Object> onSuccessListener
)
```

Adds a listener that is called if the `Task` completes successfully. The listener will be called on the main application thread. If the task has already completed successfully, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | this `Task` |

### addOnSuccessListener

```
public @NonNull Task<LoadBundleTaskProgress> addOnSuccessListener(
    @NonNull Activity activity,
    @NonNull OnSuccessListener<Object> onSuccessListener
)
```

Adds a listener that is called if the `Task` completes successfully.

If multiple listeners are added, they will be called in the order in which they were added. If the task has already completed successfully, a call to the listener will be immediately scheduled.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity` | When the supplied `https://developer.android.com/reference/kotlin/android/app/Activity.html` stops, this listener will automatically be removed. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | this `Task` |

### addOnSuccessListener

```
public @NonNull Task<LoadBundleTaskProgress> addOnSuccessListener(
    @NonNull Executor executor,
    @NonNull OnSuccessListener<Object> onSuccessListener
)
```

Adds a listener that is called if the `Task` completes successfully.

If multiple listeners are added, they will be called in the order in which they were added. If the task has already completed successfully, a call to the listener will be immediately scheduled.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | the executor to use to call the listener |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress>` | this `Task` |

### continueWith

```
public @NonNull Task<TContinuationResult> <TContinuationResult> continueWith(
    @NonNull Continuation<LoadBundleTaskProgress, TContinuationResult> continuation
)
```

Returns a new `Task` that will be completed with the result of applying the specified Continuation to this Task.

The `Continuation` will be called on the main application thread.

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-` |   |

### continueWith

```
public @NonNull Task<TContinuationResult> <TContinuationResult> continueWith(
    @NonNull Executor executor,
    @NonNull Continuation<LoadBundleTaskProgress, TContinuationResult> continuation
)
```

Returns a new `Task` that will be completed with the result of applying the specified `Continuation` to this Task.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | the executor to use to call the Continuation |

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-` |   |

### continueWithTask

```
public @NonNull Task<TContinuationResult> <TContinuationResult> continueWithTask(
    @NonNull Continuation<LoadBundleTaskProgress, Task<TContinuationResult>> continuation
)
```

Returns a new `Task` that will be completed with the result of applying the specified `Continuation` to this Task.

The Continuation will be called on the main application thread.

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-` |   |

### continueWithTask

```
public @NonNull Task<TContinuationResult> <TContinuationResult> continueWithTask(
    @NonNull Executor executor,
    @NonNull Continuation<LoadBundleTaskProgress, Task<TContinuationResult>> continuation
)
```

Returns a new `Task` that will be completed with the result of applying the specified `Continuation` to this Task.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | the executor to use to call the `Continuation` |

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-` |   |

### getException

```
public @Nullable Exception getException()
```

Returns the exception that caused the `Task` to fail. Returns `null` if the Task is not yet complete, or completed successfully.

### getResult

```
public @NonNull LoadBundleTaskProgress getResult()
```

Gets the result of the `Task`, if it has already completed.

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html java.lang.IllegalStateException` | if the Task is not yet complete |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/RuntimeExecutionException.html com.google.android.gms.tasks.RuntimeExecutionException` | if the Task failed with an exception |

### getResult

```
public @NonNull LoadBundleTaskProgress <X extends Throwable> getResult(@NonNull Class<X> exceptionType)
```

Gets the result of the `Task`, if it has already completed.

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html java.lang.IllegalStateException` | if the Task is not yet complete |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask#getResult(java.lang.Class<X>) X` | if the Task failed with an exception of type X |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/RuntimeExecutionException.html com.google.android.gms.tasks.RuntimeExecutionException` | if the Task failed with an exception that was not of type X |

### isCanceled

```
public boolean isCanceled()
```

Returns `true` if the task has been canceled.

### isComplete

```
public boolean isComplete()
```

Returns `true` if the `Task` is complete; `false` otherwise.

### isSuccessful

```
public boolean isSuccessful()
```

Returns `true` if the `Task` has completed successfully; `false` otherwise.

### onSuccessTask

```
public @NonNull Task<TContinuationResult> <TContinuationResult> onSuccessTask(
    @NonNull SuccessContinuation<LoadBundleTaskProgress, TContinuationResult> successContinuation
)
```

Returns a new `Task` that will be completed with the result of applying the specified `SuccessContinuation` to this `Task` when this `Task` completes successfully. If the previous `Task` fails, the `onSuccessTask` completion will be skipped and failure listeners will be invoked.

The `SuccessContinuation` will be called on the main application thread.

If the previous `Task` is canceled, the returned Task will also be canceled and the `SuccessContinuation` would not execute.

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html` |   |

### onSuccessTask

```
public @NonNull Task<TContinuationResult> <TContinuationResult> onSuccessTask(
    @NonNull Executor executor,
    @NonNull SuccessContinuation<LoadBundleTaskProgress, TContinuationResult> successContinuation
)
```

Returns a new `Task` that will be completed with the result of applying the specified `SuccessContinuation` to this `Task` when this `Task` completes successfully. If the previous `Task` fails, the onSuccessTask completion will be skipped and failure listeners will be invoked.

If the previous `Task` is canceled, the returned `Task` will also be canceled and the `SuccessContinuation` would not execute.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | the executor to use to call the SuccessContinuation |

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html` |   |