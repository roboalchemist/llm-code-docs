# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/OnDisconnect.md.txt

# OnDisconnect

public class **OnDisconnect** extends Object  
The OnDisconnect class is used to manage operations that will be run on the server when this
client disconnects. It can be used to add or remove data based on a client's connection status.
It is very useful in applications looking for 'presence' functionality.   

<br />


Instances of this class are obtained by calling `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#onDisconnect()` on a Firebase Database ref.

### Public Method Summary

|---|---|
| void | [cancel](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/OnDisconnect#cancel(com.google.firebase.database.DatabaseReference.CompletionListener))([DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener) Cancel any disconnect operations that are queued up at this location |
| ApiFuture\<Void\> | [cancelAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/OnDisconnect#cancelAsync())() Cancel any disconnect operations that are queued up at this location |
| void | [removeValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/OnDisconnect#removeValue(com.google.firebase.database.DatabaseReference.CompletionListener))([DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener) Remove the value at this location when the client disconnects |
| ApiFuture\<Void\> | [removeValueAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/OnDisconnect#removeValueAsync())() Remove the value at this location when the client disconnects |
| void | [setValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object, double, com.google.firebase.database.DatabaseReference.CompletionListener))(Object value, double priority, [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener) Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| void | [setValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object, java.util.Map, com.google.firebase.database.DatabaseReference.CompletionListener))(Object value, Map priority, [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener) Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| void | [setValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object, java.lang.String, com.google.firebase.database.DatabaseReference.CompletionListener))(Object value, String priority, [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener) Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| void | [setValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object, com.google.firebase.database.DatabaseReference.CompletionListener))(Object value, [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener) Ensure the data at this location is set to the specified value when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| ApiFuture\<Void\> | [setValueAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/OnDisconnect#setValueAsync(java.lang.Object, java.lang.String))(Object value, String priority) Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| ApiFuture\<Void\> | [setValueAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/OnDisconnect#setValueAsync(java.lang.Object))(Object value) Ensure the data at this location is set to the specified value when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| ApiFuture\<Void\> | [setValueAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/OnDisconnect#setValueAsync(java.lang.Object, double))(Object value, double priority) Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| void | [updateChildren](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/OnDisconnect#updateChildren(java.util.Map<java.lang.String, java.lang.Object>, com.google.firebase.database.DatabaseReference.CompletionListener))(Map\<String, Object\> update, [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener) Ensure the data has the specified child values updated when the client is disconnected |
| ApiFuture\<Void\> | [updateChildrenAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/OnDisconnect#updateChildrenAsync(java.util.Map<java.lang.String, java.lang.Object>))(Map\<String, Object\> update) Ensure the data has the specified child values updated when the client is disconnected |

### Inherited Method Summary

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

#### public void
**cancel**
([DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener)

Cancel any disconnect operations that are queued up at this location

##### Parameters

| listener | A listener that will be triggered once the server has cancelled the operations |
|---|---|

#### public ApiFuture\<Void\>
**cancelAsync**
()

Cancel any disconnect operations that are queued up at this location

##### Returns

- The ApiFuture for this operation.

#### public void
**removeValue**
([DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener)

Remove the value at this location when the client disconnects

##### Parameters

| listener | A listener that will be triggered once the server has queued up the operation |
|---|---|

#### public ApiFuture\<Void\>
**removeValueAsync**
()

Remove the value at this location when the client disconnects

##### Returns

- The ApiFuture for this operation.

#### public void
**setValue**
(Object value, double priority, [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener)

Ensure the data at this location is set to the specified value and priority when the client is
disconnected (due to closing the browser, navigating to a new page, or network issues).   

<br />


This method is especially useful for implementing "presence" systems, where a value should be
changed or cleared when a user disconnects so that they appear "offline" to other users.

##### Parameters

| value | The value to be set when a disconnect occurs |
| priority | The priority to be set when a disconnect occurs |
| listener | A listener that will be triggered once the server has queued up the operation |
|---|---|

#### public void
**setValue**
(Object value, Map priority, [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener)

Ensure the data at this location is set to the specified value and priority when the client is
disconnected (due to closing the browser, navigating to a new page, or network issues).   

<br />


This method is especially useful for implementing "presence" systems, where a value should be
changed or cleared when a user disconnects so that they appear "offline" to other users.

##### Parameters

| value | The value to be set when a disconnect occurs |
| priority | The priority to be set when a disconnect occurs |
| listener | A listener that will be triggered once the server has queued up the operation |
|---|---|

#### public void
**setValue**
(Object value, String priority, [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener)

Ensure the data at this location is set to the specified value and priority when the client is
disconnected (due to closing the browser, navigating to a new page, or network issues).   

<br />


This method is especially useful for implementing "presence" systems, where a value should be
changed or cleared when a user disconnects so that they appear "offline" to other users.

##### Parameters

| value | The value to be set when a disconnect occurs |
| priority | The priority to be set when a disconnect occurs |
| listener | A listener that will be triggered once the server has queued up the operation |
|---|---|

#### public void
**setValue**
(Object value, [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener)

Ensure the data at this location is set to the specified value when the client is disconnected
(due to closing the browser, navigating to a new page, or network issues).   

<br />


This method is especially useful for implementing "presence" systems, where a value should be
changed or cleared when a user disconnects so that they appear "offline" to other users.

##### Parameters

| value | The value to be set when a disconnect occurs |
| listener | A listener that will be triggered once the server has queued up the operation |
|---|---|

#### public ApiFuture\<Void\>
**setValueAsync**
(Object value, String priority)

Ensure the data at this location is set to the specified value and priority when the client is
disconnected (due to closing the browser, navigating to a new page, or network issues).   

<br />


This method is especially useful for implementing "presence" systems, where a value should be
changed or cleared when a user disconnects so that they appear "offline" to other users.

##### Parameters

| value | The value to be set when a disconnect occurs |
| priority | The priority to be set when a disconnect occurs |
|---|---|

##### Returns

- The ApiFuture for this operation.

#### public ApiFuture\<Void\>
**setValueAsync**
(Object value)

Ensure the data at this location is set to the specified value when the client is disconnected
(due to closing the browser, navigating to a new page, or network issues).   

<br />


This method is especially useful for implementing "presence" systems, where a value should be
changed or cleared when a user disconnects so that they appear "offline" to other users.

##### Parameters

| value | The value to be set when a disconnect occurs |
|---|---|

##### Returns

- The ApiFuture for this operation.

#### public ApiFuture\<Void\>
**setValueAsync**
(Object value, double priority)

Ensure the data at this location is set to the specified value and priority when the client is
disconnected (due to closing the browser, navigating to a new page, or network issues).   

<br />


This method is especially useful for implementing "presence" systems, where a value should be
changed or cleared when a user disconnects so that they appear "offline" to other users.

##### Parameters

| value | The value to be set when a disconnect occurs |
| priority | The priority to be set when a disconnect occurs |
|---|---|

##### Returns

- The ApiFuture for this operation.

#### public void
**updateChildren**
(Map\<String, Object\> update, [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) listener)

Ensure the data has the specified child values updated when the client is disconnected

##### Parameters

| update | The paths to update, along with their desired values |
| listener | A listener that will be triggered once the server has queued up the operation |
|---|---|

#### public ApiFuture\<Void\>
**updateChildrenAsync**
(Map\<String, Object\> update)

Ensure the data has the specified child values updated when the client is disconnected

##### Parameters

| update | The paths to update, along with their desired values |
|---|---|

##### Returns

- The ApiFuture for this operation.