# Source: https://firebase.google.com/docs/auth/web/twitter-login.md.txt

# Source: https://firebase.google.com/docs/auth/unity/twitter-login.md.txt

# Source: https://firebase.google.com/docs/auth/ios/twitter-login.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/twitter-login.md.txt

# Source: https://firebase.google.com/docs/auth/android/twitter-login.md.txt

# Source: https://firebase.google.com/docs/auth/unity/twitter-login.md.txt

# Source: https://firebase.google.com/docs/auth/ios/twitter-login.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/twitter-login.md.txt

# Source: https://firebase.google.com/docs/auth/android/twitter-login.md.txt

You can let your users authenticate with Firebase using their Twitter accounts by integrating web-based generic OAuth Login into your app using the Firebase SDK to carry out the end to end sign-in flow.

## Before you begin

To sign in users using Twitter accounts, you must first enable Twitter as a sign-in provider for your Firebase project:

1. If you haven't already,[add Firebase to your Android project](https://firebase.google.com/docs/android/setup).

2. In the[Firebaseconsole](https://console.firebase.google.com/), open the**Auth**section.
3. On the**Sign in method** tab, enable the**Twitter**provider.
4. Add the**API key** and**API secret** from that provider's developer console to the provider configuration:
   1. [Register your app](https://apps.twitter.com/)as a developer application on Twitter and get your app's OAuth**API key** and**API secret**.
   2. Make sure your Firebase**OAuth redirect URI** (e.g.`my-app-12345.firebaseapp.com/__/auth/handler`) is set as your**Authorization callback URL** in your app's settings page on your[Twitter app's config](https://apps.twitter.com/).
5. Click**Save**.
6. In your**module (app-level) Gradle file** (usually`<project>/<app-module>/build.gradle.kts`or`<project>/<app-module>/build.gradle`), add the dependency for theFirebase Authenticationlibrary for Android. We recommend using the[Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)to control library versioning.

   <br />

   ```carbon
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.7.0"))

       // Add the dependency for the Firebase Authentication library
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-auth")
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
   }
   ```

   <br />

7. If you haven't yet specified your app's SHA-1 fingerprint, do so from the[Settings page](https://console.firebase.google.com/project/_/settings/general/)of theFirebaseconsole. Refer to[Authenticating Your Client](https://developers.google.com/android/guides/client-auth)for details on how to get your app's SHA-1 fingerprint.

## Handle the sign-in flow with the Firebase SDK

If you are building an Android app, the easiest way to authenticate your users with Firebase using their Twitter accounts is to handle the entire sign-in flow with the Firebase Android SDK.

To handle the sign-in flow with the Firebase Android SDK, follow these steps:

1. Construct an instance of an**OAuthProvider** using its**Builder** with the provider ID**Twitter.com**

   ### Kotlin

   <br />

   ```kotlin
   val provider = OAuthProvider.newBuilder("twitter.com")https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GenericIdpActivity.kt#L24-L24
   ```

   <br />

   ### Java

   <br />

   ```java
   OAuthProvider.Builder provider = OAuthProvider.newBuilder("twitter.com");https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/GenericIdpActivity.java#L24-L24
   ```

   <br />

2. **Optional**: Specify additional custom OAuth parameters that you want to send with the OAuth request.

   ### Kotlin

   <br />

   ```kotlin
   // Localize to French.
   provider.addCustomParameter("lang", "fr")https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GenericIdpActivity.kt#L28-L29
   ```

   <br />

   ### Java

   <br />

   ```java
   // Localize to French.
   provider.addCustomParameter("lang", "fr");https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/GenericIdpActivity.java#L28-L29
   ```

   <br />

   For the parameters Twitter supports, see the[Twitter OAuth documentation](https://www.google.com/url?q=https://developer.twitter.com/en/docs/basics/authentication/guides/authorizing-a-request&usg=AFQjCNG0rNdIaYnGfs5odh4bN7brggMOoA). Note that you can't pass Firebase-required parameters with`setCustomParameters()`. These parameters are**client_id** ,**response_type** ,**redirect_uri** ,**state** ,**scope** and**response_mode**.
3. Authenticate with Firebase using the OAuth provider object. Note that unlike other FirebaseAuth operations, this will take control of your UI by popping up a[Custom Chrome Tab](https://developer.chrome.com/multidevice/android/customtabs). As a result, do not reference your Activity in the`OnSuccessListener`and`OnFailureListener`that you attach as they will immediately detach when the operation starts the UI.

   You should first check if you've already received a response. Signing in via this method puts your Activity in the background, which means that it can be reclaimed by the system during the sign in flow. In order to make sure that you don't make the user try again if this happens, you should check if a result is already present.

   To check if there is a pending result, call`getPendingAuthResult`:  

   ### Kotlin

   <br />

   ```kotlin
   val pendingResultTask = firebaseAuth.pendingAuthResult
   if (pendingResultTask != null) {
       // There's something already here! Finish the sign-in for your user.
       pendingResultTask
           .addOnSuccessListener {
               // User is signed in.
               // IdP data available in
               // authResult.getAdditionalUserInfo().getProfile().
               // The OAuth access token can also be retrieved:
               // ((OAuthCredential)authResult.getCredential()).getAccessToken().
               // The OAuth secret can be retrieved by calling:
               // ((OAuthCredential)authResult.getCredential()).getSecret().
           }
           .addOnFailureListener {
               // Handle failure.
           }
   } else {
       // There's no pending result so you need to start the sign-in flow.
       // See below.
   }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GenericIdpActivity.kt#L118-L137
   ```

   <br />

   ### Java

   <br />

   ```java
   Task<AuthResult> pendingResultTask = firebaseAuth.getPendingAuthResult();
   if (pendingResultTask != null) {
       // There's something already here! Finish the sign-in for your user.
       pendingResultTask
               .addOnSuccessListener(
                       new OnSuccessListener<AuthResult>() {
                           @Override
                           public void onSuccess(AuthResult authResult) {
                               // User is signed in.
                               // IdP data available in
                               // authResult.getAdditionalUserInfo().getProfile().
                               // The OAuth access token can also be retrieved:
                               // ((OAuthCredential)authResult.getCredential()).getAccessToken().
                               // The OAuth secret can be retrieved by calling:
                               // ((OAuthCredential)authResult.getCredential()).getSecret().
                           }
                       })
               .addOnFailureListener(
                       new OnFailureListener() {
                           @Override
                           public void onFailure(@NonNull Exception e) {
                               // Handle failure.
                           }
                       });
   } else {
       // There's no pending result so you need to start the sign-in flow.
       // See below.
   }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/GenericIdpActivity.java#L151-L178
   ```

   <br />

   To start the sign in flow, call`startActivityForSignInWithProvider`:  

   ### Kotlin

   <br />

   ```kotlin
   firebaseAuth
       .startActivityForSignInWithProvider(activity, provider.build())
       .addOnSuccessListener {
           // User is signed in.
           // IdP data available in
           // authResult.getAdditionalUserInfo().getProfile().
           // The OAuth access token can also be retrieved:
           // ((OAuthCredential)authResult.getCredential()).getAccessToken().
           // The OAuth secret can be retrieved by calling:
           // ((OAuthCredential)authResult.getCredential()).getSecret().
       }
       .addOnFailureListener {
           // Handle failure.
       }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GenericIdpActivity.kt#L143-L156
   ```

   <br />

   ### Java

   <br />

   ```java
   firebaseAuth
           .startActivityForSignInWithProvider(/* activity= */ this, provider.build())
           .addOnSuccessListener(
                   new OnSuccessListener<AuthResult>() {
                       @Override
                       public void onSuccess(AuthResult authResult) {
                           // User is signed in.
                           // IdP data available in
                           // authResult.getAdditionalUserInfo().getProfile().
                           // The OAuth access token can also be retrieved:
                           // ((OAuthCredential)authResult.getCredential()).getAccessToken().
                           // The OAuth secret can be retrieved by calling:
                           // ((OAuthCredential)authResult.getCredential()).getSecret().
                       }
                   })
           .addOnFailureListener(
                   new OnFailureListener() {
                       @Override
                       public void onFailure(@NonNull Exception e) {
                           // Handle failure.
                       }
                   });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/GenericIdpActivity.java#L184-L205
   ```

   <br />

   On successful completion, the OAuth access token associated with the provider can be retrieved from the`OAuthCredential`object returned.

   Using the OAuth access token, you can call the[Twitter API](https://developer.Twitter.com/apps/building-oauth-apps/authorizing-oauth-apps/).

   For example, to get basic profile information, you can call the REST API, passing the access token in the`Authorization`header:
4. While the above examples focus on sign-in flows, you also have the ability to link a Twitter provider to an existing user using`startActivityForLinkWithProvider`. For example, you can link multiple providers to the same user allowing them to sign in with either.

   ### Kotlin

   <br />

   ```kotlin
   // The user is already signed-in.
   val firebaseUser = firebaseAuth.currentUser!!
   firebaseUser
       .startActivityForLinkWithProvider(activity, provider.build())
       .addOnSuccessListener {
           // Provider credential is linked to the current user.
           // IdP data available in
           // authResult.getAdditionalUserInfo().getProfile().
           // The OAuth access token can also be retrieved:
           // authResult.getCredential().getAccessToken().
           // The OAuth secret can be retrieved by calling:
           // authResult.getCredential().getSecret().
       }
       .addOnFailureListener {
           // Handle failure.
       }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GenericIdpActivity.kt#L162-L177
   ```

   <br />

   ### Java

   <br />

   ```java
   // The user is already signed-in.
   FirebaseUser firebaseUser = firebaseAuth.getCurrentUser();

   firebaseUser
           .startActivityForLinkWithProvider(/* activity= */ this, provider.build())
           .addOnSuccessListener(
                   new OnSuccessListener<AuthResult>() {
                       @Override
                       public void onSuccess(AuthResult authResult) {
                           // Provider credential is linked to the current user.
                           // IdP data available in
                           // authResult.getAdditionalUserInfo().getProfile().
                           // The OAuth access token can also be retrieved:
                           // authResult.getCredential().getAccessToken().
                           // The OAuth secret can be retrieved by calling:
                           // authResult.getCredential().getSecret().
                       }
                   })
           .addOnFailureListener(
                   new OnFailureListener() {
                       @Override
                       public void onFailure(@NonNull Exception e) {
                           // Handle failure.
                       }
                   });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/GenericIdpActivity.java#L211-L235
   ```

   <br />

5. The same pattern can be used with`startActivityForReauthenticateWithProvider`which can be used to retrieve fresh credentials for sensitive operations that require recent login.

   ### Kotlin

   <br />

   ```kotlin
   // The user is already signed-in.
   val firebaseUser = firebaseAuth.currentUser!!
   firebaseUser
       .startActivityForReauthenticateWithProvider(activity, provider.build())
       .addOnSuccessListener {
           // User is re-authenticated with fresh tokens and
           // should be able to perform sensitive operations
           // like account deletion and email or password
           // update.
       }
       .addOnFailureListener {
           // Handle failure.
       }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GenericIdpActivity.kt#L183-L195
   ```

   <br />

   ### Java

   <br />

   ```java
   // The user is already signed-in.
   FirebaseUser firebaseUser = firebaseAuth.getCurrentUser();

   firebaseUser
           .startActivityForReauthenticateWithProvider(/* activity= */ this, provider.build())
           .addOnSuccessListener(
                   new OnSuccessListener<AuthResult>() {
                       @Override
                       public void onSuccess(AuthResult authResult) {
                           // User is re-authenticated with fresh tokens and
                           // should be able to perform sensitive operations
                           // like account deletion and email or password
                           // update.
                       }
                   })
           .addOnFailureListener(
                   new OnFailureListener() {
                       @Override
                       public void onFailure(@NonNull Exception e) {
                           // Handle failure.
                       }
                   });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/GenericIdpActivity.java#L241-L262
   ```

   <br />

## Next steps

After a user signs in for the first time, a new user account is created and linked to the credentials---that is, the user name and password, phone number, or auth provider information---the user signed in with. This new account is stored as part of your Firebase project, and can be used to identify a user across every app in your project, regardless of how the user signs in.

- In your apps, you can get the user's basic profile information from the[`FirebaseUser`](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser)object. See[Manage Users](https://firebase.google.com/docs/auth/android/manage-users).

- In yourFirebase Realtime DatabaseandCloud Storage[Security Rules](https://firebase.google.com/docs/database/security/user-security), you can get the signed-in user's unique user ID from the`auth`variable, and use it to control what data a user can access.

You can allow users to sign in to your app using multiple authentication providers by[linking auth provider credentials to an existing user account.](https://firebase.google.com/docs/auth/android/account-linking)

To sign out a user, call[`signOut`](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signOut()):  

### Kotlin

```kotlin
Firebase.auth.signOut()https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/MainActivity.kt#L415-L415
```

### Java

```java
FirebaseAuth.getInstance().signOut();https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/MainActivity.java#L501-L501
```