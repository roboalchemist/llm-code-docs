# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/tool-config.md.txt

# Firebase.AI.ToolConfig Struct Reference

# Firebase.AI.ToolConfig

[Tool](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/tool#struct_firebase_1_1_a_i_1_1_tool) configuration for any [Tool](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/tool#struct_firebase_1_1_a_i_1_1_tool) specified in the request.

## Summary

| ### Constructors and Destructors ||
|---|---|
| [ToolConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/tool-config#struct_firebase_1_1_a_i_1_1_tool_config_1a99237fa34b4f97f5674f964a1369a580)`(`[FunctionCallingConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/function-calling-config#struct_firebase_1_1_a_i_1_1_function_calling_config)`? functionCallingConfig)` Constructs a new [ToolConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/tool-config#struct_firebase_1_1_a_i_1_1_tool_config). ||

## Public functions

### ToolConfig

```c#
 Firebase::AI::ToolConfig::ToolConfig(
  FunctionCallingConfig? functionCallingConfig
)
```  
Constructs a new [ToolConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/tool-config#struct_firebase_1_1_a_i_1_1_tool_config).

<br />

|                                                                                             Details                                                                                             ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-------------------------|-------------------------------------------------------------| | `functionCallingConfig` | Configures how the model should use the provided functions. | |