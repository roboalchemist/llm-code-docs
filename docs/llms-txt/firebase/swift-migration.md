# Source: https://firebase.google.com/docs/ios/swift-migration.md.txt

<br />

We're merging our Swift extension SDKs into the main SDKs in order to make Swift-native APIs more broadly available and increase our ability to support new Swift language features in the future. The changes we're making and their expected impacts on your projects are documented below.

## What's changing?

Starting with Firebase for Apple SDK 10.17.0, the Swift extension SDKs have been merged into their corresponding main SDKs. For example, all of the APIs from the`FirebaseFirestoreSwift`module have been added to`FirebaseFirestore`, so you no longer have to import the`FirebaseFirestoreSwift`module to access those APIs.

As all Swift extensions now are part of the main modules, the extension SDKs are no longer required, and are deprecated. Including or using the Swift extension SDKs will raise a compiler warning and as early as February 2024, we'll stop releasing the Swift extensions entirely.

â Note: Any currently or previously released versions of the Swift extensions will still function. However, we recommend that you migrate your app to use Swift APIs from the main module to ensure you continue to receive fixes and can take advantage of changes and new features.

## Important dates for this change

### In October 2023

The Swift extension SDKs have been merged into the main SDKs and then deprecated in favor of the main SDKs. See the release notes for version 10.17.0 announcing this change.

You can now use the Swift extension SDK APIs directly from the main SDK modules. Usage of the extension SDKs will is still possible until the next major version release but will raise a deprecation warning when used.

### As early as February 2024

We'll stop releasing new versions of the Swift extensions, and we'll remove the Swift extensions from Firebase's`Package.swift`. Older versions will continue to function but will not receive updates.

## How to migrate to use Swift-native APIs from the main module

If you currently do not use the Swift extension SDKs, no action is necessary. If you do use a Swift extension SDK, make the following changes in your project.

### Workspace changes

#### Swift Package Manager

After updating Firebase to version 10.17.0+, navigate to the Frameworks, Libraries, and Embedded Content section in the General tab of your target's settings and remove the Swift extension SDK (such as`FirebaseFirestoreSwift`).

#### CocoaPods

After updating Firebase to version 10.17.0+, navigate to your Podfile and remove the line corresponding to your project's dependency on adding the frameworks section for your target and remove the Swift extension SDK (such as pod`FirebaseFirestoreSwift`). Then, re-run the`pod install`command.

#### Zip distribution and Carthage

After updating Firebase to version 10.17.0+, remove any Swift extension`xcframeworks`within your project (such as`FirebaseFirestoreSwift.xcframework`).

### Source code changes

For all of the Swift extension SDKs you previously used, take the following actions:

1. Delete any import statements referencing the Swift extension SDK. If the main SDK was not imported separately, you will need to replace the Swift extension import with the main SDK import by deleting the`Swift`at the end of the line.
2. If you used Swift's explicit-module namespacing to reference any Swift extension SDK types, you will need to replace those with the corresponding main SDK. For example,`FirebaseFirestoreSwift.QueryPredicate`would need to be renamed to`FirebaseFirestore.QueryPredicate`.