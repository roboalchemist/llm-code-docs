# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.md.txt

# DatabaseReference

# DatabaseReference


```
class DatabaseReference : Query
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.database.Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) ||
|   | ↳ | [com.google.firebase.database.DatabaseReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference) |

*** ** * ** ***

A Firebase reference represents a particular location in your Database and can be used for reading or writing data to that Database location.

This class is the starting point for all Database operations. After you've initialized it with a URL, you can use it to read data, write data, and to create new DatabaseReferences.

## Summary

| ### Nested types |
|---|
| `interface https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener` This interface is used as a method of being notified when an operation has been acknowledged by the Database servers and can be considered complete |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#child(java.lang.String)(pathString: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Get a reference to location relative to this one |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#equals(java.lang.Object)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#getDatabase()()` Gets the Database instance associated with this reference. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#getKey()()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#getParent()()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#getRoot()()` |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#goOffline()()` Manually disconnect the Firebase Database client from the server and disable automatic reconnection. |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#goOnline()()` Manually reestablish a connection to the Firebase Database server and enable automatic reconnection. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#hashCode()()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#onDisconnect()()` Provides access to disconnect operations at this location |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#push()()` Create a reference to an auto-generated child location. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#removeValue()()` Set the value at this location to 'null' |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#removeValue(com.google.firebase.database.DatabaseReference.CompletionListener)(listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener?)` Set the value at this location to 'null' |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#runTransaction(com.google.firebase.database.Transaction.Handler)(handler: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Handler)` Run a transaction on the data at this location. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#runTransaction(com.google.firebase.database.Transaction.Handler,boolean)(handler: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Handler, fireLocalEvents: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Run a transaction on the data at this location. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#setPriority(java.lang.Object)(priority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Set a priority for the data at this Database location. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#setPriority(java.lang.Object,com.google.firebase.database.DatabaseReference.CompletionListener)( priority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener? )` Set a priority for the data at this Database location. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#setValue(java.lang.Object)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Set the data at this location to the given value. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#setValue(java.lang.Object,com.google.firebase.database.DatabaseReference.CompletionListener)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener?)` Set the data at this location to the given value. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#setValue(java.lang.Object,java.lang.Object)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?, priority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Set the data and priority to the given values. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#setValue(java.lang.Object,java.lang.Object,com.google.firebase.database.DatabaseReference.CompletionListener)( value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?, priority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener? )` Set the data and priority to the given values. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#toString()()` |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#updateChildren(java.util.Map<java.lang.String,java.lang.Object>)(update: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Update the specific child keys to the specified values. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#updateChildren(java.util.Map<java.lang.String,java.lang.Object>,com.google.firebase.database.DatabaseReference.CompletionListener)( update: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener? )` Update the specific child keys to the specified values. |

| ### Inherited functions |
|---|
| From [com.google.firebase.database.Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEventListener` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#addChildEventListener(com.google.firebase.database.ChildEventListener)(listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEventListener)` Add a listener for child events occurring at this location. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#addListenerForSingleValueEvent(com.google.firebase.database.ValueEventListener)(listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ValueEventListener)` Add a listener for a single change in the data at this location. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ValueEventListener` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#addValueEventListener(com.google.firebase.database.ValueEventListener)(listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ValueEventListener)` Add a listener for changes in the data at this location. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endAt(java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endAt(double)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endAt(boolean)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endAt(java.lang.String,java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than or equal to the given key. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endAt(double,java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html, key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than or equal to the given key. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endAt(boolean,java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than or equal to the given key. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endBefore(java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return child nodes with a value less than the given value, using the given `orderBy` directive or priority as default. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endBefore(double)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Creates a query constrained to only return child nodes with a value less than the given value, using the given `orderBy` directive or priority as default. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endBefore(boolean)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Creates a query constrained to only return child nodes with a value less than the given value, using the given `orderBy` directive or priority as default. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endBefore(java.lang.String,java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than the given key. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endBefore(double,java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html, key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than the given key. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#endBefore(boolean,java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than the given key. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#equalTo(java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return child nodes with the given value. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#equalTo(double)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Creates a query constrained to only return child nodes with the given value. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#equalTo(boolean)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Creates a query constrained to only return child nodes with the given value. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#equalTo(java.lang.String,java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return the child node with the given key and value. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#equalTo(double,java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html, key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return the child node with the given key and value. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#equalTo(boolean,java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return the child node with the given key and value. | | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#get()()` Gets the server values for this query. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#getRef()()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#keepSynced(boolean)(keepSynced: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` By calling \`keepSynced(true)\` on a location, the data for that location will automatically be downloaded and kept in sync, even when no listeners are attached for that location. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#limitToFirst(int)(limit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates a query with limit and anchor it to the start of the window. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#limitToLast(int)(limit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates a query with limit and anchor it to the end of the window. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#orderByChild(java.lang.String)(path: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates a query in which child nodes are ordered by the values of the specified path. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#orderByKey()()` Creates a query in which child nodes are ordered by their keys. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#orderByPriority()()` Creates a query in which child nodes are ordered by their priorities. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#orderByValue()()` Creates a query in which nodes are ordered by their value | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#removeEventListener(com.google.firebase.database.ChildEventListener)(listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ChildEventListener)` Remove the specified listener from this location. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#removeEventListener(com.google.firebase.database.ValueEventListener)(listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ValueEventListener)` Remove the specified listener from this location. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAfter(java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return child nodes with a value greater than the given value, using the given `orderBy` directive or priority as default. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAfter(double)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Creates a query constrained to only return child nodes with a value greater than the given value, using the given `orderBy` directive or priority as default. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAfter(boolean)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Creates a query constrained to only return child nodes with a value greater than the given value, using the given `orderBy` directive or priority as default. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAfter(java.lang.String,java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return child nodes with a value greater or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than the given key. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAfter(double,java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html, key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than the given key. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAfter(boolean,java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than the given key. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAt(java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAt(double)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAt(boolean)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAt(java.lang.String,java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAt(double,java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html, key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#startAt(boolean,java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key. | |

## Public functions

### child

```
fun child(pathString: String): DatabaseReference
```

Get a reference to location relative to this one

| Parameters |
|---|---|
| `pathString: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The relative path from this reference to the new one that should be created |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference` | A new DatabaseReference to the given path |

### equals

```
fun equals(other: Any!): Boolean
```

### getDatabase

```
fun getDatabase(): FirebaseDatabase
```

Gets the Database instance associated with this reference.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase` | The Database object for this reference. |

### getKey

```
fun getKey(): String?
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The last token in the location pointed to by this reference or null if this reference points to the database root |

### getParent

```
fun getParent(): DatabaseReference?
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference?` | A DatabaseReference to the parent location, or null if this instance references the root location |

### getRoot

```
fun getRoot(): DatabaseReference
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference` | A reference to the root location of this Firebase Database |

### goOffline

```
java-static fun goOffline(): Unit
```

Manually disconnect the Firebase Database client from the server and disable automatic reconnection.

Note: Invoking this method will impact all Firebase Database connections.

### goOnline

```
java-static fun goOnline(): Unit
```

Manually reestablish a connection to the Firebase Database server and enable automatic reconnection.

Note: Invoking this method will impact all Firebase Database connections.

### hashCode

```
fun hashCode(): Int
```

### onDisconnect

```
fun onDisconnect(): OnDisconnect
```

Provides access to disconnect operations at this location

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect` | An object for managing disconnect operations at this location |

### push

```
fun push(): DatabaseReference
```

Create a reference to an auto-generated child location. The child key is generated client-side and incorporates an estimate of the server's time for sorting purposes. Locations generated on a single client will be sorted in the order that they are created, and will be sorted approximately in order across all clients.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference` | A DatabaseReference pointing to the new location |

### removeValue

```
fun removeValue(): Task<Void!>
```

Set the value at this location to 'null'

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### removeValue

```
fun removeValue(listener: DatabaseReference.CompletionListener?): Unit
```

Set the value at this location to 'null'

| Parameters |
|---|---|
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener?` | A listener that will be triggered when the operation is complete |

### runTransaction

```
fun runTransaction(handler: Transaction.Handler): Unit
```

Run a transaction on the data at this location. For more information on running transactions, see `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Handler`.

| Parameters |
|---|---|
| `handler: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Handler` | An object to handle running the transaction |

### runTransaction

```
fun runTransaction(handler: Transaction.Handler, fireLocalEvents: Boolean): Unit
```

Run a transaction on the data at this location. For more information on running transactions, see `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Handler`.

| Parameters |
|---|---|
| `handler: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Handler` | An object to handle running the transaction |
| `fireLocalEvents: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | Defaults to true. If set to false, events will only be fired for the final result state of the transaction, and not for any intermediate states |

### setPriority

```
fun setPriority(priority: Any?): Task<Void!>
```

Set a priority for the data at this Database location. Priorities can be used to provide a custom ordering for the children at a location (if no priorities are specified, the children are ordered by key). You cannot set a priority on an empty location. For this reason setValue(data, priority) should be used when setting initial data with a specific priority and setPriority should be used when updating the priority of existing data. Children are sorted based on this priority using the following rules:

- Children with no priority come first.
- Children with a number as their priority come next. They are sorted numerically by priority (small to large).
- Children with a string as their priority come last. They are sorted lexicographically by priority.
- Whenever two children have the same priority (including no priority), they are sorted by key. Numeric keys come first (sorted numerically), followed by the remaining keys (sorted lexicographically).

Note that numerical priorities are parsed and ordered as IEEE 754 double-precision floating-point numbers. Keys are always stored as strings and are treated as numeric only when they can be parsed as a 32-bit integer.

| Parameters |
|---|---|
| `priority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The priority to set at the specified location or null to clear the existing priority |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### setPriority

```
fun setPriority(
    priority: Any?,
    listener: DatabaseReference.CompletionListener?
): Unit
```

Set a priority for the data at this Database location. Priorities can be used to provide a custom ordering for the children at a location (if no priorities are specified, the children are ordered by key). You cannot set a priority on an empty location. For this reason setValue(data, priority) should be used when setting initial data with a specific priority and setPriority should be used when updating the priority of existing data. Children are sorted based on this priority using the following rules:

- Children with no priority come first.
- Children with a number as their priority come next. They are sorted numerically by priority (small to large).
- Children with a string as their priority come last. They are sorted lexicographically by priority.
- Whenever two children have the same priority (including no priority), they are sorted by key. Numeric keys come first (sorted numerically), followed by the remaining keys (sorted lexicographically).

Note that numerical priorities are parsed and ordered as IEEE 754 double-precision floating-point numbers. Keys are always stored as strings and are treated as numeric only when they can be parsed as a 32-bit integer.

| Parameters |
|---|---|
| `priority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The priority to set at the specified location or null to clear the existing priority |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener?` | A listener that will be triggered with results of the operation |

### setValue

```
fun setValue(value: Any?): Task<Void!>
```

Set the data at this location to the given value. Passing null to setValue() will delete the data at the specified location. The native types accepted by this method for the value correspond to the JSON types:

- `Boolean`
- `Long`
- `Double`
- `String`
- `Map<String, Object>`
- `List<Object>`

In addition, you can set instances of your own class into this location, provided they satisfy the following constraints:

1. The class must have a default constructor that takes no arguments
2. The class must define public getters for the properties to be assigned. Properties without a public getter will be set to their default value when an instance is deserialized

Generic collections of objects that satisfy the above constraints are also permitted, i.e. `Map<String, MyPOJO>`, as well as null values.

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value to set at this location or null to delete the existing data |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### setValue

```
fun setValue(value: Any?, listener: DatabaseReference.CompletionListener?): Unit
```

Set the data at this location to the given value. Passing null to setValue() will delete the data at the specified location. The native types accepted by this method for the value correspond to the JSON types:

- `Boolean`
- `Long`
- `Double`
- `String`
- `Map<String, Object>`
- `List<Object>`

In addition, you can set instances of your own class into this location, provided they satisfy the following constraints:

1. The class must have a default constructor that takes no arguments
2. The class must define public getters for the properties to be assigned. Properties without a public getter will be set to their default value when an instance is deserialized

Generic collections of objects that satisfy the above constraints are also permitted, i.e. `Map<String, MyPOJO>`, as well as null values.

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value to set at this location or null to delete the existing data |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener?` | A listener that will be triggered with the results of the operation |

### setValue

```
fun setValue(value: Any?, priority: Any?): Task<Void!>
```

Set the data and priority to the given values. Passing null to setValue() will delete the data at the specified location. The native types accepted by this method for the value correspond to the JSON types:

- `Boolean`
- `Long`
- `Double`
- `String`
- `Map<String, Object>`
- `List<Object>`

In addition, you can set instances of your own class into this location, provided they satisfy the following constraints:

1. The class must have a default constructor that takes no arguments
2. The class must define public getters for the properties to be assigned. Properties without a public getter will be set to their default value when an instance is deserialized

Generic collections of objects that satisfy the above constraints are also permitted, i.e. `Map<String, MyPOJO>`, as well as null values.

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value to set at this location or null to delete the existing data |
| `priority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The priority to set at this location or null to clear the existing priority |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### setValue

```
fun setValue(
    value: Any?,
    priority: Any?,
    listener: DatabaseReference.CompletionListener?
): Unit
```

Set the data and priority to the given values. The native types accepted by this method for the value correspond to the JSON types:

- `Boolean`
- `Long`
- `Double`
- `String`
- `Map<String, Object>`
- `List<Object>`

In addition, you can set instances of your own class into this location, provided they satisfy the following constraints:

1. The class must have a default constructor that takes no arguments
2. The class must define public getters for the properties to be assigned. Properties without a public getter will be set to their default value when an instance is deserialized

Generic collections of objects that satisfy the above constraints are also permitted, i.e. `Map<String, MyPOJO>`, as well as null values.

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value to set at this location or null to delete the existing data |
| `priority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The priority to set at this location or null to clear the existing priority |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener?` | A listener that will be triggered with the results of the operation |

### toString

```
fun toString(): String!
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | The full location url for this reference |

### updateChildren

```
fun updateChildren(update: (Mutable)Map<String!, Any!>): Task<Void!>
```

Update the specific child keys to the specified values. Passing null in a map to updateChildren() will remove the value at the specified location.

| Parameters |
|---|---|
| `update: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>` | The paths to update and their new values |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### updateChildren

```
fun updateChildren(
    update: (Mutable)Map<String!, Any!>,
    listener: DatabaseReference.CompletionListener?
): Unit
```

Update the specific child keys to the specified values. Passing null in a map to updateChildren() will remove the value at the specified location.

| Parameters |
|---|---|
| `update: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>` | The paths to update and their new values |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener?` | A listener that will be triggered with results of the operation |