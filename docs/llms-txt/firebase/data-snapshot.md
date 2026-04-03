# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot.md.txt

# Firebase.Database.DataSnapshot Class Reference

# Firebase.Database.DataSnapshot

A [DataSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot) instance contains data from a [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) location.

## Summary

A [DataSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot) instance contains data from a [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) location. Any time you read [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) data, you receive the data as a [DataSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot).   


DataSnapshots are passed to events [Query.ValueChanged](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a80a78f3505955b9ed2583dc2f14cf739)

, [Query.ChildChanged](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a71e2af7868312246b5da3024bb13204c)

, [Query.ChildMoved](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1ade5832ad58d0b31fd5a649019bb8f2c9)

, [Query.ChildRemoved](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1af4ef267bfef07b1969bd1394eb45c428)

, or [Query.ChildAdded](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a6c892241cfe3d3cfa77540d6341a0016)

<br />

<br />


They are efficiently-generated immutable copies of the data at a [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) location. They can't be modified and will never change. To modify data at a location, use a [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) reference (e.g. with [DatabaseReference.SetValueAsync(object)](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1af0d327eaa52ab10ee0f270507f926599)

).

|                                                                                                                                                                                                           ### Properties                                                                                                                                                                                                           ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Children](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot_1ae4827fb6022f78793c8cfd2a9f6cc488)      | `IEnumerable< `[DataSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot)` >` Gives access to all of the immediate children of this Snapshot.  |
| [ChildrenCount](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot_1a2e77720d94c47774cffe029ba8b6a5ca) | `long` The number of immediate children in the this snapshot.                                                                                                                                                                            |
| [Exists](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot_1aa2df06207ff639ea37e2c61f868279e0)        | `bool` Returns true if the snapshot contains a non-null value.                                                                                                                                                                           |
| [HasChildren](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot_1a255f564843ce8380bc818ee8433bee29)   | `bool` Indicates whether this snapshot has any children                                                                                                                                                                                  |
| [Key](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot_1a59b2e89bf8e589ae6e1150d27cf32a33)           | `string` The key name for the source location of this snapshot.                                                                                                                                                                          |
| [Priority](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot_1af608ba0a94e034a92c20dc14bcac74ad)      | `object` Returns the priority of the data contained in this snapshot as a native type.                                                                                                                                                   |
| [Reference](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot_1aa6a3946cb0a226837169ca8656823d41)     | [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) Used to obtain a reference to the source location for this Snapshot. |
| [Value](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot_1a45e32265ebf6ad5ee66848b425e9a934)         | `object` Value returns the data contained in this snapshot as native types.                                                                                                                                                              |

|                                                                                                                                                                                                                                                                             ### Public functions                                                                                                                                                                                                                                                                              ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Child](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot_1a0dbbb319d6dcd8fc7ade50301915e714)`(string path)`             | [DataSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot) Get a [DataSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot) for the location at the specified relative path. |
| [GetRawJsonValue](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot_1aeac5f8a0bcdf5bc3761a13f9f7081570)`()`              | `string` [GetRawJsonValue()](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot_1aeac5f8a0bcdf5bc3761a13f9f7081570) returns the data contained in this snapshot as a json serialized string.                                                                                   |
| [GetValue](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot_1a7b9ec71968b4a435c8c6b251b1596cfb)`(bool useExportFormat)` | `object` [GetValue()](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot_1a7b9ec71968b4a435c8c6b251b1596cfb) returns the data contained in this snapshot as native types.                                                                                                      |
| [HasChild](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot_1a053a31df8410a2bec88c285d40c1930c)`(string path)`          | `bool` Can be used to determine if this [DataSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot) has data at a particular location                                                                                                                                   |
| [ToString](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot_1ad158736fcc1ce7aa91fb055aea2610b0)`()`                     | `override string` A string representing the [DataSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot) as a key, value pair.                                                                                                                                           |

## Properties

### Children

```c#
IEnumerable< DataSnapshot > Children
```  
Gives access to all of the immediate children of this Snapshot.

Gives access to all of the immediate children of this Snapshot. Can be used in native for loops:

<br />

|                       Details                        ||
|-------------|-----------------------------------------|
| **Returns** | The immediate children of this snapshot |

### ChildrenCount

```c#
long ChildrenCount
```  
The number of immediate children in the this snapshot.  

### Exists

```c#
bool Exists
```  
Returns true if the snapshot contains a non-null value.

<br />

|                                   Details                                    ||
|-------------|-----------------------------------------------------------------|
| **Returns** | True if the snapshot contains a non-null value, otherwise false |

### HasChildren

```c#
bool HasChildren
```  
Indicates whether this snapshot has any children

<br />

|                               Details                               ||
|-------------|--------------------------------------------------------|
| **Returns** | True if the snapshot has any children, otherwise false |

### Key

```c#
string Key
```  
The key name for the source location of this snapshot.  

### Priority

```c#
object Priority
```  
Returns the priority of the data contained in this snapshot as a native type.

Returns the priority of the data contained in this snapshot as a native type. Possible return types:

- double
- string Note that null is also allowed.

<br />

<br />

|                                      Details                                      ||
|-------------|----------------------------------------------------------------------|
| **Returns** | the priority of the data contained in this snapshot as a native type |

### Reference

```c#
DatabaseReference Reference
```  
Used to obtain a reference to the source location for this Snapshot.

<br />

|                                                                                                                    Details                                                                                                                    ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) corresponding to the location that this snapshot came from |

### Value

```c#
object Value
```  
Value returns the data contained in this snapshot as native types.

Value returns the data contained in this snapshot as native types. The possible types returned are:

- bool
- string
- long
- double
- IDictionary{string, object}
- List{object} This list is recursive; the possible types for object in the above list is given by the same list. These types correspond to the types available in JSON.

<br />

<br />

|                             Details                              ||
|-------------|-----------------------------------------------------|
| **Returns** | The data contained in this snapshot as native types |

## Public functions

### Child

```c#
DataSnapshot Child(
  string path
)
```  
Get a [DataSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot) for the location at the specified relative path.

Get a [DataSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot) for the location at the specified relative path. The relative path can either be a simple child key (e.g. 'fred') or a deeper slash-separated path (e.g. 'fred/name/first'). If the child location has no data, an empty [DataSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot) is returned.

<br />

|                                                                                           Details                                                                                            ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------|-----------------------------------------------| | `path` | A relative path to the location of child data |                                                           |
| **Returns** | The [DataSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot) for the child location |

### GetRawJsonValue

```c#
string GetRawJsonValue()
```  
[GetRawJsonValue()](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot_1aeac5f8a0bcdf5bc3761a13f9f7081570) returns the data contained in this snapshot as a json serialized string.

[GetRawJsonValue()](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot_1aeac5f8a0bcdf5bc3761a13f9f7081570) returns the data contained in this snapshot as a json string.

|                                      Details                                      ||
|-------------|----------------------------------------------------------------------|
| **Returns** | The data contained in this snapshot as json. Return null if no data. |

### GetValue

```c#
object GetValue(
  bool useExportFormat
)
```  
[GetValue()](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot_1a7b9ec71968b4a435c8c6b251b1596cfb) returns the data contained in this snapshot as native types.

[GetValue()](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot_1a7b9ec71968b4a435c8c6b251b1596cfb) returns the data contained in this snapshot as native types. The possible types returned are:

- bool
- string
- long
- double
- IDictionary{string, object}
- List{object} This list is recursive; the possible types for object in the above list is given by the same list. These types correspond to the types available in JSON. If useExportFormat is set to true, priority information will be included in the output. Priority information shows up as a .priority key in a map. For data that would not otherwise be a map, the map will also include a .value key with the data.

<br />

<br />

|                                                                          Details                                                                           ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------------------|------------------------------------------------| | `useExportFormat` | Whether or not to include priority information | |
| **Returns** | The data, along with its priority, in native types                                                                                            |

### HasChild

```c#
bool HasChild(
  string path
)
```  
Can be used to determine if this [DataSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot) has data at a particular location

<br />

|                                                              Details                                                               ||
|-------------|-----------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------|-----------------------------------------------| | `path` | A relative path to the location of child data | |
| **Returns** | Whether or not the specified child location has data                                                                  |

### ToString

```c#
override string ToString()
```  
A string representing the [DataSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot) as a key, value pair.

It returns the following form: [DataSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot)` { key = {Key}, value = {Value} };`