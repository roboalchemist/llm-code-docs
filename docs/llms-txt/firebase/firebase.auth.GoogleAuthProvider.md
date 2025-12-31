# Source: https://firebase.google.com/docs/reference/node/firebase.auth.GoogleAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.GoogleAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.auth.GoogleAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.GoogleAuthProvider.md.txt

# GoogleAuthProvider | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- GoogleAuthProvider

Google auth provider.

example
:

        // Using a redirect.
        firebase.auth().getRedirectResult().then(function(result) {
          if (result.credential) {
            // This gives you a Google Access Token.
            var token = result.credential.accessToken;
          }
          var user = result.user;
        });

        // Start a sign in process for an unauthenticated user.
        var provider = new firebase.auth.GoogleAuthProvider();
        provider.addScope('profile');
        provider.addScope('email');
        firebase.auth().signInWithRedirect(provider);


example
:

        // Using a popup.
        var provider = new firebase.auth.GoogleAuthProvider();
        provider.addScope('profile');
        provider.addScope('email');
        firebase.auth().signInWithPopup(provider).then(function(result) {
         // This gives you a Google Access Token.
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

- [providerId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.GoogleAuthProvider#providerid)
- [GOOGLE_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/js/v8/firebase.auth.GoogleAuthProvider#google_sign_in_method)
- [PROVIDER_ID](https://firebase.google.com/docs/reference/js/v8/firebase.auth.GoogleAuthProvider#provider_id)

### Methods

- [addScope](https://firebase.google.com/docs/reference/js/v8/firebase.auth.GoogleAuthProvider#addscope)
- [setCustomParameters](https://firebase.google.com/docs/reference/js/v8/firebase.auth.GoogleAuthProvider#setcustomparameters)
- [credential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.GoogleAuthProvider#credential)

## Properties

### providerId

providerId: string
| Implementation of [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider).[providerId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider#providerid)
| Inherited from [GoogleAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.GoogleAuthProvider).[providerId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.GoogleAuthProvider#providerid)

### Static GOOGLE_SIGN_IN_METHOD

GOOGLE_SIGN_IN_METHOD: string  
This corresponds to the sign-in method identifier as returned in
[firebase.auth.Auth.fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#fetchsigninmethodsforemail).

### Static PROVIDER_ID

PROVIDER_ID: string

## Methods

### addScope

- addScope ( scope : string ) : [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)
-
  Inherited from [GoogleAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.GoogleAuthProvider).[addScope](https://firebase.google.com/docs/reference/js/v8/firebase.auth.GoogleAuthProvider#addscope)  

  #### Parameters

  -

    ##### scope: string

    Google OAuth scope.

  #### Returns [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)

  The provider instance itself.

### setCustomParameters

- setCustomParameters ( customOAuthParameters : Object ) : [AuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthProvider)
-
  Inherited from [GoogleAuthProvider](https://firebase.google.com/docs/reference/js/v8/firebase.auth.GoogleAuthProvider).[setCustomParameters](https://firebase.google.com/docs/reference/js/v8/firebase.auth.GoogleAuthProvider#setcustomparameters)  
  Sets the OAuth custom parameters to pass in a Google OAuth request for popup
  and redirect sign-in operations.
  Valid parameters include 'hd', 'hl', 'include_granted_scopes', 'login_hint'
  and 'prompt'.
  For a detailed list, check the
  [Google](https://goo.gl/Xo01Jm)
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

- credential ( idToken ? : string \| null , accessToken ? : string \| null ) : [OAuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthCredential)
- Creates a credential for Google. At least one of ID token and access token
  is required.

  example
  :

          // \`googleUser\` from the onsuccess Google Sign In callback.
          var credential = firebase.auth.GoogleAuthProvider.credential(
          googleUser.getAuthResponse().id_token);
          firebase.auth().signInWithCredential(credential)


  #### Parameters

  -

    ##### Optional idToken: string \| null

    Google ID token.
  -

    ##### Optional accessToken: string \| null

    Google access token.

  #### Returns [OAuthCredential](https://firebase.google.com/docs/reference/js/v8/firebase.auth.OAuthCredential)

The auth provider credential.