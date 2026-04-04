# Source: https://firebase.google.com/docs/auth/android/facebook-login.md.txt

You can let your users authenticate with Firebase using their Facebook accounts
by integrating Facebook Login into your app.

## Before you begin

1. If you haven't already,
   [add Firebase to your Android project](https://firebase.google.com/docs/android/setup).

2. On the [Facebook for Developers](https://developers.facebook.com/) site, get the **App ID** and an **App Secret** for your app.
3. Enable Facebook Login:
   1. In the [Firebase console](https://console.firebase.google.com/), open the **Authentication** section.
   2. On the **Sign in method** tab, enable the **Facebook** sign-in method and specify the **App ID** and **App Secret** you got from Facebook.
   3. Then, make sure your **OAuth redirect URI** (e.g. `my-app-12345.firebaseapp.com/__/auth/handler`) is listed as one of your **OAuth redirect URIs** in your Facebook app's settings page on the [Facebook for Developers](https://developers.facebook.com/) site in the **Product Settings \> Facebook Login** config.
4.


   In your **module (app-level) Gradle file**
   (usually `<project>/<app-module>/build.gradle.kts` or
   `<project>/<app-module>/build.gradle`),
   add the dependency for the Firebase Authentication library for Android. We recommend using the
   [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)
   to control library versioning.


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

   <br />

## Authenticate with Firebase

1. Integrate Facebook Login into your app by following the [developer's documentation](https://developers.facebook.com/docs/facebook-login/android). When you configure the `LoginButton` or `LoginManager` object, request the `public_profile` and `email` permissions. If you integrated Facebook Login using a `LoginButton`, your sign-in activity has code similar to the following:

   ### Kotlin

   ```kotlin
   // Initialize Facebook Login button
   callbackManager = CallbackManager.Factory.create()

   buttonFacebookLogin.setReadPermissions("email", "public_profile")
   buttonFacebookLogin.registerCallback(
       callbackManager,
       object : FacebookCallback<LoginResult> {
           override fun onSuccess(loginResult: LoginResult) {
               Log.d(TAG, "facebook:onSuccess:$loginResult")
               handleFacebookAccessToken(loginResult.accessToken)
           }

           override fun onCancel() {
               Log.d(TAG, "facebook:onCancel")
           }

           override fun onError(error: FacebookException) {
               Log.d(TAG, "facebook:onError", error)
           }
       },
   )
   // ...
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
       super.onActivityResult(requestCode, resultCode, data)

       // Pass the activity result back to the Facebook SDK
       callbackManager.onActivityResult(requestCode, resultCode, data)
   }
   ```

   ### Java

   ```java
   // Initialize Facebook Login button
   mCallbackManager = CallbackManager.Factory.create();
   LoginButton loginButton = findViewById(R.id.button_sign_in);
   loginButton.setReadPermissions("email", "public_profile");
   loginButton.registerCallback(mCallbackManager, new FacebookCallback<LoginResult>() {
       @Override
       public void onSuccess(LoginResult loginResult) {
           Log.d(TAG, "facebook:onSuccess:" + loginResult);
           handleFacebookAccessToken(loginResult.getAccessToken());
       }

       @Override
       public void onCancel() {
           Log.d(TAG, "facebook:onCancel");
       }

       @Override
       public void onError(FacebookException error) {
           Log.d(TAG, "facebook:onError", error);
       }
   });
   // ...
   @Override
   protected void onActivityResult(int requestCode, int resultCode, Intent data) {
       super.onActivityResult(requestCode, resultCode, data);

       // Pass the activity result back to the Facebook SDK
       mCallbackManager.onActivityResult(requestCode, resultCode, data);
   }
   ```
2. In your sign-in activity's `onCreate` method, get the shared instance of the `FirebaseAuth` object:

   ### Kotlin

   ```kotlin
   private lateinit var auth: FirebaseAuth
   // ...
   // Initialize Firebase Auth
   auth = Firebase.authhttps://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/FacebookLoginActivity.kt#L35-L36
   ```

   ### Java

   ```java
   private FirebaseAuth mAuth;
   // ...
   // Initialize Firebase Auth
   mAuth = FirebaseAuth.getInstance();
   ```
3. When initializing your Activity, check to see if the user is currently signed in:

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
4. After a user successfully signs in, in the `LoginButton`'s `onSuccess` callback method, get an access token for the signed-in user, exchange it for a Firebase credential, and authenticate with Firebase using the Firebase credential:

   ### Kotlin

   ```kotlin
   private fun handleFacebookAccessToken(token: AccessToken) {
       Log.d(TAG, "handleFacebookAccessToken:$token")

       val credential = FacebookAuthProvider.getCredential(token.token)
       auth.signInWithCredential(credential)
           .addOnCompleteListener(this) { task ->
               if (task.isSuccessful) {
                   // Sign in success, update UI with the signed-in user's information
                   Log.d(TAG, "signInWithCredential:success")
                   val user = auth.currentUser
                   updateUI(user)
               } else {
                   // If sign in fails, display a message to the user.
                   Log.w(TAG, "signInWithCredential:failure", task.exception)
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
   private void handleFacebookAccessToken(AccessToken token) {
       Log.d(TAG, "handleFacebookAccessToken:" + token);

       AuthCredential credential = FacebookAuthProvider.getCredential(token.getToken());
       mAuth.signInWithCredential(credential)
               .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
                   @Override
                   public void onComplete(@NonNull Task<AuthResult> task) {
                       if (task.isSuccessful()) {
                           // Sign in success, update UI with the signed-in user's information
                           Log.d(TAG, "signInWithCredential:success");
                           FirebaseUser user = mAuth.getCurrentUser();
                           updateUI(user);
                       } else {
                           // If sign in fails, display a message to the user.
                           Log.w(TAG, "signInWithCredential:failure", task.getException());
                           Toast.makeText(FacebookLoginActivity.this, "Authentication failed.",
                                   Toast.LENGTH_SHORT).show();
                           updateUI(null);
                       }
                   }
               });
   }
   ```
   If the call to `signInWithCredential` succeeds, you can use the `getCurrentUser` method to get the user's account data.

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