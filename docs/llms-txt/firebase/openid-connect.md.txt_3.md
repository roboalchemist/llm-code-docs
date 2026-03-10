# Source: https://firebase.google.com/docs/auth/android/openid-connect.md.txt

If you've upgraded to Firebase Authentication with Identity Platform, you can authenticate your users with
Firebase using the OpenID Connect (OIDC) compliant provider of your choice. This
makes it possible to use identity providers not natively supported by Firebase.

## Before you begin

To sign in users using an OIDC provider, you must first collect some information
from the provider:

- **Client ID** : A string unique to the provider that identifies your app. Your
  provider might assign you a different client ID for each platform you support.
  This is one of the values of the `aud` claim in ID tokens issued by your
  provider.

- **Client secret** : A secret string that the provider uses to confirm ownership
  of a client ID. For every client ID, you will need a matching client secret.
  (This value is required only if you're using the *auth code flow*, which is
  strongly recommended.)

- **Issuer** : A string that identifies your provider. This value must be a URL
  that, when appended with `/.well-known/openid-configuration`, is the location
  of the provider's OIDC discovery document. For example, if the issuer is
  `https://auth.example.com`, the discovery document must be available at
  `https://auth.example.com/.well-known/openid-configuration`.

After you have the above information, enable OpenID Connect as a sign-in
provider for your Firebase project:

1. [Add Firebase to your Android project](https://firebase.google.com/docs/android/setup).

2. If you haven't upgraded to Firebase Authentication with Identity Platform, do so. OpenID Connect authentication
   is only available in upgraded projects.

3. On the [**Sign-in providers**](https://console.firebase.google.com/project/_/authentication/providers)
   page of the Firebase console, click **Add new provider** , and then click
   **OpenID Connect**.

4. Select whether you will be using the *authorization code flow* or the
   *implicit grant flow*.

   **You should use always the code flow if your provider supports it**. The
   implicit flow is less secure and using it is strongly discouraged.
5. Give a name to this provider. Note the provider ID that's generated:
   something like `oidc.example-provider`. You'll need this ID when you add
   sign-in code to your app.

6. Specify your client ID and client secret, and your provider's issuer string.
   These values must exactly match the values your provider assigned to you.

7. Save your changes.

## Handle the sign-in flow with the Firebase SDK

If you are building an Android app, the easiest way to authenticate your users
with Firebase using your OIDC provider is to handle the entire sign-in flow with
the Firebase Android SDK.

To handle the sign-in flow with the Firebase Android SDK, follow these steps:

1. Construct an instance of an **OAuthProvider** using its **Builder** with the
   provider's ID

   ### Kotlin


   ```kotlin
   val providerBuilder = OAuthProvider.newBuilder("oidc.example-provider")
   ```

   <br />

   ### Java


   ```java
   OAuthProvider.Builder providerBuilder = OAuthProvider.newBuilder("oidc.example-provider");
   ```

   <br />

2. **Optional**: Specify additional custom OAuth parameters that you want to
   send with the OAuth request.

   ### Kotlin


   ```kotlin
   // Target specific email with login hint.
   providerBuilder.addCustomParameter("login_hint", "user@example.com")
   ```

   <br />

   ### Java


   ```java
   // Target specific email with login hint.
   providerBuilder.addCustomParameter("login_hint", "user@example.com");
   ```

   <br />

   Check with your OIDC provider for the parameters they support.
   Note that you can't pass Firebase-required parameters with
   `setCustomParameters()`. These parameters are **client_id** ,
   **response_type** , **redirect_uri** , **state** , **scope** and
   **response_mode**.
3. **Optional**: Specify additional OAuth 2.0 scopes beyond basic profile that
   you want to request from the authentication provider.

   ### Kotlin


   ```kotlin
   // Request read access to a user's email addresses.
   // This must be preconfigured in the app's API permissions.
   providerBuilder.scopes = listOf("mail.read", "calendars.read")
   ```

   <br />

   ### Java


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
   providerBuilder.setScopes(scopes);
   ```

   <br />

   Check with your OIDC provider for the scopes they use.
4. Authenticate with Firebase using the OAuth provider object. Note that unlike
   other FirebaseAuth
   operations, this will take control of your UI by popping up a
   [Custom Chrome Tab](https://developer.chrome.com/multidevice/android/customtabs).
   As a result, do not reference your Activity in the `OnSuccessListener`
   and `OnFailureListener` that you attach as they will immediately detach when
   the operation starts the UI.

   You should first check if you've already received a response. Signing in with
   this method puts your Activity in the background, which means that it can be
   reclaimed by the system during the sign in flow. In order to make sure that
   you don't make the user try again if this happens, you should check if a
   result is already present.

   To check if there is a pending result, call `getPendingAuthResult`:

   ### Kotlin


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
   }
   ```

   <br />

   ### Java


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
   }
   ```

   <br />

   To start the sign in flow, call `startActivityForSignInWithProvider`:

   ### Kotlin


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
       }
   ```

   <br />

   ### Java


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
                   });
   ```

   <br />

5. While the above examples focus on sign-in flows, you also have the
   ability to link an OIDC provider to an existing user using
   `startActivityForLinkWithProvider`. For example, you can link multiple
   providers to the same user allowing them to sign in with either.

   ### Kotlin


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
       }
   ```

   <br />

   ### Java


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
                   });
   ```

   <br />

6. The same pattern can be used with
   `startActivityForReauthenticateWithProvider` which can be used to retrieve
   fresh credentials for sensitive operations that require recent login.

   ### Kotlin


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
       }
   ```

   <br />

   ### Java


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
                   });
   ```

   <br />

## Handle the sign-in flow manually

If you've already implemented the OpenID Connect sign-in flow in your app, you
can use the ID token directly to authenticate with Firebase:

### Kotlin


```kotlin
val providerId = "oidc.example-provider" // As registered in Firebase console.
val credential = oAuthCredential(providerId) {
    setIdToken(idToken) // ID token from OpenID Connect flow.
}
Firebase.auth
    .signInWithCredential(credential)
    .addOnSuccessListener { authResult ->
        // User is signed in.

        // IdP data available in:
        //    authResult.additionalUserInfo.profile
    }
    .addOnFailureListener { e ->
        // Handle failure.
    }
```

<br />

### Java


```java
AuthCredential credential = OAuthProvider
        .newCredentialBuilder("oidc.example-provider")  // As registered in Firebase console.
        .setIdToken(idToken)  // ID token from OpenID Connect flow.
        .build();
FirebaseAuth.getInstance()
        .signInWithCredential(credential)
        .addOnSuccessListener(new OnSuccessListener<AuthResult>() {
            @Override
            public void onSuccess(AuthResult authResult) {
                // User is signed in.

                // IdP data available in:
                //    authResult.getAdditionalUserInfo().getProfile()
            }
        })
        .addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception e) {
                // Handle failure.
            }
        });
```

<br />

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