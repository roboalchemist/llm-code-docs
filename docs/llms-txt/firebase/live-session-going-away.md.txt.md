# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/live-session-going-away.md.txt

# Firebase.AI.LiveSessionGoingAway Struct Reference

# Firebase.AI.LiveSessionGoingAway

A server message indicating that the server will not be able to service the client soon.

## Summary

### Inheritance

Inherits from: [Firebase.AI.ILiveSessionMessage](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/i-live-session-message)

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/live-session-going-away#struct_firebase_1_1_a_i_1_1_live_session_going_away_1afb01c70633afcd5066d99fce411ce6b4` | `readonly TimeSpan` The remaining time before the connection will be terminated as ABORTED. |

## Properties

### TimeLeft

```c#
readonly TimeSpan Firebase::AI::LiveSessionGoingAway::TimeLeft
```
The remaining time before the connection will be terminated as ABORTED.