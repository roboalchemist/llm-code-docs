# Source: https://firebase.google.com/docs/reference/node/firebase.auth.phoneauthcredential.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.phoneauthcredential.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.auth.phoneauthcredential.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.phoneauthcredential.md.txt

# PhoneAuthCredential | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- PhoneAuthCredential

Classes that represents the Phone Auth credentials returned by a
[firebase.auth.PhoneAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneAuthProvider).

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phoneauthcredential#constructor)

### Properties

- [providerId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phoneauthcredential#providerid)
- [signInMethod](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phoneauthcredential#signinmethod)

### Methods

- [toJSON](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phoneauthcredential#tojson)
- [fromJSON](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phoneauthcredential#fromjson)

## Constructors

### Private constructor

- new PhoneAuthCredential ( ) : [PhoneAuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phoneauthcredential)
-

  #### Returns [PhoneAuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phoneauthcredential)

## Properties

### providerId

providerId: string
Inherited from [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential).[providerId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential#providerid)  
The authentication provider ID for the credential.
For example, 'facebook.com', or 'google.com'.

### signInMethod

signInMethod: string
Inherited from [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential).[signInMethod](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential#signinmethod)  
The authentication sign in method for the credential.
For example, 'password', or 'emailLink. This corresponds to the sign-in
method identifier as returned in
[firebase.auth.Auth.fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#fetchsigninmethodsforemail).

## Methods

### toJSON

- toJSON ( ) : Object
-
  Inherited from [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential).[toJSON](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential#tojson)  
  Returns a JSON-serializable representation of this object.

  #### Returns Object

### Static fromJSON

- fromJSON ( json : Object \| string ) : [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential) \| null
-
  Inherited from [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential).[fromJSON](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential#fromjson)  
  Static method to deserialize a JSON representation of an object into an
  [firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential). Input can be either Object or the
  stringified representation of the object. When string is provided,
  JSON.parse would be called first. If the JSON input does not represent
  an`AuthCredential`, null is returned.

  #### Parameters

  -

    ##### json: Object \| string

    The plain object representation of an
    AuthCredential.

  #### Returns [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential) \| null