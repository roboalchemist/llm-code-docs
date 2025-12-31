# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode.md.txt

# FirebaseAuth Framework Reference

# FIRAuthErrorCode

    enum FIRAuthErrorCode : NSInteger {}

Error codes used by Firebase Auth.
- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidCustomToken](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidCustomToken)

  `
  `  
  Indicates a validation error with the custom token.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidCustomToken = 17000

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeCustomTokenMismatch](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeCustomTokenMismatch)

  `
  `  
  Indicates the service account and the API key belong to different projects.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeCustomTokenMismatch = 17002

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidCredential](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidCredential)

  `
  `  
  Indicates the IDP token or requestUri is invalid.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidCredential = 17004

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeUserDisabled](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeUserDisabled)

  `
  `  
  Indicates the user's account is disabled on the server.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeUserDisabled = 17005

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeOperationNotAllowed](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeOperationNotAllowed)

  `
  `  
  Indicates the administrator disabled sign in with the specified identity provider.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeOperationNotAllowed = 17006

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeEmailAlreadyInUse](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeEmailAlreadyInUse)

  `
  `  
  Indicates the email used to attempt a sign up is already in use.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeEmailAlreadyInUse = 17007

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidEmail](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidEmail)

  `
  `  
  Indicates the email is invalid.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidEmail = 17008

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeWrongPassword](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeWrongPassword)

  `
  `  
  Indicates the user attempted sign in with a wrong password.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeWrongPassword = 17009

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeTooManyRequests](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeTooManyRequests)

  `
  `  
  Indicates that too many requests were made to a server method.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeTooManyRequests = 17010

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeUserNotFound](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeUserNotFound)

  `
  `  
  Indicates the user account was not found.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeUserNotFound = 17011

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeAccountExistsWithDifferentCredential](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeAccountExistsWithDifferentCredential)

  `
  `  
  Indicates account linking is required.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeAccountExistsWithDifferentCredential = 17012

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeRequiresRecentLogin](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeRequiresRecentLogin)

  `
  `  
  Indicates the user has attemped to change email or password more than 5 minutes after
  signing in.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeRequiresRecentLogin = 17014

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeProviderAlreadyLinked](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeProviderAlreadyLinked)

  `
  `  
  Indicates an attempt to link a provider to which the account is already linked.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeProviderAlreadyLinked = 17015

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeNoSuchProvider](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeNoSuchProvider)

  `
  `  
  Indicates an attempt to unlink a provider that is not linked.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeNoSuchProvider = 17016

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidUserToken](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidUserToken)

  `
  `  
  Indicates user's saved auth credential is invalid, the user needs to sign in again.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidUserToken = 17017

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeNetworkError](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeNetworkError)

  `
  `  
  Indicates a network error occurred (such as a timeout, interrupted connection, or
  unreachable host). These types of errors are often recoverable with a retry. The
  `NSUnderlyingError` field in the `NSError.userInfo` dictionary will contain the error
  encountered.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeNetworkError = 17020

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeUserTokenExpired](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeUserTokenExpired)

  `
  `  
  Indicates the saved token has expired, for example, the user may have changed account
  password on another device. The user needs to sign in again on the device that made this
  request.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeUserTokenExpired = 17021

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidAPIKey](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidAPIKey)

  `
  `  
  Indicates an invalid API key was supplied in the request.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidAPIKey = 17023

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeUserMismatch](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeUserMismatch)

  `
  `  
  Indicates that an attempt was made to reauthenticate with a user which is not the current
  user.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeUserMismatch = 17024

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeCredentialAlreadyInUse](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeCredentialAlreadyInUse)

  `
  `  
  Indicates an attempt to link with a credential that has already been linked with a
  different Firebase account  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeCredentialAlreadyInUse = 17025

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeWeakPassword](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeWeakPassword)

  `
  `  
  Indicates an attempt to set a password that is considered too weak.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeWeakPassword = 17026

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeAppNotAuthorized](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeAppNotAuthorized)

  `
  `  
  Indicates the App is not authorized to use Firebase Authentication with the
  provided API Key.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeAppNotAuthorized = 17028

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeExpiredActionCode](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeExpiredActionCode)

  `
  `  
  Indicates the OOB code is expired.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeExpiredActionCode = 17029

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidActionCode](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidActionCode)

  `
  `  
  Indicates the OOB code is invalid.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidActionCode = 17030

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidMessagePayload](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidMessagePayload)

  `
  `  
  Indicates that there are invalid parameters in the payload during a "send password reset
  \* email" attempt.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidMessagePayload = 17031

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidSender](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidSender)

  `
  `  
  Indicates that the sender email is invalid during a "send password reset email" attempt.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidSender = 17032

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidRecipientEmail](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidRecipientEmail)

  `
  `  
  Indicates that the recipient email is invalid.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidRecipientEmail = 17033

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeMissingEmail](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingEmail)

  `
  `  
  Indicates that an email address was expected but one was not provided.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeMissingEmail = 17034

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeMissingIosBundleID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingIosBundleID)

  `
  `  
  Indicates that the iOS bundle ID is missing when a iOS App Store ID is provided.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeMissingIosBundleID = 17036

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeMissingAndroidPackageName](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingAndroidPackageName)

  `
  `  
  Indicates that the android package name is missing when the `androidInstallApp` flag is set
  to true.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeMissingAndroidPackageName = 17037

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeUnauthorizedDomain](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeUnauthorizedDomain)

  `
  `  
  Indicates that the domain specified in the continue URL is not allowlisted in the Firebase
  console.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeUnauthorizedDomain = 17038

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidContinueURI](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidContinueURI)

  `
  `  
  Indicates that the domain specified in the continue URI is not valid.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidContinueURI = 17039

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeMissingContinueURI](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingContinueURI)

  `
  `  
  Indicates that a continue URI was not provided in a request to the backend which requires
  one.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeMissingContinueURI = 17040

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeMissingPhoneNumber](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingPhoneNumber)

  `
  `  
  Indicates that a phone number was not provided in a call to
  `verifyPhoneNumber:completion:`.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeMissingPhoneNumber = 17041

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidPhoneNumber](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidPhoneNumber)

  `
  `  
  Indicates that an invalid phone number was provided in a call to
  `verifyPhoneNumber:completion:`.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidPhoneNumber = 17042

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeMissingVerificationCode](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingVerificationCode)

  `
  `  
  Indicates that the phone auth credential was created with an empty verification code.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeMissingVerificationCode = 17043

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidVerificationCode](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidVerificationCode)

  `
  `  
  Indicates that an invalid verification code was used in the verifyPhoneNumber request.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidVerificationCode = 17044

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeMissingVerificationID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingVerificationID)

  `
  `  
  Indicates that the phone auth credential was created with an empty verification ID.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeMissingVerificationID = 17045

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidVerificationID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidVerificationID)

  `
  `  
  Indicates that an invalid verification ID was used in the verifyPhoneNumber request.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidVerificationID = 17046

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeMissingAppCredential](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingAppCredential)

  `
  `  
  Indicates that the APNS device token is missing in the verifyClient request.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeMissingAppCredential = 17047

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidAppCredential](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidAppCredential)

  `
  `  
  Indicates that an invalid APNS device token was used in the verifyClient request.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidAppCredential = 17048

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeSessionExpired](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeSessionExpired)

  `
  `  
  Indicates that the SMS code has expired.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeSessionExpired = 17051

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeQuotaExceeded](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeQuotaExceeded)

  `
  `  
  Indicates that the quota of SMS messages for a given project has been exceeded.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeQuotaExceeded = 17052

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeMissingAppToken](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingAppToken)

  `
  `  
  Indicates that the APNs device token could not be obtained. The app may not have set up
  remote notification correctly, or may fail to forward the APNs device token to Auth
  if app delegate swizzling is disabled.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeMissingAppToken = 17053

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeNotificationNotForwarded](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeNotificationNotForwarded)

  `
  `  
  Indicates that the app fails to forward remote notification to Auth.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeNotificationNotForwarded = 17054

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeAppNotVerified](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeAppNotVerified)

  `
  `  
  Indicates that the app could not be verified by Firebase during phone number authentication.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeAppNotVerified = 17055

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeCaptchaCheckFailed](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeCaptchaCheckFailed)

  `
  `  
  Indicates that the reCAPTCHA token is not valid.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeCaptchaCheckFailed = 17056

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeWebContextAlreadyPresented](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeWebContextAlreadyPresented)

  `
  `  
  Indicates that an attempt was made to present a new web context while one was already being
  presented.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeWebContextAlreadyPresented = 17057

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeWebContextCancelled](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeWebContextCancelled)

  `
  `  
  Indicates that the URL presentation was cancelled prematurely by the user.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeWebContextCancelled = 17058

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeAppVerificationUserInteractionFailure](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeAppVerificationUserInteractionFailure)

  `
  `  
  Indicates a general failure during the app verification flow.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeAppVerificationUserInteractionFailure = 17059

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidClientID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidClientID)

  `
  `  
  Indicates that the clientID used to invoke a web flow is invalid.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidClientID = 17060

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeWebNetworkRequestFailed](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeWebNetworkRequestFailed)

  `
  `  
  Indicates that a network request within a SFSafariViewController or WKWebView failed.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeWebNetworkRequestFailed = 17061

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeWebInternalError](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeWebInternalError)

  `
  `  
  Indicates that an internal error occurred within a SFSafariViewController or WKWebView.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeWebInternalError = 17062

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeWebSignInUserInteractionFailure](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeWebSignInUserInteractionFailure)

  `
  `  
  Indicates a general failure during a web sign-in flow.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeWebSignInUserInteractionFailure = 17063

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeLocalPlayerNotAuthenticated](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeLocalPlayerNotAuthenticated)

  `
  `  
  Indicates that the local player was not authenticated prior to attempting Game Center
  signin.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeLocalPlayerNotAuthenticated = 17066

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeNullUser](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeNullUser)

  `
  `  
  Indicates that a non-null user was expected as an argmument to the operation but a null
  user was provided.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeNullUser = 17067

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeDynamicLinkNotActivated](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeDynamicLinkNotActivated)

  `
  `  
  Indicates that a Firebase Dynamic Link is not activated.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeDynamicLinkNotActivated = 17068

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidProviderID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidProviderID)

  `
  `  
  Represents the error code for when the given provider id for a web operation is invalid.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidProviderID = 17071

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeTenantIDMismatch](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeTenantIDMismatch)

  `
  `  
  Represents the error code for when an attempt is made to update the current user with a
  tenantId that differs from the current FirebaseAuth instance's tenantId.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeTenantIDMismatch = 17072

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeUnsupportedTenantOperation](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeUnsupportedTenantOperation)

  `
  `  
  Represents the error code for when a request is made to the backend with an associated tenant
  ID for an operation that does not support multi-tenancy.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeUnsupportedTenantOperation = 17073

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidDynamicLinkDomain](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidDynamicLinkDomain)

  `
  `  
  Indicates that the Firebase Dynamic Link domain used is either not configured or is
  unauthorized for the current project.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidDynamicLinkDomain = 17074

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeRejectedCredential](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeRejectedCredential)

  `
  `  
  Indicates that the credential is rejected because it's misformed or mismatching.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeRejectedCredential = 17075

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeGameKitNotLinked](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeGameKitNotLinked)

  `
  `  
  Indicates that the GameKit framework is not linked prior to attempting Game Center signin.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeGameKitNotLinked = 17076

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeSecondFactorRequired](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeSecondFactorRequired)

  `
  `  
  Indicates that the second factor is required for signin.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeSecondFactorRequired = 17078

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeMissingMultiFactorSession](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingMultiFactorSession)

  `
  `  
  Indicates that the multi factor session is missing.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeMissingMultiFactorSession = 17081

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeMissingMultiFactorInfo](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingMultiFactorInfo)

  `
  `  
  Indicates that the multi factor info is missing.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeMissingMultiFactorInfo = 17082

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidMultiFactorSession](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidMultiFactorSession)

  `
  `  
  Indicates that the multi factor session is invalid.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidMultiFactorSession = 17083

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeMultiFactorInfoNotFound](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeMultiFactorInfoNotFound)

  `
  `  
  Indicates that the multi factor info is not found.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeMultiFactorInfoNotFound = 17084

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeAdminRestrictedOperation](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeAdminRestrictedOperation)

  `
  `  
  Indicates that the operation is admin restricted.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeAdminRestrictedOperation = 17085

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeUnverifiedEmail](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeUnverifiedEmail)

  `
  `  
  Indicates that the email is required for verification.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeUnverifiedEmail = 17086

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeSecondFactorAlreadyEnrolled](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeSecondFactorAlreadyEnrolled)

  `
  `  
  Indicates that the second factor is already enrolled.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeSecondFactorAlreadyEnrolled = 17087

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeMaximumSecondFactorCountExceeded](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeMaximumSecondFactorCountExceeded)

  `
  `  
  Indicates that the maximum second factor count is exceeded.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeMaximumSecondFactorCountExceeded = 17088

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeUnsupportedFirstFactor](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeUnsupportedFirstFactor)

  `
  `  
  Indicates that the first factor is not supported.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeUnsupportedFirstFactor = 17089

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeEmailChangeNeedsVerification](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeEmailChangeNeedsVerification)

  `
  `  
  Indicates that the a verifed email is required to changed to.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeEmailChangeNeedsVerification = 17090

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeMissingClientIdentifier](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingClientIdentifier)

  `
  `  
  Indicates that the request does not contain a client identifier.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeMissingClientIdentifier = 17093

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeMissingOrInvalidNonce](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingOrInvalidNonce)

  `
  `  
  Indicates that the nonce is missing or invalid.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeMissingOrInvalidNonce = 17094

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeBlockingCloudFunctionError](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeBlockingCloudFunctionError)

  `
  `  
  Raised when a Cloud Function returns a blocking error. Will include a message returned from
  \* the function.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeBlockingCloudFunctionError = 17105

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeRecaptchaNotEnabled](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeRecaptchaNotEnabled)

  `
  `  
  Indicates that reCAPTCHA Enterprise integration is not enabled for this project.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeRecaptchaNotEnabled = 17200

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeMissingRecaptchaToken](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingRecaptchaToken)

  `
  `  
  Indicates that the reCAPTCHA token is missing from the backend request.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeMissingRecaptchaToken = 17201

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidRecaptchaToken](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidRecaptchaToken)

  `
  `  
  Indicates that the reCAPTCHA token sent with the backend request is invalid.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidRecaptchaToken = 17202

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidRecaptchaAction](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidRecaptchaAction)

  `
  `  
  Indicates that the requested reCAPTCHA action is invalid.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidRecaptchaAction = 17203

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeMissingClientType](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingClientType)

  `
  `  
  Indicates that the client type is missing from the request.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeMissingClientType = 17204

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeMissingRecaptchaVersion](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeMissingRecaptchaVersion)

  `
  `  
  Indicates that the reCAPTCHA version is missing from the request.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeMissingRecaptchaVersion = 17205

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidRecaptchaVersion](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidRecaptchaVersion)

  `
  `  
  Indicates that the reCAPTCHA version sent to the backend is invalid.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidRecaptchaVersion = 17206

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInvalidReqType](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInvalidReqType)

  `
  `  
  Indicates that the request type sent to the backend is invalid.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInvalidReqType = 17207

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeRecaptchaSDKNotLinked](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeRecaptchaSDKNotLinked)

  `
  `  
  Indicates that the reCAPTCHA SDK is not linked to the app.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeRecaptchaSDKNotLinked = 17208

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeKeychainError](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeKeychainError)

  `
  `  
  Indicates an error occurred while attempting to access the keychain.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeKeychainError = 17995

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeInternalError](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeInternalError)

  `
  `  
  Indicates an internal error occurred.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeInternalError = 17999

- `
  ``
  ``
  `

  ### [FIRAuthErrorCodeMalformedJWT](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRAuthErrorCode#/c:@E@FIRAuthErrorCode@FIRAuthErrorCodeMalformedJWT)

  `
  `  
  Raised when a JWT fails to parse correctly. May be accompanied by an underlying error
  describing which step of the JWT parsing process failed.  

  #### Declaration

  Objective-C  

      FIRAuthErrorCodeMalformedJWT = 18000