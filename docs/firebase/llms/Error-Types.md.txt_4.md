# Source: https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Enums/Error-Types.md.txt

# FirebaseMessaging Framework Reference

# _ErrorType

    typealias MessagingError.Code._ErrorType = MessagingError

@enum FIRMessagingError
- `


  ### [unknown](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Enums/Error-Types#/c:@E@FIRMessagingError@FIRMessagingErrorUnknown)


  ` Unknown error.

  #### Declaration

  Swift

      static var unknown: MessagingError.Code { get }

- `


  ### [authentication](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Enums/Error-Types#/c:@E@FIRMessagingError@FIRMessagingErrorAuthentication)


  ` FIRMessaging couldn't validate request from this client.

  #### Declaration

  Swift

      static var authentication: MessagingError.Code { get }

- `


  ### [noAccess](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Enums/Error-Types#/c:@E@FIRMessagingError@FIRMessagingErrorNoAccess)


  ` InstanceID service cannot be accessed.

  #### Declaration

  Swift

      static var noAccess: MessagingError.Code { get }

- `


  ### [timeout](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Enums/Error-Types#/c:@E@FIRMessagingError@FIRMessagingErrorTimeout)


  ` Request to InstanceID backend timed out.

  #### Declaration

  Swift

      static var timeout: MessagingError.Code { get }

- `


  ### [network](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Enums/Error-Types#/c:@E@FIRMessagingError@FIRMessagingErrorNetwork)


  ` No network available to reach the servers.

  #### Declaration

  Swift

      static var network: MessagingError.Code { get }

- `


  ### [operationInProgress](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Enums/Error-Types#/c:@E@FIRMessagingError@FIRMessagingErrorOperationInProgress)


  ` Another similar operation in progress, bailing this one.

  #### Declaration

  Swift

      static var operationInProgress: MessagingError.Code { get }

- `


  ### [invalidRequest](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Enums/Error-Types#/c:@E@FIRMessagingError@FIRMessagingErrorInvalidRequest)


  ` Some parameters of the request were invalid.

  #### Declaration

  Swift

      static var invalidRequest: MessagingError.Code { get }

- `


  ### [invalidTopicName](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Enums/Error-Types#/c:@E@FIRMessagingError@FIRMessagingErrorInvalidTopicName)


  ` Topic name is invalid for subscription/unsubscription.

  #### Declaration

  Swift

      static var invalidTopicName: MessagingError.Code { get }