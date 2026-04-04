# Source: https://firebase.google.com/docs/auth/android/apple.md.txt

You can let your users authenticate with Firebase using their Apple ID by
using the Firebase SDK to carry out the end-to-end OAuth 2.0 sign-in flow.
**Important**: To sign in with an Apple account, users must:

- Have an Apple ID with two-factor authentication (2FA) enabled.
- Be signed in to iCloud on an Apple device.

See [How
to use Sign in with Apple](https://support.apple.com/en-us/HT210318). You will also need to meet these requirements
to test your integration with Sign In with Apple.

## Before you begin

[Video](https://www.youtube.com/watch?v=HyiNbqLOCQ8)

To sign in users using Apple, first configure Sign In with Apple
on Apple's developer site, then enable Apple as a sign-in provider for your
Firebase project.

### Join the Apple Developer Program

Sign In with Apple can only be configured by members of the [Apple Developer
Program](https://developer.apple.com/programs/).

### Configure Sign In with Apple

On the [Apple
Developer](https://developer.apple.com/account/resources) site, do the following:

1. Associate your website with your app as described in the first section
   of [Configure Sign In with Apple for the web](https://developer.apple.com/help/account/configure-app-capabilities/configure-sign-in-with-apple-for-the-web/). When prompted, register the
   following URL as a Return URL:

   ```
   https://YOUR_FIREBASE_PROJECT_ID.firebaseapp.com/__/auth/handler
   ```

   You can get your Firebase project ID on the
   [Firebase console
   settings page](https://console.firebase.google.com/project/_/settings/general/).

   When you're done, take note of your new Service ID, which you'll need in
   the next section.
2. [Create a
   Sign In with Apple private key](https://developer.apple.com/help/account/configure-app-capabilities/create-a-sign-in-with-apple-private-key/). You'll need your new private key and key ID in the next section.
3. If you use any of Firebase Authentication's features that send emails to users,
   including email link sign-in, email address verification, account change
   revocation, and
   others, [configure the Apple private email relay service](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service/) and register
   `noreply@YOUR_FIREBASE_PROJECT_ID.firebaseapp.com`
   (or your customized email template domain) so Apple can relay emails sent
   by Firebase Authentication to anonymized Apple email addresses.

### Enable Apple as a sign-in provider

1. [Add Firebase to your Android project](https://firebase.google.com/docs/android/setup). Be sure to register your app's SHA-1 signature when you set up your app in the Firebase console.
2. In the [Firebase console](https://console.firebase.google.com/), open the **Auth** section. On the **Sign in method** tab, enable the **Apple** provider. Specify the Service ID you created in the previous section. Also, in the **OAuth code flow configuration section**, specify your Apple Team ID and the private key and key ID you created in the previous section.

## Comply with Apple anonymized data requirements

Sign In with Apple gives users the option of anonymizing their data,
including their email address, when signing in. Users who choose this option
have email addresses with the domain `privaterelay.appleid.com`. When
you use Sign In with Apple in your app, you must comply with any applicable
developer policies or terms from Apple regarding these anonymized Apple
IDs.

This includes obtaining any required user consent before you
associate any directly identifying personal information with an anonymized Apple
ID. When using Firebase Authentication, this may include the following
actions:

- Link an email address to an anonymized Apple ID or vice versa.
- Link a phone number to an anonymized Apple ID or vice versa
- Link a non-anonymous social credential (Facebook, Google, etc) to an anonymized Apple ID or vice versa.

The above list is not exhaustive. Refer to the Apple Developer Program
License Agreement in the Membership section of your developer account to make
sure your app meets Apple's requirements.

## Handle the sign-in flow with the Firebase SDK

On Android, the easiest way to authenticate your users with Firebase using their
Apple accounts is to handle the entire sign-in flow with the Firebase Android
SDK.

To handle the sign-in flow with the Firebase Android SDK, follow these steps:

1. Construct an instance of an `OAuthProvider` using its Builder with the
   provider ID `apple.com`:

   ### Kotlin

       val provider = OAuthProvider.newBuilder("apple.com")

   ### Java

       OAuthProvider.Builder provider = OAuthProvider.newBuilder("apple.com");

2. **Optional:** Specify additional OAuth 2.0 scopes beyond the default that
   you want to request from the authentication provider.

   ### Kotlin

       provider.setScopes(arrayOf("email", "name"))

   ### Java

       List<String> scopes =
           new ArrayList<String>() {
             {
               add("email");
               add("name");
             }
           };
       provider.setScopes(scopes);

   By default, when **One account per email address** is enabled, Firebase
   requests email and name scopes. If you change this setting to **Multiple
   accounts per email address**, Firebase doesn't request any scopes from Apple
   unless you specify them.
3. **Optional:** If you want to display Apple's sign-in screen in a language
   other than English, set the `locale` parameter. See the
   [Sign In with Apple docs](https://developer.apple.com/documentation/signinwithapplejs/incorporating_sign_in_with_apple_into_other_platforms#3332112)
   for the supported locales.

   ### Kotlin

       // Localize the Apple authentication screen in French.
       provider.addCustomParameter("locale", "fr")

   ### Java

       // Localize the Apple authentication screen in French.
       provider.addCustomParameter("locale", "fr");

4. Authenticate with Firebase using the OAuth provider object. Note that unlike
   other `FirebaseAuth` operations, this will take control of your UI by
   opening a Custom Chrome Tab. Consequently, do not reference your Activity in
   the `OnSuccessListener` and `OnFailureListener` that you attach as they will
   immediately detach when the operation starts the UI.

   You should first check if you've already received a response. Signing in
   with this method puts your Activity in the background, which means that it
   can be reclaimed by the system during the sign in flow. In order to make
   sure that you don't make the user try again if this happens, you should
   check if a result is already present.

   To check if there is a pending result, call `getPendingAuthResult()`:

   ### Kotlin

       val pending = auth.pendingAuthResult
       if (pending != null) {
           pending.addOnSuccessListener { authResult ->
               Log.d(TAG, "checkPending:onSuccess:$authResult")
               // Get the user profile with authResult.getUser() and
               // authResult.getAdditionalUserInfo(), and the ID
               // token from Apple with authResult.getCredential().
           }.addOnFailureListener { e ->
               Log.w(TAG, "checkPending:onFailure", e)
           }
       } else {
           Log.d(TAG, "pending: null")
       }

   ### Java

       mAuth = FirebaseAuth.getInstance();
       Task<AuthResult> pending = mAuth.getPendingAuthResult();
       if (pending != null) {
           pending.addOnSuccessListener(new OnSuccessListener<AuthResult>() {
               @Override
               public void onSuccess(AuthResult authResult) {
                   Log.d(TAG, "checkPending:onSuccess:" + authResult);
                   // Get the user profile with authResult.getUser() and
                   // authResult.getAdditionalUserInfo(), and the ID
                   // token from Apple with authResult.getCredential().
               }
           }).addOnFailureListener(new OnFailureListener() {
               @Override
               public void onFailure(@NonNull Exception e) {
                   Log.w(TAG, "checkPending:onFailure", e);
               }
           });
       } else {
           Log.d(TAG, "pending: null");
       }

   If there's no pending result, start the sign in flow, by calling
   `startActivityForSignInWithProvider()`:

   ### Kotlin

       auth.startActivityForSignInWithProvider(this, provider.build())
               .addOnSuccessListener { authResult ->
                   // Sign-in successful!
                   Log.d(TAG, "activitySignIn:onSuccess:${authResult.user}")
                   val user = authResult.user
                   // ...
               }
               .addOnFailureListener { e ->
                   Log.w(TAG, "activitySignIn:onFailure", e)
               }

   ### Java

       mAuth.startActivityForSignInWithProvider(this, provider.build())
               .addOnSuccessListener(
                       new OnSuccessListener<AuthResult>() {
                           @Override
                           public void onSuccess(AuthResult authResult) {
                               // Sign-in successful!
                               Log.d(TAG, "activitySignIn:onSuccess:" + authResult.getUser());
                               FirebaseUser user = authResult.getUser();
                               // ...
                           }
                       })
               .addOnFailureListener(
                       new OnFailureListener() {
                           @Override
                           public void onFailure(@NonNull Exception e) {
                               Log.w(TAG, "activitySignIn:onFailure", e);
                           }
                       });

   Unlike other providers supported by Firebase Auth, Apple does not provide a
   photo URL.

   Also, when the user chooses not to share their email with the app, Apple
   provisions a unique email address for that user (of the form
   `xyz@privaterelay.appleid.com`), which it shares with your app. If you
   configured the private email relay service, Apple forwards emails sent to
   the anonymized address to the user's real email address.

   Apple only shares user information such as the display name with apps the
   first time a user signs in. Usually, Firebase stores the display name the
   first time a user signs in with Apple, which you can get with
   `getCurrentUser().getDisplayName()`.
   However, if you previously used Apple to sign a user in to the app without
   using Firebase, Apple will not provide Firebase with the user's display
   name.

### Reauthentication and account linking

The same pattern can be used with `startActivityForReauthenticateWithProvider()`
which you can use to retrieve a fresh credential for sensitive operations that
require recent sign-in:

### Kotlin

    // The user is already signed-in.
    val firebaseUser = auth.getCurrentUser()

    firebaseUser
        .startActivityForReauthenticateWithProvider(/* activity= */ this, provider.build())
        .addOnSuccessListener( authResult -> {
            // User is re-authenticated with fresh tokens and
            // should be able to perform sensitive operations
            // like account deletion and email or password
            // update.
        })
        .addOnFailureListener( e -> {
            // Handle failure.
        })

### Java

    // The user is already signed-in.
    FirebaseUser firebaseUser = mAuth.getCurrentUser();

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

And, you can use `linkWithCredential()` to link different identity providers to
existing accounts.

Note that Apple requires you to get explicit consent from users before you link
their Apple accounts to other data.

For example, to link a Facebook account to the current Firebase account, use the
access token you got from signing the user in to Facebook:

### Kotlin

    // Initialize a Facebook credential with a Facebook access token.
    val credential = FacebookAuthProvider.getCredential(token.getToken())

    // Assuming the current user is an Apple user linking a Facebook provider.
    mAuth.getCurrentUser().linkWithCredential(credential)
        .addOnCompleteListener(this, task -> {
            if (task.isSuccessful()) {
              // Facebook credential is linked to the current Apple user.
              // The user can now sign in to the same account
              // with either Apple or Facebook.
            }
          });

### Java

    // Initialize a Facebook credential with a Facebook access token.
    AuthCredential credential = FacebookAuthProvider.getCredential(token.getToken());

    // Assuming the current user is an Apple user linking a Facebook provider.
    mAuth.getCurrentUser().linkWithCredential(credential)
        .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
          @Override
          public void onComplete(@NonNull Task<AuthResult> task) {
            if (task.isSuccessful()) {
              // Facebook credential is linked to the current Apple user.
              // The user can now sign in to the same account
              // with either Apple or Facebook.
            }
          }
        });

## Advanced: Handle the sign-in flow manually

You can also authenticate with Firebase using an Apple Account by handling the
sign-in flow by either using the Apple Sign-In JS SDK, manually building the
OAuth flow or by using an OAuth library such as
[AppAuth](https://github.com/openid/AppAuth-Android).

1. For every sign-in request, generate a random string---a
   "nonce"---which you will use to make sure the ID token you get was
   granted specifically in response to your app's authentication request. This
   step is important to prevent replay attacks.

   You can generate a cryptographically secure nonce on Android with
   `SecureRandom`, as in the following example:

   ### Kotlin

       private fun generateNonce(length: Int): String {
           val generator = SecureRandom()

           val charsetDecoder = StandardCharsets.US_ASCII.newDecoder()
           charsetDecoder.onUnmappableCharacter(CodingErrorAction.IGNORE)
           charsetDecoder.onMalformedInput(CodingErrorAction.IGNORE)

           val bytes = ByteArray(length)
           val inBuffer = ByteBuffer.wrap(bytes)
           val outBuffer = CharBuffer.allocate(length)
           while (outBuffer.hasRemaining()) {
               generator.nextBytes(bytes)
               inBuffer.rewind()
               charsetDecoder.reset()
               charsetDecoder.decode(inBuffer, outBuffer, false)
           }
           outBuffer.flip()
           return outBuffer.toString()
       }

   ### Java

       private String generateNonce(int length) {
           SecureRandom generator = new SecureRandom();

           CharsetDecoder charsetDecoder = StandardCharsets.US_ASCII.newDecoder();
           charsetDecoder.onUnmappableCharacter(CodingErrorAction.IGNORE);
           charsetDecoder.onMalformedInput(CodingErrorAction.IGNORE);

           byte[] bytes = new byte[length];
           ByteBuffer inBuffer = ByteBuffer.wrap(bytes);
           CharBuffer outBuffer = CharBuffer.allocate(length);
           while (outBuffer.hasRemaining()) {
               generator.nextBytes(bytes);
               inBuffer.rewind();
               charsetDecoder.reset();
               charsetDecoder.decode(inBuffer, outBuffer, false);
           }
           outBuffer.flip();
           return outBuffer.toString();
       }

   Then, get the SHA246 hash of the nonce as a hex string:

   ### Kotlin

       private fun sha256(s: String): String {
           val md = MessageDigest.getInstance("SHA-256")
           val digest = md.digest(s.toByteArray())
           val hash = StringBuilder()
           for (c in digest) {
               hash.append(String.format("%02x", c))
           }
           return hash.toString()
       }

   ### Java

       private String sha256(String s) throws NoSuchAlgorithmException {
           MessageDigest md = MessageDigest.getInstance("SHA-256");
           byte[] digest = md.digest(s.getBytes());
           StringBuilder hash = new StringBuilder();
           for (byte c: digest) {
               hash.append(String.format("%02x", c));
           }
           return hash.toString();
       }

   You will send the SHA256 hash of the nonce with your sign-in request, which
   Apple will pass unchanged in the response. Firebase validates the response
   by hashing the original nonce and comparing it to the value passed by Apple.
2. Initiate Apple's sign-in flow using your OAuth library or other method. Be
   sure to include the hashed nonce as a parameter in your request.

3. After you receive Apple's response, get the ID token from the response and
   use it and the unhashed nonce to create an `AuthCredential`:

   ### Kotlin

       val credential =  OAuthProvider.newCredentialBuilder("apple.com")
           .setIdTokenWithRawNonce(appleIdToken, rawUnhashedNonce)
           .build()

   ### Java

       AuthCredential credential =  OAuthProvider.newCredentialBuilder("apple.com")
           .setIdTokenWithRawNonce(appleIdToken, rawUnhashedNonce)
           .build();

4. Authenticate with Firebase using the Firebase credential:

   ### Kotlin

       auth.signInWithCredential(credential)
             .addOnCompleteListener(this) { task ->
                 if (task.isSuccessful) {
                   // User successfully signed in with Apple ID token.
                   // ...
                 }
             }

   ### Java

       mAuth.signInWithCredential(credential)
           .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
             @Override
             public void onComplete(@NonNull Task<AuthResult> task) {
               if (task.isSuccessful()) {
                 // User successfully signed in with Apple ID token.
                 // ...
               }
             }
           });

If the call to `signInWithCredential` succeeds, you can use the `getCurrentUser`
method to get the user's account data.

## Token Revocation

Apple requires that apps that support account creation must let users initiate
deletion of their account within the app, as described in the [App Store Review
Guidelines](https://developer.apple.com/app-store/review/guidelines/#5.1.1v)

In addition, apps that support Sign in with Apple should use the Sign in with Apple
REST API to revoke user tokens.

To meet this requirement, implement the following steps:

1. Use `startActivityForSignInWithProvider()` method to sign-in using Apple and obtain `AuthResult`.

2. Obtain the access token for Apple provider.

   ### Kotlin

       val oauthCredential: OAuthCredential =  authResult.credential
       val accessToken = oauthCredential.accessToken

   ### Java

       OAuthCredential oauthCredential = (OAuthCredential) authResult.getCredential();
       String accessToken = oauthCredential.getAccessToken();

3. Revoke the token using `revokeAccessToken` API.

   ### Kotlin

       mAuth.revokeAccessToken(accessToken)
         .addOnCompleteListener(this) { task ->
           if (task.isSuccessful) {
             // Access token successfully revoked
             // for the user ...
           }
       }

   ### Java

       mAuth.revokeAccessToken(accessToken)
           .addOnCompleteListener(this, new OnCompleteListener<Void>() {
               @Override
               public void onComplete(@NonNull Task<Void> task) {
                 if (task.isSuccessful()) {
                   // Access token successfully revoked
                   // for the user ...
                 }
               }
         });

<!-- -->

1. Finally, [delete the user account](https://firebase.google.com/docs/auth/android/manage-users#delete_a_user) (and all associated data)

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