# Source: https://firebase.google.com/docs/unity/build-debug-guide.md.txt

<br />

## Introduction

The following is a guide to debugging the compile and build process for Unity games using the Firebase SDK for Unity. It describes how to investigate and solve many of the more common issues you can encounter while configuring and building your game for a new platform or after an update. It is arranged in order of when these errors may occur in the process. Consult them in order and proceed as each is resolved.

In addition to this doc, consult the[Firebase for Unity FAQ](https://firebase.google.com/docs/unity/troubleshooting-faq)for more information.

## Play Mode compilation issues

The first class of build issues can occur while testing in the editor before you try to start a mobile build. This section concerns all Firebase errors that occur before and during Play Mode.

When Unity starts or detects changes to dependencies, code or other assets, it will try to rebuild the project. If the project is unable to compile at that time, the editor will log compilation errors to the console and if you attempt to enter Play Mode, you will receive an error popup in Unity's**Scene** tab that reads`All compiler errors have to be fixed before you can enter playmode!`.

### Debugging Firebase-related compilation issues

#### Missing types, classes, methods and members

Many Firebase issues occur due to an inability of the editor and compiler to find necessary types, classes, methods and members. Common symptoms of this are variants of the following:

`The type or namespace name '<CLASS OR NAMESPACE NAME>' could not be found. Are you missing a using directive or an assembly reference?`

`The type or namespace name <TYPE OR NAMESPACE NAME> does not exist in the namespace 'Firebase<.OPTIONAL NESTED NAMESPACE NAME PATH>' (are you missing an assembly reference?)`

`'<CLASS NAME>' does not contain a definition for '<MEMBER VARIABLE OR METHOD NAME>'`

##### Resolution steps:

1. Where you are using Firebase classes or methods in code, make sure you are making them available by having the correct`using`directives for the particular Firebase products needed.

   1. Examples from[MechaHamster: Level Up With Firebase Edition](https://github.com/firebase/level-up-with-firebase):
      1. [`using Firebase.RemoteConfig;`](https://github.com/firebase/level-up-with-firebase/commit/9101f212bcd4764f00a1efa7178ec61ba8182da1#diff-c29e72ed39484e95376e121a707bdea4c3eb1bb53d4308101fef934e7ba94727)
      2. [`using Firebase.Crashlytics;`](https://github.com/firebase/level-up-with-firebase/commit/212463cb12f258a893fc84f71926d2e7f55f1901#diff-316bdfcacae445fcb469d91fafe5e17dd2833534bbf0d27123d4d067ff607a13)
2. Verify that you have imported the appropriate Firebase packages:

   1. To import the appropriate packages either:
      1. [Add Firebase Unity SDK as`.unitypackage`s](https://firebase.google.com/docs/unity/setup#add-sdks)or
      2. Look into and perform one of the alternatives in[Additional Unity installation options](https://firebase.google.com/docs/unity/setup-alternative).
   2. Ensure that every Firebase product in your project and[EDM4U](https://github.com/googlesamples/unity-jar-resolver):
      - Are at the same version
      - Were installed either as`.unitypackage`s exclusively*OR*exclusively through the Unity Package Manager.
3. If you have imported the Firebase Unity SDK prior to version "10.0.0" as`.unitypackage`s, the Firebase Unity SDK zip archive contains packages for both .NET 3.x and .NET 4.x support. Make sure that you have only included the compatible .NET Framework level in your project:

   1. Compatibility between versions of the Unity Editor and .NET Frameworks Levels are discussed in[Add Firebase to your Unity project](https://firebase.google.com/docs/unity/setup#add-sdks).
   2. If you accidentally imported your Firebase packages at the wrong .NET Framework Level or need to switch from using`.unitypackage`s to one of the[Additional Unity installation options](https://firebase.google.com/docs/unity/setup-alternative), the cleanest way is to remove every Firebase package through the methods mentioned in[this migration section](https://firebase.google.com/docs/unity/setup-alternative#manual-removal)and then reimport all Firebase packages again.
4. Check that your editor is rebuilding your project and that your attempts to play reflect the most current state of your project:

   1. By default, the Unity editor is set to rebuild whenever asset or configuration changes are detected.
   2. It is possible that this functionality has been disabled and that the Unity Editor is set to[manual refresh/recompile](https://support.unity.com/hc/en-us/articles/210452343-How-to-stop-automatic-assembly-compilation-from-script#:%7E:text=You%20can%20change%20this%20behavior,or%20Stop%20Playing%20And%20Recompile). Investigate this and try a manual refresh if this is the case.

## Play Mode runtime errors

If your game starts, but runs into issues with Firebase while running, try the following:

### Ensure that you approve Firebase bundles in "Security \& Privacy" on Mac OS

If, on starting up your game in the editor on Mac OS, you are presented a dialogue that says, "FirebaseCppApp-\<version\>.bundle Cannot be opened because the developer cannot be verified.", you must approve that specific bundle file in Mac's Security \& Privacy menu.

To do so, click**Apple Icon** \>**System Preferences** \>**Security \& Privacy**

In the security menu, about halfway down the page, there is a section that says ""FirebaseCppApp-\<version\>.bundle" was blocked from use because it is not from an identified developer."

Click the button labeled**Allow Anyway**.

![c35166e224cce720.png](https://firebase.google.com/static/docs/unity/build-debug-guide/img/c35166e224cce720.png)
| **Caution:** Do not approve files like this unless you trust the source or wrote them yourself and understand what they do and why they have been flagged by the system.

Go back to Unity and press**Play**again.

You will then see a warning similar to the first:

![5ad9ddb0d3a52892.png](https://firebase.google.com/static/docs/unity/build-debug-guide/img/5ad9ddb0d3a52892.png)

Press**Open**and your program will be able to proceed; you will not be asked about this particular file again.

### Ensure your project contains and is using valid configuration files

1. Make sure your build settings are set for the target you intend (iOS or Android) in**File \> Build Settings** . For a more complete discussion, read the[Unity Build Settings Documentation](https://docs.unity3d.com/Manual/BuildSettings.html).
2. Download the config file for your app (`google-services.json`for Android or`GoogleService-Info.plist`for iOS) and build target from the Firebase console in**Project Settings \> Your Apps**: If you already have these files, delete them in your project and replace them with the most recent version, making sure that they are spelled exactly as displayed above without "(1)" or other numbers attached to the file names.
3. If the console contains a message regarding files in`Assets/StreamingAssets/`, make sure there are no console messages saying Unity was unable to edit files there
4. Make sure`Assets/StreamingAssets/google-services-desktop.json`is generated and matches the downloaded config file.
   - If it is not automatically generated and`StreamingAssets/`does not exist, manually create the directory in the`Assets`directory.
   - Check if Unity has now generated`google-services-desktop.json`.

### Ensure that every Firebase product and[EDM4U](https://github.com/googlesamples/unity-jar-resolver)were installed exclusively through either`.unitypackage`or the Unity Package Manager

1. Check both the`Assets/`folder and Unity Package Manager to make sure that Firebase SDKs and EDM4U were installed through one or the other method exclusively.
2. Some[Google-developed plugins](https://developers.google.com/unity), such as Google Play, and third-party plugins may depend on EDM4U. Those plugins may include EDM4U in their`.unitypackage`s or Unity Package Manager (UPM) packages. Ensure there is only one copy of EDM4U in your project. If any UPM packages depend on EDM4U, it is best to keep only the UPM versions of EDM4U, which can be found on the[Google APIs for Unity Archive page](https://developers.google.com/unity/archive#external_dependency_manager_for_unity).

### Ensure that every Firebase product in your project is at the same version.

1. If Firebase SDKs were installed through`.unitypackage`, check if all the`FirebaseCppApp`libraries under`Assets/Firebase/Plugins/x86_64/`are at the same version.
2. If Firebase SDKs were installed through Unity Package Manager (UPM), open**Windows** \>**Package Manager**, search for "Firebase" and make sure all Firebase packages are at the same version.
3. If your project contains different versions of Firebase SDKs, we recommend that you remove all Firebase SDKs entirely before installing all Firebase SDKs again, this time with the same versions. The cleanest way is to remove every Firebase package through the methods mentioned in[this migration section](https://firebase.google.com/docs/unity/setup-alternative#manual-removal).

## Resolver and target device build errors

If your game works in the editor (configured for the appropriate build target of your choosing), next verify that the[External Dependency Manager for Unity](https://github.com/googlesamples/unity-jar-resolver)(EDM4U) is properly configured and functioning.
| **Note:** You will have added EDM4U as part of the Unity Firebase setup process.

The EDM4U GitHub repository contains[a step by step guide](https://github.com/googlesamples/unity-jar-resolver/blob/master/troubleshooting-faq.md)for this part of the process that you should review and follow before proceeding.

## 'Single Dex' issues and minification (*Mandatory*if using Cloud Firestore)

While building an Android app, you may encounter a build failure related to having a single dex file. The error message looks similar to the following (if your project is configured to use the Gradle build system):

`Cannot fit requested classes in a single dex file.`

`.dex`files are used to hold a set of class definitions and their associated adjunct data for Android applications. A single dex file is limited to reference to 65,536 methods; builds will fail if the total number of methods from all Android libraries in your project exceeds this limit.

The following two steps can be applied sequentially; only enable multidex if minification doesn't resolve the issue.

#### Enable Minification

Unity introduced[Minification](https://docs.unity3d.com/2017.2/Documentation/Manual/android-gradle-overview.html)in 2017.2 to strip out unused code, which can reduce the total number of referenced methods in a single dex file. \* The option can be found in**Player Settings \> Android \> Publishing Settings \> Minify**. \* The options may differ in different versions of Unity so refer to the official Unity documentation.

#### Enable Multidex

If, after enabling minification, the number of referenced methods still exceeds the limit, another option is to enable`multidex`. There are multiple ways to achieve this in Unity:

- If**Custom Gradle Template** under**Player Settings** is enabled, modify`mainTemplate.gradle`.
- If you use Android Studio to build the exported project, modify the module-level**build.gradle**file.

More details can be found in the[multidex user guide](https://developer.android.com/studio/build/multidex).

## Understanding and fixing target device runtime errors

If your game works in editor and can be built for and installed to your target device, but you encounter runtime errors, inspect and*investigate the logs generated on the device*.

This section elaborates how to investigate your logs for possible errors and one such error that only occurs at runtime on device or simulator.

### Android

#### Simulator

- Inspect the logs displayed in your Emulator's console or view the[Logcat](https://developer.android.com/studio/debug/logcat)window.

#### Device

Familiarize yourself with[adb](https://developer.android.com/studio/command-line/adb)and[adb logcat](https://developer.android.com/studio/command-line/logcat#filteringOutput)and how to use them.

- While you can use your command line environment's various tools to filter the output, consider alternatively looking into logcat's[options](https://developer.android.com/studio/command-line/logcat#options).
- A simple way to start an ADB session with a clean slate is:

      adb logcat -c && adb logcat <OPTIONS>

  where`OPTIONS`are whichever flags you pass the command line to filter output.

#### Using Logcat through Android Studio

When using Logcat through Android Studio[additional search tools are available](https://developer.android.com/studio/debug/logcat#key-value-search)that make generating productive searches simpler.

### iOS

#### Inspecting Logs

If running a physical device, attach it to your computer. Inspect**lldb**in Xcode.

#### Swift Issues

If you run into error logs mentioning swift, consult the[External Dependency Manager for Unity](https://github.com/googlesamples/unity-jar-resolver)section regarding them.

# Further Steps

If your game still has compile, build or run issues related to Firebase, investigate the[Firebase SDK for Unity issues page](https://github.com/firebase/firebase-unity-sdk/issues)and consider filing a new issue. Additionally, refer to the Firebase[support page](https://firebase.google.com/support)to learn about additional options.