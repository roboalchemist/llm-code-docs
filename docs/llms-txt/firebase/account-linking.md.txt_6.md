# Source: https://firebase.google.com/docs/auth/cpp/account-linking.md.txt

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

## Link auth provider credentials to a user account

To link auth provider credentials to an existing user account:

1. Sign in the user using any authentication provider or method.
2. Complete the sign-in flow for the new authentication provider up to, but not including, calling one of the [`firebase::auth::Auth::SignInWithCredential`](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#signinwithcredential) methods. For example, get the user's Google ID token, Facebook access token, or email and password.
3. Get a `firebase::auth::Credential` for the new authentication provider:

   **Google Sign-In**

   ```c++
   firebase::auth::Credential credential =
       firebase::auth::GoogleAuthProvider::GetCredential(google_id_token,
                                                         nullptr);
   ```
   **Facebook Login**

   ```c++
   firebase::auth::Credential credential =
       firebase::auth::FacebookAuthProvider::GetCredential(access_token);
   ```
   **Email-password sign-in**

   ```c++
   firebase::auth::Credential credential =
       firebase::auth::EmailAuthProvider::GetCredential(email, password);
   ```
4. Pass the `firebase::auth::Credential` object to the signed-in user's
   `LinkWithCredential` method:

   ```c++
   // Link the new credential to the currently active user.
   firebase::auth::User current_user = auth->current_user();
   firebase::Future<firebase::auth::AuthResult> result =
       current_user.LinkWithCredential(credential);
   ```

   The call to `LinkWithCredential` will fail if the credentials are
   already linked to another user account. In this situation, you must handle
   merging the accounts and associated data as appropriate for your app:

   ```c++
   // Gather data for the currently signed in User.
   firebase::auth::User current_user = auth->current_user();
   std::string current_email = current_user.email();
   std::string current_provider_id = current_user.provider_id();
   std::string current_display_name = current_user.display_name();
   std::string current_photo_url = current_user.photo_url();

   // Sign in with the new credentials.
   firebase::Future<firebase::auth::AuthResult> result =
       auth->SignInAndRetrieveDataWithCredential(credential);

   // To keep example simple, wait on the current thread until call completes.
   while (result.status() == firebase::kFutureStatusPending) {
     Wait(100);
   }

   // The new User is now active.
   if (result.error() == firebase::auth::kAuthErrorNone) {
     firebase::auth::User* new_user = *result.result();

     // Merge new_user with the user in details.
     // ...
     (void)new_user;
   }
   ```

If the call to `LinkWithCredential` succeeds, the user can now sign in using
any linked authentication provider and access the same Firebase data.

## Unlink an auth provider from a user account

A single Firebase user account can have multiple authentication providers linked to it (for example, email/password, Google, Facebook), which lets the user sign in to the same Firebase account through different methods.

If you unlink an authentication provider from a user's account, they can no longer sign in with that provider.
**Important:** If a user signs in again with the same provider after it has been unlinked, Firebase creates a new, separate user account instead of restoring link to the original account.

To unlink an auth provider from a user account, pass the provider ID to the
`Unlink` method. You can get the provider IDs of the auth providers
linked to a user by calling [`ProviderData`](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#providerdata).

```c++
// Unlink the sign-in provider from the currently active user.
firebase::auth::User current_user = auth->current_user();
firebase::Future<firebase::auth::AuthResult> result =
    current_user.Unlink(providerId);
```

## Troubleshooting

If you encounter errors when trying to link multiple accounts, see the
[documentation on
verified email addresses](https://firebase.google.com/docs/auth/users#verified_email_addresses).