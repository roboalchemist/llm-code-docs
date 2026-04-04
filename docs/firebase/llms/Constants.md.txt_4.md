# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants.md.txt

# FirebaseAuth Framework Reference

# Constants

The following constants are available globally.
- `


  ### [FIRAuthStateDidChangeNotification](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRAuthStateDidChangeNotification)


  ` @brief The name of the `NSNotificationCenter` notification which is posted when the auth state
  changes (for example, a new token has been produced, a user signs in or signs out). The
  object parameter of the notification is the sender `Auth` instance.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(AuthStateDidChange) const NSNotificationName
          FIRAuthStateDidChangeNotification

- `


  ### [FIRAuthErrorDomain](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRAuthErrorDomain)


  ` @brief The Firebase Auth error domain.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(AuthErrorDomain) NSString *const FIRAuthErrorDomain

- `


  ### [FIRAuthErrorUserInfoNameKey](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRAuthErrorUserInfoNameKey)


  ` @brief The name of the key for the error short string of an error code.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(AuthErrorUserInfoNameKey) NSString *const
          FIRAuthErrorUserInfoNameKey

- `


  ### [FIRAuthErrorUserInfoEmailKey](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRAuthErrorUserInfoEmailKey)


  ` @brief Errors with one of the following three codes:
  - `AuthErrorCodeAccountExistsWithDifferentCredential`
  - `AuthErrorCodeCredentialAlreadyInUse`
  - `AuthErrorCodeEmailAlreadyInUse`
  may contain an `NSError.userInfo` dictionary object which contains this key. The value
  associated with this key is an NSString of the email address of the account that already
  exists.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(AuthErrorUserInfoEmailKey) NSString *const
          FIRAuthErrorUserInfoEmailKey

- `


  ### [FIRAuthErrorUserInfoUpdatedCredentialKey](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRAuthErrorUserInfoUpdatedCredentialKey)


  ` @brief The key used to read the updated Auth credential from the userInfo dictionary of the
  NSError object returned. This is the updated auth credential the developer should use for
  recovery if applicable.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(AuthErrorUserInfoUpdatedCredentialKey) NSString *const
          FIRAuthErrorUserInfoUpdatedCredentialKey

- `


  ### [FIRAuthErrorUserInfoMultiFactorResolverKey](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRAuthErrorUserInfoMultiFactorResolverKey)


  ` @brief The key used to read the MFA resolver from the userInfo dictionary of the NSError object
  returned when 2FA is required for sign-incompletion.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(AuthErrorUserInfoMultiFactorResolverKey) NSString *const
          FIRAuthErrorUserInfoMultiFactorResolverKey

- `


  ### [FIREmailAuthProviderID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIREmailAuthProviderID)


  ` @brief A string constant identifying the email \& password identity provider.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(EmailAuthProviderID) NSString *const FIREmailAuthProviderID

- `


  ### [FIREmailLinkAuthSignInMethod](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIREmailLinkAuthSignInMethod)


  ` @brief A string constant identifying the email-link sign-in method.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(EmailLinkAuthSignInMethod) NSString *const
          FIREmailLinkAuthSignInMethod

- `


  ### [FIREmailPasswordAuthSignInMethod](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIREmailPasswordAuthSignInMethod)


  ` @brief A string constant identifying the email \& password sign-in method.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(EmailPasswordAuthSignInMethod) NSString *const
          FIREmailPasswordAuthSignInMethod

- `


  ### [FIRFacebookAuthProviderID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRFacebookAuthProviderID)


  ` @brief A string constant identifying the Facebook identity provider.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(FacebookAuthProviderID) NSString *const
          FIRFacebookAuthProviderID

- `


  ### [FIRFacebookAuthSignInMethod](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRFacebookAuthSignInMethod)


  ` @brief A string constant identifying the Facebook sign-in method.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(FacebookAuthSignInMethod) NSString *const
          FIRFacebookAuthSignInMethod

- `


  ### [FIRGameCenterAuthProviderID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRGameCenterAuthProviderID)


  ` @brief A string constant identifying the Game Center identity provider.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(GameCenterAuthProviderID) NSString *const
          FIRGameCenterAuthProviderID

- `


  ### [FIRGameCenterAuthSignInMethod](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRGameCenterAuthSignInMethod)


  ` @brief A string constant identifying the Game Center sign-in method.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(
          GameCenterAuthSignInMethod) NSString *const
          FIRGameCenterAuthSignInMethod

- `


  ### [FIRGitHubAuthProviderID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRGitHubAuthProviderID)


  ` @brief A string constant identifying the GitHub identity provider.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(GitHubAuthProviderID) NSString *const
          FIRGitHubAuthProviderID

- `


  ### [FIRGitHubAuthSignInMethod](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRGitHubAuthSignInMethod)


  ` @brief A string constant identifying the GitHub sign-in method.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(GitHubAuthSignInMethod) NSString *const
          FIRGitHubAuthSignInMethod

- `


  ### [FIRGoogleAuthProviderID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRGoogleAuthProviderID)


  ` @brief A string constant identifying the Google identity provider.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(GoogleAuthProviderID) NSString *const
          FIRGoogleAuthProviderID

- `


  ### [FIRGoogleAuthSignInMethod](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRGoogleAuthSignInMethod)


  ` @brief A string constant identifying the Google sign-in method.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(GoogleAuthSignInMethod) NSString *const
          FIRGoogleAuthSignInMethod

- `


  ### [FIRPhoneMultiFactorID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRPhoneMultiFactorID)


  ` @brief The string identifier for using phone as a second factor.
  This constant is available on iOS only.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(PhoneMultiFactorID) NSString *const FIRPhoneMultiFactorID

- `


  ### [FIRTOTPMultiFactorID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRTOTPMultiFactorID)


  ` @brief The string identifier for using TOTP as a second factor.
  This constant is available on iOS only.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(TOTPMultiFactorID) NSString *const FIRTOTPMultiFactorID

- `


  ### [FIRPhoneAuthProviderID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRPhoneAuthProviderID)


  ` @var FIRPhoneAuthProviderID
  @brief A string constant identifying the phone identity provider.
  This constant is available on iOS only.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(PhoneAuthProviderID) NSString *const FIRPhoneAuthProviderID

- `


  ### [FIRPhoneAuthSignInMethod](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRPhoneAuthSignInMethod)


  ` @var FIRPhoneAuthProviderID
  @brief A string constant identifying the phone sign-in method.
  This constant is available on iOS only.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(PhoneAuthSignInMethod) NSString *const
          FIRPhoneAuthSignInMethod

- `


  ### [FIRTwitterAuthProviderID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRTwitterAuthProviderID)


  ` @brief A string constant identifying the Twitter identity provider.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(TwitterAuthProviderID) NSString *const
          FIRTwitterAuthProviderID

- `


  ### [FIRTwitterAuthSignInMethod](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Constants#/c:@FIRTwitterAuthSignInMethod)


  ` @brief A string constant identifying the Twitter sign-in method.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(TwitterAuthSignInMethod) NSString *const
          FIRTwitterAuthSignInMethod