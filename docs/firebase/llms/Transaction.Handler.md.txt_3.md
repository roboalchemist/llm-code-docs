# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Handler.md.txt

# Transaction.Handler

# Transaction.Handler


```
interface Transaction.Handler
```

<br />

*** ** * ** ***

An object implementing this interface is used to run a transaction, and will be notified of the results of the transaction.

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Result` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Handler#doTransaction(com.google.firebase.database.MutableData)(currentData: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData)` This method will be called, *possibly multiple times*, with the current data at this location. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Handler#onComplete(com.google.firebase.database.DatabaseError,boolean,com.google.firebase.database.DataSnapshot)( error: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError?, committed: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, currentData: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot? )` This method will be called once with the results of the transaction. |

## Public functions

### doTransaction

```
fun doTransaction(currentData: MutableData): Transaction.Result
```

This method will be called, *possibly multiple times* , with the current data at this location. It is responsible for inspecting that data and returning a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Result` specifying either the desired new data at the location or that the transaction should be aborted. Since this method may be called repeatedly for the same transaction, be extremely careful of any side effects that may be triggered by this method. In addition, this method is called from within the Firebase Database library's run loop, so care is also required when accessing data that may be in use by other threads in your application. Best practices for this method are to rely only on the data that is passed in.

| Parameters |
|---|---|
| `currentData: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData` | The current data at the location. Update this to the desired data at the location |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Result` | Either the new data, or an indication to abort the transaction |

### onComplete

```
fun onComplete(
    error: DatabaseError?,
    committed: Boolean,
    currentData: DataSnapshot?
): Unit
```

This method will be called once with the results of the transaction.

| Parameters |
|---|---|
| `error: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError?` | null if no errors occurred, otherwise it contains a description of the error |
| `committed: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | True if the transaction successfully completed, false if it was aborted or an error occurred |
| `currentData: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot?` | The current data at the location or null if an error occurred |