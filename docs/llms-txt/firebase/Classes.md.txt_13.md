# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes.md.txt

# FirebaseAuth Framework Reference

# Classes

The following classes are available globally.
- `


  ### [FIRActionCodeSettings](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeSettings)


  ` Used to set and retrieve settings related to handling action codes.

  #### Declaration

  Objective-C


      @interface FIRActionCodeSettings : NSObject

- `


  ### [FIRAdditionalUserInfo](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAdditionalUserInfo)


  ` Represents additional user data returned from an identity provider.

  #### Declaration

  Objective-C


      @interface FIRAdditionalUserInfo : NSObject

- `


  ### [FIRActionCodeInfo](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeInfo)


  ` Manages information regarding action codes.

  #### Declaration

  Objective-C


      @interface FIRActionCodeInfo : NSObject

- `


  ### [FIRActionCodeURL](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeURL)


  ` This class will allow developers to easily extract information about out of band links.

  #### Declaration

  Objective-C


      @interface FIRActionCodeURL : NSObject

- `


  ### [FIRAuth](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth)


  ` Manages authentication for Firebase apps.
  This class is thread-safe.

  #### Declaration

  Objective-C


      @interface FIRAuth : NSObject

- `


  ### [FIRAuthCredential](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthCredential)


  ` Represents a credential.

  #### Declaration

  Objective-C


      @interface FIRAuthCredential : NSObject

- `


  ### [FIRAuthDataResult](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthDataResult)


  ` Helper object that contains the result of a successful sign-in, link and reauthenticate
  action. It contains references to a `User` instance and a `AdditionalUserInfo` instance.

  #### Declaration

  Objective-C


      @interface FIRAuthDataResult : NSObject

- `


  ### [FIRAuthErrors](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes#/c:objc(cs)FIRAuthErrors)


  ` Error Codes common to all API Methods:

      + `AuthErrorCodeNetworkError`
      + `AuthErrorCodeUserNotFound`
      + `AuthErrorCodeUserTokenExpired`
      + `AuthErrorCodeTooManyRequests`
      + `AuthErrorCodeInvalidAPIKey`
      + `AuthErrorCodeAppNotAuthorized`
      + `AuthErrorCodeKeychainError`
      + `AuthErrorCodeInternalError`

  Common error codes for `User` operations:

      + `AuthErrorCodeInvalidUserToken`
      + `AuthErrorCodeUserDisabled`

  #### Declaration

  Objective-C


      @interface FIRAuthErrors

- `


  ### [FIRAuthSettings](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthSettings)


  ` Determines settings related to an auth object.

  #### Declaration

  Objective-C


      @interface FIRAuthSettings : NSObject <NSCopying>

- `


  ### [FIRAuthTokenResult](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthTokenResult)


  ` A data class containing the ID token JWT string and other properties associated with the
  token including the decoded payload claims.

  #### Declaration

  Objective-C


      @interface FIRAuthTokenResult : NSObject

- `


  ### [FIREmailAuthProvider](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIREmailAuthProvider)


  ` A concrete implementation of `AuthProvider` for Email \& Password Sign In.

  #### Declaration

  Objective-C


      @interface FIREmailAuthProvider : NSObject

- `


  ### [FIRFacebookAuthProvider](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRFacebookAuthProvider)


  ` Utility class for constructing Facebook credentials.

  #### Declaration

  Objective-C


      @interface FIRFacebookAuthProvider : NSObject

- `


  ### [FIRGameCenterAuthProvider](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRGameCenterAuthProvider)


  ` A concrete implementation of `AuthProvider` for Game Center Sign In. Not available on
  watchOS.

  #### Declaration

  Objective-C


      @interface FIRGameCenterAuthProvider : NSObject

- `


  ### [FIRGitHubAuthProvider](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRGitHubAuthProvider)


  ` Utility class for constructing GitHub credentials.

  #### Declaration

  Objective-C


      @interface FIRGitHubAuthProvider : NSObject

- `


  ### [FIRGoogleAuthProvider](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRGoogleAuthProvider)


  ` Utility class for constructing Google Sign In credentials.

  #### Declaration

  Objective-C


      @interface FIRGoogleAuthProvider : NSObject

- `


  ### [FIRMultiFactor](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactor)


  ` The interface defining the multi factor related properties and operations pertaining to a
  user.
  This class is available on iOS only.

  #### Declaration

  Objective-C


      @interface FIRMultiFactor : NSObject

- `


  ### [FIRMultiFactorAssertion](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorAssertion)


  ` The base class for asserting ownership of a second factor. This is equivalent to the
  AuthCredential class.
  This class is available on iOS only.

  #### Declaration

  Objective-C


      @interface FIRMultiFactorAssertion : NSObject

- `


  ### [FIRMultiFactorInfo](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorInfo)


  ` Safe public structure used to represent a second factor entity from a client perspective.
  This class is available on iOS only.

  #### Declaration

  Objective-C


      @interface FIRMultiFactorInfo : NSObject

- `


  ### [FIRMultiFactorResolver](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorResolver)


  ` The data structure used to help developers resolve 2nd factor requirements on users that
  have opted in to 2 factor authentication.
  This class is available on iOS only.

  #### Declaration

  Objective-C


      @interface FIRMultiFactorResolver : NSObject

- `


  ### [FIRMultiFactorSession](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes#/c:objc(cs)FIRMultiFactorSession)


  ` Opaque object that identifies the current session to enroll a second factor or to
  complete sign in when previously enrolled.
  This class is available on iOS only.

  #### Declaration

  Objective-C


      @interface FIRMultiFactorSession : NSObject

- `


  ### [FIROAuthCredential](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthCredential)


  ` Internal implementation of FIRAuthCredential for generic credentials.

  #### Declaration

  Objective-C


      @interface FIROAuthCredential : https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthCredential <NSSecureCoding>

- `


  ### [FIROAuthProvider](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthProvider)


  ` A concrete implementation of `AuthProvider` for generic OAuth Providers.

  #### Declaration

  Objective-C


      @interface FIROAuthProvider : NSObject <https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRFederatedAuthProvider>

- `


  ### [FIRPhoneAuthCredential](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneAuthCredential)


  ` Implementation of FIRAuthCredential for Phone Auth credentials.
  This class is available on iOS only.

  #### Declaration

  Objective-C


      @interface FIRPhoneAuthCredential : https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthCredential <NSSecureCoding>

- `


  ### [FIRPhoneAuthProvider](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneAuthProvider)


  ` A concrete implementation of `AuthProvider` for phone auth providers.
  This class is available on iOS only.

  #### Declaration

  Objective-C


      @interface FIRPhoneAuthProvider : NSObject

- `


  ### [FIRPhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes#/c:objc(cs)FIRPhoneMultiFactorAssertion)


  ` The subclass of base class FIRMultiFactorAssertion, used to assert ownership of a phone
  second factor.
  This class is available on iOS only.

  #### Declaration

  Objective-C


      @interface FIRPhoneMultiFactorAssertion : https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorAssertion

- `


  ### [FIRPhoneMultiFactorGenerator](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneMultiFactorGenerator)


  ` The data structure used to help initialize an assertion for a second factor entity to the
  Firebase Auth/CICP server. Depending on the type of second factor, this will help generate
  the assertion.
  This class is available on iOS only.

  #### Declaration

  Objective-C


      @interface FIRPhoneMultiFactorGenerator : NSObject

- `


  ### [FIRPhoneMultiFactorInfo](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRPhoneMultiFactorInfo)


  ` Extends the MultiFactorInfo class for phone number second factors.
  The identifier of this second factor is "phone".
  This class is available on iOS only.

  #### Declaration

  Objective-C


      @interface FIRPhoneMultiFactorInfo : https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorInfo

- `


  ### [FIRTOTPMultiFactorAssertion](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes#/c:objc(cs)FIRTOTPMultiFactorAssertion)


  ` The subclass of base class MultiFactorAssertion, used to assert ownership of a TOTP
  (Time-based One Time Password) second factor.
  This class is available on iOS only.

  #### Declaration

  Objective-C


      @interface FIRTOTPMultiFactorAssertion : https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorAssertion

- `


  ### [FIRTOTPMultiFactorGenerator](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRTOTPMultiFactorGenerator)


  ` The data structure used to help initialize an assertion for a second factor entity to the
  Firebase Auth/CICP server. Depending on the type of second factor, this will help generate
  the assertion.
  This class is available on iOS only.

  #### Declaration

  Objective-C


      @interface FIRTOTPMultiFactorGenerator : NSObject

- `


  ### [FIRTOTPSecret](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRTOTPSecret)


  `

  #### Declaration

  Objective-C


      @interface FIRTOTPSecret : NSObject

- `


  ### [FIRTwitterAuthProvider](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRTwitterAuthProvider)


  ` Utility class for constructing Twitter credentials.

  #### Declaration

  Objective-C


      @interface FIRTwitterAuthProvider : NSObject

- `


  ### [FIRUser](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser)


  ` Represents a user. Firebase Auth does not attempt to validate users
  when loading them from the keychain. Invalidated users (such as those
  whose passwords have been changed on another client) are automatically
  logged out when an auth-dependent operation is attempted or when the
  ID token is automatically refreshed.
  This class is thread-safe.

  #### Declaration

  Objective-C


      @interface FIRUser : NSObject <https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRUserInfo>

- `


  ### [FIRUserProfileChangeRequest](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUserProfileChangeRequest)


  ` Represents an object capable of updating a user's profile data.
  Properties are marked as being part of a profile update when they are set. Setting a
  property value to nil is not the same as leaving the property unassigned.

  #### Declaration

  Objective-C


      @interface FIRUserProfileChangeRequest : NSObject

- `


  ### [FIRUserMetadata](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUserMetadata)


  ` A data class representing the metadata corresponding to a Firebase user.

  #### Declaration

  Objective-C


      @interface FIRUserMetadata : NSObject