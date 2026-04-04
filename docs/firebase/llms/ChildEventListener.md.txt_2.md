# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEventListener.md.txt

# ChildEventListener

# ChildEventListener


```
public interface ChildEventListener
```

<br />

*** ** * ** ***

Classes implementing this interface can be used to receive events about changes in the child locations of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference` ref. Attach the listener to a location using `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#addChildEventListener(com.google.firebase.database.ChildEventListener)` and the appropriate method will be triggered when changes occur.

## Summary

| ### Public methods |
|---|---|
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEventListener#onCancelled(com.google.firebase.database.DatabaseError)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError error)` This method will be triggered in the event that this listener either failed at the server, or is removed as a result of the security and Firebase rules. |
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEventListener#onChildAdded(com.google.firebase.database.DataSnapshot,java.lang.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html previousChildName )` This method is triggered when a new child is added to the location to which this listener was added. |
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEventListener#onChildChanged(com.google.firebase.database.DataSnapshot,java.lang.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html previousChildName )` This method is triggered when the data at a child location has changed. |
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEventListener#onChildMoved(com.google.firebase.database.DataSnapshot,java.lang.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html previousChildName )` This method is triggered when a child location's priority changes. |
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEventListener#onChildRemoved(com.google.firebase.database.DataSnapshot)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot)` This method is triggered when a child is removed from the location to which this listener was added. |

## Public methods

### onCancelled

```
abstract void onCancelled(@NonNull DatabaseError error)
```

This method will be triggered in the event that this listener either failed at the server, or is removed as a result of the security and Firebase rules. For more information on securing your data, see: [Security Quickstart](https://firebase.google.com/docs/database/security/quickstart)

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError error` | A description of the error that occurred |

### onChildAdded

```
abstract void onChildAdded(
    @NonNull DataSnapshot snapshot,
    @Nullable String previousChildName
)
```

This method is triggered when a new child is added to the location to which this listener was added.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot` | An immutable snapshot of the data at the new child location |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html previousChildName` | The key name of sibling location ordered before the new child. This will be null for the first child node of a location. |

### onChildChanged

```
abstract void onChildChanged(
    @NonNull DataSnapshot snapshot,
    @Nullable String previousChildName
)
```

This method is triggered when the data at a child location has changed.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot` | An immutable snapshot of the data at the new data at the child location |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html previousChildName` | The key name of sibling location ordered before the child. This will be null for the first child node of a location. |

### onChildMoved

```
abstract void onChildMoved(
    @NonNull DataSnapshot snapshot,
    @Nullable String previousChildName
)
```

This method is triggered when a child location's priority changes. See `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#setPriority(java.lang.Object)` and [Ordered Data](https://firebase.google.com/docs/database/android/retrieve-data#data_order) for more information on priorities and ordering data.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot` | An immutable snapshot of the data at the location that moved. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html previousChildName` | The key name of the sibling location ordered before the child location. This will be null if this location is ordered first. |

### onChildRemoved

```
abstract void onChildRemoved(@NonNull DataSnapshot snapshot)
```

This method is triggered when a child is removed from the location to which this listener was added.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot` | An immutable snapshot of the data at the child that was removed. |