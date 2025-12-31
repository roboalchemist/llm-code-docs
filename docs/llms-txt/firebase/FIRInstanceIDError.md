# Source: https://firebase.google.com/docs/reference/ios/firebaseinstanceid/api/reference/Enums/FIRInstanceIDError.md.txt

# FirebaseInstanceID Framework Reference

# FIRInstanceIDError

    enum FIRInstanceIDError {}

Public errors produced by InstanceID.
- `
  ``
  ``
  `

  ### [FIRInstanceIDErrorUnknown](https://firebase.google.com/docs/reference/ios/firebaseinstanceid/api/reference/Enums/FIRInstanceIDError#/c:@E@FIRInstanceIDError@FIRInstanceIDErrorUnknown)

  `
  `  
  Unknown error.  

  #### Declaration

  Objective-C  

      FIRInstanceIDErrorUnknown = 0

- `
  ``
  ``
  `

  ### [FIRInstanceIDErrorAuthentication](https://firebase.google.com/docs/reference/ios/firebaseinstanceid/api/reference/Enums/FIRInstanceIDError#/c:@E@FIRInstanceIDError@FIRInstanceIDErrorAuthentication)

  `
  `  
  Auth Error -- GCM couldn't validate request from this client.  

  #### Declaration

  Objective-C  

      FIRInstanceIDErrorAuthentication = 1

- `
  ``
  ``
  `

  ### [FIRInstanceIDErrorNoAccess](https://firebase.google.com/docs/reference/ios/firebaseinstanceid/api/reference/Enums/FIRInstanceIDError#/c:@E@FIRInstanceIDError@FIRInstanceIDErrorNoAccess)

  `
  `  
  NoAccess -- InstanceID service cannot be accessed.  

  #### Declaration

  Objective-C  

      FIRInstanceIDErrorNoAccess = 2

- `
  ``
  ``
  `

  ### [FIRInstanceIDErrorTimeout](https://firebase.google.com/docs/reference/ios/firebaseinstanceid/api/reference/Enums/FIRInstanceIDError#/c:@E@FIRInstanceIDError@FIRInstanceIDErrorTimeout)

  `
  `  
  Timeout -- Request to InstanceID backend timed out.  

  #### Declaration

  Objective-C  

      FIRInstanceIDErrorTimeout = 3

- `
  ``
  ``
  `

  ### [FIRInstanceIDErrorNetwork](https://firebase.google.com/docs/reference/ios/firebaseinstanceid/api/reference/Enums/FIRInstanceIDError#/c:@E@FIRInstanceIDError@FIRInstanceIDErrorNetwork)

  `
  `  
  Network -- No network available to reach the servers.  

  #### Declaration

  Objective-C  

      FIRInstanceIDErrorNetwork = 4

- `
  ``
  ``
  `

  ### [FIRInstanceIDErrorOperationInProgress](https://firebase.google.com/docs/reference/ios/firebaseinstanceid/api/reference/Enums/FIRInstanceIDError#/c:@E@FIRInstanceIDError@FIRInstanceIDErrorOperationInProgress)

  `
  `  
  OperationInProgress -- Another similar operation in progress,
  bailing this one.  

  #### Declaration

  Objective-C  

      FIRInstanceIDErrorOperationInProgress = 5

- `
  ``
  ``
  `

  ### [FIRInstanceIDErrorInvalidRequest](https://firebase.google.com/docs/reference/ios/firebaseinstanceid/api/reference/Enums/FIRInstanceIDError#/c:@E@FIRInstanceIDError@FIRInstanceIDErrorInvalidRequest)

  `
  `  
  InvalidRequest -- Some parameters of the request were invalid.  

  #### Declaration

  Objective-C  

      FIRInstanceIDErrorInvalidRequest = 7