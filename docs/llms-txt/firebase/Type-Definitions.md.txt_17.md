# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions.md.txt

# FirebaseAuth Framework Reference

# Type Definitions

The following type definitions are available globally.
- `


  ### [FIRUserUpdateCallback](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions#/c:FIRAuth.h@T@FIRUserUpdateCallback)


  ` @typedef FIRUserUpdateCallback
  @brief The type of block invoked when a request to update the current user is completed.
- `


  ### [AuthStateDidChangeListenerHandle](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions#/c:FIRAuth.h@T@FIRAuthStateDidChangeListenerHandle)


  ` @typedef FIRAuthStateDidChangeListenerHandle
  @brief The type of handle returned by `Auth.addAuthStateDidChangeListener(_:)`.

  #### Declaration

  Swift

      typealias AuthStateDidChangeListenerHandle = any NSObjectProtocol

- `


  ### [FIRAuthStateDidChangeListenerBlock](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions#/c:FIRAuth.h@T@FIRAuthStateDidChangeListenerBlock)


  ` @typedef FIRAuthStateDidChangeListenerBlock
  @brief The type of block which can be registered as a listener for auth state did change events.

      - parameter: auth The Auth object on which state changes occurred.
      - parameter: user Optionally; the current signed in user, if any.

- `


  ### [IDTokenDidChangeListenerHandle](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions#/c:FIRAuth.h@T@FIRIDTokenDidChangeListenerHandle)


  ` @typedef FIRIDTokenDidChangeListenerHandle
  @brief The type of handle returned by `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)addIDTokenDidChangeListener:`.

  #### Declaration

  Swift

      typealias IDTokenDidChangeListenerHandle = any NSObjectProtocol

- `


  ### [FIRIDTokenDidChangeListenerBlock](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions#/c:FIRAuth.h@T@FIRIDTokenDidChangeListenerBlock)


  ` @typedef FIRIDTokenDidChangeListenerBlock
  @brief The type of block which can be registered as a listener for ID token did change events.

      - parameter: auth The Auth object on which ID token changes occurred.
      - parameter: user Optionally; the current signed in user, if any.

- `


  ### [FIRAuthDataResultCallback](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions#/c:FIRAuth.h@T@FIRAuthDataResultCallback)


  ` @typedef FIRAuthDataResultCallback
  @brief The type of block invoked when sign-in related events complete.

      - parameter: authResult Optionally; Result of sign-in request containing both the user and
         the additional user info associated with the user.
      - parameter: error Optionally; the error which occurred - or nil if the request was successful.

- `


  ### [FIRAuthResultCallback](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions#/c:FIRAuth.h@T@FIRAuthResultCallback)


  ` @typedef FIRAuthResultCallback
  @brief The type of block invoked when sign-in related events complete.

      - parameter: user Optionally; the signed in user, if any.
      - parameter: error Optionally; if an error occurs, this is the NSError object that describes the
          problem. Set to nil otherwise.

- `


  ### [FIRProviderQueryCallback](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions#/c:FIRAuth.h@T@FIRProviderQueryCallback)


  ` @typedef FIRProviderQueryCallback
  @brief The type of block invoked when a list of identity providers for a given email address is
  requested.

      - parameter: providers Optionally; a list of provider identifiers, if any.
          - see: GoogleAuthProviderID etc.
      - parameter: error Optionally; if an error occurs, this is the NSError object that describes the
          problem. Set to nil otherwise.

- `


  ### [FIRSignInMethodQueryCallback](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions#/c:FIRAuth.h@T@FIRSignInMethodQueryCallback)


  ` @typedef FIRSignInMethodQueryCallback
  @brief The type of block invoked when a list of sign-in methods for a given email address is
  requested.
- `


  ### [FIRSendPasswordResetCallback](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions#/c:FIRAuth.h@T@FIRSendPasswordResetCallback)


  ` @typedef FIRSendPasswordResetCallback
  @brief The type of block invoked when sending a password reset email.

      - parameter: error Optionally; if an error occurs, this is the NSError object that describes the
          problem. Set to nil otherwise.

- `


  ### [FIRSendSignInLinkToEmailCallback](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions#/c:FIRAuth.h@T@FIRSendSignInLinkToEmailCallback)


  ` @typedef FIRSendSignInLinkToEmailCallback
  @brief The type of block invoked when sending an email sign-in link email.
- `


  ### [FIRConfirmPasswordResetCallback](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions#/c:FIRAuth.h@T@FIRConfirmPasswordResetCallback)


  ` @typedef FIRConfirmPasswordResetCallback
  @brief The type of block invoked when performing a password reset.

      - parameter: error Optionally; if an error occurs, this is the NSError object that describes the
          problem. Set to nil otherwise.

- `


  ### [FIRVerifyPasswordResetCodeCallback](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions#/c:FIRAuth.h@T@FIRVerifyPasswordResetCodeCallback)


  ` @typedef FIRVerifyPasswordResetCodeCallback
  @brief The type of block invoked when verifying that an out of band code should be used to
  perform password reset.

      - parameter: email Optionally; the email address of the user for which the out of band code applies.
      - parameter: error Optionally; if an error occurs, this is the NSError object that describes the
          problem. Set to nil otherwise.

- `


  ### [FIRApplyActionCodeCallback](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions#/c:FIRAuth.h@T@FIRApplyActionCodeCallback)


  ` @typedef FIRApplyActionCodeCallback
  @brief The type of block invoked when applying an action code.

      - parameter: error Optionally; if an error occurs, this is the NSError object that describes the
          problem. Set to nil otherwise.

- `


  ### [FIRAuthVoidErrorCallback](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions#/c:FIRAuth.h@T@FIRAuthVoidErrorCallback)


  ` Undocumented
- `


  ### [FIRAuthCredentialCallback](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions#/c:FIRFederatedAuthProvider.h@T@FIRAuthCredentialCallback)


  ` @typedef FIRAuthCredentialCallback
  @brief The type of block invoked when obtaining an auth credential.
  - parameter: credential The credential obtained.
  - parameter: error The error that occurred if any.
- `


  ### [FIRGameCenterCredentialCallback](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions#/c:FIRGameCenterAuthProvider.h@T@FIRGameCenterCredentialCallback)


  ` @typedef FIRGameCenterCredentialCallback
  @brief The type of block invoked when the Game Center credential code has finished.
  - parameter: credential On success, the credential will be provided, nil otherwise.
  - parameter: error On error, the error that occurred, nil otherwise.
- `


  ### [FIRMultiFactorSessionCallback](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions#/c:FIRMultiFactor.h@T@FIRMultiFactorSessionCallback)


  ` @typedef FIRMultiFactorSessionCallback
  @brief The callback that triggered when a developer calls `getSessionWithCompletion`.
  This type is available on iOS and macOS.
  - parameter: session The multi factor session returned, if any.
  - parameter: error The error which occurred, if any.
- `


  ### [FIRVerificationResultCallback](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Type-Definitions#/c:FIRPhoneAuthProvider.h@T@FIRVerificationResultCallback)


  ` @typedef FIRVerificationResultCallback
  @brief The type of block invoked when a request to send a verification code has finished.
  This type is available on iOS only.

      - parameter: verificationID On success, the verification ID provided, nil otherwise.
      - parameter: error On error, the error that occurred, nil otherwise.