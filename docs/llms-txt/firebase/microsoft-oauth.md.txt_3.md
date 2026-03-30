# Source: https://firebase.google.com/docs/auth/web/microsoft-oauth.md.txt

You can let your users authenticate with Firebase using OAuth providers like
Microsoft Azure Active Directory by integrating generic OAuth Login
into your app using the Firebase SDK to carry out the end to end sign-in flow.

## Before you begin

To sign in users using Microsoft accounts (Azure Active Directory and personal
Microsoft accounts), you must first enable Microsoft as a sign-in provider for
your Firebase project:

1. [Add Firebase to your JavaScript project](https://firebase.google.com/docs/web/setup).
2. In the [Firebase console](https://console.firebase.google.com/), open the **Auth** section.
3. On the **Sign in method** tab, enable the **Microsoft** provider.
4. Add the **Client ID** and **Client Secret** from that provider's developer console to the provider configuration:
   1. To register a Microsoft OAuth client, follow the instructions in [Quickstart: Register an app with the Azure Active Directory v2.0 endpoint](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-v2-register-an-app). Note that this endpoint supports sign-in using Microsoft personal accounts as well as Azure Active Directory accounts. [Learn more](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-overview) about Azure Active Directory v2.0.
   2. When registering apps with these providers, be sure to register the `*.firebaseapp.com` domain for your project as the redirect domain for your app.
5. Click **Save**.

## Handle the sign-in flow with the Firebase SDK

If you are building a web app, the easiest way to authenticate your users with
Firebase using their Microsoft accounts is to handle the entire sign-in flow
with the Firebase JavaScript SDK.

To handle the sign-in flow with the Firebase JavaScript SDK, follow these steps:

1. Create an instance of an **OAuthProvider** using the provider ID
   **microsoft.com**.

   ### Web

   ```javascript
   import { OAuthProvider } from "firebase/auth";

   const provider = new OAuthProvider('microsoft.com');
   ```

   ### Web

   ```javascript
   var provider = new firebase.auth.OAuthProvider('microsoft.com');
   ```
2. **Optional**: Specify additional custom OAuth parameters that you want to
   send with the OAuth request.

   ### Web

   ```javascript
   provider.setCustomParameters({
     // Force re-consent.
     prompt: 'consent',
     // Target specific email with login hint.
     login_hint: 'user@firstadd.onmicrosoft.com'
   });
   ```

   ### Web

   ```javascript
   provider.setCustomParameters({
     // Force re-consent.
     prompt: 'consent',
     // Target specific email with login hint.
     login_hint: 'user@firstadd.onmicrosoft.com'
   });
   ```

   For the parameters Microsoft supports, see the
   [Microsoft OAuth documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v1-protocols-oauth-code).
   Note that you can't pass Firebase-required parameters with
   `setCustomParameters()`. These parameters are **client_id** ,
   **response_type** , **redirect_uri** , **state** , **scope** and
   **response_mode**.

   To allow only users from a particular Azure AD tenant to sign
   into the application, either the friendly domain name of the Azure AD tenant
   or the tenant's GUID identifier can be used. This can be done by specifying
   the "tenant" field in the custom parameters object.

   ### Web

   ```javascript
   provider.setCustomParameters({
     // Optional "tenant" parameter in case you are using an Azure AD tenant.
     // eg. '8eaef023-2b34-4da1-9baa-8bc8c9d6a490' or 'contoso.onmicrosoft.com'
     // or "common" for tenant-independent tokens.
     // The default value is "common".
     tenant: 'TENANT_ID'
   });
   ```

   ### Web

   ```javascript
   provider.setCustomParameters({
     // Optional "tenant" parameter in case you are using an Azure AD tenant.
     // eg. '8eaef023-2b34-4da1-9baa-8bc8c9d6a490' or 'contoso.onmicrosoft.com'
     // or "common" for tenant-independent tokens.
     // The default value is "common".
     tenant: 'TENANT_ID'
   });
   ```
3. **Optional**: Specify additional OAuth 2.0 scopes beyond basic profile that
   you want to request from the authentication provider.

   ```
   provider.addScope('mail.read');
   provider.addScope('calendars.read');
   ```

   To learn more, refer to the
   [Microsoft permissions and consent documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent).
4. Authenticate with Firebase using the OAuth provider object. You can prompt
   your users to sign in with their Microsoft Accounts either by opening a
   pop-up window or by redirecting to the sign-in page. The redirect method is
   preferred on mobile devices.

   - To sign in with a pop-up window, call `signInWithPopup`:

   ### Web

   ```javascript
   import { getAuth, signInWithPopup, OAuthProvider } from "firebase/auth";

   const auth = getAuth();
   signInWithPopup(auth, provider)
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
   ```

   ### Web

   ```javascript
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
   ```
   - To sign in by redirecting to the sign-in page, call `signInWithRedirect`:


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

   After the user completes sign-in and returns to the page, you can obtain
   the sign-in result by calling `getRedirectResult`.

   ### Web

   ```javascript
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
   ```

   ### Web

   ```javascript
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
   ```

   On successful completion, the OAuth access token associated with the
   provider can be retrieved from the `firebase.auth.UserCredential` object
   returned.

   Using the OAuth access token, you can call the
   [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/overview?toc=./toc.json&view=graph-rest-1.0).

   For example, to get the basic profile information, the following REST API
   can be called:

   ```
   curl -i -H "Authorization: Bearer ACCESS_TOKEN" https://graph.microsoft.com/v1.0/me
   ```

   Unlike other providers supported by Firebase Auth, Microsoft does not
   provide a photo URL and instead, the binary data for a profile photo has to
   be requested via
   [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/api/profilephoto-get?view=graph-rest-1.0).

   In addition to the OAuth access token, the user's OAuth
   [ID token](https://docs.microsoft.com/en-us/azure/active-directory/develop/id-tokens)
   can also be retrieved from the `firebase.auth.UserCredential` object. The
   `sub` claim in the ID token is app-specific and will not match the federated
   user identifier used by Firebase Auth and accessible via
   `user.providerData[0].uid`. The `oid` claim field should be used instead.
   When using a Azure AD tenant to sign-in, the `oid` claim will be an exact
   match.
   However for the non-tenant case, the `oid` field is padded. For a federated
   ID `4b2eabcdefghijkl`, the `oid` will have have a form
   `00000000-0000-0000-4b2e-abcdefghijkl`.
5. While the above examples focus on sign-in flows, you also have the
   ability to link a Microsoft provider to an existing user using
   `linkWithPopup`/`linkWithRedirect`. For example, you can link multiple
   providers to the same user allowing them to sign in with either.

   ### Web

   ```javascript
   import { getAuth, linkWithPopup, OAuthProvider } from "firebase/auth";

   const provider = new OAuthProvider('microsoft.com');
   const auth = getAuth();

   linkWithPopup(auth.currentUser, provider)
       .then((result) => {
         // Microsoft credential is linked to the current user.
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
   var provider = new firebase.auth.OAuthProvider('microsoft.com');
   firebase.auth().currentUser.linkWithPopup(provider)
       .then((result) => {
         // Microsoft credential is linked to the current user.
         // IdP data available in result.additionalUserInfo.profile.
         // OAuth access token can also be retrieved:
         // result.credential.accessToken
         // OAuth ID token can also be retrieved:
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

   const provider = new OAuthProvider('microsoft.com');
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
   var provider = new firebase.auth.OAuthProvider('microsoft.com');
   firebase.auth().currentUser.reauthenticateWithPopup(provider)
       .then((result) => {
         // User is re-authenticated with fresh tokens minted and
         // should be able to perform sensitive operations like account
         // deletion and email or password update.
         // IdP data available in result.additionalUserInfo.profile.
         // OAuth access token can also be retrieved:
         // result.credential.accessToken
         // OAuth ID token can also be retrieved:
         // result.credential.idToken
       })
       .catch((error) => {
         // Handle error.
       });
   ```

## Handling account-exists-with-different-credential Errors

If you enabled the **One account per email address** setting in the [Firebase console](https://console.firebase.google.com/),
when a user tries to sign in a to a provider (such as Microsoft) with an email that already
exists for another Firebase user's provider (such as Google), the error
`auth/account-exists-with-different-credential` is thrown along with an
`AuthCredential` object (Microsoft credential). To complete the sign in to the
intended provider, the user has to sign first to the existing provider (Google) and then link to the
former `AuthCredential` (Microsoft credential).

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
  // Step 1: User tries to sign in using Microsoft.
  let result = await signInWithPopup(getAuth(), new OAuthProvider());
} catch (error) {
  // Step 2: User's email already exists.
  if (error.code === "auth/account-exists-with-different-credential") {
    // The pending Microsoft credential.
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

  // Step 6: Link to the Microsoft credential.
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
providers such as Microsoft due to the inability of the Firebase
Auth server to verify the audience of Microsoft OAuth access tokens.
This is a critical security requirement and could expose applications and
websites to replay attacks where a Microsoft OAuth access token obtained for
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

## Customizing the redirect domain for Microsoft sign-in

On project creation, Firebase will provision a unique subdomain for your project:
`https://my-app-12345.firebaseapp.com`.

This will also be used as the redirect mechanism for OAuth sign in. That domain would need to be
allowed for all supported OAuth providers. However, this means that users may see that
domain while signing in to Microsoft before redirecting back to the application:
**Continue to: https://my-app-12345.firebaseapp.com**.

To avoid displaying your subdomain, you can set up a custom domain with Firebase Hosting:

1. Follow steps 1 through 3 in [Set up your domain for Hosting](https://firebase.google.com/docs/hosting/custom-domain). When you verify your domain ownership, Hosting provisions an SSL certificate for your custom domain.
2. Add your custom domain to the list of authorized domains in the [Firebase console](https://console.firebase.google.com/): `auth.custom.domain.com`.
3. In the Microsoft developer console or OAuth setup page, whitelist the URL of the redirect page, which will be accessible on your custom domain: `https://auth.custom.domain.com/__/auth/handler`.
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