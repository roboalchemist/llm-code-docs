# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction.Handler.md.txt

# Transaction.Handler

# Transaction.Handler


```
public interface Transaction.Handler
```

<br />

*** ** * ** ***

An object implementing this interface is used to run a transaction, and will be notified of the results of the transaction.

## Summary

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction.Result` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction.Handler#doTransaction(com.google.firebase.database.MutableData)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData currentData)` This method will be called, *possibly multiple times*, with the current data at this location. |
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction.Handler#onComplete(com.google.firebase.database.DatabaseError,boolean,com.google.firebase.database.DataSnapshot)( @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError error, boolean committed, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot currentData )` This method will be called once with the results of the transaction. |

## Public methods

### doTransaction

```
abstract @NonNull Transaction.Result doTransaction(@NonNull MutableData currentData)
```

This method will be called, *possibly multiple times* , with the current data at this location. It is responsible for inspecting that data and returning a `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction.Result` specifying either the desired new data at the location or that the transaction should be aborted. Since this method may be called repeatedly for the same transaction, be extremely careful of any side effects that may be triggered by this method. In addition, this method is called from within the Firebase Database library's run loop, so care is also required when accessing data that may be in use by other threads in your application. Best practices for this method are to rely only on the data that is passed in.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData currentData` | The current data at the location. Update this to the desired data at the location |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction.Result` | Either the new data, or an indication to abort the transaction |

### onComplete

```
abstract void onComplete(
    @Nullable DatabaseError error,
    boolean committed,
    @Nullable DataSnapshot currentData
)
```

This method will be called once with the results of the transaction.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError error` | null if no errors occurred, otherwise it contains a description of the error |
| `boolean committed` | True if the transaction successfully completed, false if it was aborted or an error occurred |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot currentData` | The current data at the location or null if an error occurred |