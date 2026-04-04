# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask.md.txt

# UpdateTask

# UpdateTask


```
abstract class UpdateTask : Task
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.android.gms.tasks.Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) ||
|   | ↳ | [com.google.firebase.appdistribution.UpdateTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask) |

*** ** * ** ***

Represents an asynchronous operation to update an app.

This task also receives progress and other state change notifications.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask#UpdateTask()()` |

| ### Public functions |
|---|---|
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask#addOnProgressListener(com.google.firebase.appdistribution.OnProgressListener)(listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/OnProgressListener)` Adds a listener that is called periodically while this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask` executes. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask#addOnProgressListener(java.util.concurrent.Executor,com.google.firebase.appdistribution.OnProgressListener)(executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html?, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/OnProgressListener)` Adds a listener that is called periodically while `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask` executes. |

| ### Inherited functions |
|---|
| From [com.google.android.gms.tasks.Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) |---|---| | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult!>!` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnCanceledListener-com.google.android.gms.tasks.OnCanceledListener-(p: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html!)` | | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult!>!` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnCompleteListener-com.google.android.gms.tasks.OnCompleteListener&lt;TResult&gt;-(p: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html<TResult!>!)` | | `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult!>!` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnFailureListener-com.google.android.gms.tasks.OnFailureListener-(p: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html!)` | | `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult!>!` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnSuccessListener-com.google.android.gms.tasks.OnSuccessListener&lt;? super TResult&gt;-(p: https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>!)` | | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult!>!` | `<TContinuationResult> https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#continueWith-com.google.android.gms.tasks.Continuation&lt;TResult,TContinuationResult&gt;-( p: https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<TResult!, TContinuationResult!>! )` | | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult!>!` | `<TContinuationResult> https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#continueWithTask-com.google.android.gms.tasks.Continuation&lt;TResult,com.google.android.gms.tasks.Task&lt;TContinuationResult&gt;&gt;-( p: https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<TResult!, https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult!>!>! )` | | `abstract https://developer.android.com/reference/kotlin/java/lang/Exception.html!` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#getException--()` | | `abstract TResult!` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#getResult--()` | | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isCanceled--()` | | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isComplete--()` | | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isSuccessful--()` | | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult!>!` | `<TContinuationResult> https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#onSuccessTask-com.google.android.gms.tasks.SuccessContinuation&lt;TResult,TContinuationResult&gt;-( p: https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html<TResult!, TContinuationResult!>! )` | |

## Public constructors

### UpdateTask

```
UpdateTask()
```

## Public functions

### addOnProgressListener

```
abstract fun addOnProgressListener(listener: OnProgressListener): UpdateTask
```

Adds a listener that is called periodically while this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask` executes.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask` | this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask` |

### addOnProgressListener

```
abstract fun addOnProgressListener(executor: Executor?, listener: OnProgressListener): UpdateTask
```

Adds a listener that is called periodically while `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask` executes.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html?` | the executor to use to call the listener |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask` | this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask` |