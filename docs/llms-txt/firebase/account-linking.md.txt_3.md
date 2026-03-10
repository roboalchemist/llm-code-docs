# Source: https://firebase.google.com/docs/auth/unity/account-linking.md.txt

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
The `FirebaseAuth` class is the gateway for all API calls. It is accessible through [FirebaseAuth.DefaultInstance](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#defaultinstance).

```c#
Firebase.Auth.FirebaseAuth auth = Firebase.Auth.FirebaseAuth.DefaultInstance;
```

## Link auth provider credentials to a user account

To link auth provider credentials to an existing user account:

1. Sign in the user using any authentication provider or method.
2. Complete the sign-in flow for the new authentication provider up to, but not including, calling one of the [`Firebase.Auth.FirebaseAuth.SignInAndRetrieveDataWithCredentialAsync`](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#signinandretrievedatawithcredentialasync) methods. For example, get the user's Google ID token, Facebook access token, or email and password.
3. Get a `Firebase.Auth.Credential` for the new authentication provider:

   **Google Sign-In**

   ```c#
   Firebase.Auth.Credential credential =
       Firebase.Auth.GoogleAuthProvider.GetCredential(googleIdToken, googleAccessToken);
   ```
   **Facebook Login**

   ```c#
   Firebase.Auth.Credential credential =
       Firebase.Auth.FacebookAuthProvider.GetCredential(accessToken);
   ```
   **Email-password sign-in**

   ```c#
   Firebase.Auth.Credential credential =
       Firebase.Auth.EmailAuthProvider.GetCredential(email, password);
   ```
4. Pass the `Firebase.Auth.Credential` object to the signed-in user's
   `LinkWithCredentialAsync` method:

   ```c#
   auth.CurrentUser.LinkWithCredentialAsync(credential).ContinueWith(task => {
     if (task.IsCanceled) {
       Debug.LogError("LinkWithCredentialAsync was canceled.");
       return;
     }
     if (task.IsFaulted) {
       Debug.LogError("LinkWithCredentialAsync encountered an error: " + task.Exception);
       return;
     }

     Firebase.Auth.AuthResult result = task.Result;
     Debug.LogFormat("Credentials successfully linked to Firebase user: {0} ({1})",
         result.User.DisplayName, result.User.UserId);
   });
   ```

   The call to `LinkWithCredentialAsync` will fail if the credentials are
   already linked to another user account. In this situation, you must handle
   merging the accounts and associated data as appropriate for your app:

   ```c#
   // Gather data for the currently signed in User.
   string currentUserId = auth.CurrentUser.UserId;
   string currentEmail = auth.CurrentUser.Email;
   string currentDisplayName = auth.CurrentUser.DisplayName;
   System.Uri currentPhotoUrl = auth.CurrentUser.PhotoUrl;

   // Sign in with the new credentials.
   auth.SignInAndRetrieveDataWithCredentialAsync(credential).ContinueWith(task => {
     if (task.IsCanceled) {
       Debug.LogError("SignInAndRetrieveDataWithCredentialAsync was canceled.");
       return;
     }
     if (task.IsFaulted) {
       Debug.LogError("SignInAndRetrieveDataWithCredentialAsync encountered an error: " + task.Exception);
       return;
     }

     Firebase.Auth.AuthResult result = task.Result;
     Debug.LogFormat("User signed in successfully: {0} ({1})",
         result.User.DisplayName, result.User.UserId);

     // TODO: Merge app specific details using the newUser and values from the
     // previous user, saved above.
   });
   ```

If the call to `LinkWithCredentialAsync` succeeds, the user can now sign in using
any linked authentication provider and access the same Firebase data.

## Unlink an auth provider from a user account

A single Firebase user account can have multiple authentication providers linked to it (for example, email/password, Google, Facebook), which lets the user sign in to the same Firebase account through different methods.

If you unlink an authentication provider from a user's account, they can no longer sign in with that provider.
**Important:** If a user signs in again with the same provider after it has been unlinked, Firebase creates a new, separate user account instead of restoring link to the original account.

To unlink an auth provider from a user account, pass the provider ID to the
`UnlinkAsync` method. You can get the provider IDs of the auth
providers linked to a user by calling
[`ProviderData`](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#providerdata).

```c#
// Unlink the sign-in provider from the currently active user.
// providerIdString is a string identifying a provider,
// retrieved via FirebaseAuth.FetchProvidersForEmail().
auth.CurrentUser.UnlinkAsync(providerIdString).ContinueWith(task => {
  if (task.IsCanceled) {
    Debug.LogError("UnlinkAsync was canceled.");
    return;
  }
  if (task.IsFaulted) {
    Debug.LogError("UnlinkAsync encountered an error: " + task.Exception);
    return;
  }

  // The user has been unlinked from the provider.
  Firebase.Auth.AuthResult result = task.Result;
  Debug.LogFormat("Credentials successfully unlinked from user: {0} ({1})",
      result.User.DisplayName, result.User.UserId);
});
```

## Troubleshooting

If you encounter errors when trying to link multiple accounts, see the
[documentation on
verified email addresses](https://firebase.google.com/docs/auth/users#verified_email_addresses).