# Source: https://firebase.google.com/docs/auth/web/account-linking.md.txt

**Important** : There is a [known issue](https://github.com/firebase/firebase-js-sdk/issues/7675) that prevents `linkWithCredentials()` from working correctly in some projects. See the issue report for a workaround and the status of a fix.

You can allow users to sign in to your app using multiple authentication
providers by linking auth provider credentials to an existing user account.
Users are identifiable by the same Firebase user ID regardless of the
authentication provider they used to sign in. For example, a user who signed in
with a password can link a Google account and sign in with either method in the
future. Or, an anonymous user can link a Facebook account and then, later, sign
in with Facebook to continue using your app.

## Before you begin

Add support for two or more authentication providers (possibly including
anonymous authentication) to your app.

## Link federated auth provider credentials to a user account

To link credentials from an auth provider such as Google or Facebook to an
existing user account:

1. Sign in the user using any authentication provider or method.
2. Get the `AuthProvider` object that corresponds to the provider you want to link to the user's account. Examples:

   ### Web

   ```javascript
   import { GoogleAuthProvider, FacebookAuthProvider, TwitterAuthProvider, GithubAuthProvider } from "firebase/auth";

   const googleProvider = new GoogleAuthProvider();
   const facebookProvider = new FacebookAuthProvider();
   const twitterProvider = new TwitterAuthProvider();
   const githubProvider = new GithubAuthProvider();
   ```

   ### Web

   ```javascript
   var googleProvider = new firebase.auth.GoogleAuthProvider();
   var facebookProvider = new firebase.auth.FacebookAuthProvider();
   var twitterProvider = new firebase.auth.TwitterAuthProvider();
   var githubProvider = new firebase.auth.GithubAuthProvider();
   ```
3. Prompt the user to sign in with the provider you want to link. You can prompt your users to sign in either by opening a pop-up window or by redirecting to the provider's sign-in page. The redirect method is preferred on mobile devices.
   - To sign in with a pop-up window, call `linkWithPopup`:

     ### Web

     ```javascript
     import { getAuth, linkWithPopup, GoogleAuthProvider } from "firebase/auth";
     const provider = new GoogleAuthProvider();

     const auth = getAuth();
     linkWithPopup(auth.currentUser, provider).then((result) => {
       // Accounts successfully linked.
       const credential = GoogleAuthProvider.credentialFromResult(result);
       const user = result.user;
       // ...
     }).catch((error) => {
       // Handle Errors here.
       // ...
     });
     ```

     ### Web

     ```javascript
     auth.currentUser.linkWithPopup(provider).then((result) => {
       // Accounts successfully linked.
       var credential = result.credential;
       var user = result.user;
       // ...
     }).catch((error) => {
       // Handle Errors here.
       // ...
     });
     ```
   - To sign in by redirecting to the provider's sign-in page, call `linkWithRedirect`: Follow the [best practices](https://firebase.google.com/docs/auth/web/redirect-best-practices) when using \`linkWithRedirect\`.

     ### Web

     ```javascript
     import { getAuth, linkWithRedirect, GoogleAuthProvider } from "firebase/auth";
     const provider = new GoogleAuthProvider();

     const auth = getAuth();
     linkWithRedirect(auth.currentUser, provider)
       .then(/* ... */)
       .catch(/* ... */);
     ```

     ### Web

     ```javascript
     auth.currentUser.linkWithRedirect(provider)
       .then(/* ... */)
       .catch(/* ... */);
     ```
     After the user signs in, they are redirected back to your page. Then, you can retrieve the sign-in result by calling `getRedirectResult` when your page loads:

     ### Web

     ```javascript
     import { getRedirectResult } from "firebase/auth";
     getRedirectResult(auth).then((result) => {
       const credential = GoogleAuthProvider.credentialFromResult(result);
       if (credential) {
         // Accounts successfully linked.
         const user = result.user;
         // ...
       }
     }).catch((error) => {
       // Handle Errors here.
       // ...
     });
     ```

     ### Web

     ```javascript
     auth.getRedirectResult().then((result) => {
       if (result.credential) {
         // Accounts successfully linked.
         var credential = result.credential;
         var user = result.user;
         // ...
       }
     }).catch((error) => {
       // Handle Errors here.
       // ...
     });
     ```

   If the user is signed in successfully, the user's account with the provider is linked to the user's account in your Firebase project.

   Account linking will fail if the credentials are
   already linked to another user account. In this situation, you must handle
   merging the accounts and associated data as appropriate for your app:

   ### Web

   ```javascript
   import { getAuth, signInWithCredential, linkWithCredential, OAuthProvider } from "firebase/auth";

   // The implementation of how you store your user data depends on your application
   const repo = new MyUserDataRepo();

   // Get reference to the currently signed-in user
   const auth = getAuth();
   const prevUser = auth.currentUser;

   // Get the data which you will want to merge. This should be done now
   // while the app is still signed in as this user.
   const prevUserData = repo.get(prevUser);

   // Delete the user's data now, we will restore it if the merge fails
   repo.delete(prevUser);

   // Sign in user with the account you want to link to
   signInWithCredential(auth, newCredential).then((result) => {
     console.log("Sign In Success", result);
     const currentUser = result.user;
     const currentUserData = repo.get(currentUser);

     // Merge prevUser and currentUser data stored in Firebase.
     // Note: How you handle this is specific to your application
     const mergedData = repo.merge(prevUserData, currentUserData);

     const credential = OAuthProvider.credentialFromResult(result);
     return linkWithCredential(prevUser, credential)
       .then((linkResult) => {
         // Sign in with the newly linked credential
         const linkCredential = OAuthProvider.credentialFromResult(linkResult);
         return signInWithCredential(auth, linkCredential);
       })
       .then((signInResult) => {
         // Save the merged data to the new user
         repo.set(signInResult.user, mergedData);
       });
   }).catch((error) => {
     // If there are errors we want to undo the data merge/deletion
     console.log("Sign In Error", error);
     repo.set(prevUser, prevUserData);
   });
   ```

   ### Web

   ```javascript
   // The implementation of how you store your user data depends on your application
   var repo = new MyUserDataRepo();

   // Get reference to the currently signed-in user
   var prevUser = auth.currentUser;

   // Get the data which you will want to merge. This should be done now
   // while the app is still signed in as this user.
   var prevUserData = repo.get(prevUser);

   // Delete the user's data now, we will restore it if the merge fails
   repo.delete(prevUser);

   // Sign in user with the account you want to link to
   auth.signInWithCredential(newCredential).then((result) => {
     console.log("Sign In Success", result);
     var currentUser = result.user;
     var currentUserData = repo.get(currentUser);

     // Merge prevUser and currentUser data stored in Firebase.
     // Note: How you handle this is specific to your application
     var mergedData = repo.merge(prevUserData, currentUserData);

     return prevUser.linkWithCredential(result.credential)
       .then((linkResult) => {
         // Sign in with the newly linked credential
         return auth.signInWithCredential(linkResult.credential);
       })
       .then((signInResult) => {
         // Save the merged data to the new user
         repo.set(signInResult.user, mergedData);
       });
   }).catch((error) => {
     // If there are errors we want to undo the data merge/deletion
     console.log("Sign In Error", error);
     repo.set(prevUser, prevUserData);
   });
   ```

## Link email address and password credentials to a user account

To add email address and password credentials to an existing user
account:

1. Sign in the user using any authentication provider or method.
2. Prompt the user for an email address and new password.
3. Create an `AuthCredential` object with the email address and password:

   ### Web

   ```javascript
   import { EmailAuthProvider } from "firebase/auth";

   const credential = EmailAuthProvider.credential(email, password);
   ```

   ### Web

   ```javascript
   var credential = firebase.auth.EmailAuthProvider.credential(email, password);
   ```
4. Pass the `AuthCredential` object to the signed-in user's
   `linkWithCredential` method:

   ### Web

   ```javascript
   import { getAuth, linkWithCredential } from "firebase/auth";

   const auth = getAuth();
   linkWithCredential(auth.currentUser, credential)
     .then((usercred) => {
       const user = usercred.user;
       console.log("Account linking success", user);
     }).catch((error) => {
       console.log("Account linking error", error);
     });
   ```

   ### Web

   ```javascript
   auth.currentUser.linkWithCredential(credential)
     .then((usercred) => {
       var user = usercred.user;
       console.log("Account linking success", user);
     }).catch((error) => {
       console.log("Account linking error", error);
     });
   ```

   The call to `linkWithCredential` will fail if the credentials are
   already linked to another user account. In this situation, you must handle
   merging the accounts and associated data as appropriate for your app (see example above).

## Unlink an auth provider from a user account

A single Firebase user account can have multiple authentication providers linked to it (for example, email/password, Google, Facebook), which lets the user sign in to the same Firebase account through different methods.

If you unlink an authentication provider from a user's account, they can no longer sign in with that provider.
**Important:** If a user signs in again with the same provider after it has been unlinked, Firebase creates a new, separate user account instead of restoring link to the original account.

To unlink an auth provider from a user account, pass the provider ID to the
`unlink` method. You can get the provider IDs of the auth providers
linked to a user from the `providerData` property.

### Web

```javascript
import { getAuth, unlink } from "firebase/auth";

const auth = getAuth();
unlink(auth.currentUser, providerId).then(() => {
  // Auth provider unlinked from account
  // ...
}).catch((error) => {
  // An error happened
  // ...
});
```

### Web

```javascript
user.unlink(providerId).then(() => {
  // Auth provider unlinked from account
  // ...
}).catch((error) => {
  // An error happened
  // ...
});
```

## Troubleshooting

If you encounter errors when trying to link multiple accounts, see the
[documentation on
verified email addresses](https://firebase.google.com/docs/auth/users#verified_email_addresses).