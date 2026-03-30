# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ValueEventListener.md.txt

# ValueEventListener

# ValueEventListener


```
interface ValueEventListener
```

<br />

*** ** * ** ***

Classes implementing this interface can be used to receive events about data changes at a location. Attach the listener to a location user `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#addValueEventListener(com.google.firebase.database.ValueEventListener)`.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ValueEventListener#onCancelled(com.google.firebase.database.DatabaseError)(error: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError)` This method will be triggered in the event that this listener either failed at the server, or is removed as a result of the security and Firebase Database rules. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ValueEventListener#onDataChange(com.google.firebase.database.DataSnapshot)(snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot)` This method will be called with a snapshot of the data at this location. |

## Public functions

### onCancelled

```
fun onCancelled(error: DatabaseError): Unit
```

This method will be triggered in the event that this listener either failed at the server, or is removed as a result of the security and Firebase Database rules. For more information on securing your data, see: [Security Quickstart](https://firebase.google.com/docs/database/security/quickstart)

| Parameters |
|---|---|
| `error: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError` | A description of the error that occurred |

### onDataChange

```
fun onDataChange(snapshot: DataSnapshot): Unit
```

This method will be called with a snapshot of the data at this location. It will also be called each time that data changes.

| Parameters |
|---|---|
| `snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot` | The current data at the location |