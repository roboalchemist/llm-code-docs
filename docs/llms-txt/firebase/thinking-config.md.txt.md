# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/thinking-config.md.txt

# Firebase.AI.ThinkingConfig Struct Reference

# Firebase.AI.ThinkingConfig

Configuration options for Thinking features.

## Summary

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/thinking-config#struct_firebase_1_1_a_i_1_1_thinking_config_1a3bc4db652d93e066efa3514ddf0b505c(int? thinkingBudget, bool? includeThoughts)` Initializes configuration options for Thinking features. ||
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/thinking-config#struct_firebase_1_1_a_i_1_1_thinking_config_1ae37552731a61d9ee9680d859e5f79623(https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/thinking-config#struct_firebase_1_1_a_i_1_1_thinking_config_1a9e82fe2f29a0cd35fed26769732776ec thinkingLevel, bool? includeThoughts)` Initializes configuration options for Thinking features with a given ThinkingLevel. ||

| ### Public types ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/thinking-config#struct_firebase_1_1_a_i_1_1_thinking_config_1a9e82fe2f29a0cd35fed26769732776ec{ https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/thinking-config#struct_firebase_1_1_a_i_1_1_thinking_config_1a9e82fe2f29a0cd35fed26769732776eca30fc6bbba82125243ecf4ddb27fee645, https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/thinking-config#struct_firebase_1_1_a_i_1_1_thinking_config_1a9e82fe2f29a0cd35fed26769732776eca28d0edd045e05cf5af64e35ae0c4c6ef, https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/thinking-config#struct_firebase_1_1_a_i_1_1_thinking_config_1a9e82fe2f29a0cd35fed26769732776eca87f8a6ab85c9ced3702b4ea641ad4bb5, https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/thinking-config#struct_firebase_1_1_a_i_1_1_thinking_config_1a9e82fe2f29a0cd35fed26769732776eca655d20c1ca69519ca647684edbb2db35 }` | enumA preset that balances the trade-off between reasoning quality and response speed for a model's "thinking" process. |

## Public types

### ThinkingLevel

```c#
 Firebase::AI::ThinkingConfig::ThinkingLevel
```
A preset that balances the trade-off between reasoning quality and response speed for a model's "thinking" process.

Note, not all models support every level.

| Properties ||
|---|---|
| `High` | Maximizes reasoning depth. |
| `Low` | Minimizes latency and cost. |
| `Medium` | Balanced thinking for most tasks. |
| `Minimal` | Matches the "no thinking" setting for most queries. |

## Public functions

### ThinkingConfig

```c#
 Firebase::AI::ThinkingConfig::ThinkingConfig(
  int? thinkingBudget,
  bool? includeThoughts
)
```
Initializes configuration options for Thinking features.

Used for Gemini models 2.5 and earlier.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `thinkingBudget` | The token budget for the model's thinking process. | | `includeThoughts` | If true, summaries of the model's "thoughts" are included in responses. | |

### ThinkingConfig

```c#
 Firebase::AI::ThinkingConfig::ThinkingConfig(
  ThinkingLevel thinkingLevel,
  bool? includeThoughts
)
```
Initializes configuration options for Thinking features with a given ThinkingLevel.

Used for Gemini models 3.0 and newer. See <https://ai.google.dev/gemini-api/docs/thinking#thinking-levels>

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `thinkingLevel` | Defines the model's thinking process. | | `includeThoughts` | If true, summaries of the model's "thoughts" are included in responses. | |