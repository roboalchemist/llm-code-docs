# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/live-session-response.md.txt

# Firebase.AI.LiveSessionResponse Struct Reference

# Firebase.AI.LiveSessionResponse

Represents the response from the model for live content updates.

## Summary

|                                                                                                                                                                                                           ### Properties                                                                                                                                                                                                            ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Audio](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/live-session-response#struct_firebase_1_1_a_i_1_1_live_session_response_1a91a87e93668e8b1f5c6255d601ee7969)        | `IReadOnlyList< byte[]>` The response's content that was audio, if it exists.                                                                                                                                                      |
| [AudioAsFloat](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/live-session-response#struct_firebase_1_1_a_i_1_1_live_session_response_1ad85519e424827e9065bf0eb5d8e354aa) | `IReadOnlyList< float[]>` The response's content that was audio, if it exists, converted into floats.                                                                                                                              |
| [Message](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/live-session-response#struct_firebase_1_1_a_i_1_1_live_session_response_1aa412e5542d81993faceeae5421ac8cb8)      | `readonly `[ILiveSessionMessage](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/i-live-session-message#interface_firebase_1_1_a_i_1_1_i_live_session_message) The detailed message from the live session. |
| [Text](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/live-session-response#struct_firebase_1_1_a_i_1_1_live_session_response_1a4363b805a08d0a07e8b0730cfec87321)         | `string` The response's content as text, if it exists.                                                                                                                                                                             |

## Properties

### Audio

```c#
IReadOnlyList< byte[]> Firebase::AI::LiveSessionResponse::Audio
```  
The response's content that was audio, if it exists.  

### AudioAsFloat

```c#
IReadOnlyList< float[]> Firebase::AI::LiveSessionResponse::AudioAsFloat
```  
The response's content that was audio, if it exists, converted into floats.  

### Message

```c#
readonly ILiveSessionMessage Firebase::AI::LiveSessionResponse::Message
```  
The detailed message from the live session.  

### Text

```c#
string Firebase::AI::LiveSessionResponse::Text
```  
The response's content as text, if it exists.