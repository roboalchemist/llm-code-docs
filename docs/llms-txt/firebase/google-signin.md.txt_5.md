# Source: https://firebase.google.com/docs/auth/web/google-signin.md.txt

You can let your users authenticate with Firebase using their Google Accounts.
You can either use the Firebase SDK to carry out the Google sign-in flow, or
carry out the sign-in flow manually using the Sign In With Google library and
passing the resulting ID token to Firebase.

## Before you begin

1. [Add Firebase to your JavaScript project](https://firebase.google.com/docs/web/setup).
2. Enable Google as a sign-in method in the Firebase console:
   1. In the [Firebase console](https://console.firebase.google.com/), open the **Auth** section.
   2. On the **Sign in method** tab, enable the **Google** sign-in method and click **Save**.

## Handle the sign-in flow with the Firebase SDK

If you are building a web app, the easiest way to authenticate your users
with Firebase using their Google Accounts is to handle the sign-in flow with
the Firebase JavaScript SDK. (If you want to authenticate a user in Node.js
or other non-browser environment, you must handle the sign-in flow manually.)

To handle the sign-in flow with the Firebase JavaScript SDK, follow these
steps:

1. Create an instance of the Google provider object:

   ### Web

   ```javascript
   import { GoogleAuthProvider } from "firebase/auth";

   const provider = new GoogleAuthProvider();
   ```

   ### Web

   ```javascript
   var provider = new firebase.auth.GoogleAuthProvider();
   ```
2. **Optional** : Specify additional OAuth 2.0 scopes that you want to request from the authentication provider. To add a scope, call `addScope`. For example:

   ### Web

   ```javascript
   provider.addScope('https://www.googleapis.com/auth/contacts.readonly');
   ```

   ### Web

   ```javascript
   provider.addScope('https://www.googleapis.com/auth/contacts.readonly');
   ```
   See the [authentication provider
   documentation](https://developers.google.com/identity/protocols/googlescopes).
3. **Optional** : To localize the provider's OAuth flow to the user's preferred language without explicitly passing the relevant custom OAuth parameters, update the language code on the Auth instance before starting the OAuth flow. For example:

   ### Web

   ```javascript
   import { getAuth } from "firebase/auth";

   const auth = getAuth();
   auth.languageCode = 'it';
   // To apply the default browser preference instead of explicitly setting it.
   // auth.useDeviceLanguage();https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/auth-next/index/auth_set_language_code.js#L8-L13
   ```

   ### Web

   ```javascript
   firebase.auth().languageCode = 'it';
   // To apply the default browser preference instead of explicitly setting it.
   // firebase.auth().useDeviceLanguage();https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/auth/index.js#L73-L75
   ```
4. **Optional** : Specify additional custom OAuth provider parameters that you want to send with the OAuth request. To add a custom parameter, call `setCustomParameters` on the initialized provider with an object containing the key as specified by the OAuth provider documentation and the corresponding value. For example:

   ### Web

   ```javascript
   provider.setCustomParameters({
     'login_hint': 'user@example.com'
   });
   ```

   ### Web

   ```javascript
   provider.setCustomParameters({
     'login_hint': 'user@example.com'
   });
   ```
   Reserved required OAuth parameters are not allowed and will be ignored. See the [authentication provider reference](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#setCustomParameters) for more details.
5. Authenticate with Firebase using the Google provider object. You can prompt your users to sign in with their Google Accounts either by opening a pop-up window or by redirecting to the sign-in page. The redirect method is preferred on mobile devices.
   - To sign in with a pop-up window, call `signInWithPopup`:

     ### Web

     ```javascript
     import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";

     const auth = getAuth();
     signInWithPopup(auth, provider)
       .then((result) => {
         // This gives you a Google Access Token. You can use it to access the Google API.
         const credential = GoogleAuthProvider.credentialFromResult(result);
         const token = credential.accessToken;
         // The signed-in user info.
         const user = result.user;
         // IdP data available using getAdditionalUserInfo(result)
         // ...
       }).catch((error) => {
         // Handle Errors here.
         const errorCode = error.code;
         const errorMessage = error.message;
         // The email of the user's account used.
         const email = error.customData.email;
         // The AuthCredential type that was used.
         const credential = GoogleAuthProvider.credentialFromError(error);
         // ...
       });
     ```

     ### Web

     ```javascript
     firebase.auth()
       .signInWithPopup(provider)
       .then((result) => {
         /** @type {firebase.auth.OAuthCredential} */
         var credential = result.credential;

         // This gives you a Google Access Token. You can use it to access the Google API.
         var token = credential.accessToken;
         // The signed-in user info.
         var user = result.user;
         // IdP data available in result.additionalUserInfo.profile.
           // ...
       }).catch((error) => {
         // Handle Errors here.
         var errorCode = error.code;
         var errorMessage = error.message;
         // The email of the user's account used.
         var email = error.email;
         // The firebase.auth.AuthCredential type that was used.
         var credential = error.credential;
         // ...
       });
     ```
     Also notice that you can retrieve the Google provider's OAuth token which can be used to fetch additional data using the Google APIs.


     This is also where you can catch and handle errors. For a list of error codes have a look at the [Auth Reference Docs](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signInWithPopup).
   - To sign in by redirecting to the sign-in page, call `signInWithRedirect`: Follow the [best practices](https://firebase.google.com/docs/auth/web/redirect-best-practices) when using \`signInWithRedirect\`.

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
     Then, you can also retrieve the Google provider's OAuth token by calling `getRedirectResult` when your page loads:

     ### Web

     ```javascript
     import { getAuth, getRedirectResult, GoogleAuthProvider } from "firebase/auth";

     const auth = getAuth();
     getRedirectResult(auth)
       .then((result) => {
         // This gives you a Google Access Token. You can use it to access Google APIs.
         const credential = GoogleAuthProvider.credentialFromResult(result);
         const token = credential.accessToken;

         // The signed-in user info.
         const user = result.user;
         // IdP data available using getAdditionalUserInfo(result)
         // ...
       }).catch((error) => {
         // Handle Errors here.
         const errorCode = error.code;
         const errorMessage = error.message;
         // The email of the user's account used.
         const email = error.customData.email;
         // The AuthCredential type that was used.
         const credential = GoogleAuthProvider.credentialFromError(error);
         // ...
       });
     ```

     ### Web

     ```javascript
     firebase.auth()
       .getRedirectResult()
       .then((result) => {
         if (result.credential) {
           /** @type {firebase.auth.OAuthCredential} */
           var credential = result.credential;

           // This gives you a Google Access Token. You can use it to access the Google API.
           var token = credential.accessToken;
           // ...
         }
         // The signed-in user info.
         var user = result.user;
         // IdP data available in result.additionalUserInfo.profile.
           // ...
       }).catch((error) => {
         // Handle Errors here.
         var errorCode = error.code;
         var errorMessage = error.message;
         // The email of the user's account used.
         var email = error.email;
         // The firebase.auth.AuthCredential type that was used.
         var credential = error.credential;
         // ...
       });
     ```
     This is also where you can catch and handle errors. For a list of error codes have a look at the [Auth Reference Docs](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#getRedirectResult).

## Handling account-exists-with-different-credential Errors

> [!NOTE]
> Google serves as both an email and social identity provider. Email IDPs are authoritative for all email addresses related to their hosted email domain while social IDPs assert email identities based having done a one time confirmation of the email address. A user logging in with Google will never cause this error when their account is hosted at Google even if they signed up for their account with a password or a social IDP.

If you enabled the **One account per email address** setting in the [Firebase console](https://console.firebase.google.com/),
when a user tries to sign in a to a provider (such as Google) with an email that already
exists for another Firebase user's provider (such as Facebook), the error
`auth/account-exists-with-different-credential` is thrown along with an
`AuthCredential` object (Google ID token). To complete the sign in to the
intended provider, the user has to sign first to the existing provider (Facebook) and then link to the
former `AuthCredential` (Google ID token).

### Popup mode

If you use `signInWithPopup`, you can handle
`auth/account-exists-with-different-credential` errors with code like the following
example:

```
import {
  getAuth,
  linkWithCredential,
  signInWithPopup,
  GoogleAuthProvider,
} from "firebase/auth";

try {
  // Step 1: User tries to sign in using Google.
  let result = await signInWithPopup(getAuth(), new GoogleAuthProvider());
} catch (error) {
  // Step 2: User's email already exists.
  if (error.code === "auth/account-exists-with-different-credential") {
    // The pending Google credential.
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

  // Step 6: Link to the Google credential.
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

You can also authenticate with Firebase using a Google Account by handling
the sign-in flow with the Sign In With Google library:

1. Integrate Sign In With Google into your app by following the [integration guide](https://developers.google.com/identity/gsi/web/guides/display-button#javascript). Be sure to configure Google Sign-In with the Google Client ID generated for your Firebase project. You can find your project's Google Client ID in your Project's Developers Console [Credentials page](https://console.developers.google.com/apis/credentials?project=_).
2. In the sign-in result callback, exchange the ID token from the Google auth response for a Firebase credential and use it to authenticate with Firebase:

   ```
   function handleCredentialResponse(response) {
     // Build Firebase credential with the Google ID token.
     const idToken = response.credential;
     const credential = GoogleAuthProvider.credential(idToken);

     // Sign in with credential from the Google user.
     signInWithCredential(auth, credential).catch((error) => {
       // Handle Errors here.
       const errorCode = error.code;
       const errorMessage = error.message;
       // The email of the user's account used.
       const email = error.email;
       // The credential that was used.
       const credential = GoogleAuthProvider.credentialFromError(error);
       // ...
     });
   }
   ```

## Advanced: Authenticate with Firebase in Node.js

To authenticate with Firebase in a Node.js application:

1. Sign in the user with their Google Account and get the user's Google ID token. You can accomplish this in several ways. For example:
   - If your app has a browser front end, use Google Sign-In as described in the [Handle the
     sign-in flow manually](https://firebase.google.com/docs/auth/web/google-signin#advanced-handle-the-sign-in-flow-manually) section. Get the Google ID token from the auth response:

     ```
     var id_token = googleUser.getAuthResponse().id_token
     ```
     Then, send this token to your Node.js app.
   - If your app runs on a device with limited input capabilities, such as a TV, you can use the [Google
     Sign-In for TVs and Devices](https://developers.google.com/identity/sign-in/devices) flow.
2. After you get the user's Google ID token, use it to build a Credential object and then sign in the user with the credential:

   ### Web

   ```javascript
   import { getAuth, signInWithCredential, GoogleAuthProvider } from "firebase/auth";

   // Build Firebase credential with the Google ID token.
   const credential = GoogleAuthProvider.credential(id_token);

   // Sign in with credential from the Google user.
   const auth = getAuth();
   signInWithCredential(auth, credential).catch((error) => {
     // Handle Errors here.
     const errorCode = error.code;
     const errorMessage = error.message;
     // The email of the user's account used.
     const email = error.customData.email;
     // The AuthCredential type that was used.
     const credential = GoogleAuthProvider.credentialFromError(error);
     // ...
   });
   ```

   ### Web

   ```javascript
   // Build Firebase credential with the Google ID token.
   var credential = firebase.auth.GoogleAuthProvider.credential(id_token);

   // Sign in with credential from the Google user.
   firebase.auth().signInWithCredential(credential).catch((error) => {
     // Handle Errors here.
     var errorCode = error.code;
     var errorMessage = error.message;
     // The email of the user's account used.
     var email = error.email;
     // The firebase.auth.AuthCredential type that was used.
     var credential = error.credential;
     // ...
   });
   ```

## Authenticate with Firebase in a Chrome extension

If you are building a Chrome extension app, see the [Offscreen Documents guide](https://firebase.google.com/docs/auth/web/chrome-extension#use_offscreen_documents).

## Customizing the redirect domain for Google sign-in

On project creation, Firebase will provision a unique subdomain for your project:
`https://my-app-12345.firebaseapp.com`.

This will also be used as the redirect mechanism for OAuth sign in. That domain would need to be
allowed for all supported OAuth providers. However, this means that users may see that
domain while signing in to Google before redirecting back to the application:
**Continue to: https://my-app-12345.firebaseapp.com**.

To avoid displaying your subdomain, you can set up a custom domain with Firebase Hosting:

1. Follow steps 1 through 3 in [Set up your domain for Hosting](https://firebase.google.com/docs/hosting/custom-domain). When you verify your domain ownership, Hosting provisions an SSL certificate for your custom domain.
2. Add your custom domain to the list of authorized domains in the [Firebase console](https://console.firebase.google.com/): `auth.custom.domain.com`.
3. In the Google developer console or OAuth setup page, whitelist the URL of the redirect page, which will be accessible on your custom domain: `https://auth.custom.domain.com/__/auth/handler`.
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