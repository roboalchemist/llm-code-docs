# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/User.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.md.txt

# FirebaseAuth Framework Reference

# User

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRUser)
    open class User : NSObject, https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/UserInfo.html

    extension User: NSSecureCoding

Represents a user.

Firebase Auth does not attempt to validate users
when loading them from the keychain. Invalidated users (such as those
whose passwords have been changed on another client) are automatically
logged out when an auth-dependent operation is attempted or when the
ID token is automatically refreshed.

This class is thread-safe.
- `
  ``
  ``
  `

  ### [isAnonymous](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(py)isAnonymous)

  `
  `  
  Indicates the user represents an anonymous user.  

  #### Declaration

  Swift  

      @objc
      public internal(set) var isAnonymous: Bool { get }

- `
  ``
  ``
  `

  ### [anonymous()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)anonymous)

  `
  `  
  Indicates the user represents an anonymous user.  

  #### Declaration

  Swift  

      @objc
      open func anonymous() -> Bool

- `
  ``
  ``
  `

  ### [isEmailVerified](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(py)isEmailVerified)

  `
  `  
  Indicates the email address associated with this user has been verified.  

  #### Declaration

  Swift  

      @objc
      public private(set) var isEmailVerified: Bool { get }

- `
  ``
  ``
  `

  ### [emailVerified()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)emailVerified)

  `
  `  
  Indicates the email address associated with this user has been verified.  

  #### Declaration

  Swift  

      @objc
      open func emailVerified() -> Bool

- `
  ``
  ``
  `

  ### [providerData](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(py)providerData)

  `
  `  
  Profile data for each identity provider, if any.

  This data is cached on sign-in and updated when linking or unlinking.  

  #### Declaration

  Swift  

      @objc
      open var providerData: [https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/UserInfo.html] { get }

- `
  ``
  ``
  `

  ### [metadata](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(py)metadata)

  `
  `  
  Metadata associated with the Firebase user in question.  

  #### Declaration

  Swift  

      @objc
      public private(set) var metadata: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/UserMetadata.html { get }

- `
  ``
  ``
  `

  ### [tenantID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(py)tenantID)

  `
  `  
  The tenant ID of the current user. `nil` if none is available.  

  #### Declaration

  Swift  

      @objc
      public private(set) var tenantID: String? { get }

- `
  ``
  ``
  `

  ### [multiFactor](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(py)multiFactor)

  `
  `  
  Multi factor object associated with the user.

  This property is available on iOS and macOS.  

  #### Declaration

  Swift  

      @objc
      public private(set) var multiFactor: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactor.html { get }

- `
  ``
  ``
  `

  ### [updateEmail(to:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)updateEmail:completion:)

  `
  `  
  \[Deprecated\] Updates the email address for the user.

  On success, the cached user profile data is updated. Returns an error when
  [Email Enumeration Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)
  is enabled.

  May fail if there is already an account with this email address that was created using
  email and password authentication.

  Invoked asynchronously on the main thread in the future.

  Possible error codes:
  - `AuthErrorCodeInvalidRecipientEmail` - Indicates an invalid recipient email was sent in the request.
  - `AuthErrorCodeInvalidSender` - Indicates an invalid sender email is set in the console for this action.
  - `AuthErrorCodeInvalidMessagePayload` - Indicates an invalid email template for sending update email.
  - `AuthErrorCodeEmailAlreadyInUse` - Indicates the email is already in use by another account.
  - `AuthErrorCodeInvalidEmail` - Indicates the email address is malformed.
  - `AuthErrorCodeRequiresRecentLogin` - Updating a user's email is a security sensitive operation that requires a recent login from the user. This error indicates the user has not signed in recently enough. To resolve, reauthenticate the user by calling [reauthenticate(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html#/s:12FirebaseAuth4UserC14reauthenticate4withAA0B10DataResultCAA0B10CredentialC_tYaKF).  

  #### Declaration

  Swift  

      @available(*, deprecated, message: "`updateEmail` is deprecated and will be removed in a future release. Use sendEmailVerification(beforeUpdatingEmail:ï¹ instead.")
      @objc(updateEmail:completion:)
      open func updateEmail(to email: String, completion: ((Error?) -> Void)? = nil)

  #### Parameters

  |--------------------|--------------------------------------------------------------------------|
  | ` `*email*` `      | The email address for the user.                                          |
  | ` `*completion*` ` | Optionally; the block invoked when the user profile change has finished. |

- `
  ``
  ``
  `

  ### [updateEmail(to:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/s:12FirebaseAuth4UserC11updateEmail2toySS_tYaKF)

  `
  `  
  \[Deprecated\] Updates the email address for the user.

  On success, the cached user profile data is updated. Throws when
  [Email Enumeration Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)
  is enabled.

  May fail if there is already an account with this email address that was created using
  email and password authentication.

  Invoked asynchronously on the main thread in the future.

  Possible error codes:
  - `AuthErrorCodeInvalidRecipientEmail` - Indicates an invalid recipient email was sent in the request.
  - `AuthErrorCodeInvalidSender` - Indicates an invalid sender email is set in the console for this action.
  - `AuthErrorCodeInvalidMessagePayload` - Indicates an invalid email template for sending update email.
  - `AuthErrorCodeEmailAlreadyInUse` - Indicates the email is already in use by another account.
  - `AuthErrorCodeInvalidEmail` - Indicates the email address is malformed.
  - `AuthErrorCodeRequiresRecentLogin` - Updating a user's email is a security sensitive operation that requires a recent login from the user. This error indicates the user has not signed in recently enough. To resolve, reauthenticate the user by calling [reauthenticate(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html#/s:12FirebaseAuth4UserC14reauthenticate4withAA0B10DataResultCAA0B10CredentialC_tYaKF).  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @available(*, deprecated, message: "`updateEmail` is deprecated and will be removed in a future release. Use sendEmailVerification(beforeUpdatingEmail:ï¹ instead.")
      open func updateEmail(to email: String) async throws

  #### Parameters

  |---------------|---------------------------------|
  | ` `*email*` ` | The email address for the user. |

- `
  ``
  ``
  `

  ### [updatePassword(to:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)updatePassword:completion:)

  `
  `  
  Updates the password for the user. On success, the cached user profile data is updated.

  Invoked asynchronously on the main thread in the future.

  Possible error codes:
  - `AuthErrorCodeOperationNotAllowed` - Indicates the administrator disabled sign in with the specified identity provider.
  - `AuthErrorCodeRequiresRecentLogin` - Updating a user's password is a security sensitive operation that requires a recent login from the user. This error indicates the user has not signed in recently enough. To resolve, reauthenticate the user by calling [reauthenticate(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html#/s:12FirebaseAuth4UserC14reauthenticate4withAA0B10DataResultCAA0B10CredentialC_tYaKF).
  - `AuthErrorCodeWeakPassword` - Indicates an attempt to set a password that is considered too weak. The `NSLocalizedFailureReasonErrorKey` field in the `userInfo` dictionary object will contain more detailed explanation that can be shown to the user.  

  #### Declaration

  Swift  

      @objc(updatePassword:completion:)
      open func updatePassword(to password: String, completion: ((Error?) -> Void)? = nil)

  #### Parameters

  |--------------------|--------------------------------------------------------------------------|
  | ` `*password*` `   | The new password for the user.                                           |
  | ` `*completion*` ` | Optionally; the block invoked when the user profile change has finished. |

- `
  ``
  ``
  `

  ### [updatePassword(to:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/s:12FirebaseAuth4UserC14updatePassword2toySS_tYaKF)

  `
  `  
  Updates the password for the user. On success, the cached user profile data is updated.

  Invoked asynchronously on the main thread in the future.

  Possible error codes:
  - `AuthErrorCodeOperationNotAllowed` - Indicates the administrator disabled sign in with the specified identity provider.
  - `AuthErrorCodeRequiresRecentLogin` - Updating a user's password is a security sensitive operation that requires a recent login from the user. This error indicates the user has not signed in recently enough. To resolve, reauthenticate the user by calling [reauthenticate(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html#/s:12FirebaseAuth4UserC14reauthenticate4withAA0B10DataResultCAA0B10CredentialC_tYaKF).
  - `AuthErrorCodeWeakPassword` - Indicates an attempt to set a password that is considered too weak. The `NSLocalizedFailureReasonErrorKey` field in the `userInfo` dictionary object will contain more detailed explanation that can be shown to the user.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func updatePassword(to password: String) async throws

  #### Parameters

  |------------------|--------------------------------|
  | ` `*password*` ` | The new password for the user. |

- `
  ``
  ``
  `

  ### [updatePhoneNumber(_:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)updatePhoneNumberCredential:completion:)

  `
  `  
  Updates the phone number for the user. On success, the cached user profile data is updated.

  Invoked asynchronously on the main thread in the future.

  This method is available on iOS only.

  Possible error codes:
  - `AuthErrorCodeRequiresRecentLogin` - Updating a user's phone number is a security sensitive operation that requires a recent login from the user. This error indicates the user has not signed in recently enough. To resolve, reauthenticate the user by calling [reauthenticate(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html#/s:12FirebaseAuth4UserC14reauthenticate4withAA0B10DataResultCAA0B10CredentialC_tYaKF).  

  #### Declaration

  Swift  

      @objc(updatePhoneNumberCredential:completion:)
      open func updatePhoneNumber(_ credential: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneAuthCredential.html,
                                  completion: ((Error?) -> Void)? = nil)

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*credential*` ` | The new phone number credential corresponding to the phone number to be added to the Firebase account, if a phone number is already linked to the account this new phone number will replace it. |
  | ` `*completion*` ` | Optionally; the block invoked when the user profile change has finished.                                                                                                                         |

- `
  ``
  ``
  `

  ### [updatePhoneNumber(_:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/s:12FirebaseAuth4UserC17updatePhoneNumberyyAA0eB10CredentialCYaKF)

  `
  `  
  Updates the phone number for the user. On success, the cached user profile data is updated.

  Invoked asynchronously on the main thread in the future.

  This method is available on iOS only.

  Possible error codes:
  - `AuthErrorCodeRequiresRecentLogin` - Updating a user's phone number is a security sensitive operation that requires a recent login from the user. This error indicates the user has not signed in recently enough. To resolve, reauthenticate the user by calling [reauthenticate(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html#/s:12FirebaseAuth4UserC14reauthenticate4withAA0B10DataResultCAA0B10CredentialC_tYaKF).  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func updatePhoneNumber(_ credential: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneAuthCredential.html) async throws

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*credential*` ` | The new phone number credential corresponding to the phone number to be added to the Firebase account, if a phone number is already linked to the account this new phone number will replace it. |

- `
  ``
  ``
  `

  ### [createProfileChangeRequest()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)profileChangeRequest)

  `
  `  
  Creates an object which may be used to change the user's profile data.

  Set the properties of the returned object, then call
  [UserProfileChangeRequest.commitChanges()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/UserProfileChangeRequest.html#/s:12FirebaseAuth24UserProfileChangeRequestC13commitChangesyyYaKF) to perform the updates atomically.  

  #### Declaration

  Swift  

      @objc(profileChangeRequest)
      open func createProfileChangeRequest() -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/UserProfileChangeRequest.html

  #### Return Value

  An object which may be used to change the user's profile data atomically.
- `
  ``
  ``
  `

  ### [refreshToken](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(py)refreshToken)

  `
  `  
  A refresh token; useful for obtaining new access tokens independently.

  This property should only be used for advanced scenarios, and is not typically needed.  

  #### Declaration

  Swift  

      @objc
      open var refreshToken: String? { get }

- `
  ``
  ``
  `

  ### [reload(completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)reloadWithCompletion:)

  `
  `  
  Reloads the user's profile data from the server.

  May fail with an `AuthErrorCodeRequiresRecentLogin` error code. In this case
  you should call [reauthenticate(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html#/s:12FirebaseAuth4UserC14reauthenticate4withAA0B10DataResultCAA0B10CredentialC_tYaKF) before re-invoking
  [updateEmail(to:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html#/s:12FirebaseAuth4UserC11updateEmail2toySS_tYaKF).  

  #### Declaration

  Swift  

      @objc
      open func reload(completion: ((Error?) -> Void)? = nil)

  #### Parameters

  |--------------------|----------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | Optionally; the block invoked when the reload has finished. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [reload()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/s:12FirebaseAuth4UserC6reloadyyYaKF)

  `
  `  
  Reloads the user's profile data from the server.

  May fail with an `AuthErrorCodeRequiresRecentLogin` error code. In this case
  you should call [reauthenticate(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html#/s:12FirebaseAuth4UserC14reauthenticate4withAA0B10DataResultCAA0B10CredentialC_tYaKF) before re-invoking
  [updateEmail(to:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html#/s:12FirebaseAuth4UserC11updateEmail2toySS_tYaKF).  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func reload() async throws

- `
  ``
  ``
  `

  ### [reauthenticate(with:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)reauthenticateWithCredential:completion:)

  `
  `  
  Renews the user's authentication tokens by validating a fresh set of credentials supplied
  by the user and returns additional identity provider data.

  If the user associated with the supplied credential is different from the current user,
  or if the validation of the supplied credentials fails; an error is returned and the current
  user remains signed in.

  Possible error codes:
  - `AuthErrorCodeInvalidCredential` - Indicates the supplied credential is invalid. This could happen if it has expired or it is malformed.
  - `AuthErrorCodeOperationNotAllowed` - Indicates that accounts with the identity provider represented by the credential are not enabled. Enable them in the Auth section of the Firebase console.
  - `AuthErrorCodeEmailAlreadyInUse` - Indicates the email asserted by the credential (e.g. the email in a Facebook access token) is already in use by an existing account, that cannot be authenticated with this method. This error will only be thrown if the "One account per email address" setting is enabled in the Firebase console, under Auth settings. Please note that the error code raised in this specific situation may not be the same on Web and Android.
  - `AuthErrorCodeUserDisabled` - Indicates the user's account is disabled.
  - `AuthErrorCodeWrongPassword` - Indicates the user attempted reauthentication with an incorrect password, if credential is of the type `EmailPasswordAuthCredential`.
  - `AuthErrorCodeUserMismatch` - Indicates that an attempt was made to reauthenticate with a user which is not the current user.
  - `AuthErrorCodeInvalidEmail` - Indicates the email address is malformed.  

  #### Declaration

  Swift  

      @objc(reauthenticateWithCredential:completion:)
      open func reauthenticate(with credential: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html,
                               completion: ((https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html?, Error?) -> Void)? = nil)

  #### Parameters

  |--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*credential*` ` | A user-supplied credential, which will be validated by the server. This can be a successful third-party identity provider sign-in, or an email address and password. |
  | ` `*completion*` ` | Optionally; the block invoked when the re-authentication operation has finished. Invoked asynchronously on the main thread in the future.                            |

- `
  ``
  ``
  `

  ### [reauthenticate(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/s:12FirebaseAuth4UserC14reauthenticate4withAA0B10DataResultCAA0B10CredentialC_tYaKF)

  `
  `  
  Renews the user's authentication tokens by validating a fresh set of credentials supplied
  by the user and returns additional identity provider data.

  If the user associated with the supplied credential is different from the current user,
  or if the validation of the supplied credentials fails; an error is returned and the current
  user remains signed in.

  Possible error codes:
  - `AuthErrorCodeInvalidCredential` - Indicates the supplied credential is invalid. This could happen if it has expired or it is malformed.
  - `AuthErrorCodeOperationNotAllowed` - Indicates that accounts with the identity provider represented by the credential are not enabled. Enable them in the Auth section of the Firebase console.
  - `AuthErrorCodeEmailAlreadyInUse` - Indicates the email asserted by the credential (e.g. the email in a Facebook access token) is already in use by an existing account, that cannot be authenticated with this method. This error will only be thrown if the "One account per email address" setting is enabled in the Firebase console, under Auth settings. Please note that the error code raised in this specific situation may not be the same on Web and Android.
  - `AuthErrorCodeUserDisabled` - Indicates the user's account is disabled.
  - `AuthErrorCodeWrongPassword` - Indicates the user attempted reauthentication with an incorrect password, if credential is of the type `EmailPasswordAuthCredential`.
  - `AuthErrorCodeUserMismatch` - Indicates that an attempt was made to reauthenticate with a user which is not the current user.
  - `AuthErrorCodeInvalidEmail` - Indicates the email address is malformed.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @discardableResult
      open func reauthenticate(with credential: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html) async throws -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html

  #### Parameters

  |--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*credential*` ` | A user-supplied credential, which will be validated by the server. This can be a successful third-party identity provider sign-in, or an email address and password. |

  #### Return Value

  The [AuthDataResult](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html) after the reauthentication.
- `
  ``
  ``
  `

  ### [reauthenticate(with:uiDelegate:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)reauthenticateWithProvider:UIDelegate:completion:)

  `
  `  
  Renews the user's authentication using the provided auth provider instance.

  This method is available on iOS only.  

  #### Declaration

  Swift  

      @objc(reauthenticateWithProvider:UIDelegate:completion:)
      open func reauthenticate(with provider: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/FederatedAuthProvider.html,
                               uiDelegate: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html?,
                               completion: ((https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html?, Error?) -> Void)? = nil)

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*provider*` `   | An instance of an auth provider used to initiate the reauthenticate flow.                                                                                                                                                                                                                                                                                                                  |
  | ` `*uiDelegate*` ` | Optionally an instance of a class conforming to the [AuthUIDelegate](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html) protocol, used for presenting the web context. If nil, a default [AuthUIDelegate](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html) will be used. |
  | ` `*completion*` ` | Optionally; a block which is invoked when the reauthenticate flow finishes, or is canceled. Invoked asynchronously on the main thread in the future.                                                                                                                                                                                                                                       |

- `
  ``
  ``
  `

  ### [reauthenticate(with:uiDelegate:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/s:12FirebaseAuth4UserC14reauthenticate4with10uiDelegateAA0B10DataResultCAA09FederatedB8Provider_p_AA0B10UIDelegate_pSgtYaKF)

  `
  `  
  Renews the user's authentication using the provided auth provider instance.

  This method is available on iOS only.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @discardableResult
      open func reauthenticate(with provider: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/FederatedAuthProvider.html,
                               uiDelegate: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html?) async throws -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*provider*` `   | An instance of an auth provider used to initiate the reauthenticate flow.                                                                                                                                                                                                                                                                                                                  |
  | ` `*uiDelegate*` ` | Optionally an instance of a class conforming to the [AuthUIDelegate](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html) protocol, used for presenting the web context. If nil, a default [AuthUIDelegate](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html) will be used. |

  #### Return Value

  The [AuthDataResult](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html) after the reauthentication.
- `
  ``
  ``
  `

  ### [getIDToken(completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)getIDTokenWithCompletion:)

  `
  `  
  Retrieves the Firebase authentication token, possibly refreshing it if it has expired.  

  #### Declaration

  Swift  

      @objc(getIDTokenWithCompletion:)
      open func getIDToken(completion: ((String?, Error?) -> Void)?)

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | Optionally; the block invoked when the token is available. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [getIDTokenForcingRefresh(_:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)getIDTokenForcingRefresh:completion:)

  `
  `  
  Retrieves the Firebase authentication token, possibly refreshing it if it has expired.

  The authentication token will be refreshed (by making a network request) if it has
  expired, or if `forceRefresh` is `true`.  

  #### Declaration

  Swift  

      @objc(getIDTokenForcingRefresh:completion:)
      open func getIDTokenForcingRefresh(_ forceRefresh: Bool,
                                         completion: ((String?, Error?) -> Void)?)

  #### Parameters

  |----------------------|---------------------------------------------------------------------------------------------------------------------|
  | ` `*forceRefresh*` ` | Forces a token refresh. Useful if the token becomes invalid for some reason other than an expiration.               |
  | ` `*completion*` `   | Optionally; the block invoked when the token is available. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [getIDToken(forcingRefresh:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/s:12FirebaseAuth4UserC10getIDToken14forcingRefreshSSSb_tYaKF)

  `
  `  
  Retrieves the Firebase authentication token, possibly refreshing it if it has expired.

  The authentication token will be refreshed (by making a network request) if it has
  expired, or if `forceRefresh` is `true`.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func getIDToken(forcingRefresh forceRefresh: Bool = false) async throws -> String

  #### Parameters

  |----------------------|-------------------------------------------------------------------------------------------------------|
  | ` `*forceRefresh*` ` | Forces a token refresh. Useful if the token becomes invalid for some reason other than an expiration. |

  #### Return Value

  The Firebase authentication token.
- `
  ``
  ``
  `

  ### [idTokenForcingRefresh(_:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/s:12FirebaseAuth4UserC21idTokenForcingRefreshySSSbYaKF)

  `
  `  
  API included for compatibility with a mis-named Firebase 10 API.
  Use `getIDToken(forcingRefresh forceRefresh: Bool = false)` instead.  

  #### Declaration

  Swift  

      open func idTokenForcingRefresh(_ forceRefresh: Bool) async throws -> String

- `
  ``
  ``
  `

  ### [getIDTokenResult(completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)getIDTokenResultWithCompletion:)

  `
  `  
  Retrieves the Firebase authentication token, possibly refreshing it if it has expired.  

  #### Declaration

  Swift  

      @objc(getIDTokenResultWithCompletion:)
      open func getIDTokenResult(completion: ((https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthTokenResult.html?, Error?) -> Void)?)

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | Optionally; the block invoked when the token is available. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [getIDTokenResult(forcingRefresh:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)getIDTokenResultForcingRefresh:completion:)

  `
  `  
  Retrieves the Firebase authentication token, possibly refreshing it if it has expired.

  The authentication token will be refreshed (by making a network request) if it has
  expired, or if `forcingRefresh` is `true`.  

  #### Declaration

  Swift  

      @objc(getIDTokenResultForcingRefresh:completion:)
      open func getIDTokenResult(forcingRefresh: Bool,
                                 completion: ((https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthTokenResult.html?, Error?) -> Void)?)

  #### Parameters

  |------------------------|---------------------------------------------------------------------------------------------------------------------|
  | ` `*forcingRefresh*` ` | Forces a token refresh. Useful if the token becomes invalid for some reason other than an expiration.               |
  | ` `*completion*` `     | Optionally; the block invoked when the token is available. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [getIDTokenResult(forcingRefresh:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/s:12FirebaseAuth4UserC16getIDTokenResult14forcingRefreshAA0b5TokenF0CSb_tYaKF)

  `
  `  
  Retrieves the Firebase authentication token, possibly refreshing it if it has expired.

  The authentication token will be refreshed (by making a network request) if it has
  expired, or if `forceRefresh` is `true`.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func getIDTokenResult(forcingRefresh forceRefresh: Bool = false) async throws
        -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthTokenResult.html

  #### Parameters

  |----------------------|-------------------------------------------------------------------------------------------------------|
  | ` `*forceRefresh*` ` | Forces a token refresh. Useful if the token becomes invalid for some reason other than an expiration. |

  #### Return Value

  The Firebase authentication token.
- `
  ``
  ``
  `

  ### [link(with:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)linkWithCredential:completion:)

  `
  `  
  Associates a user account from a third-party identity provider with this user and
  returns additional identity provider data.

  Invoked asynchronously on the main thread in the future.

  Possible error codes:
  - `AuthErrorCodeProviderAlreadyLinked` - Indicates an attempt to link a provider of a type already linked to this account.
  - `AuthErrorCodeCredentialAlreadyInUse` - Indicates an attempt to link with a credential that has already been linked with a different Firebase account.
  - `AuthErrorCodeOperationNotAllowed` - Indicates that accounts with the identity provider represented by the credential are not enabled. Enable them in the Auth section of the Firebase console.

  This method may also return error codes associated with [updateEmail(to:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html#/s:12FirebaseAuth4UserC11updateEmail2toySS_tYaKF) and
  [updatePassword(to:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html#/s:12FirebaseAuth4UserC14updatePassword2toySS_tYaKF) on `User`.  

  #### Declaration

  Swift  

      @objc(linkWithCredential:completion:)
      open func link(with credential: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html,
                     completion: ((https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html?, Error?) -> Void)? = nil)

  #### Parameters

  |--------------------|-------------------------------------------------------------------------|
  | ` `*credential*` ` | The credential for the identity provider.                               |
  | ` `*completion*` ` | Optionally; the block invoked when the unlinking is complete, or fails. |

- `
  ``
  ``
  `

  ### [link(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/s:12FirebaseAuth4UserC4link4withAA0B10DataResultCAA0B10CredentialC_tYaKF)

  `
  `  
  Associates a user account from a third-party identity provider with this user and
  returns additional identity provider data.

  Invoked asynchronously on the main thread in the future.

  Possible error codes:
  - `AuthErrorCodeProviderAlreadyLinked` - Indicates an attempt to link a provider of a type already linked to this account.
  - `AuthErrorCodeCredentialAlreadyInUse` - Indicates an attempt to link with a credential that has already been linked with a different Firebase account.
  - `AuthErrorCodeOperationNotAllowed` - Indicates that accounts with the identity provider represented by the credential are not enabled. Enable them in the Auth section of the Firebase console.

  This method may also return error codes associated with [updateEmail(to:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html#/s:12FirebaseAuth4UserC11updateEmail2toySS_tYaKF) and
  [updatePassword(to:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html#/s:12FirebaseAuth4UserC14updatePassword2toySS_tYaKF) on `User`.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @discardableResult
      open func link(with credential: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html) async throws -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html

  #### Parameters

  |--------------------|-------------------------------------------|
  | ` `*credential*` ` | The credential for the identity provider. |

  #### Return Value

  An [AuthDataResult](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html).
- `
  ``
  ``
  `

  ### [link(with:uiDelegate:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)linkWithProvider:UIDelegate:completion:)

  `
  `  
  Link the user with the provided auth provider instance.

  This method is available on iOSonly.  

  #### Declaration

  Swift  

      @objc(linkWithProvider:UIDelegate:completion:)
      open func link(with provider: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/FederatedAuthProvider.html,
                     uiDelegate: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html?,
                     completion: ((https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html?, Error?) -> Void)? = nil)

  #### Parameters

  |--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*provider*` `   | An instance of an auth provider used to initiate the link flow.                                                                                                                                                                                                                                                                                                                           |
  | ` `*uiDelegate*` ` | Optionally an instance of a class conforming to the [AuthUIDelegate](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html) protocol used for presenting the web context. If nil, a default [AuthUIDelegate](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html) will be used. |
  | ` `*completion*` ` | Optionally; a block which is invoked when the link flow finishes, or is canceled. Invoked asynchronously on the main thread in the future.                                                                                                                                                                                                                                                |

- `
  ``
  ``
  `

  ### [link(with:uiDelegate:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/s:12FirebaseAuth4UserC4link4with10uiDelegateAA0B10DataResultCAA09FederatedB8Provider_p_AA0B10UIDelegate_pSgtYaKF)

  `
  `  
  Link the user with the provided auth provider instance.

  This method is available on iOSonly.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @discardableResult
      open func link(with provider: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/FederatedAuthProvider.html,
                     uiDelegate: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html?) async throws -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html

  #### Parameters

  |--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*provider*` `   | An instance of an auth provider used to initiate the link flow.                                                                                                                                                                                                                                                                                                                           |
  | ` `*uiDelegate*` ` | Optionally an instance of a class conforming to the [AuthUIDelegate](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html) protocol used for presenting the web context. If nil, a default [AuthUIDelegate](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html) will be used. |

  #### Return Value

  An AuthDataResult.
- `
  ``
  ``
  `

  ### [unlink(fromProvider:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)unlinkFromProvider:completion:)

  `
  `  
  Disassociates a user account from a third-party identity provider with this user.

  Invoked asynchronously on the main thread in the future.

  Possible error codes:
  - `AuthErrorCodeNoSuchProvider` - Indicates an attempt to unlink a provider that is not linked to the account.
  - `AuthErrorCodeRequiresRecentLogin` - Updating email is a security sensitive operation that requires a recent login from the user. This error indicates the user has not signed in recently enough. To resolve, reauthenticate the user by calling [reauthenticate(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html#/s:12FirebaseAuth4UserC14reauthenticate4withAA0B10DataResultCAA0B10CredentialC_tYaKF).  

  #### Declaration

  Swift  

      @objc
      open func unlink(fromProvider provider: String,
                       completion: ((User?, Error?) -> Void)? = nil)

  #### Parameters

  |--------------------|-------------------------------------------------------------------------|
  | ` `*provider*` `   | The provider ID of the provider to unlink.                              |
  | ` `*completion*` ` | Optionally; the block invoked when the unlinking is complete, or fails. |

- `
  ``
  ``
  `

  ### [unlink(fromProvider:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/s:12FirebaseAuth4UserC6unlink12fromProviderACSS_tYaKF)

  `
  `  
  Disassociates a user account from a third-party identity provider with this user.

  Invoked asynchronously on the main thread in the future.

  Possible error codes:
  - `AuthErrorCodeNoSuchProvider` - Indicates an attempt to unlink a provider that is not linked to the account.
  - `AuthErrorCodeRequiresRecentLogin` - Updating email is a security sensitive operation that requires a recent login from the user. This error indicates the user has not signed in recently enough. To resolve, reauthenticate the user by calling [reauthenticate(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html#/s:12FirebaseAuth4UserC14reauthenticate4withAA0B10DataResultCAA0B10CredentialC_tYaKF).  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func unlink(fromProvider provider: String) async throws -> User

  #### Parameters

  |------------------|--------------------------------------------|
  | ` `*provider*` ` | The provider ID of the provider to unlink. |

  #### Return Value

  The user.
- `
  ``
  ``
  `

  ### [__sendEmailVerification(withCompletion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)sendEmailVerificationWithCompletion:)

  `
  `  
  Initiates email verification for the user.

  Possible error codes:
  - `AuthErrorCodeInvalidRecipientEmail` - Indicates an invalid recipient email was sent in the request.
  - `AuthErrorCodeInvalidSender` - Indicates an invalid sender email is set in the console for this action.
  - `AuthErrorCodeInvalidMessagePayload` - Indicates an invalid email template for sending update email.
  - `AuthErrorCodeUserNotFound` - Indicates the user account was not found.  

  #### Declaration

  Swift  

      @objc(sendEmailVerificationWithCompletion:)
      open func __sendEmailVerification(withCompletion completion: ((Error?) -> Void)?)

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | Optionally; the block invoked when the request to send an email verification is complete, or fails. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [sendEmailVerification(with:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)sendEmailVerificationWithActionCodeSettings:completion:)

  `
  `  
  Initiates email verification for the user.

  Possible error codes:
  - `AuthErrorCodeInvalidRecipientEmail` - Indicates an invalid recipient email was sent in the request.
  - `AuthErrorCodeInvalidSender` - Indicates an invalid sender email is set in the console for this action.
  - `AuthErrorCodeInvalidMessagePayload` - Indicates an invalid email template for sending update email.
  - `AuthErrorCodeUserNotFound` - Indicates the user account was not found.  

  #### Declaration

  Swift  

      @objc(sendEmailVerificationWithActionCodeSettings:completion:)
      open func sendEmailVerification(with actionCodeSettings: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.html? = nil,
                                      completion: ((Error?) -> Void)? = nil)

  #### Parameters

  |----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*actionCodeSettings*` ` | An [ActionCodeSettings](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.html) object containing settings related to handling action codes. |
  | ` `*completion*` `         | Optionally; the block invoked when the request to send an email verification is complete, or fails. Invoked asynchronously on the main thread in the future.                                      |

- `
  ``
  ``
  `

  ### [sendEmailVerification(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/s:12FirebaseAuth4UserC21sendEmailVerification4withyAA18ActionCodeSettingsCSg_tYaKF)

  `
  `  
  Initiates email verification for the user.

  Possible error codes:
  - `AuthErrorCodeInvalidRecipientEmail` - Indicates an invalid recipient email was sent in the request.
  - `AuthErrorCodeInvalidSender` - Indicates an invalid sender email is set in the console for this action.
  - `AuthErrorCodeInvalidMessagePayload` - Indicates an invalid email template for sending update email.
  - `AuthErrorCodeUserNotFound` - Indicates the user account was not found.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func sendEmailVerification(with actionCodeSettings: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.html? = nil) async throws

  #### Parameters

  |----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*actionCodeSettings*` ` | An [ActionCodeSettings](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.html) object containing settings related to handling action codes. The default value is `nil`. |

- `
  ``
  ``
  `

  ### [delete(completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)deleteWithCompletion:)

  `
  `  
  Deletes the user account (also signs out the user, if this was the current user).

  Possible error codes:
  - `AuthErrorCodeRequiresRecentLogin` - Updating email is a security sensitive operation that requires a recent login from the user. This error indicates the user has not signed in recently enough. To resolve, reauthenticate the user by calling [reauthenticate(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html#/s:12FirebaseAuth4UserC14reauthenticate4withAA0B10DataResultCAA0B10CredentialC_tYaKF).  

  #### Declaration

  Swift  

      @objc
      open func delete(completion: ((Error?) -> Void)? = nil)

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | Optionally; the block invoked when the request to delete the account is complete, or fails. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [delete()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/s:12FirebaseAuth4UserC6deleteyyYaKF)

  `
  `  
  Deletes the user account (also signs out the user, if this was the current user).

  Possible error codes:
  - `AuthErrorCodeRequiresRecentLogin` - Updating email is a security sensitive operation that requires a recent login from the user. This error indicates the user has not signed in recently enough. To resolve, reauthenticate the user by calling [reauthenticate(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html#/s:12FirebaseAuth4UserC14reauthenticate4withAA0B10DataResultCAA0B10CredentialC_tYaKF).  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func delete() async throws

- `
  ``
  ``
  `

  ### [__sendEmailVerificationBeforeUpdating(email:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)sendEmailVerificationBeforeUpdatingEmail:completion:)

  `
  `  
  Send an email to verify the ownership of the account then update to the new email.  

  #### Declaration

  Swift  

      @objc(sendEmailVerificationBeforeUpdatingEmail:completion:)
      open func __sendEmailVerificationBeforeUpdating(email: String, completion: ((Error?) -> Void)?)

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------|
  | ` `*email*` `      | The email to be updated to.                                                                          |
  | ` `*completion*` ` | Optionally; the block invoked when the request to send the verification email is complete, or fails. |

- `
  ``
  ``
  `

  ### [sendEmailVerification(beforeUpdatingEmail:actionCodeSettings:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)sendEmailVerificationBeforeUpdatingEmail:actionCodeSettings:completion:)

  `
  `  
  Send an email to verify the ownership of the account then update to the new email.  

  #### Declaration

  Swift  

      @objc
      open func sendEmailVerification(beforeUpdatingEmail email: String,
                                      actionCodeSettings: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.html? = nil,
                                      completion: ((Error?) -> Void)? = nil)

  #### Parameters

  |----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*email*` `              | The email to be updated to.                                                                                                                                                                       |
  | ` `*actionCodeSettings*` ` | An [ActionCodeSettings](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.html) object containing settings related to handling action codes. |
  | ` `*completion*` `         | Optionally; the block invoked when the request to send the verification email is complete, or fails.                                                                                              |

- `
  ``
  ``
  `

  ### [sendEmailVerification(beforeUpdatingEmail:actionCodeSettings:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/s:12FirebaseAuth4UserC21sendEmailVerification014beforeUpdatingE018actionCodeSettingsySS_AA06ActionjK0CSgtYaKF)

  `
  `  
  Send an email to verify the ownership of the account then update to the new email.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func sendEmailVerification(beforeUpdatingEmail newEmail: String,
                                      actionCodeSettings: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.html? = nil) async throws

  #### Parameters

  |----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*newEmail*` `           | The email to be updated to.                                                                                                                                                                       |
  | ` `*actionCodeSettings*` ` | An [ActionCodeSettings](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.html) object containing settings related to handling action codes. |

[## Internal implementations below](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/Internal-implementations-below)

- `
  ``
  ``
  `

  ### [providerID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(pl)FIRUserInfo(py)providerID)

  `
  `  

  #### Declaration

  Swift  

      open var providerID: String { get }

- `
  ``
  ``
  `

  ### [uid](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(py)uid)

  `
  `  
  The provider's user ID for the user.  

  #### Declaration

  Swift  

      open var uid: String

- `
  ``
  ``
  `

  ### [displayName](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(py)displayName)

  `
  `  
  The name of the user.  

  #### Declaration

  Swift  

      open var displayName: String?

- `
  ``
  ``
  `

  ### [photoURL](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(py)photoURL)

  `
  `  
  The URL of the user's profile photo.  

  #### Declaration

  Swift  

      open var photoURL: URL?

- `
  ``
  ``
  `

  ### [email](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(py)email)

  `
  `  
  The user's email address.  

  #### Declaration

  Swift  

      open var email: String?

- `
  ``
  ``
  `

  ### [phoneNumber](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(py)phoneNumber)

  `
  `  
  A phone number associated with the user.

  This property is only available for users authenticated via phone number auth.  

  #### Declaration

  Swift  

      open var phoneNumber: String?

[## NSSecureCoding](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/NSSecureCoding)

- `
  ``
  ``
  `

  ### [supportsSecureCoding](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(cpy)supportsSecureCoding)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static let supportsSecureCoding: Bool

- `
  ``
  ``
  `

  ### [encode(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)encodeWithCoder:)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public func encode(with coder: NSCoder)

- `
  ``
  ``
  `

  ### [init(coder:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#/c:@M@FirebaseAuth@objc(cs)FIRUser(im)initWithCoder:)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public required init?(coder: NSCoder)