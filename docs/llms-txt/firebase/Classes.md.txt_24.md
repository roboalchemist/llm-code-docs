# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes.md.txt

# FirebaseAuth Framework Reference

# Classes

The following classes are available globally.
- `


  ### [ActionCodeInfo](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeInfo)


  ` Manages information regarding action codes.

  #### Declaration

  Swift

      @objc(FIRActionCodeInfo)
      open class ActionCodeInfo : NSObject, @unchecked Sendable

- `


  ### [ActionCodeSettings](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings)


  ` Used to set and retrieve settings related to handling action codes.

  #### Declaration

  Swift

      @objc(FIRActionCodeSettings)
      open class ActionCodeSettings: NSObject,
        @unchecked Sendable

- `


  ### [ActionCodeURL](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeURL)


  ` This class will allow developers to easily extract information about out of band links.

  #### Declaration

  Swift

      @objc(FIRActionCodeURL)
      open class ActionCodeURL : NSObject, @unchecked Sendable

- `


  ### [Auth](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/Auth)


  ` Manages authentication for Firebase apps.

  This class is thread-safe.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @preconcurrency
      @objc(FIRAuth)
      open class Auth : NSObject

      extension Auth: UISceneDelegate

      extension Auth: UIApplicationDelegate

      extension Auth: AuthInterop

- `


  ### [AuthDataResult](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthDataResult)


  ` Helper object that contains the result of a successful sign-in, link and reauthenticate
  action.

  It contains references to a `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User` instance and an `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AdditionalUserInfo` instance.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRAuthDataResult)
      open class AuthDataResult : NSObject

      extension AuthDataResult: NSSecureCoding

- `


  ### [AuthSettings](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthSettings)


  ` Determines settings related to an auth object.

  #### Declaration

  Swift

      @objc(FIRAuthSettings)
      open class AuthSettings : NSObject, NSCopying

- `


  ### [AuthTokenResult](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthTokenResult)


  ` A data class containing the ID token JWT string and other properties associated with the
  token including the decoded payload claims.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRAuthTokenResult)
      open class AuthTokenResult : NSObject

      extension AuthTokenResult: NSSecureCoding

- `


  ### [AuthCredential](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential)


  ` Public representation of a credential.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRAuthCredential)
      open class AuthCredential : NSObject, @unchecked Sendable

- `


  ### [EmailAuthProvider](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/EmailAuthProvider)


  ` A concrete implementation of `AuthProvider` for Email \& Password Sign In.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIREmailAuthProvider)
      open class EmailAuthProvider : NSObject

- `


  ### [FacebookAuthProvider](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/FacebookAuthProvider)


  ` Utility class for constructing Facebook Sign In credentials.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRFacebookAuthProvider)
      open class FacebookAuthProvider : NSObject

- `


  ### [GameCenterAuthProvider](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/GameCenterAuthProvider)


  ` A concrete implementation of `AuthProvider` for Game Center Sign In. Not available on watchOS.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRGameCenterAuthProvider)
      open class GameCenterAuthProvider : NSObject

- `


  ### [GitHubAuthProvider](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/GitHubAuthProvider)


  ` Utility class for constructing GitHub Sign In credentials.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRGitHubAuthProvider)
      open class GitHubAuthProvider : NSObject

- `


  ### [GoogleAuthProvider](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/GoogleAuthProvider)


  ` Utility class for constructing Google Sign In credentials.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRGoogleAuthProvider)
      open class GoogleAuthProvider : NSObject

- `


  ### [OAuthCredential](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthCredential)


  ` Internal implementation of `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential` for generic credentials.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIROAuthCredential)
      open class OAuthCredential: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential, NSSecureCoding,
        @unchecked Sendable

- `


  ### [OAuthProvider](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthProvider)


  ` Utility class for constructing OAuth Sign In credentials.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIROAuthProvider)
      open class OAuthProvider : NSObject, https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/FederatedAuthProvider

- `


  ### [PhoneAuthCredential](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneAuthCredential)


  ` Implementation of AuthCredential for Phone Auth credentials.

  This class is available on iOS only.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRPhoneAuthCredential)
      open class PhoneAuthCredential: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthCredential, NSSecureCoding,
        @unchecked Sendable

- `


  ### [PhoneAuthProvider](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneAuthProvider)


  ` A concrete implementation of `AuthProvider` for phone auth providers.

  This class is available on iOS only.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRPhoneAuthProvider)
      open class PhoneAuthProvider : NSObject, @unchecked Sendable

- `


  ### [TwitterAuthProvider](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/TwitterAuthProvider)


  ` Utility class for constructing Twitter Sign In credentials.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRTwitterAuthProvider)
      open class TwitterAuthProvider : NSObject

- `


  ### [MultiFactor](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactor)


  ` The interface defining the multi factor related properties and operations pertaining to a
  user.

  This class is available on iOS and macOS.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRMultiFactor)
      open class MultiFactor : NSObject

      extension MultiFactor: NSSecureCoding

- `


  ### [MultiFactorAssertion](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorAssertion)


  ` The base class for asserting ownership of a second factor. This is equivalent to the
  AuthCredential class.

  This class is available on iOS and macOS.

  #### Declaration

  Swift

      @objc(FIRMultiFactorAssertion)
      open class MultiFactorAssertion : NSObject

- `


  ### [MultiFactorInfo](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorInfo)


  ` Safe public structure used to represent a second factor entity from a client perspective.

  This class is available on iOS and macOS.

  #### Declaration

  Swift

      @objc(FIRMultiFactorInfo)
      open class MultiFactorInfo : NSObject, @unchecked Sendable

      extension MultiFactorInfo: NSSecureCoding

- `


  ### [MultiFactorResolver](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorResolver)


  ` The subclass of base class `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorAssertion`, used to assert ownership of a phone
  second factor.

  This class is available on iOS and macOS.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRMultiFactorResolver)
      open class MultiFactorResolver : NSObject

- `


  ### [MultiFactorSession](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes#/c:@M@FirebaseAuth@objc(cs)FIRMultiFactorSession)


  ` Opaque object that identifies the current session to enroll a second factor or to
  complete sign in when previously enrolled.

  Identifies the current session to enroll a second factor
  or to complete sign in when previously enrolled. It contains additional context on the
  existing user, notably the confirmation that the user passed the first factor challenge.

  This class is available on iOS and macOS.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRMultiFactorSession)
      open class MultiFactorSession : NSObject

- `


  ### [PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes#/c:@M@FirebaseAuth@objc(cs)FIRPhoneMultiFactorAssertion)


  ` The subclass of base class FIRMultiFactorAssertion, used to assert ownership of a phone
  second factor.

  This class is available on iOS and macOS.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRPhoneMultiFactorAssertion)
      open class PhoneMultiFactorAssertion : https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorAssertion

- `


  ### [PhoneMultiFactorGenerator](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneMultiFactorGenerator)


  ` The data structure used to help initialize an assertion for a second factor entity to the
  Firebase Auth/CICP server.

  Depending on the type of second factor, this will help generate the assertion.

  This class is available on iOS and macOS.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRPhoneMultiFactorGenerator)
      open class PhoneMultiFactorGenerator : NSObject

- `


  ### [PhoneMultiFactorInfo](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneMultiFactorInfo)


  ` Extends the MultiFactorInfo class for phone number second factors.

  The identifier of this second factor is "phone".

  This class is available on iOS and macOS.

  #### Declaration

  Swift

      @objc(FIRPhoneMultiFactorInfo)
      open class PhoneMultiFactorInfo: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorInfo,
        @unchecked Sendable

- `


  ### [TOTPMultiFactorAssertion](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes#/c:@M@FirebaseAuth@objc(cs)FIRTOTPMultiFactorAssertion)


  ` The subclass of base class MultiFactorAssertion, used to assert ownership of a TOTP
  (Time-based One Time Password) second factor.

  This class is available on iOS and macOS.

  #### Declaration

  Swift

      @objc(FIRTOTPMultiFactorAssertion)
      open class TOTPMultiFactorAssertion : https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorAssertion

- `


  ### [TOTPMultiFactorGenerator](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/TOTPMultiFactorGenerator)


  ` The data structure used to help initialize an assertion for a second factor entity to the
  Firebase Auth/CICP server. Depending on the type of second factor, this will help generate
  the assertion.

  This class is available on iOS and macOS.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRTOTPMultiFactorGenerator)
      open class TOTPMultiFactorGenerator : NSObject

- `


  ### [TOTPSecret](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/TOTPSecret)


  ` The subclass of base class MultiFactorAssertion, used to assert ownership of a TOTP
  (Time-based One Time Password) second factor.

  This class is available on iOS and macOS.

  #### Declaration

  Swift

      @objc(FIRTOTPSecret)
      open class TOTPSecret : NSObject

- `


  ### [AdditionalUserInfo](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AdditionalUserInfo)


  ` Undocumented

  #### Declaration

  Swift

      @objc(FIRAdditionalUserInfo)
      open class AdditionalUserInfo : NSObject

      extension AdditionalUserInfo: NSSecureCoding

- `


  ### [User](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User)


  ` Represents a user.

  Firebase Auth does not attempt to validate users
  when loading them from the keychain. Invalidated users (such as those
  whose passwords have been changed on another client) are automatically
  logged out when an auth-dependent operation is attempted or when the
  ID token is automatically refreshed.

  This class is thread-safe.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRUser)
      open class User : NSObject, https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/UserInfo

      extension User: NSSecureCoding

- `


  ### [UserMetadata](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/UserMetadata)


  ` A data class representing the metadata corresponding to a Firebase user.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRUserMetadata)
      open class UserMetadata : NSObject

      extension UserMetadata: NSSecureCoding

- `


  ### [UserProfileChangeRequest](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/UserProfileChangeRequest)


  ` Represents an object capable of updating a user's profile data.

  Properties are marked as being part of a profile update when they are set. Setting a
  property value to nil is not the same as leaving the property unassigned.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRUserProfileChangeRequest)
      open class UserProfileChangeRequest : NSObject

- `


  ### [AuthErrors](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AuthErrors)


  ` Error Codes common to all API Methods:

  #### Declaration

  Swift

      @objc(FIRAuthErrors)
      open class AuthErrors : NSObject