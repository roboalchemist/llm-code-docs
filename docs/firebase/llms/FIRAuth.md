# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth.md.txt

# FirebaseAuth Framework Reference

# FIRAuth


    @interface FIRAuth : NSObject

Manages authentication for Firebase apps.
This class is thread-safe.
- `
  ``
  ``
  `

  ### [+auth](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(cm)auth)

  `
  `  
  Gets the auth object for the default Firebase app.
  The default Firebase app must have already been configured or an exception will be
  raised.  

  #### Declaration

  Objective-C  

      + (nonnull FIRAuth *)auth;

- `
  ``
  ``
  `

  ### [+authWithApp:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(cm)authWithApp:)

  `
  `  
  Gets the auth object for a `FirebaseApp`.  

  #### Declaration

  Objective-C  

      + (nonnull FIRAuth *)authWithApp:(nonnull FIRApp *)app;

  #### Parameters

  |-------------|---------------------------------------------------------------|
  | ` `*app*` ` | The app for which to retrieve the associated `Auth` instance. |

  #### Return Value

  The `Auth` instance associated with the given app.
- `
  ``
  ``
  `

  ### [app](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(py)app)

  `
  `  
  Gets the `FirebaseApp` object that this auth object is connected to.  

  #### Declaration

  Objective-C  

      @property (nonatomic, weak, readonly, nullable) FIRApp *app;

- `
  ``
  ``
  `

  ### [currentUser](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(py)currentUser)

  `
  `  
  Synchronously gets the cached current user, or null if there is none.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser.html *currentUser;

- `
  ``
  ``
  `

  ### [languageCode](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(py)languageCode)

  `
  `  
  The current user language code. This property can be set to the app's current language by
  calling `useAppLanguage()`.

  The string used to set this property must be a language code that follows BCP 47.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *languageCode;

- `
  ``
  ``
  `

  ### [settings](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(py)settings)

  `
  `  
  Contains settings related to the auth object.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthSettings.html *settings;

- `
  ``
  ``
  `

  ### [userAccessGroup](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(py)userAccessGroup)

  `
  `  
  The current user access group that the Auth instance is using. Default is nil.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *userAccessGroup;

- `
  ``
  ``
  `

  ### [shareAuthStateAcrossDevices](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(py)shareAuthStateAcrossDevices)

  `
  `  
  Contains shareAuthStateAcrossDevices setting related to the auth object.
  If userAccessGroup is not set, setting shareAuthStateAcrossDevices will
  have no effect. You should set shareAuthStateAcrossDevices to it's desired
  state and then set the userAccessGroup after.  

  #### Declaration

  Objective-C  

      @property (nonatomic) BOOL shareAuthStateAcrossDevices;

- `
  ``
  ``
  `

  ### [tenantID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(py)tenantID)

  `
  `  
  The tenant ID of the auth instance. nil if none is available.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *tenantID;

- `
  ``
  ``
  `

  ### [APNSToken](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(py)APNSToken)

  `
  `  
  The APNs token used for phone number authentication. The type of the token (production
  or sandbox) will be automatically detected based on your provisioning profile.
  This property is available on iOS only.
  If swizzling is disabled, the APNs Token must be set for phone number auth to work,
  by either setting this property or by calling `setAPNSToken(_:type:)`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, nullable) NSData *APNSToken;

- `
  ``
  ``
  `

  ### [customAuthDomain](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(py)customAuthDomain)

  `
  `  
  The custom authentication domain used to handle all sign-in redirects. End-users will see
  this domain when signing in. This domain must be allowlisted in the Firebase Console.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *customAuthDomain;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)init)

  `
  `  
  Please access auth instances using `Auth.auth()` and `Auth.auth(app:)`.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [-updateCurrentUser:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)updateCurrentUser:completion:)

  `
  `  
  Sets the [currentUser](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth.html#/c:objc(cs)FIRAuth(py)currentUser) on the receiver to the provided user object.  

  #### Declaration

  Objective-C  

      - (void)updateCurrentUser:(nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser.html *)user
                     completion:(nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |--------------------|-----------------------------------------------------------------------------------------------------------------------|
  | ` `*user*` `       | The user object to be set as the current user of the calling Auth instance.                                           |
  | ` `*completion*` ` | Optionally; a block invoked after the user of the calling Auth instance has been updated or an error was encountered. |

- `
  ``
  ``
  `

  ### [-fetchSignInMethodsForEmail:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)fetchSignInMethodsForEmail:completion:)

  `
  `  
  \[Deprecated\] Fetches the list of all sign-in methods previously used for the provided
  email address. This method returns an empty list when [Email Enumeration
  Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)
  is enabled, irrespective of the number of authentication methods available for the given email.

  Possible error codes:  

       + `AuthErrorCodeInvalidEmail` - Indicates the email address is malformed.

  See `AuthErrors` for a list of error codes that are common to all API methods.  

  #### Declaration

  Objective-C  

      - (void)fetchSignInMethodsForEmail:(nonnull NSString *)email
                              completion:
                                  (nullable void (^)(NSArray<NSString *> *_Nullable,
                                                     NSError *_Nullable))completion;

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*email*` `      | The email address for which to obtain a list of sign-in methods.                                                                                                                                     |
  | ` `*completion*` ` | Optionally; a block which is invoked when the list of sign in methods for the specified email address is ready or an error was encountered. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-signInWithEmail:password:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)signInWithEmail:password:completion:)

  `
  `  
  Signs in using an email address and password. When [Email Enumeration
  Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)
  is enabled, this method fails with FIRAuthErrorCodeInvalidCredentials in case of an invalid
  email/password.

  Possible error codes:  

       + `AuthErrorCodeOperationNotAllowed` - Indicates that email and password
           accounts are not enabled. Enable them in the Auth section of the
           Firebase console.
       + `AuthErrorCodeUserDisabled` - Indicates the user's account is disabled.
       + `AuthErrorCodeWrongPassword` - Indicates the user attempted
           sign in with an incorrect password.
       + `AuthErrorCodeInvalidEmail` - Indicates the email address is malformed.

  See `AuthErrors` for a list of error codes that are common to all API methods.  

  #### Declaration

  Objective-C  

      - (void)signInWithEmail:(nonnull NSString *)email
                     password:(nonnull NSString *)password
                   completion:(nullable void (^)(https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthDataResult.html *_Nullable,
                                                 NSError *_Nullable))completion;

  #### Parameters

  |--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*email*` `      | The user's email address.                                                                                                                     |
  | ` `*password*` `   | The user's password.                                                                                                                          |
  | ` `*completion*` ` | Optionally; a block which is invoked when the sign in flow finishes, or is canceled. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-signInWithEmail:link:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)signInWithEmail:link:completion:)

  `
  `  
  Signs in using an email address and email sign-in link.

  Possible error codes:  

      + `AuthErrorCodeOperationNotAllowed` - Indicates that email and email sign-in link
          accounts are not enabled. Enable them in the Auth section of the
          Firebase console.
      + `AuthErrorCodeUserDisabled` - Indicates the user's account is disabled.
      + `AuthErrorCodeInvalidEmail` - Indicates the email address is invalid.

  See `AuthErrors` for a list of error codes that are common to all API methods.  

  #### Declaration

  Objective-C  

      - (void)signInWithEmail:(nonnull NSString *)email
                         link:(nonnull NSString *)link
                   completion:(nullable void (^)(https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthDataResult.html *_Nullable,
                                                 NSError *_Nullable))completion;

  #### Parameters

  |--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*email*` `      | The user's email address.                                                                                                                     |
  | ` `*link*` `       | The email sign-in link.                                                                                                                       |
  | ` `*completion*` ` | Optionally; a block which is invoked when the sign in flow finishes, or is canceled. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-signInWithProvider:UIDelegate:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)signInWithProvider:UIDelegate:completion:)

  `
  `  
  Signs in using the provided auth provider instance.
  This method is available on iOS, macOS Catalyst, and tvOS only.

  Possible error codes:
  - `AuthErrorCodeOperationNotAllowed` - Indicates that email and password accounts are not enabled. Enable them in the Auth section of the Firebase console.
  - `AuthErrorCodeUserDisabled` - Indicates the user's account is disabled.
  - `AuthErrorCodeWebNetworkRequestFailed` - Indicates that a network request within a SFSafariViewController or WKWebView failed.
  - `AuthErrorCodeWebInternalError` - Indicates that an internal error occurred within a SFSafariViewController or WKWebView.
  - `AuthErrorCodeWebSignInUserInteractionFailure` - Indicates a general failure during a web sign-in flow.
  - `AuthErrorCodeWebContextAlreadyPresented` - Indicates that an attempt was made to present a new web context while one was already being presented.
  - `AuthErrorCodeWebContextCancelled` - Indicates that the URL presentation was cancelled prematurely by the user.
  - `AuthErrorCodeAccountExistsWithDifferentCredential` - Indicates the email asserted by the credential (e.g. the email in a Facebook access token) is already in use by an existing account, that cannot be authenticated with this sign-in method. Call fetchProvidersForEmail for this user's email and then prompt them to sign in with any of the sign-in providers returned. This error will only be thrown if the "One account per email address" setting is enabled in the Firebase console, under Auth settings.

  See `AuthErrors` for a list of error codes that are common to all API methods.  

  #### Declaration

  Objective-C  

      - (void)signInWithProvider:(nonnull id<https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRFederatedAuthProvider.html>)provider
                      UIDelegate:(nullable id<https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRAuthUIDelegate.html>)UIDelegate
                      completion:(nullable void (^)(https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthDataResult.html *_Nullable,
                                                    NSError *_Nullable))completion;

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*provider*` `   | An instance of an auth provider used to initiate the sign-in flow.                                                                                                       |
  | ` `*UIDelegate*` ` | Optionally an instance of a class conforming to the AuthUIDelegate protocol, this is used for presenting the web context. If nil, a default AuthUIDelegate will be used. |
  | ` `*completion*` ` | Optionally; a block which is invoked when the sign in flow finishes, or is canceled. Invoked asynchronously on the main thread in the future.                            |

- `
  ``
  ``
  `

  ### [-signInWithCredential:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)signInWithCredential:completion:)

  `
  `  
  Asynchronously signs in to Firebase with the given 3rd-party credentials (e.g. a Facebook
  login Access Token, a Google ID Token/Access Token pair, etc.) and returns additional
  identity provider data.

  Possible error codes:
  - `AuthErrorCodeInvalidCredential` - Indicates the supplied credential is invalid. This could happen if it has expired or it is malformed.
  - `AuthErrorCodeOperationNotAllowed` - Indicates that accounts with the identity provider represented by the credential are not enabled. Enable them in the Auth section of the Firebase console.
  - `AuthErrorCodeAccountExistsWithDifferentCredential` - Indicates the email asserted by the credential (e.g. the email in a Facebook access token) is already in use by an existing account, that cannot be authenticated with this sign-in method. Call fetchProvidersForEmail for this user's email and then prompt them to sign in with any of the sign-in providers returned. This error will only be thrown if the "One account per email address" setting is enabled in the Firebase console, under Auth settings.
  - `AuthErrorCodeUserDisabled` - Indicates the user's account is disabled.
  - `AuthErrorCodeWrongPassword` - Indicates the user attempted sign in with an incorrect password, if credential is of the type EmailPasswordAuthCredential.
  - `AuthErrorCodeInvalidEmail` - Indicates the email address is malformed.
  - `AuthErrorCodeMissingVerificationID` - Indicates that the phone auth credential was created with an empty verification ID.
  - `AuthErrorCodeMissingVerificationCode` - Indicates that the phone auth credential was created with an empty verification code.
  - `AuthErrorCodeInvalidVerificationCode` - Indicates that the phone auth credential was created with an invalid verification Code.
  - `AuthErrorCodeInvalidVerificationID` - Indicates that the phone auth credential was created with an invalid verification ID.
  - `AuthErrorCodeSessionExpired` - Indicates that the SMS code has expired.

  See `AuthErrors` for a list of error codes that are common to all API methods  

  #### Declaration

  Objective-C  

      - (void)signInWithCredential:(nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthCredential.html *)credential
                        completion:(nullable void (^)(https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthDataResult.html *_Nullable,
                                                      NSError *_Nullable))completion;

  #### Parameters

  |--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*credential*` ` | The credential supplied by the IdP.                                                                                                           |
  | ` `*completion*` ` | Optionally; a block which is invoked when the sign in flow finishes, or is canceled. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-signInAnonymouslyWithCompletion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)signInAnonymouslyWithCompletion:)

  `
  `  
  Asynchronously creates and becomes an anonymous user.

  If there is already an anonymous user signed in, that user will be returned instead.
  If there is any other existing user signed in, that user will be signed out.

  Possible error codes:  

      + `AuthErrorCodeOperationNotAllowed` - Indicates that anonymous accounts are
          not enabled. Enable them in the Auth section of the Firebase console.

  See `AuthErrors` for a list of error codes that are common to all API methods.  

  #### Declaration

  Objective-C  

      - (void)signInAnonymouslyWithCompletion:
          (nullable void (^)(https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthDataResult.html *_Nullable,
                             NSError *_Nullable))completion;

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | Optionally; a block which is invoked when the sign in finishes, or is canceled. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-signInWithCustomToken:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)signInWithCustomToken:completion:)

  `
  `  
  Asynchronously signs in to Firebase with the given Auth token.

  Possible error codes:  

      + `AuthErrorCodeInvalidCustomToken` - Indicates a validation error with
          the custom token.
      + `AuthErrorCodeCustomTokenMismatch` - Indicates the service account and the API key
          belong to different projects.

  See `AuthErrors` for a list of error codes that are common to all API methods.  

  #### Declaration

  Objective-C  

      - (void)signInWithCustomToken:(nonnull NSString *)token
                         completion:(nullable void (^)(https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthDataResult.html *_Nullable,
                                                       NSError *_Nullable))completion;

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*token*` `      | A self-signed custom auth token.                                                                                                         |
  | ` `*completion*` ` | Optionally; a block which is invoked when the sign in finishes, or is canceled. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-createUserWithEmail:password:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)createUserWithEmail:password:completion:)

  `
  `  
  Creates and, on success, signs in a user with the given email address and password.

  Possible error codes:  

      + `AuthErrorCodeInvalidEmail` - Indicates the email address is malformed.
      + `AuthErrorCodeEmailAlreadyInUse` - Indicates the email used to attempt sign up
          already exists. Call fetchProvidersForEmail to check which sign-in mechanisms the user
          used, and prompt the user to sign in with one of those.
      + `AuthErrorCodeOperationNotAllowed` - Indicates that email and password accounts
          are not enabled. Enable them in the Auth section of the Firebase console.
      + `AuthErrorCodeWeakPassword` - Indicates an attempt to set a password that is
          considered too weak. The NSLocalizedFailureReasonErrorKey field in the NSError.userInfo
          dictionary object will contain more detailed explanation that can be shown to the user.

  See `AuthErrors` for a list of error codes that are common to all API methods.  

  #### Declaration

  Objective-C  

      - (void)createUserWithEmail:(nonnull NSString *)email
                         password:(nonnull NSString *)password
                       completion:(nullable void (^)(https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthDataResult.html *_Nullable,
                                                     NSError *_Nullable))completion;

  #### Parameters

  |--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*email*` `      | The user's email address.                                                                                                                     |
  | ` `*password*` `   | The user's desired password.                                                                                                                  |
  | ` `*completion*` ` | Optionally; a block which is invoked when the sign up flow finishes, or is canceled. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-confirmPasswordResetWithCode:newPassword:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)confirmPasswordResetWithCode:newPassword:completion:)

  `
  `  
  Resets the password given a code sent to the user outside of the app and a new password
  for the user.

  Possible error codes:  

      + `AuthErrorCodeWeakPassword` - Indicates an attempt to set a password that is
          considered too weak.
      + `AuthErrorCodeOperationNotAllowed` - Indicates the administrator disabled sign
          in with the specified identity provider.
      + `AuthErrorCodeExpiredActionCode` - Indicates the OOB code is expired.
      + `AuthErrorCodeInvalidActionCode` - Indicates the OOB code is invalid.

  See `AuthErrors` for a list of error codes that are common to all API methods.  

  #### Declaration

  Objective-C  

      - (void)confirmPasswordResetWithCode:(nonnull NSString *)code
                               newPassword:(nonnull NSString *)newPassword
                                completion:
                                    (nonnull void (^)(NSError *_Nullable))completion;

  #### Parameters

  |---------------------|--------------------------------------------------------------------------------------------------------------------------|
  | ` `*newPassword*` ` | The new password.                                                                                                        |
  | ` `*completion*` `  | Optionally; a block which is invoked when the request finishes. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-checkActionCode:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)checkActionCode:completion:)

  `
  `  
  Checks the validity of an out of band code.  

  #### Declaration

  Objective-C  

      - (void)checkActionCode:(nonnull NSString *)code
                   completion:(nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeInfo.html *_Nullable,
                                                NSError *_Nullable))completion;

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------|
  | ` `*code*` `       | The out of band code to check validity.                                                                                  |
  | ` `*completion*` ` | Optionally; a block which is invoked when the request finishes. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-verifyPasswordResetCode:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)verifyPasswordResetCode:completion:)

  `
  `  
  Checks the validity of a verify password reset code.  

  #### Declaration

  Objective-C  

      - (void)verifyPasswordResetCode:(nonnull NSString *)code
                           completion:
                               (nonnull void (^)(NSString *_Nullable,
                                                 NSError *_Nullable))completion;

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------|
  | ` `*code*` `       | The password reset code to be verified.                                                                                  |
  | ` `*completion*` ` | Optionally; a block which is invoked when the request finishes. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-applyActionCode:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)applyActionCode:completion:)

  `
  `  
  Applies out of band code.

  This method will not work for out of band codes which require an additional parameter,
  such as password reset code.  

  #### Declaration

  Objective-C  

      - (void)applyActionCode:(nonnull NSString *)code
                   completion:(nonnull void (^)(NSError *_Nullable))completion;

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------|
  | ` `*code*` `       | The out of band code to be applied.                                                                                      |
  | ` `*completion*` ` | Optionally; a block which is invoked when the request finishes. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-sendPasswordResetWithEmail:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)sendPasswordResetWithEmail:completion:)

  `
  `  
  Initiates a password reset for the given email address. This method does not throw an
  error when there's no user account with the given email address and [Email Enumeration
  Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)
  is enabled.

  Possible error codes:  

       + `AuthErrorCodeInvalidRecipientEmail` - Indicates an invalid recipient email was
           sent in the request.
       + `AuthErrorCodeInvalidSender` - Indicates an invalid sender email is set in
           the console for this action.
       + `AuthErrorCodeInvalidMessagePayload` - Indicates an invalid email template for
           sending update email.

  #### Declaration

  Objective-C  

      - (void)sendPasswordResetWithEmail:(nonnull NSString *)email
                              completion:
                                  (nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------|
  | ` `*email*` `      | The email address of the user.                                                                                           |
  | ` `*completion*` ` | Optionally; a block which is invoked when the request finishes. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-sendPasswordResetWithEmail:actionCodeSettings:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)sendPasswordResetWithEmail:actionCodeSettings:completion:)

  `
  `  
  Initiates a password reset for the given email address and `ActionCodeSettings` object.

  Possible error codes:  

      + `AuthErrorCodeInvalidRecipientEmail` - Indicates an invalid recipient email was
          sent in the request.
      + `AuthErrorCodeInvalidSender` - Indicates an invalid sender email is set in
          the console for this action.
      + `AuthErrorCodeInvalidMessagePayload` - Indicates an invalid email template for
          sending update email.
      + `AuthErrorCodeMissingIosBundleID` - Indicates that the iOS bundle ID is missing when
          `handleCodeInApp` is set to true.
      + `AuthErrorCodeMissingAndroidPackageName` - Indicates that the android package name
          is missing when the `androidInstallApp` flag is set to true.
      + `AuthErrorCodeUnauthorizedDomain` - Indicates that the domain specified in the
          continue URL is not allowlisted in the Firebase console.
      + `AuthErrorCodeInvalidContinueURI` - Indicates that the domain specified in the
          continue URL is not valid.

  #### Declaration

  Objective-C  

      - (void)sendPasswordResetWithEmail:(nonnull NSString *)email
                      actionCodeSettings:
                          (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeSettings.html *)actionCodeSettings
                              completion:
                                  (nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |----------------------------|--------------------------------------------------------------------------------------------------------------------------|
  | ` `*email*` `              | The email address of the user.                                                                                           |
  | ` `*actionCodeSettings*` ` | An `ActionCodeSettings` object containing settings related to handling action codes.                                     |
  | ` `*completion*` `         | Optionally; a block which is invoked when the request finishes. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-sendSignInLinkToEmail:actionCodeSettings:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)sendSignInLinkToEmail:actionCodeSettings:completion:)

  `
  `  
  Sends a sign in with email link to provided email address.  

  #### Declaration

  Objective-C  

      - (void)sendSignInLinkToEmail:(nonnull NSString *)email
                 actionCodeSettings:
                     (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeSettings.html *)actionCodeSettings
                         completion:(nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |----------------------------|--------------------------------------------------------------------------------------------------------------------------|
  | ` `*email*` `              | The email address of the user.                                                                                           |
  | ` `*actionCodeSettings*` ` | An `ActionCodeSettings` object containing settings related to handling action codes.                                     |
  | ` `*completion*` `         | Optionally; a block which is invoked when the request finishes. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-signOut:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)signOut:)

  `
  `  
  Signs out the current user.

  Possible error codes:  

      + `AuthErrorCodeKeychainError` - Indicates an error occurred when accessing the
          keychain. The `NSLocalizedFailureReasonErrorKey` field in the `userInfo`
          dictionary will contain more information about the error encountered.

  #### Declaration

  Objective-C  

      - (BOOL)signOut:(NSError *_Nullable *_Nullable)error;

  #### Parameters

  |---------------|----------------------------------------------------------------------------------------------------------------------|
  | ` `*error*` ` | Optionally; if an error occurs, upon return contains an NSError object that describes the problem; is nil otherwise. |

  #### Return Value

  @YES when the sign out request was successful. @NO otherwise.
- `
  ``
  ``
  `

  ### [-isSignInWithEmailLink:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)isSignInWithEmailLink:)

  `
  `  
  Checks if link is an email sign-in link.  

  #### Declaration

  Objective-C  

      - (BOOL)isSignInWithEmailLink:(nonnull NSString *)link;

  #### Parameters

  |--------------|-------------------------|
  | ` `*link*` ` | The email sign-in link. |

  #### Return Value

  Returns true when the link passed matches the expected format of an email sign-in link.
- `
  ``
  ``
  `

  ### [-addAuthStateDidChangeListener:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)addAuthStateDidChangeListener:)

  `
  `  
  Registers a block as an "auth state did change" listener. To be invoked when:
  - The block is registered as a listener,
  - A user with a different UID from the current user has signed in, or
  - The current user has signed out.

  The block is invoked immediately after adding it according to it's standard invocation
  semantics, asynchronously on the main thread. Users should pay special attention to
  making sure the block does not inadvertently retain objects which should not be retained by
  the long-lived block. The block itself will be retained by `Auth` until it is
  unregistered or until the `Auth` instance is otherwise deallocated.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Type-Definitions.html#/c:FIRAuth.h@T@FIRAuthStateDidChangeListenerHandle)addAuthStateDidChangeListener:
          (nonnull void (^)(FIRAuth *_Nonnull, https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser.html *_Nullable))listener;

  #### Parameters

  |------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*listener*` ` | The block to be invoked. The block is always invoked asynchronously on the main thread, even for it's initial invocation after having been added as a listener. |

  #### Return Value

  A handle useful for manually unregistering the block as a listener.
- `
  ``
  ``
  `

  ### [-removeAuthStateDidChangeListener:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)removeAuthStateDidChangeListener:)

  `
  `  
  Unregisters a block as an "auth state did change" listener.  

  #### Declaration

  Objective-C  

      - (void)removeAuthStateDidChangeListener:
          (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Type-Definitions.html#/c:FIRAuth.h@T@FIRAuthStateDidChangeListenerHandle)listenerHandle;

  #### Parameters

  |------------------------|------------------------------|
  | ` `*listenerHandle*` ` | The handle for the listener. |

- `
  ``
  ``
  `

  ### [-addIDTokenDidChangeListener:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)addIDTokenDidChangeListener:)

  `
  `  
  Registers a block as an "ID token did change" listener. To be invoked when:
  - The block is registered as a listener,
  - A user with a different UID from the current user has signed in,
  - The ID token of the current user has been refreshed, or
  - The current user has signed out.

  The block is invoked immediately after adding it according to it's standard invocation
  semantics, asynchronously on the main thread. Users should pay special attention to
  making sure the block does not inadvertently retain objects which should not be retained by
  the long-lived block. The block itself will be retained by `Auth` until it is
  unregistered or until the `Auth` instance is otherwise deallocated.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Type-Definitions.html#/c:FIRAuth.h@T@FIRIDTokenDidChangeListenerHandle)addIDTokenDidChangeListener:
          (nonnull void (^)(FIRAuth *_Nonnull, https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser.html *_Nullable))listener;

  #### Parameters

  |------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*listener*` ` | The block to be invoked. The block is always invoked asynchronously on the main thread, even for it's initial invocation after having been added as a listener. |

  #### Return Value

  A handle useful for manually unregistering the block as a listener.
- `
  ``
  ``
  `

  ### [-removeIDTokenDidChangeListener:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)removeIDTokenDidChangeListener:)

  `
  `  
  Unregisters a block as an "ID token did change" listener.  

  #### Declaration

  Objective-C  

      - (void)removeIDTokenDidChangeListener:
          (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Type-Definitions.html#/c:FIRAuth.h@T@FIRIDTokenDidChangeListenerHandle)listenerHandle;

  #### Parameters

  |------------------------|------------------------------|
  | ` `*listenerHandle*` ` | The handle for the listener. |

- `
  ``
  ``
  `

  ### [-useAppLanguage](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)useAppLanguage)

  `
  `  
  Sets [languageCode](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth.html#/c:objc(cs)FIRAuth(py)languageCode) to the app's current language.  

  #### Declaration

  Objective-C  

      - (void)useAppLanguage;

- `
  ``
  ``
  `

  ### [-useEmulatorWithHost:port:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)useEmulatorWithHost:port:)

  `
  `  
  Configures Firebase Auth to connect to an emulated host instead of the remote backend.  

  #### Declaration

  Objective-C  

      - (void)useEmulatorWithHost:(nonnull NSString *)host port:(NSInteger)port;

- `
  ``
  ``
  `

  ### [-canHandleURL:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)canHandleURL:)

  `
  `  
  Whether the specific URL is handled by `Auth` .
  This method is available on iOS only.  

  #### Declaration

  Objective-C  

      - (BOOL)canHandleURL:(nonnull NSURL *)URL;

  #### Parameters

  |-------------|------------------------------------------------------------------------------|
  | ` `*URL*` ` | The URL received by the application delegate from any of the openURL method. |

  #### Return Value

  Whether or the URL is handled. YES means the URL is for Firebase Auth
  so the caller should ignore the URL from further processing, and NO means the
  the URL is for the app (or another library) so the caller should continue handling
  this URL as usual.
  If swizzling is disabled, URLs received by the application delegate must be forwarded
  to this method for phone number auth to work.
- `
  ``
  ``
  `

  ### [-setAPNSToken:type:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)setAPNSToken:type:)

  `
  `  
  Sets the APNs token along with its type.
  This method is available on iOS only.
  If swizzling is disabled, the APNs Token must be set for phone number auth to work,
  by either setting calling this method or by setting the [APNSToken](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth.html#/c:objc(cs)FIRAuth(py)APNSToken) property.  

  #### Declaration

  Objective-C  

      - (void)setAPNSToken:(nonnull NSData *)token type:(https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthAPNSTokenType.html)type;

- `
  ``
  ``
  `

  ### [-canHandleNotification:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)canHandleNotification:)

  `
  `  
  Whether the specific remote notification is handled by `Auth` .
  This method is available on iOS only.  

  #### Declaration

  Objective-C  

      - (BOOL)canHandleNotification:(nonnull NSDictionary *)userInfo;

  #### Parameters

  |------------------|---------------------------------------------------------------------------------|
  | ` `*userInfo*` ` | A dictionary that contains information related to the notification in question. |

  #### Return Value

  Whether or the notification is handled. A return value of true means the notification
  is for Firebase Auth so the caller should ignore the notification from further processing,
  and false means the notification is for the app (or another library) so the caller
  should continue handling this notification as usual.
  If swizzling is disabled, related remote notifications must be forwarded to this method
  for phone number auth to work.
- `
  ``
  ``
  `

  ### [-revokeTokenWithAuthorizationCode:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)revokeTokenWithAuthorizationCode:completion:)

  `
  `  
  Revoke the users token with authorization code.  

  #### Declaration

  Objective-C  

      - (void)revokeTokenWithAuthorizationCode:(nonnull NSString *)authorizationCode
                                    completion:(nullable void (^)(NSError *_Nullable))
                                                   completion;

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | (Optional) the block invoked when the request to revoke the token is complete, or fails. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [-initializeRecaptchaConfigWithCompletion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)initializeRecaptchaConfigWithCompletion:)

  `
  `  
  Initializes reCAPTCHA using the settings configured for the project or
  tenant.

  If you change the tenant ID of the `Auth` instance, the configuration will be
  reloaded.  

  #### Declaration

  Objective-C  

      - (void)initializeRecaptchaConfigWithCompletion:
          (nullable void (^)(NSError *_Nullable))completion;

[## User sharing](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/User-sharing)

- `
  ``
  ``
  `

  ### [-useUserAccessGroup:error:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)useUserAccessGroup:error:)

  `
  `  
  Switch userAccessGroup and current user to the given accessGroup and the user stored in
  it.  

  #### Declaration

  Objective-C  

      - (BOOL)useUserAccessGroup:(NSString *_Nullable)accessGroup
                           error:(NSError *_Nullable *_Nullable)outError;

- `
  ``
  ``
  `

  ### [-getStoredUserForAccessGroup:error:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth#/c:objc(cs)FIRAuth(im)getStoredUserForAccessGroup:error:)

  `
  `  
  Get the stored user in the given accessGroup.  
  Note
  This API is not supported on tvOS when [shareAuthStateAcrossDevices](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth.html#/c:objc(cs)FIRAuth(py)shareAuthStateAcrossDevices) is set to `true`. This case will return `nil`. Please refer to <https://github.com/firebase/firebase-ios-sdk/issues/8878> for details.  

  #### Declaration

  Objective-C  

      - (nullable https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser.html *)
          getStoredUserForAccessGroup:(NSString *_Nullable)accessGroup
                                error:(NSError *_Nullable *_Nullable)outError;