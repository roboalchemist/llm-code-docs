# Source: https://firebase.google.com/docs/reference/node/firebase.auth.md.txt

# auth | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- auth

### Callable

- auth ( app ? : [App](https://firebase.google.com/docs/reference/node/firebase.app.App) ) : [Auth](https://firebase.google.com/docs/reference/node/firebase.auth.Auth)
- Gets the [`Auth`](https://firebase.google.com/docs/reference/node/firebase.auth.Auth) service for the default app or a
  given app.

  `firebase.auth()` can be called with no arguments to access the default app's
  [`Auth`](https://firebase.google.com/docs/reference/node/firebase.auth.Auth) service or as `firebase.auth(app)` to
  access the [`Auth`](https://firebase.google.com/docs/reference/node/firebase.auth.Auth) service associated with a
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

    ##### Optional app: [App](https://firebase.google.com/docs/reference/node/firebase.app.App)

  #### Returns [Auth](https://firebase.google.com/docs/reference/node/firebase.auth.Auth)

## Index

### Modules

- [ActionCodeInfo](https://firebase.google.com/docs/reference/node/firebase.auth.ActionCodeInfo)
- [Auth](https://firebase.google.com/docs/reference/node/firebase.auth.Auth)

### Classes

- [ActionCodeURL](https://firebase.google.com/docs/reference/node/firebase.auth.ActionCodeURL)
- [AuthCredential](https://firebase.google.com/docs/reference/node/firebase.auth.AuthCredential)
- [EmailAuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.EmailAuthProvider)
- [FacebookAuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.FacebookAuthProvider)
- [GithubAuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.GithubAuthProvider)
- [GoogleAuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.GoogleAuthProvider)
- [MultiFactorAssertion](https://firebase.google.com/docs/reference/node/firebase.auth.multifactorassertion)
- [MultiFactorResolver](https://firebase.google.com/docs/reference/node/firebase.auth.multifactorresolver)
- [MultiFactorSession](https://firebase.google.com/docs/reference/node/firebase.auth.multifactorsession)
- [OAuthCredential](https://firebase.google.com/docs/reference/node/firebase.auth.OAuthCredential)
- [OAuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.OAuthProvider)
- [PhoneAuthCredential](https://firebase.google.com/docs/reference/node/firebase.auth.phoneauthcredential)
- [PhoneAuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.PhoneAuthProvider)
- [PhoneMultiFactorAssertion](https://firebase.google.com/docs/reference/node/firebase.auth.phonemultifactorassertion)
- [PhoneMultiFactorGenerator](https://firebase.google.com/docs/reference/node/firebase.auth.phonemultifactorgenerator)
- [SAMLAuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.SAMLAuthProvider)
- [TwitterAuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.TwitterAuthProvider)

### Interfaces

- [ApplicationVerifier](https://firebase.google.com/docs/reference/node/firebase.auth.ApplicationVerifier)
- [AuthError](https://firebase.google.com/docs/reference/node/firebase.auth.AuthError)
- [AuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.AuthProvider)
- [AuthSettings](https://firebase.google.com/docs/reference/node/firebase.auth.AuthSettings)
- [Config](https://firebase.google.com/docs/reference/node/firebase.auth.Config)
- [ConfirmationResult](https://firebase.google.com/docs/reference/node/firebase.auth.ConfirmationResult)
- [EmulatorConfig](https://firebase.google.com/docs/reference/node/firebase.auth.EmulatorConfig)
- [Error](https://firebase.google.com/docs/reference/node/firebase.auth.Error)
- [IdTokenResult](https://firebase.google.com/docs/reference/node/firebase.auth.IDTokenResult)
- [MultiFactorError](https://firebase.google.com/docs/reference/node/firebase.auth.multifactorerror)
- [MultiFactorInfo](https://firebase.google.com/docs/reference/node/firebase.auth.multifactorinfo)
- [OAuthCredentialOptions](https://firebase.google.com/docs/reference/node/firebase.auth.OAuthCredentialOptions)
- [PhoneMultiFactorEnrollInfoOptions](https://firebase.google.com/docs/reference/node/firebase.auth.phonemultifactorenrollinfooptions)
- [PhoneMultiFactorInfo](https://firebase.google.com/docs/reference/node/firebase.auth.phonemultifactorinfo)
- [PhoneMultiFactorSignInInfoOptions](https://firebase.google.com/docs/reference/node/firebase.auth.phonemultifactorsignininfooptions)
- [PhoneSingleFactorInfoOptions](https://firebase.google.com/docs/reference/node/firebase.auth.phonesinglefactorinfooptions)
- [UserMetadata](https://firebase.google.com/docs/reference/node/firebase.auth.UserMetadata)

### Type aliases

- [ActionCodeSettings](https://firebase.google.com/docs/reference/node/firebase.auth#actioncodesettings)
- [AdditionalUserInfo](https://firebase.google.com/docs/reference/node/firebase.auth#additionaluserinfo)
- [PhoneInfoOptions](https://firebase.google.com/docs/reference/node/firebase.auth#phoneinfooptions)
- [UserCredential](https://firebase.google.com/docs/reference/node/firebase.auth#usercredential)

## Type aliases

### ActionCodeSettings

ActionCodeSettings: { android?: { installApp?: boolean; minimumVersion?: string; packageName: string }; dynamicLinkDomain?: string; handleCodeInApp?: boolean; iOS?: { bundleId: string }; url: string } This is the interface that defines the required continue/state URL with
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

AdditionalUserInfo: { isNewUser: boolean; profile: Object \| null; providerId: string; username?: string \| null } A structure containing additional user information from a federated identity
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

PhoneInfoOptions: [PhoneSingleFactorInfoOptions](https://firebase.google.com/docs/reference/node/firebase.auth.phonesinglefactorinfooptions) \| [PhoneMultiFactorEnrollInfoOptions](https://firebase.google.com/docs/reference/node/firebase.auth.phonemultifactorenrollinfooptions) \| [PhoneMultiFactorSignInInfoOptions](https://firebase.google.com/docs/reference/node/firebase.auth.phonemultifactorsignininfooptions) The information required to verify the ownership of a phone number. The
information that's required depends on whether you are doing single-factor
sign-in, multi-factor enrollment or multi-factor sign-in.

### UserCredential

UserCredential: { additionalUserInfo?: [AdditionalUserInfo](https://firebase.google.com/docs/reference/node/firebase.auth#additionaluserinfo) \| null; credential: [AuthCredential](https://firebase.google.com/docs/reference/node/firebase.auth.AuthCredential) \| null; operationType?: string \| null; user: [User](https://firebase.google.com/docs/reference/node/firebase.User) \| null } A structure containing a User, an AuthCredential, the operationType, and
any additional user information that was returned from the identity provider.
operationType could be 'signIn' for a sign-in operation, 'link' for a linking
operation and 'reauthenticate' for a reauthentication operation.

#### Type declaration

-

  ##### Optional additionalUserInfo?: [AdditionalUserInfo](https://firebase.google.com/docs/reference/node/firebase.auth#additionaluserinfo) \| null

-

  ##### credential: [AuthCredential](https://firebase.google.com/docs/reference/node/firebase.auth.AuthCredential) \| null

-

  ##### Optional operationType?: string \| null

-

  ##### user: [User](https://firebase.google.com/docs/reference/node/firebase.User) \| null