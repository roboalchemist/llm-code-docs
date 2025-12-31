# Source: https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Enums/FIRMessagingError.md.txt

# FirebaseMessaging Framework Reference

# FIRMessagingError

    enum FIRMessagingError : NSInteger {}

@enum FIRMessagingError
- `
  ``
  ``
  `

  ### [FIRMessagingErrorUnknown](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Enums/FIRMessagingError#/c:@E@FIRMessagingError@FIRMessagingErrorUnknown)

  `
  `  
  Unknown error.  

  #### Declaration

  Objective-C  

      FIRMessagingErrorUnknown = 0

- `
  ``
  ``
  `

  ### [FIRMessagingErrorAuthentication](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Enums/FIRMessagingError#/c:@E@FIRMessagingError@FIRMessagingErrorAuthentication)

  `
  `  
  FIRMessaging couldn't validate request from this client.  

  #### Declaration

  Objective-C  

      FIRMessagingErrorAuthentication = 1

- `
  ``
  ``
  `

  ### [FIRMessagingErrorNoAccess](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Enums/FIRMessagingError#/c:@E@FIRMessagingError@FIRMessagingErrorNoAccess)

  `
  `  
  InstanceID service cannot be accessed.  

  #### Declaration

  Objective-C  

      FIRMessagingErrorNoAccess = 2

- `
  ``
  ``
  `

  ### [FIRMessagingErrorTimeout](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Enums/FIRMessagingError#/c:@E@FIRMessagingError@FIRMessagingErrorTimeout)

  `
  `  
  Request to InstanceID backend timed out.  

  #### Declaration

  Objective-C  

      FIRMessagingErrorTimeout = 3

- `
  ``
  ``
  `

  ### [FIRMessagingErrorNetwork](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Enums/FIRMessagingError#/c:@E@FIRMessagingError@FIRMessagingErrorNetwork)

  `
  `  
  No network available to reach the servers.  

  #### Declaration

  Objective-C  

      FIRMessagingErrorNetwork = 4

- `
  ``
  ``
  `

  ### [FIRMessagingErrorOperationInProgress](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Enums/FIRMessagingError#/c:@E@FIRMessagingError@FIRMessagingErrorOperationInProgress)

  `
  `  
  Another similar operation in progress, bailing this one.  

  #### Declaration

  Objective-C  

      FIRMessagingErrorOperationInProgress = 5

- `
  ``
  ``
  `

  ### [FIRMessagingErrorInvalidRequest](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Enums/FIRMessagingError#/c:@E@FIRMessagingError@FIRMessagingErrorInvalidRequest)

  `
  `  
  Some parameters of the request were invalid.  

  #### Declaration

  Objective-C  

      FIRMessagingErrorInvalidRequest = 7

- `
  ``
  ``
  `

  ### [FIRMessagingErrorInvalidTopicName](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Enums/FIRMessagingError#/c:@E@FIRMessagingError@FIRMessagingErrorInvalidTopicName)

  `
  `  
  Topic name is invalid for subscription/unsubscription.  

  #### Declaration

  Objective-C  

      FIRMessagingErrorInvalidTopicName = 8