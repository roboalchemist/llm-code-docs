# Source: https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Enums/Error-Types.md.txt

# FirebaseAppDistribution Framework Reference

# _ErrorType

    typealias AppDistributionError.Code._ErrorType = AppDistributionError

Error codes representing sign in or version check failure reasons.
- `


  ### [unknown](https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Enums/Error-Types#/c:@E@FIRAppDistributionError@FIRAppDistributionErrorUnknown)


  ` Returned when an unknown error occurred.

  #### Declaration

  Swift

      case unknown = 0

- `


  ### [authenticationFailure](https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Enums/Error-Types#/c:@E@FIRAppDistributionError@FIRAppDistributionErrorAuthenticationFailure)


  ` Returned when App Distribution failed to authenticate the user.

  #### Declaration

  Swift

      case authenticationFailure = 1

- `


  ### [authenticationCancelled](https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Enums/Error-Types#/c:@E@FIRAppDistributionError@FIRAppDistributionErrorAuthenticationCancelled)


  ` Returned when sign-in was cancelled.

  #### Declaration

  Swift

      case authenticationCancelled = 2

- `


  ### [networkFailure](https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Enums/Error-Types#/c:@E@FIRAppDistributionError@FIRAppDistributionErrorNetworkFailure)


  ` Returned when the network was unavailable to make requests or
  the request timed out.

  #### Declaration

  Swift

      case networkFailure = 3