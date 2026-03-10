# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask.md.txt

# UpdateTask

# UpdateTask


```
public abstract class UpdateTask extends Task
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.android.gms.tasks.Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) ||
|   | ↳ | [com.google.firebase.appdistribution.UpdateTask](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask) |

*** ** * ** ***

Represents an asynchronous operation to update an app.

This task also receives progress and other state change notifications.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask#UpdateTask()()` |

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask#addOnProgressListener(com.google.firebase.appdistribution.OnProgressListener)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/OnProgressListener listener)` Adds a listener that is called periodically while this `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask` executes. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask#addOnProgressListener(java.util.concurrent.Executor,com.google.firebase.appdistribution.OnProgressListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/OnProgressListener listener )` Adds a listener that is called periodically while `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask` executes. |

| ### Inherited methods |
|---|
| From [com.google.android.gms.tasks.Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) |---|---| | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnCanceledListener-com.google.android.gms.tasks.OnCanceledListener-(https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCanceledListener.html p)` | | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnCompleteListener-com.google.android.gms.tasks.OnCompleteListener&lt;TResult&gt;-(https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html<TResult> p)` | | `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnFailureListener-com.google.android.gms.tasks.OnFailureListener-(https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html p)` | | `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnSuccessListener-com.google.android.gms.tasks.OnSuccessListener&lt;? super TResult&gt;-(https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html<https://developer.android.com/reference/kotlin/java/lang/Object.html> p)` | | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult>` | `<TContinuationResult> https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#continueWith-com.google.android.gms.tasks.Continuation&lt;TResult,TContinuationResult&gt;-( https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<TResult, TContinuationResult> p )` | | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult>` | `<TContinuationResult> https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#continueWithTask-com.google.android.gms.tasks.Continuation&lt;TResult,com.google.android.gms.tasks.Task&lt;TContinuationResult&gt;&gt;-( https://developers.google.com/android/reference/com/google/android/gms/tasks/Continuation.html<TResult, https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult>> p )` | | `abstract https://developer.android.com/reference/kotlin/java/lang/Exception.html` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#getException--()` | | `abstract TResult` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#getResult--()` | | `abstract boolean` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isCanceled--()` | | `abstract boolean` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isComplete--()` | | `abstract boolean` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isSuccessful--()` | | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TContinuationResult>` | `<TContinuationResult> https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#onSuccessTask-com.google.android.gms.tasks.SuccessContinuation&lt;TResult,TContinuationResult&gt;-( https://developers.google.com/android/reference/com/google/android/gms/tasks/SuccessContinuation.html<TResult, TContinuationResult> p )` | |

## Public constructors

### UpdateTask

```
public UpdateTask()
```

## Public methods

### addOnProgressListener

```
public abstract @NonNull UpdateTask addOnProgressListener(@NonNull OnProgressListener listener)
```

Adds a listener that is called periodically while this `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask` executes.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask` | this `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask` |

### addOnProgressListener

```
public abstract @NonNull UpdateTask addOnProgressListener(
    @Nullable Executor executor,
    @NonNull OnProgressListener listener
)
```

Adds a listener that is called periodically while `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask` executes.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | the executor to use to call the listener |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask` | this `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateTask` |