# Source: https://firebase.google.com/docs/reference/node/firebase.auth.EmailAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider.md.txt

# EmailAuthProvider | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- EmailAuthProvider

Email and password auth provider implementation.

To authenticate: [firebase.auth.Auth.createUserWithEmailAndPassword](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#createuserwithemailandpassword)
and [firebase.auth.Auth.signInWithEmailAndPassword](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signinwithemailandpassword).

### Implements

- [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)

## Index

### Properties

- [providerId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider#providerid)
- [EMAIL_LINK_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider#email_link_sign_in_method)
- [EMAIL_PASSWORD_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider#email_password_sign_in_method)
- [PROVIDER_ID](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider#provider_id)

### Methods

- [credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider#credential)
- [credentialWithLink](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider#credentialwithlink)

## Properties

### providerId

providerId: string
| Implementation of [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider).[providerId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider#providerid)
| Inherited from [EmailAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider).[providerId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmailAuthProvider#providerid)

### Static EMAIL_LINK_SIGN_IN_METHOD

EMAIL_LINK_SIGN_IN_METHOD: string  
This corresponds to the sign-in method identifier as returned in
[firebase.auth.Auth.fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#fetchsigninmethodsforemail).

### Static EMAIL_PASSWORD_SIGN_IN_METHOD

EMAIL_PASSWORD_SIGN_IN_METHOD: string  
This corresponds to the sign-in method identifier as returned in
[firebase.auth.Auth.fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#fetchsigninmethodsforemail).

### Static PROVIDER_ID

PROVIDER_ID: string

## Methods

### Static credential

- credential ( email : string , password : string ) : [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential)
-

  example
  :

          var cred = firebase.auth.EmailAuthProvider.credential(
              email,
              password
          );


  #### Parameters

  -

    ##### email: string

    Email address.
  -

    ##### password: string

    User account password.

  #### Returns [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential)

  The auth provider credential.

### Static credentialWithLink

- credentialWithLink ( email : string , emailLink : string ) : [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential)
- Initialize an `EmailAuthProvider` credential using an email and an email link
  after a sign in with email link operation.

  example
  :

          var cred = firebase.auth.EmailAuthProvider.credentialWithLink(
              email,
              emailLink
          );


  #### Parameters

  -

    ##### email: string

    Email address.
  -

    ##### emailLink: string

    Sign-in email link.

  #### Returns [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential)

The auth provider credential.