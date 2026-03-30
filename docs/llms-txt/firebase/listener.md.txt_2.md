# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener.md.txt

# firebase::messaging::Listener Class Reference

# firebase::messaging::Listener


**This is an abstract class.**


`#include <messaging.h>`

Base class used to receive messages from Firebase Cloud Messaging.

## Summary

You need to override base class methods to handle any events required by the application. Methods are invoked asynchronously and may be invoked on other threads.

### Inheritance

Direct Known Subclasses:[firebase::messaging::PollableListener](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/pollable-listener)

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener#classfirebase_1_1messaging_1_1_listener_1a7e1b2e00cec0379538ad9c63a568e8fa()` ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener#classfirebase_1_1messaging_1_1_listener_1a074808bae034dd30ba1e7756ca196281(const https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message & message)=0` | `virtual void` Called on the client when a message arrives. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener#classfirebase_1_1messaging_1_1_listener_1a837d52cfb06e12c85d4df06583567eed(const char *token)=0` | `virtual void` Called on the client when a registration token arrives. |

## Public functions

### OnMessage

```c++
virtual void OnMessage(
  const Message & message
)=0
```
Called on the client when a message arrives.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `message` | The data describing this message. | |

### OnTokenReceived

```c++
virtual void OnTokenReceived(
  const char *token
)=0
```
Called on the client when a registration token arrives.

This function will eventually be called in response to a call to [firebase::messaging::Initialize](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a5e3bd7545d50f7877ce9f72909718750)(...).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `token` | The registration token. | |

### \~Listener

```c++
virtual  ~Listener()
```