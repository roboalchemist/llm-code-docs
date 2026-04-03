# Source: https://firebase.google.com/docs/auth/unity/google-signin.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/google-signin.md.txt

# Source: https://firebase.google.com/docs/auth/web/google-signin.md.txt

# Source: https://firebase.google.com/docs/auth/ios/google-signin.md.txt

# Source: https://firebase.google.com/docs/auth/android/google-signin.md.txt

# Source: https://firebase.google.com/docs/auth/web/google-signin.md.txt

# Source: https://firebase.google.com/docs/auth/ios/google-signin.md.txt

# Source: https://firebase.google.com/docs/auth/android/google-signin.md.txt

You can let your users authenticate with Firebase using their Google Accounts.

## Before you begin

1. If you haven't already,[add Firebase to your Android project](https://firebase.google.com/docs/android/setup).

2. In your**module (app-level) Gradle file** (usually`<project>/<app-module>/build.gradle.kts`or`<project>/<app-module>/build.gradle`), add the dependency for theFirebase Authenticationlibrary for Android. We recommend using the[Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)to control library versioning.

   Also, as part of setting upFirebase Authentication, you need to add the Credential Manager SDK to your app.

   <br />

   ```carbon
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.7.0"))

       // Add the dependency for the Firebase Authentication library
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-auth")

       // Also add the dependencies for the Credential Manager libraries and specify their versions
       implementation("androidx.credentials:credentials:1.3.0")
       implementation("androidx.credentials:credentials-play-services-auth:1.3.0")
       implementation("com.google.android.libraries.identity.googleid:googleid:1.1.1")
   }
   ```

   By using the[Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom), your app will always use compatible versions of Firebase Android libraries.
   *(Alternative)* Add Firebase library dependencies*without* using theBoM

   If you choose not to use theFirebase BoM, you must specify each Firebase library version in its dependency line.

   **Note that if you use*multiple* Firebase libraries in your app, we strongly recommend using theBoMto manage library versions, which ensures that all versions are compatible.**  

   ```groovy
   dependencies {
       // Add the dependency for the Firebase Authentication library
       // When NOT using the BoM, you must specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-auth:24.0.1")

       // Also add the dependencies for the Credential Manager libraries and specify their versions
       implementation("androidx.credentials:credentials:1.3.0")
       implementation("androidx.credentials:credentials-play-services-auth:1.3.0")
       implementation("com.google.android.libraries.identity.googleid:googleid:1.1.1")
   }
   ```

   <br />

3. If you haven't yet specified your app's SHA fingerprint, do so from the[Settings page](https://console.firebase.google.com/project/_/settings/general/)of theFirebaseconsole. Refer to[Authenticating Your Client](https://developers.google.com/android/guides/client-auth)for details on how to get your app's SHA fingerprint.

4. Enable Google as a sign-in method in theFirebaseconsole:
   1. In the[Firebaseconsole](https://console.firebase.google.com/), open the**Auth**section.
   2. On the**Sign in method** tab, enable the**Google** sign-in method and click**Save**.
5. When prompted in the console, download the updated Firebase config file (`google-services.json`), which now contains the OAuth client information required for Google sign-in.

6. Move this updated config file into your Android Studio project,*replacing* the now-outdated corresponding config file. (See[Add Firebase to your Android project](https://firebase.google.com/docs/android/setup#add-config-file).)

## Authenticate with Firebase

1. Integrate Sign in with Google into your app by following the steps in the[Credential Manager documentation](https://developer.android.com/identity/sign-in/credential-manager-siwg). Here are the high-level instructions:
   1. Instantiate a Google sign in request using`GetGoogleIdOption`. Then, create the Credential Manager request using`GetCredentialRequest`:  

      ### Kotlin

      ```kotlin
      // Instantiate a Google sign-in request
      val googleIdOption = GetGoogleIdOption.Builder()
          // Your server's client ID, not your Android client ID.
          .setServerClientId(getString(R.string.default_web_client_id))
          // Only show accounts previously used to sign in.
          .setFilterByAuthorizedAccounts(true)
          .build()

      // Create the Credential Manager request
      val request = GetCredentialRequest.Builder()
          .addCredentialOption(googleIdOption)
          .build()https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GoogleSignInActivity.kt#L66-L77
      ```

      ### Java

      ```java
      // Instantiate a Google sign-in request
      GetGoogleIdOption googleIdOption = new GetGoogleIdOption.Builder()
              .setFilterByAuthorizedAccounts(true)
              .setServerClientId(getString(R.string.default_web_client_id))
              .build();

      // Create the Credential Manager request
      GetCredentialRequest request = new GetCredentialRequest.Builder()
              .addCredentialOption(googleIdOption)
              .build();https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/GoogleSignInActivity.java#L88-L97
      ```

      In the request above, you must pass your "server" client ID to the`setServerClientId`method. To find the OAuth 2.0 client ID:
      1. Open the[Credentials page](https://console.cloud.google.com/apis/credentials)in theGoogle Cloudconsole.
      2. The**Web application**type client ID is your backend server's OAuth 2.0 client ID.
   2. Check that after you integrate Sign in with Google, your sign-in activity has code similar to the following:  

      ### Kotlin

      ```kotlin
      private fun handleSignIn(credential: Credential) {
          // Check if credential is of type Google ID
          if (credential is CustomCredential && credential.type == TYPE_GOOGLE_ID_TOKEN_CREDENTIAL) {
              // Create Google ID Token
              val googleIdTokenCredential = GoogleIdTokenCredential.createFrom(credential.data)

              // Sign in to Firebase with using the token
              firebaseAuthWithGoogle(googleIdTokenCredential.idToken)
          } else {
              Log.w(TAG, "Credential is not of type Google ID!")
          }
      }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GoogleSignInActivity.kt#L97-L108
      ```

      ### Java

      ```java
      private void handleSignIn(Credential credential) {
          // Check if credential is of type Google ID
          if (credential instanceof CustomCredential customCredential
                  && credential.getType().equals(TYPE_GOOGLE_ID_TOKEN_CREDENTIAL)) {
              // Create Google ID Token
              Bundle credentialData = customCredential.getData();
              GoogleIdTokenCredential googleIdTokenCredential = GoogleIdTokenCredential.createFrom(credentialData);

              // Sign in to Firebase with using the token
              firebaseAuthWithGoogle(googleIdTokenCredential.getIdToken());
          } else {
              Log.w(TAG, "Credential is not of type Google ID!");
          }
      }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/GoogleSignInActivity.java#L122-L135
      ```
2. In your sign-in activity's`onCreate`method, get the shared instance of the`FirebaseAuth`object:  

   ### Kotlin

   ```kotlin
   private lateinit var auth: FirebaseAuth
   // ...
   // Initialize Firebase Auth
   auth = Firebase.auth  
   https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GoogleSignInActivity.kt#L42-L43
   ```

   ### Java

   ```java
   private FirebaseAuth mAuth;
   // ...
   // Initialize Firebase Auth
   mAuth = FirebaseAuth.getInstance();https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/GoogleSignInActivity.java#L64-L65
   ```
3. When initializing your Activity, check to see if the user is currently signed in:  

   ### Kotlin

   ```kotlin
   override fun onStart() {
       super.onStart()
       // Check if user is signed in (non-null) and update UI accordingly.
       val currentUser = auth.currentUser
       updateUI(currentUser)
   }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GoogleSignInActivity.kt#L55-L60
   ```

   ### Java

   ```java
   @Override
   public void onStart() {
       super.onStart();
       // Check if user is signed in (non-null) and update UI accordingly.
       FirebaseUser currentUser = mAuth.getCurrentUser();
       updateUI(currentUser);
   }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/GoogleSignInActivity.java#L77-L83
   ```
4. Now get the user's Google ID token created in step 1, exchange it for a Firebase credential, and authenticate with Firebase using the Firebase credential:  

   ### Kotlin

   ```kotlin
   private fun firebaseAuthWithGoogle(idToken: String) {
       val credential = GoogleAuthProvider.getCredential(idToken, null)
       auth.signInWithCredential(credential)
           .addOnCompleteListener(this) { task ->
               if (task.isSuccessful) {
                   // Sign in success, update UI with the signed-in user's information
                   Log.d(TAG, "signInWithCredential:success")
                   val user = auth.currentUser
                   updateUI(user)
               } else {
                   // If sign in fails, display a message to the user
                   Log.w(TAG, "signInWithCredential:failure", task.exception)
                   updateUI(null)
               }
           }
   }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GoogleSignInActivity.kt#L112-L127
   ```

   ### Java

   ```java
   private void firebaseAuthWithGoogle(String idToken) {
       AuthCredential credential = GoogleAuthProvider.getCredential(idToken, null);
       mAuth.signInWithCredential(credential)
               .addOnCompleteListener(this, task -> {
                   if (task.isSuccessful()) {
                       // Sign in success, update UI with the signed-in user's information
                       Log.d(TAG, "signInWithCredential:success");
                       FirebaseUser user = mAuth.getCurrentUser();
                       updateUI(user);
                   } else {
                       // If sign in fails, display a message to the user
                       Log.w(TAG, "signInWithCredential:failure", task.getException());
                       updateUI(null);
                   }
               });
   }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/GoogleSignInActivity.java#L139-L154
   ```
   If the call to`signInWithCredential`succeeds you can use the`getCurrentUser`method to get the user's account data.

## Next steps

After a user signs in for the first time, a new user account is created and linked to the credentials---that is, the user name and password, phone number, or auth provider information---the user signed in with. This new account is stored as part of your Firebase project, and can be used to identify a user across every app in your project, regardless of how the user signs in.

- In your apps, you can get the user's basic profile information from the[`FirebaseUser`](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser)object. See[Manage Users](https://firebase.google.com/docs/auth/android/manage-users).

- In yourFirebase Realtime DatabaseandCloud Storage[Security Rules](https://firebase.google.com/docs/database/security/user-security), you can get the signed-in user's unique user ID from the`auth`variable, and use it to control what data a user can access.

You can allow users to sign in to your app using multiple authentication providers by[linking auth provider credentials to an existing user account.](https://firebase.google.com/docs/auth/android/account-linking)

To sign out a user, call[`signOut`](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signOut()). You also need to clear the current user credential state from all credential providers, as recommended by[the Credential Manager documentation](https://developer.android.com/identity/sign-in/credential-manager-siwg#handle-sign-out):  

### Kotlin

```kotlin
private fun signOut() {
    // Firebase sign out
    auth.signOut()

    // When a user signs out, clear the current user credential state from all credential providers.
    lifecycleScope.launch {
        try {
            val clearRequest = ClearCredentialStateRequest()
            credentialManager.clearCredentialState(clearRequest)
            updateUI(null)
        } catch (e: ClearCredentialException) {
            Log.e(TAG, "Couldn't clear user credentials: ${e.localizedMessage}")
        }
    }
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GoogleSignInActivity.kt#L131-L145
```

### Java

```java
private void signOut() {
    // Firebase sign out
    mAuth.signOut();

    // When a user signs out, clear the current user credential state from all credential providers.
    ClearCredentialStateRequest clearRequest = new ClearCredentialStateRequest();
    credentialManager.clearCredentialStateAsync(
            clearRequest,
            new CancellationSignal(),
            Executors.newSingleThreadExecutor(),
            new CredentialManagerCallback<>() {
                @Override
                public void onResult(@NonNull Void result) {
                    updateUI(null);
                }

                @Override
                public void onError(@NonNull ClearCredentialException e) {
                    Log.e(TAG, "Couldn't clear user credentials: " + e.getLocalizedMessage());
                }
            });
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/GoogleSignInActivity.java#L158-L179
```