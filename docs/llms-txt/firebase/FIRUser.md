# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser.md.txt

# FirebaseAuth Framework Reference

# FIRUser


    @interface FIRUser : NSObject <https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRUserInfo.html>

Represents a user. Firebase Auth does not attempt to validate users
when loading them from the keychain. Invalidated users (such as those
whose passwords have been changed on another client) are automatically
logged out when an auth-dependent operation is attempted or when the
ID token is automatically refreshed.
This class is thread-safe.
- `
  ``
  ``
  `

  ### [anonymous](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(py)anonymous)

  `
  `  
  Indicates the user represents an anonymous user.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, getter=isAnonymous) BOOL anonymous;

- `
  ``
  ``
  `

  ### [emailVerified](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(py)emailVerified)

  `
  `  
  Indicates the email address associated with this user has been verified.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, getter=isEmailVerified) BOOL emailVerified;

- `
  ``
  ``
  `

  ### [refreshToken](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(py)refreshToken)

  `
  `  
  A refresh token; useful for obtaining new access tokens independently.
  This property should only be used for advanced scenarios, and is not typically needed.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *refreshToken;

- `
  ``
  ``
  `

  ### [providerData](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(py)providerData)

  `
  `  
  Profile data for each identity provider, if any.
  This data is cached on sign-in and updated when linking or unlinking.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nonnull) NSArray<id<https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRUserInfo.html>> *providerData;

- `
  ``
  ``
  `

  ### [metadata](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(py)metadata)

  `
  `  
  Metadata associated with the Firebase user in question.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nonnull) https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUserMetadata.html *metadata;

- `
  ``
  ``
  `

  ### [tenantID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(py)tenantID)

  `
  `  
  The tenant ID of the current user. nil if none is available.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *tenantID;

- `
  ``
  ``
  `

  ### [multiFactor](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(py)multiFactor)

  `
  `  
  Multi factor object associated with the user.
  This property is available on iOS only.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nonnull) https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactor.html *multiFactor;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)init)

  `
  `  
  This class should not be instantiated.
  To retrieve the current user, use `Auth.currentUser`. To sign a user
  in or out, use the methods on `Auth`.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [-updateEmail:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)updateEmail:completion:)

  `
  `  
  \[Deprecated\] Updates the email address for the user. On success, the cached user profile
  data is updated. Throws FIRAuthErrorCodeInvalidCredentials error when [Email Enumeration
  Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)
  is enabled.
  May fail if there is already an account with this email address that was created using
  email and password authentication.

  Possible error codes:  

       + `AuthErrorCodeInvalidRecipientEmail` - Indicates an invalid recipient email was
           sent in the request.
       + `AuthErrorCodeInvalidSender` - Indicates an invalid sender email is set in
           the console for this action.
       + `AuthErrorCodeInvalidMessagePayload` - Indicates an invalid email template for
           sending update email.
       + `AuthErrorCodeEmailAlreadyInUse` - Indicates the email is already in use by another
           account.
       + `AuthErrorCodeInvalidEmail` - Indicates the email address is malformed.
       + `AuthErrorCodeRequiresRecentLogin` - Updating a user's email is a security
           sensitive operation that requires a recent login from the user. This error indicates
           the user has not signed in recently enough. To resolve, reauthenticate the user by
           calling `reauthenticate(with:)`.

  See `AuthErrors` for a list of error codes that are common to all `User` methods.  

  #### Declaration

  Objective-C  

      - (void)updateEmail:(nonnull NSString *)email
               completion:(nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |--------------------|-----------------------------------------------------------------------------------------------------------------------------------|
  | ` `*email*` `      | The email address for the user.                                                                                                   |
  | ` `*completion*` ` | Optionally; the block invoked when the user profile change has finished. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-updatePassword:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)updatePassword:completion:)

  `
  `  
  Updates the password for the user. On success, the cached user profile data is updated.

  Possible error codes:  

      + `AuthErrorCodeOperationNotAllowed` - Indicates the administrator disabled
          sign in with the specified identity provider.
      + `AuthErrorCodeRequiresRecentLogin` - Updating a user's password is a security
          sensitive operation that requires a recent login from the user. This error indicates
          the user has not signed in recently enough. To resolve, reauthenticate the user by
          calling `reauthenticate(with:)`.
      + `AuthErrorCodeWeakPassword` - Indicates an attempt to set a password that is
          considered too weak. The `NSLocalizedFailureReasonErrorKey` field in the `userInfo`
          dictionary object will contain more detailed explanation that can be shown to the user.

  See `AuthErrors` for a list of error codes that are common to all `User` methods.  

  #### Declaration

  Objective-C  

      - (void)updatePassword:(nonnull NSString *)password
                  completion:(nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |--------------------|-----------------------------------------------------------------------------------------------------------------------------------|
  | ` `*password*` `   | The new password for the user.                                                                                                    |
  | ` `*completion*` ` | Optionally; the block invoked when the user profile change has finished. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-updatePhoneNumberCredential:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)updatePhoneNumberCredential:completion:)

  `
  `  
  Updates the phone number for the user. On success, the cached user profile data is
  updated.
  This method is available on iOS only.

  Possible error codes:  

      + `AuthErrorCodeRequiresRecentLogin` - Updating a user's phone number is a security
          sensitive operation that requires a recent login from the user. This error indicates
          the user has not signed in recently enough. To resolve, reauthenticate the user by
          calling `reauthenticate(with:)`.

  See `AuthErrors` for a list of error codes that are common to all `User` methods.  

  #### Declaration

  Objective-C  

      - (void)updatePhoneNumberCredential:
                  (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneAuthCredential.html *)phoneNumberCredential
                               completion:
                                   (nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*phoneNumberCredential*` ` | The new phone number credential corresponding to the phone number to be added to the Firebase account, if a phone number is already linked to the account this new phone number will replace it. |
  | ` `*completion*` `            | Optionally; the block invoked when the user profile change has finished. Invoked asynchronously on the main thread in the future.                                                                |

- `
  ``
  ``
  `

  ### [-profileChangeRequest](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)profileChangeRequest)

  `
  `  
  Creates an object which may be used to change the user's profile data.

  Set the properties of the returned object, then call
  `UserProfileChangeRequest.commitChanges()` to perform the updates atomically.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUserProfileChangeRequest.html *)profileChangeRequest;

  #### Return Value

  An object which may be used to change the user's profile data atomically.
- `
  ``
  ``
  `

  ### [-reloadWithCompletion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)reloadWithCompletion:)

  `
  `  
  Reloads the user's profile data from the server.

  May fail with a `AuthErrorCodeRequiresRecentLogin` error code. In this case
  you should call `reauthenticate(with:)` before re-invoking
  `updateEmail(to:)`.

  See `AuthErrors` for a list of error codes that are common to all API methods.  

  #### Declaration

  Objective-C  

      - (void)reloadWithCompletion:(nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |--------------------|----------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | Optionally; the block invoked when the reload has finished. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-reauthenticateWithCredential:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)reauthenticateWithCredential:completion:)

  `
  `  
  Renews the user's authentication tokens by validating a fresh set of credentials supplied
  by the user and returns additional identity provider data.

  If the user associated with the supplied credential is different from the current user,
  or if the validation of the supplied credentials fails; an error is returned and the current
  user remains signed in.

  Possible error codes:  

      + `AuthErrorCodeInvalidCredential` - Indicates the supplied credential is invalid.
          This could happen if it has expired or it is malformed.
      + `AuthErrorCodeOperationNotAllowed` - Indicates that accounts with the
          identity provider represented by the credential are not enabled. Enable them in the
          Auth section of the Firebase console.
      + `AuthErrorCodeEmailAlreadyInUse` -  Indicates the email asserted by the credential
          (e.g. the email in a Facebook access token) is already in use by an existing account,
          that cannot be authenticated with this method. This error will only be thrown if the
        "One account per email address" setting is enabled in the Firebase console, under Auth
        settings. Please note that the error code raised in this specific situation may not be
        the same on Web and Android.
      + `AuthErrorCodeUserDisabled` - Indicates the user's account is disabled.
      + `AuthErrorCodeWrongPassword` - Indicates the user attempted reauthentication with
          an incorrect password, if credential is of the type `EmailPasswordAuthCredential`.
      + `AuthErrorCodeUserMismatch` -  Indicates that an attempt was made to
          reauthenticate with a user which is not the current user.
      + `AuthErrorCodeInvalidEmail` - Indicates the email address is malformed.

  See [FIRAuthErrors](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes.html#/c:objc(cs)FIRAuthErrors) for a list of error codes that are common to all API methods.  

  #### Declaration

  Objective-C  

      - (void)reauthenticateWithCredential:(nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthCredential.html *)credential
                                completion:
                                    (nullable void (^)(https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthDataResult.html *_Nullable,
                                                       NSError *_Nullable))completion;

  #### Parameters

  |--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*credential*` ` | A user-supplied credential, which will be validated by the server. This can be a successful third-party identity provider sign-in, or an email address and password. |
  | ` `*completion*` ` | Optionally; the block invoked when the re-authentication operation has finished. Invoked asynchronously on the main thread in the future.                            |

- `
  ``
  ``
  `

  ### [-reauthenticateWithProvider:UIDelegate:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)reauthenticateWithProvider:UIDelegate:completion:)

  `
  `  
  Renews the user's authentication using the provided auth provider instance.
  This method is available on iOS, macOS Catalyst, and tvOS only.  

  #### Declaration

  Objective-C  

      - (void)reauthenticateWithProvider:
                  (nonnull id<https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRFederatedAuthProvider.html>)provider
                              UIDelegate:(nullable id<https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRAuthUIDelegate.html>)UIDelegate
                              completion:
                                  (nullable void (^)(https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthDataResult.html *_Nullable,
                                                     NSError *_Nullable))completion;

  #### Parameters

  |--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*provider*` `   | An instance of an auth provider used to initiate the reauthenticate flow.                                                                                            |
  | ` `*UIDelegate*` ` | Optionally an instance of a class conforming to the `AuthUIDelegate` protocol, used for presenting the web context. If nil, a default `AuthUIDelegate` will be used. |
  | ` `*completion*` ` | Optionally; a block which is invoked when the reauthenticate flow finishes, or is canceled. Invoked asynchronously on the main thread in the future.                 |

- `
  ``
  ``
  `

  ### [-getIDTokenResultWithCompletion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)getIDTokenResultWithCompletion:)

  `
  `  
  Retrieves the Firebase authentication token, possibly refreshing it if it has expired.

  See `AuthErrors` for a list of error codes that are common to all API methods.  

  #### Declaration

  Objective-C  

      - (void)getIDTokenResultWithCompletion:
          (nullable void (^)(https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthTokenResult.html *_Nullable,
                             NSError *_Nullable))completion;

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | Optionally; the block invoked when the token is available. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-getIDTokenResultForcingRefresh:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)getIDTokenResultForcingRefresh:completion:)

  `
  `  
  Retrieves the Firebase authentication token, possibly refreshing it if it has expired.

  The authentication token will be refreshed (by making a network request) if it has
  expired, or if `forceRefresh` is YES.

  See `AuthErrors` for a list of error codes that are common to all API methods.  

  #### Declaration

  Objective-C  

      - (void)getIDTokenResultForcingRefresh:(BOOL)forceRefresh
                                  completion:(nullable void (^)(
                                                 https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthTokenResult.html *_Nullable,
                                                 NSError *_Nullable))completion;

  #### Parameters

  |----------------------|---------------------------------------------------------------------------------------------------------------------|
  | ` `*forceRefresh*` ` | Forces a token refresh. Useful if the token becomes invalid for some reason other than an expiration.               |
  | ` `*completion*` `   | Optionally; the block invoked when the token is available. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-getIDTokenWithCompletion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)getIDTokenWithCompletion:)

  `
  `  
  Retrieves the Firebase authentication token, possibly refreshing it if it has expired.

  See `AuthErrors` for a list of error codes that are common to all API methods.  

  #### Declaration

  Objective-C  

      - (void)getIDTokenWithCompletion:
          (nullable void (^)(NSString *_Nullable, NSError *_Nullable))completion;

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | Optionally; the block invoked when the token is available. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-getIDTokenForcingRefresh:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)getIDTokenForcingRefresh:completion:)

  `
  `  
  Retrieves the Firebase authentication token, possibly refreshing it if it has expired.

  The authentication token will be refreshed (by making a network request) if it has
  expired, or if `forceRefresh` is true.

  See `AuthErrors` for a list of error codes that are common to all API methods.  

  #### Declaration

  Objective-C  

      - (void)getIDTokenForcingRefresh:(BOOL)forceRefresh
                            completion:
                                (nullable void (^)(NSString *_Nullable,
                                                   NSError *_Nullable))completion;

  #### Parameters

  |----------------------|---------------------------------------------------------------------------------------------------------------------|
  | ` `*forceRefresh*` ` | Forces a token refresh. Useful if the token becomes invalid for some reason other than an expiration.               |
  | ` `*completion*` `   | Optionally; the block invoked when the token is available. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-linkWithCredential:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)linkWithCredential:completion:)

  `
  `  
  Associates a user account from a third-party identity provider with this user and
  returns additional identity provider data.

  Possible error codes:  

      + `AuthErrorCodeProviderAlreadyLinked` - Indicates an attempt to link a provider of a
          type already linked to this account.
      + `AuthErrorCodeCredentialAlreadyInUse` - Indicates an attempt to link with a
          credential that has already been linked with a different Firebase account.
      + `AuthErrorCodeOperationNotAllowed` - Indicates that accounts with the identity
          provider represented by the credential are not enabled. Enable them in the Auth section
          of the Firebase console.

  This method may also return error codes associated with `updateEmail(to:)` and
  `updatePassword(to:)` on `User`.

  See `AuthErrors` for a list of error codes that are common to all `User` methods.  

  #### Declaration

  Objective-C  

      - (void)linkWithCredential:(nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthCredential.html *)credential
                      completion:(nullable void (^)(https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthDataResult.html *_Nullable,
                                                    NSError *_Nullable))completion;

  #### Parameters

  |--------------------|----------------------------------------------------------------------------------------------------------------------------------|
  | ` `*credential*` ` | The credential for the identity provider.                                                                                        |
  | ` `*completion*` ` | Optionally; the block invoked when the unlinking is complete, or fails. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-linkWithProvider:UIDelegate:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)linkWithProvider:UIDelegate:completion:)

  `
  `  
  link the user with the provided auth provider instance.
  This method is available on iOS, macOS Catalyst, and tvOS only.  

  #### Declaration

  Objective-C  

      - (void)linkWithProvider:(nonnull id<https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRFederatedAuthProvider.html>)provider
                    UIDelegate:(nullable id<https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRAuthUIDelegate.html>)UIDelegate
                    completion:(nullable void (^)(https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthDataResult.html *_Nullable,
                                                  NSError *_Nullable))completion;

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*provider*` `   | An instance of an auth provider used to initiate the link flow.                                                                                                     |
  | ` `*UIDelegate*` ` | Optionally an instance of a class conforming to the `AuthUIDelegate` protocol used for presenting the web context. If nil, a default `AuthUIDelegate` will be used. |
  | ` `*completion*` ` | Optionally; a block which is invoked when the link flow finishes, or is canceled. Invoked asynchronously on the main thread in the future.                          |

- `
  ``
  ``
  `

  ### [-unlinkFromProvider:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)unlinkFromProvider:completion:)

  `
  `  
  Disassociates a user account from a third-party identity provider with this user.

  Possible error codes:  

      + `AuthErrorCodeNoSuchProvider` - Indicates an attempt to unlink a provider
          that is not linked to the account.
      + `AuthErrorCodeRequiresRecentLogin` - Updating email is a security sensitive
          operation that requires a recent login from the user. This error indicates the user
          has not signed in recently enough. To resolve, reauthenticate the user by calling
          `reauthenticate(with:)`.

  See `AuthErrors` for a list of error codes that are common to all `User` methods.  

  #### Declaration

  Objective-C  

      - (void)unlinkFromProvider:(nonnull NSString *)provider
                      completion:(nullable void (^)(FIRUser *_Nullable,
                                                    NSError *_Nullable))completion;

  #### Parameters

  |--------------------|----------------------------------------------------------------------------------------------------------------------------------|
  | ` `*provider*` `   | The provider ID of the provider to unlink.                                                                                       |
  | ` `*completion*` ` | Optionally; the block invoked when the unlinking is complete, or fails. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-sendEmailVerificationWithCompletion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)sendEmailVerificationWithCompletion:)

  `
  `  
  Initiates email verification for the user.

  Possible error codes:  

      + `AuthErrorCodeInvalidRecipientEmail` - Indicates an invalid recipient email was
          sent in the request.
      + `AuthErrorCodeInvalidSender` - Indicates an invalid sender email is set in
          the console for this action.
      + `AuthErrorCodeInvalidMessagePayload` - Indicates an invalid email template for
          sending update email.
      + `AuthErrorCodeUserNotFound` - Indicates the user account was not found.

  See `AuthErrors` for a list of error codes that are common to all `User` methods.  

  #### Declaration

  Objective-C  

      - (void)sendEmailVerificationWithCompletion:
          (nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | Optionally; the block invoked when the request to send an email verification is complete, or fails. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-sendEmailVerificationWithActionCodeSettings:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)sendEmailVerificationWithActionCodeSettings:completion:)

  `
  `  
  Initiates email verification for the user.

  Possible error codes:  

      + `AuthErrorCodeInvalidRecipientEmail` - Indicates an invalid recipient email was
          sent in the request.
      + `AuthErrorCodeInvalidSender` - Indicates an invalid sender email is set in
          the console for this action.
      + `AuthErrorCodeInvalidMessagePayload` - Indicates an invalid email template for
          sending update email.
      + `AuthErrorCodeUserNotFound` - Indicates the user account was not found.
      + `AuthErrorCodeMissingIosBundleID` - Indicates that the iOS bundle ID is missing when
          a iOS App Store ID is provided.
      + `AuthErrorCodeMissingAndroidPackageName` - Indicates that the android package name
          is missing when the `androidInstallApp` flag is set to true.
      + `AuthErrorCodeUnauthorizedDomain` - Indicates that the domain specified in the
          continue URL is not allowlisted in the Firebase console.
      + `AuthErrorCodeInvalidContinueURI` - Indicates that the domain specified in the
          continue URL is not valid.

  #### Declaration

  Objective-C  

      - (void)sendEmailVerificationWithActionCodeSettings:
                  (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeSettings.html *)actionCodeSettings
                                               completion:
                                                   (nullable void (^)(
                                                       NSError *_Nullable))completion;

  #### Parameters

  |----------------------------|--------------------------------------------------------------------------------------|
  | ` `*actionCodeSettings*` ` | An `ActionCodeSettings` object containing settings related to handling action codes. |

- `
  ``
  ``
  `

  ### [-deleteWithCompletion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)deleteWithCompletion:)

  `
  `  
  Deletes the user account (also signs out the user, if this was the current user).

  Possible error codes:  

      + `AuthErrorCodeRequiresRecentLogin` - Updating email is a security sensitive
          operation that requires a recent login from the user. This error indicates the user
          has not signed in recently enough. To resolve, reauthenticate the user by calling
          `reauthenticate(with:)`.

  See `AuthErrors` for a list of error codes that are common to all `User` methods.  

  #### Declaration

  Objective-C  

      - (void)deleteWithCompletion:(nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | Optionally; the block invoked when the request to delete the account is complete, or fails. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-sendEmailVerificationBeforeUpdatingEmail:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)sendEmailVerificationBeforeUpdatingEmail:completion:)

  `
  `  
  Send an email to verify the ownership of the account then update to the new email.  

  #### Declaration

  Objective-C  

      - (void)sendEmailVerificationBeforeUpdatingEmail:(nonnull NSString *)email
                                            completion:
                                                (nullable void (^)(
                                                    NSError *_Nullable))completion;

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------|
  | ` `*email*` `      | The email to be updated to.                                                                          |
  | ` `*completion*` ` | Optionally; the block invoked when the request to send the verification email is complete, or fails. |

- `
  ``
  ``
  `

  ### [-sendEmailVerificationBeforeUpdatingEmail:actionCodeSettings:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser#/c:objc(cs)FIRUser(im)sendEmailVerificationBeforeUpdatingEmail:actionCodeSettings:completion:)

  `
  `  
  Send an email to verify the ownership of the account then update to the new email.  

  #### Declaration

  Objective-C  

      - (void)
          sendEmailVerificationBeforeUpdatingEmail:(nonnull NSString *)email
                                actionCodeSettings:(nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeSettings.html *)
                                                       actionCodeSettings
                                        completion:(nullable void (^)(
                                                       NSError *_Nullable))completion;

  #### Parameters

  |----------------------------|------------------------------------------------------------------------------------------------------|
  | ` `*email*` `              | The email to be updated to.                                                                          |
  | ` `*actionCodeSettings*` ` | An `ActionCodeSettings` object containing settings related to handling action codes.                 |
  | ` `*completion*` `         | Optionally; the block invoked when the request to send the verification email is complete, or fails. |