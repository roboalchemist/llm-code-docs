# Source: https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigError.md.txt

# FirebaseRemoteConfig Framework Reference

# FIRRemoteConfigError

    enum FIRRemoteConfigError : NSInteger {}

Firebase Remote Config service fetch error.
- `
  ``
  ``
  `

  ### [FIRRemoteConfigErrorUnknown](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigError#/c:@E@FIRRemoteConfigError@FIRRemoteConfigErrorUnknown)

  `
  `  
  Unknown or no error.  

  #### Declaration

  Objective-C  

      FIRRemoteConfigErrorUnknown = 8001

- `
  ``
  ``
  `

  ### [FIRRemoteConfigErrorThrottled](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigError#/c:@E@FIRRemoteConfigError@FIRRemoteConfigErrorThrottled)

  `
  `  
  Frequency of fetch requests exceeds throttled limit.  

  #### Declaration

  Objective-C  

      FIRRemoteConfigErrorThrottled = 8002

- `
  ``
  ``
  `

  ### [FIRRemoteConfigErrorInternalError](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigError#/c:@E@FIRRemoteConfigError@FIRRemoteConfigErrorInternalError)

  `
  `  
  Internal error that covers all internal HTTP errors.  

  #### Declaration

  Objective-C  

      FIRRemoteConfigErrorInternalError = 8003