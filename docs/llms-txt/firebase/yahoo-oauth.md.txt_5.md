# Source: https://firebase.google.com/docs/auth/web/yahoo-oauth.md.txt

You can let your users authenticate with Firebase using OAuth providers like
Yahoo by integrating generic OAuth Login into your app using the Firebase SDK to
carry out the end to end sign-in flow.

## Before you begin

To sign in users using Yahoo accounts, you must first enable Yahoo as a sign-in
provider for your Firebase project:

1. [Add Firebase to your JavaScript project](https://firebase.google.com/docs/web/setup).
2. In the [Firebase console](https://console.firebase.google.com/), open the **Auth** section.
3. On the **Sign in method** tab, enable the **Yahoo** provider.
4. Add the **Client ID** and **Client Secret** from that provider's developer console to the provider configuration:
   1. To register a Yahoo OAuth client, follow the Yahoo developer
      documentation on [registering a web application with Yahoo](https://developer.yahoo.com/oauth2/guide/openid_connect/getting_started.html).

      Be sure to select the two OpenID Connect API permissions:
      `profile` and `email`.
   2. When registering apps with these providers, be sure to register the `*.firebaseapp.com` domain for your project as the redirect domain for your app.
5. Click **Save**.

## Handle the sign-in flow with the Firebase SDK

If you are building a web app, the easiest way to authenticate your users with
Firebase using their Yahoo accounts is to handle the entire sign-in flow
with the Firebase JavaScript SDK.

To handle the sign-in flow with the Firebase JavaScript SDK, follow these steps:

1. Create an instance of an **OAuthProvider** using the provider ID
   **yahoo.com**.

   ### Web

   ```javascript
   import { OAuthProvider } from "firebase/auth";

   const provider = new OAuthProvider('yahoo.com');
   ```

   ### Web

   ```javascript
   var provider = new firebase.auth.OAuthProvider('yahoo.com');
   ```
2. **Optional**: Specify additional custom OAuth parameters that you want to
   send with the OAuth request.

   ### Web

   ```javascript
   provider.setCustomParameters({
     // Prompt user to re-authenticate to Yahoo.
     prompt: 'login',
     // Localize to French.
     language: 'fr'
   });  
   ```

   ### Web

   ```javascript
   provider.setCustomParameters({
     // Prompt user to re-authenticate to Yahoo.
     prompt: 'login',
     // Localize to French.
     language: 'fr'
   });  
   ```

   For the parameters Yahoo supports, see the
   [Yahoo OAuth documentation](https://developer.yahoo.com/oauth2/guide/openid_connect/getting_started.html).
   Note that you can't pass Firebase-required parameters with
   `setCustomParameters()`. These parameters are **client_id** ,
   **redirect_uri** , **response_type** , **scope** and **state**.
3. **Optional** : Specify additional OAuth 2.0 scopes beyond `profile` and
   `email` that you want to request from the authentication provider. If your
   application requires access to private user data from Yahoo APIs, you'll
   need to request permissions to Yahoo APIs under **API Permissions** in the
   Yahoo developer console. Requested OAuth scopes must be exact matches to the
   preconfigured ones in the app's API permissions. For example if, read/write
   access is requested to user contacts and preconfigured in the app's API
   permissions, `sdct-w` has to be passed instead of the readonly OAuth scope
   `sdct-r`. Otherwise, the flow will fail and an error would be shown to the
   end user.

   ### Web

   ```javascript
   // Request access to Yahoo Mail API.
   provider.addScope('mail-r');
   // Request read/write access to user contacts.
   // This must be preconfigured in the app's API permissions.
   provider.addScope('sdct-w');
   ```

   ### Web

   ```javascript
   // Request access to Yahoo Mail API.
   provider.addScope('mail-r');
   // Request read/write access to user contacts.
   // This must be preconfigured in the app's API permissions.
   provider.addScope('sdct-w');
   ```

   To learn more, refer to the
   [Yahoo scopes documentation](https://developer.yahoo.com/oauth2/guide/yahoo_scopes/).
4. Authenticate with Firebase using the OAuth provider object. You can prompt
   your users to sign in with their Yahoo Accounts either by opening a
   pop-up window or by redirecting to the sign-in page. The redirect method is
   preferred on mobile devices.

   - To sign in with a pop-up window, call `signInWithPopup`:

     ### Web

     ```javascript
     import { getAuth, signInWithPopup, OAuthProvider } from "firebase/auth";

     const auth = getAuth();
     signInWithPopup(auth, provider)
       .then((result) => {
         // IdP data available in result.additionalUserInfo.profile
         // ...

         // Yahoo OAuth access token and ID token can be retrieved by calling:
         const credential = OAuthProvider.credentialFromResult(result);
         const accessToken = credential.accessToken;
         const idToken = credential.idToken;
       })
       .catch((error) => {
         // Handle error.
       });
     ```

     ### Web

     ```javascript
     firebase.auth().signInWithPopup(provider)
       .then((result) => {
         // IdP data available in result.additionalUserInfo.profile
         // ...

         /** @type {firebase.auth.OAuthCredential} */
         const credential = result.credential;

         // Yahoo OAuth access token and ID token can be retrieved by calling:
         var accessToken = credential.accessToken;
         var idToken = credential.idToken;
       })
       .catch((error) => {
         // Handle error.
       });
     ```
   - To sign in by redirecting to the sign-in page, call `signInWithRedirect`:


   <br />

   ```
     firebase.auth().signInWithRedirect(provider);
     
   ```

   <br />

   After the user completes sign-in and returns to the page, you can obtain
   the sign-in result by calling `getRedirectResult`.

   ### Web

   ```javascript
   import { getAuth, signInWithRedirect } from "firebase/auth";

   const auth = getAuth();
   signInWithRedirect(auth, provider);
   ```

   ### Web

   ```javascript
   firebase.auth().signInWithRedirect(provider);
   ```

   On successful completion, the OAuth ID token and access token associated
   with the provider can be retrieved from the `firebase.auth.UserCredential`
   object returned.

   Using the OAuth access token, you can call the
   [Yahoo API](https://developer.yahoo.com/oauth2/guide/apirequests/).

   For example, to get the basic profile information, the following REST API
   can be called:

   ```
   curl -i -H "Authorization: Bearer ACCESS_TOKEN" https://social.yahooapis.com/v1/user/YAHOO_USER_UID/profile?format=json
   ```

   Where `YAHOO_USER_UID` is the Yahoo user's ID which can be retrieved from
   the `firebase.auth().currentUser.providerData[0].uid` field or from
   `result.additionalUserInfo.profile`.
5. While the above examples focus on sign-in flows, you also have the
   ability to link a Yahoo provider to an existing user using
   `linkWithPopup`/`linkWithRedirect`. For example, you can link multiple
   providers to the same user allowing them to sign in with either.

   ### Web

   ```javascript
   import { getAuth, linkWithPopup, OAuthProvider } from "firebase/auth";

   const provider = new OAuthProvider('yahoo.com');
   const auth = getAuth();
   linkWithPopup(auth.currentUser, provider)
       .then((result) => {
         // Yahoo credential is linked to the current user.
         // IdP data available in result.additionalUserInfo.profile.

         // Get the OAuth access token and ID Token
         const credential = OAuthProvider.credentialFromResult(result);
         const accessToken = credential.accessToken;
         const idToken = credential.idToken;
       })
       .catch((error) => {
         // Handle error.
       });
   ```

   ### Web

   ```javascript
   var provider = new firebase.auth.OAuthProvider('yahoo.com');
   firebase.auth().currentUser.linkWithPopup(provider)
       .then((result) => {
         // Yahoo credential is linked to the current user.
         // IdP data available in result.additionalUserInfo.profile.
         // Yahoo OAuth access token can be retrieved by calling:
         // result.credential.accessToken
         // Yahoo OAuth ID token can be retrieved by calling:
         // result.credential.idToken
       })
       .catch((error) => {
         // Handle error.
       });
   ```
6. The same pattern can be used with
   `reauthenticateWithPopup`/`reauthenticateWithRedirect` which can be used to
   retrieve fresh credentials for sensitive operations that require recent
   login.

   ### Web

   ```javascript
   import { getAuth, reauthenticateWithPopup, OAuthProvider } from "firebase/auth";

   const provider = new OAuthProvider('yahoo.com');
   const auth = getAuth();
   reauthenticateWithPopup(auth.currentUser, provider)
       .then((result) => {
         // User is re-authenticated with fresh tokens minted and
         // should be able to perform sensitive operations like account
         // deletion and email or password update.
         // IdP data available in result.additionalUserInfo.profile.

         // Get the OAuth access token and ID Token
         const credential = OAuthProvider.credentialFromResult(result);
         const accessToken = credential.accessToken;
         const idToken = credential.idToken;
       })
       .catch((error) => {
         // Handle error.
       });
   ```

   ### Web

   ```javascript
   var provider = new firebase.auth.OAuthProvider('yahoo.com');
   firebase.auth().currentUser.reauthenticateWithPopup(provider)
       .then((result) => {
         // User is re-authenticated with fresh tokens minted and
         // should be able to perform sensitive operations like account
         // deletion and email or password update.
         // IdP data available in result.additionalUserInfo.profile.
         // Yahoo OAuth access token can be retrieved by calling:
         // result.credential.accessToken
         // Yahoo OAuth ID token can be retrieved by calling:
         // result.credential.idToken
       })
       .catch((error) => {
         // Handle error.
       });
   ```

## Handling account-exists-with-different-credential Errors

If you enabled the **One account per email address** setting in the [Firebase console](https://console.firebase.google.com/),
when a user tries to sign in a to a provider (such as Yahoo) with an email that already
exists for another Firebase user's provider (such as Google), the error
`auth/account-exists-with-different-credential` is thrown along with an
`AuthCredential` object (Yahoo credential). To complete the sign in to the
intended provider, the user has to sign first to the existing provider (Google) and then link to the
former `AuthCredential` (Yahoo credential).

### Popup mode

If you use `signInWithPopup`, you can handle
`auth/account-exists-with-different-credential` errors with code like the following
example:

```
import {
  getAuth,
  linkWithCredential,
  signInWithPopup,
  OAuthProvider,
} from "firebase/auth";

try {
  // Step 1: User tries to sign in using Yahoo.
  let result = await signInWithPopup(getAuth(), new OAuthProvider());
} catch (error) {
  // Step 2: User's email already exists.
  if (error.code === "auth/account-exists-with-different-credential") {
    // The pending Yahoo credential.
    let pendingCred = error.credential;

    // Step 3: Save the pending credential in temporary storage,

    // Step 4: Let the user know that they already have an account
    // but with a different provider, and let them choose another
    // sign-in method.
  }
}

// ...

try {
  // Step 5: Sign the user in using their chosen method.
  let result = await signInWithPopup(getAuth(), userSelectedProvider);

  // Step 6: Link to the Yahoo credential.
  // TODO: implement `retrievePendingCred` for your app.
  let pendingCred = retrievePendingCred();

  if (pendingCred !== null) {
    // As you have access to the pending credential, you can directly call the
    // link method.
    let user = await linkWithCredential(result.user, pendingCred);
  }

  // Step 7: Continue to app.
} catch (error) {
  // ...
}
```

### Redirect mode

This error is handled in a similar way in the redirect mode, with the difference that the pending
credential has to be cached between page redirects (for example, using session storage).

## Advanced: Handle the sign-in flow manually

Unlike other OAuth providers supported by Firebase such as Google, Facebook,
and Twitter, where sign-in can directly be achieved with OAuth access token
based credentials, Firebase Auth does not support the same capability for
providers such as Yahoo due to the inability of the Firebase
Auth server to verify the audience of Yahoo OAuth access tokens.
This is a critical security requirement and could expose applications and
websites to replay attacks where a Yahoo OAuth access token obtained for
one project (attacker) can be used to sign in to another project (victim).
Instead, Firebase Auth offers the ability to handle the entire OAuth flow and
the authorization code exchange using the OAuth client ID and secret
configured in the Firebase Console. As the authorization code can only be used
in conjunction with a specific client ID/secret, an authorization code
obtained for one project cannot be used with another.

If these providers are required to be used in unsupported environments, a
third party OAuth library and
[Firebase custom authentication](https://firebase.google.com/docs/auth/admin/create-custom-tokens)
would need to be used. The former is needed to authenticate with the provider
and the latter to exchange the provider's credential for a custom token.

## Authenticate with Firebase in a Chrome extension

If you are building a Chrome extension app, see the [Offscreen Documents guide](https://firebase.google.com/docs/auth/web/chrome-extension#use_offscreen_documents).

## Customizing the redirect domain for Yahoo sign-in

On project creation, Firebase will provision a unique subdomain for your project:
`https://my-app-12345.firebaseapp.com`.

This will also be used as the redirect mechanism for OAuth sign in. That domain would need to be
allowed for all supported OAuth providers. However, this means that users may see that
domain while signing in to Yahoo before redirecting back to the application:
**Continue to: https://my-app-12345.firebaseapp.com**.

To avoid displaying your subdomain, you can set up a custom domain with Firebase Hosting:

1. Follow steps 1 through 3 in [Set up your domain for Hosting](https://firebase.google.com/docs/hosting/custom-domain). When you verify your domain ownership, Hosting provisions an SSL certificate for your custom domain.
2. Add your custom domain to the list of authorized domains in the [Firebase console](https://console.firebase.google.com/): `auth.custom.domain.com`.
3. In the Yahoo developer console or OAuth setup page, whitelist the URL of the redirect page, which will be accessible on your custom domain: `https://auth.custom.domain.com/__/auth/handler`.
4. When you initialize the JavaScript library, specify your custom domain with the `authDomain` field:

   ```
   var config = {
     apiKey: '...',
     // Changed from 'PROJECT_ID.firebaseapp.com'.
     authDomain: 'auth.custom.domain.com',
     databaseURL: 'https://PROJECT_ID.firebaseio.com',
     projectId: 'PROJECT_ID',
     storageBucket: '`PROJECT_ID.firebasestorage.app`',
     messagingSenderId: 'SENDER_ID'
   };
   firebase.initializeApp(config);
   ```

## Next steps

After a user signs in for the first time, a new user account is created and
linked to the credentials---that is, the user name and password, phone
number, or auth provider information---the user signed in with. This new
account is stored as part of your Firebase project, and can be used to identify
a user across every app in your project, regardless of how the user signs in.

- In your apps, the recommended way to know the auth status of your user is to
  set an observer on the `Auth` object. You can then get the user's
  basic profile information from the `User` object. See
  [Manage Users](https://firebase.google.com/docs/auth/web/manage-users).

- In your Firebase Realtime Database and Cloud Storage
  [Security Rules](https://firebase.google.com/docs/database/security/user-security), you can
  get the signed-in user's unique user ID from the `auth` variable,
  and use it to control what data a user can access.

You can allow users to sign in to your app using multiple authentication
providers by [linking auth provider credentials to an
existing user account.](https://firebase.google.com/docs/auth/web/account-linking)

To sign out a user, call [`signOut`](https://firebase.google.com/docs/reference/js/auth#signout):

### Web

```javascript
import { getAuth, signOut } from "firebase/auth";

const auth = getAuth();
signOut(auth).then(() => {
  // Sign-out successful.
}).catch((error) => {
  // An error happened.
});
```

### Web

```javascript
firebase.auth().signOut().then(() => {
  // Sign-out successful.
}).catch((error) => {
  // An error happened.
});
```