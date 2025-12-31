# Source: https://firebase.google.com/docs/reference/node/firebase.auth.OAuthCredential.md.txt

# OAuthCredential | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [auth](https://firebase.google.com/docs/reference/node/firebase.auth).
- OAuthCredential

Interface that represents the OAuth credentials returned by an OAuth
provider. Implementations specify the details about each auth provider's
credential requirements.

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/node/firebase.auth.OAuthCredential#constructor)

### Properties

- [accessToken](https://firebase.google.com/docs/reference/node/firebase.auth.OAuthCredential#accesstoken)
- [idToken](https://firebase.google.com/docs/reference/node/firebase.auth.OAuthCredential#idtoken)
- [providerId](https://firebase.google.com/docs/reference/node/firebase.auth.OAuthCredential#providerid)
- [secret](https://firebase.google.com/docs/reference/node/firebase.auth.OAuthCredential#secret)
- [signInMethod](https://firebase.google.com/docs/reference/node/firebase.auth.OAuthCredential#signinmethod)

### Methods

- [toJSON](https://firebase.google.com/docs/reference/node/firebase.auth.OAuthCredential#tojson)
- [fromJSON](https://firebase.google.com/docs/reference/node/firebase.auth.OAuthCredential#fromjson)

## Constructors

### Private constructor

- new OAuthCredential ( ) : [OAuthCredential](https://firebase.google.com/docs/reference/node/firebase.auth.OAuthCredential)
-

  #### Returns [OAuthCredential](https://firebase.google.com/docs/reference/node/firebase.auth.OAuthCredential)

## Properties

### Optional accessToken

accessToken: string  
The OAuth access token associated with the credential if it belongs to
an OAuth provider, such as `facebook.com`, `twitter.com`, etc.

### Optional idToken

idToken: string  
The OAuth ID token associated with the credential if it belongs to an
OIDC provider, such as `google.com`.

### providerId

providerId: string
Inherited from [AuthCredential](https://firebase.google.com/docs/reference/node/firebase.auth.AuthCredential).[providerId](https://firebase.google.com/docs/reference/node/firebase.auth.AuthCredential#providerid)  
The authentication provider ID for the credential.
For example, 'facebook.com', or 'google.com'.

### Optional secret

secret: string  
The OAuth access token secret associated with the credential if it
belongs to an OAuth 1.0 provider, such as `twitter.com`.

### signInMethod

signInMethod: string
Inherited from [AuthCredential](https://firebase.google.com/docs/reference/node/firebase.auth.AuthCredential).[signInMethod](https://firebase.google.com/docs/reference/node/firebase.auth.AuthCredential#signinmethod)  
The authentication sign in method for the credential.
For example, 'password', or 'emailLink. This corresponds to the sign-in
method identifier as returned in
[firebase.auth.Auth.fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/node/firebase.auth.Auth#fetchsigninmethodsforemail).

## Methods

### toJSON

- toJSON ( ) : Object
-
  Inherited from [AuthCredential](https://firebase.google.com/docs/reference/node/firebase.auth.AuthCredential).[toJSON](https://firebase.google.com/docs/reference/node/firebase.auth.AuthCredential#tojson)  
  Returns a JSON-serializable representation of this object.

  #### Returns Object

### Static fromJSON

- fromJSON ( json : Object \| string ) : [AuthCredential](https://firebase.google.com/docs/reference/node/firebase.auth.AuthCredential) \| null
-
  Inherited from [AuthCredential](https://firebase.google.com/docs/reference/node/firebase.auth.AuthCredential).[fromJSON](https://firebase.google.com/docs/reference/node/firebase.auth.AuthCredential#fromjson)  
  Static method to deserialize a JSON representation of an object into an
  [firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/node/firebase.auth.AuthCredential). Input can be either Object or the
  stringified representation of the object. When string is provided,
  JSON.parse would be called first. If the JSON input does not represent
  an`AuthCredential`, null is returned.

  #### Parameters

  -

    ##### json: Object \| string

    The plain object representation of an
    AuthCredential.

  #### Returns [AuthCredential](https://firebase.google.com/docs/reference/node/firebase.auth.AuthCredential) \| null