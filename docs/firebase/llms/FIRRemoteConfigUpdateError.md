# Source: https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigUpdateError.md.txt

# FirebaseRemoteConfig Framework Reference

# FIRRemoteConfigUpdateError

    enum FIRRemoteConfigUpdateError : NSInteger {}

Firebase Remote Config real-time config update service error.
- `
  ``
  ``
  `

  ### [FIRRemoteConfigUpdateErrorStreamError](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigUpdateError#/c:@E@FIRRemoteConfigUpdateError@FIRRemoteConfigUpdateErrorStreamError)

  `
  `  
  Unable to make a connection to the Remote Config backend.  

  #### Declaration

  Objective-C  

      FIRRemoteConfigUpdateErrorStreamError = 8001

- `
  ``
  ``
  `

  ### [FIRRemoteConfigUpdateErrorNotFetched](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigUpdateError#/c:@E@FIRRemoteConfigUpdateError@FIRRemoteConfigUpdateErrorNotFetched)

  `
  `  
  Unable to fetch the latest version of the config.  

  #### Declaration

  Objective-C  

      FIRRemoteConfigUpdateErrorNotFetched = 8002

- `
  ``
  ``
  `

  ### [FIRRemoteConfigUpdateErrorMessageInvalid](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigUpdateError#/c:@E@FIRRemoteConfigUpdateError@FIRRemoteConfigUpdateErrorMessageInvalid)

  `
  `  
  The ConfigUpdate message was unparsable.  

  #### Declaration

  Objective-C  

      FIRRemoteConfigUpdateErrorMessageInvalid = 8003

- `
  ``
  ``
  `

  ### [FIRRemoteConfigUpdateErrorUnavailable](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigUpdateError#/c:@E@FIRRemoteConfigUpdateError@FIRRemoteConfigUpdateErrorUnavailable)

  `
  `  
  The Remote Config real-time config update service is unavailable.  

  #### Declaration

  Objective-C  

      FIRRemoteConfigUpdateErrorUnavailable = 8004