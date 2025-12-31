# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference.md.txt

# Firebase.Database.DatabaseReference Class Reference

# Firebase.Database.DatabaseReference

A [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) reference represents a particular location in your [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) and can be used for reading or writing data to that [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) location.

## Summary

A [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) reference represents a particular location in your [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) and can be used for reading or writing data to that [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) location. This class is the starting point for all [Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) operations. After you've initialized it with a URL, you can use it to read data, write data, and to create mores instances of [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference).

### Inheritance

Inherits from: [Firebase.Database.Query](https://firebase.google.com/docs/reference/unity/class/firebase/database/query)

|                                                                                                                                                                                                                                                                                                             ### Properties                                                                                                                                                                                                                                                                                                              ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Database](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1a939e8179903b48c6baace0055af59241) | [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) Gets the [Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) instance associated with this reference.                                                                                              |
| [Key](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1aa06ed0ac1ed48483d7717bb6baf6d3cb)      | `string` The last token in the location pointed to by this reference                                                                                                                                                                                                                                                                                                                                                                     |
| [Parent](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1a53ead6407807db035aee8323fe6c75d9)   | [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) A [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) to the parent location, or null if this instance references the root location.                 |
| [Root](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1ae6d8b33303fd1911b326e3cb7b25f2db)     | [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) A reference to the root location of this [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database). |

|                                                                                                                                                                                                                                                                                                                                                                                           ### Public functions                                                                                                                                                                                                                                                                                                                                                                                           ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Child](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1a0e46ffa936d157d6b93dc240313d69f1)`(string pathString)`                                                                                                                                                                                                                                                                                                                                                             | [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) Get a reference to location relative to this one        |
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1ad64dae03d140d9c741b561d8df2a3185)`(object other)`                                                                                                                                                                                                                                                                                                                                                                 | `override bool` Returns true if both objects reference the same database path.                                                                                                                                              |
| [GetHashCode](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1a73736ff8dce6efd205674cc9efda2084)`()`                                                                                                                                                                                                                                                                                                                                                                        | `override int` A hash code based on the string path of the reference.                                                                                                                                                       |
| [OnDisconnect](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1a34b15ad902d14db74fc767dc4560b699)`()`                                                                                                                                                                                                                                                                                                                                                                       | [OnDisconnect](https://firebase.google.com/docs/reference/unity/class/firebase/database/on-disconnect#class_firebase_1_1_database_1_1_on_disconnect) Provides access to disconnect operations at this location              |
| [Push](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1a0eb02bbcb15c6ac458a1a4240a25e1af)`()`                                                                                                                                                                                                                                                                                                                                                                               | [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) Create a reference to an auto-generated child location. |
| [RemoveValueAsync](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1ad77e1c00f6edbe8dc23ffd9a01174631)`()`                                                                                                                                                                                                                                                                                                                                                                   | `Task` Set the value at this location to 'null'                                                                                                                                                                             |
| [RunTransaction](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1a4b21a7318e923a839b8fcca6ca3e90b0)`(Func< `[MutableData](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data)`, `[TransactionResult](https://firebase.google.com/docs/reference/unity/class/firebase/database/transaction-result#class_firebase_1_1_database_1_1_transaction_result)` > transaction)`                       | `Task< `[DataSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot)` >` Run a transaction on the data at this location.            |
| [RunTransaction](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1ae8cb3a51aa9bf0f119897cffc5494dff)`(Func< `[MutableData](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data)`, `[TransactionResult](https://firebase.google.com/docs/reference/unity/class/firebase/database/transaction-result#class_firebase_1_1_database_1_1_transaction_result)` > transaction, bool fireLocalEvents)` | `Task< `[DataSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot)` >` Run a transaction on the data at this location.            |
| [SetPriorityAsync](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1a3aea2dee42597a5cbce83f1b6861df5a)`(object priority)`                                                                                                                                                                                                                                                                                                                                                    | `Task` Set a priority for the data at this [Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) location.                                               |
| [SetRawJsonValueAsync](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1adeb74c29f9619d905e04af20b4aa1e52)`(string jsonValue)`                                                                                                                                                                                                                                                                                                                                               | `Task` Set the data at this location to the given string json represenation.                                                                                                                                                |
| [SetRawJsonValueAsync](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1a548f63c0d8f90d1d4950bfcd070ba2a7)`(string jsonValue, object priority)`                                                                                                                                                                                                                                                                                                                              | `Task` Set the data and priority to the given values.                                                                                                                                                                       |
| [SetValueAsync](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1af0d327eaa52ab10ee0f270507f926599)`(object value)`                                                                                                                                                                                                                                                                                                                                                          | `Task` Set the data at this location to the given value.                                                                                                                                                                    |
| [SetValueAsync](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1a81a540f2549690178f47cb57db5980c4)`(object value, object priority)`                                                                                                                                                                                                                                                                                                                                         | `Task` Set the data and priority to the given values.                                                                                                                                                                       |
| [ToString](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1abab4a9c1b88836cfc581988c0f60dc0f)`()`                                                                                                                                                                                                                                                                                                                                                                           | `override string` The full location url for this reference.                                                                                                                                                                 |
| [UpdateChildrenAsync](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1a376ed13dffbd8e3064d58a0b1bb4c8a0)`(IDictionary< string, object > update)`                                                                                                                                                                                                                                                                                                                            | `Task` Update the specific child keys to the specified values.                                                                                                                                                              |

|                                                                                                                                                                                                                                               ### Public static functions                                                                                                                                                                                                                                                ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GoOffline](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1a588b792b473db41eef05609a6a3cc78c)`()` | `void` Manually disconnect the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) client from the server and disable automatic reconnection. |
| [GoOnline](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1af63730b06cfc950971d02f8b4129e439)`()`  | `void` Manually reestablish a connection to the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) server and enable automatic reconnection. |

## Properties

### Database

```c#
FirebaseDatabase Database
```  
Gets the [Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) instance associated with this reference.

<br />

|                                                                               Details                                                                                ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The [Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) object for this reference. |

### Key

```c#
string Key
```  
The last token in the location pointed to by this reference  

### Parent

```c#
DatabaseReference Parent
```  
A [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) to the parent location, or null if this instance references the root location.  

### Root

```c#
DatabaseReference Root
```  
A reference to the root location of this [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database).

## Public functions

### Child

```c#
DatabaseReference Child(
  string pathString
)
```  
Get a reference to location relative to this one

<br />

|                                                                                                  Details                                                                                                   ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------------|-----------------------------------------------------------------------------| | `pathString` | The relative path from this reference to the new one that should be created | |
| **Returns** | A new [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) to the given path   |

### Equals

```c#
override bool Equals(
  object other
)
```  
Returns true if both objects reference the same database path.  

### GetHashCode

```c#
override int GetHashCode()
```  
A hash code based on the string path of the reference.  

### OnDisconnect

```c#
OnDisconnect OnDisconnect()
```  
Provides access to disconnect operations at this location

<br />

|                                  Details                                   ||
|-------------|---------------------------------------------------------------|
| **Returns** | An object for managing disconnect operations at this location |

### Push

```c#
DatabaseReference Push()
```  
Create a reference to an auto-generated child location.

Create a reference to an auto-generated child location. The child key is generated client-side and incorporates an estimate of the server's time for sorting purposes. Locations generated on a single client will be sorted in the order that they are created, and will be sorted approximately in order across all clients.

<br />

|                                                                                                     Details                                                                                                     ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) pointing to the new location |

### RemoveValueAsync

```c#
Task RemoveValueAsync()
```  
Set the value at this location to 'null'

<br />

|                      Details                       ||
|-------------|---------------------------------------|
| **Returns** | The Task{TResult} for this operation. |

### RunTransaction

```c#
Task< DataSnapshot > RunTransaction(
  Func< MutableData, TransactionResult > transaction
)
```  
Run a transaction on the data at this location.

A transaction is a data transformation function that is continually attempted until the [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) location remains unchanged during the operation.

<br />

|                                                                                 Details                                                                                 ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|-----------------------------------------------------------| | `transaction` | A function to perform the transaction and return a result | |

### RunTransaction

```c#
Task< DataSnapshot > RunTransaction(
  Func< MutableData, TransactionResult > transaction,
  bool fireLocalEvents
)
```  
Run a transaction on the data at this location.

A transaction is a data transformation function that is continually attempted until the [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) location remains unchanged during the operation.

<br />

|                                                                                                                                                                                                                                                               Details                                                                                                                                                                                                                                                               ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------| | `transaction`     | A function to perform the transaction and return a result                                                                                       | | `fireLocalEvents` | Defaults to true. If set to false, events will only be fired for the final result state of the transaction, and not for any intermediate states | |

### SetPriorityAsync

```c#
Task SetPriorityAsync(
  object priority
)
```  
Set a priority for the data at this [Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) location.

Set a priority for the data at this [Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) location. Priorities can be used to provide a custom ordering for the children at a location (if no priorities are specified, the children are ordered by key).   


You cannot set a priority on an empty location. For this reason setValue(data, priority) should be used when setting initial data with a specific priority and setPriority should be used when updating the priority of existing data.   


Children are sorted based on this priority using the following rules:

- Children with no priority come first.
- Children with a number as their priority come next. They are sorted numerically by priority (small to large).
- Children with a string as their priority come last. They are sorted lexicographically by priority.
- Whenever two children have the same priority (including no priority), they are sorted by key. Numeric keys come first (sorted numerically), followed by the remaining keys (sorted lexicographically).

Note that numerical priorities are parsed and ordered as IEEE 754 double-precision floating-point numbers. Keys are always stored as strings and are treated as numeric only when they can be parsed as a 32-bit integer.

<br />

<br />

|                                                                   Details                                                                    ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|------------------------------------------------| | `priority` | The priority to set at the specified location. | |
| **Returns** | The Task{TResult} for this operation.                                                                                           |

### SetRawJsonValueAsync

```c#
Task SetRawJsonValueAsync(
  string jsonValue
)
```  
Set the data at this location to the given string json represenation.

<br />

|                      Details                       ||
|-------------|---------------------------------------|
| **Returns** | The Task{TResult} for this operation. |

### SetRawJsonValueAsync

```c#
Task SetRawJsonValueAsync(
  string jsonValue,
  object priority
)
```  
Set the data and priority to the given values.

<br />

|                      Details                       ||
|-------------|---------------------------------------|
| **Returns** | The Task{TResult} for this operation. |

### SetValueAsync

```c#
Task SetValueAsync(
  object value
)
```  
Set the data at this location to the given value.

Set the data at this location to the given value. Passing null to setValue() will delete the data at the specified location. The allowed types are:

- bool
- string
- long
- double
- IDictionary{string, object}
- List{object}   

<br />

<br />

|                                                   Details                                                    ||
|-------------|-------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-----------------------------------| | `value` | The value to set at this location | |
| **Returns** | The Task{TResult} for this operation.                                                           |

### SetValueAsync

```c#
Task SetValueAsync(
  object value,
  object priority
)
```  
Set the data and priority to the given values.

Set the data and priority to the given values. Passing null to setValue() will delete the data at the specified location. The allowed types are:

- bool
- string
- long
- double
- IDictionary{string, object}
- List{object}   

<br />

<br />

|                                                                                    Details                                                                                     ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|--------------------------------------| | `value`    | The value to set at this location    | | `priority` | The priority to set at this location | |
| **Returns** | The Task{TResult} for this operation.                                                                                                                             |

### ToString

```c#
override string ToString()
```  
The full location url for this reference.  

### UpdateChildrenAsync

```c#
Task UpdateChildrenAsync(
  IDictionary< string, object > update
)
```  
Update the specific child keys to the specified values.

Update the specific child keys to the specified values. Passing null in a map to updateChildren() will Remove the value at the specified location.

<br />

|                                                           Details                                                            ||
|-------------|-----------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------|------------------------------------------| | `update` | The paths to update and their new values | |
| **Returns** | The Task{TResult} for this operation.                                                                           |

## Public static functions

### GoOffline

```c#
void GoOffline()
```  
Manually disconnect the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) client from the server and disable automatic reconnection.

Manually disconnect the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) client from the server and disable automatic reconnection. Note: Invoking this method will impact all [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) connections.  

### GoOnline

```c#
void GoOnline()
```  
Manually reestablish a connection to the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) server and enable automatic reconnection.

Manually reestablish a connection to the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) server and enable automatic reconnection. Note: Invoking this method will impact all [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) connections.