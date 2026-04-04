# Source: https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRConfigUpdateListenerRegistration.md.txt

# FirebaseRemoteConfig Framework Reference

# FIRConfigUpdateListenerRegistration


    @interface FIRConfigUpdateListenerRegistration : NSObject

Listener registration returned by `addOnConfigUpdateListener`. Calling its method `remove` stops
the associated listener from receiving config updates and unregisters itself.

If remove is called and no other listener registrations remain, the connection to the real-time
RC backend is closed. Subsequently calling `addOnConfigUpdateListener` will re-open the
connection.
- `
  ``
  ``
  `

  ### [-remove](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRConfigUpdateListenerRegistration#/c:objc(cs)FIRConfigUpdateListenerRegistration(im)remove)

  `
  `  
  Removes the listener associated with this `ConfigUpdateListenerRegistration`. After the
  initial call, subsequent calls have no effect.  

  #### Declaration

  Objective-C  

      - (void)remove;