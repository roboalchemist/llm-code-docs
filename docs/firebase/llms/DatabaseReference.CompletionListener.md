# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener.md.txt

# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener.md.txt

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

|                             ### Public functions                             |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [onComplete](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener#onComplete(com.google.firebase.database.DatabaseError,com.google.firebase.database.DatabaseReference))`(error: `[DatabaseError](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError)`?, ref: `[DatabaseReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference)`)` This method will be triggered when the operation has either succeeded or failed. |

## Public functions

### onComplete

```
funÂ onComplete(error:Â DatabaseError?,Â ref:Â DatabaseReference):Â Unit
```

This method will be triggered when the operation has either succeeded or failed. If it has failed, an error will be given. If it has succeeded, the error will be null  

|                                                          Parameters                                                          |
|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| `error: `[DatabaseError](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError)`?`    | A description of any errors that occurred or null on success |
| `ref: `[DatabaseReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference) | A reference to the specified Firebase Database location      |