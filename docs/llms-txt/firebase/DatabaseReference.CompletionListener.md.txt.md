# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener.md.txt

# DatabaseReference.CompletionListener

public static interface **DatabaseReference.CompletionListener** This interface is used as a method of being notified when an operation has been acknowledged by
the Database servers and can be considered complete

### Public Method Summary

|---|---|
| abstract void | [onComplete](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener#onComplete(com.google.firebase.database.DatabaseError, com.google.firebase.database.DatabaseReference))([DatabaseError](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError) error, [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference) ref) This method will be triggered when the operation has either succeeded or failed. |

## Public Methods

#### public abstract void
**onComplete**
([DatabaseError](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError) error, [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference) ref)

This method will be triggered when the operation has either succeeded or failed. If it has
failed, an error will be given. If it has succeeded, the error will be null

##### Parameters

| error | A description of any errors that occurred or null on success |
| ref | A reference to the specified Firebase Database location |
|---|---|