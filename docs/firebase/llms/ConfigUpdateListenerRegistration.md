# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListenerRegistration.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdateListenerRegistration.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/ConfigUpdateListenerRegistration.md.txt

# FirebaseRemoteConfig Framework Reference

# ConfigUpdateListenerRegistration

    class ConfigUpdateListenerRegistration : NSObject, @unchecked Sendable

Listener registration returned by `addOnConfigUpdateListener`. Calling its method `remove` stops
the associated listener from receiving config updates and unregisters itself.

If remove is called and no other listener registrations remain, the connection to the real-time
RC backend is closed. Subsequently calling `addOnConfigUpdateListener` will re-open the
connection.
- `
  ``
  ``
  `

  ### [remove()](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/ConfigUpdateListenerRegistration#/c:objc(cs)FIRConfigUpdateListenerRegistration(im)remove)

  `
  `  
  Removes the listener associated with this `ConfigUpdateListenerRegistration`. After the
  initial call, subsequent calls have no effect.  

  #### Declaration

  Swift  

      func remove()