# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/thinking-config.md.txt

# Firebase.AI.ThinkingConfig Struct Reference

# Firebase.AI.ThinkingConfig

Configuration options for Thinking features.

## Summary

| ### Constructors and Destructors ||
|---|---|
| [ThinkingConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/thinking-config#struct_firebase_1_1_a_i_1_1_thinking_config_1a3bc4db652d93e066efa3514ddf0b505c)`(int? thinkingBudget, bool? includeThoughts)` Initializes configuration options for Thinking features. ||

## Public functions

### ThinkingConfig

```c#
 Firebase::AI::ThinkingConfig::ThinkingConfig(
  int? thinkingBudget,
  bool? includeThoughts
)
```  
Initializes configuration options for Thinking features.

<br />

|                                                                                                                                                   Details                                                                                                                                                   ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-------------------|-------------------------------------------------------------------------| | `thinkingBudget`  | The token budget for the model's thinking process.                      | | `includeThoughts` | If true, summaries of the model's "thoughts" are included in responses. | |