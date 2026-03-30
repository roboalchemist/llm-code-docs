# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/live-session-tool-call.md.txt

# Firebase.AI.LiveSessionToolCall Struct Reference

# Firebase.AI.LiveSessionToolCall

A request to use a tool from the live session.

## Summary

### Inheritance

Inherits from: [Firebase.AI.ILiveSessionMessage](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/i-live-session-message)

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/live-session-tool-call#struct_firebase_1_1_a_i_1_1_live_session_tool_call_1a2cfe2eef4f39134d31789441b6953895` | `IReadOnlyList< https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-call-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_call_part >` A list of `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-call-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_call_part` included in the response, if any. |

## Properties

### FunctionCalls

```c#
IReadOnlyList< ModelContent.FunctionCallPart > Firebase::AI::LiveSessionToolCall::FunctionCalls
```
A list of `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-call-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_call_part` included in the response, if any.

This will be empty if no function calls are present.