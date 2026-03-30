# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask.md.txt

# LoadBundleTask

# LoadBundleTask


```
class LoadBundleTask : Task
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.android.gms.tasks.Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) ||
|   | ↳ | [com.google.firebase.firestore.LoadBundleTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask) |

*** ** * ** ***

Represents the task of loading a Firestore bundle. It provides progress of bundle loading, as well as task completion and error events.

## Summary

| ### Public functions |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnCanceledListener(com.google.android.gms.tasks.OnCanceledListener)(onCanceledListener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html)` Adds a listener that is called if the `Task` is canceled. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnCanceledListener(android.app.Activity,com.google.android.gms.tasks.OnCanceledListener)( activity: https://developer.android.com/reference/kotlin/android/app/Activity.html, onCanceledListener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html )` Adds an Activity-scoped listener that is called if the `Task` is canceled. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnCanceledListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnCanceledListener)( executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, onCanceledListener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html )` Adds a listener that is called if the `Task` is canceled. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnCompleteListener(com.google.android.gms.tasks.OnCompleteListener<com.google.firebase.firestore.LoadBundleTaskProgress>)( onCompleteListener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!> )` Adds a listener that is called when the `Task` succeeds or fails. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnCompleteListener(android.app.Activity,com.google.android.gms.tasks.OnCompleteListener<com.google.firebase.firestore.LoadBundleTaskProgress>)( activity: https://developer.android.com/reference/kotlin/android/app/Activity.html, onCompleteListener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!> )` Adds a listener that is called when the `Task` succeeds or fails. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnCompleteListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnCompleteListener<com.google.firebase.firestore.LoadBundleTaskProgress>)( executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, onCompleteListener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!> )` Adds a listener that is called when the `Task` succeeds or fails. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnFailureListener(com.google.android.gms.tasks.OnFailureListener)(onFailureListener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html)` Adds a listener that is called if the `Task` fails. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnFailureListener(android.app.Activity,com.google.android.gms.tasks.OnFailureListener)( activity: https://developer.android.com/reference/kotlin/android/app/Activity.html, onFailureListener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html )` Adds a listener that is called if the `Task` fails. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnFailureListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnFailureListener)( executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, onFailureListener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html )` Adds a listener that is called if the `Task` fails. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnProgressListener(com.google.firebase.firestore.OnProgressListener<com.google.firebase.firestore.LoadBundleTaskProgress>)( listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/OnProgressListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!> )` Adds a listener that is called periodically while the `LoadBundleTask` executes. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnProgressListener(android.app.Activity,com.google.firebase.firestore.OnProgressListener<com.google.firebase.firestore.LoadBundleTaskProgress>)( activity: https://developer.android.com/reference/kotlin/android/app/Activity.html, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/OnProgressListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!> )` Adds a listener that is called periodically while the `LoadBundleTask` executes. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnProgressListener(java.util.concurrent.Executor,com.google.firebase.firestore.OnProgressListener<com.google.firebase.firestore.LoadBundleTaskProgress>)( executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/OnProgressListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!> )` Adds a listener that is called periodically while the `LoadBundleTask` executes. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnSuccessListener(com.google.android.gms.tasks.OnSuccessListener<? super com.google.firebase.firestore.LoadBundleTaskProgress>)(onSuccessListener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Adds a listener that is called if the `Task` completes successfully. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnSuccessListener(android.app.Activity,com.google.android.gms.tasks.OnSuccessListener<? super com.google.firebase.firestore.LoadBundleTaskProgress>)( activity: https://developer.android.com/reference/kotlin/android/app/Activity.html, onSuccessListener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!> )` Adds a listener that is called if the `Task` completes successfully. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnSuccessListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnSuccessListener<? super com.google.firebase.firestore.LoadBundleTaskProgress>)( executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, onSuccessListener: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!> )` Adds a listener that is called if the `Task` completes successfully. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult!>` | `<TContinuationResult> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#continueWith(com.google.android.gms.tasks.Continuation<com.google.firebase.firestore.LoadBundleTaskProgress,TContinuationResult>)( continuation: https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!, TContinuationResult!> )` Returns a new `Task` that will be completed with the result of applying the specified Continuation to this Task. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult!>` | `<TContinuationResult> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#continueWith(java.util.concurrent.Executor,com.google.android.gms.tasks.Continuation<com.google.firebase.firestore.LoadBundleTaskProgress,TContinuationResult>)( executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, continuation: https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!, TContinuationResult!> )` Returns a new `Task` that will be completed with the result of applying the specified `Continuation` to this Task. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult!>` | `<TContinuationResult> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#continueWithTask(com.google.android.gms.tasks.Continuation<com.google.firebase.firestore.LoadBundleTaskProgress,com.google.android.gms.tasks.Task<TContinuationResult>>)( continuation: https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!, https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult!>!> )` Returns a new `Task` that will be completed with the result of applying the specified `Continuation` to this Task. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult!>` | `<TContinuationResult> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#continueWithTask(java.util.concurrent.Executor,com.google.android.gms.tasks.Continuation<com.google.firebase.firestore.LoadBundleTaskProgress,com.google.android.gms.tasks.Task<TContinuationResult>>)( executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, continuation: https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!, https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult!>!> )` Returns a new `Task` that will be completed with the result of applying the specified `Continuation` to this Task. |
| `https://developer.android.com/reference/kotlin/java/lang/Exception.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#getException()()` Returns the exception that caused the `Task` to fail. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#getResult()()` Gets the result of the `Task`, if it has already completed. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress` | `<X : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#getResult(java.lang.Class<X>)(exceptionType: https://developer.android.com/reference/kotlin/java/lang/Class.html<X!>)` Gets the result of the `Task`, if it has already completed. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#isCanceled()()` Returns `true` if the task has been canceled. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#isComplete()()` Returns `true` if the `Task` is complete; `false` otherwise. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#isSuccessful()()` Returns `true` if the `Task` has completed successfully; `false` otherwise. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult!>` | `<TContinuationResult> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#onSuccessTask(com.google.android.gms.tasks.SuccessContinuation<com.google.firebase.firestore.LoadBundleTaskProgress,TContinuationResult>)( successContinuation: https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!, TContinuationResult!> )` Returns a new `Task` that will be completed with the result of applying the specified `SuccessContinuation` to this `Task` when this `Task` completes successfully. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult!>` | `<TContinuationResult> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#onSuccessTask(java.util.concurrent.Executor,com.google.android.gms.tasks.SuccessContinuation<com.google.firebase.firestore.LoadBundleTaskProgress,TContinuationResult>)( executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, successContinuation: https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!, TContinuationResult!> )` Returns a new `Task` that will be completed with the result of applying the specified `SuccessContinuation` to this `Task` when this `Task` completes successfully. |

## Public functions

### addOnCanceledListener

```
fun addOnCanceledListener(onCanceledListener: OnCanceledListener): Task<LoadBundleTaskProgress!>
```

Adds a listener that is called if the `Task` is canceled.

The listener will be called on main application thread. If the `Task` has already been canceled, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | this `Task` |

### addOnCanceledListener

```
fun addOnCanceledListener(
    activity: Activity,
    onCanceledListener: OnCanceledListener
): Task<LoadBundleTaskProgress!>
```

Adds an Activity-scoped listener that is called if the `Task` is canceled.

The listener will be called on main application thread. If the task has already been canceled, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

The listener will be automatically removed during `https://developer.android.com/reference/kotlin/android/app/Activity.html#onStop--`.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | this Task |

### addOnCanceledListener

```
fun addOnCanceledListener(
    executor: Executor,
    onCanceledListener: OnCanceledListener
): Task<LoadBundleTaskProgress!>
```

Adds a listener that is called if the `Task` is canceled.

If the task has already been canceled, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | the executor to use to call the listener |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | this Task |

### addOnCompleteListener

```
fun addOnCompleteListener(
    onCompleteListener: OnCompleteListener<LoadBundleTaskProgress!>
): Task<LoadBundleTaskProgress!>
```

Adds a listener that is called when the `Task` succeeds or fails.

The listener will be called on main application thread. If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | this `Task` |

### addOnCompleteListener

```
fun addOnCompleteListener(
    activity: Activity,
    onCompleteListener: OnCompleteListener<LoadBundleTaskProgress!>
): Task<LoadBundleTaskProgress!>
```

Adds a listener that is called when the `Task` succeeds or fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `activity: https://developer.android.com/reference/kotlin/android/app/Activity.html` | When the supplied `https://developer.android.com/reference/kotlin/android/app/Activity.html` stops, this listener will automatically be removed. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | this `Task` |

### addOnCompleteListener

```
fun addOnCompleteListener(
    executor: Executor,
    onCompleteListener: OnCompleteListener<LoadBundleTaskProgress!>
): Task<LoadBundleTaskProgress!>
```

Adds a listener that is called when the `Task` succeeds or fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | the executor to use to call the listener |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | this `Task` |

### addOnFailureListener

```
fun addOnFailureListener(onFailureListener: OnFailureListener): Task<LoadBundleTaskProgress!>
```

Adds a listener that is called if the `Task` fails.

The listener will be called on main application thread. If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | this `Task` |

### addOnFailureListener

```
fun addOnFailureListener(
    activity: Activity,
    onFailureListener: OnFailureListener
): Task<LoadBundleTaskProgress!>
```

Adds a listener that is called if the `Task` fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `activity: https://developer.android.com/reference/kotlin/android/app/Activity.html` | When the supplied `https://developer.android.com/reference/kotlin/android/app/Activity.html` stops, this listener will automatically be removed. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | this `Task` |

### addOnFailureListener

```
fun addOnFailureListener(
    executor: Executor,
    onFailureListener: OnFailureListener
): Task<LoadBundleTaskProgress!>
```

Adds a listener that is called if the `Task` fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | the executor to use to call the listener |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | this `Task` |

### addOnProgressListener

```
fun addOnProgressListener(
    listener: OnProgressListener<LoadBundleTaskProgress!>
): LoadBundleTask
```

Adds a listener that is called periodically while the `LoadBundleTask` executes.

The listener will be called on main application thread. If multiple listeners are added, they will be called in the order in which they were added.

The listener will be automatically removed during `https://developer.android.com/reference/kotlin/android/app/Activity.html#onStop--`.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask` | this `Task` |

### addOnProgressListener

```
fun addOnProgressListener(
    activity: Activity,
    listener: OnProgressListener<LoadBundleTaskProgress!>
): LoadBundleTask
```

Adds a listener that is called periodically while the `LoadBundleTask` executes.

The listener will be called on main application thread. If multiple listeners are added, they will be called in the order in which they were added.

The listener will be automatically removed during `https://developer.android.com/reference/kotlin/android/app/Activity.html#onStop--`.

| Parameters |
|---|---|
| `activity: https://developer.android.com/reference/kotlin/android/app/Activity.html` | When the supplied `https://developer.android.com/reference/kotlin/android/app/Activity.html` stops, this listener will automatically be removed. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask` | this `Task` |

### addOnProgressListener

```
fun addOnProgressListener(
    executor: Executor,
    listener: OnProgressListener<LoadBundleTaskProgress!>
): LoadBundleTask
```

Adds a listener that is called periodically while the `LoadBundleTask` executes.

If multiple listeners are added, they will be called in the order in which they were added.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | the executor to use to call the listener |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask` | this `Task` |

### addOnSuccessListener

```
fun addOnSuccessListener(onSuccessListener: OnSuccessListener<Any!>): Task<LoadBundleTaskProgress!>
```

Adds a listener that is called if the `Task` completes successfully. The listener will be called on the main application thread. If the task has already completed successfully, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | this `Task` |

### addOnSuccessListener

```
fun addOnSuccessListener(
    activity: Activity,
    onSuccessListener: OnSuccessListener<Any!>
): Task<LoadBundleTaskProgress!>
```

Adds a listener that is called if the `Task` completes successfully.

If multiple listeners are added, they will be called in the order in which they were added. If the task has already completed successfully, a call to the listener will be immediately scheduled.

| Parameters |
|---|---|
| `activity: https://developer.android.com/reference/kotlin/android/app/Activity.html` | When the supplied `https://developer.android.com/reference/kotlin/android/app/Activity.html` stops, this listener will automatically be removed. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | this `Task` |

### addOnSuccessListener

```
fun addOnSuccessListener(
    executor: Executor,
    onSuccessListener: OnSuccessListener<Any!>
): Task<LoadBundleTaskProgress!>
```

Adds a listener that is called if the `Task` completes successfully.

If multiple listeners are added, they will be called in the order in which they were added. If the task has already completed successfully, a call to the listener will be immediately scheduled.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | the executor to use to call the listener |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress!>` | this `Task` |

### continueWith

```
fun <TContinuationResult> continueWith(
    continuation: Continuation<LoadBundleTaskProgress!, TContinuationResult!>
): Task<TContinuationResult!>
```

Returns a new `Task` that will be completed with the result of applying the specified Continuation to this Task.

The `Continuation` will be called on the main application thread.

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-` |   |

### continueWith

```
fun <TContinuationResult> continueWith(
    executor: Executor,
    continuation: Continuation<LoadBundleTaskProgress!, TContinuationResult!>
): Task<TContinuationResult!>
```

Returns a new `Task` that will be completed with the result of applying the specified `Continuation` to this Task.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | the executor to use to call the Continuation |

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-` |   |

### continueWithTask

```
fun <TContinuationResult> continueWithTask(
    continuation: Continuation<LoadBundleTaskProgress!, Task<TContinuationResult!>!>
): Task<TContinuationResult!>
```

Returns a new `Task` that will be completed with the result of applying the specified `Continuation` to this Task.

The Continuation will be called on the main application thread.

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-` |   |

### continueWithTask

```
fun <TContinuationResult> continueWithTask(
    executor: Executor,
    continuation: Continuation<LoadBundleTaskProgress!, Task<TContinuationResult!>!>
): Task<TContinuationResult!>
```

Returns a new `Task` that will be completed with the result of applying the specified `Continuation` to this Task.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | the executor to use to call the `Continuation` |

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-` |   |

### getException

```
fun getException(): Exception?
```

Returns the exception that caused the `Task` to fail. Returns `null` if the Task is not yet complete, or completed successfully.

### getResult

```
fun getResult(): LoadBundleTaskProgress
```

Gets the result of the `Task`, if it has already completed.

| Throws |
|---|---|
| `java.lang.IllegalStateException: https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html` | if the Task is not yet complete |
| `com.google.android.gms.tasks.RuntimeExecutionException: https://developers.google.com/android/reference/com/google/android/gms/tasks/RuntimeExecutionException.html` | if the Task failed with an exception |

### getResult

```
fun <X : Throwable?> getResult(exceptionType: Class<X!>): LoadBundleTaskProgress
```

Gets the result of the `Task`, if it has already completed.

| Throws |
|---|---|
| `java.lang.IllegalStateException: https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html` | if the Task is not yet complete |
| `X: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#getResult(java.lang.Class<X>)` | if the Task failed with an exception of type X |
| `com.google.android.gms.tasks.RuntimeExecutionException: https://developers.google.com/android/reference/com/google/android/gms/tasks/RuntimeExecutionException.html` | if the Task failed with an exception that was not of type X |

### isCanceled

```
fun isCanceled(): Boolean
```

Returns `true` if the task has been canceled.

### isComplete

```
fun isComplete(): Boolean
```

Returns `true` if the `Task` is complete; `false` otherwise.

### isSuccessful

```
fun isSuccessful(): Boolean
```

Returns `true` if the `Task` has completed successfully; `false` otherwise.

### onSuccessTask

```
fun <TContinuationResult> onSuccessTask(
    successContinuation: SuccessContinuation<LoadBundleTaskProgress!, TContinuationResult!>
): Task<TContinuationResult!>
```

Returns a new `Task` that will be completed with the result of applying the specified `SuccessContinuation` to this `Task` when this `Task` completes successfully. If the previous `Task` fails, the `onSuccessTask` completion will be skipped and failure listeners will be invoked.

The `SuccessContinuation` will be called on the main application thread.

If the previous `Task` is canceled, the returned Task will also be canceled and the `SuccessContinuation` would not execute.

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html` |   |

### onSuccessTask

```
fun <TContinuationResult> onSuccessTask(
    executor: Executor,
    successContinuation: SuccessContinuation<LoadBundleTaskProgress!, TContinuationResult!>
): Task<TContinuationResult!>
```

Returns a new `Task` that will be completed with the result of applying the specified `SuccessContinuation` to this `Task` when this `Task` completes successfully. If the previous `Task` fails, the onSuccessTask completion will be skipped and failure listeners will be invoked.

If the previous `Task` is canceled, the returned `Task` will also be canceled and the `SuccessContinuation` would not execute.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | the executor to use to call the SuccessContinuation |

| See also |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html` |   |