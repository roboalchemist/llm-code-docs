# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration.md.txt

# firebase::remote_config::ConfigUpdateListenerRegistration Class Reference

# firebase::remote_config::ConfigUpdateListenerRegistration


`#include <config_update_listener_registration.h>`

Calling Remove stops the listener from receiving config updates and unregisters itself.

## Summary

If remove is called and no other listener registrations remain, the connection to the Remote Config backend is closed. Subsequently calling AddOnConfigUpdate will re-open the connection.

| ### Constructors and Destructors ||
|---|---|
| [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration_1ad54e752cc19a68e0b302e136a8e9ef3f)`()` Creates an invalid [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration) that has to be reassigned before it can be used. ||
| [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration_1a46960f3a5b28abaacbc375ac75c9413b)`(const `[ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration)` & other)` Copy constructor. ||
| [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration_1a0b124e32b90f1e9310f1dafac083c4bb)`(`[ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration)` && other)` Move constructor. ||
| [~ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration_1ab4dc41e98f37d02a24febd0b6462ed19)`()` ||

|                                                                                                                                                                                                                                                                                                                                                                         ### Public functions                                                                                                                                                                                                                                                                                                                                                                          ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Remove](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration_1a6ed0677a470faaa276d224566b28248f)`()`                                                                                                                                                                                                                                               | `void` Remove the listener being tracked by this [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration). |
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration_1a6fb49bd93d6e191e962ff968e97c9d54)`(const `[ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration)` & other)` | [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration)` &` Copy assignment operator.                     |
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration_1ad7a548f89f7f9119b454aa6399f044bb)`(`[ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration)` && other)`      | [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration)` &` Move assignment operator.                     |

## Public functions

### ConfigUpdateListenerRegistration

```c++
 ConfigUpdateListenerRegistration()
```  
Creates an invalid [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration) that has to be reassigned before it can be used.

Calling [Remove()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration_1a6ed0677a470faaa276d224566b28248f) on an invalid [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration) is a no-op.  

### ConfigUpdateListenerRegistration

```c++
 ConfigUpdateListenerRegistration(
  const ConfigUpdateListenerRegistration & other
)
```  
Copy constructor.

[ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration) can be efficiently copied because it simply refers to the same underlying listener. If there is more than one copy of a [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration), after calling `Remove` on one of them, the listener is removed, and calling `Remove` on any other copies will be a no-op.

<br />

|                                                                                                                                                                                                                                                           Details                                                                                                                                                                                                                                                           ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration) to copy from. | |

### ConfigUpdateListenerRegistration

```c++
 ConfigUpdateListenerRegistration(
  ConfigUpdateListenerRegistration && other
)
```  
Move constructor.

Moving is more efficient than copying for a [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration). After being moved from, a [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration) is equivalent to its default-constructed state.

<br />

|                                                                                                                                                                                                                                                                Details                                                                                                                                                                                                                                                                ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration) to move data from. | |

### Remove

```c++
void Remove()
```  
Remove the listener being tracked by this [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration).

After the initial call, subsequent calls to Remove have no effect.  

### operator=

```c++
ConfigUpdateListenerRegistration & operator=(
  const ConfigUpdateListenerRegistration & other
)
```  
Copy assignment operator.

[ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration) can be efficiently copied because it simply refers to the same underlying listener. If there is more than one copy of a [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration), after calling `Remove` on one of them, the listener is removed, and calling `Remove` on any other copies will be a no-op.

<br />

|                                                                                                                                                                                                                                                           Details                                                                                                                                                                                                                                                            ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration) to copy from. | |
| **Returns** | Reference to the destination [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration).                                                                                                                                                                                                                                                       |

### operator=

```c++
ConfigUpdateListenerRegistration & operator=(
  ConfigUpdateListenerRegistration && other
)
```  
Move assignment operator.

Moving is more efficient than copying for a [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration). After being moved from, a [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration) is equivalent to its default-constructed state.

<br />

|                                                                                                                                                                                                                                                                Details                                                                                                                                                                                                                                                                 ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration) to move data from. | |
| **Returns** | Reference to the destination [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration).                                                                                                                                                                                                                                                                 |

### \~ConfigUpdateListenerRegistration

```c++
virtual  ~ConfigUpdateListenerRegistration()
```