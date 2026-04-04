# Source: https://firebase.google.com/docs/crashlytics/android/get-deobfuscated-reports.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/crashlytics/ios/get-deobfuscated-reports) [Android](https://firebase.google.com/docs/crashlytics/android/get-deobfuscated-reports) [Flutter](https://firebase.google.com/docs/crashlytics/flutter/get-deobfuscated-reports) [Unity](https://firebase.google.com/docs/crashlytics/unity/get-deobfuscated-reports) |

<br />

The Crashlytics Gradle plugin can automatically detect when you obfuscate
your code. When your build generates a mapping file, the plugin uploads it
so the Crashlytics servers can use the file to render your app's
stack traces as unobfuscated and human-readable code.

## Required configuration when using R8, ProGuard, and DexGuard

Crashlytics can deobfuscate with any ProGuard-compatible mapping file, and
has additionally been tested with ProGuard, R8, and DexGuard.

If your app uses R8 with obfuscation turned on along with Android Gradle 4.2.0+,
Crashlytics will produce readable crash reports. Note that Crashlytics
recently improved support for apps that use both Kotlin and R8, which can lead
to some
[unexpected issue labeling](https://firebase.google.com/docs/crashlytics/troubleshooting#duplicate-kt-and-java-issues).

If your app uses the ProGuard config file, you need to preserve the information
Crashlytics requires for producing readable crash reports. Do this by adding
the following lines to your ProGuard or DexGuard config file:

```
-keepattributes SourceFile,LineNumberTable        # Keep file names and line numbers.
-keep public class * extends java.lang.Exception  # Optional: Keep custom exceptions.
```

To get help for questions or issues related to DexGuard, contact the
[Guardsquare support team](https://www.guardsquare.com/en/contact-us)
directly. For help with ProGuard, visit the
[Guardsquare Community forums](https://community.guardsquare.com/?utm_source=site&utm_medium=site-link&utm_campaign=firebase-install-community)
to get assistance from an expert.

## Keep obfuscated build variants

To prevent the Crashlytics Gradle plugin from uploading the mapping file for
variants that use obfuscation, set the
`firebaseCrashlytics.mappingFileUploadEnabled` Gradle extension property to
`false` in your **module (app-level)** Gradle file
(usually `<project>/<app-module>/build.gradle.kts` or
`<project>/<app-module>/build.gradle`). This can help speed up
build times for obfuscated builds, but note that resulting stack traces will
appear obfuscated in the Crashlytics page of the Firebase console.

### Kotlin

```kotlin
import com.google.firebase.crashlytics.buildtools.gradle.CrashlyticsExtension

// ...

android {

// To enable Crashlytics mapping file upload for specific build types:
buildTypes {
  getByName("debug") {
    minifyEnabled = true
    configure<CrashlyticsExtension> {
      mappingFileUploadEnabled = false
    }
  }
}

...

// To enable Crashlytics mapping file upload for specific product flavors:
flavorDimensions += "environment"
productFlavors {
  create("staging") {
    dimension = "environment"
    ...
    configure<CrashlyticsExtension> {
      mappingFileUploadEnabled = false
    }
  }
  create("prod") {
    dimension = "environment"
    ...
    configure<CrashlyticsExtension> {
      mappingFileUploadEnabled = true
    }
  }
}
}
```

### Groovy

```groovy
android {

// To enable Crashlytics mapping file upload for specific build types:
buildTypes {
  debug {
    minifyEnabled true
    firebaseCrashlytics {
      mappingFileUploadEnabled false
    }
  }
}

...

// To enable Crashlytics mapping file upload for specific product flavors:
flavorDimensions "environment"
productFlavors {
  staging {
    dimension "environment"
    ...
    firebaseCrashlytics {
      mappingFileUploadEnabled false
    }
  }
  prod {
    dimension "environment"
    ...
    firebaseCrashlytics {
      mappingFileUploadEnabled true
    }
  }
}
}
```