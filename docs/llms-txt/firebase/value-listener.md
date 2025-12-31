# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/database/value-listener.md.txt

# firebase::database::ValueListener Class Reference

# firebase::database::ValueListener


**This is an abstract class.**


`#include <listener.h>`

Value listener interface.

## Summary

Subclasses of this listener class can be used to receive events about data changes at a location. Attach the listener to a location using [DatabaseReference::AddValueListener()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1aeb583c0c607b01692f9aaa9a59432810) or [Query::AddValueListener()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1aeb583c0c607b01692f9aaa9a59432810), and [OnValueChanged()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/value-listener#classfirebase_1_1database_1_1_value_listener_1a02ce2f03e20564a124b5d290158494a8) will be called once immediately, and again when the value changes.

| ### Constructors and Destructors ||
|---|---|
| [~ValueListener](https://firebase.google.com/docs/reference/cpp/class/firebase/database/value-listener#classfirebase_1_1database_1_1_value_listener_1ae594401b91d5fcf0020241f8e2a09d3d)`()` ||

|                                                                                                                                                                                                                                                                        ### Public functions                                                                                                                                                                                                                                                                        ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [OnCancelled](https://firebase.google.com/docs/reference/cpp/class/firebase/database/value-listener#classfirebase_1_1database_1_1_value_listener_1a8f97aa3b6378c57d0d4b8cf853a95538)`(const `[Error](https://firebase.google.com/docs/reference/cpp/namespace/firebase/database#namespacefirebase_1_1database_1aacf6e57cd8d76d485eeb3907fc298231)` & error, const char *error_message)=0` | `virtual void` This method will be triggered in the event that this listener either failed at the server, or is removed as a result of the security and Firebase rules. |
| [OnValueChanged](https://firebase.google.com/docs/reference/cpp/class/firebase/database/value-listener#classfirebase_1_1database_1_1_value_listener_1a02ce2f03e20564a124b5d290158494a8)`(const `[DataSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/database/data-snapshot#classfirebase_1_1database_1_1_data_snapshot)` & snapshot)=0`                          | `virtual void` This method will be called with a snapshot of the data at this location each time that data changes.                                                     |

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

### OnValueChanged

```c++
virtual void OnValueChanged(
  const DataSnapshot & snapshot
)=0
```  
This method will be called with a snapshot of the data at this location each time that data changes.

<br />

|                                                      Details                                                      ||
|------------|-------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-----------------------------------| | `snapshot` | The current data at the location. | |

### \~ValueListener

```c++
virtual  ~ValueListener()
```