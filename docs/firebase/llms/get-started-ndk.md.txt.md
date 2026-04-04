# Source: https://firebase.google.com/docs/crashlytics/android/get-started-ndk.md.txt

<br />

<br />

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/crashlytics/ios/get-started) [Android](https://firebase.google.com/docs/crashlytics/android/get-started) [Android NDK](https://firebase.google.com/docs/crashlytics/android/get-started-ndk) [Flutter](https://firebase.google.com/docs/crashlytics/flutter/get-started) [Unity](https://firebase.google.com/docs/crashlytics/unity/get-started) |

<br />


<br />

<br />

If you use [native libraries](https://developer.android.com/ndk) in your
Android app, you can enable full stack traces and detailed crash reports for
your native code from Firebase Crashlytics with a few small updates to your
app's build configuration.

This guide describes how to configure crash reporting with the
Firebase Crashlytics SDK for NDK.

If you're looking for how to get started with Crashlytics in your Unity
projects, check out the
[Unity Getting Started guide](https://firebase.google.com/docs/crashlytics/unity/get-started).

## Before you begin

1. If you haven't already, [add Firebase](https://firebase.google.com/docs/android/setup) to your Android
   project. If you don't have an Android app, you can download
   a [sample app](https://firebase.google.com/docs/samples).

2. **Recommended** : To automatically get
   [breadcrumb logs](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports#get-breadcrumb-logs)
   to understand user actions leading up to a crash, non-fatal, or ANR event,
   you need to enable Google Analytics in your Firebase project.

   - If your existing Firebase project doesn't have Google Analytics
     enabled, you can enable Google Analytics from the
     [**Integrations** tab](https://console.firebase.google.com/project/_/settings/integrations/analytics) of your
     \> *Project settings*
     in the Firebase console.

   - If you're creating a new Firebase project, enable Google Analytics
     during the project creation workflow.

3. Make sure your app has the following ***minimum*** required versions:

   - Gradle 8.0
   - Android Gradle plugin 8.1.0
   - Google services Gradle plugin 4.4.1

## **Step 1** : Add the Crashlytics SDK for NDK to your app

In your **module (app-level) Gradle file** (usually `<project>/<app-module>/build.gradle.kts` or `<project>/<app-module>/build.gradle`), add the dependency for the Crashlytics NDK library for Android. We recommend using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom) to control library versioning.

<br />


For an optimal experience with Crashlytics, we recommend
[enabling Google Analytics](https://support.google.com/firebase/answer/9289399#linkga)
in your Firebase project and adding the Firebase SDK for Google Analytics to your app.

```
dependencies {
    // Import the BoM for the Firebase platform
    implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

    // Add the dependencies for the Crashlytics NDK and Analytics libraries
    // When using the BoM, you don't specify versions in Firebase library dependencies
    implementation("com.google.firebase:firebase-crashlytics-ndk")
    implementation("com.google.firebase:firebase-analytics")
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
    // Add the dependencies for the Crashlytics NDK and Analytics libraries
    // When NOT using the BoM, you must specify versions in Firebase library dependencies
    implementation("com.google.firebase:firebase-crashlytics-ndk:20.0.4")
    implementation("com.google.firebase:firebase-analytics:23.0.0")
}
```

<br />

## **Step 2** : Add the Crashlytics Gradle plugin to your app

1. In your **root-level (project-level)** Gradle file
   (`<project>/build.gradle.kts` or `<project>/build.gradle`), add the
   Crashlytics Gradle plugin to the `plugins` block:

   ### Kotlin

   > [!NOTE]
   > Are you still using the `buildscript` syntax? Learn how to [add Firebase plugins](https://firebase.google.com/docs/android/troubleshooting-faq#add-plugins-using-buildscript-syntax) using that syntax.

   ```kotlin
   plugins {
       // Make sure that you have the AGP plugin 8.1+ dependency
       id("com.android.application") version "8.1.4" apply false
       // ...

       // Make sure that you have the Google services Gradle plugin 4.4.1+ dependency
       id("com.google.gms.google-services") version "4.4.4" apply false

       // Add the dependency for the Crashlytics Gradle plugin
       id("com.google.firebase.crashlytics") version "3.0.6" apply false
   }
   ```

   ### Groovy

   > [!NOTE]
   > Are you still using the `buildscript` syntax? Learn how to [add Firebase plugins](https://firebase.google.com/docs/android/troubleshooting-faq#add-plugins-using-buildscript-syntax) using that syntax.

   ```groovy
   plugins {
       // Make sure that you have the AGP plugin 8.1+ dependency
       id 'com.android.application' version '8.1.4' apply false
       // ...

       // Make sure that you have the Google services Gradle plugin 4.4.1+ dependency
       id 'com.google.gms.google-services' version '4.4.4' apply false

       // Add the dependency for the Crashlytics Gradle plugin
       id 'com.google.firebase.crashlytics' version '3.0.6' apply false
   }
   ```

   > [!NOTE]
   > Is your app using a lower version of Gradle? Consider [upgrading](https://firebase.google.com/docs/crashlytics/troubleshooting#android-upgrade-to-gradle-plugin-v3); otherwise, you should use v2.9.9 of the Crashlytics Gradle plugin.

2. In your **module (app-level)** Gradle file
   (usually `<project>/<app-module>/build.gradle.kts` or
   `<project>/<app-module>/build.gradle`),
   add the Crashlytics Gradle plugin:

   ### Kotlin

   ```kotlin
   plugins {
     id("com.android.application")
     // ...

     // Make sure that you have the Google services Gradle plugin
     id("com.google.gms.google-services")

     // Add the Crashlytics Gradle plugin
     id("com.google.firebase.crashlytics")
   }
   ```

   ### Groovy

   ```groovy
   plugins {
     id 'com.android.application'
     // ...

     // Make sure that you have the Google services Gradle plugin
     id 'com.google.gms.google-services'

     // Add the Crashlytics Gradle plugin
     id 'com.google.firebase.crashlytics'
   }
   ```

## **Step 3**: Add the Crashlytics extension to your build

In your **module (app-level)** Gradle file
(usually `<project>/<app-module>/build.gradle.kts` or
`<project>/<app-module>/build.gradle`), configure the Crashlytics extension.

### Kotlin

```kotlin
import com.google.firebase.crashlytics.buildtools.gradle.CrashlyticsExtension

// ...

android {
  // ...
  buildTypes {
      getByName("release") {
          // Add this extension
          configure<CrashlyticsExtension> {
              // Enable processing and uploading of native symbols to Firebase servers.
              // By default, this is disabled to improve build speeds.
              // This flag must be enabled to see properly-symbolicated native
              // stack traces in the Crashlytics dashboard.
              nativeSymbolUploadEnabled = true
          }
      }
  }
}
```

### Groovy

```groovy
// ...

android {
  // ...
  buildTypes {
      release {
          // Add this extension
          firebaseCrashlytics {
              // Enable processing and uploading of native symbols to Firebase servers.
              // By default, this is disabled to improve build speeds.
              // This flag must be enabled to see properly-symbolicated native
              // stack traces in the Crashlytics dashboard.
              nativeSymbolUploadEnabled true
          }
      }
  }
}
```

> [!NOTE]
> **Note:** The Crashlytics NDK distribution includes native binaries for all [architectures](https://developer.android.com/ndk/guides/abis.html) supported by Android NDK. If your app targets a specific subset, you can use [ABI splits](http://tools.android.com/tech-docs/new-build-system/user-guide/apk-splits#TOC-ABIs-Splits) to exclude unnecessary architectures.

## **Step 4**: Set up automatic uploading of native symbols

To produce readable stack traces from NDK crashes, Crashlytics needs to know
about the symbols in your native binaries. The Crashlytics Gradle plugin
includes the `uploadCrashlyticsSymbolFileBUILD_VARIANT`
task to automate this process.

> [!NOTE]
> **Note:** Crashlytics supports [alternative options for uploading symbols](https://firebase.google.com/docs/crashlytics/android/get-started-ndk#alternative-options-symbol-uploading) depending on your app's configuration and tooling, such as non-Gradle builds.

1. So that you can access the task for automated symbol uploading, make sure
   that `nativeSymbolUploadEnabled` is set to `true` in your module (app-level)
   Gradle file.

2. For method names to appear in your stack traces, you must explicitly invoke
   the `uploadCrashlyticsSymbolFileBUILD_VARIANT`
   task after each build of your NDK library. For example:

   ```
   >./gradlew app:assembleBUILD_VARIANT\
              app:uploadCrashlyticsSymbolFileBUILD_VARIANT
   ```
3. Both the Crashlytics SDK for NDK and the Crashlytics Gradle plugin
   depend on the presence of the GNU build ID within the native shared objects.

   You can verify the presence of this ID by running
   `readelf -n` on each binary. If the build ID is
   absent, add `-Wl,--build-id` to your build system's
   flags to fix the problem.

## **Step 5**: Force a test crash to finish setup

To finish setting up Crashlytics and see initial data in the
Crashlytics dashboard of the Firebase console, you need to force a test
crash.

1. Add code to your app that you can use to force a test crash.

   You can use the following code in your app's `MainActivity` to add a button
   to your app that, when pressed, causes a crash. The button is labeled
   "Test Crash".

   ### Kotlin

   ```kotlin
   val crashButton = Button(this)
   crashButton.text = "Test Crash"
   crashButton.setOnClickListener {
      throw RuntimeException("Test Crash") // Force a crash
   }

   addContentView(crashButton, ViewGroup.LayoutParams(
          ViewGroup.LayoutParams.MATCH_PARENT,
          ViewGroup.LayoutParams.WRAP_CONTENT))
   ```

   ### Java

   ```java
   Button crashButton = new Button(this);
   crashButton.setText("Test Crash");
   crashButton.setOnClickListener(new View.OnClickListener() {
      public void onClick(View view) {
          throw new RuntimeException("Test Crash"); // Force a crash
      }
   });

   addContentView(crashButton, new ViewGroup.LayoutParams(
          ViewGroup.LayoutParams.MATCH_PARENT,
          ViewGroup.LayoutParams.WRAP_CONTENT));
   ```
2. Build and run your app.

3. Force the test crash in order to send your app's first crash report:

   1. Open your app from your test device or emulator.

   2. In your app, press the "Test Crash" button that you added using the code
      above.

   3. After your app crashes, restart it so that your app can send the crash
      report to Firebase.

4. Go to the [Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics) of the
   Firebase console to see your test crash.

   If you've refreshed the console and you're still not seeing the test crash
   after five minutes,
   [enable debug logging](https://firebase.google.com/docs/crashlytics/android/test-implementation#enable-debug-logging)
   to see if your app is sending crash reports.

<br />


And that's it! Crashlytics is now monitoring your app for crashes, and you
can view and investigate crash reports and statistics in the
Crashlytics dashboard.

## Next steps

-
  ***(Recommended)*** Get help debugging crashes caused by native memory errors by
  [collecting
  GWP-ASan reports](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports#gwp-asan).
  These memory-related errors can be associated with memory corruption within
  your app, which is the leading cause of app security vulnerabilities.
  To take advantage of this debugging feature, make sure your app has
  [GWP-ASan explicitly enabled](https://developer.android.com/ndk/guides/gwp-asan#opt-in)
  and uses the latest Crashlytics SDK for NDK (v18.3.6+ or
  Firebase BoM v31.3.0+).

- [Customize your crash report setup](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports#metadata-in-ndk-reports)
  by adding opt-in reporting, logs, keys, and tracking of non-fatal errors.

-
  [Integrate with Google Play](https://firebase.google.com/docs/crashlytics/integrate-with-google-play) so that
  you can filter your Android app's crash reports by Google Play track directly in the
  Crashlytics dashboard. This allows you to better focus your dashboard on specific builds.

## Troubleshooting

If you're seeing different stack traces in the Firebase console and in
the logcat, refer to the
[Troubleshooting guide](https://firebase.google.com/docs/crashlytics/troubleshooting#mismatch-report).

<br />

*** ** * ** ***

## Alternative options for uploading symbols

The main workflow on this page above is applicable for standard Gradle builds.
However, some apps use a different configuration or tooling (for example a build
process other than Gradle). In these situations, the following options might be
helpful for successfully uploading symbols.

### **Option**: Upload symbols for library modules and external dependencies

This option can be helpful in the following situations:

- If you use a customized NDK build process within Gradle
- If your native libraries are built in a library/feature module or provided by a third-party
- If the [automatic symbol uploading task](https://firebase.google.com/docs/crashlytics/android/get-started-ndk#set-up-automatic-native-symbols-upload) is failing or you're seeing unsymbolicated crashes in the dashboard

<br />

View instructions for this option

<br />

The standard Crashlytics symbol upload task assumes that you're building
your native libraries as part of your app module's Gradle build, using standard
NDK build tools such as CMake.

However, if you're using a customized NDK build process within Gradle, or your
native libraries are built in a library/feature module or provided by a
third-party, you may need to explicitly specify the path to your unstripped
libraries. To accomplish this, you can add the `unstrippedNativeLibsDir`
property within the Crashlytics extension in your Gradle build file.

1. Make sure that you've completed the following initial tasks from the main
   workflow earlier on this page:

   1. [Enabled Crashlytics in the Firebase console.](https://firebase.google.com/docs/crashlytics/android/get-started-ndk#enable-in-console)

   2. Added the
      [Crashlytics SDK for NDK](https://firebase.google.com/docs/crashlytics/android/get-started-ndk#add-sdk) and the
      [Crashlytics Gradle plugin](https://firebase.google.com/docs/crashlytics/android/get-started-ndk#add-plugin).

   3. [Added the Crashlytics extension to your build.](https://firebase.google.com/docs/crashlytics/android/get-started-ndk#add-extension)

   4. [Set up automatic uploading of native symbols.](https://firebase.google.com/docs/crashlytics/android/get-started-ndk#set-up-automatic-native-symbols-upload)

2. So that the automatic symbol uploading task can find your symbol
   information, add the following to your **module (app-level)** Gradle file
   (usually `<project>/<app-module>/build.gradle.kts` or
   `<project>/<app-module>/build.gradle`):

   ### Kotlin

   ```kotlin
   import com.google.firebase.crashlytics.buildtools.gradle.CrashlyticsExtension

   // ...

   android {
       // ...
       buildTypes {
           release {
               configure<CrashlyticsExtension> {
                   nativeSymbolUploadEnabled = true
                   unstrippedNativeLibsDir = file("PATH/TO/UNSTRIPPED/DIRECTORY")
               }
           }
       }
   }
   ```

   ### Groovy

   ```groovy
   // ...

   android {
       // ...
       buildTypes {
           release {
               firebaseCrashlytics {
                   nativeSymbolUploadEnabled true
                   unstrippedNativeLibsDir file("PATH/TO/UNSTRIPPED/DIRECTORY")
               }
           }
       }
   }
   ```

   The Crashlytics plugin will recursively search the specified directory
   for native libraries with a `.so` extension. Crashlytics then extracts
   debugging symbols from all such libraries and uploads them to the Firebase
   servers.

   Here's what you can specify in the `unstrippedNativeLibsDir` property:
   - Any argument allowable for
     [`org.gradle.api.Project#files(Object...)`](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html#files-java.lang.Object...-),
     including: `java.lang.String`,
     `java.io.File`, or
     `org.gradle.api.file.FileCollection`

   - Multiple directories for a single build flavor by providing a list or
     `FileCollection` instance

   - *(Starting with Crashlytics Gradle plugin v3.0.0)* Accumulate multiple
     directories in individual products and build flavors.


   View an example with multiple directories

   ```kotlin
   buildTypes {
     release {
       configure<CrashlyticsExtension> {
         nativeSymbolUploadEnabled = true
         unstrippedNativeLibsDir = file("MY/NATIVE/LIBS")
       }
     }
     productFlavors {
       flavorDimensions += "feature"
       create("basic") {
         dimension = "feature"
         // ...
       }
       create("featureX") {
         dimension = "feature"
         configure<CrashlyticsExtension> {
           unstrippedNativeLibsDir = file("MY/FEATURE_X/LIBS")
         }
       }
     }
   }
   ```


   The `uploadCrashlyticsSymbolFilesBasicRelease` task
   will only upload the symbols in
   `MY/NATIVE/LIBS`,
   but `uploadCrashlyticsSymbolFilesFeatureXRelease`
   will upload symbols in both
   `MY/NATIVE/LIBS` and
   `MY/FEATURE_X/LIBS`.
3. Finally, [force a test crash](https://firebase.google.com/docs/crashlytics/android/get-started-ndk#force-test-crash) to finish setting up
   Crashlytics and to see initial data in the Crashlytics dashboard of
   the Firebase console.

<br />

<br />

### **Option**: Upload symbols for non-Gradle builds or inaccessible unstripped native libraries

This option can be helpful in the following situations:

- If you use a build process other than Gradle

- If your unstripped native libraries are provided to you in some way that
  they're not accessible during Gradle builds

<br />

View instructions for this option

<br />

This option requires that you run a Firebase CLI command when you create a
release build or any build for which you want to see symbolicated stack traces
in the Firebase console.

1. Make sure that you've completed the following initial tasks from the main
   workflow earlier on this page:

   1. [Enabled Crashlytics in the Firebase console.](https://firebase.google.com/docs/crashlytics/android/get-started-ndk#enable-in-console%7D)

   2. Added the
      [Crashlytics SDK for NDK](https://firebase.google.com/docs/crashlytics/android/get-started-ndk#add-sdk) and the
      [Crashlytics Gradle plugin](https://firebase.google.com/docs/crashlytics/android/get-started-ndk#add-plugin).

   Note that with this option, you don't need to add the `firebaseCrashlytics`
   extension or set up automatic symbol uploading because you'll instead use
   the Firebase CLI (next steps below) to generate and upload your symbol
   files.
2. Set up your environment and project for symbol uploading:

   1. Follow the instructions to [install the Firebase CLI](https://firebase.google.com/docs/cli).

      If you've already installed the CLI, make sure to
      [update to its latest version](https://firebase.google.com/docs/cli#update-cli).

      > [!NOTE]
      > **Note:** You can also run Firebase CLI commands in Cloud Shell. [Cloud Shell](https://firebase.google.com/docs/cloud-shell) is a browser-based, pre-authenticated command-line environment, accessible from the Firebase console, and comes with the Firebase CLI pre-installed. This makes it a convenient option for getting started quickly, provided you add your project files to the Cloud Shell environment.

   2. *(only for apps using Android API level 30+)* Update your app's
      `AndroidManifest.xml` template to disable Pointer Tagging:

      1. Check the box for **Android Player Settings \> Publishing Settings \>
         Build \> Custom Main Manifest**.

      2. Open the manifest template located at
         `Assets/Plugins/Android/AndroidManifest.xml`.

      3. Add the following attribute to the application tag:
         `<application android:allowNativeHeapPointerTagging="false" ... />`

3. Build your project.

4. Upload your symbols information.

   > [!NOTE]
   > **Note:** Complete this step to get started. Then, in the future, complete this step each time that you create a release build or any build for which you want to see symbolicated stack traces in the Firebase console.

   Once your build has finished, generate a Crashlytics-compatible symbol
   file and upload it to Firebase servers by running the following
   Firebase CLI command:

   ```
   firebase crashlytics:symbols:upload --app=FIREBASE_APP_ID PATH/TO/SYMBOLS
   ```
   - <var translate="no">FIREBASE_APP_ID</var>: Your Firebase Android App ID (not your
     package name)  

     Example Firebase Android App ID: `1:567383003300:android:17104a2ced0c9b9b`

     <br />

     Need to find your Firebase App ID?

     <br />

     > Here are two ways to find your Firebase App ID:
     > - In your `google-services.json` file, your App ID is the
     >   `mobilesdk_app_id` value; or
     >
     > - In the Firebase console, go to your
     >   [*Project settings*](https://console.firebase.google.com/project/_/settings/general/).
     >   Go to the *Your apps* card, then click the intended Firebase App
     >   to find its App ID.

     <br />

     <br />

   - <var translate="no">PATH/TO/SYMBOLS</var>: The path to the symbol file generated by the
     CLI

     - Exported to an Android Studio project ---
       <var translate="no">PATH/TO/SYMBOLS</var> can be any directory. The Firebase CLI
       will recursively search the specified directory for native libraries
       with a `.so` extension.

     - Built the APK directly from within Unity ---
       <var translate="no">PATH/TO/SYMBOLS</var> is the path of the zipped symbol file
       generated in the project root directory when your build finished
       (for example:
       `myproject/myapp-1.0-v100.symbols.zip`).

   View advanced options for using the
   Firebase CLI command for symbol file generation and upload

   | **Flag** | **Description** |
   |---|---|
   | `--generator=csym` | Uses the legacy cSYM symbol file generator instead of the default Breakpad generator Not recommended for use. We recommend using the default Breakpad symbol file generator. |
   | `--generator=breakpad` | Uses the Breakpad symbol file generator Note that the default for symbol file generation is Breakpad. Only use this flag if you've added `symbolGenerator { csym() }` in your build configuration and you want to override it to use Breakpad instead. |
   | `--dry-run` | Generates the symbol files but does not upload them This flag is useful if you want to inspect the content of the files that are sent. |
   | `--debug` | Provides additional debugging information |

5. Finally, [force a test crash](https://firebase.google.com/docs/crashlytics/android/get-started-ndk#force-test-crash) to finish setting up
   Crashlytics and to see initial data in the Crashlytics dashboard of
   the Firebase console.

   After you build your app as part of forcing a crash, make sure to run the
   Firebase CLI `crashlytics:symbols:upload` command to upload your symbol
   file.

<br />

<br />

<br />

*** ** * ** ***