# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/function-calling-config.md.txt

# Firebase.AI.FunctionCallingConfig Struct Reference

# Firebase.AI.FunctionCallingConfig

Configuration for specifying function calling behavior.

## Summary

|                                                                                                                                                                                                                                         ### Public static functions                                                                                                                                                                                                                                         ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Any](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/function-calling-config#struct_firebase_1_1_a_i_1_1_function_calling_config_1a2749cd6ca620fc829aedcd5e93d6e0fb)`(params string[] allowedFunctionNames)`       | [FunctionCallingConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/function-calling-config#struct_firebase_1_1_a_i_1_1_function_calling_config) Creates a function calling config where the model will always call a provided function. |
| [Any](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/function-calling-config#struct_firebase_1_1_a_i_1_1_function_calling_config_1ae0ca8076faf5925afe4d556d7bf9f724)`(IEnumerable< string > allowedFunctionNames)` | [FunctionCallingConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/function-calling-config#struct_firebase_1_1_a_i_1_1_function_calling_config) Creates a function calling config where the model will always call a provided function. |
| [Auto](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/function-calling-config#struct_firebase_1_1_a_i_1_1_function_calling_config_1a9b4d453b301c85777a00cc2195677170)`()`                                          | [FunctionCallingConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/function-calling-config#struct_firebase_1_1_a_i_1_1_function_calling_config) Creates a function calling config where the model calls functions at its discretion.    |
| [None](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/function-calling-config#struct_firebase_1_1_a_i_1_1_function_calling_config_1ae87f4a3414d43dadc7311a72b29e4041)`()`                                          | [FunctionCallingConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/function-calling-config#struct_firebase_1_1_a_i_1_1_function_calling_config) Creates a function calling config where the model will never call a function.           |

## Public static functions

### Any

```c#
FunctionCallingConfig Firebase::AI::FunctionCallingConfig::Any(
  params string[] allowedFunctionNames
)
```  
Creates a function calling config where the model will always call a provided function.

<br />

|                                                                                                                           Details                                                                                                                           ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------------------|--------------------------------------------------------------------------------------------| | `allowedFunctionNames` | A set of function names that, when provided, limits the function that the model will call. | |

### Any

```c#
FunctionCallingConfig Firebase::AI::FunctionCallingConfig::Any(
  IEnumerable< string > allowedFunctionNames
)
```  
Creates a function calling config where the model will always call a provided function.

<br />

|                                                                                                                           Details                                                                                                                           ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------------------|--------------------------------------------------------------------------------------------| | `allowedFunctionNames` | A set of function names that, when provided, limits the function that the model will call. | |

### Auto

```c#
FunctionCallingConfig Firebase::AI::FunctionCallingConfig::Auto()
```  
Creates a function calling config where the model calls functions at its discretion.

Note: This is the default behavior.  

### None

```c#
FunctionCallingConfig Firebase::AI::FunctionCallingConfig::None()
```  
Creates a function calling config where the model will never call a function.

Note: This can also be achieved by not passing any [FunctionDeclaration](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/function-declaration#struct_firebase_1_1_a_i_1_1_function_declaration) tools when instantiating the model.