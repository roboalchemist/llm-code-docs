# Source: https://firebase.google.com/docs/reference/node/firebase.auth.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.md.txt

# auth | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- auth

### Callable

- auth ( app ? : [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App) ) : [Auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth)
- Gets the [`Auth`](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth) service for the default app or a
  given app.

  `firebase.auth()` can be called with no arguments to access the default app's
  [`Auth`](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth) service or as `firebase.auth(app)` to
  access the [`Auth`](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth) service associated with a
  specific app.

  example
  :


          // Get the Auth service for the default app
          var defaultAuth = firebase.auth();


  example
  :


          // Get the Auth service for a given app
          var otherAuth = firebase.auth(otherApp);


  #### Parameters

  -

    ##### Optional app: [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)

  #### Returns [Auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth)

## Index

### Modules

- [ActionCodeInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo)
- [Auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth)

### Classes

- [ActionCodeURL](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeURL)
- [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential)
- [EmailAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider)
- [FacebookAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.FacebookAuthProvider)
- [GithubAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.GithubAuthProvider)
- [GoogleAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.GoogleAuthProvider)
- [MultiFactorAssertion](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorAssertion)
- [MultiFactorResolver](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorResolver)
- [MultiFactorSession](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorSession)
- [OAuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthCredential)
- [OAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthProvider)
- [PhoneAuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthCredential)
- [PhoneAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthProvider)
- [PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorAssertion)
- [PhoneMultiFactorGenerator](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorGenerator)
- [RecaptchaVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier)
- [SAMLAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.SAMLAuthProvider)
- [TwitterAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.TwitterAuthProvider)

### Interfaces

- [ApplicationVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ApplicationVerifier)
- [AuthError](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthError)
- [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)
- [AuthSettings](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthSettings)
- [Config](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Config)
- [ConfirmationResult](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ConfirmationResult)
- [EmulatorConfig](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmulatorConfig)
- [Error](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Error)
- [IdTokenResult](https://firebase.google.com/docs/reference/js/v8/firebase.auth.IDTokenResult)
- [MultiFactorError](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorError)
- [MultiFactorInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorInfo)
- [OAuthCredentialOptions](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthCredentialOptions)
- [PhoneMultiFactorEnrollInfoOptions](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorEnrollInfoOptions)
- [PhoneMultiFactorInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorInfo)
- [PhoneMultiFactorSignInInfoOptions](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorSignInInfoOptions)
- [PhoneSingleFactorInfoOptions](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneSingleFactorInfoOptions)
- [UserMetadata](https://firebase.google.com/docs/reference/js/v8/firebase.auth.UserMetadata)

### Type aliases

- [ActionCodeSettings](https://firebase.google.com/docs/reference/js/v8/firebase.auth#actioncodesettings)
- [AdditionalUserInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth#additionaluserinfo)
- [PhoneInfoOptions](https://firebase.google.com/docs/reference/js/v8/firebase.auth#phoneinfooptions)
- [UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential)

## Type aliases

### ActionCodeSettings

ActionCodeSettings: { android?: { installApp?: boolean; minimumVersion?: string; packageName: string }; dynamicLinkDomain?: string; handleCodeInApp?: boolean; iOS?: { bundleId: string }; url: string }  
This is the interface that defines the required continue/state URL with
optional Android and iOS bundle identifiers.
The action code setting fields are:

- url: Sets the link continue/state URL, which has different meanings
  in different contexts:

  - When the link is handled in the web action widgets, this is the deep link in the continueUrl query parameter.
  - When the link is handled in the app directly, this is the continueUrl query parameter in the deep link of the Dynamic Link.
- iOS: Sets the iOS bundle ID. This will try to open the link in an iOS app if it is installed.
- android: Sets the Android package name. This will try to open the link in an android app if it is installed. If installApp is passed, it specifies whether to install the Android app if the device supports it and the app is not already installed. If this field is provided without a packageName, an error is thrown explaining that the packageName must be provided in conjunction with this field. If minimumVersion is specified, and an older version of the app is installed, the user is taken to the Play Store to upgrade the app.
- handleCodeInApp: The default is false. When set to true, the action code link will be be sent as a Universal Link or Android App Link and will be opened by the app if installed. In the false case, the code will be sent to the web widget first and then on continue will redirect to the app if installed.  

#### Type declaration

-

  ##### Optional android?: { installApp?: boolean; minimumVersion?: string; packageName: string }

  -

    ##### Optional installApp?: boolean

  -

    ##### Optional minimumVersion?: string

  -

    ##### packageName: string

-

  ##### Optional dynamicLinkDomain?: string

-

  ##### Optional handleCodeInApp?: boolean

-

  ##### Optional iOS?: { bundleId: string }

  -

    ##### bundleId: string

-

  ##### url: string

### AdditionalUserInfo

AdditionalUserInfo: { isNewUser: boolean; profile: Object \| null; providerId: string; username?: string \| null }  
A structure containing additional user information from a federated identity
provider.  

#### Type declaration

-

  ##### isNewUser: boolean

-

  ##### profile: Object \| null

-

  ##### providerId: string

-

  ##### Optional username?: string \| null

### PhoneInfoOptions

PhoneInfoOptions: [PhoneSingleFactorInfoOptions](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneSingleFactorInfoOptions) \| [PhoneMultiFactorEnrollInfoOptions](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorEnrollInfoOptions) \| [PhoneMultiFactorSignInInfoOptions](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorSignInInfoOptions)  
The information required to verify the ownership of a phone number. The
information that's required depends on whether you are doing single-factor
sign-in, multi-factor enrollment or multi-factor sign-in.

### UserCredential

UserCredential: { additionalUserInfo?: [AdditionalUserInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth#additionaluserinfo) \| null; credential: [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential) \| null; operationType?: string \| null; user: [User](https://firebase.google.com/docs/reference/js/v8/firebase.User) \| null }  
A structure containing a User, an AuthCredential, the operationType, and
any additional user information that was returned from the identity provider.
operationType could be 'signIn' for a sign-in operation, 'link' for a linking
operation and 'reauthenticate' for a reauthentication operation.  

#### Type declaration

-

  ##### Optional additionalUserInfo?: [AdditionalUserInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth#additionaluserinfo) \| null

-

  ##### credential: [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential) \| null

-

  ##### Optional operationType?: string \| null

-

  ##### user: [User](https://firebase.google.com/docs/reference/js/v8/firebase.User) \| null