# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ValueEventListener.md.txt

# ValueEventListener

public interface **ValueEventListener** Classes implementing this interface can be used to receive events about data changes at a
location. Attach the listener to a location user `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#addValueEventListener(com.google.firebase.database.ValueEventListener)`.

### Public Method Summary

|---|---|
| abstract void | [onCancelled](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ValueEventListener#onCancelled(com.google.firebase.database.DatabaseError))([DatabaseError](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError) error) This method will be triggered in the event that this listener either failed at the server, or is removed as a result of the security and Firebase Database rules. |
| abstract void | [onDataChange](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ValueEventListener#onDataChange(com.google.firebase.database.DataSnapshot))([DataSnapshot](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot) snapshot) This method will be called with a snapshot of the data at this location. |

## Public Methods

#### public abstract void
**onCancelled**
([DatabaseError](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError) error)

This method will be triggered in the event that this listener either failed at the server, or
is removed as a result of the security and Firebase Database rules. For more information on
securing your data, see:
[Security Quickstart](https://firebase.google.com/docs/database/security/quickstart)

##### Parameters

| error | A description of the error that occurred |
|---|---|

#### public abstract void
**onDataChange**
([DataSnapshot](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot) snapshot)

This method will be called with a snapshot of the data at this location. It will also be called
each time that data changes.

##### Parameters

| snapshot | The current data at the location |
|---|---|