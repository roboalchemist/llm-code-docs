# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration.md.txt

# firebase::firestore::ListenerRegistration Class Reference

# firebase::firestore::ListenerRegistration


`#include <listener_registration.h>`

Represents a listener that can be removed by calling [Remove()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration_1acb1a46cf74c63cd376252babe8dcc018).

## Summary

| ### Constructors and Destructors ||
|---|---|
| [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration_1a360e7b9ea3df89dca7163594f5ef0966)`()` Creates an invalid [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration) that has to be reassigned before it can be used. ||
| [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration_1a9572ff9ec2fd95ad637799b9fb29bf01)`(const `[ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration)` & other)` Copy constructor. ||
| [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration_1a1aef70877ce764cecfbb212977aa9758)`(`[ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration)` && other)` Move constructor. ||
| [~ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration_1a6f7ed3bdd53efb3b2db048078cd3c383)`()` ||

|                                                                                                                                                                                                                                                                                                             ### Public functions                                                                                                                                                                                                                                                                                                             ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Remove](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration_1acb1a46cf74c63cd376252babe8dcc018)`()`                                                                                                                                                                                              | `virtual void` Removes the listener being tracked by this [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration).      |
| [is_valid](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration_1a8865ae5416d69bee45a4a395d6fb071b)`() const `                                                                                                                                                                                     | `bool` Returns true if this [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration) is valid, false if it is not valid. |
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration_1a338d8f3e27d15b0d974dc9c091d8a270)`(const `[ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration)` & other)` | [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration)` &` Copy assignment operator.                                   |
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration_1a584846023d1cba558e5bef27627f4b76)`(`[ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration)` && other)`      | [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration)` &` Move assignment operator.                                   |

## Public functions

### ListenerRegistration

```c++
 ListenerRegistration()
```  
Creates an invalid [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration) that has to be reassigned before it can be used.

Calling [Remove()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration_1acb1a46cf74c63cd376252babe8dcc018) on an invalid [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration) is a no-op.  

### ListenerRegistration

```c++
 ListenerRegistration(
  const ListenerRegistration & other
)
```  
Copy constructor.

[ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration) can be efficiently copied because it simply refers to the same underlying listener. If there is more than one copy of a [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration), after calling `Remove` on one of them, the listener is removed, and calling `Remove` on any other copies will be a no-op.

<br />

|                                                                                                                                                                                                          Details                                                                                                                                                                                                          ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration) to copy from. | |

### ListenerRegistration

```c++
 ListenerRegistration(
  ListenerRegistration && other
)
```  
Move constructor.

Moving is more efficient than copying for a [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration). After being moved from, a [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration) is equivalent to its default-constructed state.

<br />

|                                                                                                                                                                                                               Details                                                                                                                                                                                                               ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration) to move data from. | |

### Remove

```c++
virtual void Remove()
```  
Removes the listener being tracked by this [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration).

After the initial call, subsequent calls have no effect.  

### is_valid

```c++
bool is_valid() const 
```  
Returns true if this [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration) is valid, false if it is not valid.

An invalid [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration) could be the result of:

- Creating a [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration) using the default constructor.
- Moving from the [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration).
- Deleting your [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance, which will invalidate all the [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration) instances associated with it.

<br />

<br />

|                                                                                                                                                                                                       Details                                                                                                                                                                                                       ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | true if this [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration) is valid, false if this [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration) is invalid. |

### operator=

```c++
ListenerRegistration & operator=(
  const ListenerRegistration & other
)
```  
Copy assignment operator.

[ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration) can be efficiently copied because it simply refers to the same underlying listener. If there is more than one copy of a [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration), after calling `Remove` on one of them, the listener is removed, and calling `Remove` on any other copies will be a no-op.

<br />

|                                                                                                                                                                                                          Details                                                                                                                                                                                                           ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration) to copy from. | |
| **Returns** | Reference to the destination [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration).                                                                                                                                                                                                      |

### operator=

```c++
ListenerRegistration & operator=(
  ListenerRegistration && other
)
```  
Move assignment operator.

Moving is more efficient than copying for a [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration). After being moved from, a [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration) is equivalent to its default-constructed state.

<br />

|                                                                                                                                                                                                               Details                                                                                                                                                                                                                ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration) to move data from. | |
| **Returns** | Reference to the destination [ListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration).                                                                                                                                                                                                                |

### \~ListenerRegistration

```c++
virtual  ~ListenerRegistration()
```