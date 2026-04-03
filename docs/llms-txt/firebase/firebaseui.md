# Source: https://firebase.google.com/docs/auth/web/firebaseui.md.txt

# Source: https://firebase.google.com/docs/auth/ios/firebaseui.md.txt

# Source: https://firebase.google.com/docs/auth/android/firebaseui.md.txt

![](https://firebase.google.com/static/docs/auth/images/firebaseui-android.png)

[FirebaseUI](https://github.com/firebase/firebaseui-android)is a library built on top of the Firebase Authentication SDK that provides drop-in UI flows for use in your app. FirebaseUI provides the following benefits:

- **Multiple Providers**- sign-in flows for email/password, email link, phone authentication, Google Sign-In, Facebook Login, Twitter Login, and GitHub Login.
- **Account Management**- flows to handle account management tasks, such as account creation and password resets.
- **Account Linking**- flows to safely link user accounts across identity providers.
- **Anonymous User Upgrading**- flows to safely upgrade anonymous users.
- **Custom Themes**- customize the look of FirebaseUI to match your app. Also, because FirebaseUI is open source, you can fork the project and customize it exactly to your needs.
- **Credential Manager** - automatic integration with[Credential Manager](https://developer.android.com/identity/sign-in/credential-manager)for fast cross-device sign-in.

## Before you begin

1. If you haven't already,[add Firebase to your Android project](https://firebase.google.com/docs/android/setup).

2. Add the dependencies for FirebaseUI to your app-level`build.gradle(.kts)`file. If you want to support sign-in with Facebook or Twitter, also include the Facebook and Twitter SDKs:

           dependencies {
               // ...

               implementation("com.firebaseui:firebase-ui-auth:9.0.0")

               // Required only if Facebook login support is required
               // Find the latest Facebook SDK releases here: https://goo.gl/Ce5L94
               implementation("com.facebook.android:facebook-android-sdk:8.x")
           }

   The FirebaseUI Auth SDK has transitive dependencies on the Firebase SDK and the Google Play services SDK.
3. In the[Firebaseconsole](https://console.firebase.google.com/), open the**Authentication**section and enable the sign-in methods you want to support. Some sign-in methods require additional information, usually available in the service's developer console.

4. If you enabled Google Sign-in:

   1. When prompted in the console, download the updated Firebase config file (`google-services.json`), which now contains the OAuth client information required for Google sign-in.

   2. Move this updated config file into your Android Studio project,*replacing* the now-outdated corresponding config file. (See[Add Firebase to your Android project](https://firebase.google.com/docs/android/setup#add-config-file).)

   3. If you haven't yet specified your app's SHA fingerprint, do so from the[Settings page](https://console.firebase.google.com/project/_/settings/general/)of theFirebaseconsole. See[Authenticating Your Client](https://developers.google.com/android/guides/client-auth)for details on how to get your app's SHA fingerprint.

5. If you support sign-in with Facebook or Twitter, add string resources to`strings.xml`that specify the identifying information required by each provider:

   ```ecl

   <resources>
     <!-- Facebook application ID and custom URL scheme (app ID prefixed by 'fb'). -->
     <string name="facebook_application_id" translatable="false">YOUR_APP_ID</string>
     <string name="facebook_login_protocol_scheme" translatable="false">fb<var translate="no">YOUR_APP_ID</var></string>
   </resources>
   ```

## Sign in

Create an`ActivityResultLauncher`which registers a callback for the FirebaseUI Activity result contract:  

### Kotlin

```kotlin
// See: https://developer.android.com/training/basics/intents/result
private val signInLauncher = registerForActivityResult(
    FirebaseAuthUIActivityResultContract(),
) { res ->
    this.onSignInResult(res)
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/FirebaseUIActivity.kt#L17-L22
```

### Java

```java
// See: https://developer.android.com/training/basics/intents/result
private final ActivityResultLauncher<Intent> signInLauncher = registerForActivityResult(
        new FirebaseAuthUIActivityResultContract(),
        new ActivityResultCallback<FirebaseAuthUIAuthenticationResult>() {
            @Override
            public void onActivityResult(FirebaseAuthUIAuthenticationResult result) {
                onSignInResult(result);
            }
        }
);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/FirebaseUIActivity.java#L29-L38
```

To kick off the FirebaseUI sign in flow, create a sign in intent with your preferred sign-in methods:  

### Kotlin

```kotlin
// Choose authentication providers
val providers = arrayListOf(
    AuthUI.IdpConfig.EmailBuilder().build(),
    AuthUI.IdpConfig.PhoneBuilder().build(),
    AuthUI.IdpConfig.GoogleBuilder().build(),
    AuthUI.IdpConfig.FacebookBuilder().build(),
    AuthUI.IdpConfig.TwitterBuilder().build(),
)

// Create and launch sign-in intent
val signInIntent = AuthUI.getInstance()
    .createSignInIntentBuilder()
    .setAvailableProviders(providers)
    .build()
signInLauncher.launch(signInIntent)https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/FirebaseUIActivity.kt#L32-L46
```

### Java

```java
// Choose authentication providers
List<AuthUI.IdpConfig> providers = Arrays.asList(
        new AuthUI.IdpConfig.EmailBuilder().build(),
        new AuthUI.IdpConfig.PhoneBuilder().build(),
        new AuthUI.IdpConfig.GoogleBuilder().build(),
        new AuthUI.IdpConfig.FacebookBuilder().build(),
        new AuthUI.IdpConfig.TwitterBuilder().build());

// Create and launch sign-in intent
Intent signInIntent = AuthUI.getInstance()
        .createSignInIntentBuilder()
        .setAvailableProviders(providers)
        .build();
signInLauncher.launch(signInIntent);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/FirebaseUIActivity.java#L49-L62
```

When the sign-in flow is complete, you will receive the result in`onSignInResult`:  

### Kotlin

```kotlin
private fun onSignInResult(result: FirebaseAuthUIAuthenticationResult) {
    val response = result.idpResponse
    if (result.resultCode == RESULT_OK) {
        // Successfully signed in
        val user = FirebaseAuth.getInstance().currentUser
        // ...
    } else {
        // Sign in failed. If response is null the user canceled the
        // sign-in flow using the back button. Otherwise check
        // response.getError().getErrorCode() and handle the error.
        // ...
    }
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/FirebaseUIActivity.kt#L51-L63
```

### Java

```java
private void onSignInResult(FirebaseAuthUIAuthenticationResult result) {
    IdpResponse response = result.getIdpResponse();
    if (result.getResultCode() == RESULT_OK) {
        // Successfully signed in
        FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();
        // ...
    } else {
        // Sign in failed. If response is null the user canceled the
        // sign-in flow using the back button. Otherwise check
        // response.getError().getErrorCode() and handle the error.
        // ...
    }
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/FirebaseUIActivity.java#L67-L79
```

### Set up sign-in methods

#### Email link authentication

1. In the[Firebaseconsole](https://console.firebase.google.com/), open the**Authentication** section. On the**Sign in method** tab, enable the**Email/Password**provider. Note that email/password sign-in must be enabled to use email link sign-in.

2. In the same section, enable**Email link (passwordless sign-in)** sign-in method and click**Save**.

3. You will also have to enable Firebase Dynamic Links to use email-link sign in. In the[Firebaseconsole](https://console.firebase.google.com/), click on**Dynamic Links** under**Engage** in the navigation bar. Click on**Getting started**and add a domain. The domain you choose here will be reflected in the email links sent to your users.

4. You can enable email link sign in FirebaseUI by calling the`enableEmailLinkSignIn`on an`EmailBuilder`instance. You will also need to provide a valid`ActionCodeSettings`object with`setHandleCodeInApp`set to true. Additionally, you need to whitelist the URL you pass to`setUrl`, which can be done in the[Firebaseconsole](https://console.firebase.google.com/), under Authentication -\> Sign in Methods -\> Authorized domains.

   ### Kotlin

   ```kotlin
   val actionCodeSettings = ActionCodeSettings.newBuilder()
       .setAndroidPackageName( // yourPackageName=
           "...", // installIfNotAvailable=
           true, // minimumVersion=
           null,
       )
       .setHandleCodeInApp(true) // This must be set to true
       .setUrl("https://google.com") // This URL needs to be whitelisted
       .build()

   val providers = listOf(
       EmailBuilder()
           .enableEmailLinkSignIn()
           .setActionCodeSettings(actionCodeSettings)
           .build(),
   )
   val signInIntent = AuthUI.getInstance()
       .createSignInIntentBuilder()
       .setAvailableProviders(providers)
       .build()
   signInLauncher.launch(signInIntent)https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/FirebaseUIActivity.kt#L117-L137
   ```

   ### Java

   ```java
   ActionCodeSettings actionCodeSettings = ActionCodeSettings.newBuilder()
           .setAndroidPackageName(
                   /* yourPackageName= */ "...",
                   /* installIfNotAvailable= */ true,
                   /* minimumVersion= */ null)
           .setHandleCodeInApp(true) // This must be set to true
           .setUrl("https://google.com") // This URL needs to be whitelisted
           .build();

   List<AuthUI.IdpConfig> providers = Arrays.asList(
           new AuthUI.IdpConfig.EmailBuilder()
                   .enableEmailLinkSignIn()
                   .setActionCodeSettings(actionCodeSettings)
                   .build()
   );
   Intent signInIntent = AuthUI.getInstance()
           .createSignInIntentBuilder()
           .setAvailableProviders(providers)
           .build();
   signInLauncher.launch(signInIntent);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/FirebaseUIActivity.java#L138-L157
   ```
5. If you want to catch the link in a specific activity, please follow the steps outlined[here](https://firebase.google.com/docs/auth/android/email-link-auth). Otherwise, the link will redirect to your launcher activity.

6. Once you catch the deep link, you will need to call verify that we can handle it for you. If we can, you need to then pass it to us via`setEmailLink`.

   ### Kotlin

   ```kotlin
   if (AuthUI.canHandleIntent(intent)) {
       val extras = intent.extras ?: return
       val link = extras.getString("email_link_sign_in")
       if (link != null) {
           val signInIntent = AuthUI.getInstance()
               .createSignInIntentBuilder()
               .setEmailLink(link)
               .setAvailableProviders(providers)
               .build()
           signInLauncher.launch(signInIntent)
       }
   }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/FirebaseUIActivity.kt#L145-L156
   ```

   ### Java

   ```java
   if (AuthUI.canHandleIntent(getIntent())) {
       if (getIntent().getExtras() == null) {
           return;
       }
       String link = getIntent().getExtras().getString("email_link_sign_in");
       if (link != null) {
           Intent signInIntent = AuthUI.getInstance()
                   .createSignInIntentBuilder()
                   .setEmailLink(link)
                   .setAvailableProviders(providers)
                   .build();
           signInLauncher.launch(signInIntent);
       }
   }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/FirebaseUIActivity.java#L165-L178
   ```
7. **Optional** Cross device email link sign in is supported, which means that the link sent via your Android app can be used to log in on your web or Apple apps. By default, cross device support is enabled. You can disable it by calling`setForceSameDevice`on the`EmailBuilder`instance.

   See[FirebaseUI-Web](https://github.com/firebase/FirebaseUI-Android/tree/master/auth#configuring-email-link-sign-in)and[FirebaseUI-iOS](https://github.com/firebase/FirebaseUI-iOS/tree/master/Auth#configuring-email-link-sign-in)for more information.

## Sign Out

FirebaseUI provides convenience methods to sign out of Firebase Authentication as well as all social identity providers:  

### Kotlin

```kotlin
AuthUI.getInstance()
    .signOut(this)
    .addOnCompleteListener {
        // ...
    }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/FirebaseUIActivity.kt#L68-L72
```

### Java

```java
AuthUI.getInstance()
        .signOut(this)
        .addOnCompleteListener(new OnCompleteListener<Void>() {
            public void onComplete(@NonNull Task<Void> task) {
                // ...
            }
        });https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/FirebaseUIActivity.java#L84-L90
```

You can also completely delete the user's account:  

### Kotlin

```kotlin
AuthUI.getInstance()
    .delete(this)
    .addOnCompleteListener {
        // ...
    }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/FirebaseUIActivity.kt#L78-L82
```

### Java

```java
AuthUI.getInstance()
        .delete(this)
        .addOnCompleteListener(new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
                // ...
            }
        });https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/FirebaseUIActivity.java#L96-L103
```

## Customization

By default FirebaseUI uses AppCompat for theming, which means it will naturally adopt the color scheme of your app. If you require further customization you can pass a theme and a logo to the sign-in`Intent`builder:  

### Kotlin

```kotlin
val signInIntent = AuthUI.getInstance()
    .createSignInIntentBuilder()
    .setAvailableProviders(providers)
    .setLogo(R.drawable.my_great_logo) // Set logo drawable
    .setTheme(R.style.MySuperAppTheme) // Set theme
    .build()
signInLauncher.launch(signInIntent)https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/FirebaseUIActivity.kt#L90-L96
```

### Java

```java
Intent signInIntent = AuthUI.getInstance()
        .createSignInIntentBuilder()
        .setAvailableProviders(providers)
        .setLogo(R.drawable.my_great_logo)      // Set logo drawable
        .setTheme(R.style.MySuperAppTheme)      // Set theme
        .build();
signInLauncher.launch(signInIntent);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/FirebaseUIActivity.java#L111-L117
```

You can also set a custom privacy policy and terms of service:  

### Kotlin

```kotlin
val signInIntent = AuthUI.getInstance()
    .createSignInIntentBuilder()
    .setAvailableProviders(providers)
    .setTosAndPrivacyPolicyUrls(
        "https://example.com/terms.html",
        "https://example.com/privacy.html",
    )
    .build()
signInLauncher.launch(signInIntent)https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/FirebaseUIActivity.kt#L103-L111
```

### Java

```java
Intent signInIntent = AuthUI.getInstance()
        .createSignInIntentBuilder()
        .setAvailableProviders(providers)
        .setTosAndPrivacyPolicyUrls(
                "https://example.com/terms.html",
                "https://example.com/privacy.html")
        .build();
signInLauncher.launch(signInIntent);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/FirebaseUIActivity.java#L125-L132
```

## Next Steps

- For more information on using and customizing FirebaseUI, see the[README](https://github.com/firebase/FirebaseUI-Android/blob/master/auth/README.md)file on GitHub.
- If you find an issue in FirebaseUI and would like to report it, use the[GitHub issue tracker](https://github.com/firebase/FirebaseUI-Android/issues).