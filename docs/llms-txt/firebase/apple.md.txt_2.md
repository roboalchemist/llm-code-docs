# Source: https://firebase.google.com/docs/auth/web/apple.md.txt

You can let your users authenticate with Firebase using their Apple ID by
using the Firebase SDK to carry out the end-to-end OAuth 2.0 sign-in flow.
**Important**: To sign in with an Apple account, users must:

- Have an Apple ID with two-factor authentication (2FA) enabled.
- Be signed in to iCloud on an Apple device.

See [How
to use Sign in with Apple](https://support.apple.com/en-us/HT210318). You will also need to meet these requirements
to test your integration with Sign In with Apple.

## Before you begin

[Video](https://www.youtube.com/watch?v=HyiNbqLOCQ8)

To sign in users using Apple, first configure Sign In with Apple
on Apple's developer site, then enable Apple as a sign-in provider for your
Firebase project.

### Join the Apple Developer Program

Sign In with Apple can only be configured by members of the [Apple Developer
Program](https://developer.apple.com/programs/).

### Configure Sign In with Apple

On the [Apple
Developer](https://developer.apple.com/account/resources) site, do the following:

1. Associate your website with your app as described in the first section
   of [Configure Sign In with Apple for the web](https://developer.apple.com/help/account/configure-app-capabilities/configure-sign-in-with-apple-for-the-web/). When prompted, register the
   following URL as a Return URL:

   ```
   https://YOUR_FIREBASE_PROJECT_ID.firebaseapp.com/__/auth/handler
   ```

   You can get your Firebase project ID on the
   [Firebase console
   settings page](https://console.firebase.google.com/project/_/settings/general/).

   When you're done, take note of your new Service ID, which you'll need in
   the next section.
2. [Create a
   Sign In with Apple private key](https://developer.apple.com/help/account/configure-app-capabilities/create-a-sign-in-with-apple-private-key/). You'll need your new private key and key ID in the next section.
3. If you use any of Firebase Authentication's features that send emails to users,
   including email link sign-in, email address verification, account change
   revocation, and
   others, [configure the Apple private email relay service](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service/) and register
   `noreply@YOUR_FIREBASE_PROJECT_ID.firebaseapp.com`
   (or your customized email template domain) so Apple can relay emails sent
   by Firebase Authentication to anonymized Apple email addresses.

### Enable Apple as a sign-in provider

1. [Add Firebase to your project](https://firebase.google.com/docs/web/setup).
2. In the [Firebase console](https://console.firebase.google.com/), open the **Auth** section. On the **Sign in method** tab, enable the **Apple** provider. Specify the Service ID you created in the previous section. Also, in the **OAuth code flow configuration section**, specify your Apple Team ID and the private key and key ID you created in the previous section.

## Comply with Apple anonymized data requirements

Sign In with Apple gives users the option of anonymizing their data,
including their email address, when signing in. Users who choose this option
have email addresses with the domain `privaterelay.appleid.com`. When
you use Sign In with Apple in your app, you must comply with any applicable
developer policies or terms from Apple regarding these anonymized Apple
IDs.

This includes obtaining any required user consent before you
associate any directly identifying personal information with an anonymized Apple
ID. When using Firebase Authentication, this may include the following
actions:

- Link an email address to an anonymized Apple ID or vice versa.
- Link a phone number to an anonymized Apple ID or vice versa
- Link a non-anonymous social credential (Facebook, Google, etc) to an anonymized Apple ID or vice versa.

The above list is not exhaustive. Refer to the Apple Developer Program
License Agreement in the Membership section of your developer account to make
sure your app meets Apple's requirements.

## Handle the sign-in flow with the Firebase SDK

If you are building a web app, the easiest way to authenticate your users with
Firebase using their Apple accounts is to handle the entire sign-in flow with
the Firebase JavaScript SDK.

To handle the sign-in flow with the Firebase JavaScript SDK, follow these
steps:

1. Create an instance of an **OAuthProvider** using the corresponding
   provider ID **apple.com**.

   ### Web

   ```javascript
   import { OAuthProvider } from "firebase/auth";

   const provider = new OAuthProvider('apple.com');
   ```

   ### Web

   ```javascript
   var provider = new firebase.auth.OAuthProvider('apple.com');
   ```
2. **Optional:** Specify additional OAuth 2.0 scopes beyond the default that
   you want to request from the authentication provider.

   ### Web

   ```javascript
   provider.addScope('email');
   provider.addScope('name');
   ```

   ### Web

   ```javascript
   provider.addScope('email');
   provider.addScope('name');
   ```

   By default, when **One account per email address** is enabled, Firebase
   requests email and name scopes. If you change this setting to **Multiple
   accounts per email address**, Firebase doesn't request any scopes from Apple
   unless you specify them.
3. **Optional:** If you want to display Apple's sign-in screen in a language
   other than English, set the `locale` parameter. See the
   [Sign In with Apple docs](https://developer.apple.com/documentation/signinwithapplejs/incorporating_sign_in_with_apple_into_other_platforms#3332112)
   for the supported locales.

   ### Web

   ```javascript
   provider.setCustomParameters({
     // Localize the Apple authentication screen in French.
     locale: 'fr'
   });
   ```

   ### Web

   ```javascript
   provider.setCustomParameters({
     // Localize the Apple authentication screen in French.
     locale: 'fr'
   });
   ```
4. Authenticate with Firebase using the OAuth provider object. You can
   prompt your users to sign in with their Apple Accounts either by opening a
   pop-up window or by redirecting to the sign-in page. The redirect method is
   preferred on mobile devices.

   - To sign in with a pop-up window, call `signInWithPopup()`:

     ### Web

     ```javascript
     import { getAuth, signInWithPopup, OAuthProvider } from "firebase/auth";

     const auth = getAuth();
     signInWithPopup(auth, provider)
       .then((result) => {
         // The signed-in user info.
         const user = result.user;

         // Apple credential
         const credential = OAuthProvider.credentialFromResult(result);
         const accessToken = credential.accessToken;
         const idToken = credential.idToken;

         // IdP data available using getAdditionalUserInfo(result)
         // ...
       })
       .catch((error) => {
         // Handle Errors here.
         const errorCode = error.code;
         const errorMessage = error.message;
         // The email of the user's account used.
         const email = error.customData.email;
         // The credential that was used.
         const credential = OAuthProvider.credentialFromError(error);

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

         // You can also get the Apple OAuth Access and ID Tokens.
         var accessToken = credential.accessToken;
         var idToken = credential.idToken;

         // IdP data available using getAdditionalUserInfo(result)
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
   - To sign in by redirecting to the sign-in page, call
     `signInWithRedirect()`:


   Follow the [best practices](https://firebase.google.com/docs/auth/web/redirect-best-practices) when using `signInWithRedirect`, `linkWithRedirect`, or `reauthenticateWithRedirect`.

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

   After the user completes sign-in and returns to the page, you can get the
   sign-in result by calling `getRedirectResult()`:

   ### Web

   ```javascript
   import { getAuth, getRedirectResult, OAuthProvider } from "firebase/auth";

   // Result from Redirect auth flow.
   const auth = getAuth();
   getRedirectResult(auth)
     .then((result) => {
       const credential = OAuthProvider.credentialFromResult(result);
       if (credential) {
         // You can also get the Apple OAuth Access and ID Tokens.
         const accessToken = credential.accessToken;
         const idToken = credential.idToken;
       }
       // The signed-in user info.
       const user = result.user;
     })
     .catch((error) => {
       // Handle Errors here.
       const errorCode = error.code;
       const errorMessage = error.message;
       // The email of the user's account used.
       const email = error.customData.email;
       // The credential that was used.
       const credential = OAuthProvider.credentialFromError(error);

       // ...
     });
   ```

   ### Web

   ```javascript
   // Result from Redirect auth flow.
   firebase
     .auth()
     .getRedirectResult()
     .then((result) => {
       if (result.credential) {
         /** @type {firebase.auth.OAuthCredential} */
         var credential = result.credential;

         // You can get the Apple OAuth Access and ID Tokens.
         var accessToken = credential.accessToken;
         var idToken = credential.idToken;

         // IdP data available in result.additionalUserInfo.profile.
         // ...
       }
       // The signed-in user info.
       var user = result.user;
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

   This is also where you can catch and handle errors. For a list of error
   codes, see the
   [API reference](https://firebase.google.com/docs/reference/js/auth#autherrorcodes).

   Unlike other providers supported by Firebase Auth, Apple does not provide a
   photo URL.

   Also, when the user chooses not to share their email with the app, Apple
   provisions a unique email address for that user (of the form
   `xyz@privaterelay.appleid.com`), which it shares with your app. If you
   configured the private email relay service, Apple forwards emails sent to the
   anonymized address to the user's real email address.

   Apple only shares user information such as the display name with apps the
   first time a user signs in. Usually, Firebase stores the display name the
   first time a user signs in with Apple, which you can get with
   `firebase.auth().currentUser.displayName`.
   However, if you previously used Apple to sign a user in to the app without
   using Firebase, Apple will not provide Firebase with the user's display name.

### Reauthentication and account linking

The same pattern can be used with `reauthenticateWithPopup()` and
`reauthenticateWithRedirect()`, which you can use to retrieve a fresh
credential for sensitive operations that require recent sign-in:

### Web

```javascript
import { getAuth, reauthenticateWithPopup, OAuthProvider } from "firebase/auth";

// Result from Redirect auth flow.
const auth = getAuth();
const provider = new OAuthProvider('apple.com');

reauthenticateWithPopup(auth.currentUser, provider)
  .then((result) => {
    // User is re-authenticated with fresh tokens minted and can perform
    // sensitive operations like account deletion, or updating their email
    // address or password.

    // The signed-in user info.
    const user = result.user;

    // You can also get the Apple OAuth Access and ID Tokens.
    const credential = OAuthProvider.credentialFromResult(result);
    const accessToken = credential.accessToken;
    const idToken = credential.idToken;

    // ...
  })
  .catch((error) => {
    // Handle Errors here.
    const errorCode = error.code;
    const errorMessage = error.message;
    // The email of the user's account used.
    const email = error.customData.email;
    // The credential that was used.
    const credential = OAuthProvider.credentialFromError(error);

    // ...
  });
```

### Web

```javascript
const provider = new firebase.auth.OAuthProvider('apple.com');

firebase
  .auth()
  .currentUser
  .reauthenticateWithPopup(provider)
  .then((result) => {
    // User is re-authenticated with fresh tokens minted and can perform
    // sensitive operations like account deletion, or updating their email
    // address or password.
    /** @type {firebase.auth.OAuthCredential} */
    var credential = result.credential;

    // The signed-in user info.
    var user = result.user;
     // You can also get the Apple OAuth Access and ID Tokens.
    var accessToken = credential.accessToken;
    var idToken = credential.idToken;

    // IdP data available in result.additionalUserInfo.profile.
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

And, you can use `linkWithPopup()` and `linkWithRedirect()`, to link different
identity providers to existing accounts.

Note that Apple requires you to get explicit consent from users before you link
their Apple accounts to other data.

For example, to link a Facebook account to the current Firebase account, use the
access token you got from signing the user in to Facebook:

### Web

```javascript
import { getAuth, linkWithPopup, FacebookAuthProvider } from "firebase/auth";

const auth = getAuth();
const provider = new FacebookAuthProvider();
provider.addScope('user_birthday');

// Assuming the current user is an Apple user linking a Facebook provider.
linkWithPopup(auth.currentUser, provider)
    .then((result) => {
      // Facebook credential is linked to the current Apple user.
      // ...

      // The user can now sign in to the same account
      // with either Apple or Facebook.
    })
    .catch((error) => {
      // Handle error.
    });
```

### Web

```javascript
const provider = new firebase.auth.FacebookAuthProvider();
provider.addScope('user_birthday');

// Assuming the current user is an Apple user linking a Facebook provider.
firebase.auth().currentUser.linkWithPopup(provider)
    .then((result) => {
      // Facebook credential is linked to the current Apple user.
      // Facebook additional data available in result.additionalUserInfo.profile,

      // Additional Facebook OAuth access token can also be retrieved.
      // result.credential.accessToken

      // The user can now sign in to the same account
      // with either Apple or Facebook.
    })
    .catch((error) => {
      // Handle error.
    });
```

## Authenticate with Firebase in a Chrome extension

If you are building a Chrome extension app, see the [Offscreen Documents guide](https://firebase.google.com/docs/auth/web/chrome-extension#use_offscreen_documents).

## Customizing the redirect domain for Apple sign-in

On project creation, Firebase will provision a unique subdomain for your project:
`https://my-app-12345.firebaseapp.com`.

This will also be used as the redirect mechanism for OAuth sign in. That domain would need to be
allowed for all supported OAuth providers. However, this means that users may see that
domain while signing in to Apple before redirecting back to the application:
**Continue to: https://my-app-12345.firebaseapp.com**.

To avoid displaying your subdomain, you can set up a custom domain with Firebase Hosting:

1. Follow steps 1 through 3 in [Set up your domain for Hosting](https://firebase.google.com/docs/hosting/custom-domain). When you verify your domain ownership, Hosting provisions an SSL certificate for your custom domain.
2. Add your custom domain to the list of authorized domains in the [Firebase console](https://console.firebase.google.com/): `auth.custom.domain.com`.
3. In the Apple developer console or OAuth setup page, whitelist the URL of the redirect page, which will be accessible on your custom domain: `https://auth.custom.domain.com/__/auth/handler`.
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

Note that you must still verify the custom domain with Apple similarly to the
default firebaseapp.com domain:

    http://auth.custom.example.com/.well-known/apple-developer-domain-association.txt

## Token revocation

Apple requires that apps that support account creation must let users initiate
deletion of their account within the app, as described in the [App Store Review
Guidelines](https://developer.apple.com/app-store/review/guidelines/#5.1.1v)

To meet this requirement, implement the following steps:

1. Make sure you filled out the *Services ID* and *OAuth code flow
   configuration* section of the Sign in with Apple provider configuration, as
   outlined in the [Configure Sign in with Apple](https://firebase.google.com/docs/auth/web/apple#configure-sign-in-with-apple)
   section.

2. Since Firebase does not store user tokens when users are created with
   Sign in with Apple, you must ask the user to sign in again before revoking
   their token and deleting the account.

   Then, obtain the Apple OAuth access token from the `OAuthCredential`, and
   use it to call `revokeAccessToken(auth, token)` to revoke the Apple OAuth
   access token.

       const provider = new OAuthProvider('apple.com');
       provider.addScope('email');
       provider.addScope('name');

       const auth = getAuth();
       signInWithPopup(auth, provider).then(result => {
         // Get the Apple OAuth access token.
         const credential = OAuthProvider.credentialFromResult(result);
         const accessToken = credential.accessToken;

         // Revoke the Apple OAuth access token.
         revokeAccessToken(auth, accessToken)
           .then(() => {
             // Token revoked.

             // Delete the user account.
             // ...
           })
           .catch(error => {
             // An error happened.
             // ...
           });
       });

3. Finally, [delete the user account](https://firebase.google.com/docs/auth/web/manage-users#delete_a_user) (and all
   associated data).

## Advanced: Authenticate with Firebase in Node.js

To authenticate with Firebase in a Node.js application:

1. Sign in the user with their Apple Account and get the user's Apple ID
   token. You can accomplish this in several ways. For example, if your Node.js
   app has a browser front end:

   1. On your backend, generate a random string (a "nonce") and compute its
      SHA256 hash. The nonce is a one-time use value you use to validate a
      single round trip between your backend and Apple's auth servers.

      ### Web

      ```javascript
      const crypto = require("crypto");
      const string_decoder = require("string_decoder");

      // Generate a new random string for each sign-in
      const generateNonce = (length) => {
        const decoder = new string_decoder.StringDecoder("ascii");
        const buf = Buffer.alloc(length);
        let nonce = "";
        while (nonce.length < length) {
          crypto.randomFillSync(buf);
          nonce = decoder.write(buf);
        }
        return nonce.slice(0, length);
      };

      const unhashedNonce = generateNonce(10);

      // SHA256-hashed nonce in hex
      const hashedNonceHex = crypto.createHash('sha256')
        .update(unhashedNonce).digest().toString('hex');
      ```

      ### Web

      ```javascript
      const crypto = require("crypto");
      const string_decoder = require("string_decoder");

      // Generate a new random string for each sign-in
      const generateNonce = function(length) {
        const decoder = new string_decoder.StringDecoder("ascii");
        const buf = Buffer.alloc(length);
        var nonce = "";
        while (nonce.length < length) {
          crypto.randomFillSync(buf);
          nonce = decoder.write(buf);
        }
        return nonce.slice(0, length);
      };

      const unhashedNonce = generateNonce(10);

      // SHA256-hashed nonce in hex
      const hashedNonceHex = crypto.createHash('sha256')
        .update(unhashedNonce).digest().toString('hex');
      ```
   2. On your sign-in page, specify the hashed nonce in your Sign In with
      Apple configuration:

          <script src="https://appleid.cdn-apple.com/appleauth/static/jsapi/appleid/1/en_US/appleid.auth.js"></script>
          <div id="appleid-signin" data-color="black" data-border="true" data-type="sign in"></div>
          <script>
              AppleID.auth.init({
                  clientId: YOUR_APPLE_CLIENT_ID,
                  scope: 'name email',
                  redirectURI: URL_TO_YOUR_REDIRECT_HANDLER,  // See the next step.
                  state: '[STATE]',  // Optional value that Apple will send back to you
                                     // so you can return users to the same context after
                                     // they sign in.
                  nonce: HASHED_NONCE  // The hashed nonce you generated in the previous step.
              });
          </script>

   3. Get the Apple ID token from POSTed auth response server-side:

          app.post('/redirect', (req, res) => {
            const savedState = req.cookies.__session;
            const code = req.body.code;
            const state = req.body.state;
            const appleIdToken = req.body.id_token;
            if (savedState !== state || !code) {
              res.status(403).send('403: Permission denied');
            } else {
              // Sign in with Firebase using appleIdToken. (See next step).
            }
          });

   Also see [Configuring Your Webpage for Sign In with Apple](https://developer.apple.com/documentation/signinwithapplejs/configuring_your_webpage_for_sign_in_with_apple).
2. After you get the user's Apple ID token, use it to build a Credential
   object and then sign in the user with the credential:

   ### Web

   ```javascript
   import { getAuth, signInWithCredential, OAuthProvider } from "firebase/auth";

   const auth = getAuth();

   // Build Firebase credential with the Apple ID token.
   const provider = new OAuthProvider('apple.com');
   const authCredential = provider.credential({
     idToken: appleIdToken,
     rawNonce: unhashedNonce,
   });

   // Sign in with credential form the Apple user.
   signInWithCredential(auth, authCredential)
     .then((result) => {
       // User signed in.
     })
     .catch((error) => {
       // An error occurred. If error.code == 'auth/missing-or-invalid-nonce',
       // make sure you're sending the SHA256-hashed nonce as a hex string
       // with your request to Apple.
       console.log(error);
     });
   ```

   ### Web

   ```javascript
   // Build Firebase credential with the Apple ID token.
   const provider = new firebase.auth.OAuthProvider('apple.com');
   const authCredential = provider.credential({
     idToken: appleIdToken,
     rawNonce: unhashedNonce,
   });

   // Sign in with credential form the Apple user.
   firebase.auth().signInWithCredential(authCredential)
     .then((result) => {
       // User signed in.
     })
     .catch((error) => {
       // An error occurred. If error.code == 'auth/missing-or-invalid-nonce',
       // make sure you're sending the SHA256-hashed nonce as a hex string
       // with your request to Apple.
       console.log(error);
     });
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