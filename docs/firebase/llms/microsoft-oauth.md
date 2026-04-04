# Source: https://firebase.google.com/docs/auth/web/microsoft-oauth.md.txt

# Source: https://firebase.google.com/docs/auth/unity/microsoft-oauth.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/microsoft-oauth.md.txt

# Source: https://firebase.google.com/docs/auth/ios/microsoft-oauth.md.txt

# Source: https://firebase.google.com/docs/auth/android/microsoft-oauth.md.txt

# Source: https://firebase.google.com/docs/auth/ios/microsoft-oauth.md.txt

# Source: https://firebase.google.com/docs/auth/android/microsoft-oauth.md.txt

You can let your users authenticate with Firebase using OAuth providers like Microsoft Azure Active Directory by integrating web-based generic OAuth Login into your app using the Firebase SDK to carry out the end to end sign-in flow.

## Before you begin

To sign in users using Microsoft accounts (Azure Active Directory and personal Microsoft accounts), you must first enable Microsoft as a sign-in provider for your Firebase project:

1. [Add Firebase to your Android project](https://firebase.google.com/docs/android/setup).

2. In the[Firebaseconsole](https://console.firebase.google.com/), open the**Auth**section.
3. On the**Sign in method** tab, enable the**Microsoft**provider.
4. Add the**Client ID** and**Client Secret** from that provider's developer console to the provider configuration:
   1. To register a Microsoft OAuth client, follow the instructions in[Quickstart: Register an app with the Azure Active Directory v2.0 endpoint](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-v2-register-an-app). Note that this endpoint supports sign-in using Microsoft personal accounts as well as Azure Active Directory accounts.[Learn more](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-overview)about Azure Active Directory v2.0.
   2. When registering apps with these providers, be sure to register the`*.firebaseapp.com`domain for your project as the redirect domain for your app.
5. Click**Save**.
6. If you haven't yet specified your app's SHA-1 fingerprint, do so from the[Settings page](https://console.firebase.google.com/project/_/settings/general/)of theFirebaseconsole. Refer to[Authenticating Your Client](https://developers.google.com/android/guides/client-auth)for details on how to get your app's SHA-1 fingerprint.

## Handle the sign-in flow with the Firebase SDK

If you are building an Android app, the easiest way to authenticate your users with Firebase using their Microsoft accounts is to handle the entire sign-in flow with the Firebase Android SDK.

To handle the sign-in flow with the Firebase Android SDK, follow these steps:

1. Construct an instance of an**OAuthProvider** using its**Builder** with the provider ID**microsoft.com**.

   ### Kotlin

   <br />

   ```kotlin
   val provider = OAuthProvider.newBuilder("microsoft.com")https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GenericIdpActivity.kt#L52-L52
   ```

   <br />

   ### Java

   <br />

   ```java
   OAuthProvider.Builder provider = OAuthProvider.newBuilder("microsoft.com");https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/GenericIdpActivity.java#L58-L58
   ```

   <br />

2. **Optional**: Specify additional custom OAuth parameters that you want to send with the OAuth request.

   ### Kotlin

   <br />

   ```kotlin
   // Target specific email with login hint.
   // Force re-consent.
   provider.addCustomParameter("prompt", "consent")

   // Target specific email with login hint.
   provider.addCustomParameter("login_hint", "user@firstadd.onmicrosoft.com")https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GenericIdpActivity.kt#L56-L61
   ```

   <br />

   ### Java

   <br />

   ```java
   // Target specific email with login hint.
   // Force re-consent.
   provider.addCustomParameter("prompt", "consent");

   // Target specific email with login hint.
   provider.addCustomParameter("login_hint", "user@firstadd.onmicrosoft.com");https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/GenericIdpActivity.java#L62-L67
   ```

   <br />

   For the parameters Microsoft supports, see the[Microsoft OAuth documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v1-protocols-oauth-code). Note that you can't pass Firebase-required parameters with`setCustomParameters()`. These parameters are**client_id** ,**response_type** ,**redirect_uri** ,**state** ,**scope** and**response_mode**.

   To allow only users from a particular Azure AD tenant to sign into the application, either the friendly domain name of the Azure AD tenant or the tenant's GUID identifier can be used. This can be done by specifying the "tenant" field in the custom parameters object.  

   ### Kotlin

   <br />

   ```kotlin
   // Optional "tenant" parameter in case you are using an Azure AD tenant.
   // eg. '8eaef023-2b34-4da1-9baa-8bc8c9d6a490' or 'contoso.onmicrosoft.com'
   // or "common" for tenant-independent tokens.
   // The default value is "common".
   provider.addCustomParameter("tenant", "TENANT_ID")https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GenericIdpActivity.kt#L65-L69
   ```

   <br />

   ### Java

   <br />

   ```java
   // Optional "tenant" parameter in case you are using an Azure AD tenant.
   // eg. '8eaef023-2b34-4da1-9baa-8bc8c9d6a490' or 'contoso.onmicrosoft.com'
   // or "common" for tenant-independent tokens.
   // The default value is "common".
   provider.addCustomParameter("tenant", "TENANT_ID");https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/GenericIdpActivity.java#L71-L75
   ```

   <br />

3. **Optional**: Specify additional OAuth 2.0 scopes beyond basic profile that you want to request from the authentication provider.

   ### Kotlin

   <br />

   ```kotlin
   // Request read access to a user's email addresses.
   // This must be preconfigured in the app's API permissions.
   provider.scopes = listOf("mail.read", "calendars.read")https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GenericIdpActivity.kt#L73-L75
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
                   add("mail.read");
                   add("calendars.read");
               }
           };
   provider.setScopes(scopes);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/GenericIdpActivity.java#L79-L88
   ```

   <br />

   To learn more, refer to the[Microsoft permissions and consent documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent).
4. Authenticate with Firebase using the OAuth provider object. Note that unlike other FirebaseAuth operations, this will take control of your UI by popping up a[Custom Chrome Tab](https://developer.chrome.com/multidevice/android/customtabs). As a result, do not reference your Activity in the`OnSuccessListener`and`OnFailureListener`that you attach as they will immediately detach when the operation starts the UI.

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
   }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GenericIdpActivity.kt#L118-L137
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
   }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/GenericIdpActivity.java#L151-L178
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
       }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GenericIdpActivity.kt#L143-L156
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
                   });https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/GenericIdpActivity.java#L184-L205
   ```

   <br />

   On successful completion, the OAuth access token associated with the provider can be retrieved from the`OAuthCredential`object returned.

   Using the OAuth access token, you can call the[Microsoft Graph API](https://docs.microsoft.com/en-us/graph/overview?toc=./toc.json&view=graph-rest-1.0).

   Unlike other providers supported by Firebase Auth, Microsoft does not provide a photo URL and instead, the binary data for a profile photo has to be requested via[Microsoft Graph API](https://docs.microsoft.com/en-us/graph/api/profilephoto-get?view=graph-rest-1.0).

   In addition to the OAuth access token, the user's OAuth[ID token](https://docs.microsoft.com/en-us/azure/active-directory/develop/id-tokens)can also be retrieved from the`OAuthCredential`object. The`sub`claim in the ID token is app-specific and will not match the federated user identifier used by Firebase Auth and accessible via`user.getProviderData().get(0).getUid()`. The`oid`claim field should be used instead. When using a Azure AD tenant to sign-in, the`oid`claim will be an exact match. However for the non-tenant case, the`oid`field is padded. For a federated ID`4b2eabcdefghijkl`, the`oid`will have have a form`00000000-0000-0000-4b2e-abcdefghijkl`.
5. While the above examples focus on sign-in flows, you also have the ability to link a Microsoft provider to an existing user using`startActivityForLinkWithProvider`. For example, you can link multiple providers to the same user allowing them to sign in with either.

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
       }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GenericIdpActivity.kt#L162-L177
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
                   });https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/GenericIdpActivity.java#L211-L235
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
       }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/GenericIdpActivity.kt#L183-L195
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
                   });https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/GenericIdpActivity.java#L241-L262
   ```

   <br />

## Advanced: Handle the sign-in flow manually

Unlike other OAuth providers supported by Firebase such as Google, Facebook, and Twitter, where sign-in can directly be achieved with OAuth access token based credentials, Firebase Auth does not support the same capability for providers such as Microsoft due to the inability of the Firebase Auth server to verify the audience of Microsoft OAuth access tokens. This is a critical security requirement and could expose applications and websites to replay attacks where a Microsoft OAuth access token obtained for one project (attacker) can be used to sign in to another project (victim). Instead, Firebase Auth offers the ability to handle the entire OAuth flow and the authorization code exchange using the OAuth client ID and secret configured in the Firebase Console. As the authorization code can only be used in conjunction with a specific client ID/secret, an authorization code obtained for one project cannot be used with another.

If these providers are required to be used in unsupported environments, a third party OAuth library and[Firebase custom authentication](https://firebase.google.com/docs/auth/admin/create-custom-tokens)would need to be used. The former is needed to authenticate with the provider and the latter to exchange the provider's credential for a custom token.

## Next steps

After a user signs in for the first time, a new user account is created and linked to the credentials---that is, the user name and password, phone number, or auth provider information---the user signed in with. This new account is stored as part of your Firebase project, and can be used to identify a user across every app in your project, regardless of how the user signs in.

- In your apps, you can get the user's basic profile information from the[`FirebaseUser`](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser)object. See[Manage Users](https://firebase.google.com/docs/auth/android/manage-users).

- In yourFirebase Realtime DatabaseandCloud Storage[Security Rules](https://firebase.google.com/docs/database/security/user-security), you can get the signed-in user's unique user ID from the`auth`variable, and use it to control what data a user can access.

You can allow users to sign in to your app using multiple authentication providers by[linking auth provider credentials to an existing user account.](https://firebase.google.com/docs/auth/android/account-linking)

To sign out a user, call[`signOut`](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signOut()):  

### Kotlin

```kotlin
Firebase.auth.signOut()https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/MainActivity.kt#L415-L415
```

### Java

```java
FirebaseAuth.getInstance().signOut();https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/MainActivity.java#L501-L501
```