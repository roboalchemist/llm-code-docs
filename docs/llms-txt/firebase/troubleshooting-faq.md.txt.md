# Source: https://firebase.google.com/docs/android/troubleshooting-faq.md.txt

This page offers tips and troubleshooting for Android-specific issues
that you might encounter when using Firebase.

Have other challenges or don't see your issue outlined below? Make sure to check
out the [main Firebase FAQ](https://firebase.google.com/support/faq) for more pan-Firebase or
product-specific FAQ.

You can also check out the
[Firebase Android SDK GitHub repo](https://github.com/firebase/firebase-android-sdk/issues)
for an up-to-date list of reported issues and troubleshooting. We encourage you
to file your own Firebase Android SDK related issues there, too!

#### I'm getting an error that the `ktx` library failed to resolve or
could not be found.

This error is likely because you're using the Firebase BoM and
specifying a KTX module as your product library dependency.

**In July 2025, we stopped releasing new versions of the KTX modules,
and we removed the KTX libraries from the Firebase Android BoM
(v34.0.0).**

If you use KTX APIs from previously released KTX modules, we recommend
that you ***migrate your app to use KTX APIs from the main modules
instead*** . For details, see the
[FAQ about this initiative](https://firebase.google.com/docs/android/kotlin-migration).

#### Do I need to provide a SHA-1 when adding an Android app to a Firebase
project?

[SHA-1 information](https://developers.google.com/android/guides/client-auth)
is required by Firebase Authentication (when using
[Google signin](https://firebase.google.com/docs/auth/android/google-signin) or
[phone number signin](https://firebase.google.com/docs/auth/android/phone-auth)) and
[Firebase Dynamic Links](https://firebase.google.com/docs/dynamic-links). If you're not using
these features, you don't have to provide a SHA-1.

#### How do I resolve this error: "An OAuth2 client already exists for this
package name and SHA-1 in another project"?

This error occurs if we detect that another Firebase or Google Cloud
project contains an OAuth 2.0 client ID with the package name
and SHA-1 that you specified. Learn how to
[resolve this error](https://support.google.com/firebase/answer/6401008).

#### When I add Firebase to my Android project, I get a "Could not find" error.

This error usually means that your app is missing one or more references
to Google's Maven repository. Make sure to include Google's Maven repository
(`google()`) in your Gradle Configuration file.

- If your project is using the `plugins` syntax, include it in the `plugins` section in your `settings.gradle.kts` or `settings.gradle` file.
- If your project is using the `buildscript` syntax, include it in both the `buildscript` and `allprojects` sections in your project-level `build.gradle.kts` or `build.gradle` file.

<br />

<br />

#### When I add a Firebase SDK to my Android project, I get an error about
invoke-custom support and enabling desugaring.

<br />

In May 2021 (Firebase BoM v28.0.0), Firebase disabled desugaring for all its
Android libraries
(see [release note](https://firebase.google.com/support/release-notes/android#2021-05-11)).

This change means that Gradle builds that use Android Gradle plugin (AGP) v4.2
or earlier need to enable Java 8 support. Otherwise, when adding a Firebase SDK,
these Android projects get the following build failure:

```
D8: Invoke-customs are only supported starting with Android O (--min-api 26)
Caused by: com.android.builder.dexing.DexArchiveBuilderException: Error while dexing.
The dependency contains Java 8 bytecode. Please enable desugaring by adding the following to build.gradle
android {
    compileOptions {
        sourceCompatibility 1.8
        targetCompatibility 1.8
    }
}
See https://developer.android.com/studio/write/java8-support.html for details.
Alternatively, increase the minSdkVersion to 26 or above.
```

To fix this build failure, you can follow one of two options:

- Add the listed `compileOptions` from the error message to your **app-level** `build.gradle.kts` or `build.gradle` file.
- Increase the `minSdkVersion` for your Android project to 26 or above.

<br />

<br />

#### Google Sign-in is showing the error "12500:" after I released my app. How
do I fix it?


There are two possible reasons why this would happen: you haven't provided a
support email or you're missing a SHA key. In order to fix this error, make
sure **all** of these conditions are true:

- You've added a support email to the [General Settings of your project](https://console.firebase.google.com/project/_/settings/general/) in the Firebase console.
- You've added the [SHA-1 Certificate fingerprint from your release/production keystore](https://developers.google.com/android/guides/client-auth#using_keytool_on_the_certificate) to your Firebase Android App in the Firebase console (go to [**Project settings**](https://console.firebase.google.com/project/_/settings/general/), scroll down to *Your apps*, and then select your Android App).
- You've added the [SHA-1 Certificate fingerprint from the Google Play Console](https://developer.android.com/studio/publish/app-signing#api-providers) to your Firebase Android App in the Firebase console (go to [**Project settings**](https://console.firebase.google.com/project/_/settings/general/), scroll down to *Your apps*, and then select your Android App).

<br />

<br />

<br />

#### How to add Firebase plugins to an Android project using the `buildscript`
syntax?

<br />

> [!TIP]
> **Tip:** Consider [migrating from `buildscript` to `plugin` syntax](https://developer.android.com/build/migrate-to-kotlin-dsl#migrate-buildscript) as this allows Android Studio to perform code completion and provide other helpful suggestions.

Firebase has the following Gradle plugins:

| Plugin name | Maven coordinates | Latest version | Plugin ID |
|---|---|---|---|
| Google Play services plugin | `com.google.gms:google-services` | 4.4.4 | `com.google.gms.google-services` |
| App Distribution plugin | `com.google.firebase:firebase-appdistribution-gradle` | 5.2.1 | `com.google.firebase.appdistribution` |
| Crashlytics plugin | `com.google.firebase:firebase-crashlytics-gradle` | 3.0.6 | `com.google.firebase.crashlytics` |
| Performance Monitoring plugin | `com.google.firebase:perf-plugin` | 2.0.2 | `com.google.firebase.firebase-perf` |

<br />

Here's how to add a Firebase plugin to an Android project that still uses the
`buildscript` syntax:

1. In your **root-level (project-level)** Gradle file
   (`<project>/build.gradle.kts` or `<project>/build.gradle`), add the plugin as
   a dependency using its Maven coordinates:

   ### Kotlin

       buildscript {

           repositories {
             // Make sure that you have the following two repositories
             google()  // Google's Maven repository
             mavenCentral()  // Maven Central repository
           }

           dependencies {
             ...

             // Add the Maven coordinates and latest version of the plugin
             classpath ("PLUGIN_MAVEN_COORDINATES:PLUGIN_VERSION")
           }
       }

       allprojects {
         ...

         repositories {
           // Make sure that you have the following two repositories
           google()  // Google's Maven repository
           mavenCentral()  // Maven Central repository
         }
       }

   ### Groovy

       buildscript {

           repositories {
             // Make sure that you have the following two repositories
             google()  // Google's Maven repository
             mavenCentral()  // Maven Central repository
           }

           dependencies {
             ...

             // Add the Maven coordinates and latest version of the plugin
             classpath 'PLUGIN_MAVEN_COORDINATES:PLUGIN_VERSION'
           }
       }

       allprojects {
         ...

         repositories {
           // Make sure that you have the following two repositories
           google()  // Google's Maven repository
           mavenCentral()  // Maven Central repository
         }
       }

2. In your **module (app-level)** Gradle file (usually
   `<project>/<app-module>/build.gradle.kts` or
   `<project>/<app-module>/build.gradle`), add the plugin using its
   plugin ID:

   ### Kotlin

       plugins {
           id("com.android.application")

           // Add the ID of the plugin
           id("FIREBASE_PLUGIN_ID")
           ...
       }

   ### Groovy

       plugins {
           id 'com.android.application'

           // Add the ID of the plugin
           id 'FIREBASE_PLUGIN_ID'
           ...
       }

<br />

<br />

<br />

<br />

<br />

#### What open source notices should I include in my app?

<br />

The Firebase Android SDK contains a
[helper `Activity`](https://developers.google.com/android/guides/opensource)
for showing license information.

<br />

<br />