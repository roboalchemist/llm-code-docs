# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.md.txt

# DatabaseReference

# DatabaseReference


```
public class DatabaseReference extends Query
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.database.Query](https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query) ||
|   | ↳ | [com.google.firebase.database.DatabaseReference](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference) |

*** ** * ** ***

A Firebase reference represents a particular location in your Database and can be used for reading or writing data to that Database location.

This class is the starting point for all Database operations. After you've initialized it with a URL, you can use it to read data, write data, and to create new DatabaseReferences.

## Summary

| ### Nested types |
|---|
| `public interface https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener` This interface is used as a method of being notified when an operation has been acknowledged by the Database servers and can be considered complete |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#child(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pathString)` Get a reference to location relative to this one |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html other)` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#getDatabase()()` Gets the Database instance associated with this reference. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#getKey()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#getParent()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#getRoot()()` |
| `static void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#goOffline()()` Manually disconnect the Firebase Database client from the server and disable automatic reconnection. |
| `static void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#goOnline()()` Manually reestablish a connection to the Firebase Database server and enable automatic reconnection. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#hashCode()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/OnDisconnect` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#onDisconnect()()` Provides access to disconnect operations at this location |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#push()()` Create a reference to an auto-generated child location. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#removeValue()()` Set the value at this location to 'null' |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#removeValue(com.google.firebase.database.DatabaseReference.CompletionListener)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener)` Set the value at this location to 'null' |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#runTransaction(com.google.firebase.database.Transaction.Handler)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction.Handler handler)` Run a transaction on the data at this location. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#runTransaction(com.google.firebase.database.Transaction.Handler,boolean)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction.Handler handler, boolean fireLocalEvents )` Run a transaction on the data at this location. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#setPriority(java.lang.Object)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html priority)` Set a priority for the data at this Database location. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#setPriority(java.lang.Object,com.google.firebase.database.DatabaseReference.CompletionListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html priority, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener )` Set a priority for the data at this Database location. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#setValue(java.lang.Object)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value)` Set the data at this location to the given value. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#setValue(java.lang.Object,com.google.firebase.database.DatabaseReference.CompletionListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener )` Set the data at this location to the given value. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#setValue(java.lang.Object,java.lang.Object)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html priority)` Set the data and priority to the given values. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#setValue(java.lang.Object,java.lang.Object,com.google.firebase.database.DatabaseReference.CompletionListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html priority, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener )` Set the data and priority to the given values. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#toString()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#updateChildren(java.util.Map<java.lang.String,java.lang.Object>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html> update)` Update the specific child keys to the specified values. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#updateChildren(java.util.Map<java.lang.String,java.lang.Object>,com.google.firebase.database.DatabaseReference.CompletionListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html> update, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener )` Update the specific child keys to the specified values. |

| ### Inherited methods |
|---|
| From [com.google.firebase.database.Query](https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query) |---|---| | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEventListener` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#addChildEventListener(com.google.firebase.database.ChildEventListener)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEventListener listener)` Add a listener for child events occurring at this location. | | `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#addListenerForSingleValueEvent(com.google.firebase.database.ValueEventListener)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/ValueEventListener listener)` Add a listener for a single change in the data at this location. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/ValueEventListener` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#addValueEventListener(com.google.firebase.database.ValueEventListener)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/ValueEventListener listener)` Add a listener for changes in the data at this location. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#endAt(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#endAt(double)(double value)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#endAt(boolean)(boolean value)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#endAt(java.lang.String,java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than or equal to the given key. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#endAt(double,java.lang.String)(double value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than or equal to the given key. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#endAt(boolean,java.lang.String)(boolean value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than or equal to the given key. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#endBefore(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Creates a query constrained to only return child nodes with a value less than the given value, using the given `orderBy` directive or priority as default. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#endBefore(double)(double value)` Creates a query constrained to only return child nodes with a value less than the given value, using the given `orderBy` directive or priority as default. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#endBefore(boolean)(boolean value)` Creates a query constrained to only return child nodes with a value less than the given value, using the given `orderBy` directive or priority as default. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#endBefore(java.lang.String,java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than the given key. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#endBefore(double,java.lang.String)(double value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than the given key. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#endBefore(boolean,java.lang.String)(boolean value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Creates a query constrained to only return child nodes with a value less than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key less than the given key. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#equalTo(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Creates a query constrained to only return child nodes with the given value. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#equalTo(double)(double value)` Creates a query constrained to only return child nodes with the given value. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#equalTo(boolean)(boolean value)` Creates a query constrained to only return child nodes with the given value. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#equalTo(java.lang.String,java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Creates a query constrained to only return the child node with the given key and value. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#equalTo(double,java.lang.String)(double value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Creates a query constrained to only return the child node with the given key and value. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#equalTo(boolean,java.lang.String)(boolean value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Creates a query constrained to only return the child node with the given key and value. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#get()()` Gets the server values for this query. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#getRef()()` | | `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#keepSynced(boolean)(boolean keepSynced)` By calling \`keepSynced(true)\` on a location, the data for that location will automatically be downloaded and kept in sync, even when no listeners are attached for that location. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#limitToFirst(int)(int limit)` Creates a query with limit and anchor it to the start of the window. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#limitToLast(int)(int limit)` Creates a query with limit and anchor it to the end of the window. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#orderByChild(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html path)` Creates a query in which child nodes are ordered by the values of the specified path. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#orderByKey()()` Creates a query in which child nodes are ordered by their keys. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#orderByPriority()()` Creates a query in which child nodes are ordered by their priorities. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#orderByValue()()` Creates a query in which nodes are ordered by their value | | `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#removeEventListener(com.google.firebase.database.ChildEventListener)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/ChildEventListener listener)` Remove the specified listener from this location. | | `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#removeEventListener(com.google.firebase.database.ValueEventListener)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/ValueEventListener listener)` Remove the specified listener from this location. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#startAfter(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Creates a query constrained to only return child nodes with a value greater than the given value, using the given `orderBy` directive or priority as default. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#startAfter(double)(double value)` Creates a query constrained to only return child nodes with a value greater than the given value, using the given `orderBy` directive or priority as default. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#startAfter(boolean)(boolean value)` Creates a query constrained to only return child nodes with a value greater than the given value, using the given `orderBy` directive or priority as default. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#startAfter(java.lang.String,java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Creates a query constrained to only return child nodes with a value greater or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than the given key. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#startAfter(double,java.lang.String)(double value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than the given key. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#startAfter(boolean,java.lang.String)(boolean value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than the given key. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#startAt(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#startAt(double)(double value)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#startAt(boolean)(boolean value)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#startAt(java.lang.String,java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#startAt(double,java.lang.String)(double value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#startAt(boolean,java.lang.String)(boolean value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Creates a query constrained to only return child nodes with a value greater than or equal to the given value, using the given `orderBy` directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key. | |

## Public methods

### child

```
public @NonNull DatabaseReference child(@NonNull String pathString)
```

Get a reference to location relative to this one

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pathString` | The relative path from this reference to the new one that should be created |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference` | A new DatabaseReference to the given path |

### equals

```
public boolean equals(Object other)
```

### getDatabase

```
public @NonNull FirebaseDatabase getDatabase()
```

Gets the Database instance associated with this reference.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` | The Database object for this reference. |

### getKey

```
public @Nullable String getKey()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | The last token in the location pointed to by this reference or null if this reference points to the database root |

### getParent

```
public @Nullable DatabaseReference getParent()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference` | A DatabaseReference to the parent location, or null if this instance references the root location |

### getRoot

```
public @NonNull DatabaseReference getRoot()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference` | A reference to the root location of this Firebase Database |

### goOffline

```
public static void goOffline()
```

Manually disconnect the Firebase Database client from the server and disable automatic reconnection.

Note: Invoking this method will impact all Firebase Database connections.

### goOnline

```
public static void goOnline()
```

Manually reestablish a connection to the Firebase Database server and enable automatic reconnection.

Note: Invoking this method will impact all Firebase Database connections.

### hashCode

```
public int hashCode()
```

### onDisconnect

```
public @NonNull OnDisconnect onDisconnect()
```

Provides access to disconnect operations at this location

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/OnDisconnect` | An object for managing disconnect operations at this location |

### push

```
public @NonNull DatabaseReference push()
```

Create a reference to an auto-generated child location. The child key is generated client-side and incorporates an estimate of the server's time for sorting purposes. Locations generated on a single client will be sorted in the order that they are created, and will be sorted approximately in order across all clients.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference` | A DatabaseReference pointing to the new location |

### removeValue

```
public @NonNull Task<Void> removeValue()
```

Set the value at this location to 'null'

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### removeValue

```
public void removeValue(@Nullable DatabaseReference.CompletionListener listener)
```

Set the value at this location to 'null'

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener` | A listener that will be triggered when the operation is complete |

### runTransaction

```
public void runTransaction(@NonNull Transaction.Handler handler)
```

Run a transaction on the data at this location. For more information on running transactions, see `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction.Handler`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction.Handler handler` | An object to handle running the transaction |

### runTransaction

```
public void runTransaction(
    @NonNull Transaction.Handler handler,
    boolean fireLocalEvents
)
```

Run a transaction on the data at this location. For more information on running transactions, see `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction.Handler`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction.Handler handler` | An object to handle running the transaction |
| `boolean fireLocalEvents` | Defaults to true. If set to false, events will only be fired for the final result state of the transaction, and not for any intermediate states |

### setPriority

```
public @NonNull Task<Void> setPriority(@Nullable Object priority)
```

Set a priority for the data at this Database location. Priorities can be used to provide a custom ordering for the children at a location (if no priorities are specified, the children are ordered by key). You cannot set a priority on an empty location. For this reason setValue(data, priority) should be used when setting initial data with a specific priority and setPriority should be used when updating the priority of existing data. Children are sorted based on this priority using the following rules:

- Children with no priority come first.
- Children with a number as their priority come next. They are sorted numerically by priority (small to large).
- Children with a string as their priority come last. They are sorted lexicographically by priority.
- Whenever two children have the same priority (including no priority), they are sorted by key. Numeric keys come first (sorted numerically), followed by the remaining keys (sorted lexicographically).

Note that numerical priorities are parsed and ordered as IEEE 754 double-precision floating-point numbers. Keys are always stored as strings and are treated as numeric only when they can be parsed as a 32-bit integer.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html priority` | The priority to set at the specified location or null to clear the existing priority |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### setPriority

```
public void setPriority(
    @Nullable Object priority,
    @Nullable DatabaseReference.CompletionListener listener
)
```

Set a priority for the data at this Database location. Priorities can be used to provide a custom ordering for the children at a location (if no priorities are specified, the children are ordered by key). You cannot set a priority on an empty location. For this reason setValue(data, priority) should be used when setting initial data with a specific priority and setPriority should be used when updating the priority of existing data. Children are sorted based on this priority using the following rules:

- Children with no priority come first.
- Children with a number as their priority come next. They are sorted numerically by priority (small to large).
- Children with a string as their priority come last. They are sorted lexicographically by priority.
- Whenever two children have the same priority (including no priority), they are sorted by key. Numeric keys come first (sorted numerically), followed by the remaining keys (sorted lexicographically).

Note that numerical priorities are parsed and ordered as IEEE 754 double-precision floating-point numbers. Keys are always stored as strings and are treated as numeric only when they can be parsed as a 32-bit integer.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html priority` | The priority to set at the specified location or null to clear the existing priority |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener` | A listener that will be triggered with results of the operation |

### setValue

```
public @NonNull Task<Void> setValue(@Nullable Object value)
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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The value to set at this location or null to delete the existing data |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### setValue

```
public void setValue(
    @Nullable Object value,
    @Nullable DatabaseReference.CompletionListener listener
)
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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The value to set at this location or null to delete the existing data |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener` | A listener that will be triggered with the results of the operation |

### setValue

```
public @NonNull Task<Void> setValue(@Nullable Object value, @Nullable Object priority)
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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The value to set at this location or null to delete the existing data |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html priority` | The priority to set at this location or null to clear the existing priority |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### setValue

```
public void setValue(
    @Nullable Object value,
    @Nullable Object priority,
    @Nullable DatabaseReference.CompletionListener listener
)
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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The value to set at this location or null to delete the existing data |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html priority` | The priority to set at this location or null to clear the existing priority |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener` | A listener that will be triggered with the results of the operation |

### toString

```
public String toString()
```

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | The full location url for this reference |

### updateChildren

```
public @NonNull Task<Void> updateChildren(@NonNull Map<String, Object> update)
```

Update the specific child keys to the specified values. Passing null in a map to updateChildren() will remove the value at the specified location.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html> update` | The paths to update and their new values |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### updateChildren

```
public void updateChildren(
    @NonNull Map<String, Object> update,
    @Nullable DatabaseReference.CompletionListener listener
)
```

Update the specific child keys to the specified values. Passing null in a map to updateChildren() will remove the value at the specified location.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html> update` | The paths to update and their new values |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener` | A listener that will be triggered with results of the operation |