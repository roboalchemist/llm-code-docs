# Source: https://firebase.google.com/docs/auth/web/facebook-login.md.txt

You can let your users authenticate with Firebase using their Facebook accounts
by integrating Facebook Login into your app. You can integrate Facebook Login
either by using the Firebase SDK to carry out the sign-in flow, or by carrying
out the Facebook Login flow manually and passing the resulting access token to
Firebase.

## Before you begin

1. [Add Firebase to your JavaScript project](https://firebase.google.com/docs/web/setup).
2. On the [Facebook for Developers](https://developers.facebook.com/) site, get the **App ID** and an **App Secret** for your app.
3. Enable Facebook Login:
   1. In the [Firebase console](https://console.firebase.google.com/), open the **Authentication** section.
   2. On the **Sign in method** tab, enable the **Facebook** sign-in method and specify the **App ID** and **App Secret** you got from Facebook.
   3. Then, make sure your **OAuth redirect URI** (e.g. `my-app-12345.firebaseapp.com/__/auth/handler`) is listed as one of your **OAuth redirect URIs** in your Facebook app's settings page on the [Facebook for Developers](https://developers.facebook.com/) site in the **Product Settings \> Facebook Login** config.

## Handle the sign-in flow with the Firebase SDK

If you are building a web app, the easiest way to authenticate your users
with Firebase using their Facebook accounts is to handle the sign-in flow with
the Firebase JavaScript SDK. (If you want to authenticate a user in Node.js
or other non-browser environment, you must handle the sign-in flow manually.)

To handle the sign-in flow with the Firebase JavaScript SDK, follow these
steps:

1. Create an instance of the Facebook provider object:

   ### Web

   ```javascript
   import { FacebookAuthProvider } from "firebase/auth";

   const provider = new FacebookAuthProvider();
   ```

   ### Web

   ```javascript
   var provider = new firebase.auth.FacebookAuthProvider();
   ```
2. **Optional** : Specify additional OAuth 2.0 scopes that you want to request from the authentication provider. To add a scope, call `addScope`. For example:

   ### Web

   ```javascript
   provider.addScope('user_birthday');
   ```

   ### Web

   ```javascript
   provider.addScope('user_birthday');
   ```
   See the [authentication provider
   documentation](https://developers.facebook.com/docs/facebook-login/permissions).
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
     'display': 'popup'
   });
   ```

   ### Web

   ```javascript
   provider.setCustomParameters({
     'display': 'popup'
   });
   ```
   Reserved required OAuth parameters are not allowed and will be ignored. See the [authentication provider reference](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#setCustomParameters) for more details.
5. Authenticate with Firebase using the Facebook provider object. You can prompt your users to sign in with their Facebook accounts either by opening a pop-up window or by redirecting to the sign-in page. The redirect method is preferred on mobile devices.
   - To sign in with a pop-up window, call `signInWithPopup`:

     ### Web

     ```javascript
     import { getAuth, signInWithPopup, FacebookAuthProvider } from "firebase/auth";

     const auth = getAuth();
     signInWithPopup(auth, provider)
       .then((result) => {
         // The signed-in user info.
         const user = result.user;

         // This gives you a Facebook Access Token. You can use it to access the Facebook API.
         const credential = FacebookAuthProvider.credentialFromResult(result);
         const accessToken = credential.accessToken;

         // IdP data available using getAdditionalUserInfo(result)
         // ...
       })
       .catch((error) => {
         // Handle Errors here.
         const errorCode = error.code;
         const errorMessage = error.message;
         // The email of the user's account used.
         const email = error.customData.email;
         // The AuthCredential type that was used.
         const credential = FacebookAuthProvider.credentialFromError(error);

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

         // The signed-in user info.
         var user = result.user;
         // IdP data available in result.additionalUserInfo.profile.
           // ...

         // This gives you a Facebook Access Token. You can use it to access the Facebook API.
         var accessToken = credential.accessToken;

         // ...
       })
       .catch((error) => {
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
     Also notice that you can retrieve the Facebook provider's OAuth token which can be used to fetch additional data using the Facebook APIs.


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
     Then, you can also retrieve the Facebook provider's OAuth token by calling `getRedirectResult` when your page loads:

     ### Web

     ```javascript
     import { getAuth, getRedirectResult, FacebookAuthProvider } from "firebase/auth";

     const auth = getAuth();
     getRedirectResult(auth)
       .then((result) => {
         // This gives you a Facebook Access Token. You can use it to access the Facebook API.
         const credential = FacebookAuthProvider.credentialFromResult(result);
         const token = credential.accessToken;

         const user = result.user;
         // IdP data available using getAdditionalUserInfo(result)
         // ...
       }).catch((error) => {
         // Handle Errors here.
         const errorCode = error.code;
         const errorMessage = error.message;
         // The email of the user's account used.
         const email = error.customData.email;
         // AuthCredential type that was used.
         const credential = FacebookAuthProvider.credentialFromError(error);
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

           // This gives you a Facebook Access Token. You can use it to access the Facebook API.
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

> [!NOTE]
> **Note:** Facebook [enforces HTTPS](https://developers.facebook.com/blog/post/2018/06/08/enforce-https-facebook-login/) and does not allow login with insecure hosts. When using Facebook in development mode with an `http://localhost` origin, you need to ensure that development mode is turned on for this Facebook App. In addition, sign-in will only be allowed with Facebook test accounts.

## Handling account-exists-with-different-credential Errors

If you enabled the **One account per email address** setting in the [Firebase console](https://console.firebase.google.com/),
when a user tries to sign in a to a provider (such as Facebook) with an email that already
exists for another Firebase user's provider (such as Google), the error
`auth/account-exists-with-different-credential` is thrown along with an
`AuthCredential` object (Facebook access token). To complete the sign in to the
intended provider, the user has to sign first to the existing provider (Google) and then link to the
former `AuthCredential` (Facebook access token).

### Popup mode

If you use `signInWithPopup`, you can handle
`auth/account-exists-with-different-credential` errors with code like the following
example:

```
import {
  getAuth,
  linkWithCredential,
  signInWithPopup,
  FacebookAuthProvider,
} from "firebase/auth";

try {
  // Step 1: User tries to sign in using Facebook.
  let result = await signInWithPopup(getAuth(), new FacebookAuthProvider());
} catch (error) {
  // Step 2: User's email already exists.
  if (error.code === "auth/account-exists-with-different-credential") {
    // The pending Facebook credential.
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

  // Step 6: Link to the Facebook credential.
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

You can also authenticate with Firebase using a Facebook account by handling
the sign-in flow with the Facebook Login JavaScript SDK:

1. Integrate Facebook Login into your app by following the [developer docs](https://developers.facebook.com/docs/facebook-login/web). Be sure to configure Facebook Login with your Facebook app ID:

   ```
   <script src="//connect.facebook.net/en_US/sdk.js"></script>
   <script>
     FB.init({
       /**********************************************************************
        * TODO(Developer): Change the value below with your Facebook app ID. *
        **********************************************************************/
       appId: '<YOUR_FACEBOOK_APP_ID>',
       status: true,
       xfbml: true,
       version: 'v2.6',
     });
   </script>
   ```
2. We also setup a listener on the Facebook auth state:

   ```
   FB.Event.subscribe('auth.authResponseChange', checkLoginState);
   ```
3. After you integrate Facebook Login, add a Facebook Login button on your web pages:

   ```
   <fb:login-button
     data-auto-logout-link="true"
     scope="public_profile,email"
     size="large"
   ></fb:login-button>
   ```
4. In the Facebook auth state callback, exchange the auth token from Facebook's auth response for a Firebase credential and sign-in Firebase:

   ### Web

   ```javascript
   import { getAuth, onAuthStateChanged, signInWithCredential, signOut, FacebookAuthProvider } from "firebase/auth";
   const auth = getAuth();

   function checkLoginState(response) {
     if (response.authResponse) {
       // User is signed-in Facebook.
       const unsubscribe = onAuthStateChanged(auth, (firebaseUser) => {
         unsubscribe();
         // Check if we are already signed-in Firebase with the correct user.
         if (!isUserEqual(response.authResponse, firebaseUser)) {
           // Build Firebase credential with the Facebook auth token.
           const credential = FacebookAuthProvider.credential(
               response.authResponse.accessToken);

           // Sign in with the credential from the Facebook user.
           signInWithCredential(auth, credential)
             .catch((error) => {
               // Handle Errors here.
               const errorCode = error.code;
               const errorMessage = error.message;
               // The email of the user's account used.
               const email = error.customData.email;
               // The AuthCredential type that was used.
               const credential = FacebookAuthProvider.credentialFromError(error);
               // ...
             });
         } else {
           // User is already signed-in Firebase with the correct user.
         }
       });
     } else {
       // User is signed-out of Facebook.
       signOut(auth);
     }
   }
   ```

   ### Web

   ```javascript
   function checkLoginState(response) {
     if (response.authResponse) {
       // User is signed-in Facebook.
       var unsubscribe = firebase.auth().onAuthStateChanged((firebaseUser) => {
         unsubscribe();
         // Check if we are already signed-in Firebase with the correct user.
         if (!isUserEqual(response.authResponse, firebaseUser)) {
           // Build Firebase credential with the Facebook auth token.
           var credential = firebase.auth.FacebookAuthProvider.credential(
               response.authResponse.accessToken);

           // Sign in with the credential from the Facebook user.
           firebase.auth().signInWithCredential(credential)
             .catch((error) => {
               // Handle Errors here.
               var errorCode = error.code;
               var errorMessage = error.message;
               // The email of the user's account used.
               var email = error.email;
               // The firebase.auth.AuthCredential type that was used.
               var credential = error.credential;
               // ...
             });
         } else {
           // User is already signed-in Firebase with the correct user.
         }
       });
     } else {
       // User is signed-out of Facebook.
       firebase.auth().signOut();
     }
   }
   ```
   This is also where you can catch and handle errors. For a list of error codes have a look at the [Auth Reference Docs](https://firebase.google.com/docs/reference/js/auth#autherrorcodes).
5. Also you should check that the Facebook user is not already signed-in Firebase to avoid un-needed re-auth:

   ### Web

   ```javascript
   import { FacebookAuthProvider } from "firebase/auth";

   function isUserEqual(facebookAuthResponse, firebaseUser) {
     if (firebaseUser) {
       const providerData = firebaseUser.providerData;
       for (let i = 0; i < providerData.length; i++) {
         if (providerData[i].providerId === FacebookAuthProvider.PROVIDER_ID &&
             providerData[i].uid === facebookAuthResponse.userID) {
           // We don't need to re-auth the Firebase connection.
           return true;
         }
       }
     }
     return false;
   }
   ```

   ### Web

   ```javascript
   function isUserEqual(facebookAuthResponse, firebaseUser) {
     if (firebaseUser) {
       var providerData = firebaseUser.providerData;
       for (var i = 0; i < providerData.length; i++) {
         if (providerData[i].providerId === firebase.auth.FacebookAuthProvider.PROVIDER_ID &&
             providerData[i].uid === facebookAuthResponse.userID) {
           // We don't need to re-auth the Firebase connection.
           return true;
         }
       }
     }
     return false;
   }
   ```

## Advanced: Authenticate with Firebase in Node.js

To authenticate with Firebase in a Node.js application:

1. Sign in the user with their Facebook Account and get the user's Facebook access token. For example, sign in the user in a browser as described in the [Handle the sign-in
   flow manually](https://firebase.google.com/docs/auth/web/facebook-login#advanced-handle-the-sign-in-flow-manually) section, but send the access token to your Node.js application instead of using it in the client app.
2. After you get the user's Facebook access token, use it to build a Credential object and then sign in the user with the credential:

   ### Web

   ```javascript
   import { getAuth, signInWithCredential, FacebookAuthProvider } from "firebase/auth";

   // Sign in with the credential from the Facebook user.
   const auth = getAuth();
   signInWithCredential(auth, credential)
     .then((result) => {
       // Signed in 
       const credential = FacebookAuthProvider.credentialFromResult(result);
     })
     .catch((error) => {
       // Handle Errors here.
       const errorCode = error.code;
       const errorMessage = error.message;
       // The email of the user's account used.
       const email = error.customData.email;
       // The AuthCredential type that was used.
       const credential = FacebookAuthProvider.credentialFromError(error);
       // ...
     });
   ```

   ### Web

   ```javascript
   // Sign in with the credential from the Facebook user.
   firebase.auth().signInWithCredential(credential)
     .then((result) => {
       // Signed in       
       var credential = result.credential;
       // ...
     })
     .catch((error) => {
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

## Customizing the redirect domain for Facebook sign-in

On project creation, Firebase will provision a unique subdomain for your project:
`https://my-app-12345.firebaseapp.com`.

This will also be used as the redirect mechanism for OAuth sign in. That domain would need to be
allowed for all supported OAuth providers. However, this means that users may see that
domain while signing in to Facebook before redirecting back to the application:
**Continue to: https://my-app-12345.firebaseapp.com**.

To avoid displaying your subdomain, you can set up a custom domain with Firebase Hosting:

1. Follow steps 1 through 3 in [Set up your domain for Hosting](https://firebase.google.com/docs/hosting/custom-domain). When you verify your domain ownership, Hosting provisions an SSL certificate for your custom domain.
2. Add your custom domain to the list of authorized domains in the [Firebase console](https://console.firebase.google.com/): `auth.custom.domain.com`.
3. In the Facebook developer console or OAuth setup page, whitelist the URL of the redirect page, which will be accessible on your custom domain: `https://auth.custom.domain.com/__/auth/handler`.
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