# Source: https://firebase.google.com/docs/auth/web/passing-state-in-email-actions.md.txt

# Source: https://firebase.google.com/docs/auth/ios/passing-state-in-email-actions.md.txt

# Source: https://firebase.google.com/docs/auth/flutter/passing-state-in-email-actions.md.txt

# Source: https://firebase.google.com/docs/auth/android/passing-state-in-email-actions.md.txt

# Source: https://firebase.google.com/docs/auth/ios/passing-state-in-email-actions.md.txt

# Source: https://firebase.google.com/docs/auth/flutter/passing-state-in-email-actions.md.txt

# Source: https://firebase.google.com/docs/auth/android/passing-state-in-email-actions.md.txt

| **Note**: The legacy implementation of email link authentication and actions in SDK versions lower than Android SDK v23.2.0 and iOS SDK 11.8.0 uses Firebase Dynamic Links, which will be shut down on August 25, 2025.
|
| This guide has been updated to refer to the new solution in later SDK versions.
|
| For specific information and migration guidance, visit the[Dynamic LinksDeprecation FAQ](https://firebase.google.com/support/dynamic-links-faq#impacts-on-email-link-authentication).

You can pass state via a continue URL when sending email actions for password resets or verifying a user's email. This provides the user the ability to go back to the app after the action is completed. In addition, you can specify whether to handle the email action link directly from a mobile application when it is installed instead of a web page.

This can be extremely useful in the following common scenarios:

- A user, not currently logged in, may be trying to access content that requires the user to be signed in. However, the user might have forgotten their password and therefore trigger the reset password flow. At the end of the flow, the user expects to go back to the section of the app they were trying to access.

- An application may only offer access to verified accounts. For example, a newsletter may require the user to verify their email before subscribing. The user would go through the email verification flow and expect to go back to the app to complete their subscription.

- In other cases, the user may have started the flow from their mobile device and expect after verification to return back to their mobile app instead of the browser.

Having the ability to pass state via a continue URL is a powerful feature that Firebase Auth provides and which can significantly enhance the user experience.

## Passing state of a continue URL in email actions

In order to securely pass a continue URL, the domain for the URL will need to be whitelisted in the[Firebaseconsole](https://console.firebase.google.com/). This is done in the**Authentication** section by adding this domain to the list of**Authorized domains** under the**Sign-in method**tab if it is not already there.

An[ActionCodeSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings)instance needs to be provided when sending a password reset email or a verification email. It can be created with the associated[ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder)class which contains the following methods:

|                                                  Method                                                  |                                                                                                                                                                                   Description                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `setUrl(String url)`                                                                                     | Sets the link (state/continue URL) which has different meanings in different contexts: - When the link is handled in the web action widgets, this is the deep link in the`continueUrl`query parameter. - When the link is handled in the app directly, this is the`continueUrl`query parameter in the deep link of theHostinglink.                                              |
| `setIOSBundleId(String iOSBundleId)`                                                                     | Sets the iOS bundle ID to helpFirebase Authenticationdetermine if it should create a web-only or mobile link which is opened on an Apple device                                                                                                                                                                                                                                 |
| `setAndroidPackageName(String androidPackageName, boolean installIfNotAvailable, String minimumVersion)` | Sets the Android package name to helpFirebase Authenticationdetermine if it should create a web-only or mobile link which is opened on an Android device                                                                                                                                                                                                                        |
| `setHandleCodeInApp(boolean status)`                                                                     | Whether the email action link will be opened in a mobile app or a web link first. The default is false. When set to true, the action code link will be be sent as a Universal Link or Android App Link and will be opened by the app if installed. In the false case, the code will be sent to the web widget first and then on continue will redirect to the app if installed. |
| `setLinkDomain(String customDomain)`                                                                     | When customHostinglink domains are defined for a project, specify which one to use when the link is to be opened by a specified mobile app. Otherwise, the default domain is automatically selected (for example,<var translate="no">PROJECT_ID</var>`.firebaseapp.com`).                                                                                                       |
| `setDynamicLinkDomain(String dynamicLinkDomain)`                                                         | Deprecated. Don't specify this parameter.                                                                                                                                                                                                                                                                                                                                       |

The following example illustrates how to send an email verification link that will open in a mobile app first. The deep link will contain the continue URL payload`http://www.example.com/verify?uid=1234`.  

### Kotlin

```kotlin
val auth = Firebase.auth
val user = auth.currentUser!!

val url = "http://www.example.com/verify?uid=" + user.uid
val actionCodeSettings = ActionCodeSettings.newBuilder()
    .setUrl(url)
    .setIOSBundleId("com.example.ios")
    // The default for this is populated with the current android package name.
    .setAndroidPackageName("com.example.android", false, null)
    .build()

user.sendEmailVerification(actionCodeSettings)
    .addOnCompleteListener { task ->
        if (task.isSuccessful) {
            Log.d(TAG, "Email sent.")
        }
    }
https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/kotlin/MainActivity.kt#L153-L170
```

### Java

```java
FirebaseAuth auth = FirebaseAuth.getInstance();
FirebaseUser user = auth.getCurrentUser();

String url = "http://www.example.com/verify?uid=" + user.getUid();
ActionCodeSettings actionCodeSettings = ActionCodeSettings.newBuilder()
        .setUrl(url)
        .setIOSBundleId("com.example.ios")
        // The default for this is populated with the current android package name.
        .setAndroidPackageName("com.example.android", false, null)
        .build();

user.sendEmailVerification(actionCodeSettings)
        .addOnCompleteListener(new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
                if (task.isSuccessful()) {
                    Log.d(TAG, "Email sent.");
                }
            }
        });
https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/auth/app/src/main/java/com/google/firebase/quickstart/auth/MainActivity.java#L188-L208
```

## Configuring Firebase Hosting links

Firebase Authenticationuses[Firebase Hosting](https://firebase.google.com/docs/hosting)when sending a link that is meant to be opened in a mobile application. In order to use this feature, Hosting links need to be configured in theFirebaseconsole.

1. Configuring Android applications:

   1. If you plan on handling these links from your Android application, your app's package name needs to be specified in theFirebaseconsole project settings. In addition, the SHA-1 and SHA-256 of the application certificate need to be provided.
   2. You will also need to configure the intent filter for the deep link in your`AndroidManifest.xml`file.
   3. For more on this, refer to[Receiving Android Hosting links instructions](https://firebase.google.com/docs/auth/android/email-link-migration).
2. Configuring iOS applications:

   1. If you plan on handling these links from your iOS application, you will need to configure theHostinglink domain as an Associated Domain in your application capabilities.
   2. For more on this, refer to[Receiving iOS Hosting links instructions](https://firebase.google.com/docs/auth/ios/email-link-migration).

## Handling email actions in a web application

You can specify whether you want to handle the action code link from a web application first and then redirect to another web page or mobile application after successful completion, provided the mobile application is available. This is done by calling`setHandleCodeInApp(false)`in the[ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder)object. While an iOS bundle ID or Android package name are not required, providing them will allow the user to redirect back to the specified app on email action code completion.

The web URL used here, is the one configured in the email action templates section. A default one is provisioned for all projects. Refer to[customizing email handlers](https://firebase.google.com/docs/auth/custom-email-handler)to learn more on how to customize the email action handler.

In this case, the link within the`continueUrl`query parameter will be anHostinglink whose payload is the`URL`specified in the`ActionCodeSettings`object.

When handling email actions such as email verification, the action code from the`oobCode`query parameter needs to be parsed from the deep link and then applied via`applyActionCode`for the change to take effect, i.e. email to be verified.

## Handling email actions in a mobile application

You can specify whether you want to handle the action code link within your mobile application first, provided it is installed. If the link is clicked from a device that does not support the mobile application, it is opened from a web page instead. This is done by calling`setHandleCodeInApp(true)`in the[ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder)object. The mobile application's Android package name or iOS bundle ID will also need to be specified.

The fallback web URL used here, when no mobile app is available, is the one configured in the email action templates section. A default one is provisioned for all projects. Refer to[customizing email handlers](https://firebase.google.com/docs/auth/custom-email-handler)to learn more on how to customize the email action handler.

In this case, the mobile app link sent to the user will be aHostinglink whose payload is the action code URL, configured in the Console, with the query parameters`oobCode`,`mode`,`apiKey`and`continueUrl`. The latter will be the original`URL`specified in the`ActionCodeSettings`object. The action code can be applied directly from a mobile application similar to how it is handled from the web flow described in the[customizing email handlers](https://firebase.google.com/docs/auth/custom-email-handler)section.

When handling email actions such as email verification, the action code from the`oobCode`query parameter needs to be parsed from the deep link and then applied via`applyActionCode`for the change to take effect, i.e. email to be verified.