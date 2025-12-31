# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-update.md.txt

# firebase::remote_config::ConfigUpdate Struct Reference

# firebase::remote_config::ConfigUpdate


`#include <remote_config.h>`

Information about the updated config.

## Summary

|                                                                                                                                               ### Public attributes                                                                                                                                               ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [updated_keys](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-update#structfirebase_1_1remote__config_1_1_config_update_1aeae7e1d0e6797a9bf79ff9151fd469c0) | `std::vector< std::string >` Parameter keys whose values have been updated from the currently activated values. |

## Public attributes

### updated_keys

```c++
std::vector< std::string > firebase::remote_config::ConfigUpdate::updated_keys
```  
Parameter keys whose values have been updated from the currently activated values.

Includes keys that are added, deleted, and whose value, value source, or metadata has changed.