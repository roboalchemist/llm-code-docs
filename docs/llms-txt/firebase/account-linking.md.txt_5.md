# Source: https://firebase.google.com/docs/auth/android/account-linking.md.txt

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
2. Complete the sign-in flow for the new authentication provider up to, but not including, calling one of the [`FirebaseAuth.signInWith`](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#public-method-summary) methods. For example, get the user's Google ID token, Facebook access token, or email and password.
3. Get a `AuthCredential` for the new authentication provider:

   ##### Google Sign-In

   ### Kotlin

   ```kotlin
   val credential = GoogleAuthProvider.getCredential(googleIdToken, null)
   ```

   ### Java

   ```java
   AuthCredential credential = GoogleAuthProvider.getCredential(googleIdToken, null);
   ```

   ##### Facebook Login

   ### Kotlin

   ```kotlin
   val credential = FacebookAuthProvider.getCredential(token.token)
   ```

   ### Java

   ```java
   AuthCredential credential = FacebookAuthProvider.getCredential(token.getToken());
   ```

   ##### Email-password sign-in

   ### Kotlin

   ```kotlin
   val credential = EmailAuthProvider.getCredential(email, password)
   ```

   ### Java

   ```java
   AuthCredential credential = EmailAuthProvider.getCredential(email, password);
   ```
4. Pass the `AuthCredential` object to the signed-in user's
   `linkWithCredential` method:

   ### Kotlin

   ```kotlin
   auth.currentUser!!.linkWithCredential(credential)
       .addOnCompleteListener(this) { task ->
           if (task.isSuccessful) {
               Log.d(TAG, "linkWithCredential:success")
               val user = task.result?.user
               updateUI(user)
           } else {
               Log.w(TAG, "linkWithCredential:failure", task.exception)
               Toast.makeText(
                   baseContext,
                   "Authentication failed.",
                   Toast.LENGTH_SHORT,
               ).show()
               updateUI(null)
           }
       }
   ```

   ### Java

   ```java
   mAuth.getCurrentUser().linkWithCredential(credential)
           .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
               @Override
               public void onComplete(@NonNull Task<AuthResult> task) {
                   if (task.isSuccessful()) {
                       Log.d(TAG, "linkWithCredential:success");
                       FirebaseUser user = task.getResult().getUser();
                       updateUI(user);
                   } else {
                       Log.w(TAG, "linkWithCredential:failure", task.getException());
                       Toast.makeText(AnonymousAuthActivity.this, "Authentication failed.",
                               Toast.LENGTH_SHORT).show();
                       updateUI(null);
                   }
               }
           });
   ```

   The call to `linkWithCredential` will fail if the credentials are
   already linked to another user account. In this situation, you must handle
   merging the accounts and associated data as appropriate for your app:

   ### Kotlin

   ```kotlin
   val prevUser = auth.currentUser
   auth.signInWithCredential(credential)
       .addOnSuccessListener { result ->
           val currentUser = result.user
           // Merge prevUser and currentUser accounts and data
           // ...
       }
       .addOnFailureListener {
           // ...
       }
   ```

   ### Java

   ```java
   FirebaseUser prevUser = FirebaseAuth.getInstance().getCurrentUser();
   mAuth.signInWithCredential(credential)
           .addOnCompleteListener(new OnCompleteListener<AuthResult>() {
               @Override
               public void onComplete(@NonNull Task<AuthResult> task) {
                   FirebaseUser currentUser = task.getResult().getUser();
                   // Merge prevUser and currentUser accounts and data
                   // ...
               }
           });
   ```

If the call to `linkWithCredential` succeeds, the user can now sign in using
any linked authentication provider and access the same Firebase data.

## Unlink an auth provider from a user account

A single Firebase user account can have multiple authentication providers linked to it (for example, email/password, Google, Facebook), which lets the user sign in to the same Firebase account through different methods.

If you unlink an authentication provider from a user's account, they can no longer sign in with that provider.
**Important:** If a user signs in again with the same provider after it has been unlinked, Firebase creates a new, separate user account instead of restoring link to the original account.

To unlink an auth provider from a user account, pass the provider ID to the
`unlink` method. You can get the provider IDs of the auth providers
linked to a user by calling [`getProviderData`](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#getProviderData()).

### Kotlin

```kotlin
Firebase.auth.currentUser!!.unlink(providerId)
    .addOnCompleteListener(this) { task ->
        if (task.isSuccessful) {
            // Auth provider unlinked from account
            // ...
        }
    }
```

### Java

```java
mAuth.getCurrentUser().unlink(providerId)
        .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                if (task.isSuccessful()) {
                    // Auth provider unlinked from account
                    // ...
                }
            }
        });
```

## Troubleshooting

If you encounter errors when trying to link multiple accounts, see the
[documentation on
verified email addresses](https://firebase.google.com/docs/auth/users#verified_email_addresses).