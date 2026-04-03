# Source: https://firebase.google.com/docs/reference/unity/class/firebase/messaging/token-received-event-args.md.txt

# Firebase.Messaging.TokenReceivedEventArgs Class Reference

# Firebase.Messaging.TokenReceivedEventArgs

Token argument for the TokenReceived event containing the token string.

## Summary

### Inheritance

Inherits from: EventArgs

| ### Constructors and Destructors ||
|---|---|
| [TokenReceivedEventArgs](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/token-received-event-args#class_firebase_1_1_messaging_1_1_token_received_event_args_1aa0b02dea7b181f762cc4ec942d17dce8)`(string token)` ||

|                                                                                                                                       ### Properties                                                                                                                                       ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [Token](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/token-received-event-args#class_firebase_1_1_messaging_1_1_token_received_event_args_1aecd92b911214c629be6e47367b759bd1) | `string` An identity token string provided by the TokenReceived event handler. |

## Properties

### Token

```c#
string Token
```  
An identity token string provided by the TokenReceived event handler.

## Public functions

### TokenReceivedEventArgs

```c#
 TokenReceivedEventArgs(
  string token
)
```