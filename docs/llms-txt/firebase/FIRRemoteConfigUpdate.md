# Source: https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigUpdate.md.txt

# FirebaseRemoteConfig Framework Reference

# FIRRemoteConfigUpdate


    @interface FIRRemoteConfigUpdate : NSObject

Used by Remote Config real-time config update service, this class represents changes between the
newly fetched config and the current one. An instance of this class is passed to
[FIRRemoteConfigUpdateCompletion](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Type-Definitions.html#/c:FIRRemoteConfig.h@T@FIRRemoteConfigUpdateCompletion) when a new config version has been automatically fetched.
- `
  ``
  ``
  `

  ### [updatedKeys](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigUpdate#/c:objc(cs)FIRRemoteConfigUpdate(py)updatedKeys)

  `
  `  
  Parameter keys whose values have been updated from the currently activated values. Includes
  keys that are added, deleted, and whose value, value source, or metadata has changed.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nonnull) NSSet<NSString *> *updatedKeys;