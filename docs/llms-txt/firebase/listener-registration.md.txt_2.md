# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration.md.txt

# Firebase.Firestore.ListenerRegistration Class Reference

# Firebase.Firestore.ListenerRegistration

Represents a listener for either document or query snapshots that is returned from `Listen` methods.

## Summary

The listener can be removed by calling [ListenerRegistration.Stop](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration#class_firebase_1_1_firestore_1_1_listener_registration_1a6c7f69812ca19b3acfeed3668d9b4655).

### Inheritance

Inherits from: IDisposable

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration#class_firebase_1_1_firestore_1_1_listener_registration_1aafd6719cda4c067ce42429b4c9af55f1` | `Task` A task that will complete when the listen operation finishes. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration#class_firebase_1_1_firestore_1_1_listener_registration_1a4aba914d3acc380ca718ae0a42c9b237()` | `void` Calls the [Stop()](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration#class_firebase_1_1_firestore_1_1_listener_registration_1a6c7f69812ca19b3acfeed3668d9b4655) method. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration#class_firebase_1_1_firestore_1_1_listener_registration_1a6c7f69812ca19b3acfeed3668d9b4655()` | `void` Removes the listener being tracked by this `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration#class_firebase_1_1_firestore_1_1_listener_registration`. |

## Properties

### ListenerTask

```c#
Task ListenerTask
```
A task that will complete when the listen operation finishes.

The task will finish in a state of `TaskStatus.Faulted` if any kind of exception was thrown, including any non-retriable RPC exceptions. The task will finish in a state of `TaskStatus.RanToCompletion"` if the listener stopped gracefully.

## Public functions

### Dispose

```c#
void Dispose()
```
Calls the [Stop()](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration#class_firebase_1_1_firestore_1_1_listener_registration_1a6c7f69812ca19b3acfeed3668d9b4655) method.

Note that this method is *not* invoked by the destructor. This is intentional as this class does not handle unmanaged resources. The usage of the IDisposable interface does however enable using this class with external reactive libraries that expect it.

### Stop

```c#
void Stop()
```
Removes the listener being tracked by this `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration#class_firebase_1_1_firestore_1_1_listener_registration`.

If [ListenerTask](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration#class_firebase_1_1_firestore_1_1_listener_registration_1aafd6719cda4c067ce42429b4c9af55f1) is not completed, then it will transition to the `TaskStatus.RanToCompletion"` state. After the initial call of this method, subsequent calls have no effect.