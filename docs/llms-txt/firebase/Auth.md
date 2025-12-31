# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth.md.txt

# FirebaseAuth Framework Reference

# Auth

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @preconcurrency
    @objc(FIRAuth)
    open class Auth : NSObject

    extension Auth: UISceneDelegate

    extension Auth: UIApplicationDelegate

    extension Auth: AuthInterop

Manages authentication for Firebase apps.

This class is thread-safe.
- `
  ``
  ``
  `

  ### [auth()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(cm)auth)

  `
  `  
  Gets the auth object for the default Firebase app.

  The default Firebase app must have already been configured or an exception will be raised.  

  #### Declaration

  Swift  

      @objc
      open class func auth() -> Auth

- `
  ``
  ``
  `

  ### [auth(app:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(cm)authWithApp:)

  `
  `  
  Gets the auth object for a `FirebaseApp`.  

  #### Declaration

  Swift  

      @objc
      open class func auth(app: FirebaseApp) -> Auth

  #### Parameters

  |-------------|---------------------------------------------------------------|
  | ` `*app*` ` | The app for which to retrieve the associated `Auth` instance. |

  #### Return Value

  The `Auth` instance associated with the given app.
- `
  ``
  ``
  `

  ### [app](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(py)app)

  `
  `  
  Gets the `FirebaseApp` object that this auth object is connected to.  

  #### Declaration

  Swift  

      @objc
      public internal(set) weak var app: FirebaseApp? { get }

- `
  ``
  ``
  `

  ### [currentUser](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(py)currentUser)

  `
  `  
  Synchronously gets the cached current user, or null if there is none.  

  #### Declaration

  Swift  

      @objc
      public var currentUser: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html? { get }

- `
  ``
  ``
  `

  ### [languageCode](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(py)languageCode)

  `
  `  
  The current user language code.

  This property can be set to the app's current language by
  calling [useAppLanguage()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth.html#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)useAppLanguage).

  The string used to set this property must be a language code that follows BCP 47.  

  #### Declaration

  Swift  

      @objc
      open var languageCode: String? { get set }

- `
  ``
  ``
  `

  ### [settings](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(py)settings)

  `
  `  
  Contains settings related to the auth object.  

  #### Declaration

  Swift  

      @NSCopying
      @objc
      open var settings: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthSettings.html?

- `
  ``
  ``
  `

  ### [userAccessGroup](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(py)userAccessGroup)

  `
  `  
  The current user access group that the Auth instance is using.

  Default is `nil`.  

  #### Declaration

  Swift  

      @objc
      public internal(set) var userAccessGroup: String? { get }

- `
  ``
  ``
  `

  ### [shareAuthStateAcrossDevices](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(py)shareAuthStateAcrossDevices)

  `
  `  
  Contains shareAuthStateAcrossDevices setting related to the auth object.

  If userAccessGroup is not set, setting shareAuthStateAcrossDevices will
  have no effect. You should set shareAuthStateAcrossDevices to its desired
  state and then set the userAccessGroup after.  

  #### Declaration

  Swift  

      @objc
      open var shareAuthStateAcrossDevices: Bool

- `
  ``
  ``
  `

  ### [tenantID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(py)tenantID)

  `
  `  
  The tenant ID of the auth instance. `nil` if none is available.  

  #### Declaration

  Swift  

      @objc
      open var tenantID: String?

- `
  ``
  ``
  `

  ### [customAuthDomain](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(py)customAuthDomain)

  `
  `  
  The custom authentication domain used to handle all sign-in redirects.
  End-users will see
  this domain when signing in. This domain must be allowlisted in the Firebase Console.  

  #### Declaration

  Swift  

      @objc
      open var customAuthDomain: String?

- `
  ``
  ``
  `

  ### [updateCurrentUser(_:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)updateCurrentUser:completion:)

  `
  `  
  Sets the [currentUser](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth.html#/c:@M@FirebaseAuth@objc(cs)FIRAuth(py)currentUser) on the receiver to the provided user object.  

  #### Declaration

  Swift  

      @objc
      open func updateCurrentUser(_ user: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html?, completion: ((Error?) -> Void)? = nil)

  #### Parameters

  |--------------------|-----------------------------------------------------------------------------------------------------------------------|
  | ` `*user*` `       | The user object to be set as the current user of the calling Auth instance.                                           |
  | ` `*completion*` ` | Optionally; a block invoked after the user of the calling Auth instance has been updated or an error was encountered. |

- `
  ``
  ``
  `

  ### [updateCurrentUser(_:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/s:12FirebaseAuth0B0C17updateCurrentUseryyAA0E0CYaKF)

  `
  `  
  Sets the [currentUser](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth.html#/c:@M@FirebaseAuth@objc(cs)FIRAuth(py)currentUser) on the receiver to the provided user object.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func updateCurrentUser(_ user: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html) async throws

  #### Parameters

  |--------------|-----------------------------------------------------------------------------|
  | ` `*user*` ` | The user object to be set as the current user of the calling Auth instance. |

- `
  ``
  ``
  `

  ### [fetchSignInMethods(forEmail:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)fetchSignInMethodsForEmail:completion:)

  `
  `  
  \[Deprecated\] Fetches the list of all sign-in methods previously used for the provided
  email address. This method returns an empty list when [Email Enumeration
  Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)
  is enabled, irrespective of the number of authentication methods available for the given
  email.

  Possible error codes: `AuthErrorCodeInvalidEmail` - Indicates the email address is malformed.  

  #### Declaration

  Swift  

      @available(*, deprecated, message: "`fetchSignInMethods` is deprecated and will be removed in a future release. This method returns an empty list when Email Enumeration Protection is enabled.")
      @objc
      open func fetchSignInMethods(forEmail email: String,
                                   completion: (([String]?, Error?) -> Void)? = nil)

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*email*` `      | The email address for which to obtain a list of sign-in methods.                                                                                                                                     |
  | ` `*completion*` ` | Optionally; a block which is invoked when the list of sign in methods for the specified email address is ready or an error was encountered. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [fetchSignInMethods(forEmail:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/s:12FirebaseAuth0B0C18fetchSignInMethods8forEmailSaySSGSS_tYaKF)

  `
  `  
  \[Deprecated\] Fetches the list of all sign-in methods previously used for the provided
  email address. This method returns an empty list when [Email Enumeration
  Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)
  is enabled, irrespective of the number of authentication methods available for the given
  email.

  Possible error codes: `AuthErrorCodeInvalidEmail` - Indicates the email address is malformed.  

  #### Declaration

  Swift  

      @available(*, deprecated, message: "`fetchSignInMethods` is deprecated and will be removed in a future release. This method returns an empty list when Email Enumeration Protection is enabled.")
      open func fetchSignInMethods(forEmail email: String) async throws -> [String]

  #### Parameters

  |---------------|------------------------------------------------------------------|
  | ` `*email*` ` | The email address for which to obtain a list of sign-in methods. |

  #### Return Value

  List of sign-in methods
- `
  ``
  ``
  `

  ### [signIn(withEmail:password:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)signInWithEmail:password:completion:)

  `
  `  
  Signs in using an email address and password.

  When [Email Enumeration
  Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)
  is enabled, this method fails with an error in case of an invalid
  email/password.

  Possible error codes:
  - `AuthErrorCodeOperationNotAllowed` - Indicates that email and password accounts are not enabled. Enable them in the Auth section of the Firebase console.
    - `AuthErrorCodeUserDisabled` - Indicates the user's account is disabled.
    - `AuthErrorCodeWrongPassword` - Indicates the user attempted sign in with an incorrect password.
  - `AuthErrorCodeInvalidEmail` - Indicates the email address is malformed.  

  #### Declaration

  Swift  

      @objc
      open func signIn(withEmail email: String,
                       password: String,
                       completion: ((https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html?, Error?) -> Void)? = nil)

  #### Parameters

  |--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*email*` `      | The user's email address.                                                                                                                     |
  | ` `*password*` `   | The user's password.                                                                                                                          |
  | ` `*completion*` ` | Optionally; a block which is invoked when the sign in flow finishes, or is canceled. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [signIn(withEmail:password:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/s:12FirebaseAuth0B0C6signIn9withEmail8passwordAA0B10DataResultCSS_SStYaKF)

  `
  `  
  Signs in using an email address and password.

  Possible error codes:
  - `AuthErrorCodeOperationNotAllowed` - Indicates that email and password accounts are not enabled. Enable them in the Auth section of the Firebase console.
    - `AuthErrorCodeUserDisabled` - Indicates the user's account is disabled.
    - `AuthErrorCodeWrongPassword` - Indicates the user attempted sign in with an incorrect password.
  - `AuthErrorCodeInvalidEmail` - Indicates the email address is malformed.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @discardableResult
      open func signIn(withEmail email: String, password: String) async throws -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html

  #### Parameters

  |------------------|---------------------------|
  | ` `*email*` `    | The user's email address. |
  | ` `*password*` ` | The user's password.      |

  #### Return Value

  The [AuthDataResult](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html) after a successful signin.
- `
  ``
  ``
  `

  ### [signIn(withEmail:link:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)signInWithEmail:link:completion:)

  `
  `  
  Signs in using an email address and email sign-in link.

  Possible error codes:
  - `AuthErrorCodeOperationNotAllowed` - Indicates that email and password accounts are not enabled. Enable them in the Auth section of the Firebase console.
    - `AuthErrorCodeUserDisabled` - Indicates the user's account is disabled.
    - `AuthErrorCodeWrongPassword` - Indicates the user attempted sign in with an incorrect password.
  - `AuthErrorCodeInvalidEmail` - Indicates the email address is malformed.  

  #### Declaration

  Swift  

      @objc
      open func signIn(withEmail email: String,
                       link: String,
                       completion: ((https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html?, Error?) -> Void)? = nil)

  #### Parameters

  |--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*email*` `      | The user's email address.                                                                                                                     |
  | ` `*link*` `       | The email sign-in link.                                                                                                                       |
  | ` `*completion*` ` | Optionally; a block which is invoked when the sign in flow finishes, or is canceled. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [signIn(withEmail:link:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/s:12FirebaseAuth0B0C6signIn9withEmail4linkAA0B10DataResultCSS_SStYaKF)

  `
  `  
  Signs in using an email address and email sign-in link.
  Possible error codes:
  - `AuthErrorCodeOperationNotAllowed` - Indicates that email and password accounts are not enabled. Enable them in the Auth section of the Firebase console.
    - `AuthErrorCodeUserDisabled` - Indicates the user's account is disabled.
    - `AuthErrorCodeWrongPassword` - Indicates the user attempted sign in with an incorrect password.
  - `AuthErrorCodeInvalidEmail` - Indicates the email address is malformed.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func signIn(withEmail email: String, link: String) async throws -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html

  #### Parameters

  |---------------|---------------------------|
  | ` `*email*` ` | The user's email address. |
  | ` `*link*` `  | The email sign-in link.   |

  #### Return Value

  The [AuthDataResult](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html) after a successful signin.
- `
  ``
  ``
  `

  ### [signIn(with:uiDelegate:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)signInWithProvider:UIDelegate:completion:)

  `
  `  
  Signs in using the provided auth provider instance.

  Possible error codes:
  - `AuthErrorCodeOperationNotAllowed` - Indicates that email and password accounts are not enabled. Enable them in the Auth section of the Firebase console.
    - `AuthErrorCodeUserDisabled` - Indicates the user's account is disabled.
    - `AuthErrorCodeWrongPassword` - Indicates the user attempted sign in with an incorrect password.
    - `AuthErrorCodeWebNetworkRequestFailed` - Indicates that a network request within a SFSafariViewController or WKWebView failed.
    - `AuthErrorCodeWebInternalError` - Indicates that an internal error occurred within a SFSafariViewController or WKWebView.
    - `AuthErrorCodeWebSignInUserInteractionFailure` - Indicates a general failure during a web sign-in flow.
    - `AuthErrorCodeWebContextAlreadyPresented` - Indicates that an attempt was made to present a new web context while one was already being presented.
    - `AuthErrorCodeWebContextCancelled` - Indicates that the URL presentation was cancelled prematurely by the user.
  - `AuthErrorCodeAccountExistsWithDifferentCredential` - Indicates the email asserted by the credential (e.g. the email in a Facebook access token) is already in use by an existing account, that cannot be authenticated with this sign-in method. Call fetchProvidersForEmail for this user's email and then prompt them to sign in with any of the sign-in providers returned. This error will only be thrown if the "One account per email address" setting is enabled in the Firebase console, under Auth settings.  

  #### Declaration

  Swift  

      @available(tvOS, unavailable)
      @available(macOS, unavailable)
      @available(watchOS, unavailable)
      @objc(signInWithProvider:UIDelegate:completion:)
      open func signIn(with provider: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/FederatedAuthProvider.html,
                       uiDelegate: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html?,
                       completion: ((https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html?, Error?) -> Void)?)

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*provider*` `   | An instance of an auth provider used to initiate the sign-in flow.                                                                                                       |
  | ` `*uiDelegate*` ` | Optionally an instance of a class conforming to the AuthUIDelegate protocol, this is used for presenting the web context. If nil, a default AuthUIDelegate will be used. |
  | ` `*completion*` ` | Optionally; a block which is invoked when the sign in flow finishes, or is canceled. Invoked asynchronously on the main thread in the future.                            |

- `
  ``
  ``
  `

  ### [signIn(with:uiDelegate:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/s:12FirebaseAuth0B0C6signIn4with10uiDelegateAA0B10DataResultCAA09FederatedB8Provider_p_AA0B10UIDelegate_pSgtYaKF)

  `
  `  
  Signs in using the provided auth provider instance.

  Possible error codes:
  - `AuthErrorCodeOperationNotAllowed` - Indicates that email and password accounts are not enabled. Enable them in the Auth section of the Firebase console.
    - `AuthErrorCodeUserDisabled` - Indicates the user's account is disabled.
    - `AuthErrorCodeWrongPassword` - Indicates the user attempted sign in with an incorrect password.
    - `AuthErrorCodeWebNetworkRequestFailed` - Indicates that a network request within a SFSafariViewController or WKWebView failed.
    - `AuthErrorCodeWebInternalError` - Indicates that an internal error occurred within a SFSafariViewController or WKWebView.
    - `AuthErrorCodeWebSignInUserInteractionFailure` - Indicates a general failure during a web sign-in flow.
    - `AuthErrorCodeWebContextAlreadyPresented` - Indicates that an attempt was made to present a new web context while one was already being presented.
    - `AuthErrorCodeWebContextCancelled` - Indicates that the URL presentation was cancelled prematurely by the user.
  - `AuthErrorCodeAccountExistsWithDifferentCredential` - Indicates the email asserted by the credential (e.g. the email in a Facebook access token) is already in use by an existing account, that cannot be authenticated with this sign-in method. Call fetchProvidersForEmail for this user's email and then prompt them to sign in with any of the sign-in providers returned. This error will only be thrown if the "One account per email address" setting is enabled in the Firebase console, under Auth settings.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @available(tvOS, unavailable)
      @available(macOS, unavailable)
      @available(watchOS, unavailable)
      @discardableResult
      open func signIn(with provider: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/FederatedAuthProvider.html,
                       uiDelegate: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.html?) async throws -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*provider*` `   | An instance of an auth provider used to initiate the sign-in flow.                                                                                                       |
  | ` `*uiDelegate*` ` | Optionally an instance of a class conforming to the AuthUIDelegate protocol, this is used for presenting the web context. If nil, a default AuthUIDelegate will be used. |

  #### Return Value

  The [AuthDataResult](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html) after the successful signin.
- `
  ``
  ``
  `

  ### [signIn(with:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)signInWithCredential:completion:)

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

  #### Declaration

  Swift  

      @objc(signInWithCredential:completion:)
      open func signIn(with credential: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html,
                       completion: ((https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html?, Error?) -> Void)? = nil)

  #### Parameters

  |--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*credential*` ` | The credential supplied by the IdP.                                                                                                           |
  | ` `*completion*` ` | Optionally; a block which is invoked when the sign in flow finishes, or is canceled. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [signIn(with:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/s:12FirebaseAuth0B0C6signIn4withAA0B10DataResultCAA0B10CredentialC_tYaKF)

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

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @discardableResult
      open func signIn(with credential: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential.html) async throws -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html

  #### Parameters

  |--------------------|-------------------------------------|
  | ` `*credential*` ` | The credential supplied by the IdP. |

  #### Return Value

  The [AuthDataResult](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html) after the successful signin.
- `
  ``
  ``
  `

  ### [signInAnonymously(completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)signInAnonymouslyWithCompletion:)

  `
  `  
  Asynchronously creates and becomes an anonymous user.

  If there is already an anonymous user signed in, that user will be returned instead.
  If there is any other existing user signed in, that user will be signed out.

  Possible error codes:
  - `AuthErrorCodeOperationNotAllowed` - Indicates that anonymous accounts are not enabled. Enable them in the Auth section of the Firebase console.  

  #### Declaration

  Swift  

      @objc
      open func signInAnonymously(completion: ((https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html?, Error?) -> Void)? = nil)

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | Optionally; a block which is invoked when the sign in finishes, or is canceled. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [signInAnonymously()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)signInAnonymouslyWithCompletionHandler:)

  `
  `  
  Asynchronously creates and becomes an anonymous user.

  If there is already an anonymous user signed in, that user will be returned instead.
  If there is any other existing user signed in, that user will be signed out.

  Possible error codes:
  - `AuthErrorCodeOperationNotAllowed` - Indicates that anonymous accounts are not enabled. Enable them in the Auth section of the Firebase console.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @discardableResult
      @objc
      open func signInAnonymously() async throws -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html

  #### Return Value

  The [AuthDataResult](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html) after the successful signin.
- `
  ``
  ``
  `

  ### [signIn(withCustomToken:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)signInWithCustomToken:completion:)

  `
  `  
  Asynchronously signs in to Firebase with the given Auth token.

  Possible error codes:
  - `AuthErrorCodeInvalidCustomToken` - Indicates a validation error with the custom token.
  - `AuthErrorCodeCustomTokenMismatch` - Indicates the service account and the API key belong to different projects.  

  #### Declaration

  Swift  

      @objc
      open func signIn(withCustomToken token: String,
                       completion: ((https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html?, Error?) -> Void)? = nil)

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*token*` `      | A self-signed custom auth token.                                                                                                         |
  | ` `*completion*` ` | Optionally; a block which is invoked when the sign in finishes, or is canceled. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [signIn(withCustomToken:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/s:12FirebaseAuth0B0C6signIn15withCustomTokenAA0B10DataResultCSS_tYaKF)

  `
  `  
  Asynchronously signs in to Firebase with the given Auth token.

  Possible error codes:
  - `AuthErrorCodeInvalidCustomToken` - Indicates a validation error with the custom token.
  - `AuthErrorCodeCustomTokenMismatch` - Indicates the service account and the API key belong to different projects.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @discardableResult
      open func signIn(withCustomToken token: String) async throws -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html

  #### Parameters

  |---------------|----------------------------------|
  | ` `*token*` ` | A self-signed custom auth token. |

  #### Return Value

  The [AuthDataResult](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html) after the successful signin.
- `
  ``
  ``
  `

  ### [createUser(withEmail:password:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)createUserWithEmail:password:completion:)

  `
  `  
  Creates and, on success, signs in a user with the given email address and password.

  Possible error codes:
  - `AuthErrorCodeInvalidEmail` - Indicates the email address is malformed.
  - `AuthErrorCodeEmailAlreadyInUse` - Indicates the email used to attempt sign up already exists. Call fetchProvidersForEmail to check which sign-in mechanisms the user used, and prompt the user to sign in with one of those.
  - `AuthErrorCodeOperationNotAllowed` - Indicates that email and password accounts are not enabled. Enable them in the Auth section of the Firebase console.
  - `AuthErrorCodeWeakPassword` - Indicates an attempt to set a password that is considered too weak. The NSLocalizedFailureReasonErrorKey field in the NSError.userInfo dictionary object will contain more detailed explanation that can be shown to the user.  

  #### Declaration

  Swift  

      @objc
      open func createUser(withEmail email: String,
                           password: String,
                           completion: ((https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html?, Error?) -> Void)? = nil)

  #### Parameters

  |--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*email*` `      | The user's email address.                                                                                                                     |
  | ` `*password*` `   | The user's desired password.                                                                                                                  |
  | ` `*completion*` ` | Optionally; a block which is invoked when the sign up flow finishes, or is canceled. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [createUser(withEmail:password:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/s:12FirebaseAuth0B0C10createUser9withEmail8passwordAA0B10DataResultCSS_SStYaKF)

  `
  `  
  Creates and, on success, signs in a user with the given email address and password.

  Possible error codes:
  - `AuthErrorCodeInvalidEmail` - Indicates the email address is malformed.
  - `AuthErrorCodeEmailAlreadyInUse` - Indicates the email used to attempt sign up already exists. Call fetchProvidersForEmail to check which sign-in mechanisms the user used, and prompt the user to sign in with one of those.
  - `AuthErrorCodeOperationNotAllowed` - Indicates that email and password accounts are not enabled. Enable them in the Auth section of the Firebase console.
  - `AuthErrorCodeWeakPassword` - Indicates an attempt to set a password that is considered too weak. The NSLocalizedFailureReasonErrorKey field in the NSError.userInfo dictionary object will contain more detailed explanation that can be shown to the user.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @discardableResult
      open func createUser(withEmail email: String, password: String) async throws -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html

  #### Parameters

  |------------------|------------------------------|
  | ` `*email*` `    | The user's email address.    |
  | ` `*password*` ` | The user's desired password. |

  #### Return Value

  The [AuthDataResult](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult.html) after the successful signin.
- `
  ``
  ``
  `

  ### [confirmPasswordReset(withCode:newPassword:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)confirmPasswordResetWithCode:newPassword:completion:)

  `
  `  
  Resets the password given a code sent to the user outside of the app and a new password
  for the user.

  Possible error codes:
  - `AuthErrorCodeWeakPassword` - Indicates an attempt to set a password that is considered too weak.
  - `AuthErrorCodeOperationNotAllowed` - Indicates the administrator disabled sign in with the specified identity provider.
  - `AuthErrorCodeExpiredActionCode` - Indicates the OOB code is expired.
  - `AuthErrorCodeInvalidActionCode` - Indicates the OOB code is invalid.  

  #### Declaration

  Swift  

      @objc
      open func confirmPasswordReset(withCode code: String, newPassword: String,
                                     completion: @escaping (Error?) -> Void)

  #### Parameters

  |---------------------|--------------------------------------------------------------------------------------------------------------------------|
  | ` `*code*` `        | The reset code.                                                                                                          |
  | ` `*newPassword*` ` | The new password.                                                                                                        |
  | ` `*completion*` `  | Optionally; a block which is invoked when the request finishes. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [confirmPasswordReset(withCode:newPassword:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/s:12FirebaseAuth0B0C20confirmPasswordReset8withCode03newD0ySS_SStYaKF)

  `
  `  
  Resets the password given a code sent to the user outside of the app and a new password
  for the user.

  Possible error codes:
  - `AuthErrorCodeWeakPassword` - Indicates an attempt to set a password that is considered too weak.
  - `AuthErrorCodeOperationNotAllowed` - Indicates the administrator disabled sign in with the specified identity provider.
  - `AuthErrorCodeExpiredActionCode` - Indicates the OOB code is expired.
  - `AuthErrorCodeInvalidActionCode` - Indicates the OOB code is invalid.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func confirmPasswordReset(withCode code: String, newPassword: String) async throws

  #### Parameters

  |---------------------|-------------------|
  | ` `*code*` `        | The reset code.   |
  | ` `*newPassword*` ` | The new password. |

- `
  ``
  ``
  `

  ### [checkActionCode(_:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)checkActionCode:completion:)

  `
  `  
  Checks the validity of an out of band code.  

  #### Declaration

  Swift  

      @objc
      open func checkActionCode(_ code: String,
                                completion: @escaping (https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeInfo.html?, Error?) -> Void)

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------|
  | ` `*code*` `       | The out of band code to check validity.                                                                                  |
  | ` `*completion*` ` | Optionally; a block which is invoked when the request finishes. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [checkActionCode(_:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/s:12FirebaseAuth0B0C15checkActionCodeyAA0dE4InfoCSSYaKF)

  `
  `  
  Checks the validity of an out of band code.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func checkActionCode(_ code: String) async throws -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeInfo.html

  #### Parameters

  |--------------|-----------------------------------------|
  | ` `*code*` ` | The out of band code to check validity. |

  #### Return Value

  An [ActionCodeInfo](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeInfo.html).
- `
  ``
  ``
  `

  ### [verifyPasswordResetCode(_:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)verifyPasswordResetCode:completion:)

  `
  `  
  Checks the validity of a verify password reset code.  

  #### Declaration

  Swift  

      @objc
      open func verifyPasswordResetCode(_ code: String,
                                        completion: @escaping (String?, Error?) -> Void)

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------|
  | ` `*code*` `       | The password reset code to be verified.                                                                                  |
  | ` `*completion*` ` | Optionally; a block which is invoked when the request finishes. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [verifyPasswordResetCode(_:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/s:12FirebaseAuth0B0C23verifyPasswordResetCodeyS2SYaKF)

  `
  `  
  Checks the validity of a verify password reset code.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func verifyPasswordResetCode(_ code: String) async throws -> String

  #### Parameters

  |--------------|-----------------------------------------|
  | ` `*code*` ` | The password reset code to be verified. |

  #### Return Value

  An email.
- `
  ``
  ``
  `

  ### [applyActionCode(_:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)applyActionCode:completion:)

  `
  `  
  Applies out of band code.

  This method will not work for out of band codes which require an additional parameter,
  such as password reset code.  

  #### Declaration

  Swift  

      @objc
      open func applyActionCode(_ code: String, completion: @escaping (Error?) -> Void)

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------|
  | ` `*code*` `       | The out of band code to be applied.                                                                                      |
  | ` `*completion*` ` | Optionally; a block which is invoked when the request finishes. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [applyActionCode(_:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/s:12FirebaseAuth0B0C15applyActionCodeyySSYaKF)

  `
  `  
  Applies out of band code.

  This method will not work for out of band codes which require an additional parameter,
  such as password reset code.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func applyActionCode(_ code: String) async throws

  #### Parameters

  |--------------|-------------------------------------|
  | ` `*code*` ` | The out of band code to be applied. |

- `
  ``
  ``
  `

  ### [sendPasswordReset(withEmail:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)sendPasswordResetWithEmail:completion:)

  `
  `  
  Initiates a password reset for the given email address.

  This method does not throw an
  error when there's no user account with the given email address and [Email Enumeration
  Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)
  is enabled.

  Possible error codes:
  - `AuthErrorCodeInvalidRecipientEmail` - Indicates an invalid recipient email was sent in the request.
  - `AuthErrorCodeInvalidSender` - Indicates an invalid sender email is set in the console for this action.
  - `AuthErrorCodeInvalidMessagePayload` - Indicates an invalid email template for sending update email.  

  #### Declaration

  Swift  

      @objc
      open func sendPasswordReset(withEmail email: String,
                                  completion: ((Error?) -> Void)? = nil)

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------|
  | ` `*email*` `      | The email address of the user.                                                                                           |
  | ` `*completion*` ` | Optionally; a block which is invoked when the request finishes. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [sendPasswordReset(withEmail:actionCodeSettings:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)sendPasswordResetWithEmail:actionCodeSettings:completion:)

  `
  `  
  Initiates a password reset for the given email address and [ActionCodeSettings](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.html) object.

  This method does not throw an
  error when there's no user account with the given email address and [Email Enumeration
  Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)
  is enabled.

  Possible error codes:
  - `AuthErrorCodeInvalidRecipientEmail` - Indicates an invalid recipient email was sent in the request.
  - `AuthErrorCodeInvalidSender` - Indicates an invalid sender email is set in the console for this action.
  - `AuthErrorCodeInvalidMessagePayload` - Indicates an invalid email template for sending update email.
  - `AuthErrorCodeMissingIosBundleID` - Indicates that the iOS bundle ID is missing when `handleCodeInApp` is set to true.
  - `AuthErrorCodeMissingAndroidPackageName` - Indicates that the android package name is missing when the `androidInstallApp` flag is set to true.
  - `AuthErrorCodeUnauthorizedDomain` - Indicates that the domain specified in the continue URL is not allowlisted in the Firebase console.
  - `AuthErrorCodeInvalidContinueURI` - Indicates that the domain specified in the continue URL is not valid.  

  #### Declaration

  Swift  

      @objc
      open func sendPasswordReset(withEmail email: String,
                                  actionCodeSettings: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.html?,
                                  completion: ((Error?) -> Void)? = nil)

  #### Parameters

  |----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*email*` `              | The email address of the user.                                                                                                                                                                    |
  | ` `*actionCodeSettings*` ` | An [ActionCodeSettings](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.html) object containing settings related to handling action codes. |
  | ` `*completion*` `         | Optionally; a block which is invoked when the request finishes. Invoked asynchronously on the main thread in the future.                                                                          |

- `
  ``
  ``
  `

  ### [sendPasswordReset(withEmail:actionCodeSettings:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/s:12FirebaseAuth0B0C17sendPasswordReset9withEmail18actionCodeSettingsySS_AA06ActioniJ0CSgtYaKF)

  `
  `  
  Initiates a password reset for the given email address and [ActionCodeSettings](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.html) object.

  This method does not throw an
  error when there's no user account with the given email address and [Email Enumeration
  Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)
  is enabled.

  Possible error codes:
  - `AuthErrorCodeInvalidRecipientEmail` - Indicates an invalid recipient email was sent in the request.
  - `AuthErrorCodeInvalidSender` - Indicates an invalid sender email is set in the console for this action.
  - `AuthErrorCodeInvalidMessagePayload` - Indicates an invalid email template for sending update email.
  - `AuthErrorCodeMissingIosBundleID` - Indicates that the iOS bundle ID is missing when `handleCodeInApp` is set to true.
  - `AuthErrorCodeMissingAndroidPackageName` - Indicates that the android package name is missing when the `androidInstallApp` flag is set to true.
  - `AuthErrorCodeUnauthorizedDomain` - Indicates that the domain specified in the continue URL is not allowlisted in the Firebase console.
  - `AuthErrorCodeInvalidContinueURI` - Indicates that the domain specified in the continue URL is not valid.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func sendPasswordReset(withEmail email: String,
                                  actionCodeSettings: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.html? = nil) async throws

  #### Parameters

  |----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*email*` `              | The email address of the user.                                                                                                                                                                    |
  | ` `*actionCodeSettings*` ` | An [ActionCodeSettings](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.html) object containing settings related to handling action codes. |

- `
  ``
  ``
  `

  ### [sendSignInLink(toEmail:actionCodeSettings:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)sendSignInLinkToEmail:actionCodeSettings:completion:)

  `
  `  
  Sends a sign in with email link to provided email address.  

  #### Declaration

  Swift  

      @objc
      open func sendSignInLink(toEmail email: String,
                               actionCodeSettings: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.html,
                               completion: ((Error?) -> Void)? = nil)

  #### Parameters

  |----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*email*` `              | The email address of the user.                                                                                                                                                                    |
  | ` `*actionCodeSettings*` ` | An [ActionCodeSettings](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.html) object containing settings related to handling action codes. |
  | ` `*completion*` `         | Optionally; a block which is invoked when the request finishes. Invoked asynchronously on the main thread in the future.                                                                          |

- `
  ``
  ``
  `

  ### [sendSignInLink(toEmail:actionCodeSettings:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/s:12FirebaseAuth0B0C14sendSignInLink7toEmail18actionCodeSettingsySS_AA06ActionjK0CtYaKF)

  `
  `  
  Sends a sign in with email link to provided email address.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func sendSignInLink(toEmail email: String,
                               actionCodeSettings: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.html) async throws

  #### Parameters

  |----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*email*` `              | The email address of the user.                                                                                                                                                                    |
  | ` `*actionCodeSettings*` ` | An [ActionCodeSettings](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.html) object containing settings related to handling action codes. |

- `
  ``
  ``
  `

  ### [signOut()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)signOut:)

  `
  `  
  Signs out the current user.

  Possible error codes:
  - `AuthErrorCodeKeychainError` - Indicates an error occurred when accessing the keychain. The `NSLocalizedFailureReasonErrorKey` field in the `userInfo` dictionary will contain more information about the error encountered.  

  #### Declaration

  Swift  

      @objc(signOut:)
      open func signOut() throws

- `
  ``
  ``
  `

  ### [isSignIn(withEmailLink:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)isSignInWithEmailLink:)

  `
  `  
  Checks if link is an email sign-in link.  

  #### Declaration

  Swift  

      @objc
      open func isSignIn(withEmailLink link: String) -> Bool

  #### Parameters

  |--------------|-------------------------|
  | ` `*link*` ` | The email sign-in link. |

  #### Return Value

  `true` when the link passed matches the expected format of an email sign-in link.
- `
  ``
  ``
  `

  ### [initializeRecaptchaConfig(completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/)

  `
  `  
  Initializes reCAPTCHA using the settings configured for the project or tenant.

  If you change the tenant ID of the `Auth` instance, the configuration will be
  reloaded.
- `
  ``
  ``
  `

  ### [initializeRecaptchaConfig()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/)

  `
  `  
  Initializes reCAPTCHA using the settings configured for the project or tenant.

  If you change the tenant ID of the `Auth` instance, the configuration will be
  reloaded.
- `
  ``
  ``
  `

  ### [addStateDidChangeListener(_:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)addAuthStateDidChangeListener:)

  `
  `  
  Registers a block as an "auth state did change" listener.

  To be invoked when:
  - The block is registered as a listener,
  - A user with a different UID from the current user has signed in, or
  - The current user has signed out.

  The block is invoked immediately after adding it according to its standard invocation
  semantics, asynchronously on the main thread. Users should pay special attention to
  making sure the block does not inadvertently retain objects which should not be retained by
  the long-lived block. The block itself will be retained by `Auth` until it is
  unregistered or until the `Auth` instance is otherwise deallocated.  

  #### Declaration

  Swift  

      @objc(addAuthStateDidChangeListener:)
      open func addStateDidChangeListener(_ listener: @escaping (Auth, https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html?) -> Void)
        -> NSObjectProtocol

  #### Parameters

  |------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*listener*` ` | The block to be invoked. The block is always invoked asynchronously on the main thread, even for it's initial invocation after having been added as a listener. |

  #### Return Value

  A handle useful for manually unregistering the block as a listener.
- `
  ``
  ``
  `

  ### [removeStateDidChangeListener(_:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)removeAuthStateDidChangeListener:)

  `
  `  
  Unregisters a block as an "auth state did change" listener.  

  #### Declaration

  Swift  

      @objc(removeAuthStateDidChangeListener:)
      open func removeStateDidChangeListener(_ listenerHandle: NSObjectProtocol)

  #### Parameters

  |------------------------|------------------------------|
  | ` `*listenerHandle*` ` | The handle for the listener. |

- `
  ``
  ``
  `

  ### [addIDTokenDidChangeListener(_:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)addIDTokenDidChangeListener:)

  `
  `  
  Registers a block as an "ID token did change" listener.

  To be invoked when:
  - The block is registered as a listener,
  - A user with a different UID from the current user has signed in,
  - The ID token of the current user has been refreshed, or
  - The current user has signed out.

  The block is invoked immediately after adding it according to its standard invocation
  semantics, asynchronously on the main thread. Users should pay special attention to
  making sure the block does not inadvertently retain objects which should not be retained by
  the long-lived block. The block itself will be retained by `Auth` until it is
  unregistered or until the `Auth` instance is otherwise deallocated.  

  #### Declaration

  Swift  

      @objc
      open func addIDTokenDidChangeListener(_ listener: @escaping (Auth, https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html?) -> Void)
        -> NSObjectProtocol

  #### Parameters

  |------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*listener*` ` | The block to be invoked. The block is always invoked asynchronously on the main thread, even for it's initial invocation after having been added as a listener. |

  #### Return Value

  A handle useful for manually unregistering the block as a listener.
- `
  ``
  ``
  `

  ### [removeIDTokenDidChangeListener(_:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)removeIDTokenDidChangeListener:)

  `
  `  
  Unregisters a block as an "ID token did change" listener.  

  #### Declaration

  Swift  

      @objc
      open func removeIDTokenDidChangeListener(_ listenerHandle: NSObjectProtocol)

  #### Parameters

  |------------------------|------------------------------|
  | ` `*listenerHandle*` ` | The handle for the listener. |

- `
  ``
  ``
  `

  ### [useAppLanguage()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)useAppLanguage)

  `
  `  
  Sets [languageCode](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth.html#/c:@M@FirebaseAuth@objc(cs)FIRAuth(py)languageCode) to the app's current language.  

  #### Declaration

  Swift  

      @objc
      open func useAppLanguage()

- `
  ``
  ``
  `

  ### [useEmulator(withHost:port:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)useEmulatorWithHost:port:)

  `
  `  
  Configures Firebase Auth to connect to an emulated host instead of the remote backend.  

  #### Declaration

  Swift  

      @objc
      open func useEmulator(withHost host: String, port: Int)

- `
  ``
  ``
  `

  ### [revokeToken(withAuthorizationCode:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)revokeTokenWithAuthorizationCode:completion:)

  `
  `  
  Revoke the users token with authorization code.  

  #### Declaration

  Swift  

      @objc
      open func revokeToken(withAuthorizationCode authorizationCode: String,
                            completion: ((Error?) -> Void)? = nil)

  #### Parameters

  |---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*authorizationCode*` ` | The authorization code used to perform the revocation.                                                                                            |
  | ` `*completion*` `        | (Optional) the block invoked when the request to revoke the token is complete, or fails. Invoked asynchronously on the main thread in the future. |

- `
  ``
  ``
  `

  ### [revokeToken(withAuthorizationCode:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/s:12FirebaseAuth0B0C11revokeToken21withAuthorizationCodeySS_tYaKF)

  `
  `  
  Revoke the users token with authorization code.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func revokeToken(withAuthorizationCode authorizationCode: String) async throws

  #### Parameters

  |---------------------------|--------------------------------------------------------|
  | ` `*authorizationCode*` ` | The authorization code used to perform the revocation. |

- `
  ``
  ``
  `

  ### [useUserAccessGroup(_:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)useUserAccessGroup:error:)

  `
  `  
  Switch userAccessGroup and current user to the given accessGroup and the user stored in it.  

  #### Declaration

  Swift  

      @objc
      open func useUserAccessGroup(_ accessGroup: String?) throws

- `
  ``
  ``
  `

  ### [getStoredUser(forAccessGroup:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/s:12FirebaseAuth0B0C13getStoredUser14forAccessGroupAA0E0CSgSSSg_tKF)

  `
  `  
  Get the stored user in the given accessGroup.

  This API is not supported on tvOS when [shareAuthStateAcrossDevices](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth.html#/c:@M@FirebaseAuth@objc(cs)FIRAuth(py)shareAuthStateAcrossDevices) is set to `true`.
  and will return `nil`.

  Please refer to <https://github.com/firebase/firebase-ios-sdk/issues/8878> for details.  

  #### Declaration

  Swift  

      open func getStoredUser(forAccessGroup accessGroup: String?) throws -> https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User.html?

- `
  ``
  ``
  `

  ### [apnsToken](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(py)APNSToken)

  `
  `  
  The APNs token used for phone number authentication.

  The type of the token (production or sandbox) will be automatically
  detected based on your provisioning profile.

  This property is available on iOS only.

  If swizzling is disabled, the APNs Token must be set for phone number auth to work,
  by either setting this property or by calling [setAPNSToken(_:type:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth.html#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)setAPNSToken:type:).  

  #### Declaration

  Swift  

      @objc(APNSToken)
      open var apnsToken: Data? { get }

- `
  ``
  ``
  `

  ### [setAPNSToken(_:type:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)setAPNSToken:type:)

  `
  `  
  Sets the APNs token along with its type.

  This method is available on iOS only.

  If swizzling is disabled, the APNs Token must be set for phone number auth to work,
  by either setting calling this method or by setting the `APNSToken` property.  

  #### Declaration

  Swift  

      @objc
      open func setAPNSToken(_ token: Data, type: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthAPNSTokenType.html)

- `
  ``
  ``
  `

  ### [canHandleNotification(_:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)canHandleNotification:)

  `
  `  
  Whether the specific remote notification is handled by `Auth` .

  This method is available on iOS only.

  If swizzling is disabled, related remote notifications must be forwarded to this method
  for phone number auth to work.  

  #### Declaration

  Swift  

      @objc
      open func canHandleNotification(_ userInfo: [AnyHashable : Any]) -> Bool

  #### Parameters

  |------------------|---------------------------------------------------------------------------------|
  | ` `*userInfo*` ` | A dictionary that contains information related to the notification in question. |

  #### Return Value

  Whether or the notification is handled. A return value of `true` means the
  notification is for Firebase Auth so the caller should ignore the notification from further
  processing, and `false` means the notification is for the app (or another library) so
  the caller should continue handling this notification as usual.
- `
  ``
  ``
  `

  ### [canHandle(_:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@M@FirebaseAuth@objc(cs)FIRAuth(im)canHandleURL:)

  `
  `  
  Whether the specific URL is handled by `Auth` .

  This method is available on iOS only.

  If swizzling is disabled, URLs received by the application delegate must be forwarded
  to this method for phone number auth to work.  

  #### Declaration

  Swift  

      @objc(canHandleURL:)
      open func canHandle(_ url: URL) -> Bool

  #### Parameters

  |-------------|------------------------------------------------------------------------------|
  | ` `*url*` ` | The URL received by the application delegate from any of the openURL method. |

  #### Return Value

  Whether or the URL is handled. `true` means the URL is for Firebase Auth
  so the caller should ignore the URL from further processing, and `false` means the
  the URL is for the app (or another library) so the caller should continue handling
  this URL as usual.
- `
  ``
  ``
  `

  ### [authStateDidChangeNotification](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/s:12FirebaseAuth0B0C30authStateDidChangeNotificationSo18NSNotificationNameavpZ)

  `
  `  
  The name of the `NSNotificationCenter` notification which is posted when the auth state
  changes (for example, a new token has been produced, a user signs in or signs out).

  The object parameter of the notification is the sender `Auth` instance.  

  #### Declaration

  Swift  

      public static let authStateDidChangeNotification: NSNotification.Name

[## Internal properties](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/Internal-properties)

- `
  ``
  ``
  `

  ### [mainBundleUrlTypes](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/)

  `
  `  
  Allow tests to swap in an alternate mainBundle, including ObjC unit tests via CocoaPods.
- `
  ``
  ``
  `

  ### [scene(_:openURLContexts:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@CM@FirebaseAuth@objc(cs)FIRAuth(im)scene:openURLContexts:)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      @MainActor
      open func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>)

- `
  ``
  ``
  `

  ### [application(_:didRegisterForRemoteNotificationsWithDeviceToken:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@CM@FirebaseAuth@objc(cs)FIRAuth(im)application:didRegisterForRemoteNotificationsWithDeviceToken:)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      @MainActor
      open func application(_ application: UIApplication,
                            didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data)

- `
  ``
  ``
  `

  ### [application(_:didFailToRegisterForRemoteNotificationsWithError:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@CM@FirebaseAuth@objc(cs)FIRAuth(im)application:didFailToRegisterForRemoteNotificationsWithError:)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      @MainActor
      open func application(_ application: UIApplication,
                            didFailToRegisterForRemoteNotificationsWithError error: Error)

- `
  ``
  ``
  `

  ### [application(_:didReceiveRemoteNotification:fetchCompletionHandler:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@CM@FirebaseAuth@objc(cs)FIRAuth(im)application:didReceiveRemoteNotification:fetchCompletionHandler:)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      @MainActor
      open func application(_ application: UIApplication,
                            didReceiveRemoteNotification userInfo: [AnyHashable: Any],
                            fetchCompletionHandler completionHandler:
                            @escaping (UIBackgroundFetchResult) -> Void)

- `
  ``
  ``
  `

  ### [application(_:open:options:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@CM@FirebaseAuth@objc(cs)FIRAuth(im)application:openURL:options:)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      @MainActor
      open func application(_ application: UIApplication,
                            open url: URL,
                            options: [UIApplication.OpenURLOptionsKey: Any]) -> Bool

- `
  ``
  ``
  `

  ### [getToken(forcingRefresh:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@CM@FirebaseAuth@objc(cs)FIRAuth(im)getTokenForcingRefresh:withCallback:)

  `
  `  
  Retrieves the Firebase authentication token, possibly refreshing it if it has expired.

  This method is not for public use. It is for Firebase clients of AuthInterop.  

  #### Declaration

  Swift  

      @objc(getTokenForcingRefresh:withCallback:)
      public func getToken(forcingRefresh forceRefresh: Bool,
                           completion callback: @escaping (String?, Error?) -> Void)

- `
  ``
  ``
  `

  ### [getUserID()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth#/c:@CM@FirebaseAuth@objc(cs)FIRAuth(im)getUserID)

  `
  `  
  Get the current Auth user's UID. Returns nil if there is no user signed in.

  This method is not for public use. It is for Firebase clients of AuthInterop.  

  #### Declaration

  Swift  

      open func getUserID() -> String?