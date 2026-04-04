# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-value.md.txt

# Firebase.RemoteConfig.ConfigValue Struct Reference

# Firebase.RemoteConfig.ConfigValue

Wrapper for a Remote Config parameter value, with methods to get it as different types, such as bools and doubles, along with information about where the data came from.

## Summary

|                                                                                                                                                                                                       ### Properties                                                                                                                                                                                                       ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [BooleanValue](https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-value#struct_firebase_1_1_remote_config_1_1_config_value_1a5db8544200e2b5f4b3ed0970a6cb0465)   | `bool` Gets the value as a bool.                                                                                                                                                                                      |
| [ByteArrayValue](https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-value#struct_firebase_1_1_remote_config_1_1_config_value_1a607b9243b637d3805d1620e2386e157b) | `System.Collections.Generic.IEnumerable< byte >` Gets the value as an IEnumerable of byte.                                                                                                                            |
| [DoubleValue](https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-value#struct_firebase_1_1_remote_config_1_1_config_value_1a608cce4d1921a2f45d8082db723848bf)    | `double` Gets the value as a double.                                                                                                                                                                                  |
| [LongValue](https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-value#struct_firebase_1_1_remote_config_1_1_config_value_1a87920e3217816b81ae20a964df6a64d1)      | `long` Gets the value as a long.                                                                                                                                                                                      |
| [Source](https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-value#struct_firebase_1_1_remote_config_1_1_config_value_1ad01d2ad869cf5afd2a84902ee7ca5689)         | [ValueSource](https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config#namespace_firebase_1_1_remote_config_1a2f4f400ab2b2d9f09a147439cd0c5ca2) Indicates which source this value came from. |
| [StringValue](https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-value#struct_firebase_1_1_remote_config_1_1_config_value_1a8d1cc34954f656aac89a4f3e6bde5116)    | `string` Gets the value as a string.                                                                                                                                                                                  |

## Properties

### BooleanValue

```c#
bool Firebase::RemoteConfig::ConfigValue::BooleanValue
```  
Gets the value as a bool.

<br />

|                                                                            Details                                                                             ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |--------------------------|-------------------------------------------| | `System.FormatException` | if the data fails be converted to a bool. | |
| **Returns** | Bool representation of this parameter value.                                                                                                      |

### ByteArrayValue

```c#
System.Collections.Generic.IEnumerable< byte > Firebase::RemoteConfig::ConfigValue::ByteArrayValue
```  
Gets the value as an IEnumerable of byte.

<br />

|                                 Details                                  ||
|-------------|-------------------------------------------------------------|
| **Returns** | IEnumerable of byte representation of this parameter value. |

### DoubleValue

```c#
double Firebase::RemoteConfig::ConfigValue::DoubleValue
```  
Gets the value as a double.

<br />

|                                                                              Details                                                                               ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |--------------------------|---------------------------------------------| | `System.FormatException` | if the data fails be converted to a double. | |
| **Returns** | Double representation of this parameter value.                                                                                                        |

### LongValue

```c#
long Firebase::RemoteConfig::ConfigValue::LongValue
```  
Gets the value as a long.

<br />

|                                                                            Details                                                                             ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |--------------------------|-------------------------------------------| | `System.FormatException` | if the data fails be converted to a long. | |
| **Returns** | Long representation of this parameter value.                                                                                                      |

### Source

```c#
ValueSource Firebase::RemoteConfig::ConfigValue::Source
```  
Indicates which source this value came from.

<br />

|                                                                    Details                                                                     ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The ValueSource corresponding to where the value came from, either the server, the default value provided, or static, if neither. |

### StringValue

```c#
string Firebase::RemoteConfig::ConfigValue::StringValue
```  
Gets the value as a string.

<br />

|                           Details                           ||
|-------------|------------------------------------------------|
| **Returns** | String representation of this parameter value. |