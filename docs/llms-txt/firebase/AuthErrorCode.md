# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AuthErrorCode.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode.md.txt

# FirebaseAuth Framework Reference

# AuthErrorCode

    @objc(FIRAuthErrorCode)
    public enum AuthErrorCode : Int, Error

Error codes used by Firebase Auth.
- `
  ``
  ``
  `

  ### [invalidCustomToken](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidCustomToken)

  `
  `  
  Indicates a validation error with the custom token.  

  #### Declaration

  Swift  

      case invalidCustomToken = 17000

- `
  ``
  ``
  `

  ### [customTokenMismatch](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeCustomTokenMismatch)

  `
  `  
  Indicates the service account and the API key belong to different projects.  

  #### Declaration

  Swift  

      case customTokenMismatch = 17002

- `
  ``
  ``
  `

  ### [invalidCredential](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidCredential)

  `
  `  
  Indicates the IDP token or requestUri is invalid.  

  #### Declaration

  Swift  

      case invalidCredential = 17004

- `
  ``
  ``
  `

  ### [userDisabled](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeUserDisabled)

  `
  `  
  Indicates the user's account is disabled on the server.  

  #### Declaration

  Swift  

      case userDisabled = 17005

- `
  ``
  ``
  `

  ### [operationNotAllowed](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeOperationNotAllowed)

  `
  `  
  Indicates the administrator disabled sign in with the specified identity provider.  

  #### Declaration

  Swift  

      case operationNotAllowed = 17006

- `
  ``
  ``
  `

  ### [emailAlreadyInUse](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeEmailAlreadyInUse)

  `
  `  
  Indicates the email used to attempt a sign up is already in use.  

  #### Declaration

  Swift  

      case emailAlreadyInUse = 17007

- `
  ``
  ``
  `

  ### [invalidEmail](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidEmail)

  `
  `  
  Indicates the email is invalid.  

  #### Declaration

  Swift  

      case invalidEmail = 17008

- `
  ``
  ``
  `

  ### [wrongPassword](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeWrongPassword)

  `
  `  
  Indicates the user attempted sign in with a wrong password.  

  #### Declaration

  Swift  

      case wrongPassword = 17009

- `
  ``
  ``
  `

  ### [tooManyRequests](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeTooManyRequests)

  `
  `  
  Indicates that too many requests were made to a server method.  

  #### Declaration

  Swift  

      case tooManyRequests = 17010

- `
  ``
  ``
  `

  ### [userNotFound](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeUserNotFound)

  `
  `  
  Indicates the user account was not found.  

  #### Declaration

  Swift  

      case userNotFound = 17011

- `
  ``
  ``
  `

  ### [accountExistsWithDifferentCredential](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeAccountExistsWithDifferentCredential)

  `
  `  
  Indicates account linking is required.  

  #### Declaration

  Swift  

      case accountExistsWithDifferentCredential = 17012

- `
  ``
  ``
  `

  ### [requiresRecentLogin](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeRequiresRecentLogin)

  `
  `  
  Indicates the user has attempted to change email or password more than 5 minutes after
  signing in.  

  #### Declaration

  Swift  

      case requiresRecentLogin = 17014

- `
  ``
  ``
  `

  ### [providerAlreadyLinked](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeProviderAlreadyLinked)

  `
  `  
  Indicates an attempt to link a provider to which the account is already linked.  

  #### Declaration

  Swift  

      case providerAlreadyLinked = 17015

- `
  ``
  ``
  `

  ### [noSuchProvider](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeNoSuchProvider)

  `
  `  
  Indicates an attempt to unlink a provider that is not linked.  

  #### Declaration

  Swift  

      case noSuchProvider = 17016

- `
  ``
  ``
  `

  ### [invalidUserToken](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidUserToken)

  `
  `  
  Indicates user's saved auth credential is invalid the user needs to sign in again.  

  #### Declaration

  Swift  

      case invalidUserToken = 17017

- `
  ``
  ``
  `

  ### [networkError](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeNetworkError)

  `
  `  
  Indicates a network error occurred (such as a timeout interrupted connection or
  unreachable host). These types of errors are often recoverable with a retry. The
  `NSUnderlyingError` field in the `NSError.userInfo` dictionary will contain the error
  encountered.  

  #### Declaration

  Swift  

      case networkError = 17020

- `
  ``
  ``
  `

  ### [userTokenExpired](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeUserTokenExpired)

  `
  `  
  Indicates the saved token has expired for example the user may have changed account
  password on another device. The user needs to sign in again on the device that made this
  request.  

  #### Declaration

  Swift  

      case userTokenExpired = 17021

- `
  ``
  ``
  `

  ### [invalidAPIKey](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidAPIKey)

  `
  `  
  Indicates an invalid API key was supplied in the request.  

  #### Declaration

  Swift  

      case invalidAPIKey = 17023

- `
  ``
  ``
  `

  ### [userMismatch](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeUserMismatch)

  `
  `  
  Indicates that an attempt was made to reauthenticate with a user which is not the current
  user.  

  #### Declaration

  Swift  

      case userMismatch = 17024

- `
  ``
  ``
  `

  ### [credentialAlreadyInUse](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeCredentialAlreadyInUse)

  `
  `  
  Indicates an attempt to link with a credential that has already been linked with a
  different Firebase account.  

  #### Declaration

  Swift  

      case credentialAlreadyInUse = 17025

- `
  ``
  ``
  `

  ### [weakPassword](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeWeakPassword)

  `
  `  
  Indicates an attempt to set a password that is considered too weak.  

  #### Declaration

  Swift  

      case weakPassword = 17026

- `
  ``
  ``
  `

  ### [appNotAuthorized](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeAppNotAuthorized)

  `
  `  
  Indicates the App is not authorized to use Firebase Authentication with the
  provided API Key.  

  #### Declaration

  Swift  

      case appNotAuthorized = 17028

- `
  ``
  ``
  `

  ### [expiredActionCode](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeExpiredActionCode)

  `
  `  
  Indicates the OOB code is expired.  

  #### Declaration

  Swift  

      case expiredActionCode = 17029

- `
  ``
  ``
  `

  ### [invalidActionCode](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidActionCode)

  `
  `  
  Indicates the OOB code is invalid.  

  #### Declaration

  Swift  

      case invalidActionCode = 17030

- `
  ``
  ``
  `

  ### [invalidMessagePayload](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidMessagePayload)

  `
  `  
  Indicates that there are invalid parameters in the payload during a
  "send password reset email" attempt.  

  #### Declaration

  Swift  

      case invalidMessagePayload = 17031

- `
  ``
  ``
  `

  ### [invalidSender](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidSender)

  `
  `  
  Indicates that the sender email is invalid during a "send password reset email" attempt.  

  #### Declaration

  Swift  

      case invalidSender = 17032

- `
  ``
  ``
  `

  ### [invalidRecipientEmail](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidRecipientEmail)

  `
  `  
  Indicates that the recipient email is invalid.  

  #### Declaration

  Swift  

      case invalidRecipientEmail = 17033

- `
  ``
  ``
  `

  ### [missingEmail](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingEmail)

  `
  `  
  Indicates that an email address was expected but one was not provided.  

  #### Declaration

  Swift  

      case missingEmail = 17034

- `
  ``
  ``
  `

  ### [missingIosBundleID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingIosBundleID)

  `
  `  
  Indicates that the iOS bundle ID is missing when a iOS App Store ID is provided.  

  #### Declaration

  Swift  

      case missingIosBundleID = 17036

- `
  ``
  ``
  `

  ### [missingAndroidPackageName](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingAndroidPackageName)

  `
  `  
  Indicates that the android package name is missing when the `androidInstallApp` flag is set
  to `true`.  

  #### Declaration

  Swift  

      case missingAndroidPackageName = 17037

- `
  ``
  ``
  `

  ### [unauthorizedDomain](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeUnauthorizedDomain)

  `
  `  
  Indicates that the domain specified in the continue URL is not allowlisted in the Firebase
  console.  

  #### Declaration

  Swift  

      case unauthorizedDomain = 17038

- `
  ``
  ``
  `

  ### [invalidContinueURI](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidContinueURI)

  `
  `  
  Indicates that the domain specified in the continue URI is not valid.  

  #### Declaration

  Swift  

      case invalidContinueURI = 17039

- `
  ``
  ``
  `

  ### [missingContinueURI](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingContinueURI)

  `
  `  
  Indicates that a continue URI was not provided in a request to the backend which requires one.  

  #### Declaration

  Swift  

      case missingContinueURI = 17040

- `
  ``
  ``
  `

  ### [missingPhoneNumber](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingPhoneNumber)

  `
  `  
  Indicates that a phone number was not provided in a call to
  `verifyPhoneNumber:completion:`.  

  #### Declaration

  Swift  

      case missingPhoneNumber = 17041

- `
  ``
  ``
  `

  ### [invalidPhoneNumber](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidPhoneNumber)

  `
  `  
  Indicates that an invalid phone number was provided in a call to
  `verifyPhoneNumber:completion:`.  

  #### Declaration

  Swift  

      case invalidPhoneNumber = 17042

- `
  ``
  ``
  `

  ### [missingVerificationCode](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingVerificationCode)

  `
  `  
  Indicates that the phone auth credential was created with an empty verification code.  

  #### Declaration

  Swift  

      case missingVerificationCode = 17043

- `
  ``
  ``
  `

  ### [invalidVerificationCode](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidVerificationCode)

  `
  `  
  Indicates that an invalid verification code was used in the verifyPhoneNumber request.  

  #### Declaration

  Swift  

      case invalidVerificationCode = 17044

- `
  ``
  ``
  `

  ### [missingVerificationID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingVerificationID)

  `
  `  
  Indicates that the phone auth credential was created with an empty verification ID.  

  #### Declaration

  Swift  

      case missingVerificationID = 17045

- `
  ``
  ``
  `

  ### [invalidVerificationID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidVerificationID)

  `
  `  
  Indicates that an invalid verification ID was used in the verifyPhoneNumber request.  

  #### Declaration

  Swift  

      case invalidVerificationID = 17046

- `
  ``
  ``
  `

  ### [missingAppCredential](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingAppCredential)

  `
  `  
  Indicates that the APNS device token is missing in the verifyClient request.  

  #### Declaration

  Swift  

      case missingAppCredential = 17047

- `
  ``
  ``
  `

  ### [invalidAppCredential](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidAppCredential)

  `
  `  
  Indicates that an invalid APNS device token was used in the verifyClient request.  

  #### Declaration

  Swift  

      case invalidAppCredential = 17048

- `
  ``
  ``
  `

  ### [sessionExpired](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeSessionExpired)

  `
  `  
  Indicates that the SMS code has expired.  

  #### Declaration

  Swift  

      case sessionExpired = 17051

- `
  ``
  ``
  `

  ### [quotaExceeded](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeQuotaExceeded)

  `
  `  
  Indicates that the quota of SMS messages for a given project has been exceeded.  

  #### Declaration

  Swift  

      case quotaExceeded = 17052

- `
  ``
  ``
  `

  ### [missingAppToken](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingAppToken)

  `
  `  
  Indicates that the APNs device token could not be obtained. The app may not have set up
  remote notification correctly or may fail to forward the APNs device token to Auth
  if app delegate swizzling is disabled.  

  #### Declaration

  Swift  

      case missingAppToken = 17053

- `
  ``
  ``
  `

  ### [notificationNotForwarded](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeNotificationNotForwarded)

  `
  `  
  Indicates that the app fails to forward remote notification to FIRAuth.  

  #### Declaration

  Swift  

      case notificationNotForwarded = 17054

- `
  ``
  ``
  `

  ### [appNotVerified](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeAppNotVerified)

  `
  `  
  Indicates that the app could not be verified by Firebase during phone number authentication.  

  #### Declaration

  Swift  

      case appNotVerified = 17055

- `
  ``
  ``
  `

  ### [captchaCheckFailed](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeCaptchaCheckFailed)

  `
  `  
  Indicates that the reCAPTCHA token is not valid.  

  #### Declaration

  Swift  

      case captchaCheckFailed = 17056

- `
  ``
  ``
  `

  ### [webContextAlreadyPresented](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeWebContextAlreadyPresented)

  `
  `  
  Indicates that an attempt was made to present a new web context while one was already being
  presented.  

  #### Declaration

  Swift  

      case webContextAlreadyPresented = 17057

- `
  ``
  ``
  `

  ### [webContextCancelled](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeWebContextCancelled)

  `
  `  
  Indicates that the URL presentation was cancelled prematurely by the user.  

  #### Declaration

  Swift  

      case webContextCancelled = 17058

- `
  ``
  ``
  `

  ### [appVerificationUserInteractionFailure](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeAppVerificationUserInteractionFailure)

  `
  `  
  Indicates a general failure during the app verification flow.  

  #### Declaration

  Swift  

      case appVerificationUserInteractionFailure = 17059

- `
  ``
  ``
  `

  ### [invalidClientID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidClientID)

  `
  `  
  Indicates that the clientID used to invoke a web flow is invalid.  

  #### Declaration

  Swift  

      case invalidClientID = 17060

- `
  ``
  ``
  `

  ### [webNetworkRequestFailed](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeWebNetworkRequestFailed)

  `
  `  
  Indicates that a network request within a SFSafariViewController or WKWebView failed.  

  #### Declaration

  Swift  

      case webNetworkRequestFailed = 17061

- `
  ``
  ``
  `

  ### [webInternalError](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeWebInternalError)

  `
  `  
  Indicates that an internal error occurred within a SFSafariViewController or WKWebView.  

  #### Declaration

  Swift  

      case webInternalError = 17062

- `
  ``
  ``
  `

  ### [webSignInUserInteractionFailure](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeWebSignInUserInteractionFailure)

  `
  `  
  Indicates a general failure during a web sign-in flow.  

  #### Declaration

  Swift  

      case webSignInUserInteractionFailure = 17063

- `
  ``
  ``
  `

  ### [localPlayerNotAuthenticated](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeLocalPlayerNotAuthenticated)

  `
  `  
  Indicates that the local player was not authenticated prior to attempting Game Center signin.  

  #### Declaration

  Swift  

      case localPlayerNotAuthenticated = 17066

- `
  ``
  ``
  `

  ### [nullUser](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeNullUser)

  `
  `  
  Indicates that a non-null user was expected as an argument to the operation but a null
  user was provided.  

  #### Declaration

  Swift  

      case nullUser = 17067

- `
  ``
  ``
  `

  ### [invalidProviderID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidProviderID)

  `
  `  
  Represents the error code for when the given provider id for a web operation is invalid.  

  #### Declaration

  Swift  

      case invalidProviderID = 17071

- `
  ``
  ``
  `

  ### [tenantIDMismatch](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeTenantIDMismatch)

  `
  `  
  Represents the error code for when an attempt is made to update the current user with a
  tenantId that differs from the current FirebaseAuth instance's tenantId.  

  #### Declaration

  Swift  

      case tenantIDMismatch = 17072

- `
  ``
  ``
  `

  ### [unsupportedTenantOperation](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeUnsupportedTenantOperation)

  `
  `  
  Represents the error code for when a request is made to the backend with an associated tenant
  ID for an operation that does not support multi-tenancy.  

  #### Declaration

  Swift  

      case unsupportedTenantOperation = 17073

- `
  ``
  ``
  `

  ### [invalidHostingLinkDomain](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidHostingLinkDomain)

  `
  `  
  Indicates that the provided Firebase Hosting Link domain is not owned by the current project.  

  #### Declaration

  Swift  

      case invalidHostingLinkDomain = 17214

- `
  ``
  ``
  `

  ### [rejectedCredential](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeRejectedCredential)

  `
  `  
  Indicates that the credential is rejected because it's malformed or mismatching.  

  #### Declaration

  Swift  

      case rejectedCredential = 17075

- `
  ``
  ``
  `

  ### [gameKitNotLinked](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeGameKitNotLinked)

  `
  `  
  Indicates that the GameKit framework is not linked prior to attempting Game Center signin.  

  #### Declaration

  Swift  

      case gameKitNotLinked = 17076

- `
  ``
  ``
  `

  ### [secondFactorRequired](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeSecondFactorRequired)

  `
  `  
  Indicates that the second factor is required for signin.  

  #### Declaration

  Swift  

      case secondFactorRequired = 17078

- `
  ``
  ``
  `

  ### [missingMultiFactorSession](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingMultiFactorSession)

  `
  `  
  Indicates that the multi factor session is missing.  

  #### Declaration

  Swift  

      case missingMultiFactorSession = 17081

- `
  ``
  ``
  `

  ### [missingMultiFactorInfo](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingMultiFactorInfo)

  `
  `  
  Indicates that the multi factor info is missing.  

  #### Declaration

  Swift  

      case missingMultiFactorInfo = 17082

- `
  ``
  ``
  `

  ### [invalidMultiFactorSession](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidMultiFactorSession)

  `
  `  
  Indicates that the multi factor session is invalid.  

  #### Declaration

  Swift  

      case invalidMultiFactorSession = 17083

- `
  ``
  ``
  `

  ### [multiFactorInfoNotFound](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeMultiFactorInfoNotFound)

  `
  `  
  Indicates that the multi factor info is not found.  

  #### Declaration

  Swift  

      case multiFactorInfoNotFound = 17084

- `
  ``
  ``
  `

  ### [adminRestrictedOperation](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeAdminRestrictedOperation)

  `
  `  
  Indicates that the operation is admin restricted.  

  #### Declaration

  Swift  

      case adminRestrictedOperation = 17085

- `
  ``
  ``
  `

  ### [unverifiedEmail](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeUnverifiedEmail)

  `
  `  
  Indicates that the email is required for verification.  

  #### Declaration

  Swift  

      case unverifiedEmail = 17086

- `
  ``
  ``
  `

  ### [secondFactorAlreadyEnrolled](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeSecondFactorAlreadyEnrolled)

  `
  `  
  Indicates that the second factor is already enrolled.  

  #### Declaration

  Swift  

      case secondFactorAlreadyEnrolled = 17087

- `
  ``
  ``
  `

  ### [maximumSecondFactorCountExceeded](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeMaximumSecondFactorCountExceeded)

  `
  `  
  Indicates that the maximum second factor count is exceeded.  

  #### Declaration

  Swift  

      case maximumSecondFactorCountExceeded = 17088

- `
  ``
  ``
  `

  ### [unsupportedFirstFactor](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeUnsupportedFirstFactor)

  `
  `  
  Indicates that the first factor is not supported.  

  #### Declaration

  Swift  

      case unsupportedFirstFactor = 17089

- `
  ``
  ``
  `

  ### [emailChangeNeedsVerification](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeEmailChangeNeedsVerification)

  `
  `  
  Indicates that the a verified email is required to changed to.  

  #### Declaration

  Swift  

      case emailChangeNeedsVerification = 17090

- `
  ``
  ``
  `

  ### [missingClientIdentifier](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingClientIdentifier)

  `
  `  
  Indicates that the request does not contain a client identifier.  

  #### Declaration

  Swift  

      case missingClientIdentifier = 17093

- `
  ``
  ``
  `

  ### [missingOrInvalidNonce](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingOrInvalidNonce)

  `
  `  
  Indicates that the nonce is missing or invalid.  

  #### Declaration

  Swift  

      case missingOrInvalidNonce = 17094

- `
  ``
  ``
  `

  ### [blockingCloudFunctionError](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeBlockingCloudFunctionError)

  `
  `  
  Raised when a Cloud Function returns a blocking error. Will include a message returned from
  the function.  

  #### Declaration

  Swift  

      case blockingCloudFunctionError = 17105

- `
  ``
  ``
  `

  ### [recaptchaNotEnabled](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeRecaptchaNotEnabled)

  `
  `  
  Indicates that reCAPTCHA Enterprise integration is not enabled for this project.  

  #### Declaration

  Swift  

      case recaptchaNotEnabled = 17200

- `
  ``
  ``
  `

  ### [missingRecaptchaToken](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingRecaptchaToken)

  `
  `  
  Indicates that the reCAPTCHA token is missing from the backend request.  

  #### Declaration

  Swift  

      case missingRecaptchaToken = 17201

- `
  ``
  ``
  `

  ### [invalidRecaptchaToken](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidRecaptchaToken)

  `
  `  
  Indicates that the reCAPTCHA token sent with the backend request is invalid.  

  #### Declaration

  Swift  

      case invalidRecaptchaToken = 17202

- `
  ``
  ``
  `

  ### [invalidRecaptchaAction](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidRecaptchaAction)

  `
  `  
  Indicates that the requested reCAPTCHA action is invalid.  

  #### Declaration

  Swift  

      case invalidRecaptchaAction = 17203

- `
  ``
  ``
  `

  ### [missingClientType](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingClientType)

  `
  `  
  Indicates that the client type is missing from the request.  

  #### Declaration

  Swift  

      case missingClientType = 17204

- `
  ``
  ``
  `

  ### [missingRecaptchaVersion](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingRecaptchaVersion)

  `
  `  
  Indicates that the reCAPTCHA version is missing from the request.  

  #### Declaration

  Swift  

      case missingRecaptchaVersion = 17205

- `
  ``
  ``
  `

  ### [invalidRecaptchaVersion](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidRecaptchaVersion)

  `
  `  
  Indicates that the reCAPTCHA version sent to the backend is invalid.  

  #### Declaration

  Swift  

      case invalidRecaptchaVersion = 17206

- `
  ``
  ``
  `

  ### [invalidReqType](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidReqType)

  `
  `  
  Indicates that the request type sent to the backend is invalid.  

  #### Declaration

  Swift  

      case invalidReqType = 17207

- `
  ``
  ``
  `

  ### [recaptchaSDKNotLinked](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeRecaptchaSDKNotLinked)

  `
  `  
  Indicates that the reCAPTCHA SDK is not linked to the app.  

  #### Declaration

  Swift  

      case recaptchaSDKNotLinked = 17208

- `
  ``
  ``
  `

  ### [recaptchaSiteKeyMissing](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeRecaptchaSiteKeyMissing)

  `
  `  
  Indicates that the reCAPTCHA SDK site key wasn't found.  

  #### Declaration

  Swift  

      case recaptchaSiteKeyMissing = 17209

- `
  ``
  ``
  `

  ### [recaptchaActionCreationFailed](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeRecaptchaActionCreationFailed)

  `
  `  
  Indicates that the reCAPTCHA SDK actions class failed to create.  

  #### Declaration

  Swift  

      case recaptchaActionCreationFailed = 17210

- `
  ``
  ``
  `

  ### [keychainError](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeKeychainError)

  `
  `  
  Indicates an error occurred while attempting to access the keychain.  

  #### Declaration

  Swift  

      case keychainError = 17995

- `
  ``
  ``
  `

  ### [internalError](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeInternalError)

  `
  `  
  Indicates an internal error occurred.  

  #### Declaration

  Swift  

      case internalError = 17999

- `
  ``
  ``
  `

  ### [malformedJWT](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/c:@M@FirebaseAuth@E@FIRAuthErrorCode@FIRAuthErrorCodeMalformedJWT)

  `
  `  
  Raised when a JWT fails to parse correctly. May be accompanied by an underlying error
  describing which step of the JWT parsing process failed.  

  #### Declaration

  Swift  

      case malformedJWT = 18000

- `
  ``
  ``
  `

  ### [code](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthErrorCode#/s:12FirebaseAuth0B9ErrorCodeO4codeACvp)

  `
  `  
  The error code. It's redundant but implemented for compatibility with the Objective-C
  implementation.  

  #### Declaration

  Swift  

      public var code: `Self` { get }