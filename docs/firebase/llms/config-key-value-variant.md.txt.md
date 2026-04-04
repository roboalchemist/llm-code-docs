# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-key-value-variant.md.txt

# firebase::remote_config::ConfigKeyValueVariant Struct Reference

# firebase::remote_config::ConfigKeyValueVariant


`#include <remote_config.h>`

Describes a mapping of a key to a value of any type.

## Summary

Used to set default values.

| ### Public attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-key-value-variant#structfirebase_1_1remote__config_1_1_config_key_value_variant_1adf662c70b581975139c77964dabe7073` | `const char *` The lookup key string. |
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-key-value-variant#structfirebase_1_1remote__config_1_1_config_key_value_variant_1a706397e732b5f14be5927b01c7b2092e` | `https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant` The value to be stored. |

## Public attributes

### key

```c++
const char * firebase::remote_config::ConfigKeyValueVariant::key
```
The lookup key string.


> [!NOTE]
> **Note:** Ensure this string stays valid for the duration of the call to SetDefaults.

<br />

### value

```c++
Variant firebase::remote_config::ConfigKeyValueVariant::value
```
The value to be stored.

The type of the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) determines the type of default data for the given key.


> [!NOTE]
> **Note:** If you use a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of type StaticString, ensure it stays valid for the duration of the call to SetDefaults.

<br />