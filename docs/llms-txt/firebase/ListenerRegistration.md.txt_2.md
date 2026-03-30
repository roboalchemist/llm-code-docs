# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/ListenerRegistration.md.txt

# FirebaseFirestore Framework Reference

# ListenerRegistration

    protocol ListenerRegistration : NSObjectProtocol

Represents a listener that can be removed by calling remove.
- `


  ### [remove()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/ListenerRegistration#/c:objc(pl)FIRListenerRegistration(im)remove)


  ` Removes the listener being tracked by this `ListenerRegistration`. After the initial call,
  subsequent calls have no effect.

  #### Declaration

  Swift

      func remove()