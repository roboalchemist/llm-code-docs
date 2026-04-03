# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/pollable-listener.md.txt

# firebase::messaging::PollableListener Class Reference

# firebase::messaging::PollableListener


`#include <messaging.h>`

A listener that can be polled to consume pending [Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message)s.

## Summary

This class is intended to be used with applications that have a main loop that frequently updates, such as in the case of a game that has a main loop that updates 30 to 60 times a second. Rather than respond to incoming messages and tokens via the `OnMessage` virtual function, this class will queue up the message internally in a thread-safe manner so that it can be consumed with `PollMessage`. For example:  

```c++
::firebase::messaging::PollableListener listener;
::firebase::messaging::Initialize(app, &listener);

while (true) {
  std::string token;
  if (listener.PollRegistrationToken(&token)) {
    LogMessage("Received a registration token");
  }

  ::firebase::messaging::Message message;
  while (listener.PollMessage(&message)) {
    LogMessage("Received a new message");
  }

  // Remainder of application logic...
}  
```

<br />

### Inheritance

Inherits from: [firebase::messaging::Listener](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener)

| ### Constructors and Destructors ||
|---|---|
| [PollableListener](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/pollable-listener#classfirebase_1_1messaging_1_1_pollable_listener_1aada54b5d624c0593b2521ba0a12231af)`()` The default constructor. ||
| [~PollableListener](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/pollable-listener#classfirebase_1_1messaging_1_1_pollable_listener_1a5a43c4b5802989eab4081bf513d09c6a)`()` The required virtual destructor. ||

|                                                                                                                                                                                                                                           ### Public functions                                                                                                                                                                                                                                            ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [OnMessage](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/pollable-listener#classfirebase_1_1messaging_1_1_pollable_listener_1aeb924594f29e81b9e90eafc450b9813e)`(const `[Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message)` & message)` | `virtual void` An implementation of `OnMessage` which adds the incoming messages to a queue, which can be consumed by calling `PollMessage`.         |
| [OnTokenReceived](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/pollable-listener#classfirebase_1_1messaging_1_1_pollable_listener_1acdd9f0597ba7687863bab94d9867f95f)`(const char *token)`                                                                                                                               | `virtual void` An implementation of `OnTokenReceived` which stores the incoming token so that it can be consumed by calling `PollRegistrationToken`. |
| [PollMessage](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/pollable-listener#classfirebase_1_1messaging_1_1_pollable_listener_1a9ad784d05e512afb638be6081c9df3f5)`(`[Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message)` *message)`      | `bool` Returns the first message queued up, if any.                                                                                                  |
| [PollRegistrationToken](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/pollable-listener#classfirebase_1_1messaging_1_1_pollable_listener_1a39915cdfda32fc52e7930288ddaac202)`(std::string *token)`                                                                                                                        | `bool` Returns the registration key, if a new one has been received.                                                                                 |

## Public functions

### OnMessage

```c++
virtual void OnMessage(
  const Message & message
)
```  
An implementation of `OnMessage` which adds the incoming messages to a queue, which can be consumed by calling `PollMessage`.  

### OnTokenReceived

```c++
virtual void OnTokenReceived(
  const char *token
)
```  
An implementation of `OnTokenReceived` which stores the incoming token so that it can be consumed by calling `PollRegistrationToken`.  

### PollMessage

```c++
bool PollMessage(
  Message *message
)
```  
Returns the first message queued up, if any.

If one or more messages has been received, the first message in the queue will be popped and used to populate the `message` argument and the function will return `true`. If there are no pending messages, `false` is returned. This function should be called in a loop until all messages have been consumed, like so:  

```c++
::firebase::messaging::Message message;
while (listener.PollMessage(&message)) {
  LogMessage("Received a new message");
}
```

<br />

<br />

|                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                  ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `message` | The [Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message) struct to be populated. If there were no pending messages, `message` is not modified. | |
| **Returns** | Returns `true` if there was a pending message, `false` otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                           |

### PollRegistrationToken

```c++
bool PollRegistrationToken(
  std::string *token
)
```  
Returns the registration key, if a new one has been received.

When a new registration token is received, it is cached internally and can be retrieved by calling `PollRegistrationToken`. The cached registration token will be used to populate the `token` argument, then the cache will be cleared and the function will return `true`. If there is no cached registration token this function retuns `false`.  

```c++
std::string token;
if (listener.PollRegistrationToken(&token)) {
  LogMessage("Received a registration token");
}
```

<br />

<br />

|                                                                                                                                                  Details                                                                                                                                                   ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|----------------------------------------------------------------------------------------------------------------------------------| | `token` | A string to be populated with the new token if one has been received. If there were no new token, the string is left unmodified. | |
| **Returns** | Returns `true` if there was a new token, `false` otherwise.                                                                                                                                                                                                                                   |

### PollableListener

```c++
 PollableListener()
```  
The default constructor.  

### \~PollableListener

```c++
virtual  ~PollableListener()
```  
The required virtual destructor.