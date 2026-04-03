# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/database/child-listener.md.txt

# firebase::database::ChildListener Class Reference

# firebase::database::ChildListener


**This is an abstract class.**


`#include <listener.h>`

Child listener interface.

## Summary

Subclasses of this listener class can be used to receive events about changes in the child locations of a [firebase::database::Query](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query) or [firebase::database::DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference). Attach the listener to a location with [Query::AddChildListener()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a6ac1ee1619acbc89b03824e562cc9750) or [DatabaseReference::AddChildListener()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a6ac1ee1619acbc89b03824e562cc9750) and the appropriate method will be triggered when changes occur.

| ### Constructors and Destructors ||
|---|---|
| [~ChildListener](https://firebase.google.com/docs/reference/cpp/class/firebase/database/child-listener#classfirebase_1_1database_1_1_child_listener_1a3abd908fb54faa511b47b96f204ef478)`()` ||

|                                                                                                                                                                                                                                                                            ### Public functions                                                                                                                                                                                                                                                                             ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [OnCancelled](https://firebase.google.com/docs/reference/cpp/class/firebase/database/child-listener#classfirebase_1_1database_1_1_child_listener_1ab63ac7fbf9b270f8454393dee0621d58)`(const `[Error](https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aacf6e57cd8d76d485eeb3907fc298231)` & error, const char *error_message)=0`          | `virtual void` This method will be triggered in the event that this listener either failed at the server, or is removed as a result of the security and Firebase rules. |
| [OnChildAdded](https://firebase.google.com/docs/reference/cpp/class/firebase/database/child-listener#classfirebase_1_1database_1_1_child_listener_1a85903f8c0785c8acf41be3097b489f93)`(const `[DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot)` & snapshot, const char *previous_sibling_key)=0`   | `virtual void` This method is triggered when a new child is added to the location to which this listener was added.                                                     |
| [OnChildChanged](https://firebase.google.com/docs/reference/cpp/class/firebase/database/child-listener#classfirebase_1_1database_1_1_child_listener_1a48d5e76e56d5e426a38073e875321edd)`(const `[DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot)` & snapshot, const char *previous_sibling_key)=0` | `virtual void` This method is triggered when the data at a child location has changed.                                                                                  |
| [OnChildMoved](https://firebase.google.com/docs/reference/cpp/class/firebase/database/child-listener#classfirebase_1_1database_1_1_child_listener_1a5e3e042aca509c8963f9f8337ccf1d7a)`(const `[DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot)` & snapshot, const char *previous_sibling_key)=0`   | `virtual void` This method is triggered when a child location's priority changes.                                                                                       |
| [OnChildRemoved](https://firebase.google.com/docs/reference/cpp/class/firebase/database/child-listener#classfirebase_1_1database_1_1_child_listener_1aa93f2703105e48959081e5c18d7a6df8)`(const `[DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot)` & snapshot)=0`                                   | `virtual void` This method is triggered when a child is removed from the location to which this listener was added.                                                     |

## Public functions

### OnCancelled

```c++
virtual void OnCancelled(
  const Error & error,
  const char *error_message
)=0
```  
This method will be triggered in the event that this listener either failed at the server, or is removed as a result of the security and Firebase rules.

<br />

|                                                                                                             Details                                                                                                              ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|--------------------------------------------------| | `error`         | A code corresponding to the error that occurred. | | `error_message` | A description of the error that occurred.        | |

### OnChildAdded

```c++
virtual void OnChildAdded(
  const DataSnapshot & snapshot,
  const char *previous_sibling_key
)=0
```  
This method is triggered when a new child is added to the location to which this listener was added.

<br />

|                                                                                                                                                                                                                                  Details                                                                                                                                                                                                                                   ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------------------|-------------------------------------------------------------------------------------------------------------------------| | `snapshot`             | An immutable snapshot of the data at the new data at the child location.                                                | | `previous_sibling_key` | The key name of sibling location ordered before the child. This will be nullptr for the first child node of a location. | |

### OnChildChanged

```c++
virtual void OnChildChanged(
  const DataSnapshot & snapshot,
  const char *previous_sibling_key
)=0
```  
This method is triggered when the data at a child location has changed.

<br />

|                                                                                                                                                                                                                                  Details                                                                                                                                                                                                                                   ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------------------|-------------------------------------------------------------------------------------------------------------------------| | `snapshot`             | An immutable snapshot of the data at the new data at the child location.                                                | | `previous_sibling_key` | The key name of sibling location ordered before the child. This will be nullptr for the first child node of a location. | |

### OnChildMoved

```c++
virtual void OnChildMoved(
  const DataSnapshot & snapshot,
  const char *previous_sibling_key
)=0
```  
This method is triggered when a child location's priority changes.

See [DatabaseReference::SetPriority()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference_1a9f87499352b02d550de465316358bef6) for more information on priorities and ordering data.

<br />

|                                                                                                                                                                                                                                  Details                                                                                                                                                                                                                                   ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------------------|-------------------------------------------------------------------------------------------------------------------------| | `snapshot`             | An immutable snapshot of the data at the new data at the child location.                                                | | `previous_sibling_key` | The key name of sibling location ordered before the child. This will be nullptr for the first child node of a location. | |

### OnChildRemoved

```c++
virtual void OnChildRemoved(
  const DataSnapshot & snapshot
)=0
```  
This method is triggered when a child is removed from the location to which this listener was added.

<br />

|                                                                                             Details                                                                                             ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|--------------------------------------------------------------------------| | `snapshot` | An immutable snapshot of the data at the new data at the child location. | |

### \~ChildListener

```c++
virtual  ~ChildListener()
```