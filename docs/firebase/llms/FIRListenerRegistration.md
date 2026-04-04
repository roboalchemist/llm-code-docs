# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols/FIRListenerRegistration.md.txt

# FirebaseFirestore Framework Reference

# FIRListenerRegistration

    @protocol FIRListenerRegistration <NSObject>

Represents a listener that can be removed by calling remove.
- `
  ``
  ``
  `

  ### [-remove](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols/FIRListenerRegistration#/c:objc(pl)FIRListenerRegistration(im)remove)

  `
  `  
  Removes the listener being tracked by this `ListenerRegistration`. After the initial call,
  subsequent calls have no effect.  

  #### Declaration

  Objective-C  

      - (void)remove;