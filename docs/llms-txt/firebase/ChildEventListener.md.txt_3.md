# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEventListener.md.txt

# ChildEventListener

# ChildEventListener


```
interface ChildEventListener
```

<br />

*** ** * ** ***

Classes implementing this interface can be used to receive events about changes in the child locations of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference` ref. Attach the listener to a location using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#addChildEventListener(com.google.firebase.database.ChildEventListener)` and the appropriate method will be triggered when changes occur.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEventListener#onCancelled(com.google.firebase.database.DatabaseError)(error: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError)` This method will be triggered in the event that this listener either failed at the server, or is removed as a result of the security and Firebase rules. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEventListener#onChildAdded(com.google.firebase.database.DataSnapshot,java.lang.String)(snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot, previousChildName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` This method is triggered when a new child is added to the location to which this listener was added. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEventListener#onChildChanged(com.google.firebase.database.DataSnapshot,java.lang.String)(snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot, previousChildName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` This method is triggered when the data at a child location has changed. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEventListener#onChildMoved(com.google.firebase.database.DataSnapshot,java.lang.String)(snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot, previousChildName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` This method is triggered when a child location's priority changes. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEventListener#onChildRemoved(com.google.firebase.database.DataSnapshot)(snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot)` This method is triggered when a child is removed from the location to which this listener was added. |

## Public functions

### onCancelled

```
fun onCancelled(error: DatabaseError): Unit
```

This method will be triggered in the event that this listener either failed at the server, or is removed as a result of the security and Firebase rules. For more information on securing your data, see: [Security Quickstart](https://firebase.google.com/docs/database/security/quickstart)

| Parameters |
|---|---|
| `error: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError` | A description of the error that occurred |

### onChildAdded

```
fun onChildAdded(snapshot: DataSnapshot, previousChildName: String?): Unit
```

This method is triggered when a new child is added to the location to which this listener was added.

| Parameters |
|---|---|
| `snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot` | An immutable snapshot of the data at the new child location |
| `previousChildName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The key name of sibling location ordered before the new child. This will be null for the first child node of a location. |

### onChildChanged

```
fun onChildChanged(snapshot: DataSnapshot, previousChildName: String?): Unit
```

This method is triggered when the data at a child location has changed.

| Parameters |
|---|---|
| `snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot` | An immutable snapshot of the data at the new data at the child location |
| `previousChildName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The key name of sibling location ordered before the child. This will be null for the first child node of a location. |

### onChildMoved

```
fun onChildMoved(snapshot: DataSnapshot, previousChildName: String?): Unit
```

This method is triggered when a child location's priority changes. See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#setPriority(java.lang.Object)` and [Ordered Data](https://firebase.google.com/docs/database/android/retrieve-data#data_order) for more information on priorities and ordering data.

| Parameters |
|---|---|
| `snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot` | An immutable snapshot of the data at the location that moved. |
| `previousChildName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The key name of the sibling location ordered before the child location. This will be null if this location is ordered first. |

### onChildRemoved

```
fun onChildRemoved(snapshot: DataSnapshot): Unit
```

This method is triggered when a child is removed from the location to which this listener was added.

| Parameters |
|---|---|
| `snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot` | An immutable snapshot of the data at the child that was removed. |