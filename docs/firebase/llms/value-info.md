# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/value-info.md.txt

# firebase::remote_config::ValueInfo Struct Reference

# firebase::remote_config::ValueInfo


`#include <remote_config.h>`

Describes a retrieved value.

## Summary

|                                                                                                                                                                                                                  ### Public attributes                                                                                                                                                                                                                  ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [conversion_successful](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/value-info#structfirebase_1_1remote__config_1_1_value_info_1a928a62cf1928dd8cfc1d4175e9570324) | `bool` If `true` this indicates conversion to the requested type succeeded, otherwise conversion failed so the static value for the requested type was retrieved instead.                                                                          |
| [source](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/value-info#structfirebase_1_1remote__config_1_1_value_info_1a472cb3d7f57af12fae1449f43c86e48a)                | [ValueSource](https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#namespacefirebase_1_1remote__config_1a825e9930f665960955ee8c7ae071192f) Where the config value was retrieved from (Default Config or Active Config). |

## Public attributes

### conversion_successful

```c++
bool firebase::remote_config::ValueInfo::conversion_successful
```  
If `true` this indicates conversion to the requested type succeeded, otherwise conversion failed so the static value for the requested type was retrieved instead.  

### source

```c++
ValueSource firebase::remote_config::ValueInfo::source
```  
Where the config value was retrieved from (Default Config or Active Config).