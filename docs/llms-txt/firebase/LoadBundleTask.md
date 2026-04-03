# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/LoadBundleTask.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/LoadBundleTask.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask.md.txt

# LoadBundleTask

# LoadBundleTask


```
class LoadBundleTask : Task
```

<br />

|---|---|------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                    |||
| â³ | [com.google.android.gms.tasks.Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)                       ||
|   | â³ | [com.google.firebase.firestore.LoadBundleTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask) |

*** ** * ** ***

Represents the task of loading a Firestore bundle. It provides progress of bundle loading, as well as task completion and error events.

## Summary

|                                                                                                         ### Public functions                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | [addOnCanceledListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnCanceledListener(com.google.android.gms.tasks.OnCanceledListener))`(onCanceledListener: `[OnCanceledListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html)`)` Adds a listener that is called if the `Task` is canceled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | [addOnCanceledListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnCanceledListener(android.app.Activity,com.google.android.gms.tasks.OnCanceledListener))`(` ` activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html)`,` ` onCanceledListener: `[OnCanceledListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html) `)` Adds an Activity-scoped listener that is called if the `Task` is canceled.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | [addOnCanceledListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnCanceledListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnCanceledListener))`(` ` executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)`,` ` onCanceledListener: `[OnCanceledListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html) `)` Adds a listener that is called if the `Task` is canceled.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | [addOnCompleteListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnCompleteListener(com.google.android.gms.tasks.OnCompleteListener<com.google.firebase.firestore.LoadBundleTaskProgress>))`(` ` onCompleteListener: `[OnCompleteListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` `)` Adds a listener that is called when the `Task` succeeds or fails.                                                                                                                                                                                                                                                                                                                                                                    |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | [addOnCompleteListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnCompleteListener(android.app.Activity,com.google.android.gms.tasks.OnCompleteListener<com.google.firebase.firestore.LoadBundleTaskProgress>))`(` ` activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html)`,` ` onCompleteListener: `[OnCompleteListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` `)` Adds a listener that is called when the `Task` succeeds or fails.                                                                                                                                                                                                                                          |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | [addOnCompleteListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnCompleteListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnCompleteListener<com.google.firebase.firestore.LoadBundleTaskProgress>))`(` ` executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)`,` ` onCompleteListener: `[OnCompleteListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` `)` Adds a listener that is called when the `Task` succeeds or fails.                                                                                                                                                                                                                        |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | [addOnFailureListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnFailureListener(com.google.android.gms.tasks.OnFailureListener))`(onFailureListener: `[OnFailureListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html)`)` Adds a listener that is called if the `Task` fails.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | [addOnFailureListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnFailureListener(android.app.Activity,com.google.android.gms.tasks.OnFailureListener))`(` ` activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html)`,` ` onFailureListener: `[OnFailureListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html) `)` Adds a listener that is called if the `Task` fails.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | [addOnFailureListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnFailureListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnFailureListener))`(` ` executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)`,` ` onFailureListener: `[OnFailureListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html) `)` Adds a listener that is called if the `Task` fails.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [LoadBundleTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask)                                                                                                                      | [addOnProgressListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnProgressListener(com.google.firebase.firestore.OnProgressListener<com.google.firebase.firestore.LoadBundleTaskProgress>))`(` ` listener: `[OnProgressListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/OnProgressListener)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` `)` Adds a listener that is called periodically while the `LoadBundleTask` executes.                                                                                                                                                                                                                                                                                                                                                                |
| [LoadBundleTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask)                                                                                                                      | [addOnProgressListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnProgressListener(android.app.Activity,com.google.firebase.firestore.OnProgressListener<com.google.firebase.firestore.LoadBundleTaskProgress>))`(` ` activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html)`,` ` listener: `[OnProgressListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/OnProgressListener)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` `)` Adds a listener that is called periodically while the `LoadBundleTask` executes.                                                                                                                                                                                                                                      |
| [LoadBundleTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask)                                                                                                                      | [addOnProgressListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnProgressListener(java.util.concurrent.Executor,com.google.firebase.firestore.OnProgressListener<com.google.firebase.firestore.LoadBundleTaskProgress>))`(` ` executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)`,` ` listener: `[OnProgressListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/OnProgressListener)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` `)` Adds a listener that is called periodically while the `LoadBundleTask` executes.                                                                                                                                                                                                                    |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | [addOnSuccessListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnSuccessListener(com.google.android.gms.tasks.OnSuccessListener<? super com.google.firebase.firestore.LoadBundleTaskProgress>))`(onSuccessListener: `[OnSuccessListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>)` Adds a listener that is called if the `Task` completes successfully.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | [addOnSuccessListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnSuccessListener(android.app.Activity,com.google.android.gms.tasks.OnSuccessListener<? super com.google.firebase.firestore.LoadBundleTaskProgress>))`(` ` activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html)`,` ` onSuccessListener: `[OnSuccessListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>` `)` Adds a listener that is called if the `Task` completes successfully.                                                                                                                                                                                                                                                                                           |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | [addOnSuccessListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#addOnSuccessListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnSuccessListener<? super com.google.firebase.firestore.LoadBundleTaskProgress>))`(` ` executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)`,` ` onSuccessListener: `[OnSuccessListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>` `)` Adds a listener that is called if the `Task` completes successfully.                                                                                                                                                                                                                                                                         |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<TContinuationResult!>`                                                                                                                | `<TContinuationResult> `[continueWith](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#continueWith(com.google.android.gms.tasks.Continuation<com.google.firebase.firestore.LoadBundleTaskProgress,TContinuationResult>))`(` ` continuation: `[Continuation](https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!, TContinuationResult!>` `)` Returns a new `Task` that will be completed with the result of applying the specified Continuation to this Task.                                                                                                                                                                                                                                                                                             |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<TContinuationResult!>`                                                                                                                | `<TContinuationResult> `[continueWith](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#continueWith(java.util.concurrent.Executor,com.google.android.gms.tasks.Continuation<com.google.firebase.firestore.LoadBundleTaskProgress,TContinuationResult>))`(` ` executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)`,` ` continuation: `[Continuation](https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!, TContinuationResult!>` `)` Returns a new `Task` that will be completed with the result of applying the specified `Continuation` to this Task.                                                                                                                                               |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<TContinuationResult!>`                                                                                                                | `<TContinuationResult> `[continueWithTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#continueWithTask(com.google.android.gms.tasks.Continuation<com.google.firebase.firestore.LoadBundleTaskProgress,com.google.android.gms.tasks.Task<TContinuationResult>>))`(` ` continuation: `[Continuation](https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!, `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<TContinuationResult!>!>` `)` Returns a new `Task` that will be completed with the result of applying the specified `Continuation` to this Task.                                                                                                                                             |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<TContinuationResult!>`                                                                                                                | `<TContinuationResult> `[continueWithTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#continueWithTask(java.util.concurrent.Executor,com.google.android.gms.tasks.Continuation<com.google.firebase.firestore.LoadBundleTaskProgress,com.google.android.gms.tasks.Task<TContinuationResult>>))`(` ` executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)`,` ` continuation: `[Continuation](https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!, `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<TContinuationResult!>!>` `)` Returns a new `Task` that will be completed with the result of applying the specified `Continuation` to this Task. |
| [Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html)`?`                                                                                                                                               | [getException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#getException())`()` Returns the exception that caused the `Task` to fail.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)                                                                                                      | [getResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#getResult())`()` Gets the result of the `Task`, if it has already completed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)                                                                                                      | `<X : `[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`?> `[getResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#getResult(java.lang.Class<X>))`(exceptionType: `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<X!>)` Gets the result of the `Task`, if it has already completed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                                                                    | [isCanceled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#isCanceled())`()` Returns `true` if the task has been canceled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                                                                    | [isComplete](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#isComplete())`()` Returns `true` if the `Task` is complete; `false` otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                                                                    | [isSuccessful](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#isSuccessful())`()` Returns `true` if the `Task` has completed successfully; `false` otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<TContinuationResult!>`                                                                                                                | `<TContinuationResult> `[onSuccessTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#onSuccessTask(com.google.android.gms.tasks.SuccessContinuation<com.google.firebase.firestore.LoadBundleTaskProgress,TContinuationResult>))`(` ` successContinuation: `[SuccessContinuation](https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!, TContinuationResult!>` `)` Returns a new `Task` that will be completed with the result of applying the specified `SuccessContinuation` to this `Task` when this `Task` completes successfully.                                                                                                                                                                                                            |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<TContinuationResult!>`                                                                                                                | `<TContinuationResult> `[onSuccessTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#onSuccessTask(java.util.concurrent.Executor,com.google.android.gms.tasks.SuccessContinuation<com.google.firebase.firestore.LoadBundleTaskProgress,TContinuationResult>))`(` ` executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)`,` ` successContinuation: `[SuccessContinuation](https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!, TContinuationResult!>` `)` Returns a new `Task` that will be completed with the result of applying the specified `SuccessContinuation` to this `Task` when this `Task` completes successfully.                                                                |

## Public functions

### addOnCanceledListener

```
funÂ addOnCanceledListener(onCanceledListener:Â OnCanceledListener):Â Task<LoadBundleTaskProgress!>
```

Adds a listener that is called if the `Task` is canceled.

The listener will be called on main application thread. If the `Task` has already been canceled, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.  

|                                                                                                                Returns                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | this `Task` |

### addOnCanceledListener

```
funÂ addOnCanceledListener(
Â Â Â Â activity:Â Activity,
Â Â Â Â onCanceledListener:Â OnCanceledListener
):Â Task<LoadBundleTaskProgress!>
```

Adds an Activity-scoped listener that is called if the `Task` is canceled.

The listener will be called on main application thread. If the task has already been canceled, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.

The listener will be automatically removed during [onStop](https://developer.android.com/reference/kotlin/android/app/Activity.html#onStop--).  

|                                                                                                                Returns                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | this Task |

### addOnCanceledListener

```
funÂ addOnCanceledListener(
Â Â Â Â executor:Â Executor,
Â Â Â Â onCanceledListener:Â OnCanceledListener
):Â Task<LoadBundleTaskProgress!>
```

Adds a listener that is called if the `Task` is canceled.

If the task has already been canceled, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------|
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) | the executor to use to call the listener |

|                                                                                                                Returns                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | this Task |

### addOnCompleteListener

```
funÂ addOnCompleteListener(
Â Â Â Â onCompleteListener:Â OnCompleteListener<LoadBundleTaskProgress!>
):Â Task<LoadBundleTaskProgress!>
```

Adds a listener that is called when the `Task` succeeds or fails.

The listener will be called on main application thread. If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.  

|                                                                                                                Returns                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | this `Task` |

### addOnCompleteListener

```
funÂ addOnCompleteListener(
Â Â Â Â activity:Â Activity,
Â Â Â Â onCompleteListener:Â OnCompleteListener<LoadBundleTaskProgress!>
):Â Task<LoadBundleTaskProgress!>
```

Adds a listener that is called when the `Task` succeeds or fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.  

|                                            Parameters                                            |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) | When the supplied [Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) stops, this listener will automatically be removed. |

|                                                                                                                Returns                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | this `Task` |

### addOnCompleteListener

```
funÂ addOnCompleteListener(
Â Â Â Â executor:Â Executor,
Â Â Â Â onCompleteListener:Â OnCompleteListener<LoadBundleTaskProgress!>
):Â Task<LoadBundleTaskProgress!>
```

Adds a listener that is called when the `Task` succeeds or fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------|
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) | the executor to use to call the listener |

|                                                                                                                Returns                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | this `Task` |

### addOnFailureListener

```
funÂ addOnFailureListener(onFailureListener:Â OnFailureListener):Â Task<LoadBundleTaskProgress!>
```

Adds a listener that is called if the `Task` fails.

The listener will be called on main application thread. If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.  

|                                                                                                                Returns                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | this `Task` |

### addOnFailureListener

```
funÂ addOnFailureListener(
Â Â Â Â activity:Â Activity,
Â Â Â Â onFailureListener:Â OnFailureListener
):Â Task<LoadBundleTaskProgress!>
```

Adds a listener that is called if the `Task` fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.  

|                                            Parameters                                            |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) | When the supplied [Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) stops, this listener will automatically be removed. |

|                                                                                                                Returns                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | this `Task` |

### addOnFailureListener

```
funÂ addOnFailureListener(
Â Â Â Â executor:Â Executor,
Â Â Â Â onFailureListener:Â OnFailureListener
):Â Task<LoadBundleTaskProgress!>
```

Adds a listener that is called if the `Task` fails.

If the task has already failed, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------|
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) | the executor to use to call the listener |

|                                                                                                                Returns                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | this `Task` |

### addOnProgressListener

```
funÂ addOnProgressListener(
Â Â Â Â listener:Â OnProgressListener<LoadBundleTaskProgress!>
):Â LoadBundleTask
```

Adds a listener that is called periodically while the `LoadBundleTask` executes.

The listener will be called on main application thread. If multiple listeners are added, they will be called in the order in which they were added.

The listener will be automatically removed during [onStop](https://developer.android.com/reference/kotlin/android/app/Activity.html#onStop--).  

|                                                     Returns                                                      |
|------------------------------------------------------------------------------------------------------------------|-------------|
| [LoadBundleTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask) | this `Task` |

### addOnProgressListener

```
funÂ addOnProgressListener(
Â Â Â Â activity:Â Activity,
Â Â Â Â listener:Â OnProgressListener<LoadBundleTaskProgress!>
):Â LoadBundleTask
```

Adds a listener that is called periodically while the `LoadBundleTask` executes.

The listener will be called on main application thread. If multiple listeners are added, they will be called in the order in which they were added.

The listener will be automatically removed during [onStop](https://developer.android.com/reference/kotlin/android/app/Activity.html#onStop--).  

|                                            Parameters                                            |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) | When the supplied [Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) stops, this listener will automatically be removed. |

|                                                     Returns                                                      |
|------------------------------------------------------------------------------------------------------------------|-------------|
| [LoadBundleTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask) | this `Task` |

### addOnProgressListener

```
funÂ addOnProgressListener(
Â Â Â Â executor:Â Executor,
Â Â Â Â listener:Â OnProgressListener<LoadBundleTaskProgress!>
):Â LoadBundleTask
```

Adds a listener that is called periodically while the `LoadBundleTask` executes.

If multiple listeners are added, they will be called in the order in which they were added.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------|
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) | the executor to use to call the listener |

|                                                     Returns                                                      |
|------------------------------------------------------------------------------------------------------------------|-------------|
| [LoadBundleTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask) | this `Task` |

### addOnSuccessListener

```
funÂ addOnSuccessListener(onSuccessListener:Â OnSuccessListener<Any!>):Â Task<LoadBundleTaskProgress!>
```

Adds a listener that is called if the `Task` completes successfully. The listener will be called on the main application thread. If the task has already completed successfully, a call to the listener will be immediately scheduled. If multiple listeners are added, they will be called in the order in which they were added.  

|                                                                                                                Returns                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | this `Task` |

### addOnSuccessListener

```
funÂ addOnSuccessListener(
Â Â Â Â activity:Â Activity,
Â Â Â Â onSuccessListener:Â OnSuccessListener<Any!>
):Â Task<LoadBundleTaskProgress!>
```

Adds a listener that is called if the `Task` completes successfully.

If multiple listeners are added, they will be called in the order in which they were added. If the task has already completed successfully, a call to the listener will be immediately scheduled.  

|                                            Parameters                                            |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `activity: `[Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) | When the supplied [Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) stops, this listener will automatically be removed. |

|                                                                                                                Returns                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | this `Task` |

### addOnSuccessListener

```
funÂ addOnSuccessListener(
Â Â Â Â executor:Â Executor,
Â Â Â Â onSuccessListener:Â OnSuccessListener<Any!>
):Â Task<LoadBundleTaskProgress!>
```

Adds a listener that is called if the `Task` completes successfully.

If multiple listeners are added, they will be called in the order in which they were added. If the task has already completed successfully, a call to the listener will be immediately scheduled.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------|
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) | the executor to use to call the listener |

|                                                                                                                Returns                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress)`!>` | this `Task` |

### continueWith

```
funÂ <TContinuationResult> continueWith(
Â Â Â Â continuation:Â Continuation<LoadBundleTaskProgress!,Â TContinuationResult!>
):Â Task<TContinuationResult!>
```

Returns a new `Task` that will be completed with the result of applying the specified Continuation to this Task.

The `Continuation` will be called on the main application thread.  

|                                                                           See also                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [then](https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-) |   |

### continueWith

```
funÂ <TContinuationResult> continueWith(
Â Â Â Â executor:Â Executor,
Â Â Â Â continuation:Â Continuation<LoadBundleTaskProgress!,Â TContinuationResult!>
):Â Task<TContinuationResult!>
```

Returns a new `Task` that will be completed with the result of applying the specified `Continuation` to this Task.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------|
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) | the executor to use to call the Continuation |

|                                                                           See also                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [then](https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-) |   |

### continueWithTask

```
funÂ <TContinuationResult> continueWithTask(
Â Â Â Â continuation:Â Continuation<LoadBundleTaskProgress!,Â Task<TContinuationResult!>!>
):Â Task<TContinuationResult!>
```

Returns a new `Task` that will be completed with the result of applying the specified `Continuation` to this Task.

The Continuation will be called on the main application thread.  

|                                                                           See also                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [then](https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-) |   |

### continueWithTask

```
funÂ <TContinuationResult> continueWithTask(
Â Â Â Â executor:Â Executor,
Â Â Â Â continuation:Â Continuation<LoadBundleTaskProgress!,Â Task<TContinuationResult!>!>
):Â Task<TContinuationResult!>
```

Returns a new `Task` that will be completed with the result of applying the specified `Continuation` to this Task.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------------|
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) | the executor to use to call the `Continuation` |

|                                                                           See also                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [then](https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html#then-com.google.android.gms.tasks.Task&lt;TResult&gt;-) |   |

### getException

```
funÂ getException():Â Exception?
```

Returns the exception that caused the `Task` to fail. Returns `null` if the Task is not yet complete, or completed successfully.  

### getResult

```
funÂ getResult():Â LoadBundleTaskProgress
```

Gets the result of the `Task`, if it has already completed.  

|                                                                                                             Throws                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| `java.lang.IllegalStateException: `[java.lang.IllegalStateException](https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html)                                                                       | if the Task is not yet complete      |
| `com.google.android.gms.tasks.RuntimeExecutionException: `[com.google.android.gms.tasks.RuntimeExecutionException](https://developers.google.com/android/reference/com/google/android/gms/tasks/RuntimeExecutionException.html) | if the Task failed with an exception |

### getResult

```
funÂ <XÂ :Â Throwable?> getResult(exceptionType:Â Class<X!>):Â LoadBundleTaskProgress
```

Gets the result of the `Task`, if it has already completed.  

|                                                                                                             Throws                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| `java.lang.IllegalStateException: `[java.lang.IllegalStateException](https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html)                                                                       | if the Task is not yet complete                             |
| `X: `[X](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask#getResult(java.lang.Class<X>))                                                                                          | if the Task failed with an exception of type X              |
| `com.google.android.gms.tasks.RuntimeExecutionException: `[com.google.android.gms.tasks.RuntimeExecutionException](https://developers.google.com/android/reference/com/google/android/gms/tasks/RuntimeExecutionException.html) | if the Task failed with an exception that was not of type X |

### isCanceled

```
funÂ isCanceled():Â Boolean
```

Returns `true` if the task has been canceled.  

### isComplete

```
funÂ isComplete():Â Boolean
```

Returns `true` if the `Task` is complete; `false` otherwise.  

### isSuccessful

```
funÂ isSuccessful():Â Boolean
```

Returns `true` if the `Task` has completed successfully; `false` otherwise.  

### onSuccessTask

```
funÂ <TContinuationResult> onSuccessTask(
Â Â Â Â successContinuation:Â SuccessContinuation<LoadBundleTaskProgress!,Â TContinuationResult!>
):Â Task<TContinuationResult!>
```

Returns a new `Task` that will be completed with the result of applying the specified `SuccessContinuation` to this `Task` when this `Task` completes successfully. If the previous `Task` fails, the `onSuccessTask` completion will be skipped and failure listeners will be invoked.

The `SuccessContinuation` will be called on the main application thread.

If the previous `Task` is canceled, the returned Task will also be canceled and the `SuccessContinuation` would not execute.  

|                                                           See also                                                           |
|------------------------------------------------------------------------------------------------------------------------------|---|
| [SuccessContinuation](https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html) |   |

### onSuccessTask

```
funÂ <TContinuationResult> onSuccessTask(
Â Â Â Â executor:Â Executor,
Â Â Â Â successContinuation:Â SuccessContinuation<LoadBundleTaskProgress!,Â TContinuationResult!>
):Â Task<TContinuationResult!>
```

Returns a new `Task` that will be completed with the result of applying the specified `SuccessContinuation` to this `Task` when this `Task` completes successfully. If the previous `Task` fails, the onSuccessTask completion will be skipped and failure listeners will be invoked.

If the previous `Task` is canceled, the returned `Task` will also be canceled and the `SuccessContinuation` would not execute.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) | the executor to use to call the SuccessContinuation |

|                                                           See also                                                           |
|------------------------------------------------------------------------------------------------------------------------------|---|
| [SuccessContinuation](https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html) |   |