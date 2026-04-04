# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener.md.txt

# DatabaseReference.CompletionListener

# DatabaseReference.CompletionListener


```
interface DatabaseReference.CompletionListener
```

<br />

*** ** * ** ***

This interface is used as a method of being notified when an operation has been acknowledged by the Database servers and can be considered complete

1.1

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener#onComplete(com.google.firebase.database.DatabaseError,com.google.firebase.database.DatabaseReference)(error: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError?, ref: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference)` This method will be triggered when the operation has either succeeded or failed. |

## Public functions

### onComplete

```
fun onComplete(error: DatabaseError?, ref: DatabaseReference): Unit
```

This method will be triggered when the operation has either succeeded or failed. If it has failed, an error will be given. If it has succeeded, the error will be null

| Parameters |
|---|---|
| `error: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError?` | A description of any errors that occurred or null on success |
| `ref: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference` | A reference to the specified Firebase Database location |