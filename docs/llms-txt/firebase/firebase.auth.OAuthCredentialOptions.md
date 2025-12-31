# Source: https://firebase.google.com/docs/reference/node/firebase.auth.OAuthCredentialOptions.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthCredentialOptions.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.auth.OAuthCredentialOptions.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthCredentialOptions.md.txt

# OAuthCredentialOptions | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- OAuthCredentialOptions

Defines the options for initializing an
[firebase.auth.OAuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthCredential). For ID tokens with nonce claim,
the raw nonce has to also be provided.

## Index

### Properties

- [accessToken](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthCredentialOptions#accesstoken)
- [idToken](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthCredentialOptions#idtoken)
- [rawNonce](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthCredentialOptions#rawnonce)

## Properties

### Optional accessToken

accessToken: string  
The OAuth access token used to initialize the OAuthCredential.

### Optional idToken

idToken: string  
The OAuth ID token used to initialize the OAuthCredential.

### Optional rawNonce

rawNonce: string  
The raw nonce associated with the ID token. It is required when an ID token
with a nonce field is provided. The SHA-256 hash of the raw nonce must match
the nonce field in the ID token.