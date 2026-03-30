# Source: https://firebase.google.com/docs/android/learn-more.md.txt

As you're developing your Android project using Firebase, you might discover
concepts that are unfamiliar or specific to Firebase. This page aims to answer
those questions or point you to resources to learn more.

If you have questions about a topic not covered on this page, feel free to visit
one of our [online communities](https://firebase.google.com/community#join-the-discussion). We'll also
update this page with new topics periodically, so check back to see if we've
added the topic you want to learn about!

## Firebase Assistant plugin for Android Studio

The Firebase Assistant is an Android Studio plugin that registers your Android
app with a Firebase project and adds the necessary Firebase config files,
plugins, and dependencies to your Android project --- all from within Android
Studio!

Follow the instructions in the
[Android getting started page](https://firebase.google.com/docs/android/setup#assistant) to use the
Firebase Assistant. Make sure that you're using the most up-to-date versions of
both Android Studio and the Firebase Assistant
(go to **File \> Check for updates**).

When you select specific Firebase products to add to your app, the Firebase
Assistant automatically declares the required dependencies in your
`app/build.gradle` file. Note that if you want to use the
[Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom) *(recommended)* , update the dependencies in your
**module (app-level) Gradle file** (usually `app/build.gradle`) to import the
BoM platform. You'll also need to remove the versions from each Firebase
library dependency line.

Additionally, to use some Firebase products, you must enable APIs or provision
resources outside of Android Studio. The instructions for each product in the
Firebase Assistant describe any additional actions that you need to do. For
example, to use Cloud Firestore, you need to set up your database and rules in the
Firebase console.

## Google services --- plugin and config file

As part of adding Firebase to your Android project, you need to add the
`google-services` plugin and a `google-services.json` configuration file to
your project.

If you add Firebase to your Android project via
the [Firebase console](https://firebase.google.com/docs/android/setup#console),
the [Management REST API](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project?platform=android#add-apps),
or the [Firebase CLI](https://firebase.google.com/docs/cli#management-commands),
you must manually add the plugin and config file to your project. However, if
you use the [Firebase Assistant](https://firebase.google.com/docs/android/learn-more#firebase-assistant), these tasks are
automatically done for you during setup.

> [!NOTE]
> **Note:** The `google-services.json` config file contains unique, but non-secret identifiers for your project. To learn more about this config file, visit [Understand Firebase Projects](https://firebase.google.com/docs/projects/learn-more).

Visit the
[Android documentation](https://developers.google.com/android/guides/google-services-plugin)
to learn about how the Google services plugin and config file work together.

## Firebase Android BoM (Bill of Materials)

The Firebase Android BoM (Bill of Materials) lets you manage all your
Firebase library versions by specifying only one version --- the BoM's
version.

When you use the Firebase BoM in your app, the BoM automatically pulls
in the individual library versions mapped to BoM's version. **All the
individual library versions will be compatible.** When you update the BoM's
version in your app, all the Firebase libraries that you use in your app will
update to the versions mapped to that BoM version.

To learn which Firebase library versions are mapped to a specific BoM
version, check out the [release notes](https://firebase.google.com/support/release-notes/android) for that
BoM version. If you need to compare the library versions mapped to one
BoM version compared to another BoM version, use the
[comparison widget](https://firebase.google.com/docs/android/learn-more#compare-bom-versions) below.

Learn more about [Gradle's support for BoM platforms](https://docs.gradle.org/4.6-rc-1/userguide/managing_transitive_dependencies.html#sec:bom_import).

Here's how to use the Firebase Android BoM to declare dependencies in your
**module (app-level) Gradle file** (usually `app/build.gradle`). When using the
BoM, you don't specify individual library versions in the dependency lines.

```
dependencies {
  // Import the BoM for the Firebase platform
  implementation platform('com.google.firebase:firebase-bom:34.10.0')

  // Declare the dependencies for the desired Firebase products without specifying versions
  // For example, declare the dependencies for Firebase Authentication and Cloud Firestore
  implementation 'com.google.firebase:firebase-auth'
  implementation 'com.google.firebase:firebase-firestore'
}
```

Here are some frequently asked questions about using the Firebase Android BoM:

<br />


How do I use a *different* library version than what's designated in
the BoM?

<br />

> [!NOTE]
> **Important:** If you use more than one Firebase library in your app, specifying a different version than what's designated in the BoM is not recommended. The specified version may not be compatible with other Firebase library versions.

Here's how to override a library version designated in the BoM:

1. Maintain the line to import the BoM platform.

2. In the library's dependency line, specify the desired library version. For
   example, here's how to declare dependencies if you want to use v18.0.0
   of App Indexing no matter what version is designated in the BoM,
   ***but*** you want to use the BoM's versions for
   Authentication and Cloud Firestore:

   ```
   dependencies {
     // Import the BoM for the Firebase platform
     implementation platform('com.google.firebase:firebase-bom:34.10.0')

     // Declare the dependency for the App Indexing library and specify a version
     // This specified library version overrides the version designated in the BoM.
     implementation 'com.google.firebase:firebase-appindexing:18.0.0'

     // Declare the dependencies for the other Firebase libraries without specifying versions
     // These libraries will use the versions designated in the BoM.
     implementation 'com.google.firebase:firebase-auth'
     implementation 'com.google.firebase:firebase-firestore'
   }
   ```

<br />

<br />

<br />


Does the BoM automatically add all the Firebase libraries to my app?

<br />

No. To actually add and use Firebase libraries in your app, you must declare
each library as a separate dependency line in your **module (app-level) Gradle
file** (usually `app/build.gradle`).

Using the BoM ensures that the *versions* of any Firebase libraries in your
app are compatible, but the BoM doesn't actually *add* those Firebase
libraries to your app.

<br />

<br />

<br />


Are the Firebase Kotlin extensions (KTX) libraries supported by the BoM?

<br />

In July 2025 (BoM v34.0.0), the Firebase Kotlin extensions (KTX) libraries
were removed from the BoM. If you use a BoM version earlier than
v34.0.0, then you can continue using KTX libraries in your app.

However, we recommend that you migrate your app to use KTX APIs from the main
modules; otherwise, you won't be able to update to newer BoM versions and
thus newer versions of the Firebase product libraries. For details, see the
[FAQ about this initiative](https://firebase.google.com/docs/android/kotlin-migration).

<br />

<br />

<br />


Can I use the BoM to add Android libraries that are *not* from
Firebase?

<br />

No. The Firebase Android BoM only manages library versions for Firebase
libraries.

<br />

<br />

<br />


Why is the BoM the recommended way to manage Firebase library versions?

<br />

Even though each Firebase library is versioned independently, they are built
together to ensure that the latest release of each library is compatible with
the others.

By using the BoM to manage your app's Firebase library versions, you don't
need to track which version of a Firebase library is compatible with another
Firebase library.

Even if you only use one Firebase library in your app right now, we still
recommend using the BoM because you never know when you might want to use
another Firebase library!

<br />

<br />

<br />


My app uses a Gradle version *earlier than 5.0* --- can I still use the
BoM?

<br />

Yes, you can still use the BoM! For Gradle 5.0 and later, BoM support is
automatically enabled. However, **for earlier versions of Gradle,**
you just need to
[enable the BoM feature](https://docs.gradle.org/4.6-rc-1/release-notes.html)
and import the BoM a bit differently.

1. To your `settings.gradle` file, add
   `enableFeaturePreview('IMPROVED_POM_SUPPORT')`.

2. To your **module (app-level) Gradle file** (usually
   `app/build.gradle`), import the BoM like a normal library (without the
   `platform` modifier), like so:

   ```
   dependencies {
     // Import the Firebase BoM
     implementation 'com.google.firebase:firebase-bom:34.10.0'

     // Declare the dependencies for the desired Firebase products, without specifying versions
     // For example, declare the dependencies for Firebase Authentication and Cloud Firestore
     implementation 'com.google.firebase:firebase-auth'
     implementation 'com.google.firebase:firebase-firestore'
   }
   ```

<br />

<br />

<br />


How do I report an issue or offer feedback on the BoM?

<br />

Visit the
[Firebase Android SDK repo on GitHub](https://github.com/firebase/firebase-android-sdk/issues).

<br />

<br />

#### Compare Firebase BoM versions

<iframe src="https:///frame/docs/android/learn-more_3db40c83baac740808bcda9748085e5ac5987adbf452e0f44f2ba8b3356e2fb8.frame" class="framebox inherit-locale " allow="clipboard-write https://" allowfullscreen is-upgraded></iframe>

## Kotlin extensions (KTX) library modules

> [!WARNING]
> **In [July 2025](https://firebase.google.com/support/release-notes/android#2025-07-21),
> we stopped releasing new versions of KTX modules for Firebase libraries, and
> we removed the KTX libraries from the Firebase Android BoM (v34.0.0).**
>
> If you use KTX APIs from the previously released KTX modules, we strongly
> recommend that you ***migrate your app to use KTX APIs from the main
> modules instead*** . For details, see the
> [FAQ about this initiative](https://firebase.google.com/docs/android/kotlin-migration).

## Feature modules and Play Feature Delivery

As of May 2021 (Firebase BoM v28.0.0), Firebase Android SDKs can be
used in dynamic feature modules which are installed separately from your base
application module.

To enable support for dynamic feature modules, add the following dependency
to your **base** module's `build.gradle` file:

    dependencies {
      implementation 'com.google.firebase:firebase-dynamic-module-support:16.0.0-beta04'
    }

Now that you've added dynamic module support, you can add Firebase SDK
dependencies (with or without the Firebase BoM) to feature modules of your
app and use them as you normally would.

For example, if your application uses Realtime Database to power a specific realtime
feature you could add the `firebase-database` dependency to the `build.gradle`
of the feature module rather than the base module. This will reduce download
size for most users.

Be aware of the following caveats when using Firebase SDKs in feature modules:

- Products such as Dynamic Links or Firebase In-App Messaging which rely on the Analytics
  `first_open` event may miss this event when used in a dynamic feature module.

- When using Cloud Firestore and Authentication together, you should always include them
  both in the same module. If this is not possible, then make sure that Authentication
  is loaded *before* Cloud Firestore; otherwise, some Cloud Firestore operations may
  have an incorrect authentication state.

- When using `firebase-crashlytics-ndk` as a dependency of a dynamic feature
  module, you need to set the `unstrippedNativeLibsDir` property in your app's
  `build.gradle` file, as described in the
  [Crashlytics NDK documentation](https://firebase.google.com/docs/crashlytics/ndk-reports#upload-external-dependencies).

For more information on feature modules and Play Feature Delivery, visit
[Overview of Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery).

## Google services Gradle plugin vs Google Play services vs Google Play Store

Several pieces of the Google, Firebase, and Android ecosystem have similar
naming conventions. Here's a brief explanation for each:

Google services Gradle plugin
:   A Gradle plugin (`com.google.gms.google-services`) that runs at build time to
    ensure that your app has the right configuration to access Firebase and Google
    APIs
:   Despite its name, this plugin has no relation to Google Play services (see
    next entry) and has no impact on your app's capabilities at runtime.
:   This plugin also processes the `google-services.json` file that you add to
    your app as part of setting up Firebase. Learn more about the
    [Google services Gradle plugin](https://firebase.google.com/docs/android/learn-more#google-services-plugin-and-file).

Google Play services
:   An invisible background service that runs on an Android device and provides
    several common Google APIs (like Google Maps and Google Sign In) to apps on
    the device
:   By centralizing these common APIs into a single service, it reduces the size
    of other apps and allows a device to receive automatic security updates and
    feature enhancements without an OS update. Learn more about
    [Google Play services](https://developers.google.com/android/guides/overview).

Google Play Store
:   A store to download apps, movies, books, and more on an Android device
:   As a developer, you manage the distribution, releases, etc. for your app via
    the Google Play Console. If a device has the Google Play Store, it's also
    running Google Play services (see previous entry). Learn more about the
    [Google Play Store for developers](https://developer.android.com/distribute).

Google Play Games services
:   A set of APIs for mobile game developers
:   Learn more about
    [Google Play Games services](https://developers.google.com/games/services)
    and how to
    [integrate Firebase with your Google Play Games services project](https://firebase.google.com/support/guides/integrate-play-games).

## Open source resources for Firebase Android SDKs

Firebase supports open source development, and we encourage community
contributions and feedback.

### Firebase Android SDKs

Most Firebase Android SDKs are developed as open source libraries in our public
[Firebase GitHub repository](https://github.com/firebase/firebase-android-sdk).
We're actively working to move the remaining privately developed Firebase
libraries to our public GitHub soon!

### Quickstart samples

Firebase maintains a collection of quickstart samples for most Firebase APIs on
Android. Find these quickstarts in our public
[Firebase GitHub quickstart repository](https://github.com/firebase/quickstart-android).

You can open each quickstart as an Android Studio project, then run them on a
mobile device or a virtual device (AVD). Or you can use these quickstarts as
example code for using Firebase SDKs.

## Other topics of interest

- [Dependencies of Firebase Android SDKs on Google Play services](https://firebase.google.com/docs/android/android-play-services)
- [Link your Firebase app to Google Play](https://support.google.com/firebase/answer/6392038)
- [Integrate with your Play Games services project](https://firebase.google.com/support/guides/integrate-play-games)