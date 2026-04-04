# Source: https://firebase.google.com/docs/dynamic-links/android/receive.md.txt

> [!NOTE]
> **Note:** Firebase Dynamic Links is *deprecated* and should not be used in new projects. The service will be shutting down soon. Follow the [migration guide](https://firebase.google.com/support/dynamic-links-faq#how_should_i_migrate_from_the_service) and see the [Dynamic Links Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq) for more information.

To receive the Firebase Dynamic Links that [you created](https://firebase.google.com/docs/dynamic-links/create-links), you must include the Dynamic Links SDK in your app and call the
`FirebaseDynamicLinks.getDynamicLink()` method when your app loads to
get the data passed in the Dynamic Link.

## Set up Firebase and the Dynamic Links SDK

1. If you haven't already,
   [add Firebase to your Android project](https://firebase.google.com/docs/android/setup).

   When you register your app, specify your SHA-1 signing key. If you use
   App Links, also specify your SHA-256 key.
2.


   In your **module (app-level) Gradle file**
   (usually `<project>/<app-module>/build.gradle.kts` or
   `<project>/<app-module>/build.gradle`),
   add the dependency for the Dynamic Links library for Android. We recommend using the
   [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)
   to control library versioning.


   For an optimal experience with Dynamic Links, we recommend
   [enabling Google Analytics](https://support.google.com/firebase/answer/9289399#linkga)
   in your Firebase project and adding the Firebase SDK for Google Analytics to your app.

   ```
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

       // Add the dependencies for the Dynamic Links and Analytics libraries
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation 'com.google.firebase:firebase-dynamic-links'
       implementation 'com.google.firebase:firebase-analytics'
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
       // Add the dependencies for the Dynamic Links and Analytics libraries
       // When NOT using the BoM, you must specify versions in Firebase library dependencies
       implementation 'com.google.firebase:firebase-dynamic-links:22.1.0'
       implementation 'com.google.firebase:firebase-analytics:23.0.0'
   }
   ```
3. In the [Firebase console](https://console.firebase.google.com/), open the **Dynamic Links** section. Accept the terms of service if you are prompted to do so.

## Add an intent filter for deep links

As with [plain deep links](https://developer.android.com/training/app-indexing/deep-linking.html), you must add a new intent filter to the activity that handles
deep links for your app. The intent filter should catch deep links of your domain, since the
Dynamic Link will redirect to your domain if your app is installed. This is required for your app to
receive the Dynamic Link data after it is installed/updated from the Play Store and one taps on
Continue button. In `AndroidManifest.xml`:

```
<intent-filter>
    <action android:name="android.intent.action.VIEW"/>
    <category android:name="android.intent.category.DEFAULT"/>
    <category android:name="android.intent.category.BROWSABLE"/>
    <data
        android:host="example.com"
        android:scheme="https"/>
</intent-filter>https://github.com/firebase/quickstart-android/blob/c3626e43ae9dc75e671c5c56eb062c26eee8db52/dynamiclinks/app/src/main/AndroidManifest.xml#L23-L30
```

When users open a Dynamic Link with a deep link to the scheme and host you specify, your app will
start the activity with this intent filter to handle the link.

## Handle deep links

To receive the deep link, call the `getDynamicLink()` method:

### Kotlin

```kotlin
Firebase.dynamicLinks
    .getDynamicLink(intent)
    .addOnSuccessListener(this) { pendingDynamicLinkData: PendingDynamicLinkData? ->
        // Get deep link from result (may be null if no link is found)
        var deepLink: Uri? = null
        if (pendingDynamicLinkData != null) {
            deepLink = pendingDynamicLinkData.link
        }

        // Handle the deep link. For example, open the linked
        // content, or apply promotional credit to the user's
        // account.
        // ...
    }
    .addOnFailureListener(this) { e -> Log.w(TAG, "getDynamicLink:onFailure", e) }
```

### Java

```java
FirebaseDynamicLinks.getInstance()
        .getDynamicLink(getIntent())
        .addOnSuccessListener(this, new OnSuccessListener<PendingDynamicLinkData>() {
            @Override
            public void onSuccess(PendingDynamicLinkData pendingDynamicLinkData) {
                // Get deep link from result (may be null if no link is found)
                Uri deepLink = null;
                if (pendingDynamicLinkData != null) {
                    deepLink = pendingDynamicLinkData.getLink();
                }


                // Handle the deep link. For example, open the linked
                // content, or apply promotional credit to the user's
                // account.
                // ...

                // ...
            }
        })
        .addOnFailureListener(this, new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception e) {
                Log.w(TAG, "getDynamicLink:onFailure", e);
            }
        });
```

You must call `getDynamicLink()` in every activity that might be
launched by the link, even though the link might be available from the intent
using `getIntent().getData()`. Calling `getDynamicLink()`
retrieves the link and clears that data so it is only processed once by your
app.

You normally call `getDynamicLink()` in the main activity as well
as any activities launched by intent filters that match the link.

## Record analytics

The following events can be automatically tracked in Google Analytics and shown in the
Firebase console.

- `dynamic_link_app_open`
- `dynamic_link_first_open`
- `dynamic_link_app_update`

In order to register these events, you need to configure Google Analytics before you
retrieve the deep link. Check the following conditions are met:

- Call `FirebaseDynamicLinks.getDynamicLink()` in your app entry points:
  - Launcher activities. e.g.: `action="android.intent.action.MAIN"`, `category="android.intent.category.LAUNCHER"`.
  - Activity entry points. e.g.: `onStart()`, `onCreate()`.
  - Deep link activities.
- Set up and use Google Analytics:
  - Include the Google Analytics dependency. This is usually automatically added by the `google-services` Gradle plugin.
  - [Include the
    `google-services.json` config file](https://firebase.google.com/docs/android/setup) in your app.
  - Call `FirebaseAnalytics.getInstance()` before calling `FirebaseDynamicLinks.getDynamicLink()`.

## Handling Dynamic Links using App Links

On Android 6.0 (API level 23) and higher, you can set up your app to handle Dynamic Links
directly when your app is already installed by using
[Android App Links](https://developer.android.com/training/app-links/index.html).

Ensure that you have added the SHA256 certificate fingerprint for your app into your project in
the [Firebase console](https://console.firebase.google.com/). Dynamic Links will handle setting up the App Links website association for
your Dynamic Links domain.

Add an auto-verified intent filter to the Activity that will handle the Dynamic Link, setting the
host to your project's Dynamic Links domain as
[found in the Firebase console](https://firebase.google.com/docs/dynamic-links/android/receive#find_domain). In
the `AndroidManifest.xml`:

```
<intent-filter android:autoVerify="true">
    <action android:name="android.intent.action.VIEW"/>
    <category android:name="android.intent.category.DEFAULT"/>
    <category android:name="android.intent.category.BROWSABLE"/>
    <data android:host="example.com/link" android:scheme="http"/>
    <data android:host="example.com/link" android:scheme="https"/>
</intent-filter>
```

Note that the `android:host` must be set to your Dynamic Links domain, and not the domain
of your deep link.

All `autoVerify` intent filters in your manifest must be registered in order for App
Links to engage. Firebase handles this automatically for your Dynamic Links domains, but you can check
this by opening the `assetlinks.json` file hosted on your Dynamic Links domain:

```
https://YOUR_DOMAIN/.well-known/assetlinks.json
```
All of your Firebase apps' package names should be included.

<br />

Dynamic Links will now be sent directly to your app. You will be able to get the deep link and other
Dynamic Link data by calling `getDynamicLink()` in the Activity you added the App Links
intent filter to (as described in
[Handle deep links](https://firebase.google.com/docs/dynamic-links/android/receive#handle_deep_links)).


**Note:** Since invoking through App Links takes the user directly to the app, a
Dynamic Link cannot honor the required minimum version. So once the app is opened, you
need to compare the Dynamic Link's minimum version (
[getminimumappversion](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#public-int-getminimumappversion)) against [PackageInfo.versionCode](https://developer.android.com/reference/android/content/pm/PackageInfo.html#versionCode) and redirect the user to upgrade the app if required using [getUpdateAppIntent](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData#public-intent-getupdateappintent-context-context).