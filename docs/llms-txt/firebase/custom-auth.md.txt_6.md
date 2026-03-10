# Source: https://firebase.google.com/docs/auth/android/custom-auth.md.txt

You can integrate Firebase Authentication with a custom authentication system by
modifying your authentication server to produce custom signed tokens when a user
successfully signs in. Your app receives this token and uses it to authenticate
with Firebase.

## Before you begin

1. If you haven't already, [add Firebase to your Android project](https://firebase.google.com/docs/android/setup).
2. In your **module (app-level) Gradle file** (usually `<project>/<app-module>/build.gradle.kts` or `<project>/<app-module>/build.gradle`), add the dependency for the Firebase Authentication library for Android. We recommend using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom) to control library versioning.

   ```
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

       // Add the dependency for the Firebase Authentication library
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-auth")
   }
   ```

   By using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom),
   your app will always use compatible versions of Firebase Android libraries.
   *(Alternative)*
   Add Firebase library dependencies *without* using the BoM

   If you choose not to use the Firebase BoM, you must specify each Firebase library version
   in its dependency line.

   **Note that if you use *multiple* Firebase libraries in your app, we strongly
   recommend using the BoM to manage library versions, which ensures that all versions are
   compatible.**

   ```groovy
   dependencies {
       // Add the dependency for the Firebase Authentication library
       // When NOT using the BoM, you must specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-auth:24.0.1")
   }
   ```
3. Get your project's server keys:
   1. Go to the [Service Accounts](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk) page in your project's settings.
   2. Click *Generate New Private Key* at the bottom of the *Firebase Admin SDK* section of the *Service Accounts* page.
   3. The new service account's public/private key pair is automatically saved on your computer. Copy this file to your authentication server.

## Authenticate with Firebase

1. In your sign-in activity's `onCreate` method, get the shared instance of the `FirebaseAuth` object:

   ### Kotlin

   ```kotlin
   private lateinit var auth: FirebaseAuth
   // ...
   // Initialize Firebase Auth
   auth = Firebase.authhttps://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/CustomAuthActivity.kt#L27-L28
   ```

   ### Java

   ```java
   private FirebaseAuth mAuth;
   // ...
   // Initialize Firebase Auth
   mAuth = FirebaseAuth.getInstance();
   ```
2. When initializing your Activity, check to see if the user is currently signed in:

   ### Kotlin

   ```kotlin
   public override fun onStart() {
       super.onStart()
       // Check if user is signed in (non-null) and update UI accordingly.
       val currentUser = auth.currentUser
       updateUI(currentUser)
   }
   ```

   ### Java

   ```java
   @Override
   public void onStart() {
       super.onStart();
       // Check if user is signed in (non-null) and update UI accordingly.
       FirebaseUser currentUser = mAuth.getCurrentUser();
       updateUI(currentUser);
   }
   ```
3. When users sign in to your app, send their sign-in credentials (for example, their username and password) to your authentication server. Your server checks the credentials and returns a [custom token](https://firebase.google.com/docs/auth/admin/create-custom-tokens) if they are valid.
4. After you receive the custom token from your authentication server, pass it to `signInWithCustomToken` to sign in the user:

   ### Kotlin

   ```kotlin
   customToken?.let {
       auth.signInWithCustomToken(it)
           .addOnCompleteListener(this) { task ->
               if (task.isSuccessful) {
                   // Sign in success, update UI with the signed-in user's information
                   Log.d(TAG, "signInWithCustomToken:success")
                   val user = auth.currentUser
                   updateUI(user)
               } else {
                   // If sign in fails, display a message to the user.
                   Log.w(TAG, "signInWithCustomToken:failure", task.exception)
                   Toast.makeText(
                       baseContext,
                       "Authentication failed.",
                       Toast.LENGTH_SHORT,
                   ).show()
                   updateUI(null)
               }
           }
   }
   ```

   ### Java

   ```java
   mAuth.signInWithCustomToken(mCustomToken)
           .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
               @Override
               public void onComplete(@NonNull Task<AuthResult> task) {
                   if (task.isSuccessful()) {
                       // Sign in success, update UI with the signed-in user's information
                       Log.d(TAG, "signInWithCustomToken:success");
                       FirebaseUser user = mAuth.getCurrentUser();
                       updateUI(user);
                   } else {
                       // If sign in fails, display a message to the user.
                       Log.w(TAG, "signInWithCustomToken:failure", task.getException());
                       Toast.makeText(CustomAuthActivity.this, "Authentication failed.",
                               Toast.LENGTH_SHORT).show();
                       updateUI(null);
                   }
               }
           });
   ```
   If sign-in succeeds, the `AuthStateListener` you can use the `getCurrentUser` method to get the user's account data.

## Next steps

After a user signs in for the first time, a new user account is created and
linked to the credentials---that is, the user name and password, phone
number, or auth provider information---the user signed in with. This new
account is stored as part of your Firebase project, and can be used to identify
a user across every app in your project, regardless of how the user signs in.

- In your apps, you can get the user's basic profile information from the
  [`FirebaseUser`](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser) object. See [Manage Users](https://firebase.google.com/docs/auth/android/manage-users).

- In your Firebase Realtime Database and Cloud Storage
  [Security Rules](https://firebase.google.com/docs/database/security/user-security), you can
  get the signed-in user's unique user ID from the `auth` variable,
  and use it to control what data a user can access.

You can allow users to sign in to your app using multiple authentication
providers by [linking auth provider credentials to an
existing user account.](https://firebase.google.com/docs/auth/android/account-linking)

To sign out a user, call [`signOut`](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signOut()):

### Kotlin

```kotlin
Firebase.auth.signOut()
```

### Java

```java
FirebaseAuth.getInstance().signOut();
```