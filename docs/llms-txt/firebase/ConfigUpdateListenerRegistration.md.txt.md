# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdateListenerRegistration.md.txt

# ConfigUpdateListenerRegistration

# ConfigUpdateListenerRegistration


```
public interface ConfigUpdateListenerRegistration
```

<br />

*** ** * ** ***

Listener registration returned by `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#addOnConfigUpdateListener(com.google.firebase.remoteconfig.ConfigUpdateListener)`.

Calling `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdateListenerRegistration#remove()` stops the listener from receiving config updates and unregisters itself. If remove is called and no other listener registrations remain, the connection to the Remote Config backend is closed. Subsequently calling `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#addOnConfigUpdateListener(com.google.firebase.remoteconfig.ConfigUpdateListener)` will re-open the connection.

## Summary

| ### Public methods |
|---|---|
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdateListenerRegistration#remove()()` Removes the listener being tracked by this `ConfigUpdateListenerRegistration`. |

## Public methods

### remove

```
abstract void remove()
```

Removes the listener being tracked by this `ConfigUpdateListenerRegistration`. After the initial call, subsequent calls to `remove()` have no effect.