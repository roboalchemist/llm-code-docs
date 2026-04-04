# Source: https://firebase.google.com/docs/auth/web/anonymous-auth.md.txt

You can use Firebase Authentication to create and use temporary anonymous accounts
to authenticate with Firebase. These temporary anonymous accounts can be used to
allow users who haven't yet signed up to your app to work with data protected
by security rules. If an anonymous user decides to sign up to your app, you can
[link their sign-in credentials to the anonymous
account](https://firebase.google.com/docs/auth/web/account-linking) so that they can continue to work with their protected data in
future sessions.

## Before you begin

1. [Add Firebase to your JavaScript project](https://firebase.google.com/docs/web/setup).
2. If you haven't yet connected your app to your Firebase project, do so from the [Firebase console](https://console.firebase.google.com/).
3. Enable anonymous auth:
   1. In the [Firebase console](https://console.firebase.google.com/), open the **Auth** section.
   2. On the **Sign-in Methods** page, enable the **Anonymous** sign-in method.
   3. **Optional** : If you've upgraded your project to [Firebase Authentication with Identity Platform](https://firebase.google.com/docs/auth#identity-platform), you can enable automatic clean-up. When you enable this setting, anonymous accounts older than 30 days will be automatically deleted. In projects with automatic clean-up enabled, anonymous authentication will no longer count toward usage limits or billing quotas. See [Automatic clean-up](https://firebase.google.com/docs/auth/web/anonymous-auth#auto-cleanup).

## Authenticate with Firebase anonymously

When a signed-out user uses an app feature that requires authentication with
Firebase, sign in the user anonymously by completing the following steps:

1. Call the `signInAnonymously` method:

   ### Web

   ```javascript
   import { getAuth, signInAnonymously } from "firebase/auth";

   const auth = getAuth();
   signInAnonymously(auth)
     .then(() => {
       // Signed in..
     })
     .catch((error) => {
       const errorCode = error.code;
       const errorMessage = error.message;
       // ...
     });
   ```

   ### Web

   ```javascript
   firebase.auth().signInAnonymously()
     .then(() => {
       // Signed in..
     })
     .catch((error) => {
       var errorCode = error.code;
       var errorMessage = error.message;
       // ...
     });
   ```
   This is also where you can catch and handle errors. For a list of error codes have a look at the [Auth Reference Docs](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#signInAnonymously).
2. If the `signInAnonymously` method completes without error, the observer registered in the `onAuthStateChanged` will trigger and you can get the anonymous user's account data from the `User` object:

   ### Web

   ```javascript
   import { getAuth, onAuthStateChanged } from "firebase/auth";

   const auth = getAuth();
   onAuthStateChanged(auth, (user) => {
     if (user) {
       // User is signed in, see docs for a list of available properties
       // https://firebase.google.com/docs/reference/js/auth.user
       const uid = user.uid;
       // ...
     } else {
       // User is signed out
       // ...
     }
   });
   ```

   ### Web

   ```javascript
   firebase.auth().onAuthStateChanged((user) => {
     if (user) {
       // User is signed in, see docs for a list of available properties
       // https://firebase.google.com/docs/reference/js/v8/firebase.User
       var uid = user.uid;
       // ...
     } else {
       // User is signed out
       // ...
     }
   });
   ```

To protect your project from abuse, Firebase limits the number of new email/password and anonymous sign-ups that your application can have from the same IP address in a short period of time. You can request and schedule temporary changes to this quota from the [Firebase console](https://console.firebase.google.com/project/_/authentication/providers).

## Convert an anonymous account to a permanent account

When an anonymous user signs up to your app, you might want to allow them to
continue their work with their new account---for example, you might want to
make the items the user added to their shopping cart before they signed up
available in their new account's shopping cart. To do so, complete the following
steps:

1. When the user signs up, complete the sign-in flow for the user's authentication provider up to, but not including, calling one of the `Auth.signInWith` methods. For example, get the user's Google ID token, Facebook access token, or email address and password.
2. Get an `AuthCredential` for the new authentication provider:

   ##### Google Sign-In

   ### Web

   ```javascript
   import { GoogleAuthProvider } from "firebase/auth";

   const credential = GoogleAuthProvider.credential(
     googleUser.getAuthResponse().id_token);
   ```

   ### Web

   ```javascript
   var credential = firebase.auth.GoogleAuthProvider.credential(
     googleUser.getAuthResponse().id_token);
   ```

   ##### Facebook Login

   ### Web

   ```javascript
   import { FacebookAuthProvider } from "firebase/auth";

   const credential = FacebookAuthProvider.credential(
     response.authResponse.accessToken);
   ```

   ### Web

   ```javascript
   var credential = firebase.auth.FacebookAuthProvider.credential(
     response.authResponse.accessToken);
   ```

   ##### Email-password sign-in

   ### Web

   ```javascript
   import { EmailAuthProvider } from "firebase/auth";

   const credential = EmailAuthProvider.credential(email, password);
   ```

   ### Web

   ```javascript
   var credential = firebase.auth.EmailAuthProvider.credential(email, password);
   ```
3. Pass the `AuthCredential` object to the sign-in user's
   `link` method:

   ### Web

   ```javascript
   import { getAuth, linkWithCredential } from "firebase/auth";

   const auth = getAuth();
   linkWithCredential(auth.currentUser, credential)
     .then((usercred) => {
       const user = usercred.user;
       console.log("Anonymous account successfully upgraded", user);
     }).catch((error) => {
       console.log("Error upgrading anonymous account", error);
     });
   ```

   ### Web

   ```javascript
   auth.currentUser.linkWithCredential(credential)
     .then((usercred) => {
       var user = usercred.user;
       console.log("Anonymous account successfully upgraded", user);
     }).catch((error) => {
       console.log("Error upgrading anonymous account", error);
     });
   ```

If the call to `link` succeeds, the user's new account can
access the anonymous account's Firebase data.

> [!NOTE]
> This technique can also be used to [link any two accounts](https://firebase.google.com/docs/auth/web/account-linking).

## Automatic clean-up

If you've upgraded your project to [Firebase Authentication with Identity Platform](https://firebase.google.com/docs/auth#identity-platform), you can
enable automatic clean-up in the Firebase console. When you enable this feature you allow
Firebase to automatically delete anonymous accounts older than 30 days. In projects with automatic
clean-up enabled, anonymous authentication will not count toward usage limits or billing quotas.

- Any anonymous accounts created after enabling automatic clean-up might be automatically deleted any time after 30 days post-creation.
- Existing anonymous accounts will be eligible for automatic deletion 30 days after enabling automatic clean-up.
- If you turn automatic clean-up off, any anonymous accounts scheduled to be deleted will remain scheduled to be deleted.
- If you "upgrade" an anonymous account by linking it to any sign-in method, the account will not get automatically deleted.

If you want to see how many users will be affected before you enable this feature, and you've
upgraded your project to [Firebase Authentication with Identity Platform](https://firebase.google.com/docs/auth#identity-platform), you can filter by
`is_anon` in [Cloud
Logging](https://cloud.google.com/logging/docs).

## Next steps

Now that users can authenticate with Firebase, you can control their access to
data in your Firebase database using
[Firebase rules](https://firebase.google.com/docs/database/security#section-authorization).