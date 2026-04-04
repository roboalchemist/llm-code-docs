# Source: https://firebase.google.com/docs/auth/web/openid-connect.md.txt

If you've upgraded to Firebase Authentication with Identity Platform, you can authenticate your users with
Firebase using the OpenID Connect (OIDC) compliant provider of your choice. This
makes it possible to use identity providers not natively supported by Firebase.

## Before you begin

To sign in users using an OIDC provider, you must first collect some information
from the provider:

- **Client ID** : A string unique to the provider that identifies your app. Your
  provider might assign you a different client ID for each platform you support.
  This is one of the values of the `aud` claim in ID tokens issued by your
  provider.

- **Client secret** : A secret string that the provider uses to confirm ownership
  of a client ID. For every client ID, you will need a matching client secret.
  (This value is required only if you're using the *auth code flow*, which is
  strongly recommended.)

- **Issuer** : A string that identifies your provider. This value must be a URL
  that, when appended with `/.well-known/openid-configuration`, is the location
  of the provider's OIDC discovery document. For example, if the issuer is
  `https://auth.example.com`, the discovery document must be available at
  `https://auth.example.com/.well-known/openid-configuration`.

After you have the above information, enable OpenID Connect as a sign-in
provider for your Firebase project:

1. [Add Firebase to your JavaScript project](https://firebase.google.com/docs/web/setup).

2. If you haven't upgraded to Firebase Authentication with Identity Platform, do so. OpenID Connect authentication
   is only available in upgraded projects.

3. On the [**Sign-in providers**](https://console.firebase.google.com/project/_/authentication/providers)
   page of the Firebase console, click **Add new provider** , and then click
   **OpenID Connect**.

4. Select whether you will be using the *authorization code flow* or the
   *implicit grant flow*.

   **You should use always the code flow if your provider supports it**. The
   implicit flow is less secure and using it is strongly discouraged.
5. Give a name to this provider. Note the provider ID that's generated:
   something like `oidc.example-provider`. You'll need this ID when you add
   sign-in code to your app.

6. Specify your client ID and client secret, and your provider's issuer string.
   These values must exactly match the values your provider assigned to you.

7. Save your changes.

## Handle the sign-in flow with the Firebase SDK

The easiest way to authenticate your users with Firebase using your OIDC
provider is to handle the entire sign-in flow with the Firebase SDK.

To handle the sign-in flow with the Firebase JavaScript SDK, follow these
steps:

1. Create an instance of an `OAuthProvider` using the provider ID you got in
   the Firebase console.

   ### Web

       import { OAuthProvider } from "firebase/auth";

       const provider = new OAuthProvider('oidc.example-provider');

   ### Web

       var provider = new firebase.auth.OAuthProvider('oidc.example-provider');

2. **Optional**: Specify additional custom OAuth parameters that you want to
   send with the OAuth request.

   ### Web

       provider.setCustomParameters({
         // Target specific email with login hint.
         login_hint: 'user@example.com'
       });

   ### Web

       provider.setCustomParameters({
         // Target specific email with login hint.
         login_hint: 'user@example.com'
       });

   Check with your provider for the parameters it supports.
   Note that you can't pass Firebase-required parameters with
   `setCustomParameters`. These parameters are `client_id`,
   `response_type`, `redirect_uri`, `state`, `scope` and
   `response_mode`.
3. **Optional**: Specify additional OAuth 2.0 scopes beyond basic profile that
   you want to request from the authentication provider.

   ### Web

       provider.addScope('mail.read');
       provider.addScope('calendars.read');

   ### Web

       provider.addScope('mail.read');
       provider.addScope('calendars.read');

   Check with your provider for the scopes it supports.
4. Authenticate with Firebase using the OAuth provider object.

   You can either redirect the user to the provider's sign-in page or open the
   sign-in page in a pop-up browser window.

   **Redirect flow**

   Redirect to the provider sign-in page by calling `signInWithRedirect()`:

   ### Web

       import { getAuth, signInWithRedirect } from "firebase/auth";

       const auth = getAuth();
       signInWithRedirect(auth, provider);

   ### Web

       firebase.auth().signInWithRedirect(provider);

   After the user completes sign-in and returns to your app, you can obtain the
   sign-in result by calling `getRedirectResult()`.

   ### Web

       import { getAuth, getRedirectResult, OAuthProvider } from "firebase/auth";

       const auth = getAuth();
       getRedirectResult(auth)
         .then((result) => {
           // User is signed in.
           // IdP data available in result.additionalUserInfo.profile.

           // Get the OAuth access token and ID Token
           const credential = OAuthProvider.credentialFromResult(result);
           const accessToken = credential.accessToken;
           const idToken = credential.idToken;
         })
         .catch((error) => {
           // Handle error.
         });

   ### Web

       firebase.auth().getRedirectResult()
         .then((result) => {
           // IdP data available in result.additionalUserInfo.profile.
           // ...

           /** @type {firebase.auth.OAuthCredential} */
           var credential = result.credential;

           // OAuth access and id tokens can also be retrieved:
           var accessToken = credential.accessToken;
           var idToken = credential.idToken;
         })
         .catch((error) => {
           // Handle error.
         });

   **Pop-up flow**

   ### Web

       import { getAuth, signInWithPopup, OAuthProvider } from "firebase/auth";

       const auth = getAuth();
       signInWithPopup(auth, provider)
         .then((result) => {
           // User is signed in.
           // IdP data available using getAdditionalUserInfo(result)

           // Get the OAuth access token and ID Token
           const credential = OAuthProvider.credentialFromResult(result);
           const accessToken = credential.accessToken;
           const idToken = credential.idToken;
         })
         .catch((error) => {
           // Handle error.
         });

   ### Web

       firebase.auth().signInWithPopup(provider)
         .then((result) => {
           // IdP data available in result.additionalUserInfo.profile.
           // ...

           /** @type {firebase.auth.OAuthCredential} */
           var credential = result.credential;

           // OAuth access and id tokens can also be retrieved:
           var accessToken = credential.accessToken;
           var idToken = credential.idToken;
         })
         .catch((error) => {
           // Handle error.
         });

5. While the above examples focus on sign-in flows, you can use the same
   pattern to link an OIDC provider to an existing user using
   `linkWithRedirect()` and `linkWithPopup()`, and re-authenticate a user with
   `reauthenticateWithRedirect()` and `reauthenticateWithPopup()`, which can be
   used to retrieve fresh credentials for sensitive operations that require
   recent login.

## Handle the sign-in flow manually

If you've already implemented the OpenID Connect sign-in flow in your app, you
can use the ID token directly to authenticate with Firebase:

### Web

    import { getAuth, signInWithCredential, OAuthProvider } from "firebase/auth";

    const provider = new OAuthProvider("oidc.example-provider");
    const credential = provider.credential({
        idToken: idToken,
    });
    signInWithCredential(getAuth(), credential)
        .then((result) => {
            // User is signed in.
            // IdP data available in result.additionalUserInfo.profile.

            // Get the OAuth access token and ID Token
            const credential = OAuthProvider.credentialFromResult(result);
            const accessToken = credential.accessToken;
            const idToken = credential.idToken;
        })
        .catch((error) => {
            // Handle error.
        });

### Web

    const provider = new OAuthProvider("oidc.example-provider");
    const credential = provider.credential({
        idToken: idToken,
    });
    firebase.auth().signInWithCredential(credential)
        .then((result) => {
            // User is signed in.
            // IdP data available in result.additionalUserInfo.profile.

            // Get the OAuth access token and ID Token
            const credential = OAuthProvider.credentialFromResult(result);
            const accessToken = credential.accessToken;
            const idToken = credential.idToken;
        })
        .catch((error) => {
            // Handle error.
        });