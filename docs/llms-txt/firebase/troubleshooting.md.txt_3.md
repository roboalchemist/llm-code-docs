# Source: https://firebase.google.com/docs/crashlytics/troubleshooting.md.txt

This page provides troubleshooting help and answers to frequently-asked
questions about using Crashlytics. If you
can't find what you're looking for or need additional help, contact
[Firebase support](https://support.google.com/firebase/contact/support).

On this page, you can find information about the following types of topics:

- [General troubleshooting](https://firebase.google.com/docs/crashlytics/troubleshooting#troubleshooting-faq), including questions about
  display of data or working with data in the Firebase console and questions
  about regressed issues.

- [Platform-specific support](https://firebase.google.com/docs/crashlytics/troubleshooting#platform-support), including questions specific
  to [Apple platforms](https://firebase.google.com/docs/crashlytics/troubleshooting#platform-support-ios),
  [Android](https://firebase.google.com/docs/crashlytics/troubleshooting#platform-support-android), and
  [Unity](https://firebase.google.com/docs/crashlytics/troubleshooting#platform-support-unity).

- [Integrations support](https://firebase.google.com/docs/crashlytics/troubleshooting#integrations), including questions about
  BigQuery.

## General troubleshooting/FAQ

<br />

#### Seeing different formats
(and sometimes "variants") for some issues in the *Issues* table

<br />

You might notice two different formats for issues listed in your *Issues* table
in the Firebase console. And you might also notice a feature called
"variants" within some of your issues. Here's why!

In early 2023, we rolled out an improved analysis engine for grouping events as
well as an updated design and some advanced features for new issues (like
variants!). Check out our recent
[blog post](https://firebase.blog/posts/2023/05/crashlytics-event-grouping-algorithm-update)
for all the details, but you can read below for the highlights.

Crashlytics analyzes all the events from your app (like crashes, non-fatals,
and ANRs) and creates groups of events called ***issues*** --- all events in an
issue have a common point of failure.

To group events into these issues, the improved analysis engine now looks at
many aspects of the event, including the frames in the stack trace, the
exception message, the error code, and other platform or error type
characteristics.

However, within this group of events, the stack traces leading to the failure
might be different. A different stack trace could mean a different root cause.
To represent this possible difference within an issue, we now create
***variants*** within issues - each variant is a sub-group of events in an issue
that have the same failure point *and* a similar stack trace. *With variants,
you can debug the most common stack traces within an issue and determine if
different root causes are leading to the failure.*

Here's what you'll experience with these improvements:

- **Revamped metadata displayed within the issue row**   

  *It's now easier to understand and triage issues in your app.*

- **Fewer duplicate issues**   

  *A line number change doesn't result in a new issue.*

- **Easier debugging of complex issues with various root causes**   

  *Use variants to debug the most common stack traces within an issue.*

- **More meaningful alerts and signals**   

  *A new issue actually represents a new bug.*

- **More powerful search**   

  *Each issue contains more searchable metadata,
  like exception type and package name.*

Here's how these improvements are rolling out:

- When we get new events from your app, we'll check if they match to an existing
  issue.

- If there's no match, we'll automatically apply our smarter event-grouping
  algorithm to the event and create a new issue with the revamped metadata
  design.

This is the first big update that we're making to our event grouping. If you
have feedback or encounter any issues, let us know by
[filing a report.]()

<br />

<br />

<br />

#### Not seeing breadcrumb logs

<br />

If you're not seeing breadcrumb logs
([iOS+](https://firebase.google.com/docs/crashlytics/ios/customize-crash-reports#get-breadcrumb-logs) \|
[Android](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports#get-breadcrumb-logs) \|
[Flutter](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports#get-breadcrumb-logs) \|
[Unity](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports#get-breadcrumb-logs)),
we recommend checking your app's configuration for Google Analytics.
Make sure you meet the following requirements:

- You've
  [enabled Google Analytics](https://support.google.com/firebase/answer/9289399#linkga)
  in your Firebase project.

- You've enabled *Data sharing* for Google Analytics. Learn more about
  this setting in
  [Manage your Analytics data sharing settings](https://support.google.com/firebase/answer/6383877)

- You've added to your app the Firebase SDK for Google Analytics:
  [iOS+](https://firebase.google.com/docs/crashlytics/ios/get-started#add-sdk) \|
  [Android](https://firebase.google.com/docs/crashlytics/android/get-started#add-sdk) \|
  [Flutter](https://firebase.google.com/docs/crashlytics/flutter/get-started#add-sdk) \|
  [Unity](https://firebase.google.com/docs/crashlytics/unity/get-started#add-sdk).

  This SDK must be added *in addition* to the Crashlytics SDK.

- You're using the latest Firebase SDK versions for all the products that you
  use in your app
  ([iOS+](https://firebase.google.com/support/release-notes/ios) \|
  [Android](https://firebase.google.com/support/release-notes/android) \|
  [Flutter](https://github.com/firebase/flutterfire/blob/master/CHANGELOG.md) \|
  [Unity](https://firebase.google.com/support/release-notes/unity)).

  For Apple platforms and Android apps, especially check that you're using
  *at minimum* the following version of the
  Firebase SDK for Google Analytics:
  **iOS+** --- v6.3.1+ (v8.9.0+ for macOS and tvOS) \|
  **Android** --- v17.2.3+ (BoM v24.7.1+).

<br />

<br />

<br />

#### Not seeing velocity alerts

<br />

If you're not seeing velocity alerts, make sure that you're using the


<br />

<br />

<br />

#### Not seeing crash-free metrics (or seeing unreliable metrics)

<br />

If you're not seeing crash-free metrics (like crash-free users and sessions) or
seeing unreliable metrics, check the following:

- Make sure that you're using the

- Make sure that your data collection settings aren't impacting the quality of
  your crash-free metrics:


  - If you
    [enable opt-in reporting](https://firebase.google.com/docs/crashlytics/customize-crash-reports#enable-reporting)
    by disabling automatic crash reporting, crash information can only be sent
    to Crashlytics from users who have explicitly opted into data
    collection. Thus, the accuracy of crash-free metrics will be affected since
    Crashlytics only has crash information from these opted-in users (rather
    than *all* your users). This means that your crash-free metrics may be less
    reliable and less reflective of the overall stability of your app.

  - If you have automatic data collection disabled, you can use
    `sendUnsentReports` to send on-device cached reports to Crashlytics.
    Using this method will send *crash* data to Crashlytics, but not
    *sessions* data which causes the console charts to show low or zero values
    for crash-free metrics.

<br />

<br />

<br />

#### How are crash-free users calculated?

<br />

See [Understand crash-free metrics](https://firebase.google.com/docs/crashlytics/crash-free-metrics).

<br />

<br />

<br />

#### Who can view, write, and delete notes on an issue?

<br />

Notes allow project members to comment on specific issues with questions, status
updates, etc.

When a project member posts a note, it's labeled with the email of their Google
Account. This email address is visible, along with the note, to all project
members with access to view the note.

**The following describes the access required to view, write, and delete
notes:**

- Project members with any of the following roles can view and delete existing
  notes and write new notes on an issue.

  - Project [Owner or Editor](https://firebase.google.com/docs/projects/iam/roles-basic), [Firebase Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products), [Quality Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-category#quality_roles), or [Crashlytics Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-product#crashlytics)
- Project members with any of the following roles can view the notes posted on
  an issue, but they cannot delete or write a note.

  - Project [Viewer](https://firebase.google.com/docs/projects/iam/roles-basic), [Firebase Viewer](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products), [Quality Viewer](https://firebase.google.com/docs/projects/iam/roles-predefined-category#quality_roles), or [Crashlytics Viewer](https://firebase.google.com/docs/projects/iam/roles-predefined-product#crashlytics)

<br />

<br />

<br />

#### What is a regressed
issue?

<br />

An issue has had a regression when you've previously closed the issue but
Crashlytics gets a new report that the issue has re-occurred.
Crashlytics automatically re-opens these regressed issues so that you can
address them as appropriate for your app.

Here's an example scenario that explains how Crashlytics categorizes an
issue as a regression:

1. For the first time ever, Crashlytics gets a crash report about Crash "A". Crashlytics opens a corresponding issue for that crash (Issue "A").
2. You fix this bug quickly, close Issue "A", and then release a new version of your app.
3. Crashlytics gets another report about Issue "A" after you've closed the issue.
   - If the report is from an app version that Crashlytics *knew about* when you closed the issue (meaning that the version had sent a crash report for *any* crash at all), then Crashlytics won't consider the issue as regressed. The issue will remain closed.
   - If the report is from an app version that Crashlytics *did **not**
     know about* when you closed the issue (meaning that the version had *never* sent *any* crash report for any crash at all), then Crashlytics considers the issue regressed and will re-open the issue.

> [!NOTE]
> **Note:** Prior to February 2022, Crashlytics categorized an issue as a regression when that issue re-occurred in *any* app version, even for app versions that we knew about when you closed the issue. This resulted in Crashlytics sometimes inaccurately identifying regressions. We now use the convention described above.

When an issue regresses, we send a regression detection alert and add a
regression signal to the issue to let you know that Crashlytics has
re-opened the issue. If you don't want an issue to re-open due to our
regression algorithm, "mute" the issue instead of closing it.

<br />

<br />

<br />

#### Why am I seeing regressed
issues for older app versions?

<br />

If a report is from an old app version that had never sent any crash reports at
all when you closed the issue, then Crashlytics considers the issue
regressed and will re-open the issue.

This situation can happen in the following situation: You've fixed a bug and
released a new version of your app, but you still have users on earlier versions
without the bug fix. If, by chance, one of those earlier versions had *never*
sent any crash reports at all when you closed the issue, and those users start
encountering the bug, then those crash reports would trigger a regressed issue.

If you don't want an issue to re-open due to our regression algorithm, "mute"
the issue instead of closing it.

> [!NOTE]
> **Note:** Prior to February 2022, Crashlytics categorized an issue as a regression when that issue re-occurred in any app version, even for app versions that we knew about when you closed the issue. This resulted in Crashlytics sometimes inaccurately identifying regressions. We now use the convention described above.   
>
> If you see a lot of misidentified regressions from before February 2022, you can re-close them to prevent them from re-opening.

<br />

<br />

<br />

*** ** * ** ***

## Platform-specific support

The following sections provide support for platform-specific troubleshooting
and FAQ:
**[iOS+](https://firebase.google.com/docs/crashlytics/troubleshooting#platform-support-ios) \|
[Android](https://firebase.google.com/docs/crashlytics/troubleshooting#platform-support-android) \|
[Unity](https://firebase.google.com/docs/crashlytics/troubleshooting#platform-support-unity).**

### Apple platforms support

<br />

#### dSYMs are missing/not uploading

<br />

To upload your project's dSYMs and get verbose output, check the following:

1. Make sure your project's build phase contains the Crashlytics run script,
   which allows Xcode to upload your project's dSYMs at build time (read
   [Initializing Crashlytics](https://firebase.google.com/docs/crashlytics/ios/get-started#initialize-crashlytics)
   for instructions on adding the script). After updating your project,
   [force a crash](https://firebase.google.com/docs/crashlytics/ios/test-implementation) and confirm that
   the crash appears in the Crashlytics dashboard.

2. If you see a "Missing dSYM" alert in the Firebase console, check Xcode to
   make sure it's
   [properly producing dSYMs](https://firebase.google.com/docs/crashlytics/ios/get-deobfuscated-reports#check-xcode)
   for the build.

3. If Xcode is properly producing dSYMs, and you're still seeing missing dSYMs,
   it's likely the run script tool is getting stuck while uploading the dSYMs.
   In this case, try each of the following:

   - Make sure you're using the latest version of Crashlytics.

   - Upload the missing dSYM files manually:

     - **Option 1:** Use the console-based "Drag and Drop" option in the [*dSYMs* tab](https://console.firebase.google.com/project/_/crashlytics) to upload a zip archive containing the missing dSYM files.
     - **Option 2:** Use the [`upload-symbols` script](https://firebase.google.com/docs/crashlytics/ios/get-deobfuscated-reports#upload-dsyms) to upload the missing dSYM files, for the provided UUIDs in the *dSYMs* tab.
4. If you continue to see missing dSYMs, or uploads are still unsuccessful,
   contact [Firebase Support](https://firebase.google.com/support/troubleshooter/crashlytics/dsym)
   and be sure to include your logs.

<br />

<br />

<br />

#### Crashes are poorly
symbolicated

<br />

If your stack traces seem to be poorly symbolicated, check the following:

- If frames from your app's library lack references to your app's code, make
  sure that `-fomit-frame-pointer` is not set as a
  compilation flag.

- If you see several `(Missing)` frames for your app's library, check if there
  are optional dSYMs listed as missing (for the affected app version) in the
  [Crashlytics *dSYMs* tab](https://console.firebase.google.com/project/_/crashlytics)
  of the Firebase console. If so, follow the "Missing dSYM alert"
  troubleshooting step in the
  [dSYMs are missing/not uploading FAQ](https://firebase.google.com/docs/crashlytics/troubleshooting#ios-locate-dsyms)
  on this page. Note that uploading these dSYMs won't symbolicate crashes that
  have *already* occurred, but this will help ensure symbolication for
  *future* crashes.

<br />

<br />

<br />

#### Can I use Crashlytics for macOS or tvOS?

<br />

Yes, you can implement Crashlytics in macOS and tvOS projects. Make sure to
include v8.9.0+ of the Firebase SDK for Google Analytics so that crashes
will have access to metrics collected by Google Analytics (crash-free
users, latest release, velocity alerts, and breadcrumb logs).

<br />

<br />

<br />

#### Can I use Crashlytics in a Firebase
project with multiple apps on different Apple platforms?

<br />

You can now report crashes for multiple apps in a single Firebase project,
even when the apps are built for different Apple platforms (for example,
iOS, tvOS, and Mac Catalyst). Previously, you needed to separate the apps into
individual Firebase projects if they contained the same bundle ID.

<br />

<br />

<br />

*** ** * ** ***

### Android support

<br />

#### Why are ANRs only
reported for Android 11+?

<br />

Crashlytics supports ANR reporting for Android apps from devices that run
Android 11 and higher. The underlying API that we use to collect ANRs
([getHistoricalProcessExitReasons](https://developer.android.com/reference/kotlin/android/app/ActivityManager#gethistoricalprocessexitreasons))
is more reliable than SIGQUIT or watchdog-based approaches. This API is
available only on Android 11+ devices.

<br />

<br />

<br />

#### Why are some ANRs missing
their `BuildId`s?

<br />

If some of your ANRs are missing their `BuildId`s, troubleshoot as follows:

- **Make sure that you're using an up-to-date Crashlytics Android SDK and
  Crashlytics Gradle plugin version.**

  If you're missing `BuildId`s for Android 11 and some Android 12 ANRs, then
  it's likely that you're using an out-of-date SDK, Gradle plugin, or both.
  To properly collect `BuildId`s for these ANRs, you need to use the following
  versions:
  - Crashlytics Android SDK v18.3.5+ (Firebase BoM v31.2.2+)
  - Crashlytics Gradle plugin v2.9.4+
- **Check if you're using a non-standard location for your shared libraries.**

  If you're only missing`BuildId`s for your app's shared libraries, it's likely
  that you're not using the standard, default location for shared libraries. If
  this is the case, then Crashlytics might not be able to locate the
  associated `BuildId`s. We recommend that you consider using the standard
  location for shared libraries.
- **Make sure that you're not stripping `BuildId`s during the build process.**

  Note that the following troubleshooting tips apply to both ANRs and native
  crashes.
  - Check if the `BuildId`s exist by running `readelf -n` on your binaries. If
    the `BuildId`s are absent, then add `-Wl,--build-id` to the flags for your
    build system.

  - Check that you're not unintentionally stripping the `BuildId`s in an effort
    to reduce your APK size.

  - If you keep stripped and unstripped versions of a library, make sure to
    point to the correct version in your code.

<br />

<br />

<br />

#### Differences
between ANR reports in the Crashlytics dashboard and
Google Play Console

<br />

There can be a mismatch between the count of ANRs between Google Play and
Crashlytics. This is expected due to the difference in the mechanism of
collecting and reporting ANR data. Crashlytics reports ANRs when the app
next starts up, whereas Android Vitals sends ANR data after the ANR occurs.

Additionally, Crashlytics only displays ANRs that occur on devices running
Android 11+, compared to Google Play which displays ANRs from devices with
Google Play services and data collection consent accepted.

<br />

<br />

<br />

#### Why do I see crashes
from `.kt` files labeled as `.java` issues?

<br />

When an app uses an obfuscator that doesn't expose the file extension,
Crashlytics generates each issue with a `.java` file extension by default.

So that Crashlytics can generate issues with the correct file extension,
make sure your app uses the following setup:

- Uses Android Gradle 4.2.0 or higher
- Uses R8 with obfuscation turned on. To update your app to R8, follow this [documentation](https://developer.android.com/studio/build/shrink-code).

Note that after updating to the setup described above, you might start seeing
new `.kt` issues that are duplicates of existing `.java` issues. See the
[FAQ](https://firebase.google.com/docs/crashlytics/troubleshooting#duplicate-kt-and-java-issues) to learn more about that circumstance.

<br />

<br />

<br />

#### Why do I see
`.kt` issues that are duplicates of existing
`.java` issues?

<br />

Starting in mid-December 2021, Crashlytics improved support for applications
that use Kotlin.

Until recently, the available obfuscators did not expose the file extension, so
Crashlytics generated each issue with a `.java` file extension by default.
However, as of Android Gradle 4.2.0, R8 supports file extensions.

With this update, Crashlytics can now determine if each class used within
the app is written in Kotlin and include the correct filename in the issue
signature. Crashes are now correctly attributed to `.kt` files (as appropriate)
if your app has the following setup:

- Your app uses Android Gradle 4.2.0 or higher.
- Your app uses R8 with obfuscation turned on.

Since new crashes now include the correct file extension in their issue
signatures, you might see new `.kt` issues that are actually just duplicates of
existing `.java`-labeled issues. In the Firebase console, we try to identify
and communicate to you if a new `.kt` issue is a possible duplicate of an
existing `.java`-labeled issue.

<br />

<br />

<br />

#### Not getting crashes with
Dexguard

<br />

If you see the following exception, it's likely you're using a version of
DexGuard that's incompatible with the Firebase Crashlytics SDK:

```
java.lang.IllegalArgumentException: Transport backend 'cct' is not registered
```

This exception does not crash your app but prevents it from sending crash
reports. To fix this:

1. Make sure you're using the latest DexGuard 8.x release. The latest version
   contains rules that are required by the Firebase Crashlytics SDK.

2. If you don't want to change your DexGuard version, try adding the following
   line to your obfuscation rules (in your DexGuard config file):

   ```
   -keepresourcexmlelements manifest/application/service/meta-data@value=cct
   ```

<br />

<br />

<br />

#### How to upgrade to Crashlytics Gradle plugin v3?

<br />

The latest release of the Crashlytics Gradle plugin is a major
version (v3.0.0) and modernizes the SDK by dropping support for lower versions
of Gradle and the Android Gradle plugin. Additionally, the changes in this
release resolve issues with AGP v8.1+ and improve support for native apps and
customized builds.

#### Minimum requirements

The Crashlytics Gradle plugin v3 has the following minimum requirements:

- Android Gradle plugin 8.1+  

  Upgrade this plugin using the
  [Android Gradle plugin Upgrade Assistant](https://developer.android.com/build/agp-upgrade-assistant)
  on the latest version of Android Studio.

- Firebase's `google-services` Gradle plugin 4.4.1+  

  Upgrade this plugin by specifying the latest version in your project's Gradle
  build file, like so:

### Kotlin

```kotlin
plugins {
  id("com.android.application") version "8.1.4" apply false
  id("com.google.gms.google-services") version "4.4.4" apply false
  ...
}
```

### Groovy

```groovy
plugins {
  id 'com.android.application' version '8.1.4' apply false
  id 'com.google.gms.google-services' version '4.4.4' apply false
  ...
}
```

#### Changes to the Crashlytics extension

With v3 of the Crashlytics Gradle plugin, the Crashlytics extension has
the following breaking changes:

- Removed the extension from the `defaultConfig` android block. Instead, you
  should configure each variant.

- Removed the deprecated field `mappingFile`. Instead, the merged mapping file
  is now provided automatically.

- Removed the deprecated field `strippedNativeLibsDir`. Instead, you should use
  `unstrippedNativeLibsDir` for all native libs.

- Changed the field `unstrippedNativeLibsDir` to be cumulative.


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
- Replaced the closure field `symbolGenerator` with two new top level fields:

  - `symbolGeneratorType`, a String of either `"breakpad"` (default) or `"csym"`.
  - `breakpadBinary`, a File of a local `dump_syms` binary override.

##### Example for how to upgrade the extension

### Kotlin

|---|---|
| **Before** | ```kotlin buildTypes { release { configure<CrashlyticsExtension> { // ... symbolGenerator( closureOf<SymbolGenerator> { symbolGeneratorType = "breakpad" breakpadBinary = file("/PATH/TO/BREAKPAD/DUMP_SYMS") } ) } } } ``` |
| **Now in v3** | ```kotlin buildTypes { release { configure<CrashlyticsExtension> { // ... symbolGeneratorType = "breakpad" breakpadBinary = file("/PATH/TO/BREAKPAD/DUMP_SYMS") } } } ``` |

### Groovy

|---|---|
| **Before** | ```groovy buildTypes { release { firebaseCrashlytics { // ... symbolGenerator { breakpad { binary file("/PATH/TO/BREAKPAD/DUMP_SYMS") } } } } } ``` |
| **Now in v3** | ```groovy buildTypes { release { firebaseCrashlytics { // ... symbolGeneratorType "breakpad" breakpadBinary file("/PATH/TO/BREAKPAD/DUMP_SYMS") } } } ``` |

<br />

<br />

#### Android-NDK specific support

<br />

##### Differences
between NDK stack traces in Crashlytics dashboard and logcat

<br />

LLVM and GNU toolchains have distinct defaults and treatments for the read-only
segment of your app's binaries, which may generate inconsistent stack traces
in the Firebase console. To mitigate this, add the following linker flags
to your build process:

- If you're using the `lld` linker from the LLVM toolchain, add:

      -Wl,--no-rosegment

- If you're using the `ld.gold` linker from the GNU toolchain, add:

      -Wl,--rosegment

If you're still seeing stack trace inconsistencies (or if neither flag is
pertinent to your toolchain), try adding the following to your build process
instead:

    -fno-omit-frame-pointer

<br />

<br />

<br />

##### How do I use
my own Breakpad symbol file generator binary for NDK?

<br />

The Crashlytics plugin bundles a
[customized Breakpad symbol file generator](https://firebase.google.com/docs/crashlytics/ndk-reports#breakpad-symbol-file).
If you prefer to use your own binary for generating Breakpad symbol files (for
example, if you prefer to build all native executables in your build chain from
source), use the optional `symbolGeneratorBinary` extension property to specify
the path to the executable.

> [!NOTE]
> **Note:** The Linux version of the Breakpad symbol file generator is required for Android binaries.

**You can specify the path to the Breakpad symbol file generator binary in one
of two ways:**

- **Option 1** : Specify the path via the `firebaseCrashlytics`
  extension in your `build.gradle` file

  Add the following to your app-level `build.gradle.kts` file:

  ### Gradle plugin v3.0.0+

  ```kotlin
  android {
    buildTypes {
      release {
        configure<CrashlyticsExtension> {
          nativeSymbolUploadEnabled = true
          // Add these optional fields to specify the path to the executable
          symbolGeneratorType = "breakpad"
          breakpadBinary = file("/PATH/TO/BREAKPAD/DUMP_SYMS")
        }
      }
    }
  }
  ```

  ### lower plugin versions

  ```groovy
  android {
    // ...
    buildTypes {
      // ...
      release {
        // ...
        firebaseCrashlytics {
          // existing; required for either symbol file generator
          nativeSymbolUploadEnabled true
          // Add this optional new block to specify the path to the executable
          symbolGenerator {
            breakpad {
              binary file("/PATH/TO/BREAKPAD/DUMP_SYMS")
            }
          }
        }
     }
  }
  ```
- **Option 2**: Specify the path via a property line in your Gradle
  properties file

  You can use the `com.google.firebase.crashlytics.breakpadBinary`
  property to specify the path to the executable.

  You can manually update your Gradle properties file or update the file
  via the command line. For example, to specify the path via the command
  line, use a command like the following:

  ```
  ./gradlew -Pcom.google.firebase.crashlytics.symbolGenerator=breakpad \
    -Pcom.google.firebase.crashlytics.breakpadBinary=/PATH/TO/BREAKPAD/DUMP_SYMS \
    app:assembleRelease app:uploadCrashlyticsSymbolFileRelease
  ```

<br />

<br />

<br />

##### Does Crashlytics support armeabi?

<br />

The Firebase Crashlytics NDK does not support ARMv5 (armeabi).
Support for this ABI was removed as of NDK r17.

<br />

<br />

<br />

*** ** * ** ***

### Unity support

<br />

#### Seeing unsymbolicated
stack traces for Android apps in the Crashlytics dashboard

<br />

If you're using Unity [IL2CPP](https://docs.unity3d.com/Manual/IL2CPP.html)
and you're seeing unsymbolicated stack traces, then try the following:

1. Make sure that you're using v8.6.1 or higher of the Crashlytics Unity
   SDK.

2. Make sure that you're set up for and running the Firebase CLI
   `crashlytics:symbols:upload` command to generate and upload your symbol
   file.

   You need to run this CLI command each time that you create a release
   build or any build for which you want to see symbolicated stack traces in
   the Firebase console. Learn more in
   [Get readable crash reports](https://firebase.google.com/docs/crashlytics/unity/get-deobfuscated-reports).

<br />

<br />

<br />

#### Can Crashlytics be used
with apps that use IL2CPP?

<br />

Yes, Crashlytics can display symbolicated stack traces for your apps that
use IL2CPP. This capability is available for apps released on either Android or
Apple platforms. Here's what you need to do:

1. Make sure that you're using v8.6.0 or higher of the Crashlytics Unity
   SDK.

2. Complete the necessary tasks for your platform:

   - **For Apple platform apps**: No special actions are needed. For Apple
     platform apps, the Firebase Unity Editor plugin automatically configures
     your Xcode project to upload symbols.

   - **For Android apps** : Make sure that you're set up for and running the
     Firebase CLI `crashlytics:symbols:upload` command to generate and
     upload your symbol file.

     You need to run this CLI command each time that you create a release
     build or any build for which you want to see symbolicated stack traces in
     the Firebase console. Learn more in
     [Get readable crash reports](https://firebase.google.com/docs/crashlytics/unity/get-deobfuscated-reports).

<br />

<br />

#### Reporting uncaught exceptions as fatals

Crashlytics can report uncaught exceptions as fatals (starting with
[v10.4.0](https://firebase.google.com/support/release-notes/unity#version_1040_-_january_26_2023)
of the Unity SDK). The following FAQs help to explain the rationale and best
practices for using this feature.

<br />

##### Why should an app report uncaught exceptions as fatals?

<br />

By reporting uncaught exceptions as fatals, you get a more realistic indication
of what exceptions may result in the game being unplayable -- even if the app
continues to run.

Note that if you start reporting fatals, your crash-free users (CFU) percentage
will likely decrease, but the CFU metric will be more representative of the
end-users' experiences with your app.

> [!IMPORTANT]
> **Important:** Reporting uncaught exceptions as fatals does ***not*** affect your [Android Vitals](https://developer.android.com/topic/performance/vitals). The fatals reported in Crashlytics are only visible to you so that you can discover and fix issues in your apps and games.

<br />

<br />

<br />

##### Which exceptions will be
reported as fatals?

<br />

In order for Crashlytics to report an uncaught exception as fatal, both of
the following two conditions must be met:

- During initialization in your app, the
  [`ReportUncaughtExceptionsAsFatal` property must be set to `true`](https://firebase.google.com/docs/crashlytics/unity/get-started#initialize-crashlytics).

- Your app (or an included library) throws an exception that isn't caught. An
  exception that's created, *but not thrown*, is not considered uncaught.

<br />

<br />

<br />

##### After enabling reporting of uncaught exceptions as fatals, I now have many new fatals. How do I properly handle these exceptions?

<br />

When you start getting reports of your uncaught exceptions as fatals, here are
some options for handling these uncaught exceptions:

- [Consider how you can start catching and handling these uncaught exceptions.](https://firebase.google.com/docs/crashlytics/troubleshooting#catch-and-handle-thrown-exceptions)
- [Consider different options for logging exceptions to the Unity debug console and to Crashlytics.](https://firebase.google.com/docs/crashlytics/troubleshooting#log-exceptions-in-unity-or-crashlytics)

#### **Catch and handle thrown exceptions**

Exceptions are created and thrown to reflect
[unexpected or exceptional states](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/exceptions/#exceptions-overview).
Resolving the issues reflected by a thrown exception involves returning the
program to a known state (a process known as
[*exception handling*](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/exceptions/#exceptions-overview)).

It's best practice to catch and handle **all** foreseen exceptions unless the
program cannot be returned to a known state.

To control which sorts of exceptions are caught and handled by what code,
[wrap code that might generate an exception in a `try-catch` block](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/exceptions/exception-handling).
Make sure that the conditions in the `catch` statements are as narrow as
possible to handle the specific exceptions appropriately.

#### **Log exceptions in Unity or Crashlytics**

There are multiple ways to record exceptions in Unity or Crashlytics to help
debug the issue.

When using Crashlytics, here are the two most common and recommended
options:

- Option 1: Print in the Unity console, but don't report to Crashlytics,
  during development or troubleshooting

  - Print to the Unity console using `Debug.Log(exception)`, `Debug.LogWarning(exception)`, and `Debug.LogError(exception)` which print the contents of the exception to the Unity console and don't re-throw the exception.
- Option 2: Upload to Crashlytics for consolidated reporting in the
  Crashlytics dashboard for the following situations:

  - If an exception is worth logging to debug a possible subsequent Crashlytics event, then use `Crashlytics.Log(exception.ToString())`.
  - If an exception should still be reported to Crashlytics despite being caught and handled, then use `Crashlytics.LogException(exception)` to log it as a nonfatal event.

However, if you want to manually report a fatal event to Unity Cloud
Diagnostics, you can use `Debug.LogException`. This option prints the exception
to the Unity console like Option 1, but it *also throws the exception*
(whether or not it has been thrown or caught yet). It throws the error
nonlocally. This means that even a surrounding `Debug.LogException(exception)`
with `try-catch` blocks still results in an uncaught exception.

Therefore, call `Debug.LogException` if and only if you want to do ***all*** of
the following:

- To print the exception to the Unity console.
- To upload the exception to Crashlytics as a fatal event.
- To throw the exception, have it be treated as an *uncaught* exception, and have it be reported to Unity Cloud Diagnostics.

Note that if you want to print a caught exception to the Unity console ***and***
upload to Crashlytics as a nonfatal event, do the following instead:

    try
    {
        methodThatThrowsMyCustomExceptionType();
    }
    catch(MyCustomExceptionType exception)
    {
        // Print the exception to the Unity console at the error level.
        Debug.LogError(exception);
        // Upload the exception to Crashlytics as a non-fatal event.
        Crashlytics.LogException(exception); // not Debug.LogException
        //
        // Code that handles the exception
        //
    }

<br />

<br />

<br />

*** ** * ** ***

## Integrations support

<br />

#### App also uses the
Google Mobile Ads SDK but not getting crashes

<br />

If your project uses Crashlytics alongside the Google Mobile Ads SDK,
it's likely that the crash reporters are interfering when
registering exception handlers. To fix the issue, turn off crash reporting in
the Mobile Ads SDK by calling `disableSDKCrashReporting`.

<br />

<br />

<br />

#### Where is my BigQuery dataset located?

<br />

Firebase exports data to the dataset location you selected when you set up data
export to BigQuery.

- This location applies to both the Crashlytics dataset and the
  Firebase sessions dataset (if sessions data is enabled for export).

- This location is only applicable for the data exported into
  BigQuery, and it does not impact the location of data stored for
  use in the Crashlytics dashboard of the Firebase console or in
  Android Studio.

- After a dataset is created, its location can't be changed, but you can
  copy the dataset to a different location or manually move (recreate) the
  dataset in a different location. To learn more, see
  [Change the location for existing exports](https://firebase.google.com/docs/projects/bigquery-export#change-dataset-location).

<br />

<br />

<br />

#### Issues after upgrading to the new export infrastructure for BigQuery?

<br />

In mid-October 2024, Crashlytics launched a new infrastructure for *batch*
export of Crashlytics data into BigQuery.

**All Firebase projects have been automatically upgraded to the new batch export
infrastructure as of March 2, 2026.**

> [!NOTE]
> **Note:** This infrastructure upgrade only applies to Crashlytics *batch* crash exports and does *not* apply to sessions or streaming exports.

#### Important differences between the old export infrastructure and the new export infrastructure

- The new infrastructure supports Crashlytics dataset locations outside the
  United States.

  - Export enabled *before* mid-October 2024 *and* upgraded to the new export
    infrastructure --- You can now optionally
    [change the location for data export](https://firebase.google.com/docs/projects/bigquery-export#change-dataset-location).

  - Export enabled in mid-October 2024 or later --- You were prompted during
    setup to select a location for data export.

- The new infrastructure doesn't support backfills of data from *before* you
  enabled export.

  - The old infrastructure supported backfill up to 30 days prior to the date
    when you enabled export.

  - The new infrastructure supports
    [backfills](https://cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer)
    up to the past 30 days *or* for the most recent date when you enabled export
    to BigQuery (whichever is most recent).

- The new infrastructure names BigQuery batch tables using the
  identifiers set for your Firebase Apps in your Firebase project.

  - The old infrastructure wrote data to batch tables with names based on the
    bundle IDs or package names *in your app's binary*.

  - The new infrastructure writes data to batch tables with names based on the
    bundle IDs or package names
    *set for your registered Firebase Apps in your Firebase project*.

### If your legacy batch table name didn't match your Firebase App identifier

If your legacy batch table name did *not* match the bundle ID or package name
set for your registered Firebase App, implement one of these options to avoid
further disruptions to your exported batch data.

#### Understand how the export infrastructure uses identifiers to write data to BigQuery tables

Here's how the two export infrastructures write Crashlytics data to
BigQuery batch tables:

- **Legacy export infrastructure** : Wrote data to a table with a name that's
  based on the bundle ID or package name *in your app's binary*.

- **New export infrastructure** : Writes data to a table with a name that's
  based on the bundle ID or package name
  *set for your registered Firebase App in your Firebase project*.

Unfortunately, sometimes the bundle ID or package name *in your app's binary*
doesn't match the bundle ID or package name
*set for your registered Firebase App in your Firebase project*. This usually
happens if someone didn't enter the actual identifier during app registration.

#### What happens if this wasn't fixed before upgrading?

If the identifiers in these two locations don't match, then the following has
happened:

- Your Crashlytics data now writes to a *new* BigQuery batch table
  --- that is, a new table with a name based on the bundle ID or package name *set
  for your registered Firebase App in your Firebase project*.

- Any existing "legacy" table with a name based on the identifier
  *in your app's binary* no longer has data written to it.

#### Example scenarios of mismatched identifiers

Note that BigQuery batch table names are automatically appended with
`_IOS` or `_ANDROID` to indicate the platform of the app.

| Identifier(s) in your app's binary | Identifier(s) set for your Firebase App(s) | Legacy behavior | Behavior after upgrade to new export infrastructure | Solution |
|---|---|---|---|---|
| `foo` | `bar` | Writes to a *single* table named after the identifier in app's binary (`foo`) | Creates then writes to a *single* table named after the identifier set for Firebase App (`bar`) | Implement either Option 1 or 2 described below. |
| `foo` | `bar`, `qux`, etc. | Writes to a *single* table named after the identifier in app's binary (`foo`) | Creates\* then writes to *multiple* tables named after the identifiers set for Firebase Apps (`bar`, `qux`, etc.) | Implement Option 2 described below. |
| `foo`, `baz`, etc. | `bar` | Writes to *multiple* tables named after the multiple identifiers in app's binary (`foo`, `baz`, etc.) | Creates\*\* then writes every app's data to a *single* table named after the identifier set for Firebase App (`bar`) | None of the options can be implemented. You can still differentiate data from each app within the single table by using the app's `bundle_identifier` which is exported alongside the data. |

^\* *If the identifier in your app's binary matched one of the
identifiers set for a Firebase App, then the new export infrastructure didn't
create a new table for that identifier. Instead, it will continue writing
data for that specific app to it. All other apps will be written to new tables.*^

^\*\* *If one of the identifiers in your app's binary matched the
identifier set for the Firebase App, then the new export infrastructure didn't
create a new table. Instead, it will maintain that table and start writing
data for all apps to it.*^

#### Options to mitigate disruption

> [!IMPORTANT]
> **Important:** If you have any questions or don't feel comfortable implementing one of these options, then reach out to [Firebase
> Support](https://firebase.google.com/support/troubleshooter/contact).

- **OPTION 1** :  
  Use the new table created by the new export infrastructure.
  You'll copy data from your legacy table to the new table.

  1. In the Google Cloud console,
     [copy all the data](https://cloud.google.com/bigquery/docs/managing-tables#copy-table)
     from your legacy table to the new table that was created during the
     infrastructure upgrade.

  2. If you have any downstream dependencies that depend on your batch table,
     change them to use the new table.

  > [!NOTE]
  > **Note:** New data will *not* write to your legacy table. Any previously written data in the legacy table won't be deleted.

- **OPTION 2** :  
  Reconfigure to write to your legacy table again. You'll need
  to override some defaults in a BigQuery config to achieve this.

  1. In the Firebase console, find and take note of the Firebase App ID
     (for example, `1:1234567890:ios:321abc456def7890`) of the app with the
     mismatched batch table name and identifier:  

     Go to your
     [**Project settings**](https://console.firebase.google.com/project/_/settings/general/),
     then go the *Your apps* card to see all your Firebase Apps and
     their information.

  2. In the Google Cloud console, change the new "data transfer config" that
     was created by the infrastructure upgrade so that data will write to your
     legacy table:

     1. Go to
        **BigQuery** \> [**Data transfers**](https://console.cloud.google.com/projectselector2/bigquery/transfers?project=$%7BprojectId%7D&supportedpurview=project)
        to view your "data transfer config".

     2. Select the config that has the source
        `Firebase Crashlytics with Multi-Region Support`.

     3. Click **Edit** in the top-right corner.

     4. In the **Data source details** section, find a list for
        **gmp_app_id** and a list for **client_namespace**.

        In BigQuery, the Firebase App ID is called the `gmp_app_id`.
        By default, the `client_namespace` value in BigQuery is the
        corresponding unique bundle ID / package name of the app, but you'll
        be overriding this default configuration.

        BigQuery uses the `client_namespace` value for the name of
        the batch table that each linked Firebase App writes to.
     5. Find the **gmp_app_id** of the Firebase App for which you want to
        override default settings. Change its **client_namespace** value to
        the name of the table you want the Firebase App to write to instead
        (usually this is the name of the legacy table the app was writing to
        with the legacy export infrastructure).

        > [!NOTE]
        > **Note:** If you were previously writing to a single table and now you have multiple tables after upgrading, then you can use the *same* `client_namespace` for each applicable `gmp_app_id`. BigQuery will essentially merge all the tables and write all data for all the Firebase Apps to that one table.

     6. Save the config change.

  3. [Schedule a backfill](https://cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer)
     for the days that your legacy table is missing data.

  4. Once the backfill is done,
     [delete the new table](https://cloud.google.com/bigquery/docs/managing-tables#deleting_tables)
     that was automatically created by the new export infrastructure.

<br />

<br />