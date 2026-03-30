# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.md.txt

# DatabaseReference

public class **DatabaseReference** extends [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query)  
A Firebase reference represents a particular location in your Database and can be used for
reading or writing data to that Database location.

This class is the starting point for all Database operations. After you've initialized it with
a URL, you can use it to read data, write data, and to create new DatabaseReferences.

### Nested Class Summary

|---|---|---|---|
| interface | [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) || This interface is used as a method of being notified when an operation has been acknowledged by the Database servers and can be considered complete |

### Public Method Summary

|---|---|
| [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference) | [child](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#child(java.lang.String))(String pathString) Get a reference to location relative to this one |
| boolean | [equals](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#equals(java.lang.Object))(Object other) |
| [FirebaseDatabase](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase) | [getDatabase](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#getDatabase())() Gets the Database instance associated with this reference. |
| String | [getKey](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#getKey())() |
| [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference) | [getParent](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#getParent())() |
| [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference) | [getRoot](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#getRoot())() |
| static void | [goOffline](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#goOffline())() Manually disconnect the Firebase Database client from the server and disable automatic reconnection. |
| static void | [goOnline](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#goOnline())() Manually reestablish a connection to the Firebase Database server and enable automatic reconnection. |
| int | [hashCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#hashCode())() |
| [OnDisconnect](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/OnDisconnect) | [onDisconnect](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#onDisconnect())() Provides access to disconnect operations at this location |
| [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference) | [push](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#push())() Create a reference to an auto-generated child location. |
| void | [removeValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#removeValue(com.google.firebase.database.DatabaseReference.CompletionListener))([DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener) Set the value at this location to 'null' |
| ApiFuture\<Void\> | [removeValueAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#removeValueAsync())() Set the value at this location to 'null' |
| void | [runTransaction](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#runTransaction(com.google.firebase.database.Transaction.Handler, boolean))([Transaction.Handler](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Handler) handler, boolean fireLocalEvents) Run a transaction on the data at this location. |
| void | [runTransaction](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#runTransaction(com.google.firebase.database.Transaction.Handler))([Transaction.Handler](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Handler) handler) Run a transaction on the data at this location. |
| void | [setPriority](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#setPriority(java.lang.Object, com.google.firebase.database.DatabaseReference.CompletionListener))(Object priority, [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener) Set a priority for the data at this Database location. |
| ApiFuture\<Void\> | [setPriorityAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#setPriorityAsync(java.lang.Object))(Object priority) Set a priority for the data at this Database location. |
| void | [setValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#setValue(java.lang.Object, java.lang.Object, com.google.firebase.database.DatabaseReference.CompletionListener))(Object value, Object priority, [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener) Set the data and priority to the given values. |
| void | [setValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#setValue(java.lang.Object, com.google.firebase.database.DatabaseReference.CompletionListener))(Object value, [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener) Set the data at this location to the given value. |
| ApiFuture\<Void\> | [setValueAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#setValueAsync(java.lang.Object, java.lang.Object))(Object value, Object priority) Set the data and priority to the given values. |
| ApiFuture\<Void\> | [setValueAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#setValueAsync(java.lang.Object))(Object value) Set the data at this location to the given value. |
| String | [toString](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#toString())() |
| void | [updateChildren](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#updateChildren(java.util.Map<java.lang.String, java.lang.Object>, com.google.firebase.database.DatabaseReference.CompletionListener))(Map\<String, Object\> update, [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener) Update the specific child keys to the specified values. |
| ApiFuture\<Void\> | [updateChildrenAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#updateChildrenAsync(java.util.Map<java.lang.String, java.lang.Object>))(Map\<String, Object\> update) Update the specific child keys to the specified values. |

### Inherited Method Summary

From class [com.google.firebase.database.Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query)

|---|---|
| [ChildEventListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ChildEventListener) | [addChildEventListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#addChildEventListener(com.google.firebase.database.ChildEventListener))([ChildEventListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ChildEventListener) listener) Add a listener for child events occurring at this location. |
| void | [addListenerForSingleValueEvent](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#addListenerForSingleValueEvent(com.google.firebase.database.ValueEventListener))([ValueEventListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ValueEventListener) listener) Add a listener for a single change in the data at this location. |
| [ValueEventListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ValueEventListener) | [addValueEventListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#addValueEventListener(com.google.firebase.database.ValueEventListener))([ValueEventListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ValueEventListener) listener) Add a listener for changes in the data at this location. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [endAt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#endAt(java.lang.String, java.lang.String))(String value, String key) Create a query constrained to only return child nodes with a value less than or equal to the given value, using the given orderBy directive or priority as default, and additionally only child nodes with a key key less than or equal to the given key. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [endAt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#endAt(java.lang.String))(String value) Create a query constrained to only return child nodes with a value less than or equal to the given value, using the given orderBy directive or priority as default. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [endAt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#endAt(double, java.lang.String))(double value, String key) Create a query constrained to only return child nodes with a value less than or equal to the given value, using the given orderBy directive or priority as default, and additionally only child nodes with a key less than or equal to the given key. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [endAt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#endAt(double))(double value) Create a query constrained to only return child nodes with a value less than or equal to the given value, using the given orderBy directive or priority as default. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [endAt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#endAt(boolean))(boolean value) Create a query constrained to only return child nodes with a value less than or equal to the given value, using the given orderBy directive or priority as default. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [endAt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#endAt(boolean, java.lang.String))(boolean value, String key) Create a query constrained to only return child nodes with a value less than or equal to the given value, using the given orderBy directive or priority as default, and additionally only child nodes with a key less than or equal to the given key. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [equalTo](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#equalTo(java.lang.String, java.lang.String))(String value, String key) Create a query constrained to only return the child node with the given key and value. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [equalTo](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#equalTo(double))(double value) Create a query constrained to only return child nodes with the given value. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [equalTo](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#equalTo(double, java.lang.String))(double value, String key) Create a query constrained to only return the child node with the given key and value. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [equalTo](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#equalTo(java.lang.String))(String value) Create a query constrained to only return child nodes with the given value. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [equalTo](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#equalTo(boolean, java.lang.String))(boolean value, String key) Create a query constrained to only return the child node with the given key and value. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [equalTo](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#equalTo(boolean))(boolean value) Create a query constrained to only return child nodes with the given value. |
| [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference) | [getRef](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#getRef())() |
| void | [keepSynced](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#keepSynced(boolean))(boolean keepSynced) By calling `keepSynced(true)` on a location, the data for that location will automatically be downloaded and kept in sync, even when no listeners are attached for that location. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [limitToFirst](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#limitToFirst(int))(int limit) Create a query with limit and anchor it to the start of the window. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [limitToLast](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#limitToLast(int))(int limit) Create a query with limit and anchor it to the end of the window. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [orderByChild](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#orderByChild(java.lang.String))(String path) Create a query in which child nodes are ordered by the values of the specified path. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [orderByKey](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#orderByKey())() Create a query in which child nodes are ordered by their keys. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [orderByPriority](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#orderByPriority())() Create a query in which child nodes are ordered by their priorities. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [orderByValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#orderByValue())() Create a query in which nodes are ordered by their value |
| void | [removeEventListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#removeEventListener(com.google.firebase.database.ChildEventListener))([ChildEventListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ChildEventListener) listener) Remove the specified listener from this location. |
| void | [removeEventListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#removeEventListener(com.google.firebase.database.ValueEventListener))([ValueEventListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ValueEventListener) listener) Remove the specified listener from this location. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [startAt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#startAt(double))(double value) Create a query constrained to only return child nodes with a value greater than or equal to the given value, using the given orderBy directive or priority as default. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [startAt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#startAt(java.lang.String, java.lang.String))(String value, String key) Create a query constrained to only return child nodes with a value greater than or equal to the given value, using the given orderBy directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [startAt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#startAt(java.lang.String))(String value) Create a query constrained to only return child nodes with a value greater than or equal to the given value, using the given orderBy directive or priority as default. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [startAt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#startAt(double, java.lang.String))(double value, String key) Create a query constrained to only return child nodes with a value greater than or equal to the given value, using the given orderBy directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [startAt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#startAt(boolean))(boolean value) Create a query constrained to only return child nodes with a value greater than or equal to the given value, using the given orderBy directive or priority as default. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | [startAt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#startAt(boolean, java.lang.String))(boolean value, String key) Create a query constrained to only return child nodes with a value greater than or equal to the given value, using the given orderBy directive or priority as default, and additionally only child nodes with a key greater than or equal to the given key. |

From class java.lang.Object

|---|---|
| Object | clone() |
| boolean | equals(Object arg0) |
| void | finalize() |
| final Class\<?\> | getClass() |
| int | hashCode() |
| final void | notify() |
| final void | notifyAll() |
| String | toString() |
| final void | wait(long arg0, int arg1) |
| final void | wait(long arg0) |
| final void | wait() |

## Public Methods

#### public [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference)
**child**
(String pathString)

Get a reference to location relative to this one

##### Parameters

| pathString | The relative path from this reference to the new one that should be created |
|---|---|

##### Returns

- A new DatabaseReference to the given path

#### public boolean
**equals**
(Object other)

<br />

#### public [FirebaseDatabase](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase)
**getDatabase**
()

Gets the Database instance associated with this reference.

##### Returns

- The Database object for this reference.

#### public String
**getKey**
()

<br />

##### Returns

- The last token in the location pointed to by this reference

#### public [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference)
**getParent**
()

<br />

##### Returns

- A DatabaseReference to the parent location, or null if this instance references the root location

#### public [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference)
**getRoot**
()

<br />

##### Returns

- A reference to the root location of this Firebase Database

#### public static void
**goOffline**
()

Manually disconnect the Firebase Database client from the server and disable automatic
reconnection.

Note: Invoking this method will impact all Firebase Database connections.

#### public static void
**goOnline**
()

Manually reestablish a connection to the Firebase Database server and enable automatic
reconnection.

Note: Invoking this method will impact all Firebase Database connections.

#### public int
**hashCode**
()

<br />

#### public [OnDisconnect](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/OnDisconnect)
**onDisconnect**
()

Provides access to disconnect operations at this location

##### Returns

- An object for managing disconnect operations at this location

#### public [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference)
**push**
()

Create a reference to an auto-generated child location. The child key is generated client-side
and incorporates an estimate of the server's time for sorting purposes. Locations generated on
a single client will be sorted in the order that they are created, and will be sorted
approximately in order across all clients.

##### Returns

- A DatabaseReference pointing to the new location

#### public void
**removeValue**
([DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener)

Set the value at this location to 'null'

##### Parameters

| listener | A listener that will be triggered when the operation is complete |
|---|---|

#### public ApiFuture\<Void\>
**removeValueAsync**
()

Set the value at this location to 'null'

##### Returns

- The ApiFuture for this operation.

#### public void
**runTransaction**
([Transaction.Handler](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Handler) handler, boolean fireLocalEvents)

Run a transaction on the data at this location. For more information on running transactions,
see `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Handler`.

##### Parameters

| handler | An object to handle running the transaction |
| fireLocalEvents | Defaults to true. If set to false, events will only be fired for the final result state of the transaction, and not for any intermediate states |
|---|---|

#### public void
**runTransaction**
([Transaction.Handler](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Handler) handler)

Run a transaction on the data at this location. For more information on running transactions,
see `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Handler`.

##### Parameters

| handler | An object to handle running the transaction |
|---|---|

#### public void
**setPriority**
(Object priority, [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener)

Set a priority for the data at this Database location. Priorities can be used to provide a
custom ordering for the children at a location (if no priorities are specified, the children
are ordered by key).   

<br />


You cannot set a priority on an empty location. For this reason setValue(data, priority) should
be used when setting initial data with a specific priority and setPriority should be used when
updating the priority of existing data.   

<br />


Children are sorted based on this priority using the following rules:

- Children with no priority come first.
- Children with a number as their priority come next. They are sorted numerically by priority (small to large).
- Children with a string as their priority come last. They are sorted lexicographically by priority.
- Whenever two children have the same priority (including no priority), they are sorted by key. Numeric keys come first (sorted numerically), followed by the remaining keys (sorted lexicographically).

Note that numerical priorities are parsed and ordered as IEEE 754 double-precision
floating-point numbers. Keys are always stored as strings and are treated as numeric only when
they can be parsed as a 32-bit integer.

##### Parameters

| priority | The priority to set at the specified location. |
| listener | A listener that will be triggered with results of the operation |
|---|---|

#### public ApiFuture\<Void\>
**setPriorityAsync**
(Object priority)

Set a priority for the data at this Database location. Priorities can be used to provide a
custom ordering for the children at a location (if no priorities are specified, the children
are ordered by key).   

<br />


You cannot set a priority on an empty location. For this reason setValue(data, priority) should
be used when setting initial data with a specific priority and setPriority should be used when
updating the priority of existing data.   

<br />


Children are sorted based on this priority using the following rules:

- Children with no priority come first.
- Children with a number as their priority come next. They are sorted numerically by priority (small to large).
- Children with a string as their priority come last. They are sorted lexicographically by priority.
- Whenever two children have the same priority (including no priority), they are sorted by key. Numeric keys come first (sorted numerically), followed by the remaining keys (sorted lexicographically).

Note that numerical priorities are parsed and ordered as IEEE 754 double-precision
floating-point numbers. Keys are always stored as strings and are treated as numeric only when
they can be parsed as a 32-bit integer.

##### Parameters

| priority | The priority to set at the specified location. |
|---|---|

##### Returns

- The ApiFuture for this operation.

#### public void
**setValue**
(Object value, Object priority, [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener)

Set the data and priority to the given values. The native types accepted by this method for the
value correspond to the JSON types:

- Boolean
- Long
- Double
- Map\<String, Object\>
- List\<Object\>

<br />

<br />

In addition, you can set instances of your own class into this location, provided they satisfy the following constraints:

1. The class must have a default constructor that takes no arguments
2. The class must define public getters for the properties to be assigned. Properties without a public getter will be set to their default value when an instance is deserialized

<br />

<br />

Generic collections of objects that satisfy the above constraints are also permitted, i.e. `Map<String, MyPOJO>`, as well as null values.

<br />

##### Parameters

| value | The value to set at this location |
| priority | The priority to set at this location |
| listener | A listener that will be triggered with the results of the operation |
|---|---|

#### public void
**setValue**
(Object value, [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener)

Set the data at this location to the given value. Passing null to setValue() will delete the
data at the specified location. The native types accepted by this method for the value
correspond to the JSON types:

- Boolean
- Long
- Double
- Map\<String, Object\>
- List\<Object\>

<br />

<br />

In addition, you can set instances of your own class into this location, provided they satisfy the following constraints:

1. The class must have a default constructor that takes no arguments
2. The class must define public getters for the properties to be assigned. Properties without a public getter will be set to their default value when an instance is deserialized

<br />

<br />

Generic collections of objects that satisfy the above constraints are also permitted, i.e. `Map<String, MyPOJO>`, as well as null values.

<br />

##### Parameters

| value | The value to set at this location |
| listener | A listener that will be triggered with the results of the operation |
|---|---|

#### public ApiFuture\<Void\>
**setValueAsync**
(Object value, Object priority)

Set the data and priority to the given values. Passing null to setValue() will delete the data
at the specified location. The native types accepted by this method for the value correspond to
the JSON types:

- Boolean
- Long
- Double
- Map\<String, Object\>
- List\<Object\>

<br />

<br />

In addition, you can set instances of your own class into this location, provided they satisfy the following constraints:

1. The class must have a default constructor that takes no arguments
2. The class must define public getters for the properties to be assigned. Properties without a public getter will be set to their default value when an instance is deserialized

<br />

<br />

Generic collections of objects that satisfy the above constraints are also permitted, i.e. `Map<String, MyPOJO>`, as well as null values.

<br />

##### Parameters

| value | The value to set at this location |
| priority | The priority to set at this location |
|---|---|

##### Returns

- The ApiFuture for this operation.

#### public ApiFuture\<Void\>
**setValueAsync**
(Object value)

Set the data at this location to the given value. Passing null to setValue() will delete the
data at the specified location. The native types accepted by this method for the value
correspond to the JSON types:

- Boolean
- Long
- Double
- Map\<String, Object\>
- List\<Object\>

<br />

<br />

In addition, you can set instances of your own class into this location, provided they satisfy the following constraints:

1. The class must have a default constructor that takes no arguments
2. The class must define public getters for the properties to be assigned. Properties without a public getter will be set to their default value when an instance is deserialized

<br />

<br />

Generic collections of objects that satisfy the above constraints are also permitted, i.e. `Map<String, MyPOJO>`, as well as null values.

<br />

##### Parameters

| value | The value to set at this location |
|---|---|

##### Returns

- The ApiFuture for this operation.

#### public String
**toString**
()

<br />

##### Returns

- The full location url for this reference

#### public void
**updateChildren**
(Map\<String, Object\> update, [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener)

Update the specific child keys to the specified values. Passing null in a map to
updateChildren() will remove the value at the specified location.

##### Parameters

| update | The paths to update and their new values |
| listener | A listener that will be triggered with results of the operation |
|---|---|

#### public ApiFuture\<Void\>
**updateChildrenAsync**
(Map\<String, Object\> update)

Update the specific child keys to the specified values. Passing null in a map to
updateChildren() will remove the value at the specified location.

##### Parameters

| update | The paths to update and their new values |
|---|---|

##### Returns

- The ApiFuture for this operation.