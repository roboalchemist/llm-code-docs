# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEventListener.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEventListener.md.txt

# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ChildEventListener.md.txt

# ChildEventListener

public interface **ChildEventListener**  
Classes implementing this interface can be used to receive events about changes in the child
locations of a given [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference) ref. Attach the listener to a
location using [addChildEventListener(ChildEventListener)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#addChildEventListener(com.google.firebase.database.ChildEventListener)) and the
appropriate method will be triggered when changes occur.  

### Public Method Summary

|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract void | [onCancelled](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ChildEventListener#onCancelled(com.google.firebase.database.DatabaseError))([DatabaseError](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError) error) This method will be triggered in the event that this listener either failed at the server, or is removed as a result of the security and Firebase rules. |
| abstract void | [onChildAdded](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ChildEventListener#onChildAdded(com.google.firebase.database.DataSnapshot, java.lang.String))([DataSnapshot](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot) snapshot, String previousChildName) This method is triggered when a new child is added to the location to which this listener was added.       |
| abstract void | [onChildChanged](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ChildEventListener#onChildChanged(com.google.firebase.database.DataSnapshot, java.lang.String))([DataSnapshot](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot) snapshot, String previousChildName) This method is triggered when the data at a child location has changed.                                |
| abstract void | [onChildMoved](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ChildEventListener#onChildMoved(com.google.firebase.database.DataSnapshot, java.lang.String))([DataSnapshot](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot) snapshot, String previousChildName) This method is triggered when a child location's priority changes.                                         |
| abstract void | [onChildRemoved](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ChildEventListener#onChildRemoved(com.google.firebase.database.DataSnapshot))([DataSnapshot](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot) snapshot) This method is triggered when a child is removed from the location to which this listener was added.                                               |

## Public Methods

#### public abstract void
**onCancelled**
([DatabaseError](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError) error)

This method will be triggered in the event that this listener either failed at the server, or
is removed as a result of the security and Firebase rules. For more information on securing
your data, see: [Security Quickstart](https://firebase.google.com/docs/database/security/quickstart)  

##### Parameters

| error | A description of the error that occurred |
|-------|------------------------------------------|

#### public abstract void
**onChildAdded**
([DataSnapshot](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot) snapshot, String previousChildName)

This method is triggered when a new child is added to the location to which this listener was
added.  

##### Parameters

|     snapshot      |                               An immutable snapshot of the data at the new child location                                |
| previousChildName | The key name of sibling location ordered before the new child. This will be null for the first child node of a location. |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|

#### public abstract void
**onChildChanged**
([DataSnapshot](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot) snapshot, String previousChildName)

This method is triggered when the data at a child location has changed.  

##### Parameters

|     snapshot      |                       An immutable snapshot of the data at the new data at the child location                        |
| previousChildName | The key name of sibling location ordered before the child. This will be null for the first child node of a location. |
|-------------------|----------------------------------------------------------------------------------------------------------------------|

#### public abstract void
**onChildMoved**
([DataSnapshot](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot) snapshot, String previousChildName)

This method is triggered when a child location's priority changes. See [setPriorityAsync(Object)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#setPriorityAsync(java.lang.Object)) and [Ordered Data](https://firebase.google.com/docs/database/android/retrieve-data#data_order) for more information on priorities and ordering data.  

##### Parameters

|     snapshot      |                                An immutable snapshot of the data at the location that moved.                                 |
| previousChildName | The key name of the sibling location ordered before the child location. This will be null if this location is ordered first. |
|-------------------|------------------------------------------------------------------------------------------------------------------------------|

#### public abstract void
**onChildRemoved**
([DataSnapshot](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot) snapshot)

This method is triggered when a child is removed from the location to which this listener was
added.  

##### Parameters

| snapshot | An immutable snapshot of the data at the child that was removed. |
|----------|------------------------------------------------------------------|