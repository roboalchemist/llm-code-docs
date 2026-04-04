# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.GithubAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.auth.GithubAuthProvider.md.txt

# GithubAuthProvider | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [auth](https://firebase.google.com/docs/reference/node/firebase.auth).
- GithubAuthProvider

GitHub auth provider.

GitHub requires an OAuth 2.0 redirect, so you can either handle the redirect
directly, or use the signInWithPopup handler:

example
:

        // Using a redirect.
        firebase.auth().getRedirectResult().then(function(result) {
          if (result.credential) {
            // This gives you a GitHub Access Token.
            var token = result.credential.accessToken;
          }
          var user = result.user;
        }).catch(function(error) {
          // Handle Errors here.
          var errorCode = error.code;
          var errorMessage = error.message;
          // The email of the user's account used.
          var email = error.email;
          // The firebase.auth.AuthCredential type that was used.
          var credential = error.credential;
          if (errorCode === 'auth/account-exists-with-different-credential') {
            alert('You have signed up with a different provider for that email.');
            // Handle linking here if your app allows it.
          } else {
            console.error(error);
          }
        });

        // Start a sign in process for an unauthenticated user.
        var provider = new firebase.auth.GithubAuthProvider();
        provider.addScope('repo');
        firebase.auth().signInWithRedirect(provider);


example
:

        // With popup.
        var provider = new firebase.auth.GithubAuthProvider();
         provider.addScope('repo');
         firebase.auth().signInWithPopup(provider).then(function(result) {
           // This gives you a GitHub Access Token.
           var token = result.credential.accessToken;
           // The signed-in user info.
           var user = result.user;
         }).catch(function(error) {
           // Handle Errors here.
           var errorCode = error.code;
           var errorMessage = error.message;
           // The email of the user's account used.
           var email = error.email;
           // The firebase.auth.AuthCredential type that was used.
           var credential = error.credential;
           if (errorCode === 'auth/account-exists-with-different-credential') {
             alert('You have signed up with a different provider for that email.');
             // Handle linking here if your app allows it.
           } else {
             console.error(error);
           }
         });


see

:   [firebase.auth.Auth.onAuthStateChanged](https://firebase.google.com/docs/reference/node/firebase.auth.Auth#onauthstatechanged) to receive sign in state
    changes.

### Implements

- [AuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.AuthProvider)

## Index

### Properties

- [providerId](https://firebase.google.com/docs/reference/node/firebase.auth.GithubAuthProvider#providerid)
- [GITHUB_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/node/firebase.auth.GithubAuthProvider#github_sign_in_method)
- [PROVIDER_ID](https://firebase.google.com/docs/reference/node/firebase.auth.GithubAuthProvider#provider_id)

### Methods

- [addScope](https://firebase.google.com/docs/reference/node/firebase.auth.GithubAuthProvider#addscope)
- [setCustomParameters](https://firebase.google.com/docs/reference/node/firebase.auth.GithubAuthProvider#setcustomparameters)
- [credential](https://firebase.google.com/docs/reference/node/firebase.auth.GithubAuthProvider#credential)

## Properties

### providerId

providerId: string
| Implementation of [AuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.AuthProvider).[providerId](https://firebase.google.com/docs/reference/node/firebase.auth.AuthProvider#providerid)
| Inherited from [GithubAuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.GithubAuthProvider).[providerId](https://firebase.google.com/docs/reference/node/firebase.auth.GithubAuthProvider#providerid)

### Static GITHUB_SIGN_IN_METHOD

GITHUB_SIGN_IN_METHOD: string  
This corresponds to the sign-in method identifier as returned in
[firebase.auth.Auth.fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/node/firebase.auth.Auth#fetchsigninmethodsforemail).

### Static PROVIDER_ID

PROVIDER_ID: string

## Methods

### addScope

- addScope ( scope : string ) : [AuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.AuthProvider)
-
  Inherited from [GithubAuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.GithubAuthProvider).[addScope](https://firebase.google.com/docs/reference/node/firebase.auth.GithubAuthProvider#addscope)  

  #### Parameters

  -

    ##### scope: string

    Github OAuth scope.

  #### Returns [AuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.AuthProvider)

  The provider instance itself.

### setCustomParameters

- setCustomParameters ( customOAuthParameters : Object ) : [AuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.AuthProvider)
-
  Inherited from [GithubAuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.GithubAuthProvider).[setCustomParameters](https://firebase.google.com/docs/reference/node/firebase.auth.GithubAuthProvider#setcustomparameters)  
  Sets the OAuth custom parameters to pass in a GitHub OAuth request for popup
  and redirect sign-in operations.
  Valid parameters include 'allow_signup'.
  For a detailed list, check the
  [GitHub](https://developer.github.com/v3/oauth/) documentation.
  Reserved required OAuth 2.0 parameters such as 'client_id', 'redirect_uri',
  'scope', 'response_type' and 'state' are not allowed and will be ignored.

  #### Parameters

  -

    ##### customOAuthParameters: Object

    The custom OAuth parameters to pass
    in the OAuth request.

  #### Returns [AuthProvider](https://firebase.google.com/docs/reference/node/firebase.auth.AuthProvider)

  The provider instance itself.

### Static credential

- credential ( token : string ) : [OAuthCredential](https://firebase.google.com/docs/reference/node/firebase.auth.OAuthCredential)
-

  example
  :

          var cred = firebase.auth.GithubAuthProvider.credential(
              // `event` from the Github auth.authResponseChange callback.
              event.authResponse.accessToken
          );


  #### Parameters

  -

    ##### token: string

    Github access token.

  #### Returns [OAuthCredential](https://firebase.google.com/docs/reference/node/firebase.auth.OAuthCredential)

The auth provider credential.