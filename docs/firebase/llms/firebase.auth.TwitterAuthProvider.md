# Source: https://firebase.google.com/docs/reference/node/firebase.auth.TwitterAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.TwitterAuthProvider.md.txt

# TwitterAuthProvider | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- TwitterAuthProvider

Twitter auth provider.

example
:

        // Using a redirect.
        firebase.auth().getRedirectResult().then(function(result) {
          if (result.credential) {
            // For accessing the Twitter API.
            var token = result.credential.accessToken;
            var secret = result.credential.secret;
          }
          var user = result.user;
        });

        // Start a sign in process for an unauthenticated user.
        var provider = new firebase.auth.TwitterAuthProvider();
        firebase.auth().signInWithRedirect(provider);


example
:

        // Using a popup.
        var provider = new firebase.auth.TwitterAuthProvider();
        firebase.auth().signInWithPopup(provider).then(function(result) {
          // For accessing the Twitter API.
          var token = result.credential.accessToken;
          var secret = result.credential.secret;
          // The signed-in user info.
          var user = result.user;
        });


see

:   [firebase.auth.Auth.onAuthStateChanged](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#onauthstatechanged) to receive sign in state
    changes.

### Implements

- [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)

## Index

### Properties

- [providerId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.TwitterAuthProvider#providerid)
- [PROVIDER_ID](https://firebase.google.com/docs/reference/js/v8/firebase.auth.TwitterAuthProvider#provider_id)
- [TWITTER_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/js/v8/firebase.auth.TwitterAuthProvider#twitter_sign_in_method)

### Methods

- [setCustomParameters](https://firebase.google.com/docs/reference/js/v8/firebase.auth.TwitterAuthProvider#setcustomparameters)
- [credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.TwitterAuthProvider#credential)

## Properties

### providerId

providerId: string
| Implementation of [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider).[providerId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider#providerid)
| Inherited from [TwitterAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.TwitterAuthProvider).[providerId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.TwitterAuthProvider#providerid)

### Static PROVIDER_ID

PROVIDER_ID: string

### Static TWITTER_SIGN_IN_METHOD

TWITTER_SIGN_IN_METHOD: string  
This corresponds to the sign-in method identifier as returned in
[firebase.auth.Auth.fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#fetchsigninmethodsforemail).

## Methods

### setCustomParameters

- setCustomParameters ( customOAuthParameters : Object ) : [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)
-
  Inherited from [TwitterAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.TwitterAuthProvider).[setCustomParameters](https://firebase.google.com/docs/reference/js/v8/firebase.auth.TwitterAuthProvider#setcustomparameters)  
  Sets the OAuth custom parameters to pass in a Twitter OAuth request for popup
  and redirect sign-in operations.
  Valid parameters include 'lang'.
  Reserved required OAuth 1.0 parameters such as 'oauth_consumer_key',
  'oauth_token', 'oauth_signature', etc are not allowed and will be ignored.

  #### Parameters

  -

    ##### customOAuthParameters: Object

    The custom OAuth parameters to pass
    in the OAuth request.

  #### Returns [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)

  The provider instance itself.

### Static credential

- credential ( token : string , secret : string ) : [OAuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthCredential)
-

  #### Parameters

  -

    ##### token: string

    Twitter access token.
  -

    ##### secret: string

    Twitter secret.

  #### Returns [OAuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthCredential)

The auth provider credential.