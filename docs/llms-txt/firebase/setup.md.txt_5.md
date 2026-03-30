# Source: https://firebase.google.com/docs/android/setup.md.txt

[Video](https://www.youtube.com/watch?v=jbHfJpoOzkI)

## Prerequisites

- Install or update [Android Studio](https://developer.android.com/sdk)
  to its latest version.

- Make sure that your project meets these requirements (note that some products
  might have stricter requirements):

  - Targets API level 23 (Marshmallow) or higher
  - Uses Android 6.0 or higher
  - Uses [Jetpack (AndroidX)](https://developer.android.com/jetpack/androidx/migrate), which includes meeting these version requirements:
    - `com.android.tools.build:gradle` v7.3.0 or later
    - `compileSdkVersion` 28 or later
- Set up a physical device or use an
  [emulator](https://developer.android.com/studio/run/managing-avds) to
  run your app.  

  Note that [Firebase SDKs with a dependency on Google Play
  services](https://firebase.google.com/docs/android/android-play-services) require the device or
  emulator to have Google Play services installed.

- [Sign into Firebase](https://console.firebase.google.com/) using your Google
  account.

If you don't already have an Android project and just want to try out a Firebase
product, you can download one of our [quickstart samples](https://firebase.google.com/docs/samples).

<br />

**You can connect your Android app to Firebase using one of the following
options:**

- [**Option 1**](https://firebase.google.com/docs/android/setup#console): *(recommended)* Use the Firebase console setup workflow.
- [**Option 2**](https://firebase.google.com/docs/android/setup#assistant): Use the Android Studio Firebase Assistant (may require additional configuration).

<br />

*** ** * ** ***

## **Option 1** : Add Firebase using the Firebase console

Adding Firebase to your app involves tasks both in the [Firebase console](https://console.firebase.google.com/) and
in your open Android project (for example, you download Firebase config files
from the console, then move them into your Android project).

### **Step 1**: Create a Firebase project

Before you can add Firebase to your Android app, you need to create a Firebase
project to connect to your Android app. Visit
[Understand Firebase Projects](https://firebase.google.com/docs/projects/learn-more) to learn more about
Firebase projects.
**View instructions to create a Firebase project**

### New to Firebase or Cloud


Follow these steps if you're new to Firebase or Google Cloud.  

You can also follow these steps if you want to create a wholly new
Firebase project (and its underlying Google Cloud project).

1. Sign into the [Firebase console](https://console.firebase.google.com/).
2. Click the button to create a new Firebase project.
3. In the text field, enter a **project name**.

   If you're part of a Google Cloud org, you can optionally select which
   folder you create your project in.

   > [!CAUTION]
   > Your project name is used as a display name in Firebase interfaces, and Firebase auto-creates a unique project ID based on this project name. Note that you can optionally click the **Edit** icon now to set your preferred project ID, but you cannot change this ID after project creation. Learn about [how Firebase uses the
   > project ID](https://firebase.google.com/docs/projects/learn-more#project-id).

4. If prompted, review and accept the [Firebase terms](https://firebase.google.com/terms), then click **Continue**.
5. *(Optional)* Enable AI assistance in the Firebase console (called "Gemini in Firebase"), which can help you get started and streamline your development process.
6. *(Optional)* Set up Google Analytics for your project,
   which enables an optimal experience using these Firebase products:
   [Firebase A/B Testing](https://firebase.google.com/docs/ab-testing),
   [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging),
   [Crashlytics](https://firebase.google.com/docs/crashlytics),
   [In-App Messaging](https://firebase.google.com/docs/in-app-messaging), and
   [Remote Config](https://firebase.google.com/docs/remote-config)
   (including
   [Personalization](https://firebase.google.com/docs/remote-config/personalization)).

   Either select an existing
   [Google Analytics account](https://support.google.com/analytics/answer/1009618)
   or create a new account. If you create a new account, select your
   [Analytics reporting location](https://firebase.google.com/docs/projects/locations),
   then accept the data sharing settings and Google Analytics terms
   for your project.

   > [!NOTE]
   > You can always set up Google Analytics later in the [*Integrations* tab](https://console.firebase.google.com/project/_/settings/integrations) of your *Project settings*.

7. Click **Create project**.

Firebase creates your project, provisions some initial resources, and
enables important APIs. When the process completes, you'll be taken to the
overview page for your Firebase project in the Firebase console.

### Existing Cloud project


Follow these steps if you want to start using Firebase with an existing
Google Cloud project. Learn more about and troubleshoot
["adding
Firebase" to an existing Google Cloud project](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project).

1. Sign into the [Firebase console](https://console.firebase.google.com/) with the account that gives you access to the existing Google Cloud project.
2. Click the button to create a new Firebase project.
3. At the bottom of the page, click **Add Firebase to Google Cloud project**.
4. In the text field, start entering the **project name** of the existing project, and then select the project from the displayed list.
5. Click **Open project**.
6. If prompted, review and accept the [Firebase terms](https://firebase.google.com/terms), then click **Continue**.
7. *(Optional)* Enable AI assistance in the Firebase console (called "Gemini in Firebase"), which can help you get started and streamline your development process.
8. *(Optional)* Set up Google Analytics for your project,
   which enables an optimal experience using these Firebase products:
   [Firebase A/B Testing](https://firebase.google.com/docs/ab-testing),
   [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging),
   [Crashlytics](https://firebase.google.com/docs/crashlytics),
   [In-App Messaging](https://firebase.google.com/docs/in-app-messaging), and
   [Remote Config](https://firebase.google.com/docs/remote-config)
   (including
   [Personalization](https://firebase.google.com/docs/remote-config/personalization)).

   Either select an existing
   [Google Analytics account](https://support.google.com/analytics/answer/1009618)
   or create a new account. If you create a new account, select your
   [Analytics reporting location](https://firebase.google.com/docs/projects/locations),
   then accept the data sharing settings and Google Analytics terms
   for your project.

   > [!NOTE]
   > You can always set up Google Analytics later in the [*Integrations* tab](https://console.firebase.google.com/project/_/settings/integrations) of your *Project settings*.

9. Click **Add Firebase**.

Firebase
[adds
Firebase to your existing project](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#faq_what-happens-when-add-firebase).
When the process completes, you'll be taken to the overview page for your
Firebase project in the Firebase console.

### **Step 2**: Register your app with Firebase

To use Firebase in your Android app, you need to register your app with your
Firebase project. Registering your app is often called "adding" your app to your
project.

> [!NOTE]
> **Note:** Check out our [best practices](https://firebase.google.com/docs/projects/dev-workflows/general-best-practices) for adding apps to a Firebase project, including how to handle multiple variants.

1. Go to the [Firebase console](https://console.firebase.google.com/).

2. In the center of the project overview page, click the **Android** icon
   ()
   or **Add app** to launch the setup workflow.

3. Enter your app's package name in the **Android package name** field.

   <br />

   What's a package name, and where do you find it?

   <br />

   > - A [package
   >   name](https://developer.android.com/studio/build/application-id)
   >   uniquely identifies your app on the device and in the Google Play Store.
   >
   > - A *package name* is often referred to as an *application ID*.
   >
   > - Find your app's package name in your module (app-level) Gradle file,
   >   usually `app/build.gradle` (example package name:
   >   `com.yourcompany.yourproject`).
   >
   > - Be aware that the package name value is case-sensitive, and it cannot be
   >   changed for this Firebase Android app after it's registered with your
   >   Firebase project.

   <br />

   <br />

   > [!CAUTION]
   > Make sure to enter the package name that your app is actually using. The package name value is case-sensitive, and it cannot be changed for this Firebase Android app after it's registered with your Firebase project.

4. *(Optional)* Enter an **App nickname** , which is an internal, convenience
   identifier that is only visible to you in the Firebase console.

5. Click **Register app**.

### **Step 3**: Add a Firebase configuration file

1. Download and then add your app's Firebase config file
   (`google-services.json`) to your codebase:

   1. Click **Download google-services.json** to obtain your app's Firebase
      config file.

   2. Move your config file into the **module (app-level)** root directory of
      your app.

   <br />

   What do you need to know about this config file?

   <br />

   > - The Firebase config file contains unique, but non-secret identifiers for
   >   your project and app. To learn more about this config file, visit
   >   [Understand Firebase
   >   Projects](https://firebase.google.com/docs/projects/learn-more#config-files-objects).
   >
   > - You can download your [Firebase config
   >   file](https://support.google.com/firebase/answer/7015592)
   >   again at any time.
   >
   > - Make sure the config file name is not appended with additional characters,
   >   like `(2)`.

   <br />

   <br />

2. To make the values in your `google-services.json` config file accessible
   to Firebase SDKs, you need the
   [Google services Gradle plugin](https://developers.google.com/android/guides/google-services-plugin)
   (`google-services`).

   1. In your **root-level (project-level)** Gradle file
      (`<project>/build.gradle.kts` or `<project>/build.gradle`), add the
      Google services plugin as a dependency:

      ### Kotlin

      > [!NOTE]
      > Are you still using the `buildscript` syntax? Learn how to [add Firebase plugins](https://firebase.google.com/docs/android/troubleshooting-faq#add-plugins-using-buildscript-syntax) using that syntax.

      ```kotlin
      plugins {
        id("com.android.application") version "7.3.0" apply false
        // ...

        // Add the dependency for the Google services Gradle plugin
        id("com.google.gms.google-services") version "4.4.4" apply false
      }
      ```

      ### Groovy

      > [!NOTE]
      > Are you still using the `buildscript` syntax? Learn how to [add Firebase plugins](https://firebase.google.com/docs/android/troubleshooting-faq#add-plugins-using-buildscript-syntax) using that syntax.

      ```groovy
      plugins {
        id 'com.android.application' version '7.3.0' apply false
        // ...

        // Add the dependency for the Google services Gradle plugin
        id 'com.google.gms.google-services' version '4.4.4' apply false
      }
      ```
   2. In your **module (app-level)** Gradle file
      (usually `<project>/<app-module>/build.gradle.kts` or
      `<project>/<app-module>/build.gradle`),
      add the Google services plugin:

      ### Kotlin

      ```kotlin
      plugins {
        id("com.android.application")

        // Add the Google services Gradle plugin
        id("com.google.gms.google-services")
        // ...
      }
      ```

      ### Groovy

      ```groovy
      plugins {
        id 'com.android.application'

        // Add the Google services Gradle plugin
        id 'com.google.gms.google-services'
        // ...
      }
      ```

### **Step 4**: Add Firebase SDKs to your app

1. In your **module (app-level) Gradle file**
   (usually `<project>/<app-module>/build.gradle.kts` or
   `<project>/<app-module>/build.gradle`),
   add the dependencies for the
   [Firebase products](https://firebase.google.com/docs/android/setup#available-libraries)
   that you want to use in your app. We recommend using the
   [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom) to control
   library versioning.

   ### Analytics enabled

   ```groovy
   dependencies {
     // ...

     // Import the Firebase BoM
     implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

     // When using the BoM, you don't specify versions in Firebase library dependencies

     // Add the dependency for the Firebase SDK for Google Analytics
     implementation("com.google.firebase:firebase-analytics")

     // TODO: Add the dependencies for any other Firebase products you want to use
     // See https://firebase.google.com/docs/android/setup#available-libraries
     // For example, add the dependencies for Firebase Authentication and Cloud Firestore
     implementation("com.google.firebase:firebase-auth")
     implementation("com.google.firebase:firebase-firestore")
   }
   ```

   By using the
   [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom),
   your app will always use compatible versions of Firebase Android
   libraries.

   ### Analytics not enabled

   ```groovy
   dependencies {
     // ...

     // Import the Firebase BoM
     implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

     // When using the BoM, you don't specify versions in Firebase library dependencies

     // TODO: Add the dependencies for Firebase products you want to use
     // See https://firebase.google.com/docs/android/setup#available-libraries
     // For example, add the dependencies for Firebase Authentication and Cloud Firestore
     implementation("com.google.firebase:firebase-auth")
     implementation("com.google.firebase:firebase-firestore")
   }
   ```

   By using the
   [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom),
   your app will always use compatible versions of Firebase Android
   libraries.
2. After adding the dependencies for the products you want to use, sync your
   Android project with Gradle files.

   <br />


   Are you getting a build failure about invoke-custom support and enabling
   desugaring? Here's how to fix it.

   <br />

   > Gradle builds that use Android Gradle plugin (AGP) v4.2 or earlier need to
   > enable Java 8 support. Otherwise, these Android projects get a build
   > failure when adding a Firebase SDK.
   >
   > To fix this build failure, you can follow one of two options:
   > - Add the listed `compileOptions` from the error message to your **app-level** `build.gradle.kts` or `build.gradle` file.
   > - Increase the `minSdk` for your Android project to 26 or above.
   >
   > Learn more about this build failure in
   > [this FAQ](https://firebase.google.com/docs/android/troubleshooting-faq#desugaring-build-failure).

   <br />

   <br />

That's it! You can skip ahead to check out the recommended
[next steps](https://firebase.google.com/docs/android/setup#next_steps).

If you're having trouble getting set up, though, visit the
[Android troubleshooting \& FAQ](https://firebase.google.com/docs/android/troubleshooting-faq).

<br />

*** ** * ** ***

## **Option 2**: Add Firebase using the Firebase Assistant

The [Firebase Assistant](https://firebase.google.com/docs/android/learn-more#firebase-assistant) registers
your app with a Firebase project and adds the necessary Firebase files, plugins,
and dependencies to your Android project --- all from within Android Studio!

1. Open your Android project in Android Studio, then make sure that you're
   using the latest versions of Android Studio and the Firebase Assistant:

   - Windows / Linux: **Help \> Check for updates**
   - macOS: **Android Studio \> Check for updates**
2. Open the Firebase Assistant: **Tools \> Firebase**.

3. In the *Assistant* pane, choose a Firebase product to add to your app.
   Expand its section, then click the tutorial link
   (for example, **Analytics \> Log an Analytics event**).

   1. Click **Connect to Firebase** to connect your Android project with Firebase.

      <br />

      What does this workflow do?

      <br />

      > - This workflow automatically creates a new Firebase Android app using
      >   your app's
      >   [package name](https://developer.android.com/studio/build/application-id).
      >   You can create this new Firebase Android app in either an existing
      >   Firebase project or a new project.
      >
      >   Here are some tips about setting up your Firebase project:
      >   - Check out our
      >     [best practices](https://firebase.google.com/docs/projects/dev-workflows/general-best-practices)
      >     for adding apps to a Firebase project, including how to handle
      >     multiple variants.
      >
      >   - If you create a new project, we strongly recommend that you set up
      >     Google Analytics for your project, which enables you to have
      >     an optimal experience using many Firebase products.
      >
      > - This workflow also adds your Firebase project's Android
      >   configuration file (`google-services.json`) to the module
      >   (app-level) directory of your app.
      >
      >   > [!NOTE]
      >   > **Note:** The Firebase config file contains unique, but non-secret identifiers for your project.   
      >   > Visit [Understand Firebase
      >   > Projects](https://firebase.google.com/docs/projects/learn-more#config-files-objects) to learn more about this config file.
      >
      <br />

      <br />

   2. Click the button to add a desired Firebase product (for example,
      **Add Analytics to your app**).

4. Sync your app to ensure that all dependencies have the necessary versions.

5. In the *Assistant* pane, follow the remaining setup instructions for your
   selected Firebase product.

6. Add as many other Firebase products as you'd like via the Firebase
   Assistant!

> [!NOTE]
> **Do you want an easier way to manage library versions?**   
>
> You can use the
> [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom) to manage
> your Firebase library versions and ensure that your app is always using
> compatible library versions.

That's it! Make sure to check out the recommended
[next steps](https://firebase.google.com/docs/android/setup#next_steps).

If you're having trouble getting set up, though, visit the
[Android troubleshooting \& FAQ](https://firebase.google.com/docs/android/troubleshooting-faq).

<br />

*** ** * ** ***

## Available libraries

This section lists the Firebase products supported for Android and their Gradle
dependencies. Learn more about these Firebase Android libraries:

- Reference documentation
  ([Kotlin](https://firebase.google.com/docs/reference/kotlin/packages) \|
  [Java](https://firebase.google.com/docs/reference/android/packages))

- Firebase Android SDK
  [GitHub repo](https://github.com/firebase/firebase-android-sdk)

Note that when using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom),
you don't specify individual library versions when you declare Firebase library
dependencies in your Gradle build configuration file.

> [!NOTE]
> **Important:** **Kotlin developers should now
> depend on the main modules instead of the KTX modules** (when using [Firebase BoM v32.5.0+](https://firebase.google.com/support/release-notes/android#bom_v32-5-0) or main module versions listed in BoM v32.5.0+). In [July 2025](https://firebase.google.com/support/release-notes/android#2025-07-21), we stopped releasing new versions of the KTX modules, and we removed the KTX libraries from the Firebase Android BoM (v34.0.0). For details, see the [FAQ about this initiative](https://firebase.google.com/docs/android/kotlin-migration).

| Service or Product | Gradle dependency | Latest version |   |
|---|---|---|---|
| [Firebase Android BoM (Bill of Materials)](https://firebase.google.com/docs/android/learn-more#bom) | com.google.firebase:firebase-bom The latest Firebase BoM version contains the latest versions of each Firebase Android library. To learn which library versions are mapped to a specific BoM version, review the release notes for that BoM version. | 34.10.0 |   |
| [AdMob](https://firebase.google.com/docs/admob/android/quick-start) | com.google.android.gms:play-services-ads | 25.0.0 | Yes |
| [Firebase AI Logic](https://firebase.google.com/docs/ai-logic/get-started) ^1^ | com.google.firebase:firebase-ai | 17.10.0 |   |
| [Firebase AI Logic On-Device](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started) | com.google.firebase:firebase-ai-ondevice | 16.0.0-beta01 |   |
| [Firebase AI KSP](https://firebase.google.com/docs/ai-logic/get-started) | com.google.firebase:firebase-ai-ksp-processor | 16.0.1 |   |
| [Analytics](https://firebase.google.com/docs/analytics/get-started?platform=android) | com.google.firebase:firebase-analytics | 23.0.0 | Yes |
| [App Check custom provider](https://firebase.google.com/docs/app-check) | com.google.firebase:firebase-appcheck | 19.0.2 |   |
| [App Check debug provider](https://firebase.google.com/docs/app-check) | com.google.firebase:firebase-appcheck-debug | 19.0.2 |   |
| [App Check Play Integrity provider](https://firebase.google.com/docs/app-check) | com.google.firebase:firebase-appcheck-playintegrity | 19.0.2 |   |
| [App Distribution](https://firebase.google.com/docs/app-distribution/android/set-up-alerts) | com.google.firebase:firebase-appdistribution | 16.0.0-beta17 |   |
| [App Distribution API](https://firebase.google.com/docs/app-distribution/android/set-up-alerts) | com.google.firebase:firebase-appdistribution-api | 16.0.0-beta17 |   |
| [App Distribution plugin](https://firebase.google.com/docs/app-distribution) | com.google.firebase:firebase-appdistribution-gradle | 5.2.1 |   |
| [Authentication](https://firebase.google.com/docs/auth/android/start) | com.google.firebase:firebase-auth | 24.0.1 |   |
| [Cloud Firestore](https://firebase.google.com/docs/firestore) | com.google.firebase:firebase-firestore | 26.1.1 |   |
| [Cloud Functions for Firebase Client SDK](https://firebase.google.com/docs/functions) | com.google.firebase:firebase-functions | 22.1.0 |   |
| [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/android/client) | com.google.firebase:firebase-messaging | 25.0.1 | Yes |
| [Cloud Storage](https://firebase.google.com/docs/storage/android/start) | com.google.firebase:firebase-storage | 22.0.1 |   |
| [Crashlytics](https://firebase.google.com/docs/crashlytics/android/get-started) | com.google.firebase:firebase-crashlytics | 20.0.4 | Yes |
| [Crashlytics NDK](https://firebase.google.com/docs/crashlytics/android/get-started-ndk) | com.google.firebase:firebase-crashlytics-ndk | 20.0.4 | Yes |
| [Crashlytics plugin](https://firebase.google.com/docs/crashlytics/android/get-started) | com.google.firebase:firebase-crashlytics-gradle | 3.0.6 | Yes |
| [Data Connect](https://firebase.google.com/docs/data-connect/quickstart#kotlin-android) | com.google.firebase:firebase-dataconnect | 17.1.4 |   |
| [Dynamic feature module support](https://firebase.google.com/docs/android/learn-more#dynamic-feature-modules) | com.google.firebase:firebase-dynamic-module-support | 16.0.0-beta04 |   |
| [In-App Messaging](https://firebase.google.com/docs/in-app-messaging) | com.google.firebase:firebase-inappmessaging | 22.0.2 | Yes *(required)* |
| [In-App Messaging Display](https://firebase.google.com/docs/in-app-messaging) | com.google.firebase:firebase-inappmessaging-display | 22.0.2 | Yes *(required)* |
| [Firebase installations](https://firebase.google.com/docs/projects/manage-installations) | com.google.firebase:firebase-installations | 19.1.0 |   |
| [Firebase ML Model Downloader API](https://firebase.google.com/docs/ml-kit) | com.google.firebase:firebase-ml-modeldownloader | 26.0.1 |   |
| [Performance Monitoring](https://firebase.google.com/docs/perf-mon/get-started-android) | com.google.firebase:firebase-perf | 22.0.4 |   |
| [Performance Monitoring plugin](https://firebase.google.com/docs/perf-mon/get-started-android) | com.google.firebase:perf-plugin | 2.0.2 |   |
| [Firebase Phone Number Verification](https://firebase.google.com/docs/phone-number-verification/android/get-started) | com.google.firebase:firebase-pnv | 16.0.0-beta01 |   |
| [Realtime Database](https://firebase.google.com/docs/database) | com.google.firebase:firebase-database | 22.0.1 |   |
| [Remote Config](https://firebase.google.com/docs/remote-config/get-started?platform=android) | com.google.firebase:firebase-config | 23.0.1 | Yes |
| [Google Play services plugin](https://developers.google.com/android/guides/google-services-plugin) | com.google.gms:google-services | 4.4.4 |   |
| **DEPRECATED OR UNSUPPORTED LIBRARIES** ||||
| [Dynamic Links](https://firebase.google.com/docs/dynamic-links/android/create) | com.google.firebase:firebase-dynamic-links | 22.1.0 | Yes |
| **Firebase KTX modules - no longer supported** > [!WARNING] > **In [July 2025](https://firebase.google.com/support/release-notes/android#2025-07-21), > we stopped releasing new versions of KTX modules for Firebase libraries, and > we removed the KTX libraries from the Firebase Android BoM (v34.0.0).** > If you use KTX APIs from the previously released KTX modules, we strongly > recommend that you ***migrate your app to use KTX APIs from the main > modules instead*** . For details, see the > [FAQ about this initiative](https://firebase.google.com/docs/android/kotlin-migration). |---|---|---|---| | [Analytics](https://firebase.google.com/docs/analytics/get-started?platform=android) | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-analytics-ktx | 22.5.0 | Yes | | [App Check custom provider](https://firebase.google.com/docs/app-check) | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-appcheck-ktx | 18.0.0 |   | | [App Distribution API](https://firebase.google.com/docs/app-distribution/android/set-up-alerts) | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-appdistribution-api-ktx | 16.0.0-beta15 |   | | [Authentication](https://firebase.google.com/docs/auth/android/start) | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-auth-ktx | 23.2.1 |   | | [Cloud Firestore](https://firebase.google.com/docs/firestore) | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-firestore-ktx | 25.1.4 |   | | [Cloud Functions for Firebase Client SDK](https://firebase.google.com/docs/functions) | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-functions-ktx | 21.2.1 |   | | [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/android/client) | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-messaging-ktx | 24.1.2 | Yes | | [Cloud Storage](https://firebase.google.com/docs/storage/android/start) | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-storage-ktx | 21.0.2 |   | | [Crashlytics](https://firebase.google.com/docs/crashlytics/android/get-started) | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-crashlytics-ktx | 19.4.4 | Yes | | [Dynamic Links](https://firebase.google.com/docs/dynamic-links/android/create) | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-dynamic-links-ktx | 22.1.0 | Yes | | [In-App Messaging](https://firebase.google.com/docs/in-app-messaging) | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-inappmessaging-ktx | 21.0.2 | Yes *(required)* | | [In-App Messaging Display](https://firebase.google.com/docs/in-app-messaging) | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-inappmessaging-display-ktx | 21.0.2 | Yes *(required)* | | [Firebase installations](https://firebase.google.com/docs/projects/manage-installations) | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-installations-ktx | 18.0.0 |   | | [Firebase ML Model Downloader API](https://firebase.google.com/docs/ml-kit) | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-ml-modeldownloader-ktx | 25.0.1 |   | | [Performance Monitoring](https://firebase.google.com/docs/perf-mon/get-started-android) | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-perf-ktx | 21.0.5 |   | | [Realtime Database](https://firebase.google.com/docs/database) | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-database-ktx | 21.0.0 |   | | [Remote Config](https://firebase.google.com/docs/remote-config/get-started?platform=android) | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-config-ktx | 22.1.2 | Yes | ||||
| **Firebase ML Kit libraries** |---|---|---|---| | [Firebase ML Custom Model APIs](https://firebase.google.com/docs/ml-kit) | com.google.firebase:firebase-ml-model-interpreter | 22.0.4 |   | | [Firebase ML Vision APIs](https://firebase.google.com/docs/ml-kit) | com.google.firebase:firebase-ml-vision | 24.1.0 |   | | [Firebase ML: Image Labeling Model](https://firebase.google.com/docs/ml-kit) | com.google.firebase:firebase-ml-vision-image-label-model | 20.0.2 |   | | [Firebase ML: Object Detection and Tracking Model](https://firebase.google.com/docs/ml-kit) | com.google.firebase:firebase-ml-vision-object-detection-model | 19.0.6 |   | | [Firebase ML: Face Detection Model](https://firebase.google.com/docs/ml-kit) | com.google.firebase:firebase-ml-vision-face-model | 20.0.2 |   | | [Firebase ML: Barcode Scanning Model](https://firebase.google.com/docs/ml-kit) | com.google.firebase:firebase-ml-vision-barcode-model | 16.1.2 |   | | [Firebase ML: AutoML Vision Edge API](https://firebase.google.com/docs/ml-kit) | com.google.firebase:firebase-ml-vision-automl | 18.0.6 |   | | [Firebase ML: Natural Language APIs](https://firebase.google.com/docs/ml-kit) | com.google.firebase:firebase-ml-natural-language | 22.0.1 |   | | [Firebase ML: Language Identification Model](https://firebase.google.com/docs/ml-kit) | com.google.firebase:firebase-ml-natural-language-language-id-model | 20.0.8 |   | | [Firebase ML: Translate Model](https://firebase.google.com/docs/ml-kit) | com.google.firebase:firebase-ml-natural-language-translate-model | 20.0.9 |   | | [Firebase ML: Smart Reply Model](https://firebase.google.com/docs/ml-kit) | com.google.firebase:firebase-ml-natural-language-smart-reply-model | 20.0.8 |   | ||||

^**1** *Firebase AI Logic was formerly called
"Vertex AI in Firebase" with the package
`com.google.firebase:firebase-vertexai`.*^

<br />

*** ** * ** ***

## Next steps

**Add Firebase services to your app:**

- Build generative AI features with Gemini and Imagen models
  using [Firebase AI Logic](https://firebase.google.com/docs/ai-logic/get-started).

- Gain insights on user behavior with
  [Analytics](https://firebase.google.com/docs/analytics/android/start).

- Set up a user authentication flow with
  [Authentication](https://firebase.google.com/docs/auth/android/start).

- Store data, like user information, with
  [Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart) or
  [Realtime Database](https://firebase.google.com/docs/database/android/start).

- Store files, like photos and videos, with
  [Cloud Storage](https://firebase.google.com/docs/storage/android/start).

- Trigger backend code that runs in a secure environment with
  [Cloud Functions](https://firebase.google.com/docs/functions/callable#call_the_function).

- Send notifications with
  [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/android/client).

- Find out when and why your app is crashing with
  [Crashlytics](https://firebase.google.com/docs/crashlytics).

**Learn about Firebase:**

- Visit [Understand Firebase Projects](https://firebase.google.com/docs/projects/learn-more) to learn more
  about Firebase projects and best practices for projects.

- Visit [Learn more about Android and Firebase](https://firebase.google.com/docs/android/learn-more) if you
  have questions about concepts that are unfamiliar or specific to Firebase and
  Android development.

- Explore
  [sample Firebase apps](https://github.com/firebase/quickstart-android).

- Get hands-on experience with the [Firebase Android
  Codelab](https://codelabs.developers.google.com/codelabs/firebase-android/).

- Learn more with the
  [Firebase in a Weekend](https://udacity.com/course/ud0352) course.

- Prepare to launch your app:

  - Set up [budget
    alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails) for your project in the Google Cloud console.
  - Monitor the [*Usage and billing*
    dashboard](https://console.firebase.google.com/project/_/usage) in the Firebase console to get an overall picture of your project's usage across multiple Firebase services.
  - Review the [Firebase launch checklist](https://firebase.google.com/support/guides/launch-checklist).
- Having trouble with Firebase and your Android project?
  Visit the [Android troubleshooting \& FAQ](https://firebase.google.com/docs/android/troubleshooting-faq).