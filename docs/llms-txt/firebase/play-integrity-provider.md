# Source: https://firebase.google.com/docs/app-check/android/play-integrity-provider.md.txt

This page shows you how to enableApp Checkin an Android app, using the built-in Play Integrity provider. When you enableApp Check, you help ensure that only your app can access your project's backend resources. See an[Overview](https://firebase.google.com/docs/app-check)of this feature.

The Play Integrity provider supports Android apps that are published on Google Play, outside Google Play, or both. If your use case requires Play Integrity features not implemented byApp Check, or if you want to useApp Checkwith your own custom provider, see[Implement a customApp Checkprovider](https://firebase.google.com/docs/app-check/android/custom-provider).

## 1. Set up your Firebase project

1. [Add Firebase to your Android project](https://firebase.google.com/docs/android/setup)if you haven't already done so.

2. Enable the Play Integrity API:

   1. In the[Google Play Console](https://play.google.com/console/developers/), select your app, or add it if you haven't already done so.

   2. In the**Release** section, click**App integrity**.

   3. Go to the**Play Integrity API** section of the page, click**Link Cloud project**, then select your Firebase project from the list of Google Cloud projects. The project you select here must be the same Firebase project as the one in which you register your app (see the next step).

      <br />

      | You must be an**Owner**of the project you want to link. Note that being a member of a group that has been assigned the Owner role is insufficient.

      <br />

3. Register your apps to useApp Checkwith the Play Integrity provider in the[**App Check**](https://console.firebase.google.com/project/_/appcheck)section of theFirebaseconsole. You will need to[provide the SHA-256 fingerprint](https://developers.google.com/android/guides/client-auth)of your app's signing certificate.

   You usually need to register all of your project's apps, because once you enable enforcement for a Firebase product, only registered apps will be able to access the product's backend resources.
4. <br />

   <br />

   **Optional** : In the app registration settings, set a custom time-to-live (TTL) forApp Checktokens issued by the provider. You can set the TTL to any value between 30 minutes and 7 days. When changing this value, be aware of the following tradeoffs:
   - Security: Shorter TTLs provide stronger security, because it reduces the window in which a leaked or intercepted token can be abused by an attacker.
   - Performance: Shorter TTLs mean your app will perform attestation more frequently. Because the app attestation process adds latency to network requests every time it's performed, a short TTL can impact the performance of your app.
   - Quota and cost: Shorter TTLs and frequent re-attestation deplete your quota faster, and for paid services, potentially cost more. See[Quotas \& limits](https://firebase.google.com/docs/app-check#quotas_limits).

   The default TTL of**1 hour** is reasonable for most apps. Note that theApp Checklibrary refreshes tokens at approximately half the TTL duration.

   <br />

   <br />

### Configure advanced settings (optional)

App Checkoffers a number of settings to support advanced use cases, including distributing your app outside Google Play. You can configure these settings in the[**App Check**](https://console.firebase.google.com/project/_/appcheck)section of theFirebaseconsole for each of your Android apps. We recommend that you configure these settings according to the following table when you first[register your app](https://firebase.google.com/docs/app-check/android/play-integrity-provider#project-setup).

|    Your app's distribution channel     | PLAY_RECOGNIZED |   LICENSED   |   Minimum acceptable device integrity level   |
|----------------------------------------|-----------------|--------------|-----------------------------------------------|
| Exclusively on Google Play             | Required        | Required     | Don't explicitly check device integrity level |
| Exclusively outside Google Play        | Not required    | Not required | Device integrity                              |
| On Google Play and outside Google Play | Required        | Not required | Don't explicitly check device integrity level |

#### Details

Each advanced setting corresponds to a Play Integrity verdict label. Consult the[Play Integrity documentation](https://developer.android.com/google/play/integrity/verdicts)for additional details.

- By default,App Checkrequires the[`PLAY_RECOGNIZED`](https://developer.android.com/google/play/integrity/verdicts#application-integrity-field)app recognition label. Apps not published on Google Play are not eligible to receive this label.
- By default,App Checkdoesn't require the[`LICENSED`](https://developer.android.com/google/play/integrity/verdicts#account-details-field)app licensing label. Only users who have installed or updated your app directly from Google Play are eligible to receive this label.
- By default,App Checkdoes not explicitly check the device integrity verdict.App Checksupports explicitly checking for the following three device integrity levels, listed in order of increasing device integrity.

  | **Note:** Play Integrity may*implicitly* perform additional device integrity checks during the evaluation of other integrity verdicts; you cannot directly control these implicit checks, and they are**not**affected by this setting.
  - **Basic integrity** . CausesApp Checkto require the[`MEETS_BASIC_INTEGRITY`](https://developer.android.com/google/play/integrity/verdicts#optional-device-labels)device recognition label. In order for your app to be eligible to receive this*optional* label, you must first[opt in from the Google Play Console](https://developer.android.com/google/play/integrity/setup#optional).

    | **Warning:** Because your Android 13+ users who don't install or update your app from Google Play are ineligible to receive this label, they will be denied access if they are unable to meet the requirements for the stronger`MEETS_DEVICE_INTEGRITY`label. Consider using this setting only as a tool to relax device integrity requirements for users who install or update your app from Google Play. For more details, see the[Play Integrity documentation](https://developer.android.com/google/play/integrity/improvements).
  - **Device integrity** . CausesApp Checkto require the[`MEETS_DEVICE_INTEGRITY`](https://developer.android.com/google/play/integrity/verdicts#device-integrity-field)device recognition label. All apps are automatically eligible to receive this label.

  - **Strong integrity** . CausesApp Checkto require the[`MEETS_STRONG_INTEGRITY`](https://developer.android.com/google/play/integrity/verdicts#optional-device-labels)device recognition label. In order for your app to be eligible to receive this*optional* label, you must first[opt in from the Google Play Console](https://developer.android.com/google/play/integrity/setup#optional).

    | **Warning:** Because your Android 13+ users who don't install or update your app from Google Play are ineligible to receive this label, you should only consider using this setting if your app is distributed exclusively using Google Play. For more details, see the[Play Integrity documentation](https://developer.android.com/google/play/integrity/improvements).

## 2. Add theApp Checklibrary to your app

In your**module (app-level) Gradle file** (usually`<project>/<app-module>/build.gradle.kts`or`<project>/<app-module>/build.gradle`), add the dependency for theApp Checklibrary for Android. We recommend using the[Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)to control library versioning.

<br />

```carbon
dependencies {
    // Import the BoM for the Firebase platform
    implementation(platform("com.google.firebase:firebase-bom:34.7.0"))

    // Add the dependencies for the App Check libraries
    // When using the BoM, you don't specify versions in Firebase library dependencies
    implementation("com.google.firebase:firebase-appcheck-playintegrity")
}
```

By using the[Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom), your app will always use compatible versions of Firebase Android libraries.
*(Alternative)* Add Firebase library dependencies*without* using theBoM

If you choose not to use theFirebase BoM, you must specify each Firebase library version in its dependency line.

**Note that if you use*multiple* Firebase libraries in your app, we strongly recommend using theBoMto manage library versions, which ensures that all versions are compatible.**  

```groovy
dependencies {
    // Add the dependencies for the App Check libraries
    // When NOT using the BoM, you must specify versions in Firebase library dependencies
    implementation("com.google.firebase:firebase-appcheck-playintegrity:19.0.1")
}
```

<br />

## 3. InitializeApp Check

Add the following initialization code to your app so that it runs before you use any other Firebase SDKs:  

### Kotlin

```kotlin
Firebase.initialize(context = this)
Firebase.appCheck.installAppCheckProviderFactory(
    PlayIntegrityAppCheckProviderFactory.getInstance(),
)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/appcheck/app/src/main/java/com/google/firebase/example/appcheck/kotlin/MainActivity.kt#L20-L23
```

### Java

```java
FirebaseApp.initializeApp(/*context=*/ this);
FirebaseAppCheck firebaseAppCheck = FirebaseAppCheck.getInstance();
firebaseAppCheck.installAppCheckProviderFactory(
        PlayIntegrityAppCheckProviderFactory.getInstance());https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/appcheck/app/src/main/java/com/google/firebase/example/appcheck/MainActivity.java#L22-L25
```

## Next steps

Once theApp Checklibrary is installed in your app, start distributing the updated app to your users.

The updated client app will begin sendingApp Checktokens along with every request it makes to Firebase, but Firebase products will not require the tokens to be valid until you enable enforcement in theApp Checksection of the Firebase console.

### Monitor metrics and enable enforcement

Before you enable enforcement, however, you should make sure that doing so won't disrupt your existing legitimate users. On the other hand, if you're seeing suspicious use of your app resources, you might want to enable enforcement sooner.

To help make this decision, you can look atApp Checkmetrics for the services you use:

- [MonitorApp Checkrequest metrics](https://firebase.google.com/docs/app-check/monitor-metrics)forFirebase AI Logic,Data Connect,Realtime Database,Cloud Firestore,Cloud Storage,Authentication, Google Identity for iOS, Maps JavaScript API, and Places API (New).
- [MonitorApp Checkrequest metrics forCloud Functions](https://firebase.google.com/docs/app-check/monitor-functions-metrics).

### EnableApp Checkenforcement

When you understand howApp Checkwill affect your users and you're ready to proceed, you can enableApp Checkenforcement:

- [EnableApp Checkenforcement](https://firebase.google.com/docs/app-check/enable-enforcement)forFirebase AI Logic,Data Connect,Realtime Database,Cloud Firestore,Cloud Storage,Authentication, Google Identity for iOS, Maps JavaScript API, and Places API (New).
- [EnableApp Checkenforcement forCloud Functions](https://firebase.google.com/docs/app-check/cloud-functions).

### UseApp Checkin debug environments

If, after you have registered your app forApp Check, you want to run your app in an environment thatApp Checkwould normally not classify as valid, such as an emulator during development, or from a continuous integration (CI) environment, you can create a debug build of your app that uses theApp Checkdebug provider instead of a real attestation provider.

See[UseApp Checkwith the debug provider on Android](https://firebase.google.com/docs/app-check/android/debug-provider).