# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-key-value.md.txt

# firebase::remote_config::ConfigKeyValue Struct Reference

# firebase::remote_config::ConfigKeyValue


`#include <remote_config.h>`

Describes a mapping of a key to a string value.

## Summary

Used to set default values.

|                                                                                                             ### Public attributes                                                                                                              ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| [key](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-key-value#structfirebase_1_1remote__config_1_1_config_key_value_1ac90271d5a3631a664a3dd8da201a783f)   | `const char *` The lookup key string.         |
| [value](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-key-value#structfirebase_1_1remote__config_1_1_config_key_value_1a350e15f4e483d5273a46650f4731e12e) | `const char *` The value string to be stored. |

## Public attributes

### key

```c++
const char * firebase::remote_config::ConfigKeyValue::key
```  
The lookup key string.


| **Note:** Ensure this string stays valid for the duration of the call to SetDefaults.

<br />

### value

```c++
const char * firebase::remote_config::ConfigKeyValue::value
```  
The value string to be stored.


| **Note:** Ensure this string stays valid for the duration of the call to SetDefaults.

<br />