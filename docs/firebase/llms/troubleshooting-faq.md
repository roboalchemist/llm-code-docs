# Source: https://firebase.google.com/docs/ios/troubleshooting-faq.md.txt

# Source: https://firebase.google.com/docs/android/troubleshooting-faq.md.txt

# Source: https://firebase.google.com/docs/unity/troubleshooting-faq.md.txt

# Source: https://firebase.google.com/docs/android/troubleshooting-faq.md.txt

# Source: https://firebase.google.com/docs/unity/troubleshooting-faq.md.txt

<br />

This page offers tips and troubleshooting for Unity-specific issues that you might encounter when using Firebase.

Have other challenges or don't see your issue outlined below? Make sure to check out the[main Firebase FAQ](https://firebase.google.com/support/faq)for more pan-Firebase or product-specific FAQ.

## An issue with single dex while building Android app

While building Android app, you may encounter a build failure related to having a single dex file. The error message looks similar to the following, if your project is configured to use the Gradle build system.  

    Cannot fit requested classes in a single dex file.

Dalvik Executable (`.dex`) files are used to hold a set of class definitions and their associated adjunct data for Android applications (`.apk`). A single dex file is limited to reference to 65,536 methods. The build will fail if the total number of methods from all Android libraries in your project exceeds this limit.

Unity introduced[Minification](https://docs.unity3d.com/2017.2/Documentation/Manual/android-gradle-overview.html)in 2017.2, which uses Proguard (or other tools in some versions of Unity) to strip out unused code, which can reduce the total number of referenced methods in a single dex file. The option can be found in**Player Settings \> Android \> Publishing Settings \> Minify**. The options may differ in different version of Unity so refer to the official Unity documentation.

If the number of referenced methods still exceeds the limit, another option is to enable`multidex`. There are multiple ways to achieve this in Unity:

- If`Custom Gradle Template`under`Player Settings`is enabled, modify`mainTemplate.gradle`.
- If you use Android Studio to build the exported project, modify module-level`build.gradle`file.

More details can be found in[the multidex user guide](https://developer.android.com/studio/build/multidex).

## Issues when building for Android with minSdkVersion 23

When building for Android, if you target`minSdkVersion`23, it might fail on the dexing step, usually in the Gradle task ':launcher:mergeExtDexDebug', where it will say it "Failed to transform" one of the Android libraries. This is caused because of a bug in the default dex tool in the Android SDK that most Unity editors use, and can be fixed in a few different ways:

- Set the`minSdkVersion`to 24.
- Turn on Android minification, in**Player Settings \> Android \> Publishing Settings \> Minify**
- Specify a different version of the dex tool by adding this to your`settingsTemplate.gradle`file:

    buildscript {
      repositories {
        mavenLocal()
        maven { url 'https://maven.google.com'  }
        mavenCentral()
      }
      dependencies {
        classpath 'com.android.tools:r8:8.3.37'
      }
    }

## Issues when building for iOS with Cocoapods

When building for iOS, Cocoapod installation may fail with an error about the language locale, or UTF-8 encoding. There are currently several different ways to work around the issue.

- From the terminal, run`pod install`directly, and open the resulting xcworkspace file.

- Downgrade the version of Cocoapods to 1.10.2. The issue exists only in version 1.11 and newer.

- In your`~/.bash_profile`or equivalent, add`export LANG=en_US.UTF-8`

## How to update the version of Firebase Unity SDKs

The process to update the versions of Firebase Unity SDKs depends on how they were initially imported. Here are the two alternative import methods:

- Importing`.unitypackage`files under your project's`Assets/`directory
- Importing using the[Unity Package Manager](https://docs.unity3d.com/Manual/Packages.html)(UPM)
  - This is the recommended way to manage packages in Unity 2018.4+.
  - Use this method to make future version updates easier and your`Assets/`directory cleaner.

In your Unity project, you should only use one import method to manage all your Firebase packages. The instructions below can be used to not only update the version of individual packages, but also, if needed, to migrate package management to UPM (the recommended import method).
| **Note:** Before updating the SDK version, manually create a local backup. Afterward, if the project fails to build or run properly in the editor or on target platforms, you can restore from the backup.

<br />

### Packages imported as`.unitypackage`files into the`Assets/`directory

<br />

If Firebase packages are in the`Assets/`directory, you have two options for updating the SDK version:

- *Option 1*(recommended)**: Migrate to use UPM (available in Unity 2018.4+)

  - Follow the Firebase-provided[instructions to migrate package management to UPM](https://firebase.google.com/docs/unity/setup-alternative#alternative_migrate_to_upm).
  - While this method requires more initial setup than continuing to use the`.unitypackage`workflow, it pays off in ease of subsequent SDK version updates.
- *Option 2* : Continue to use`.unitypackage`files to import them into the`Assets/`directory

  1. Import[each of the packages](https://firebase.google.com/docs/unity/setup-alternative#alternative_individual_unitypackages)for the updated version.

     If you download[firebase_unity_sdk.zip](https://firebase.google.com/docs/unity/setup)from the Firebase website, make sure that you import all`.unitypackages`from the correct`dotnet`folder.
     - If you're using Unity 2019 or later, import from the`dotnet4`folder.
     - Otherwise, select*Scripting Runtime Version* in*Player Settings* , and if it's set to ".NET 3.x", import from the`dotnet3`folder.
  2. Overwriting of the previously imported package versions should be handled automatically by the External Dependency Manager (which is automatically included when you import the Firebase`.unitypackages`).

     However, if and ONLY if this automatic process fails, you'll need to manually delete the following folders and then re-try the above import step again.
     - `Assets/Editor Default Resources/Firebase`
     - `Assets/ExternalDependencyManager`
     - `Assets/Firebase`
     - `Assets/Parse`
     - `Assets/Plugins/iOS/Firebase`

<br />

### Packages managed by UPM

<br />

If Firebase packages are managed by UPM,[import the newer SDK version as a`.tgz`](https://firebase.google.com/docs/unity/setup-alternative#alternative_unity_package_manager). This import will automatically overwrite the previous version.
| **Note:** Make sure to upgrade ALL Firebase Unity packages and their dependencies (including`com.google.firebase.app`) to the same version. The only exception is the dependency on the External Dependency Manager, which should be updated to the[`com.google.external-dependency-manager`version](https://developers.google.com/unity/archive#firebase_app_core)that corresponds to the updated version of your Firebase Unity packages.