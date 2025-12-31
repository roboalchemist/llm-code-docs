# Source: https://firebase.google.com/docs/reference/node/firebase.auth.Auth.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth.md.txt

# Auth | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- Auth

The Firebase Auth service interface.

Do not call this constructor directly. Instead, use
[`firebase.auth()`](https://firebase.google.com/docs/reference/js/v8/firebase.auth).

See
[Firebase Authentication](https://firebase.google.com/docs/auth/)
for a full guide on how to use the Firebase Auth service.

## Index

### Type aliases

- [Persistence](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#persistence)

### Properties

- [app](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#app)
- [config](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#config)
- [currentUser](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#currentuser)
- [emulatorConfig](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#emulatorconfig)
- [languageCode](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#languagecode)
- [name](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#name)
- [settings](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#settings)
- [tenantId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#tenantid)

### Variables

- [Persistence](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#persistence-1)

### Methods

- [applyActionCode](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#applyactioncode)
- [checkActionCode](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#checkactioncode)
- [confirmPasswordReset](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#confirmpasswordreset)
- [createUserWithEmailAndPassword](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#createuserwithemailandpassword)
- [fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#fetchsigninmethodsforemail)
- [getRedirectResult](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#getredirectresult)
- [isSignInWithEmailLink](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#issigninwithemaillink)
- [onAuthStateChanged](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#onauthstatechanged)
- [onIdTokenChanged](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#onidtokenchanged)
- [sendPasswordResetEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#sendpasswordresetemail)
- [sendSignInLinkToEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#sendsigninlinktoemail)
- [setPersistence](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#setpersistence)
- [signInAndRetrieveDataWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signinandretrievedatawithcredential)
- [signInAnonymously](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signinanonymously)
- [signInWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signinwithcredential)
- [signInWithCustomToken](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signinwithcustomtoken)
- [signInWithEmailAndPassword](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signinwithemailandpassword)
- [signInWithEmailLink](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signinwithemaillink)
- [signInWithPhoneNumber](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signinwithphonenumber)
- [signInWithPopup](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signinwithpopup)
- [signInWithRedirect](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signinwithredirect)
- [signOut](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signout)
- [updateCurrentUser](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#updatecurrentuser)
- [useDeviceLanguage](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#usedevicelanguage)
- [useEmulator](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#useemulator)
- [verifyPasswordResetCode](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#verifypasswordresetcode)

## Type aliases

### Persistence

Persistence: string

## Properties

### app

app: [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)  
The [app](https://firebase.google.com/docs/reference/js/v8/firebase.app.App) associated with the `Auth` service
instance.

example
:

        var app = auth.app;


### config

config: [Config](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Config)  
The config used to initialize this instance.

### currentUser

currentUser: [User](https://firebase.google.com/docs/reference/js/v8/firebase.User) \| null  
The currently signed-in user (or null).

### emulatorConfig

emulatorConfig: [EmulatorConfig](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmulatorConfig) \| null  
The current emulator configuration (or null).

### languageCode

languageCode: string \| null  
The current Auth instance's language code. This is a readable/writable
property. When set to null, the default Firebase Console language setting
is applied. The language code will propagate to email action templates
(password reset, email verification and email change revocation), SMS
templates for phone authentication, reCAPTCHA verifier and OAuth
popup/redirect operations provided the specified providers support
localization with the language code specified.

### name

name: string  
The name of the app associated with the Auth service instance.

### settings

settings: [AuthSettings](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthSettings)  
The current Auth instance's settings. This is used to edit/read configuration
related options like app verification mode for phone authentication.

### tenantId

tenantId: string \| null  
The current Auth instance's tenant ID. This is a readable/writable
property. When you set the tenant ID of an Auth instance, all future
sign-in/sign-up operations will pass this tenant ID and sign in or
sign up users to the specified tenant project.
When set to null, users are signed in to the parent project. By default,
this is set to null.

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


## Variables

### Persistence

Persistence: { LOCAL: [Persistence](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#persistence); NONE: [Persistence](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#persistence); SESSION: [Persistence](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#persistence) }  
An enumeration of the possible persistence mechanism types.  

#### Type declaration

-

  ##### LOCAL: [Persistence](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#persistence)

  Indicates that the state will be persisted even when the browser window is
  closed or the activity is destroyed in react-native.
-

  ##### NONE: [Persistence](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#persistence)

  Indicates that the state will only be stored in memory and will be cleared
  when the window or activity is refreshed.
-

  ##### SESSION: [Persistence](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#persistence)

  Indicates that the state will only persist in current session/tab, relevant
  to web only, and will be cleared when the tab is closed.

## Methods

### applyActionCode

- applyActionCode ( code : string ) : Promise \< void \>
- Applies a verification code sent to the user by email or other out-of-band
  mechanism.

  #### Error Codes

  auth/expired-action-code
  :   Thrown if the action code has expired.

  auth/invalid-action-code
  :   Thrown if the action code is invalid. This can happen if the code is
      malformed or has already been used.

  auth/user-disabled
  :   Thrown if the user corresponding to the given action code has been
      disabled.

  auth/user-not-found
  :   Thrown if there is no user corresponding to the action code. This may
      have happened if the user was deleted between when the action code was
      issued and when this method was called.

  #### Parameters

  -

    ##### code: string

    A verification code sent to the user.

  #### Returns Promise\<void\>

### checkActionCode

- checkActionCode ( code : string ) : Promise \< [ActionCodeInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo) \>
- Checks a verification code sent to the user by email or other out-of-band
  mechanism.

  Returns metadata about the code.

  #### Error Codes

  auth/expired-action-code
  :   Thrown if the action code has expired.

  auth/invalid-action-code
  :   Thrown if the action code is invalid. This can happen if the code is
      malformed or has already been used.

  auth/user-disabled
  :   Thrown if the user corresponding to the given action code has been
      disabled.

  auth/user-not-found
  :   Thrown if there is no user corresponding to the action code. This may
      have happened if the user was deleted between when the action code was
      issued and when this method was called.

  #### Parameters

  -

    ##### code: string

    A verification code sent to the user.

  #### Returns Promise\<[ActionCodeInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo)\>

### confirmPasswordReset

- confirmPasswordReset ( code : string , newPassword : string ) : Promise \< void \>
- Completes the password reset process, given a confirmation code and new
  password.

  #### Error Codes

  auth/expired-action-code
  :   Thrown if the password reset code has expired.

  auth/invalid-action-code
  :   Thrown if the password reset code is invalid. This can happen if the
      code is malformed or has already been used.

  auth/user-disabled
  :   Thrown if the user corresponding to the given password reset code has
      been disabled.

  auth/user-not-found
  :   Thrown if there is no user corresponding to the password reset code. This
      may have happened if the user was deleted between when the code was
      issued and when this method was called.

  auth/weak-password
  :   Thrown if the new password is not strong enough.

  #### Parameters

  -

    ##### code: string

    The confirmation code send via email to the user.
  -

    ##### newPassword: string

    The new password.

  #### Returns Promise\<void\>

### createUserWithEmailAndPassword

- createUserWithEmailAndPassword ( email : string , password : string ) : Promise \< [UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential) \>
- Creates a new user account associated with the specified email address and
  password.

  On successful creation of the user account, this user will also be
  signed in to your application.

  User account creation can fail if the account already exists or the password
  is invalid.

  Note: The email address acts as a unique identifier for the user and
  enables an email-based password reset. This function will create
  a new user account and set the initial user password.

  #### Error Codes

  auth/email-already-in-use
  :   Thrown if there already exists an account with the given email
      address.

  auth/invalid-email
  :   Thrown if the email address is not valid.

  auth/operation-not-allowed
  :   Thrown if email/password accounts are not enabled. Enable email/password
      accounts in the Firebase Console, under the Auth tab.

  auth/weak-password
  :   Thrown if the password is not strong enough.

  example
  :

          firebase.auth().createUserWithEmailAndPassword(email, password)
              .catch(function(error) {
            // Handle Errors here.
            var errorCode = error.code;
            var errorMessage = error.message;
            if (errorCode == 'auth/weak-password') {
              alert('The password is too weak.');
            } else {
              alert(errorMessage);
            }
            console.log(error);
          });


  #### Parameters

  -

    ##### email: string

    The user's email address.
  -

    ##### password: string

    The user's chosen password.

  #### Returns Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential)\>

### fetchSignInMethodsForEmail

- fetchSignInMethodsForEmail ( email : string ) : Promise \< Array \< string \> \>
- Gets the list of possible sign in methods for the given email address. This
  is useful to differentiate methods of sign-in for the same provider,
  eg. `EmailAuthProvider` which has 2 methods of sign-in, email/password and
  email/link.

  #### Error Codes

  auth/invalid-email
  :   Thrown if the email address is not valid.

  #### Parameters

  -

    ##### email: string

  #### Returns Promise\<Array\<string\>\>

### getRedirectResult

- getRedirectResult ( ) : Promise \< [UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential) \>
- Returns a UserCredential from the redirect-based sign-in flow.

  If sign-in succeeded, returns the signed in user. If sign-in was
  unsuccessful, fails with an error. If no redirect operation was called, returns `null`.

  #### Error Codes

  auth/account-exists-with-different-credential
  :   Thrown if there already exists an account with the email address
      asserted by the credential. Resolve this by calling
      [firebase.auth.Auth.fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#fetchsigninmethodsforemail) with the error.email
      and then asking the user to sign in using one of the returned providers.
      Once the user is signed in, the original credential retrieved from the
      error.credential can be linked to the user with
      [firebase.User.linkWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#linkwithcredential) to prevent the user from signing
      in again to the original provider via popup or redirect. If you are using
      redirects for sign in, save the credential in session storage and then
      retrieve on redirect and repopulate the credential using for example
      [firebase.auth.GoogleAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.GoogleAuthProvider#credential) depending on the
      credential provider id and complete the link.

  auth/auth-domain-config-required
  :   Thrown if authDomain configuration is not provided when calling
      firebase.initializeApp(). Check Firebase Console for instructions on
      determining and passing that field.

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
  :   Thrown if the type of account corresponding to the credential
      is not enabled. Enable the account type in the Firebase Console, under
      the Auth tab.

  auth/operation-not-supported-in-this-environment
  :   Thrown if this operation is not supported in the environment your
      application is running on. "location.protocol" must be http or https.

  auth/timeout
  :   Thrown typically if the app domain is not authorized for OAuth operations
      for your Firebase project. Edit the list of authorized domains from the
      Firebase console.

  This method does not work in a Node.js environment.

  example
  :

          // First, we perform the signInWithRedirect.
          // Creates the provider object.
          var provider = new firebase.auth.FacebookAuthProvider();
          // You can add additional scopes to the provider:
          provider.addScope('email');
          provider.addScope('user_friends');
          // Sign in with redirect:
          auth.signInWithRedirect(provider)
          ////////////////////////////////////////////////////////////
          // The user is redirected to the provider's sign in flow...
          ////////////////////////////////////////////////////////////
          // Then redirected back to the app, where we check the redirect result:
          auth.getRedirectResult().then(function(result) {
            // The firebase.User instance:
            var user = result.user;
            // The Facebook firebase.auth.AuthCredential containing the Facebook
            // access token:
            var credential = result.credential;
            // As this API can be used for sign-in, linking and reauthentication,
            // check the operationType to determine what triggered this redirect
            // operation.
            var operationType = result.operationType;
          }, function(error) {
            // The provider's account email, can be used in case of
            // auth/account-exists-with-different-credential to fetch the providers
            // linked to the email:
            var email = error.email;
            // The provider's credential:
            var credential = error.credential;
            // In case of auth/account-exists-with-different-credential error,
            // you can fetch the providers using this:
            if (error.code === 'auth/account-exists-with-different-credential') {
              auth.fetchSignInMethodsForEmail(email).then(function(providers) {
                // The returned 'providers' is a list of the available providers
                // linked to the email address. Please refer to the guide for a more
                // complete explanation on how to recover from this error.
              });
            }
          });


  #### Returns Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential)\>

### isSignInWithEmailLink

- isSignInWithEmailLink ( emailLink : string ) : boolean
- Checks if an incoming link is a sign-in with email link.

  #### Parameters

  -

    ##### emailLink: string

  #### Returns boolean

### onAuthStateChanged

- onAuthStateChanged ( nextOrObserver : Observer \< any \> \| ( ( a : [User](https://firebase.google.com/docs/reference/js/v8/firebase.User) \| null ) =\> any ) , error ? : ( a : [Error](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Error) ) =\> any , completed ? : firebase.Unsubscribe ) : firebase.Unsubscribe
- Adds an observer for changes to the user's sign-in state.

  Prior to 4.0.0, this triggered the observer when users were signed in,
  signed out, or when the user's ID token changed in situations such as token
  expiry or password change. After 4.0.0, the observer is only triggered
  on sign-in or sign-out.

  To keep the old behavior, see [firebase.auth.Auth.onIdTokenChanged](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#onidtokenchanged).

  example
  :

          firebase.auth().onAuthStateChanged(function(user) {
            if (user) {
              // User is signed in.
            }
          });


  #### Parameters

  -

    ##### nextOrObserver: Observer\<any\> \| ((a: [User](https://firebase.google.com/docs/reference/js/v8/firebase.User) \| null) =\> any)

  -

    ##### Optional error: (a: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Error)) =\> any

    -
      - (a: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Error)): any

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Error)

        #### Returns any

  -

    ##### Optional completed: firebase.Unsubscribe

  #### Returns firebase.Unsubscribe

### onIdTokenChanged

- onIdTokenChanged ( nextOrObserver : Observer \< any \> \| ( ( a : [User](https://firebase.google.com/docs/reference/js/v8/firebase.User) \| null ) =\> any ) , error ? : ( a : [Error](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Error) ) =\> any , completed ? : firebase.Unsubscribe ) : firebase.Unsubscribe
- Adds an observer for changes to the signed-in user's ID token, which includes
  sign-in, sign-out, and token refresh events. This method has the same
  behavior as [firebase.auth.Auth.onAuthStateChanged](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#onauthstatechanged) had prior to 4.0.0.

  example
  :

          firebase.auth().onIdTokenChanged(function(user) {
            if (user) {
              // User is signed in or token was refreshed.
            }
          });


  #### Parameters

  -

    ##### nextOrObserver: Observer\<any\> \| ((a: [User](https://firebase.google.com/docs/reference/js/v8/firebase.User) \| null) =\> any)

  -

    ##### Optional error: (a: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Error)) =\> any

    Optional A function
    triggered on auth error.
    -
      - (a: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Error)): any

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Error)

        #### Returns any

  -

    ##### Optional completed: firebase.Unsubscribe

    Optional A function triggered when the
    observer is removed.

  #### Returns firebase.Unsubscribe

### sendPasswordResetEmail

- sendPasswordResetEmail ( email : string , actionCodeSettings ? : [ActionCodeSettings](https://firebase.google.com/docs/reference/js/v8/firebase.auth#actioncodesettings) \| null ) : Promise \< void \>
- Sends a password reset email to the given email address.

  To complete the password reset, call
  [firebase.auth.Auth.confirmPasswordReset](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#confirmpasswordreset) with the code supplied in the
  email sent to the user, along with the new password specified by the user.

  #### Error Codes

  auth/invalid-email
  :   Thrown if the email address is not valid.

  auth/missing-android-pkg-name
  :   An Android package name must be provided if the Android app is required
      to be installed.

  auth/missing-continue-uri
  :   A continue URL must be provided in the request.

  auth/missing-ios-bundle-id
  :   An iOS Bundle ID must be provided if an App Store ID is provided.

  auth/invalid-continue-uri
  :   The continue URL provided in the request is invalid.

  auth/unauthorized-continue-uri
  :   The domain of the continue URL is not whitelisted. Whitelist
      the domain in the Firebase console.

  auth/user-not-found
  :   Thrown if there is no user corresponding to the email address.

  example
  :

          var actionCodeSettings = {
            url: 'https://www.example.com/?email=user@example.com',
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
          firebase.auth().sendPasswordResetEmail(
              'user@example.com', actionCodeSettings)
              .then(function() {
                // Password reset email sent.
              })
              .catch(function(error) {
                // Error occurred. Inspect error.code.
              });


  #### Parameters

  -

    ##### email: string

    The email address with the password to be reset.
  -

    ##### Optional actionCodeSettings: [ActionCodeSettings](https://firebase.google.com/docs/reference/js/v8/firebase.auth#actioncodesettings) \| null

    The action
    code settings. If specified, the state/continue URL will be set as the
    "continueUrl" parameter in the password reset link. The default password
    reset landing page will use this to display a link to go back to the app
    if it is installed.
    If the actionCodeSettings is not specified, no URL is appended to the
    action URL.
    The state URL provided must belong to a domain that is whitelisted by the
    developer in the console. Otherwise an error will be thrown.
    Mobile app redirects will only be applicable if the developer configures
    and accepts the Firebase Dynamic Links terms of condition.
    The Android package name and iOS bundle ID will be respected only if they
    are configured in the same Firebase Auth project used.

  #### Returns Promise\<void\>

### sendSignInLinkToEmail

- sendSignInLinkToEmail ( email : string , actionCodeSettings : [ActionCodeSettings](https://firebase.google.com/docs/reference/js/v8/firebase.auth#actioncodesettings) ) : Promise \< void \>
- Sends a sign-in email link to the user with the specified email.

  The sign-in operation has to always be completed in the app unlike other out
  of band email actions (password reset and email verifications). This is
  because, at the end of the flow, the user is expected to be signed in and
  their Auth state persisted within the app.

  To complete sign in with the email link, call
  [firebase.auth.Auth.signInWithEmailLink](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signinwithemaillink) with the email address and
  the email link supplied in the email sent to the user.

  #### Error Codes

  auth/argument-error
  :   Thrown if handleCodeInApp is false.

  auth/invalid-email
  :   Thrown if the email address is not valid.

  auth/missing-android-pkg-name
  :   An Android package name must be provided if the Android app is required
      to be installed.

  auth/missing-continue-uri
  :   A continue URL must be provided in the request.

  auth/missing-ios-bundle-id
  :   An iOS Bundle ID must be provided if an App Store ID is provided.

  auth/invalid-continue-uri
  :   The continue URL provided in the request is invalid.

  auth/unauthorized-continue-uri
  :   The domain of the continue URL is not whitelisted. Whitelist
      the domain in the Firebase console.

  example
  :

          var actionCodeSettings = {
            // The URL to redirect to for sign-in completion. This is also the deep
            // link for mobile redirects. The domain (www.example.com) for this URL
            // must be whitelisted in the Firebase Console.
            url: 'https://www.example.com/finishSignUp?cartId=1234',
            iOS: {
              bundleId: 'com.example.ios'
            },
            android: {
              packageName: 'com.example.android',
              installApp: true,
              minimumVersion: '12'
            },
            // This must be true.
            handleCodeInApp: true
          };
          firebase.auth().sendSignInLinkToEmail('user@example.com', actionCodeSettings)
              .then(function() {
                // The link was successfully sent. Inform the user. Save the email
                // locally so you don't need to ask the user for it again if they open
                // the link on the same device.
              })
              .catch(function(error) {
                // Some error occurred, you can inspect the code: error.code
              });


  #### Parameters

  -

    ##### email: string

    The email account to sign in with.
  -

    ##### actionCodeSettings: [ActionCodeSettings](https://firebase.google.com/docs/reference/js/v8/firebase.auth#actioncodesettings)

    The action
    code settings. The action code settings which provides Firebase with
    instructions on how to construct the email link. This includes the
    sign in completion URL or the deep link for mobile redirects, the mobile
    apps to use when the sign-in link is opened on an Android or iOS device.
    Mobile app redirects will only be applicable if the developer configures
    and accepts the Firebase Dynamic Links terms of condition.
    The Android package name and iOS bundle ID will be respected only if they
    are configured in the same Firebase Auth project used.

  #### Returns Promise\<void\>

### setPersistence

- setPersistence ( persistence : [Persistence](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#persistence) ) : Promise \< void \>
- Changes the current type of persistence on the current Auth instance for the
  currently saved Auth session and applies this type of persistence for
  future sign-in requests, including sign-in with redirect requests. This will
  return a promise that will resolve once the state finishes copying from one
  type of storage to the other.
  Calling a sign-in method after changing persistence will wait for that
  persistence change to complete before applying it on the new Auth state.

  This makes it easy for a user signing in to specify whether their session
  should be remembered or not. It also makes it easier to never persist the
  Auth state for applications that are shared by other users or have sensitive
  data.

  The default for web browser apps and React Native apps is 'local' (provided
  the browser supports this mechanism) whereas it is 'none' for Node.js backend
  apps.

  #### Error Codes (thrown synchronously)

  auth/invalid-persistence-type
  :   Thrown if the specified persistence type is invalid.

  auth/unsupported-persistence-type
  :   Thrown if the current environment does not support the specified
      persistence type.

  example
  :

          firebase.auth().setPersistence(firebase.auth.Auth.Persistence.SESSION)
              .then(function() {
            // Existing and future Auth states are now persisted in the current
            // session only. Closing the window would clear any existing state even if
            // a user forgets to sign out.
          });


  #### Parameters

  -

    ##### persistence: [Persistence](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#persistence)

  #### Returns Promise\<void\>

### signInAndRetrieveDataWithCredential

- signInAndRetrieveDataWithCredential ( credential : [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential) ) : Promise \< [UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential) \>
-

  deprecated

  :   This method is deprecated. Use
      [firebase.auth.Auth.signInWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signinwithcredential) instead.

  Asynchronously signs in with the given credentials, and returns any available
  additional user information, such as user name.

  #### Error Codes

  auth/account-exists-with-different-credential
  :   Thrown if there already exists an account with the email address
      asserted by the credential. Resolve this by calling
      [firebase.auth.Auth.fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#fetchsigninmethodsforemail) and then asking the
      user to sign in using one of the returned providers. Once the user is
      signed in, the original credential can be linked to the user with
      [firebase.User.linkWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#linkwithcredential).

  auth/invalid-credential
  :   Thrown if the credential is malformed or has expired.

  auth/operation-not-allowed
  :   Thrown if the type of account corresponding to the credential
      is not enabled. Enable the account type in the Firebase Console, under
      the Auth tab.

  auth/user-disabled
  :   Thrown if the user corresponding to the given credential has been
      disabled.

  auth/user-not-found
  :   Thrown if signing in with a credential from
      [firebase.auth.EmailAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider#credential) and there is no user
      corresponding to the given email.

  auth/wrong-password
  :   Thrown if signing in with a credential from
      [firebase.auth.EmailAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider#credential) and the password is
      invalid for the given email, or if the account corresponding to the email
      does not have a password set.

  auth/invalid-verification-code
  :   Thrown if the credential is a
      [firebase.auth.PhoneAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthProvider#credential) and the verification
      code of the credential is not valid.

  auth/invalid-verification-id
  :   Thrown if the credential is a
      [firebase.auth.PhoneAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthProvider#credential) and the verification
      ID of the credential is not valid.

  example
  :

          firebase.auth().signInAndRetrieveDataWithCredential(credential)
              .then(function(userCredential) {
                console.log(userCredential.additionalUserInfo.username);
              });


  #### Parameters

  -

    ##### credential: [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential)

    The auth credential.

  #### Returns Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential)\>

### signInAnonymously

- signInAnonymously ( ) : Promise \< [UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential) \>
- Asynchronously signs in as an anonymous user.

  If there is already an anonymous user signed in, that user will be returned;
  otherwise, a new anonymous user identity will be created and returned.

  #### Error Codes

  auth/operation-not-allowed
  :   Thrown if anonymous accounts are not enabled. Enable anonymous accounts
      in the Firebase Console, under the Auth tab.

  example
  :

          firebase.auth().signInAnonymously().catch(function(error) {
            // Handle Errors here.
            var errorCode = error.code;
            var errorMessage = error.message;

            if (errorCode === 'auth/operation-not-allowed') {
              alert('You must enable Anonymous auth in the Firebase Console.');
            } else {
              console.error(error);
            }
          });


  #### Returns Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential)\>

### signInWithCredential

- signInWithCredential ( credential : [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential) ) : Promise \< [UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential) \>
- Asynchronously signs in with the given credentials.

  #### Error Codes

  auth/account-exists-with-different-credential
  :   Thrown if there already exists an account with the email address
      asserted by the credential. Resolve this by calling
      [firebase.auth.Auth.fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#fetchsigninmethodsforemail) and then asking the
      user to sign in using one of the returned providers. Once the user is
      signed in, the original credential can be linked to the user with
      [firebase.User.linkWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#linkwithcredential).

  auth/invalid-credential
  :   Thrown if the credential is malformed or has expired.

  auth/operation-not-allowed
  :   Thrown if the type of account corresponding to the credential
      is not enabled. Enable the account type in the Firebase Console, under
      the Auth tab.

  auth/user-disabled
  :   Thrown if the user corresponding to the given credential has been
      disabled.

  auth/user-not-found
  :   Thrown if signing in with a credential from
      [firebase.auth.EmailAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider#credential) and there is no user
      corresponding to the given email.

  auth/wrong-password
  :   Thrown if signing in with a credential from
      [firebase.auth.EmailAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider#credential) and the password is
      invalid for the given email, or if the account corresponding to the email
      does not have a password set.

  auth/invalid-verification-code
  :   Thrown if the credential is a
      [firebase.auth.PhoneAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthProvider#credential) and the verification
      code of the credential is not valid.

  auth/invalid-verification-id
  :   Thrown if the credential is a
      [firebase.auth.PhoneAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthProvider#credential) and the verification
      ID of the credential is not valid.

  example
  :

          firebase.auth().signInWithCredential(credential).catch(function(error) {
            // Handle Errors here.
            var errorCode = error.code;
            var errorMessage = error.message;
            // The email of the user's account used.
            var email = error.email;
            // The firebase.auth.AuthCredential type that was used.
            var credential = error.credential;
            if (errorCode === 'auth/account-exists-with-different-credential') {
              alert('Email already associated with another account.');
              // Handle account linking here, if using.
            } else {
              console.error(error);
            }
           });


  #### Parameters

  -

    ##### credential: [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential)

    The auth credential.

  #### Returns Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential)\>

### signInWithCustomToken

- signInWithCustomToken ( token : string ) : Promise \< [UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential) \>
- Asynchronously signs in using a custom token.

  Custom tokens are used to integrate Firebase Auth with existing auth systems,
  and must be generated by the auth backend.

  Fails with an error if the token is invalid, expired, or not accepted by the
  Firebase Auth service.

  #### Error Codes

  auth/custom-token-mismatch
  :   Thrown if the custom token is for a different Firebase App.

  auth/invalid-custom-token
  :   Thrown if the custom token format is incorrect.

  example
  :

          firebase.auth().signInWithCustomToken(token).catch(function(error) {
            // Handle Errors here.
            var errorCode = error.code;
            var errorMessage = error.message;
            if (errorCode === 'auth/invalid-custom-token') {
              alert('The token you provided is not valid.');
            } else {
              console.error(error);
            }
          });


  #### Parameters

  -

    ##### token: string

    The custom token to sign in with.

  #### Returns Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential)\>

### signInWithEmailAndPassword

- signInWithEmailAndPassword ( email : string , password : string ) : Promise \< [UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential) \>
- Asynchronously signs in using an email and password.

  Fails with an error if the email address and password do not match.

  Note: The user's password is NOT the password used to access the user's email
  account. The email address serves as a unique identifier for the user, and
  the password is used to access the user's account in your Firebase project.

  See also: [firebase.auth.Auth.createUserWithEmailAndPassword](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#createuserwithemailandpassword).

  #### Error Codes

  auth/invalid-email
  :   Thrown if the email address is not valid.

  auth/user-disabled
  :   Thrown if the user corresponding to the given email has been
      disabled.

  auth/user-not-found
  :   Thrown if there is no user corresponding to the given email.

  auth/wrong-password
  :   Thrown if the password is invalid for the given email, or the account
      corresponding to the email does not have a password set.

  example
  :

          firebase.auth().signInWithEmailAndPassword(email, password)
              .catch(function(error) {
            // Handle Errors here.
            var errorCode = error.code;
            var errorMessage = error.message;
            if (errorCode === 'auth/wrong-password') {
              alert('Wrong password.');
            } else {
              alert(errorMessage);
            }
            console.log(error);
          });


  #### Parameters

  -

    ##### email: string

    The users email address.
  -

    ##### password: string

    The users password.

  #### Returns Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential)\>

### signInWithEmailLink

- signInWithEmailLink ( email : string , emailLink ? : string ) : Promise \< [UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential) \>
- Asynchronously signs in using an email and sign-in email link. If no link
  is passed, the link is inferred from the current URL.

  Fails with an error if the email address is invalid or OTP in email link
  expires.

  Note: Confirm the link is a sign-in email link before calling this method
  [firebase.auth.Auth.isSignInWithEmailLink](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#issigninwithemaillink).

  #### Error Codes

  auth/expired-action-code
  :   Thrown if OTP in email link expires.

  auth/invalid-email
  :   Thrown if the email address is not valid.

  auth/user-disabled
  :   Thrown if the user corresponding to the given email has been
      disabled.

  example
  :

          firebase.auth().signInWithEmailLink(email, emailLink)
              .catch(function(error) {
                // Some error occurred, you can inspect the code: error.code
                // Common errors could be invalid email and invalid or expired OTPs.
              });


  #### Parameters

  -

    ##### email: string

    The email account to sign in with.
  -

    ##### Optional emailLink: string

    The optional link which contains the OTP needed
    to complete the sign in with email link. If not specified, the current
    URL is used instead.

  #### Returns Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential)\>

### signInWithPhoneNumber

- signInWithPhoneNumber ( phoneNumber : string , applicationVerifier : [ApplicationVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ApplicationVerifier) ) : Promise \< [ConfirmationResult](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ConfirmationResult) \>
- Asynchronously signs in using a phone number. This method sends a code via
  SMS to the given phone number, and returns a
  [firebase.auth.ConfirmationResult](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ConfirmationResult). After the user provides the code
  sent to their phone, call [firebase.auth.ConfirmationResult.confirm](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ConfirmationResult#confirm)
  with the code to sign the user in.

  For abuse prevention, this method also requires a
  [firebase.auth.ApplicationVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ApplicationVerifier). The Firebase Auth SDK includes
  a reCAPTCHA-based implementation, [firebase.auth.RecaptchaVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier).

  #### Error Codes

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

  auth/operation-not-allowed
  :   Thrown if you have not enabled the provider in the Firebase Console. Go
      to the Firebase Console for your project, in the Auth section and the
      **Sign in Method** tab and configure the provider.

  example
  :

          // 'recaptcha-container' is the ID of an element in the DOM.
          var applicationVerifier = new firebase.auth.RecaptchaVerifier(
              'recaptcha-container');
          firebase.auth().signInWithPhoneNumber(phoneNumber, applicationVerifier)
              .then(function(confirmationResult) {
                var verificationCode = window.prompt('Please enter the verification ' +
                    'code that was sent to your mobile device.');
                return confirmationResult.confirm(verificationCode);
              })
              .catch(function(error) {
                // Handle Errors here.
              });


  #### Parameters

  -

    ##### phoneNumber: string

    The user's phone number in E.164 format (e.g.
    +16505550101).
  -

    ##### applicationVerifier: [ApplicationVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ApplicationVerifier)

  #### Returns Promise\<[ConfirmationResult](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ConfirmationResult)\>

### signInWithPopup

- signInWithPopup ( provider : [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider) ) : Promise \< [UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential) \>
- Authenticates a Firebase client using a popup-based OAuth authentication
  flow.

  If succeeds, returns the signed in user along with the provider's credential.
  If sign in was unsuccessful, returns an error object containing additional
  information about the error.

  #### Error Codes

  auth/account-exists-with-different-credential
  :   Thrown if there already exists an account with the email address
      asserted by the credential. Resolve this by calling
      [firebase.auth.Auth.fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#fetchsigninmethodsforemail) with the error.email
      and then asking the user to sign in using one of the returned providers.
      Once the user is signed in, the original credential retrieved from the
      error.credential can be linked to the user with
      [firebase.User.linkWithCredential](https://firebase.google.com/docs/reference/js/v8/firebase.User#linkwithcredential) to prevent the user from signing
      in again to the original provider via popup or redirect. If you are using
      redirects for sign in, save the credential in session storage and then
      retrieve on redirect and repopulate the credential using for example
      [firebase.auth.GoogleAuthProvider.credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.GoogleAuthProvider#credential) depending on the
      credential provider id and complete the link.

  auth/auth-domain-config-required
  :   Thrown if authDomain configuration is not provided when calling
      firebase.initializeApp(). Check Firebase Console for instructions on
      determining and passing that field.

  auth/cancelled-popup-request
  :   Thrown if successive popup operations are triggered. Only one popup
      request is allowed at one time. All the popups would fail with this error
      except for the last one.

  auth/operation-not-allowed
  :   Thrown if the type of account corresponding to the credential
      is not enabled. Enable the account type in the Firebase Console, under
      the Auth tab.

  auth/operation-not-supported-in-this-environment
  :   Thrown if this operation is not supported in the environment your
      application is running on. "location.protocol" must be http or https.

  auth/popup-blocked
  :   Thrown if the popup was blocked by the browser, typically when this
      operation is triggered outside of a click handler.

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
          // Sign in with popup:
          auth.signInWithPopup(provider).then(function(result) {
            // The firebase.User instance:
            var user = result.user;
            // The Facebook firebase.auth.AuthCredential containing the Facebook
            // access token:
            var credential = result.credential;
          }, function(error) {
            // The provider's account email, can be used in case of
            // auth/account-exists-with-different-credential to fetch the providers
            // linked to the email:
            var email = error.email;
            // The provider's credential:
            var credential = error.credential;
            // In case of auth/account-exists-with-different-credential error,
            // you can fetch the providers using this:
            if (error.code === 'auth/account-exists-with-different-credential') {
              auth.fetchSignInMethodsForEmail(email).then(function(providers) {
                // The returned 'providers' is a list of the available providers
                // linked to the email address. Please refer to the guide for a more
                // complete explanation on how to recover from this error.
              });
            }
          });


  #### Parameters

  -

    ##### provider: [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)

    The provider to authenticate.
    The provider has to be an OAuth provider. Non-OAuth providers like [firebase.auth.EmailAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider) will throw an error.

  #### Returns Promise\<[UserCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth#usercredential)\>

### signInWithRedirect

- signInWithRedirect ( provider : [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider) ) : Promise \< void \>
- Authenticates a Firebase client using a full-page redirect flow. To handle
  the results and errors for this operation, refer to [firebase.auth.Auth.getRedirectResult](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#getredirectresult).

  #### Error Codes

  auth/auth-domain-config-required
  :   Thrown if authDomain configuration is not provided when calling
      firebase.initializeApp(). Check Firebase Console for instructions on
      determining and passing that field.

  auth/operation-not-supported-in-this-environment
  :   Thrown if this operation is not supported in the environment your
      application is running on. "location.protocol" must be http or https.

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

### signOut

- signOut ( ) : Promise \< void \>
- Signs out the current user.

  #### Returns Promise\<void\>

### updateCurrentUser

- updateCurrentUser ( user : [User](https://firebase.google.com/docs/reference/js/v8/firebase.User) \| null ) : Promise \< void \>
- Asynchronously sets the provided user as `currentUser` on the current Auth
  instance. A new instance copy of the user provided will be made and set as
  `currentUser`.

  This will trigger [firebase.auth.Auth.onAuthStateChanged](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#onauthstatechanged) and
  [firebase.auth.Auth.onIdTokenChanged](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#onidtokenchanged) listeners like other sign in
  methods.

  The operation fails with an error if the user to be updated belongs to a
  different Firebase project.

  #### Error Codes

  auth/invalid-user-token
  :   Thrown if the user to be updated belongs to a diffent Firebase
      project.

  auth/user-token-expired
  :   Thrown if the token of the user to be updated is expired.

  auth/null-user
  :   Thrown if the user to be updated is null.

  auth/tenant-id-mismatch
  :   Thrown if the provided user's tenant ID does not match the
      underlying Auth instance's configured tenant ID

  #### Parameters

  -

    ##### user: [User](https://firebase.google.com/docs/reference/js/v8/firebase.User) \| null

  #### Returns Promise\<void\>

### useDeviceLanguage

- useDeviceLanguage ( ) : void
- Sets the current language to the default device/browser preference.

  #### Returns void

### useEmulator

- useEmulator ( url : string ) : void
- Modify this Auth instance to communicate with the Firebase Auth emulator. This must be
  called synchronously immediately following the first call to `firebase.auth()`. Do not use
  with production credentials as emulator traffic is not encrypted.

  #### Parameters

  -

    ##### url: string

    The URL at which the emulator is running (eg, '<http://localhost:9099'>)

  #### Returns void

### verifyPasswordResetCode

- verifyPasswordResetCode ( code : string ) : Promise \< string \>
- Checks a password reset code sent to the user by email or other out-of-band
  mechanism.

  Returns the user's email address if valid.

  #### Error Codes

  auth/expired-action-code
  :   Thrown if the password reset code has expired.

  auth/invalid-action-code
  :   Thrown if the password reset code is invalid. This can happen if the code
      is malformed or has already been used.

  auth/user-disabled
  :   Thrown if the user corresponding to the given password reset code has
      been disabled.

  auth/user-not-found
  :   Thrown if there is no user corresponding to the password reset code. This
      may have happened if the user was deleted between when the code was
      issued and when this method was called.

  #### Parameters

  -

    ##### code: string

    A verification code sent to the user.

  #### Returns Promise\<string\>