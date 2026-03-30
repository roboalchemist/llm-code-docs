# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants.md.txt

# FirebaseAuth Framework Reference

# Constants

The following constants are available globally.
- `


  ### [AuthStateDidChange](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRAuthStateDidChangeNotification)


  ` @brief The name of the `NSNotificationCenter` notification which is posted when the auth state
  changes (for example, a new token has been produced, a user signs in or signs out). The
  object parameter of the notification is the sender `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth` instance.

  #### Declaration

  Swift

      static let AuthStateDidChange: NSNotification.Name

- `


  ### [AuthErrorDomain](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRAuthErrorDomain)


  ` @brief The Firebase Auth error domain.

  #### Declaration

  Swift

      let AuthErrorDomain: String

- `


  ### [AuthErrorUserInfoNameKey](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRAuthErrorUserInfoNameKey)


  ` @brief The name of the key for the error short string of an error code.

  #### Declaration

  Swift

      let AuthErrorUserInfoNameKey: String

- `


  ### [AuthErrorUserInfoEmailKey](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRAuthErrorUserInfoEmailKey)


  ` @brief Errors with one of the following three codes:
  - `AuthErrorCodeAccountExistsWithDifferentCredential`
  - `AuthErrorCodeCredentialAlreadyInUse`
  - `AuthErrorCodeEmailAlreadyInUse`
  may contain an `NSError.userInfo` dictionary object which contains this key. The value
  associated with this key is an NSString of the email address of the account that already
  exists.

  #### Declaration

  Swift

      let AuthErrorUserInfoEmailKey: String

- `


  ### [AuthErrorUserInfoUpdatedCredentialKey](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRAuthErrorUserInfoUpdatedCredentialKey)


  ` @brief The key used to read the updated Auth credential from the userInfo dictionary of the
  NSError object returned. This is the updated auth credential the developer should use for
  recovery if applicable.

  #### Declaration

  Swift

      let AuthErrorUserInfoUpdatedCredentialKey: String

- `


  ### [AuthErrorUserInfoMultiFactorResolverKey](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRAuthErrorUserInfoMultiFactorResolverKey)


  ` @brief The key used to read the MFA resolver from the userInfo dictionary of the NSError object
  returned when 2FA is required for sign-incompletion.

  #### Declaration

  Swift

      let AuthErrorUserInfoMultiFactorResolverKey: String

- `


  ### [EmailAuthProviderID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIREmailAuthProviderID)


  ` @brief A string constant identifying the email \& password identity provider.

  #### Declaration

  Swift

      let EmailAuthProviderID: String

- `


  ### [EmailLinkAuthSignInMethod](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIREmailLinkAuthSignInMethod)


  ` @brief A string constant identifying the email-link sign-in method.

  #### Declaration

  Swift

      let EmailLinkAuthSignInMethod: String

- `


  ### [EmailPasswordAuthSignInMethod](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIREmailPasswordAuthSignInMethod)


  ` @brief A string constant identifying the email \& password sign-in method.

  #### Declaration

  Swift

      let EmailPasswordAuthSignInMethod: String

- `


  ### [FacebookAuthProviderID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRFacebookAuthProviderID)


  ` @brief A string constant identifying the Facebook identity provider.

  #### Declaration

  Swift

      let FacebookAuthProviderID: String

- `


  ### [FacebookAuthSignInMethod](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRFacebookAuthSignInMethod)


  ` @brief A string constant identifying the Facebook sign-in method.

  #### Declaration

  Swift

      let FacebookAuthSignInMethod: String

- `


  ### [GameCenterAuthProviderID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRGameCenterAuthProviderID)


  ` @brief A string constant identifying the Game Center identity provider.

  #### Declaration

  Swift

      let GameCenterAuthProviderID: String

- `


  ### [GameCenterAuthSignInMethod](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRGameCenterAuthSignInMethod)


  ` @brief A string constant identifying the Game Center sign-in method.

  #### Declaration

  Swift

      let GameCenterAuthSignInMethod: String

- `


  ### [GitHubAuthProviderID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRGitHubAuthProviderID)


  ` @brief A string constant identifying the GitHub identity provider.

  #### Declaration

  Swift

      let GitHubAuthProviderID: String

- `


  ### [GitHubAuthSignInMethod](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRGitHubAuthSignInMethod)


  ` @brief A string constant identifying the GitHub sign-in method.

  #### Declaration

  Swift

      let GitHubAuthSignInMethod: String

- `


  ### [GoogleAuthProviderID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRGoogleAuthProviderID)


  ` @brief A string constant identifying the Google identity provider.

  #### Declaration

  Swift

      let GoogleAuthProviderID: String

- `


  ### [GoogleAuthSignInMethod](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRGoogleAuthSignInMethod)


  ` @brief A string constant identifying the Google sign-in method.

  #### Declaration

  Swift

      let GoogleAuthSignInMethod: String

- `


  ### [PhoneMultiFactorID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRPhoneMultiFactorID)


  ` @brief The string identifier for using phone as a second factor.
  This constant is available on iOS and macOS.

  #### Declaration

  Swift

      let PhoneMultiFactorID: String

- `


  ### [TOTPMultiFactorID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRTOTPMultiFactorID)


  ` @brief The string identifier for using TOTP as a second factor.
  This constant is available on iOS and macOS.

  #### Declaration

  Swift

      let TOTPMultiFactorID: String

- `


  ### [PhoneAuthProviderID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRPhoneAuthProviderID)


  ` @var FIRPhoneAuthProviderID
  @brief A string constant identifying the phone identity provider.
  This constant is available on iOS only.

  #### Declaration

  Swift

      let PhoneAuthProviderID: String

- `


  ### [PhoneAuthSignInMethod](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRPhoneAuthSignInMethod)


  ` @var FIRPhoneAuthProviderID
  @brief A string constant identifying the phone sign-in method.
  This constant is available on iOS only.

  #### Declaration

  Swift

      let PhoneAuthSignInMethod: String

- `


  ### [TwitterAuthProviderID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRTwitterAuthProviderID)


  ` @brief A string constant identifying the Twitter identity provider.

  #### Declaration

  Swift

      let TwitterAuthProviderID: String

- `


  ### [TwitterAuthSignInMethod](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Constants#/c:@FIRTwitterAuthSignInMethod)


  ` @brief A string constant identifying the Twitter sign-in method.

  #### Declaration

  Swift

      let TwitterAuthSignInMethod: String