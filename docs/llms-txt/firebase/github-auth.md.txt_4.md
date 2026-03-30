# Source: https://firebase.google.com/docs/auth/web/github-auth.md.txt

You can let your users authenticate with Firebase using their GitHub accounts
by integrating GitHub authentication into your app. You can integrate GitHub
authentication either by using the Firebase SDK to carry out the sign-in flow,
or by carrying out the GitHub OAuth 2.0 flow manually and passing the resulting
access token to Firebase.

## Before you begin

1. [Add Firebase to your JavaScript project](https://firebase.google.com/docs/web/setup).
2. In the [Firebase console](https://console.firebase.google.com/), open the **Auth** section.
3. On the **Sign in method** tab, enable the **GitHub** provider.
4. Add the **Client ID** and **Client Secret** from that provider's developer console to the provider configuration:
   1. [Register your app](https://github.com/settings/applications/new) as a developer application on GitHub and get your app's OAuth 2.0 **Client ID** and **Client Secret**.
   2. Make sure your Firebase **OAuth redirect URI** (e.g. `my-app-12345.firebaseapp.com/__/auth/handler`) is set as your **Authorization callback URL** in your app's settings page on your [GitHub app's config](https://github.com/settings/developers).
5. Click **Save**.

## Handle the sign-in flow with the Firebase SDK

If you are building a web app, the easiest way to authenticate your users
with Firebase using their GitHub accounts is to handle the sign-in flow with
the Firebase JavaScript SDK. (If you want to authenticate a user in Node.js
or other non-browser environment, you must handle the sign-in flow manually.)

To handle the sign-in flow with the Firebase JavaScript SDK, follow these
steps:

1. Create an instance of the GitHub provider object:

   ### Web

   ```javascript
   import { GithubAuthProvider } from "firebase/auth";

   const provider = new GithubAuthProvider();
   ```

   ### Web

   ```javascript
   var provider = new firebase.auth.GithubAuthProvider();
   ```
2. **Optional** : Specify additional OAuth 2.0 scopes that you want to request from the authentication provider. To add a scope, call `addScope`. For example:

   ### Web

   ```javascript
   provider.addScope('repo');
   ```

   ### Web

   ```javascript
   provider.addScope('repo');
   ```
   See the [authentication provider
   documentation](https://developer.github.com/v3/oauth/#scopes).
3. **Optional** : Specify additional custom OAuth provider parameters that you want to send with the OAuth request. To add a custom parameter, call `setCustomParameters` on the initialized provider with an object containing the key as specified by the OAuth provider documentation and the corresponding value. For example:

   ### Web

   ```javascript
   provider.setCustomParameters({
     'allow_signup': 'false'
   });
   ```

   ### Web

   ```javascript
   provider.setCustomParameters({
     'allow_signup': 'false'
   });
   ```
   Reserved required OAuth parameters are not allowed and will be ignored. See the [authentication provider reference](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#setCustomParameters) for more details.
4. Authenticate with Firebase using the GitHub provider object. You can prompt your users to sign in with their GitHub accounts either by opening a pop-up window or by redirecting to the sign-in page. The redirect method is preferred on mobile devices.
   - To sign in with a pop-up window, call `signInWithPopup`:

     ### Web

     ```javascript
     import { getAuth, signInWithPopup, GithubAuthProvider } from "firebase/auth";

     const auth = getAuth();
     signInWithPopup(auth, provider)
       .then((result) => {
         // This gives you a GitHub Access Token. You can use it to access the GitHub API.
         const credential = GithubAuthProvider.credentialFromResult(result);
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
         const credential = GithubAuthProvider.credentialFromError(error);
         // ...
       });
     ```

     ### Web

     ```javascript
     firebase
       .auth()
       .signInWithPopup(provider)
       .then((result) => {
         /** @type {firebase.auth.OAuthCredential} */
         var credential = result.credential;

         // This gives you a GitHub Access Token. You can use it to access the GitHub API.
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
     Also notice that you can retrieve the GitHub provider's OAuth token which can be used to fetch additional data using the GitHub APIs.


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
     Then, you can also retrieve the GitHub provider's OAuth token by calling `getRedirectResult` when your page loads:

     ### Web

     ```javascript
     import { getAuth, getRedirectResult, GithubAuthProvider } from "firebase/auth";

     const auth = getAuth();
     getRedirectResult(auth)
       .then((result) => {
         const credential = GithubAuthProvider.credentialFromResult(result);
         if (credential) {
           // This gives you a GitHub Access Token. You can use it to access the GitHub API.
           const token = credential.accessToken;
           // ...
         }

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
         const credential = GithubAuthProvider.credentialFromError(error);
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

           // This gives you a GitHub Access Token. You can use it to access the GitHub API.
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

If you enabled the **One account per email address** setting in the [Firebase console](https://console.firebase.google.com/),
when a user tries to sign in a to a provider (such as GitHub) with an email that already
exists for another Firebase user's provider (such as Google), the error
`auth/account-exists-with-different-credential` is thrown along with an
`AuthCredential` object (GitHub access token). To complete the sign in to the
intended provider, the user has to sign first to the existing provider (Google) and then link to the
former `AuthCredential` (GitHub access token).

### Popup mode

If you use `signInWithPopup`, you can handle
`auth/account-exists-with-different-credential` errors with code like the following
example:

```
import {
  getAuth,
  linkWithCredential,
  signInWithPopup,
  GitHubAuthProvider,
} from "firebase/auth";

try {
  // Step 1: User tries to sign in using GitHub.
  let result = await signInWithPopup(getAuth(), new GitHubAuthProvider());
} catch (error) {
  // Step 2: User's email already exists.
  if (error.code === "auth/account-exists-with-different-credential") {
    // The pending GitHub credential.
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

  // Step 6: Link to the GitHub credential.
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

## Handle the sign-in flow manually

You can also authenticate with Firebase using a GitHub account by handling the
sign-in flow by calling the GitHub OAuth 2.0 endpoints:

1. Integrate GitHub authentication into your app by following the [developer's documentation](https://developer.github.com/v3/oauth/#web-application-flow). At the end of the GitHub sign-in flow, you will receive an OAuth 2.0 access token.
2. If you need to sign in on a Node.js application, send the OAuth access token to the Node.js application.
3. After a user successfully signs in with GitHub, exchange the OAuth 2.0 access token for a Firebase credential:

   ### Web

   ```javascript
   import { GithubAuthProvider } from "firebase/auth";

   const credential = GithubAuthProvider.credential(token);
   ```

   ### Web

   ```javascript
   var credential = firebase.auth.GithubAuthProvider.credential(token);
   ```
4. Authenticate with Firebase using the Firebase credential:

   ### Web

   ```javascript
   import { getAuth, signInWithCredential } from "firebase/auth";

   // Sign in with the credential from the user.
   const auth = getAuth();
   signInWithCredential(auth, credential)
     .then((result) => {
       // Signed in 
       // ...
     })
     .catch((error) => {
       // Handle Errors here.
       const errorCode = error.code;
       const errorMessage = error.message;
       // The email of the user's account used.
       const email = error.customData.email;
       // ...
     });
   ```

   ### Web

   ```javascript
   // Sign in with the credential from the user.
   firebase.auth()
     .signInWithCredential(credential)
     .then((result) => {
       // Signed in 
       // ...
     })
     .catch((error) => {
       // Handle Errors here.
       const errorCode = error.code;
       const errorMessage = error.message;
       // The email of the user's account used.
       const email = error.email;
       // ...
     });
   ```

## Authenticate with Firebase in a Chrome extension

If you are building a Chrome extension app, see the [Offscreen Documents guide](https://firebase.google.com/docs/auth/web/chrome-extension#use_offscreen_documents).

## Customizing the redirect domain for GitHub sign-in

On project creation, Firebase will provision a unique subdomain for your project:
`https://my-app-12345.firebaseapp.com`.

This will also be used as the redirect mechanism for OAuth sign in. That domain would need to be
allowed for all supported OAuth providers. However, this means that users may see that
domain while signing in to GitHub before redirecting back to the application:
**Continue to: https://my-app-12345.firebaseapp.com**.

To avoid displaying your subdomain, you can set up a custom domain with Firebase Hosting:

1. Follow steps 1 through 3 in [Set up your domain for Hosting](https://firebase.google.com/docs/hosting/custom-domain). When you verify your domain ownership, Hosting provisions an SSL certificate for your custom domain.
2. Add your custom domain to the list of authorized domains in the [Firebase console](https://console.firebase.google.com/): `auth.custom.domain.com`.
3. In the GitHub developer console or OAuth setup page, whitelist the URL of the redirect page, which will be accessible on your custom domain: `https://auth.custom.domain.com/__/auth/handler`.
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