# Source: https://firebase.google.com/docs/reference/node/firebase.auth.FacebookAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.FacebookAuthProvider.md.txt

# FacebookAuthProvider | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- FacebookAuthProvider

Facebook auth provider.

example
:

        // Sign in using a redirect.
        firebase.auth().getRedirectResult().then(function(result) {
          if (result.credential) {
            // This gives you a Google Access Token.
            var token = result.credential.accessToken;
          }
          var user = result.user;
        })
        // Start a sign in process for an unauthenticated user.
        var provider = new firebase.auth.FacebookAuthProvider();
        provider.addScope('user_birthday');
        firebase.auth().signInWithRedirect(provider);


example
:

        // Sign in using a popup.
        var provider = new firebase.auth.FacebookAuthProvider();
        provider.addScope('user_birthday');
        firebase.auth().signInWithPopup(provider).then(function(result) {
          // This gives you a Facebook Access Token.
          var token = result.credential.accessToken;
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

- [providerId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.FacebookAuthProvider#providerid)
- [FACEBOOK_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/js/v8/firebase.auth.FacebookAuthProvider#facebook_sign_in_method)
- [PROVIDER_ID](https://firebase.google.com/docs/reference/js/v8/firebase.auth.FacebookAuthProvider#provider_id)

### Methods

- [addScope](https://firebase.google.com/docs/reference/js/v8/firebase.auth.FacebookAuthProvider#addscope)
- [setCustomParameters](https://firebase.google.com/docs/reference/js/v8/firebase.auth.FacebookAuthProvider#setcustomparameters)
- [credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.FacebookAuthProvider#credential)

## Properties

### providerId

providerId: string
| Implementation of [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider).[providerId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider#providerid)
| Inherited from [FacebookAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.FacebookAuthProvider).[providerId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.FacebookAuthProvider#providerid)

### Static FACEBOOK_SIGN_IN_METHOD

FACEBOOK_SIGN_IN_METHOD: string  
This corresponds to the sign-in method identifier as returned in
[firebase.auth.Auth.fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#fetchsigninmethodsforemail).

### Static PROVIDER_ID

PROVIDER_ID: string

## Methods

### addScope

- addScope ( scope : string ) : [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)
-
  Inherited from [FacebookAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.FacebookAuthProvider).[addScope](https://firebase.google.com/docs/reference/js/v8/firebase.auth.FacebookAuthProvider#addscope)  

  #### Parameters

  -

    ##### scope: string

    Facebook OAuth scope.

  #### Returns [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)

  The provider instance itself.

### setCustomParameters

- setCustomParameters ( customOAuthParameters : Object ) : [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)
-
  Inherited from [FacebookAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.FacebookAuthProvider).[setCustomParameters](https://firebase.google.com/docs/reference/js/v8/firebase.auth.FacebookAuthProvider#setcustomparameters)  
  Sets the OAuth custom parameters to pass in a Facebook OAuth request for
  popup and redirect sign-in operations.
  Valid parameters include 'auth_type', 'display' and 'locale'.
  For a detailed list, check the
  [Facebook](https://goo.gl/pve4fo)
  documentation.
  Reserved required OAuth 2.0 parameters such as 'client_id', 'redirect_uri',
  'scope', 'response_type' and 'state' are not allowed and will be ignored.

  #### Parameters

  -

    ##### customOAuthParameters: Object

    The custom OAuth parameters to pass
    in the OAuth request.

  #### Returns [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)

  The provider instance itself.

### Static credential

- credential ( token : string ) : [OAuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthCredential)
-

  example
  :

          var cred = firebase.auth.FacebookAuthProvider.credential(
              // `event` from the Facebook auth.authResponseChange callback.
              event.authResponse.accessToken
          );


  #### Parameters

  -

    ##### token: string

    Facebook access token.

  #### Returns [OAuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthCredential)