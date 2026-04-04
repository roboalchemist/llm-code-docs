# Source: https://firebase.google.com/docs/ios/installation-methods.md.txt

<br />

## Swift Package Manager

Firebase recommends Swift Package Manager for new projects.

### Via Xcode

Swift Package Manager support requires 16.2 or higher.

1. If migrating from a CocoaPods-based project, run`pod deintegrate`to remove CocoaPods from your Xcode project. The CocoaPods-generated`.xcworkspace`file can safely be deleted afterward. If you're adding Firebase to a project for the first time, this step can be ignored.

2. In Xcode, install the Firebase libraries by navigating to**File \> Add Packages**.

3. In the prompt that appears, select the Firebase GitHub repository:

       https://github.com/firebase/firebase-ios-sdk.git

4. Select the version of Firebase you want to use. For new projects, we recommend using the newest version of Firebase.

5. Choose the Firebase libraries you want to include in your app.

Once you're finished, Xcode will begin resolving your package dependencies and downloading them in the background.

### Via`Package.swift`

To integrate Firebase to a Swift package via a`Package.swift`manifest, you can add Firebase to the`dependencies`array of your package. For more details, see the[Swift Package Manager documentation](https://docs.swift.org/package-manager/PackageDescription/PackageDescription.html#package-dependency).  

    dependencies: [

      .package(name: "Firebase",
               url: "https://github.com/firebase/firebase-ios-sdk.git",
               from: "8.0"),
      // ...

    ],

Then in any target that depends on a Firebase product, add it to the[`dependencies`array](https://docs.swift.org/package-manager/PackageDescription/PackageDescription.html#target-dependency)of that target.  

    .target(
      name: "MyTargetName",
      dependencies: [
        .product(name: "FirebaseAuth", package: "Firebase"),
        // ...
      ]
    ),

### Product-specific considerations

Some Firebase products require extra integration steps in order to function correctly.

#### Google Analytics

Google Analyticsrequires adding the`-ObjC`linker flag to your target's build settings if included transitively.

#### Crashlytics

Crashlyticsrequires you to upload debug symbols.

You can use a run script build phase for Xcode to automatically upload debug symbols post-build. Find the run script here:  

    ${BUILD_DIR%Build/*}/SourcePackages/checkouts/firebase-ios-sdk/Crashlytics/run

Another option for uploading symbols is to use the[`upload-symbols`](https://github.com/firebase/firebase-ios-sdk/raw/master/Crashlytics/upload-symbols)script. Place the script in a subdirectory of your project file (for example`scripts/upload-symbols`), then make sure that the script is executable:  

    chmod +x scripts/upload-symbols

This script can be used to manually upload dSYM files. For usage notes and additional instructions for the script, run`upload-symbols`without any parameters.

## CocoaPods

Firebase supports installation with[CocoaPods](https://guides.cocoapods.org/using/getting-started.html#getting-started)in addition to Swift Package Manager.

Firebase's CocoaPods distribution requires Xcode 16.2 and CocoaPods 1.12.0 or higher. Here's how to install Firebase using CocoaPods:

1. Create a Podfile if you don't already have one. From the root of your project directory, run the following command:

   ```
   pod init
   ```
   | **Note:** Podfiles must include`use_frameworks!`(dynamic linking) or`use_frameworks! :linkage => :static`; please see the documentation on[linking Firebase dependencies statically or dynamically](https://firebase.google.com/docs/ios/link-firebase-static-dynamic)for more details.
2. To your Podfile, add the Firebase pods that you want to use in your app.

   You can add any of the[supported Firebase products](https://firebase.google.com/docs/ios/setup#available-pods)to your app.  

   ### Analyticsenabled

   ```text
   # Add the Firebase pod for Google Analytics
   pod 'FirebaseAnalytics'

   # For Analytics without IDFA collection capability, use this pod instead
   # pod FirebaseAnalytics/Core

   # Add the pods for any other Firebase products you want to use in your app
   # For example, to use Firebase Authentication and Cloud Firestore
   pod 'FirebaseAuth'
   pod 'FirebaseFirestore'
   ```

   Learn more about IDFA, the device-level advertising identifier, in Apple's[User Privacy and Data Use](https://developer.apple.com/app-store/user-privacy-and-data-use/)and[App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency)documentation.

   ### Analyticsnot enabled

   ```text
   # Add the pods for the Firebase products you want to use in your app
   # For example, to use Firebase Authentication and Cloud Firestore
   pod 'FirebaseAuth'
   pod 'FirebaseFirestore'
   ```
   | Binary Firebase dependencies are integrated as static frameworks by default. If you're using Firebase as a dependency of a dynamic framework, make sure you read the documentation about[using Firebase from a framework or a library](https://github.com/firebase/firebase-ios-sdk/blob/master/docs/firebase_in_libraries.md).
3. Install the pods, then open your`.xcworkspace`file to see the project in Xcode:

   ```
   pod install --repo-update
   ```  

   ```
   open your-project.xcworkspace
   ```

### Product-specific considerations

Some Firebase products require extra integration steps in order to function correctly.

#### Crashlytics

Crashlyticsrequires you to upload debug symbols.

You can use a run script build phase for Xcode to automatically upload debug symbols post-build. Find the run script here:  

    "${PODS_ROOT}/FirebaseCrashlytics/run"

## Carthage

Carthage support is experimental. See the[instructions on GitHub](https://github.com/firebase/firebase-ios-sdk/blob/master/Carthage.md)for including Firebase in your app via Carthage.

## Integrate manually

Firebase provides a pre-built binary XCFramework distribution for users who want to integrate Firebase without using a dependency manager. To install Firebase:

1. Download the[framework SDK zip](https://firebase.google.com/download/ios). This file contains architecture slices for all available target architectures for all Firebase SDKs and thus may take some time to download.

2. Unzip the file, then review the`README`for the frameworks that you want to include in your app.

3. Add the[`-ObjC`linker flag](https://developer.apple.com/library/content/qa/qa1490/_index.html)in your`Other Linker Settings`in your target's build settings.