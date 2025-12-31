# Source: https://firebase.google.com/docs/auth/web/yahoo-oauth.md.txt

# Source: https://firebase.google.com/docs/auth/unity/yahoo-oauth.md.txt

# Source: https://firebase.google.com/docs/auth/ios/yahoo-oauth.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/yahoo-oauth.md.txt

# Source: https://firebase.google.com/docs/auth/android/yahoo-oauth.md.txt

# Source: https://firebase.google.com/docs/auth/web/yahoo-oauth.md.txt

# Source: https://firebase.google.com/docs/auth/unity/yahoo-oauth.md.txt

# Source: https://firebase.google.com/docs/auth/ios/yahoo-oauth.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/yahoo-oauth.md.txt

# Source: https://firebase.google.com/docs/auth/android/yahoo-oauth.md.txt

You can let your users authenticate with Firebase using OAuth providers like Yahoo by integrating web-based generic OAuth Login into your app using the Firebase SDK to carry out the end to end sign-in flow.

## Before you begin

To sign in users using Yahoo accounts, you must first enable Yahoo as a sign-in provider for your Firebase project:

1. [Add Firebase to your Android project](https://firebase.google.com/docs/android/setup).

2. In the[Firebaseconsole](https://console.firebase.google.com/), open the**Auth**section.
3. On the**Sign in method** tab, enable the**Yahoo**provider.
4. Add the**Client ID** and**Client Secret** from that provider's developer console to the provider configuration:
   1. To register a Yahoo OAuth client, follow the Yahoo developer documentation on[registering a web application with Yahoo](https://developer.yahoo.com/oauth2/guide/openid_connect/getting_started.html).

      Be sure to select the two OpenID Connect API permissions:`profile`and`email`.
   2. When registering apps with these providers, be sure to register the`*.firebaseapp.com`domain for your project as the redirect domain for your app.
5. Click**Save**.
6. If you haven't yet specified your app's SHA-1 fingerprint, do so from the[Settings page](https://console.firebase.google.com/project/_/settings/general/)of theFirebaseconsole. Refer to[Authenticating Your Client](https://developers.google.com/android/guides/client-auth)for details on how to get your app's SHA-1 fingerprint.

## Handle the sign-in flow with the Firebase SDK

If you are building an Android app, the easiest way to authenticate your users with Firebase using their Yahoo accounts is to handle the entire sign-in flow with the Firebase Android SDK.

To handle the sign-in flow with the Firebase Android SDK, follow these steps:

1. Construct an instance of an**OAuthProvider** using its**Builder** with the provider ID**yahoo.com**.

   ### Kotlin

   <br />

   ```kotlin
   val provider = OAuthProvider.newBuilder("yahoo.com")https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GenericIdpActivity.kt#L81-L81
   ```

   <br />

   ### Java

   <br />

   ```java
   OAuthProvider.Builder provider = OAuthProvider.newBuilder("yahoo.com");https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/GenericIdpActivity.java#L94-L94
   ```

   <br />

2. **Optional**: Specify additional custom OAuth parameters that you want to send with the OAuth request.

   ### Kotlin

   <br />

   ```kotlin
   // Prompt user to re-authenticate to Yahoo.
   provider.addCustomParameter("prompt", "login")

   // Localize to French.
   provider.addCustomParameter("language", "fr")https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GenericIdpActivity.kt#L85-L89
   ```

   <br />

   ### Java

   <br />

   ```java
   // Prompt user to re-authenticate to Yahoo.
   provider.addCustomParameter("prompt", "login");

   // Localize to French.
   provider.addCustomParameter("language", "fr");https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/GenericIdpActivity.java#L99-L103
   ```

   <br />

   For the parameters Yahoo supports, see the[Yahoo OAuth documentation](https://developer.yahoo.com/oauth2/guide/openid_connect/getting_started.html). Note that you can't pass Firebase-required parameters with`setCustomParameters()`. These parameters are**client_id** ,**redirect_uri** ,**response_type** ,**scope** and**state**.
3. **Optional** : Specify additional OAuth 2.0 scopes beyond`profile`and`email`that you want to request from the authentication provider. If your application requires access to private user data from Yahoo APIs, you'll need to request permissions to Yahoo APIs under**API Permissions** in the Yahoo developer console. Requested OAuth scopes must be exact matches to the preconfigured ones in the app's API permissions. For example if, read/write access is requested to user contacts and preconfigured in the app's API permissions,`sdct-w`has to be passed instead of the readonly OAuth scope`sdct-r`. Otherwise,the flow will fail and an error would be shown to the end user.

   ### Kotlin

   <br />

   ```kotlin
   // Request read access to a user's email addresses.
   // This must be preconfigured in the app's API permissions.
   provider.scopes = listOf("mail-r", "sdct-w")https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GenericIdpActivity.kt#L93-L95
   ```

   <br />

   ### Java

   <br />

   ```java
   // Request read access to a user's email addresses.
   // This must be preconfigured in the app's API permissions.
   List<String> scopes =
           new ArrayList<String>() {
               {
                   // Request access to Yahoo Mail API.
                   add("mail-r");
                   // This must be preconfigured in the app's API permissions.
                   add("sdct-w");
               }
           };
   provider.setScopes(scopes);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/GenericIdpActivity.java#L108-L119
   ```
   To learn more, refer to the[Yahoo scopes documentation](https://developer.yahoo.com/oauth2/guide/yahoo_scopes/).

   <br />

4. Authenticate with Firebase using the OAuth provider object. Note that unlike other FirebaseAuth operations, this will take control of your UI by popping up a[Custom Chrome Tab](https://developer.chrome.com/multidevice/android/customtabs). As a result, do not reference your Activity in the OnSuccessListeners and OnFailureListeners that you attach as they will immediately detach when the operation starts the UI.

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

   Using the OAuth access token, you can call the[Yahoo API](https://developer.yahoo.com/oauth2/guide/apirequests/).

   Where`YAHOO_USER_UID`is the Yahoo user's ID which can be parsed from the`firebaseAuth.getCurrentUser().getProviderData().get(0).getUid()`field or from`authResult.getAdditionalUserInfo().getProfile()`.
5. While the above examples focus on sign-in flows, you also have the ability to link a Yahoo provider to an existing user using`startActivityForLinkWithProvider`. For example, you can link multiple providers to the same user allowing them to sign in with either.

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

6. The same pattern can be used with`startActivityForReauthenticateWithProvider`which can be used to retrieve fresh credentials for sensitive operations that require recent login.

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

## Advanced: Handle the sign-in flow manually

Unlike other OAuth providers supported by Firebase such as Google, Facebook, and Twitter, where sign-in can directly be achieved with OAuth access token based credentials, Firebase Auth does not support the same capability for providers such as Yahoo due to the inability of the Firebase Auth server to verify the audience of Yahoo OAuth access tokens. This is a critical security requirement and could expose applications and websites to replay attacks where a Yahoo OAuth access token obtained for one project (attacker) can be used to sign in to another project (victim). Instead, Firebase Auth offers the ability to handle the entire OAuth flow and the authorization code exchange using the OAuth client ID and secret configured in the Firebase Console. As the authorization code can only be used in conjunction with a specific client ID/secret, an authorization code obtained for one project cannot be used with another.

If these providers are required to be used in unsupported environments, a third party OAuth library and[Firebase custom authentication](https://firebase.google.com/docs/auth/admin/create-custom-tokens)would need to be used. The former is needed to authenticate with the provider and the latter to exchange the provider's credential for a custom token.

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