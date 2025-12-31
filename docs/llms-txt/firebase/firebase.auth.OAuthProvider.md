# Source: https://firebase.google.com/docs/reference/node/firebase.auth.OAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.auth.OAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthProvider.md.txt

# OAuthProvider | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- OAuthProvider

Generic OAuth provider.

example
:

        // Using a redirect.
        firebase.auth().getRedirectResult().then(function(result) {
          if (result.credential) {
            // This gives you the OAuth Access Token for that provider.
            var token = result.credential.accessToken;
          }
          var user = result.user;
        });

        // Start a sign in process for an unauthenticated user.
        var provider = new firebase.auth.OAuthProvider('google.com');
        provider.addScope('profile');
        provider.addScope('email');
        firebase.auth().signInWithRedirect(provider);


example
:

        // Using a popup.
        var provider = new firebase.auth.OAuthProvider('google.com');
        provider.addScope('profile');
        provider.addScope('email');
        firebase.auth().signInWithPopup(provider).then(function(result) {
         // This gives you the OAuth Access Token for that provider.
         var token = result.credential.accessToken;
         // The signed-in user info.
         var user = result.user;
        });


see

:   [firebase.auth.Auth.onAuthStateChanged](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#onauthstatechanged) to receive sign in state
    changes.

param

:   The associated provider ID, such as `github.com`.

### Implements

- [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthProvider#constructor)

### Properties

- [providerId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthProvider#providerid)

### Methods

- [addScope](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthProvider#addscope)
- [credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthProvider#credential)
- [setCustomParameters](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthProvider#setcustomparameters)

## Constructors

### constructor

- new OAuthProvider ( providerId : string ) : [OAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthProvider)
-

  #### Parameters

  -

    ##### providerId: string

  #### Returns [OAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthProvider)

## Properties

### providerId

providerId: string
| Implementation of [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider).[providerId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider#providerid)

## Methods

### addScope

- addScope ( scope : string ) : [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)
-

  #### Parameters

  -

    ##### scope: string

    Provider OAuth scope to add.

  #### Returns [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)

### credential

- credential ( optionsOrIdToken : [OAuthCredentialOptions](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthCredentialOptions) \| string \| null , accessToken ? : string ) : [OAuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthCredential)
- Creates a Firebase credential from a generic OAuth provider's access token or
  ID token. The raw nonce is required when an ID token with a nonce field is
  provided. The SHA-256 hash of the raw nonce must match the nonce field in
  the ID token.

  example
  :

          // `googleUser` from the onsuccess Google Sign In callback.
          // Initialize a generate OAuth provider with a `google.com` providerId.
          var provider = new firebase.auth.OAuthProvider('google.com');
          var credential = provider.credential({
            idToken: googleUser.getAuthResponse().id_token,
          });
          firebase.auth().signInWithCredential(credential)


  #### Parameters

  -

    ##### optionsOrIdToken: [OAuthCredentialOptions](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthCredentialOptions) \| string \| null

    Either the options object containing
    the ID token, access token and raw nonce or the ID token string.
  -

    ##### Optional accessToken: string

    The OAuth access token.

  #### Returns [OAuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthCredential)

### setCustomParameters

- setCustomParameters ( customOAuthParameters : Object ) : [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)
- Sets the OAuth custom parameters to pass in an OAuth request for popup
  and redirect sign-in operations.
  For a detailed list, check the
  reserved required OAuth 2.0 parameters such as `client_id`, `redirect_uri`,
  `scope`, `response_type` and `state` are not allowed and will be ignored.

  #### Parameters

  -

    ##### customOAuthParameters: Object

    The custom OAuth parameters to pass
    in the OAuth request.

  #### Returns [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)