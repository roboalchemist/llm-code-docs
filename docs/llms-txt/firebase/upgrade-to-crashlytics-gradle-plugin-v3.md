# Source: https://firebase.google.com/docs/crashlytics/upgrade-to-crashlytics-gradle-plugin-v3.md.txt

<br />

The latest release of theCrashlyticsGradle plugin is a major version (v3.0.0) and modernizes the SDK by dropping support for lower versions of Gradle and the Android Gradle plugin. Additionally, the changes in this release resolve issues with AGP v8.1+ and improve support for native apps and customized builds.

## Minimum requirements

TheCrashlyticsGradle plugin v3 has the following minimum requirements:

- Android Gradle plugin 8.1+  
  Upgrade this plugin using the[Android Gradle plugin Upgrade Assistant](https://developer.android.com/build/agp-upgrade-assistant)on the latest version of Android Studio.

- Firebase's`google-services`Gradle plugin 4.4.1+  
  Upgrade this plugin by specifying the latest version in your project's Gradle build file, like so:

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

## Changes to theCrashlyticsextension

With v3 of theCrashlyticsGradle plugin, theCrashlyticsextension has the following breaking changes:

- Removed the extension from the`defaultConfig`android block. Instead, you should configure each variant.

- Removed the deprecated field`mappingFile`. Instead, the merged mapping file is now provided automatically.

- Removed the deprecated field`strippedNativeLibsDir`. Instead, you should use`unstrippedNativeLibsDir`for all native libs.

- Changed the field`unstrippedNativeLibsDir`to be cumulative.

  <br />

  View an example with multiple directories

  <br />

  <br />

  ```kotlin
    buildTypes {
      release {
        configure<CrashlyticsExtension> {
          nativeSymbolUploadEnabled = true
          unstrippedNativeLibsDir = file("<var class="readonly" translate="no">MY/NATIVE/LIBS</var>")
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
            unstrippedNativeLibsDir = file("<var class="readonly" translate="no">MY/FEATURE_X/LIBS</var>")
          }
        }
      }
    }
    
  ```

  <br />

  The`uploadCrashlyticsSymbolFilesBasicRelease`task will only upload the symbols in<var class="readonly" translate="no">MY/NATIVE/LIBS</var>, but`uploadCrashlyticsSymbolFilesFeatureXRelease`will upload symbols in both<var class="readonly" translate="no">MY/NATIVE/LIBS</var>and<var class="readonly" translate="no">MY/FEATURE_X/LIBS</var>.

  <br />

- Replaced the closure field`symbolGenerator`with two new top level fields:

  - `symbolGeneratorType`, a String of either`"breakpad"`(default) or`"csym"`.
  - `breakpadBinary`, a File of a local`dump_syms`binary override.

### Example for how to upgrade the extension

### Kotlin

|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Before**    | ```kotlin buildTypes { release { configure<CrashlyticsExtension> { // ... symbolGenerator( closureOf<SymbolGenerator> { symbolGeneratorType = "breakpad" breakpadBinary = file("<var translate="no">/PATH/TO/BREAKPAD/DUMP_SYMS</var>") } ) } } } ``` |
| **Now in v3** | ```kotlin buildTypes { release { configure<CrashlyticsExtension> { // ... symbolGeneratorType = "breakpad" breakpadBinary = file("<var translate="no">/PATH/TO/BREAKPAD/DUMP_SYMS</var>") } } } ```                                                   |

### Groovy

|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Before**    | ```groovy buildTypes { release { firebaseCrashlytics { // ... symbolGenerator { breakpad { binary file("<var translate="no">/PATH/TO/BREAKPAD/DUMP_SYMS</var>") } } } } } ```       |
| **Now in v3** | ```groovy buildTypes { release { firebaseCrashlytics { // ... symbolGeneratorType "breakpad" breakpadBinary file("<var translate="no">/PATH/TO/BREAKPAD/DUMP_SYMS</var>") } } } ``` |