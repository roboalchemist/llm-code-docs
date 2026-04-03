# Source: https://firebase.google.com/docs/reference/unity/class/firebase/database/on-disconnect.md.txt

# Firebase.Database.OnDisconnect Class Reference

# Firebase.Database.OnDisconnect

The [OnDisconnect](https://firebase.google.com/docs/reference/unity/class/firebase/database/on-disconnect#class_firebase_1_1_database_1_1_on_disconnect) class is used to manage operations that will be Run on the server when this client disconnects.

## Summary

The [OnDisconnect](https://firebase.google.com/docs/reference/unity/class/firebase/database/on-disconnect#class_firebase_1_1_database_1_1_on_disconnect) class is used to manage operations that will be Run on the server when this client disconnects. It can be used to add or Remove data based on a client's connection status. It is very useful in applications looking for 'presence' functionality.   


Instances of this class are obtained by calling onDisconnect DatabaseReference.onDisconnect()

on a [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) ref.

|                                                                                                                                                                                                       ### Public functions                                                                                                                                                                                                       ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Cancel](https://firebase.google.com/docs/reference/unity/class/firebase/database/on-disconnect#class_firebase_1_1_database_1_1_on_disconnect_1a7cae8b7402a7c4bfdc028620418e99c2)`()`                                             | `Task` Cancel any disconnect operations that are queued up at this location                                                                                                                   |
| [RemoveValue](https://firebase.google.com/docs/reference/unity/class/firebase/database/on-disconnect#class_firebase_1_1_database_1_1_on_disconnect_1af30f149086a831fe1f28236cc63b4d72)`()`                                        | `Task` Remove the value at this location when the client disconnects                                                                                                                          |
| [SetValue](https://firebase.google.com/docs/reference/unity/class/firebase/database/on-disconnect#class_firebase_1_1_database_1_1_on_disconnect_1aca4606de04684e23afe3303ca7fe2fa9)`(object value)`                               | `Task` Ensure the data at this location is set to the specified value when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).              |
| [SetValue](https://firebase.google.com/docs/reference/unity/class/firebase/database/on-disconnect#class_firebase_1_1_database_1_1_on_disconnect_1a91a216dd87df98475e9b52d54b83a679)`(object value, string priority)`              | `Task` Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| [SetValue](https://firebase.google.com/docs/reference/unity/class/firebase/database/on-disconnect#class_firebase_1_1_database_1_1_on_disconnect_1a50d18d78ad92dc95cf216a986a1ad2b2)`(object value, double priority)`              | `Task` Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| [UpdateChildren](https://firebase.google.com/docs/reference/unity/class/firebase/database/on-disconnect#class_firebase_1_1_database_1_1_on_disconnect_1a8fd69769048a7607480020f6a7e88ab9)`(IDictionary< string, object > update)` | `Task` Ensure the data has the specified child values updated when the client is disconnected                                                                                                 |

## Public functions

### Cancel

```c#
Task Cancel()
```  
Cancel any disconnect operations that are queued up at this location

<br />

|                      Details                       ||
|-------------|---------------------------------------|
| **Returns** | The Task{TResult} for this operation. |

### RemoveValue

```c#
Task RemoveValue()
```  
Remove the value at this location when the client disconnects

<br />

|                      Details                       ||
|-------------|---------------------------------------|
| **Returns** | The Task{TResult} for this operation. |

### SetValue

```c#
Task SetValue(
  object value
)
```  
Ensure the data at this location is set to the specified value when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).

Ensure the data at this location is set to the specified value when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).   


This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.

<br />

|                                                              Details                                                               ||
|-------------|-----------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|----------------------------------------------| | `value` | The value to be set when a disconnect occurs | |
| **Returns** | The Task{TResult} for this operation.                                                                                 |

### SetValue

```c#
Task SetValue(
  object value,
  string priority
)
```  
Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).

Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).   


This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.

<br />

|                                                                                                     Details                                                                                                     ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|-------------------------------------------------| | `value`    | The value to be set when a disconnect occurs    | | `priority` | The priority to be set when a disconnect occurs | |
| **Returns** | The Task{TResult} for this operation.                                                                                                                                                              |

### SetValue

```c#
Task SetValue(
  object value,
  double priority
)
```  
Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).

Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).   


This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.

<br />

|                                                                                                     Details                                                                                                     ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|-------------------------------------------------| | `value`    | The value to be set when a disconnect occurs    | | `priority` | The priority to be set when a disconnect occurs | |
| **Returns** | The Task{TResult} for this operation.                                                                                                                                                              |

### UpdateChildren

```c#
Task UpdateChildren(
  IDictionary< string, object > update
)
```  
Ensure the data has the specified child values updated when the client is disconnected

<br />

|                                                                       Details                                                                        ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------|------------------------------------------------------| | `update` | The paths to update, along with their desired values | |
| **Returns** | The Task{TResult} for this operation.                                                                                                   |