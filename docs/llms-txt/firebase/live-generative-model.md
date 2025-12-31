# Source: https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-generative-model.md.txt

# Firebase.AI.LiveGenerativeModel Class Reference

# Firebase.AI.LiveGenerativeModel

A live, generative [AI](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i) model for real-time interaction.

## Summary

See the [Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/multimodal-live) for more details about the low-latency, two-way interactions that use text, audio, and video input, with audio and text output.

Warning: For [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[AI](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i), Live Model is in Public Preview, which means that the feature is not subject to any SLA or deprecation policy and could change in backwards-incompatible ways.

|                                                                                                                                                                                                                  ### Public functions                                                                                                                                                                                                                  ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ConnectAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-generative-model#class_firebase_1_1_a_i_1_1_live_generative_model_1a0acbda92cb861ccfb0907818fbbe6ed0)`(CancellationToken cancellationToken)` | `async Task< `[LiveSession](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-session#class_firebase_1_1_a_i_1_1_live_session)` >` Establishes a connection to a live generation service. |

## Public functions

### ConnectAsync

```c#
async Task< LiveSession > ConnectAsync(
  CancellationToken cancellationToken
)
```  
Establishes a connection to a live generation service.

This function handles the WebSocket connection setup and returns an [LiveSession](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-session#class_firebase_1_1_a_i_1_1_live_session) object that can be used to communicate with the service.

<br />

|                                                                                               Details                                                                                                ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|-------------------------------------------------------------------| | `cancellationToken` | The token that can be used to cancel the creation of the session. | |
| **Returns** | The [LiveSession](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-session#class_firebase_1_1_a_i_1_1_live_session), once it is established.                    |