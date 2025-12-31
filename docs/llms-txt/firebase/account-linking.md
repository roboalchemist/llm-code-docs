# Source: https://firebase.google.com/docs/auth/web/account-linking.md.txt

# Source: https://firebase.google.com/docs/auth/unity/account-linking.md.txt

# Source: https://firebase.google.com/docs/auth/ios/account-linking.md.txt

# Source: https://firebase.google.com/docs/auth/flutter/account-linking.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/account-linking.md.txt

# Source: https://firebase.google.com/docs/auth/android/account-linking.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/account-linking.md.txt

# Source: https://firebase.google.com/docs/auth/android/account-linking.md.txt

| **Important** : There is a[known issue](https://github.com/firebase/firebase-js-sdk/issues/7675)that prevents`linkWithCredentials()`from working correctly in some projects. See the issue report for a workaround and the status of a fix.

You can allow users to sign in to your app using multiple authentication providers by linking auth provider credentials to an existing user account. Users are identifiable by the same Firebase user ID regardless of the authentication provider they used to sign in. For example, a user who signed in with a password can link a Google account and sign in with either method in the future. Or, an anonymous user can link a Facebook account and then, later, sign in with Facebook to continue using your app.

## Before you begin

Add support for two or more authentication providers (possibly including anonymous authentication) to your app.

## Link auth provider credentials to a user account

To link auth provider credentials to an existing user account:

1. Sign in the user using any authentication provider or method.
2. Complete the sign-in flow for the new authentication provider up to, but not including, calling one of the[`FirebaseAuth.signInWith`](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#public-method-summary)methods. For example, get the user's Google ID token, Facebook access token, or email and password.
3. Get a`AuthCredential`for the new authentication provider:

   ##### Google Sign-In

   ### Kotlin

   ```kotlin
   val credential = GoogleAuthProvider.getCredential(googleIdToken, null)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/MainActivity.kt#L394-L394
   ```

   ### Java

   ```java
   AuthCredential credential = GoogleAuthProvider.getCredential(googleIdToken, null);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/MainActivity.java#L479-L479
   ```

   ##### Facebook Login

   ### Kotlin

   ```kotlin
   val credential = FacebookAuthProvider.getCredential(token.token)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/MainActivity.kt#L401-L401
   ```

   ### Java

   ```java
   AuthCredential credential = FacebookAuthProvider.getCredential(token.getToken());https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/MainActivity.java#L487-L487
   ```

   ##### Email-password sign-in

   ### Kotlin

   ```kotlin
   val credential = EmailAuthProvider.getCredential(email, password)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/MainActivity.kt#L409-L409
   ```

   ### Java

   ```java
   AuthCredential credential = EmailAuthProvider.getCredential(email, password);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/MainActivity.java#L495-L495
   ```
4. Pass the`AuthCredential`object to the signed-in user's`linkWithCredential`method:

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
       }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/AnonymousAuthActivity.kt#L66-L81
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
           });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/AnonymousAuthActivity.java#L91-L106
   ```

   The call to`linkWithCredential`will fail if the credentials are already linked to another user account. In this situation, you must handle merging the accounts and associated data as appropriate for your app:  

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
       }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/MainActivity.kt#L250-L259
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
           });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/MainActivity.java#L303-L312
   ```

If the call to`linkWithCredential`succeeds, the user can now sign in using any linked authentication provider and access the same Firebase data.

## Unlink an auth provider from a user account

You can unlink an auth provider from an account, so that the user can no longer sign in with that provider.

To unlink an auth provider from a user account, pass the provider ID to the`unlink`method. You can get the provider IDs of the auth providers linked to a user by calling[`getProviderData`](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#getProviderData()).  

### Kotlin

```kotlin
Firebase.auth.currentUser!!.unlink(providerId)
    .addOnCompleteListener(this) { task ->
        if (task.isSuccessful) {
            // Auth provider unlinked from account
            // ...
        }
    }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/MainActivity.kt#L265-L271
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
        });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/MainActivity.java#L321-L330
```

## Troubleshooting

If you encounter errors when trying to link multiple accounts, see the[documentation on verified email addresses](https://firebase.google.com/docs/auth/users#verified_email_addresses).