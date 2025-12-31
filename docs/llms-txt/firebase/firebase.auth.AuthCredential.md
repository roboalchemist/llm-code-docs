# Source: https://firebase.google.com/docs/reference/node/firebase.auth.AuthCredential.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.auth.AuthCredential.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential.md.txt

# AuthCredential | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- AuthCredential

Interface that represents the credentials returned by an auth provider.
Implementations specify the details about each auth provider's credential
requirements.

## Index

### Properties

- [providerId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential#providerid)
- [signInMethod](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential#signinmethod)

### Methods

- [toJSON](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential#tojson)
- [fromJSON](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential#fromjson)

## Properties

### providerId

providerId: string  
The authentication provider ID for the credential.
For example, 'facebook.com', or 'google.com'.

### signInMethod

signInMethod: string  
The authentication sign in method for the credential.
For example, 'password', or 'emailLink. This corresponds to the sign-in
method identifier as returned in
[firebase.auth.Auth.fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#fetchsigninmethodsforemail).

## Methods

### toJSON

- toJSON ( ) : Object
- Returns a JSON-serializable representation of this object.

  #### Returns Object

### Static fromJSON

- fromJSON ( json : Object \| string ) : [AuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthCredential) \| null
- Static method to deserialize a JSON representation of an object into an
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