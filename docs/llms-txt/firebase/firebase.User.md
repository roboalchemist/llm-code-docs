# Source: https://firebase.google.com/docs/reference/node/firebase.User.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.User.md.txt

# User | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- User

A user account.

## Index

### Interfaces

- [MultiFactorUser](https://firebase.google.com/docs/reference/js/v8/firebase.user.MultiFactorUser)

### Properties

- [displayName](https://firebase.google.com/docs/reference/js/v8/firebase.User#displayname)
- [email](https://firebase.google.com/docs/reference/js/v8/firebase.User#email)
- [emailVerified](https://firebase.google.com/docs/reference/js/v8/firebase.User#emailverified)
- [isAnonymous](https://firebase.google.com/docs/reference/js/v8/firebase.User#isanonymous)
- [metadata](https://firebase.google.com/docs/reference/js/v8/firebase.User#metadata)
- [multiFactor](https://firebase.google.com/docs/reference/js/v8/firebase.User#multifactor)
- [phoneNumber](https://firebase.google.com/docs/reference/js/v8/firebase.User#phonenumber)
- [photoURL](https://firebase.google.com/docs/reference/js/v8/firebase.User#photourl)
- [providerData](https://firebase.google.com/docs/reference/js/v8/firebase.User#providerdata)
- [providerId](https://firebase.google.com/docs/reference/js/v8/firebase.User#providerid)
- [refreshToken](https://firebase.google.com/docs/reference/js/v8/firebase.User#refreshtoken)
- [tenantId](https://firebase.google.com/docs/reference/js/v8/firebase.User#tenantid)
- [uid](https://firebase.google.com/docs/reference/js/v8/firebase.User#uid)

### Methods

- [delete](https://firebase.google.com/docs/reference/js/v8/firebase.User#delete)
- [getIdToken](https://firebase.google.com/docs/reference/js/v8/firebase.User#getidtoken)
- [getIdTokenResult](https://firebase.google.com/docs/reference/js/v8/firebase.User#getidtokenresult)
- [linkAndRetrieveDataWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#linkandretrievedatawithcredential)
- [linkWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#linkwithcredential)
- [linkWithPhoneNumber](https://firebase.google.com/docs/reference/js/v8/firebase.User#linkwithphonenumber)
- [linkWithPopup](https://firebase.google.com/docs/reference/js/v8/firebase.User#linkwithpopup)
- [linkWithRedirect](https://firebase.google.com/docs/reference/js/v8/firebase.User#linkwithredirect)
- [reauthenticateAndRetrieveDataWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#reauthenticateandretrievedatawithcredential)
- [reauthenticateWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#reauthenticatewithcredential)
- [reauthenticateWithPhoneNumber](https://firebase.google.com/docs/reference/js/v8/firebase.User#reauthenticatewithphonenumber)
- [reauthenticateWithPopup](https://firebase.google.com/docs/reference/js/v8/firebase.User#reauthenticatewithpopup)
- [reauthenticateWithRedirect](https://firebase.google.com/docs/reference/js/v8/firebase.User#reauthenticatewithredirect)
- [reload](https://firebase.google.com/docs/reference/js/v8/firebase.User#reload)
- [sendEmailVerification](https://firebase.google.com/docs/reference/js/v8/firebase.User#sendemailverification)
- [toJSON](https://firebase.google.com/docs/reference/js/v8/firebase.User#tojson)
- [unlink](https://firebase.google.com/docs/reference/js/v8/firebase.User#unlink)
- [updateEmail](https://firebase.google.com/docs/reference/js/v8/firebase.User#updateemail)
- [updatePassword](https://firebase.google.com/docs/reference/js/v8/firebase.User#updatepassword)
- [updatePhoneNumber](https://firebase.google.com/docs/reference/js/v8/firebase.User#updatephonenumber)
- [updateProfile](https://firebase.google.com/docs/reference/js/v8/firebase.User#updateprofile)
- [verifyBeforeUpdateEmail](https://firebase.google.com/docs/reference/js/v8/firebase.User#verifybeforeupdateemail)

## Properties

### displayName

displayName: string \| null
| Inherited from [User](https://firebase.google.com/docs/reference/js/v8/firebase.User).[displayName](https://firebase.google.com/docs/reference/js/v8/firebase.User#displayname)

### email

email: string \| null
| Inherited from [User](https://firebase.google.com/docs/reference/js/v8/firebase.User).[email](https://firebase.google.com/docs/reference/js/v8/firebase.User#email)

### emailVerified

emailVerified: boolean

### isAnonymous

isAnonymous: boolean

### metadata

metadata: [UserMetadata](https://firebase.google.com/docs/reference/js/v8/firebase.auth.UserMetadata)

### multiFactor

multiFactor: [MultiFactorUser](https://firebase.google.com/docs/reference/js/v8/firebase.user.MultiFactorUser)  
The [firebase.User.MultiFactorUser](https://firebase.google.com/docs/reference/js/v8/firebase.user.MultiFactorUser) object corresponding to the current user.
This is used to access all multi-factor properties and operations related to the
current user.

### phoneNumber

phoneNumber: string \| null
Overrides [UserInfo](https://firebase.google.com/docs/reference/js/v8/firebase.UserInfo).[phoneNumber](https://firebase.google.com/docs/reference/js/v8/firebase.UserInfo#phonenumber)  
The phone number normalized based on the E.164 standard (e.g. +16505550101)
for the current user. This is null if the user has no phone credential linked
to the account.

### photoURL

photoURL: string \| null
| Inherited from [User](https://firebase.google.com/docs/reference/js/v8/firebase.User).[photoURL](https://firebase.google.com/docs/reference/js/v8/firebase.User#photourl)

### providerData

providerData: [UserInfo](https://firebase.google.com/docs/reference/js/v8/firebase.UserInfo)\[\]

### providerId

providerId: string
| Inherited from [User](https://firebase.google.com/docs/reference/js/v8/firebase.User).[providerId](https://firebase.google.com/docs/reference/js/v8/firebase.User#providerid)

### refreshToken

refreshToken: string

### tenantId

tenantId: string \| null  
The current user's tenant ID. This is a read-only property, which indicates
the tenant ID used to sign in the current user. This is null if the user is
signed in from the parent project.

example
:

        // Set the tenant ID on Auth instance.
        firebase.auth().tenantId = 'TENANT_PROJECT_ID';

        // All future sign-in request now include tenant ID.
        firebase.auth().signInWithEmailAndPassword(email, password)
          .then(function(result) {
            // result.user.tenantId should be 'TENANT_PROJECT_ID'.
          }).catch(function(error) {
            // Handle error.
          });


### uid

uid: string
Inherited from [User](https://firebase.google.com/docs/reference/js/v8/firebase.User).[uid](https://firebase.google.com/docs/reference/js/v8/firebase.User#uid)  
The user's unique ID.

## Methods

### delete

- delete ( ) : Promise \< void \>
- Deletes and signs out the user.

  **Important:** this is a security-sensitive operation that requires the
  user to have recently signed in. If this requirement isn't met, ask the user
  to authenticate again and then call
  [firebase.User.reauthenticateWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#reauthenticatewithcredential).

  #### Error Codes

  auth/requires-recent-login
  :   Thrown if the user's last sign-in time does not meet the security
      threshold. Use [firebase.User.reauthenticateWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#reauthenticatewithcredential) to
      resolve. This does not apply if the user is anonymous.

  #### Returns Promise\<void\>

### getIdToken

- getIdToken ( forceRefresh ? : boolean ) : Promise \< string \>
- Returns a JSON Web Token (JWT) used to identify the user to a Firebase
  service.

  Returns the current token if it has not expired. Otherwise, this will
  refresh the token and return a new one.

  #### Parameters

  -

    ##### Optional forceRefresh: boolean

    Force refresh regardless of token
    expiration.

  #### Returns Promise\<string\>

### getIdTokenResult

- getIdTokenResult ( forceRefresh ? : boolean ) : Promise \< [IdTokenResult](https://firebase.google.com/docs/reference/js/v8/firebase.auth.IDTokenResult) \>
-

  #### Parameters

  -

    ##### Optional forceRefresh: boolean

  #### Returns Promise\<[IdTokenResult](https://firebase.google.com/docs/reference/js/v8/firebase.auth.IDTokenResult)\>

### linkAndRetrieveDataWithCredential

- linkAndRetrieveDataWithCredential ( credential : [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential) ) : Promise \< [UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential) \>
-

  deprecated

  :   This method is deprecated. Use
      [firebase.User.linkWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#linkwithcredential) instead.

  Links the user account with the given credentials and returns any available
  additional user information, such as user name.

  #### Error Codes

  auth/provider-already-linked
  :   Thrown if the provider has already been linked to the user. This error is
      thrown even if this is not the same provider's account that is currently
      linked to the user.

  auth/invalid-credential
  :   Thrown if the provider's credential is not valid. This can happen if it
      has already expired when calling link, or if it used invalid token(s).
      See the Firebase documentation for your provider, and make sure you pass
      in the correct parameters to the credential method.

  auth/credential-already-in-use
  :   Thrown if the account corresponding to the credential already exists
      among your users, or is already linked to a Firebase User.
      For example, this error could be thrown if you are upgrading an anonymous
      user to a Google user by linking a Google credential to it and the Google
      credential used is already associated with an existing Firebase Google
      user.
      The fields `error.email`, `error.phoneNumber`, and
      `error.credential` ([firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential))
      may be provided, depending on the type of credential. You can recover
      from this error by signing in with `error.credential` directly
      via [firebase.auth.Auth.signInWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signinwithcredential).

  auth/email-already-in-use
  :   Thrown if the email corresponding to the credential already exists
      among your users. When thrown while linking a credential to an existing
      user, an `error.email` and `error.credential`
      ([firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential)) fields are also provided.
      You have to link the credential to the existing user with that email if
      you wish to continue signing in with that credential. To do so, call
      [firebase.auth.Auth.fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#fetchsigninmethodsforemail), sign in to
      `error.email` via one of the providers returned and then
      [firebase.User.linkWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#linkwithcredential) the original credential to that
      newly signed in user.

  auth/operation-not-allowed
  :   Thrown if you have not enabled the provider in the Firebase Console. Go
      to the Firebase Console for your project, in the Auth section and the
      **Sign in Method** tab and configure the provider.

  auth/invalid-email
  :   Thrown if the email used in a
      [firebase.auth.EmailAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider#credential) is invalid.

  auth/wrong-password
  :   Thrown if the password used in a
      [firebase.auth.EmailAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider#credential) is not correct or
      when the user associated with the email does not have a password.

  auth/invalid-verification-code
  :   Thrown if the credential is a
      [firebase.auth.PhoneAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthProvider#credential) and the verification
      code of the credential is not valid.

  auth/invalid-verification-id
  :   Thrown if the credential is a
      [firebase.auth.PhoneAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthProvider#credential) and the verification
      ID of the credential is not valid.

  #### Parameters

  -

    ##### credential: [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential)

    The auth credential.

  #### Returns Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential)\>

### linkWithCredential

- linkWithCredential ( credential : [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential) ) : Promise \< [UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential) \>
- Links the user account with the given credentials.

  #### Error Codes

  auth/provider-already-linked
  :   Thrown if the provider has already been linked to the user. This error is
      thrown even if this is not the same provider's account that is currently
      linked to the user.

  auth/invalid-credential
  :   Thrown if the provider's credential is not valid. This can happen if it
      has already expired when calling link, or if it used invalid token(s).
      See the Firebase documentation for your provider, and make sure you pass
      in the correct parameters to the credential method.

  auth/credential-already-in-use
  :   Thrown if the account corresponding to the credential already exists
      among your users, or is already linked to a Firebase User.
      For example, this error could be thrown if you are upgrading an anonymous
      user to a Google user by linking a Google credential to it and the Google
      credential used is already associated with an existing Firebase Google
      user.
      The fields `error.email`, `error.phoneNumber`, and
      `error.credential` ([firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential))
      may be provided, depending on the type of credential. You can recover
      from this error by signing in with `error.credential` directly
      via [firebase.auth.Auth.signInWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signinwithcredential).

  auth/email-already-in-use
  :   Thrown if the email corresponding to the credential already exists
      among your users. When thrown while linking a credential to an existing
      user, an `error.email` and `error.credential`
      ([firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential)) fields are also provided.
      You have to link the credential to the existing user with that email if
      you wish to continue signing in with that credential. To do so, call
      [firebase.auth.Auth.fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#fetchsigninmethodsforemail), sign in to
      `error.email` via one of the providers returned and then
      [firebase.User.linkWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#linkwithcredential) the original credential to that
      newly signed in user.

  auth/operation-not-allowed
  :   Thrown if you have not enabled the provider in the Firebase Console. Go
      to the Firebase Console for your project, in the Auth section and the
      **Sign in Method** tab and configure the provider.

  auth/invalid-email
  :   Thrown if the email used in a
      [firebase.auth.EmailAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider#credential) is invalid.

  auth/wrong-password
  :   Thrown if the password used in a
      [firebase.auth.EmailAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider#credential) is not correct or
      when the user associated with the email does not have a password.

  auth/invalid-verification-code
  :   Thrown if the credential is a
      [firebase.auth.PhoneAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthProvider#credential) and the verification
      code of the credential is not valid.

  auth/invalid-verification-id
  :   Thrown if the credential is a
      [firebase.auth.PhoneAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthProvider#credential) and the verification
      ID of the credential is not valid.

  #### Parameters

  -

    ##### credential: [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential)

    The auth credential.

  #### Returns Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential)\>

### linkWithPhoneNumber

- linkWithPhoneNumber ( phoneNumber : string , applicationVerifier : [ApplicationVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ApplicationVerifier) ) : Promise \< [ConfirmationResult](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ConfirmationResult) \>
- Links the user account with the given phone number.

  #### Error Codes

  auth/provider-already-linked
  :   Thrown if the provider has already been linked to the user. This error is
      thrown even if this is not the same provider's account that is currently
      linked to the user.

  auth/captcha-check-failed
  :   Thrown if the reCAPTCHA response token was invalid, expired, or if
      this method was called from a non-whitelisted domain.

  auth/invalid-phone-number
  :   Thrown if the phone number has an invalid format.

  auth/missing-phone-number
  :   Thrown if the phone number is missing.

  auth/quota-exceeded
  :   Thrown if the SMS quota for the Firebase project has been exceeded.

  auth/user-disabled
  :   Thrown if the user corresponding to the given phone number has been
      disabled.

  auth/credential-already-in-use
  :   Thrown if the account corresponding to the phone number already exists
      among your users, or is already linked to a Firebase User.
      The fields `error.phoneNumber` and
      `error.credential` ([firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential))
      are provided in this case. You can recover from this error by signing in
      with that credential directly via
      [firebase.auth.Auth.signInWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signinwithcredential).

  auth/operation-not-allowed
  :   Thrown if you have not enabled the phone authentication provider in the
      Firebase Console. Go to the Firebase Console for your project, in the
      Auth section and the **Sign in Method** tab and configure
      the provider.

  #### Parameters

  -

    ##### phoneNumber: string

    The user's phone number in E.164 format (e.g.
    +16505550101).
  -

    ##### applicationVerifier: [ApplicationVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ApplicationVerifier)

  #### Returns Promise\<[ConfirmationResult](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ConfirmationResult)\>

### linkWithPopup

- linkWithPopup ( provider : [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider) ) : Promise \< [UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential) \>
- Links the authenticated provider to the user account using a pop-up based
  OAuth flow.

  If the linking is successful, the returned result will contain the user
  and the provider's credential.

  #### Error Codes

  auth/auth-domain-config-required
  :   Thrown if authDomain configuration is not provided when calling
      firebase.initializeApp(). Check Firebase Console for instructions on
      determining and passing that field.

  auth/cancelled-popup-request
  :   Thrown if successive popup operations are triggered. Only one popup
      request is allowed at one time on a user or an auth instance. All the
      popups would fail with this error except for the last one.

  auth/credential-already-in-use
  :   Thrown if the account corresponding to the credential already exists
      among your users, or is already linked to a Firebase User.
      For example, this error could be thrown if you are upgrading an anonymous
      user to a Google user by linking a Google credential to it and the Google
      credential used is already associated with an existing Firebase Google
      user.
      An `error.email` and `error.credential`
      ([firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential)) fields are also provided. You can
      recover from this error by signing in with that credential directly via
      [firebase.auth.Auth.signInWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signinwithcredential).

  auth/email-already-in-use
  :   Thrown if the email corresponding to the credential already exists
      among your users. When thrown while linking a credential to an existing
      user, an `error.email` and `error.credential`
      ([firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential)) fields are also provided.
      You have to link the credential to the existing user with that email if
      you wish to continue signing in with that credential. To do so, call
      [firebase.auth.Auth.fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#fetchsigninmethodsforemail), sign in to
      `error.email` via one of the providers returned and then
      [firebase.User.linkWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#linkwithcredential) the original credential to that
      newly signed in user.

  auth/operation-not-allowed
  :   Thrown if you have not enabled the provider in the Firebase Console. Go
      to the Firebase Console for your project, in the Auth section and the
      **Sign in Method** tab and configure the provider.

  auth/popup-blocked
  auth/operation-not-supported-in-this-environment
  :   Thrown if this operation is not supported in the environment your
      application is running on. "location.protocol" must be http or https.
  :   Thrown if the popup was blocked by the browser, typically when this
      operation is triggered outside of a click handler.

  auth/popup-closed-by-user
  :   Thrown if the popup window is closed by the user without completing the
      sign in to the provider.

  auth/provider-already-linked
  :   Thrown if the provider has already been linked to the user. This error is
      thrown even if this is not the same provider's account that is currently
      linked to the user.

  auth/unauthorized-domain
  :   Thrown if the app domain is not authorized for OAuth operations for your
      Firebase project. Edit the list of authorized domains from the Firebase
      console.

  This method does not work in a Node.js environment.

  example
  :

          // Creates the provider object.
          var provider = new firebase.auth.FacebookAuthProvider();
          // You can add additional scopes to the provider:
          provider.addScope('email');
          provider.addScope('user_friends');
          // Link with popup:
          user.linkWithPopup(provider).then(function(result) {
            // The firebase.User instance:
            var user = result.user;
            // The Facebook firebase.auth.AuthCredential containing the Facebook
            // access token:
            var credential = result.credential;
          }, function(error) {
            // An error happened.
          });


  #### Parameters

  -

    ##### provider: [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)

    The provider to authenticate.
    The provider has to be an OAuth provider. Non-OAuth providers like [firebase.auth.EmailAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider) will throw an error.

  #### Returns Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential)\>

### linkWithRedirect

- linkWithRedirect ( provider : [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider) ) : Promise \< void \>
- Links the authenticated provider to the user account using a full-page
  redirect flow.

  #### Error Codes

  auth/auth-domain-config-required
  :   Thrown if authDomain configuration is not provided when calling
      firebase.initializeApp(). Check Firebase Console for instructions on
      determining and passing that field.

  auth/operation-not-supported-in-this-environment
  :   Thrown if this operation is not supported in the environment your
      application is running on. "location.protocol" must be http or https.

  auth/provider-already-linked
  :   Thrown if the provider has already been linked to the user. This error is
      thrown even if this is not the same provider's account that is currently
      linked to the user.

  auth/unauthorized-domain
  :   Thrown if the app domain is not authorized for OAuth operations for your
      Firebase project. Edit the list of authorized domains from the Firebase
      console.

  #### Parameters

  -

    ##### provider: [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)

    The provider to authenticate.
    The provider has to be an OAuth provider. Non-OAuth providers like [firebase.auth.EmailAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider) will throw an error.

  #### Returns Promise\<void\>

### reauthenticateAndRetrieveDataWithCredential

- reauthenticateAndRetrieveDataWithCredential ( credential : [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential) ) : Promise \< [UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential) \>
-

  deprecated

  :   This method is deprecated. Use
      [firebase.User.reauthenticateWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#reauthenticatewithcredential) instead.

  Re-authenticates a user using a fresh credential, and returns any available
  additional user information, such as user name. Use before operations
  such as [firebase.User.updatePassword](https://firebase.google.com/docs/reference/js/v8/firebase.User#updatepassword) that require tokens from recent
  sign-in attempts.

  #### Error Codes

  auth/user-mismatch
  :   Thrown if the credential given does not correspond to the user.

  auth/user-not-found
  :   Thrown if the credential given does not correspond to any existing user.

  auth/invalid-credential
  :   Thrown if the provider's credential is not valid. This can happen if it
      has already expired when calling link, or if it used invalid token(s).
      See the Firebase documentation for your provider, and make sure you pass
      in the correct parameters to the credential method.

  auth/invalid-email
  :   Thrown if the email used in a
      [firebase.auth.EmailAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider#credential) is invalid.

  auth/wrong-password
  :   Thrown if the password used in a
      [firebase.auth.EmailAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider#credential) is not correct or when
      the user associated with the email does not have a password.

  auth/invalid-verification-code
  :   Thrown if the credential is a
      [firebase.auth.PhoneAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthProvider#credential) and the verification
      code of the credential is not valid.

  auth/invalid-verification-id
  :   Thrown if the credential is a
      [firebase.auth.PhoneAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthProvider#credential) and the verification
      ID of the credential is not valid.

  #### Parameters

  -

    ##### credential: [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential)

  #### Returns Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential)\>

### reauthenticateWithCredential

- reauthenticateWithCredential ( credential : [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential) ) : Promise \< [UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential) \>
- Re-authenticates a user using a fresh credential. Use before operations
  such as [firebase.User.updatePassword](https://firebase.google.com/docs/reference/js/v8/firebase.User#updatepassword) that require tokens from recent
  sign-in attempts.

  #### Error Codes

  auth/user-mismatch
  :   Thrown if the credential given does not correspond to the user.

  auth/user-not-found
  :   Thrown if the credential given does not correspond to any existing user.

  auth/invalid-credential
  :   Thrown if the provider's credential is not valid. This can happen if it
      has already expired when calling link, or if it used invalid token(s).
      See the Firebase documentation for your provider, and make sure you pass
      in the correct parameters to the credential method.

  auth/invalid-email
  :   Thrown if the email used in a
      [firebase.auth.EmailAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider#credential) is invalid.

  auth/wrong-password
  :   Thrown if the password used in a
      [firebase.auth.EmailAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider#credential) is not correct or when
      the user associated with the email does not have a password.

  auth/invalid-verification-code
  :   Thrown if the credential is a
      [firebase.auth.PhoneAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthProvider#credential) and the verification
      code of the credential is not valid.

  auth/invalid-verification-id
  :   Thrown if the credential is a
      [firebase.auth.PhoneAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthProvider#credential) and the verification
      ID of the credential is not valid.

  #### Parameters

  -

    ##### credential: [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential)

  #### Returns Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential)\>

### reauthenticateWithPhoneNumber

- reauthenticateWithPhoneNumber ( phoneNumber : string , applicationVerifier : [ApplicationVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ApplicationVerifier) ) : Promise \< [ConfirmationResult](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ConfirmationResult) \>
- Re-authenticates a user using a fresh credential. Use before operations
  such as [firebase.User.updatePassword](https://firebase.google.com/docs/reference/js/v8/firebase.User#updatepassword) that require tokens from recent
  sign-in attempts.

  #### Error Codes

  auth/user-mismatch
  :   Thrown if the credential given does not correspond to the user.

  auth/user-not-found
  :   Thrown if the credential given does not correspond to any existing user.

  auth/captcha-check-failed
  :   Thrown if the reCAPTCHA response token was invalid, expired, or if
      this method was called from a non-whitelisted domain.

  auth/invalid-phone-number
  :   Thrown if the phone number has an invalid format.

  auth/missing-phone-number
  :   Thrown if the phone number is missing.

  auth/quota-exceeded
  :   Thrown if the SMS quota for the Firebase project has been exceeded.

  #### Parameters

  -

    ##### phoneNumber: string

    The user's phone number in E.164 format (e.g.
    +16505550101).
  -

    ##### applicationVerifier: [ApplicationVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ApplicationVerifier)

  #### Returns Promise\<[ConfirmationResult](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ConfirmationResult)\>

### reauthenticateWithPopup

- reauthenticateWithPopup ( provider : [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider) ) : Promise \< [UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential) \>
- Reauthenticates the current user with the specified provider using a pop-up
  based OAuth flow.

  If the reauthentication is successful, the returned result will contain the
  user and the provider's credential.

  #### Error Codes

  auth/auth-domain-config-required
  :   Thrown if authDomain configuration is not provided when calling
      firebase.initializeApp(). Check Firebase Console for instructions on
      determining and passing that field.

  auth/cancelled-popup-request
  :   Thrown if successive popup operations are triggered. Only one popup
      request is allowed at one time on a user or an auth instance. All the
      popups would fail with this error except for the last one.

  auth/user-mismatch
  :   Thrown if the credential given does not correspond to the user.

  auth/operation-not-allowed
  :   Thrown if you have not enabled the provider in the Firebase Console. Go
      to the Firebase Console for your project, in the Auth section and the
      **Sign in Method** tab and configure the provider.

  auth/popup-blocked
  :   Thrown if the popup was blocked by the browser, typically when this
      operation is triggered outside of a click handler.

  auth/operation-not-supported-in-this-environment
  :   Thrown if this operation is not supported in the environment your
      application is running on. "location.protocol" must be http or https.

  auth/popup-closed-by-user
  :   Thrown if the popup window is closed by the user without completing the
      sign in to the provider.

  auth/unauthorized-domain
  :   Thrown if the app domain is not authorized for OAuth operations for your
      Firebase project. Edit the list of authorized domains from the Firebase
      console.

  This method does not work in a Node.js environment.

  example
  :

          // Creates the provider object.
          var provider = new firebase.auth.FacebookAuthProvider();
          // You can add additional scopes to the provider:
          provider.addScope('email');
          provider.addScope('user_friends');
          // Reauthenticate with popup:
          user.reauthenticateWithPopup(provider).then(function(result) {
            // The firebase.User instance:
            var user = result.user;
            // The Facebook firebase.auth.AuthCredential containing the Facebook
            // access token:
            var credential = result.credential;
          }, function(error) {
            // An error happened.
          });


  #### Parameters

  -

    ##### provider: [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)

    The provider to authenticate.
    The provider has to be an OAuth provider. Non-OAuth providers like [firebase.auth.EmailAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider) will throw an error.

  #### Returns Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential)\>

### reauthenticateWithRedirect

- reauthenticateWithRedirect ( provider : [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider) ) : Promise \< void \>
- Reauthenticates the current user with the specified OAuth provider using a
  full-page redirect flow.

  #### Error Codes

  auth/auth-domain-config-required
  :   Thrown if authDomain configuration is not provided when calling
      firebase.initializeApp(). Check Firebase Console for instructions on
      determining and passing that field.

  auth/operation-not-supported-in-this-environment
  :   Thrown if this operation is not supported in the environment your
      application is running on. "location.protocol" must be http or https.

  auth/user-mismatch
  :   Thrown if the credential given does not correspond to the user.

  auth/unauthorized-domain
  :   Thrown if the app domain is not authorized for OAuth operations for your
      Firebase project. Edit the list of authorized domains from the Firebase
      console.

  This method does not work in a Node.js environment.

  #### Parameters

  -

    ##### provider: [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)

    The provider to authenticate.
    The provider has to be an OAuth provider. Non-OAuth providers like [firebase.auth.EmailAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider) will throw an error.

  #### Returns Promise\<void\>

### reload

- reload ( ) : Promise \< void \>
- Refreshes the current user, if signed in.

  #### Returns Promise\<void\>

### sendEmailVerification

- sendEmailVerification ( actionCodeSettings ? : [ActionCodeSettings](https://firebase.google.com/docs/reference/js/v8/firebase.auth#actioncodesettings) \| null ) : Promise \< void \>
- Sends a verification email to a user.

  The verification process is completed by calling
  [firebase.auth.Auth.applyActionCode](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#applyactioncode)

  #### Error Codes

  auth/missing-android-pkg-name
  :   An Android package name must be provided if the Android app is required
      to be installed.

  auth/missing-continue-uri
  :   A continue URL must be provided in the request.

  auth/missing-ios-bundle-id
  :   An iOS bundle ID must be provided if an App Store ID is provided.

  auth/invalid-continue-uri
  :   The continue URL provided in the request is invalid.

  auth/unauthorized-continue-uri
  :   The domain of the continue URL is not whitelisted. Whitelist
      the domain in the Firebase console.

  example
  :

          var actionCodeSettings = {
            url: 'https://www.example.com/cart?email=user@example.com&cartId=123',
            iOS: {
              bundleId: 'com.example.ios'
            },
            android: {
              packageName: 'com.example.android',
              installApp: true,
              minimumVersion: '12'
            },
            handleCodeInApp: true
          };
          firebase.auth().currentUser.sendEmailVerification(actionCodeSettings)
              .then(function() {
                // Verification email sent.
              })
              .catch(function(error) {
                // Error occurred. Inspect error.code.
              });


  #### Parameters

  -

    ##### Optional actionCodeSettings: [ActionCodeSettings](https://firebase.google.com/docs/reference/js/v8/firebase.auth#actioncodesettings) \| null

    The action
    code settings. If specified, the state/continue URL will be set as the
    "continueUrl" parameter in the email verification link. The default email
    verification landing page will use this to display a link to go back to
    the app if it is installed.
    If the actionCodeSettings is not specified, no URL is appended to the
    action URL.
    The state URL provided must belong to a domain that is whitelisted by the
    developer in the console. Otherwise an error will be thrown.
    Mobile app redirects will only be applicable if the developer configures
    and accepts the Firebase Dynamic Links terms of condition.
    The Android package name and iOS bundle ID will be respected only if they
    are configured in the same Firebase Auth project used.

  #### Returns Promise\<void\>

### toJSON

- toJSON ( ) : Object
- Returns a JSON-serializable representation of this object.

  #### Returns Object

  A JSON-serializable representation of this object.

### unlink

- unlink ( providerId : string ) : Promise \< [User](https://firebase.google.com/docs/reference/js/v8/firebase.User) \>
- Unlinks a provider from a user account.

  #### Error Codes

  auth/no-such-provider
  :   Thrown if the user does not have this provider linked or when the
      provider ID given does not exist.

  #### Parameters

  -

    ##### providerId: string

  #### Returns Promise\<[User](https://firebase.google.com/docs/reference/js/v8/firebase.User)\>

### updateEmail

- updateEmail ( newEmail : string ) : Promise \< void \>
- Updates the user's email address.

  An email will be sent to the original email address (if it was set) that
  allows to revoke the email address change, in order to protect them from
  account hijacking.

  **Important:** this is a security sensitive operation that requires the
  user to have recently signed in. If this requirement isn't met, ask the user
  to authenticate again and then call
  [firebase.User.reauthenticateWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#reauthenticatewithcredential).

  #### Error Codes

  auth/invalid-email
  :   Thrown if the email used is invalid.

  auth/email-already-in-use
  :   Thrown if the email is already used by another user.

  auth/requires-recent-login
  :   Thrown if the user's last sign-in time does not meet the security
      threshold. Use [firebase.User.reauthenticateWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#reauthenticatewithcredential) to
      resolve. This does not apply if the user is anonymous.

  #### Parameters

  -

    ##### newEmail: string

    The new email address.

  #### Returns Promise\<void\>

### updatePassword

- updatePassword ( newPassword : string ) : Promise \< void \>
- Updates the user's password.

  **Important:** this is a security sensitive operation that requires the
  user to have recently signed in. If this requirement isn't met, ask the user
  to authenticate again and then call
  [firebase.User.reauthenticateWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#reauthenticatewithcredential).

  #### Error Codes

  auth/weak-password
  :   Thrown if the password is not strong enough.

  auth/requires-recent-login
  :   Thrown if the user's last sign-in time does not meet the security
      threshold. Use [firebase.User.reauthenticateWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#reauthenticatewithcredential) to
      resolve. This does not apply if the user is anonymous.

  #### Parameters

  -

    ##### newPassword: string

  #### Returns Promise\<void\>

### updatePhoneNumber

- updatePhoneNumber ( phoneCredential : [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential) ) : Promise \< void \>
- Updates the user's phone number.

  #### Error Codes

  auth/invalid-verification-code
  :   Thrown if the verification code of the credential is not valid.

  auth/invalid-verification-id
  :   Thrown if the verification ID of the credential is not valid.

  #### Parameters

  -

    ##### phoneCredential: [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential)

  #### Returns Promise\<void\>

### updateProfile

- updateProfile ( profile : { displayName ?: string \| null ; photoURL ?: string \| null } ) : Promise \< void \>
- Updates a user's profile data.

  example
  :

          // Updates the user attributes:
          user.updateProfile({
            displayName: "Jane Q. User",
            photoURL: "https://example.com/jane-q-user/profile.jpg"
          }).then(function() {
            // Profile updated successfully!
            // "Jane Q. User"
            var displayName = user.displayName;
            // "https://example.com/jane-q-user/profile.jpg"
            var photoURL = user.photoURL;
          }, function(error) {
            // An error happened.
          });

          // Passing a null value will delete the current attribute's value, but not
          // passing a property won't change the current attribute's value:
          // Let's say we're using the same user than before, after the update.
          user.updateProfile({photoURL: null}).then(function() {
            // Profile updated successfully!
            // "Jane Q. User", hasn't changed.
            var displayName = user.displayName;
            // Now, this is null.
            var photoURL = user.photoURL;
          }, function(error) {
            // An error happened.
          });


  #### Parameters

  -

    ##### profile: { displayName?: string \| null; photoURL?: string \| null }

    The profile's
    displayName and photoURL to update.
    -

      ##### Optional displayName?: string \| null

    -

      ##### Optional photoURL?: string \| null

  #### Returns Promise\<void\>

### verifyBeforeUpdateEmail

- verifyBeforeUpdateEmail ( newEmail : string , actionCodeSettings ? : [ActionCodeSettings](https://firebase.google.com/docs/reference/js/v8/firebase.auth#actioncodesettings) \| null ) : Promise \< void \>
- Sends a verification email to a new email address. The user's email will be
  updated to the new one after being verified.

  If you have a custom email action handler, you can complete the verification
  process by calling [firebase.auth.Auth.applyActionCode](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#applyactioncode).

  #### Error Codes

  auth/missing-android-pkg-name
  :   An Android package name must be provided if the Android app is required
      to be installed.

  auth/missing-continue-uri
  :   A continue URL must be provided in the request.

  auth/missing-ios-bundle-id
  :   An iOS bundle ID must be provided if an App Store ID is provided.

  auth/invalid-continue-uri
  :   The continue URL provided in the request is invalid.

  auth/unauthorized-continue-uri
  :   The domain of the continue URL is not whitelisted. Whitelist
      the domain in the Firebase console.

  example
  :

          var actionCodeSettings = {
            url: 'https://www.example.com/cart?email=user@example.com&cartId=123',
            iOS: {
              bundleId: 'com.example.ios'
            },
            android: {
              packageName: 'com.example.android',
              installApp: true,
              minimumVersion: '12'
            },
            handleCodeInApp: true
          };
          firebase.auth().currentUser.verifyBeforeUpdateEmail(
            'user@example.com', actionCodeSettings)
            .then(function() {
              // Verification email sent.
            })
            .catch(function(error) {
              // Error occurred. Inspect error.code.
            });


  #### Parameters

  -

    ##### newEmail: string

    The email address to be verified and updated to.
  -

    ##### Optional actionCodeSettings: [ActionCodeSettings](https://firebase.google.com/docs/reference/js/v8/firebase.auth#actioncodesettings) \| null

    The action
    code settings. If specified, the state/continue URL will be set as the
    "continueUrl" parameter in the email verification link. The default email
    verification landing page will use this to display a link to go back to
    the app if it is installed.
    If the actionCodeSettings is not specified, no URL is appended to the
    action URL.
    The state URL provided must belong to a domain that is whitelisted by the
    developer in the console. Otherwise an error will be thrown.
    Mobile app redirects will only be applicable if the developer configures
    and accepts the Firebase Dynamic Links terms of condition.
    The Android package name and iOS bundle ID will be respected only if they
    are configured in the same Firebase Auth project used.

  #### Returns Promise\<void\>