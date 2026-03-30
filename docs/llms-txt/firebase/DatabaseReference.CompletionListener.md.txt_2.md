# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener.md.txt

# DatabaseReference.CompletionListener

# DatabaseReference.CompletionListener


```
public interface DatabaseReference.CompletionListener
```

<br />

*** ** * ** ***

This interface is used as a method of being notified when an operation has been acknowledged by the Database servers and can be considered complete

1.1

## Summary

| ### Public methods |
|---|---|
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener#onComplete(com.google.firebase.database.DatabaseError,com.google.firebase.database.DatabaseReference)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError error, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference ref)` This method will be triggered when the operation has either succeeded or failed. |

## Public methods

### onComplete

```
abstract void onComplete(@Nullable DatabaseError error, @NonNull DatabaseReference ref)
```

This method will be triggered when the operation has either succeeded or failed. If it has failed, an error will be given. If it has succeeded, the error will be null

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError error` | A description of any errors that occurred or null on success |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference ref` | A reference to the specified Firebase Database location |