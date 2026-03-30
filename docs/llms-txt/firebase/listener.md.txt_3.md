# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/storage/listener.md.txt

# firebase::storage::Listener Class Reference

# firebase::storage::Listener


**This is an abstract class.**


`#include <listener.h>`

Base class used to receive pause and progress events on a running read or write operation.

## Summary

Subclasses of this listener class can be used to receive events about data transfer progress a location. Attach the listener to a location using [StorageReference::GetBytes()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a900b03399d3d879771d241cd70d455ff), [StorageReference::GetFile()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a2909f324048c6e74c11d699b7c33fb9e), [StorageReference::PutBytes()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1af31e70df99a05baec43a785ccffa78c0), and [StorageReference::PutFile()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1aaea029ebb63c744f6f6c1623e25af4f5); then [OnPaused()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/listener#classfirebase_1_1storage_1_1_listener_1a002fd09bad9d749588407387bc7a0527) will be called whenever the Read or Write operation is paused, and [OnProgress()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/listener#classfirebase_1_1storage_1_1_listener_1a3049e5cceb71b018b34d9170e4948fef) will be called periodically as the transfer makes progress.

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/listener#classfirebase_1_1storage_1_1_listener_1aaf899da3515aaf98a7904aab8f192d0b()` Constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/listener#classfirebase_1_1storage_1_1_listener_1a470eaf355a19303357da7472e9eb05a5()` Virtual destructor. ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/listener#classfirebase_1_1storage_1_1_listener_1a002fd09bad9d749588407387bc7a0527(https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller *controller)=0` | `virtual void` The operation was paused. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/listener#classfirebase_1_1storage_1_1_listener_1a3049e5cceb71b018b34d9170e4948fef(https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller *controller)=0` | `virtual void` There has been progress event. |

## Public functions

### Listener

```c++
 Listener()
```
Constructor.

### OnPaused

```c++
virtual void OnPaused(
  Controller *controller
)=0
```
The operation was paused.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `controller` | A controller that can be used to check the status and make changes to the ongoing operation. | |

### OnProgress

```c++
virtual void OnProgress(
  Controller *controller
)=0
```
There has been progress event.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `controller` | A controller that can be used to check the status and make changes to the ongoing operation. | |

### \~Listener

```c++
virtual  ~Listener()
```
Virtual destructor.