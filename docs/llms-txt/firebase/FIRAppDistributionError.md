# Source: https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Enums/FIRAppDistributionError.md.txt

# FirebaseAppDistribution Framework Reference

# FIRAppDistributionError

    enum FIRAppDistributionError : NSInteger {}

Error codes representing sign in or version check failure reasons.
- `
  ``
  ``
  `

  ### [FIRAppDistributionErrorUnknown](https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Enums/FIRAppDistributionError#/c:@E@FIRAppDistributionError@FIRAppDistributionErrorUnknown)

  `
  `  
  Returned when an unknown error occurred.  

  #### Declaration

  Objective-C  

      FIRAppDistributionErrorUnknown = 0

- `
  ``
  ``
  `

  ### [FIRAppDistributionErrorAuthenticationFailure](https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Enums/FIRAppDistributionError#/c:@E@FIRAppDistributionError@FIRAppDistributionErrorAuthenticationFailure)

  `
  `  
  Returned when App Distribution failed to authenticate the user.  

  #### Declaration

  Objective-C  

      FIRAppDistributionErrorAuthenticationFailure = 1

- `
  ``
  ``
  `

  ### [FIRAppDistributionErrorAuthenticationCancelled](https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Enums/FIRAppDistributionError#/c:@E@FIRAppDistributionError@FIRAppDistributionErrorAuthenticationCancelled)

  `
  `  
  Returned when sign-in was cancelled.  

  #### Declaration

  Objective-C  

      FIRAppDistributionErrorAuthenticationCancelled = 2

- `
  ``
  ``
  `

  ### [FIRAppDistributionErrorNetworkFailure](https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Enums/FIRAppDistributionError#/c:@E@FIRAppDistributionError@FIRAppDistributionErrorNetworkFailure)

  `
  `  
  Returned when the network was unavailable to make requests or
  the request timed out.  

  #### Declaration

  Objective-C  

      FIRAppDistributionErrorNetworkFailure = 3