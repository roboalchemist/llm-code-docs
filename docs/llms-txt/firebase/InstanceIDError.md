# Source: https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Enums/InstanceIDError.md.txt

# FirebaseInstanceID Framework Reference

# InstanceIDError

    enum InstanceIDError : UInt

Public errors produced by InstanceID.
- `
  ``
  ``
  `

  ### [unknown](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Enums/InstanceIDError#/c:@E@FIRInstanceIDError@FIRInstanceIDErrorUnknown)

  `
  `  
  Unknown error.  

  #### Declaration

  Swift  

      case unknown = 0

- `
  ``
  ``
  `

  ### [authentication](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Enums/InstanceIDError#/c:@E@FIRInstanceIDError@FIRInstanceIDErrorAuthentication)

  `
  `  
  Auth Error -- GCM couldn't validate request from this client.  

  #### Declaration

  Swift  

      case authentication = 1

- `
  ``
  ``
  `

  ### [noAccess](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Enums/InstanceIDError#/c:@E@FIRInstanceIDError@FIRInstanceIDErrorNoAccess)

  `
  `  
  NoAccess -- InstanceID service cannot be accessed.  

  #### Declaration

  Swift  

      case noAccess = 2

- `
  ``
  ``
  `

  ### [timeout](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Enums/InstanceIDError#/c:@E@FIRInstanceIDError@FIRInstanceIDErrorTimeout)

  `
  `  
  Timeout -- Request to InstanceID backend timed out.  

  #### Declaration

  Swift  

      case timeout = 3

- `
  ``
  ``
  `

  ### [network](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Enums/InstanceIDError#/c:@E@FIRInstanceIDError@FIRInstanceIDErrorNetwork)

  `
  `  
  Network -- No network available to reach the servers.  

  #### Declaration

  Swift  

      case network = 4

- `
  ``
  ``
  `

  ### [operationInProgress](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Enums/InstanceIDError#/c:@E@FIRInstanceIDError@FIRInstanceIDErrorOperationInProgress)

  `
  `  
  OperationInProgress -- Another similar operation in progress,
  bailing this one.  

  #### Declaration

  Swift  

      case operationInProgress = 5

- `
  ``
  ``
  `

  ### [invalidRequest](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Enums/InstanceIDError#/c:@E@FIRInstanceIDError@FIRInstanceIDErrorInvalidRequest)

  `
  `  
  InvalidRequest -- Some parameters of the request were invalid.  

  #### Declaration

  Swift  

      case invalidRequest = 7