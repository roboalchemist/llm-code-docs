# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/database/mutable-data.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data.md.txt

# Firebase.Database.MutableData Class Reference

# Firebase.Database.MutableData

Instances of this class encapsulate the data and priority at a location.

## Summary

Instances of this class encapsulate the data and priority at a location. It is used in transactions, and it is intended to be inspected and then updated to the desired data at that location.   


Note that changes made to a child [MutableData](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data) instance will be visible to the parent and vice versa.

|                                                                                                                                                                                                      ### Properties                                                                                                                                                                                                       ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Children](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data_1a3af42366ee4142bc0dc9be76877bbfd7)      | `IEnumerable< `[MutableData](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data)` >` Used to iterate over the immediate children at this location |
| [ChildrenCount](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data_1a09809a3baa7b1c7dd9afb677039bd4a7) | `long` The number of immediate children at this location.                                                                                                                                                                         |
| [HasChildren](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data_1a850fef27efd55f6da96848af871ebaa5)   | `bool` True if the data at this location has children, false otherwise.                                                                                                                                                           |
| [Key](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data_1a4bd529dad6d9751d1e73c35a429278cf)           | `string` The key name of this location, or null if it is the top-most location.                                                                                                                                                   |
| [Priority](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data_1a60cac0feb484161401f7de6b064bda75)      | `object` Gets the current priority at this location.                                                                                                                                                                              |
| [Value](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data_1a4833f23246b3079078332d57c5649254)         | `object` getValue() returns the data contained in this instance as native types.                                                                                                                                                  |

|                                                                                                                                                                                                                                                                                        ### Public functions                                                                                                                                                                                                                                                                                         ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Child](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data_1a3065ae4bbf06e227705dfbe8f423cea2)`(string path)`    | [MutableData](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data) Used to obtain a [MutableData](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data) instance that encapsulates the data and priority at the given relative path. |
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data_1a996f7674bf97a1d23478155d085374a2)`(object o)`      | `override bool` Two [MutableData](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data) are considered equal if they contain the same references and priority.                                                                                                                                                      |
| [GetHashCode](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data_1ab29f86d675a6e280c83970e0cf9b0b6c)`()`         | `override int` Overriden to ensure two objects that are Equal have the same hash.                                                                                                                                                                                                                                                                                                                 |
| [HasChild](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data_1a5794c7413ffc9a8552334d187b958a26)`(string path)` | `bool` Determines if data exists at the given path.                                                                                                                                                                                                                                                                                                                                               |
| [ToString](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data_1a39255e13dd3fe6458151eb8fcb883837)`()`            | `override string` Representation of the mutable data as a string containing a key, value pair.                                                                                                                                                                                                                                                                                                    |

## Properties

### Children

```c#
IEnumerable< MutableData > Children
```  
Used to iterate over the immediate children at this location

Used to iterate over the immediate children at this location

<br />

|                       Details                        ||
|-------------|-----------------------------------------|
| **Returns** | The immediate children at this location |

### ChildrenCount

```c#
long ChildrenCount
```  
The number of immediate children at this location.  

### HasChildren

```c#
bool HasChildren
```  
True if the data at this location has children, false otherwise.  

### Key

```c#
string Key
```  
The key name of this location, or null if it is the top-most location.  

### Priority

```c#
object Priority
```  
Gets the current priority at this location.

Gets the current priority at this location. The possible return types are:

- Double
- String

Note that null is allowed

<br />

<br />

|                           Details                           ||
|-------------|------------------------------------------------|
| **Returns** | The priority at this location as a native type |

### Value

```c#
object Value
```  
getValue() returns the data contained in this instance as native types.

getValue() returns the data contained in this instance as native types. The possible types returned are:

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
| **Returns** | The data contained in this instance as native types |

## Public functions

### Child

```c#
MutableData Child(
  string path
)
```  
Used to obtain a [MutableData](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data) instance that encapsulates the data and priority at the given relative path.

<br />

|                                    Details                                     ||
|-------------|-------------------------------------------------------------------|
| Parameters  | |--------|-----------------| | `path` | A relative path |         |
| **Returns** | An instance encapsulating the data and priority at the given path |

### Equals

```c#
override bool Equals(
  object o
)
```  
Two [MutableData](https://firebase.google.com/docs/reference/unity/class/firebase/database/mutable-data#class_firebase_1_1_database_1_1_mutable_data) are considered equal if they contain the same references and priority.  

### GetHashCode

```c#
override int GetHashCode()
```  
Overriden to ensure two objects that are Equal have the same hash.  

### HasChild

```c#
bool HasChild(
  string path
)
```  
Determines if data exists at the given path.

<br />

|                                Details                                 ||
|-------------|-----------------------------------------------------------|
| Parameters  | |--------|-----------------| | `path` | A relative path | |
| **Returns** | True if data exists at the given path, otherwise false    |

### ToString

```c#
override string ToString()
```  
Representation of the mutable data as a string containing a key, value pair.