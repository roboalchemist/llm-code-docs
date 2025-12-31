# Source: https://firebase.google.com/docs/auth/ios/email-link-auth.md.txt

# Source: https://firebase.google.com/docs/auth/web/email-link-auth.md.txt

# Source: https://firebase.google.com/docs/auth/flutter/email-link-auth.md.txt

# Source: https://firebase.google.com/docs/auth/android/email-link-auth.md.txt

# Source: https://firebase.google.com/docs/auth/web/email-link-auth.md.txt

# Source: https://firebase.google.com/docs/auth/flutter/email-link-auth.md.txt

# Source: https://firebase.google.com/docs/auth/android/email-link-auth.md.txt

| **Note**: The legacy implementation of email link authentication and actions in SDK versions lower than Android SDK v23.2.0 and iOS SDK 11.8.0 uses Firebase Dynamic Links, which will be shut down on August 25, 2025.
|
| This guide has been updated to refer to the new solution in later SDK versions.
|
| For specific information and migration guidance, visit the[Dynamic LinksDeprecation FAQ](https://firebase.google.com/support/dynamic-links-faq#impacts-on-email-link-authentication).

You can useFirebase Authenticationto sign in a user by sending them an email containing a link, which they can click to sign in. In the process, the user's email address is also verified.

There are numerous benefits to signing in by email:

- Low friction sign-up and sign-in.
- Lower risk of password reuse across applications, which can undermine security of even well-selected passwords.
- The ability to authenticate a user while also verifying that the user is the legitimate owner of an email address.
- A user only needs an accessible email account to sign in. No ownership of a phone number or social media account is required.
- A user can sign in securely without the need to provide (or remember) a password, which can be cumbersome on a mobile device.
- An existing user who previously signed in with an email identifier (password or federated) can be upgraded to sign in with just the email. For example, a user who has forgotten their password can still sign in without needing to reset their password.

## Before you begin

### Set up your Android project

1. If you haven't already,[add Firebase to your Android project](https://firebase.google.com/docs/android/setup).

2. In your**module (app-level) Gradle file** (usually`<project>/<app-module>/build.gradle.kts`or`<project>/<app-module>/build.gradle`), add the dependency for theFirebase Authenticationlibrary for Android. We recommend using the[Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)to control library versioning.

   Also, as part of setting upFirebase Authentication, you need to add the Google Play services SDK to your app.

   <br />

   ```carbon
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.7.0"))

       // Add the dependency for the Firebase Authentication library
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-auth")

       // Also add the dependency for the Google Play services library and specify its version
       implementation("com.google.android.gms:play-services-auth:21.4.0")
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

       // Also add the dependency for the Google Play services library and specify its version
       implementation("com.google.android.gms:play-services-auth:21.4.0")
   }
   ```

   <br />

## Enable Email Link sign-in for your Firebase project

To sign in users by email link, you must first enable the Email provider and Email link sign-in method for your Firebase project:

1. In the[Firebaseconsole](https://console.firebase.google.com/), open the**Auth**section.
2. On the**Sign in method** tab, enable the**Email/Password**provider. Note that email/password sign-in must be enabled to use email link sign-in.
3. In the same section, enable**Email link (passwordless sign-in)**sign-in method.
4. Click**Save**.

## Send an authentication link to the user's email address

To initiate the authentication flow, present the user with an interface that prompts the user to provide their email address and then call`sendSignInLinkToEmail`to request that Firebase send the authentication link to the user's email.

1. Construct the[ActionCodeSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings)object, which provides Firebase with instructions on how to construct the email link. Set the following fields:

   - `url`: The deep link to embed and any additional state to be passed along. The link's domain has to be whitelisted in the Firebase Console list of authorized domains, which can be found by going to the Sign-in method tab (Authentication -\> Sign-in method). The link will redirect the user to this URL if the app is not installed on their device and the app was not able to be installed.

   | **Important:** In projects created after April 28, 2025,Firebase Authenticationno longer includes`localhost`as an authorized domain by default. Google strongly discourages the use of`localhost`in production projects. If you choose to authorize`localhost`, you can manually add it in the**Settings** page, in**Authorized Domains** , by clicking**Add Domain**.
   - `androidPackageName`and`iOSBundleId`: HelpsFirebase Authenticationdetermine if it should create a web-only or mobile link which is opened on an Android or Apple device.
   - `handleCodeInApp`: Set to true. The sign-in operation has to always be completed in the app unlike other out of band email actions (password reset and email verifications). This is because, at the end of the flow, the user is expected to be signed in and their Auth state persisted within the app.
   - `linkDomain`: When customHostinglink domains are defined for a project, specify which one to use when the link is to be opened by a specified mobile app. Otherwise, the default domain is automatically selected (for example,<var translate="no">PROJECT_ID</var>`.firebaseapp.com`).
   - `dynamicLinkDomain`: Deprecated. Don't specify this parameter.

   ### Kotlin

   ```kotlin
   val actionCodeSettings = actionCodeSettings {
       // URL you want to redirect back to. The domain (www.example.com) for this
       // URL must be whitelisted in the Firebase Console.
       url = "https://www.example.com/finishSignUp?cartId=1234"
       // This must be true
       handleCodeInApp = true
       setIOSBundleId("com.example.ios")
       setAndroidPackageName(
           "com.example.android",
           true, // installIfNotAvailable
           "12", // minimumVersion
       )
   }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/MainActivity.kt#L277-L289
   ```

   ### Java

   ```java
   ActionCodeSettings actionCodeSettings =
           ActionCodeSettings.newBuilder()
                   // URL you want to redirect back to. The domain (www.example.com) for this
                   // URL must be whitelisted in the Firebase Console.
                   .setUrl("https://www.example.com/finishSignUp?cartId=1234")
                   // This must be true
                   .setHandleCodeInApp(true)
                   .setIOSBundleId("com.example.ios")
                   .setAndroidPackageName(
                           "com.example.android",
                           true, /* installIfNotAvailable */
                           "12"    /* minimumVersion */)
                   .build();https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/MainActivity.java#L336-L348
   ```

   To learn more on ActionCodeSettings, refer to the[Passing State in Email Actions](https://firebase.google.com/docs/auth/android/passing-state-in-email-actions#passing_statecontinue_url_in_email_actions)section.
2. Ask the user for their email.

3. Send the authentication link to the user's email, and save the user's email in case the user completes the email sign-in on the same device.

   ### Kotlin

   ```kotlin
   Firebase.auth.sendSignInLinkToEmail(email, actionCodeSettings)
       .addOnCompleteListener { task ->
           if (task.isSuccessful) {
               Log.d(TAG, "Email sent.")
           }
       }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/MainActivity.kt#L295-L300
   ```

   ### Java

   ```java
   FirebaseAuth auth = FirebaseAuth.getInstance();
   auth.sendSignInLinkToEmail(email, actionCodeSettings)
           .addOnCompleteListener(new OnCompleteListener<Void>() {
               @Override
               public void onComplete(@NonNull Task<Void> task) {
                   if (task.isSuccessful()) {
                       Log.d(TAG, "Email sent.");
                   }
               }
           });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/MainActivity.java#L354-L363
   ```

## Complete sign in with the email link

### Security concerns

To prevent a sign-in link from being used to sign in as an unintended user or on an unintended device,Firebase Authenticationrequires the user's email address to be provided when completing the sign-in flow. For sign-in to succeed, this email address must match the address to which the sign-in link was originally sent.

You can streamline this flow for users who open the sign-in link on the same device they request the link, by storing their email address locally - for instance using SharedPreferences - when you send the sign-in email. Then, use this address to complete the flow. Do not pass the user's email in the redirect URL parameters and re-use it as this may enable session injections.

After sign-in completion, any previous unverified mechanism of sign-in will be removed from the user and any existing sessions will be invalidated. For example, if someone previously created an unverified account with the same email and password, the user's password will be removed to prevent the impersonator who claimed ownership and created that unverified account from signing in again with the unverified email and password.

Also make sure you use an HTTPS URL in production to avoid your link being potentially intercepted by intermediary servers.

### Completing sign-in in an Android App

Firebase AuthenticationusesFirebase Hostingto send the email link to a mobile device. For sign-in completion via mobile application, the application has to be configured to detect the incoming application link, parse the underlying deep link and then complete the sign-in. To learn more, see[Android App Links documentation](https://developer.android.com/training/app-links).

#### ConfigureFirebase Hosting

Firebase Authenticationuses[Firebase Hosting](https://firebase.google.com/docs/hosting)domains when creating and sending a link that is meant to be opened in a mobile application. A defaultFirebase Hostingdomain has already been configured for you.

1. ConfigureFirebase Hostingdomains:

   In theFirebaseconsole, open the[Hosting](https://console.firebase.google.com/project/_/hosting/sites)section.
   - If you want to use the default domain for the email link that opens in mobile applications, go to your default site and take note of your defaultHostingdomain. A defaultHostingdomain typically looks like this:<var translate="no">PROJECT_ID</var>`.firebaseapp.com`.

     You'll need this value when you configure your app to intercept the incoming link.
   - If you want to use a custom domain for the email link, you can[register one withFirebase Hosting](https://firebase.google.com/docs/hosting/custom-domain)and use that for the link's domain.

2. Configuring Android applications:

   In order to handle these links from your Android application, your app's package name needs to be specified in theFirebaseconsole project settings. In addition, the SHA-1 and SHA-256 of the application certificate need to be provided.

   If you want these links to redirect to a specific activity, you will need to configure an intent filter in your`AndroidManifest.xml`file. The intent filter should catch email links of your domain. In`AndroidManifest.xml`:  

       <intent-filter android:autoVerify="true">
         <action android:name="android.intent.action.VIEW" />
         <category android:name="android.intent.category.BROWSABLE" />
         <category android:name="android.intent.category.DEFAULT" />
         <data
           android:scheme="https"
           android:host="<PROJECT_ID>.firebaseapp.com or your custom domain"
           android:pathPrefix="/__/auth/links" />
       </intent-filter>

   When users open a hosting link with the`/__/auth/links`path and the scheme and host you specify, your app will start the activity with this intent filter to[handle the link](https://developer.android.com/training/app-links).

#### Verify link and sign in

After you receive the link as described above, verify that it is meant for email link authentication and complete the sign in.  

### Kotlin

```kotlin
val auth = Firebase.auth
val intent = intent
val emailLink = intent.data.toString()

// Confirm the link is a sign-in with email link.
if (auth.isSignInWithEmailLink(emailLink)) {
    // Retrieve this from wherever you stored it
    val email = "someemail@domain.com"

    // The client SDK will parse the code from the link for you.
    auth.signInWithEmailLink(email, emailLink)
        .addOnCompleteListener { task ->
            if (task.isSuccessful) {
                Log.d(TAG, "Successfully signed in with email link!")
                val result = task.result
                // You can access the new user via result.getUser()
                // Additional user info profile *not* available via:
                // result.getAdditionalUserInfo().getProfile() == null
                // You can check if the user is new or existing:
                // result.getAdditionalUserInfo().isNewUser()
            } else {
                Log.e(TAG, "Error signing in with email link", task.exception)
            }
        }
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/MainActivity.kt#L306-L330
```

### Java

```java
FirebaseAuth auth = FirebaseAuth.getInstance();
Intent intent = getIntent();
String emailLink = intent.getData().toString();

// Confirm the link is a sign-in with email link.
if (auth.isSignInWithEmailLink(emailLink)) {
    // Retrieve this from wherever you stored it
    String email = "someemail@domain.com";

    // The client SDK will parse the code from the link for you.
    auth.signInWithEmailLink(email, emailLink)
            .addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                @Override
                public void onComplete(@NonNull Task<AuthResult> task) {
                    if (task.isSuccessful()) {
                        Log.d(TAG, "Successfully signed in with email link!");
                        AuthResult result = task.getResult();
                        // You can access the new user via result.getUser()
                        // Additional user info profile *not* available via:
                        // result.getAdditionalUserInfo().getProfile() == null
                        // You can check if the user is new or existing:
                        // result.getAdditionalUserInfo().isNewUser()
                    } else {
                        Log.e(TAG, "Error signing in with email link", task.getException());
                    }
                }
            });
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/MainActivity.java#L369-L396
```

To learn more on how to handle sign-in with email link in an Apple application, refer to the[Apple platforms guide](https://firebase.google.com/docs/auth/ios/email-link-auth).

To learn about how to handle sign-in with email link in a web application, refer to the[Web guide](https://firebase.google.com/docs/auth/web/email-link-auth).

### Linking/re-authentication with email link

You can also link this method of authentication to an existing user. For example a user previously authenticated with another provider, such as a phone number, can add this method of sign-in to their existing account.

The difference would be in the second half of the operation:  

### Kotlin

```kotlin
// Construct the email link credential from the current URL.
val credential = EmailAuthProvider.getCredentialWithLink(email, emailLink)

// Link the credential to the current user.
Firebase.auth.currentUser!!.linkWithCredential(credential)
    .addOnCompleteListener { task ->
        if (task.isSuccessful) {
            Log.d(TAG, "Successfully linked emailLink credential!")
            val result = task.result
            // You can access the new user via result.getUser()
            // Additional user info profile *not* available via:
            // result.getAdditionalUserInfo().getProfile() == null
            // You can check if the user is new or existing:
            // result.getAdditionalUserInfo().isNewUser()
        } else {
            Log.e(TAG, "Error linking emailLink credential", task.exception)
        }
    }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/MainActivity.kt#L336-L353
```

### Java

```java
// Construct the email link credential from the current URL.
AuthCredential credential =
        EmailAuthProvider.getCredentialWithLink(email, emailLink);

// Link the credential to the current user.
auth.getCurrentUser().linkWithCredential(credential)
        .addOnCompleteListener(new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                if (task.isSuccessful()) {
                    Log.d(TAG, "Successfully linked emailLink credential!");
                    AuthResult result = task.getResult();
                    // You can access the new user via result.getUser()
                    // Additional user info profile *not* available via:
                    // result.getAdditionalUserInfo().getProfile() == null
                    // You can check if the user is new or existing:
                    // result.getAdditionalUserInfo().isNewUser()
                } else {
                    Log.e(TAG, "Error linking emailLink credential", task.getException());
                }
            }
        });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/MainActivity.java#L404-L425
```

This can also be used to re-authenticate an email link user before running a sensitive operation.  

### Kotlin

```kotlin
// Construct the email link credential from the current URL.
val credential = EmailAuthProvider.getCredentialWithLink(email, emailLink)

// Re-authenticate the user with this credential.
Firebase.auth.currentUser!!.reauthenticateAndRetrieveData(credential)
    .addOnCompleteListener { task ->
        if (task.isSuccessful) {
            // User is now successfully reauthenticated
        } else {
            Log.e(TAG, "Error reauthenticating", task.exception)
        }
    }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/MainActivity.kt#L359-L370
```

### Java

```java
// Construct the email link credential from the current URL.
AuthCredential credential =
        EmailAuthProvider.getCredentialWithLink(email, emailLink);

// Re-authenticate the user with this credential.
auth.getCurrentUser().reauthenticateAndRetrieveData(credential)
        .addOnCompleteListener(new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                if (task.isSuccessful()) {
                    // User is now successfully reauthenticated
                } else {
                    Log.e(TAG, "Error reauthenticating", task.getException());
                }
            }
        });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/auth/app/src/main/java/com/google/firebase/quickstart/auth/MainActivity.java#L433-L448
```

However, as the flow could end up on a different device where the original user was not logged in, this flow might not be completed. In that case, an error can be shown to the user to force them to open the link on the same device. Some state can be passed in the link to provide information on the type of operation and the user uid.

## Deprecated:Firebase Dynamic Linksbased verification

Email link authentication previously relied onFirebase Dynamic Links, which will be[shut down on August 25, 2025](https://firebase.google.com/support/dynamic-links-faq).

We've published an alternative solution in theFirebase AuthenticationAndroid SDK v23.2.0+ andFirebase BoMv33.9.0+.

If your app uses the old style links, you should[migrate your app](https://firebase.google.com/docs/auth/android/email-link-migration)to the newFirebase Hostingbased system.

## Deprecated: Differentiating email-password from email link

If you created your project on or after September 15, 2023, email enumeration protection is enabled by default. This feature improves the security of your project's user accounts, but it disables the`fetchSignInMethodsForEmail()`method, which we formerly recommended to implement identifier-first flows.

Although you can disable email enumeration protection for your project, we recommend against doing so.

See the documentation on[email enumeration protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection)for more details.

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