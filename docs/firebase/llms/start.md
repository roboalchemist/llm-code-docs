# Source: https://firebase.google.com/docs/database/unity/start.md.txt

# Source: https://firebase.google.com/docs/database/rest/start.md.txt

# Source: https://firebase.google.com/docs/database/flutter/start.md.txt

# Source: https://firebase.google.com/docs/database/android/start.md.txt

# Source: https://firebase.google.com/docs/database/admin/start.md.txt

# Source: https://firebase.google.com/docs/auth/web/start.md.txt

# Source: https://firebase.google.com/docs/auth/ios/start.md.txt

# Source: https://firebase.google.com/docs/storage/unity/start.md.txt

# Source: https://firebase.google.com/docs/storage/flutter/start.md.txt

# Source: https://firebase.google.com/docs/storage/cpp/start.md.txt

# Source: https://firebase.google.com/docs/storage/android/start.md.txt

# Source: https://firebase.google.com/docs/storage/admin/start.md.txt

# Source: https://firebase.google.com/docs/database/web/start.md.txt

# Source: https://firebase.google.com/docs/database/ios/start.md.txt

# Source: https://firebase.google.com/docs/database/cpp/start.md.txt

# Source: https://firebase.google.com/docs/auth/unity/start.md.txt

# Source: https://firebase.google.com/docs/auth/flutter/start.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/start.md.txt

# Source: https://firebase.google.com/docs/auth/android/start.md.txt

# Source: https://firebase.google.com/docs/analytics/unity/start.md.txt

# Source: https://firebase.google.com/docs/analytics/cpp/start.md.txt

# Source: https://firebase.google.com/docs/storage/web/start.md.txt

# Source: https://firebase.google.com/docs/storage/ios/start.md.txt

# Source: https://firebase.google.com/docs/database/web/start.md.txt

# Source: https://firebase.google.com/docs/database/ios/start.md.txt

# Source: https://firebase.google.com/docs/database/cpp/start.md.txt

# Source: https://firebase.google.com/docs/auth/unity/start.md.txt

# Source: https://firebase.google.com/docs/auth/flutter/start.md.txt

# Source: https://firebase.google.com/docs/auth/cpp/start.md.txt

# Source: https://firebase.google.com/docs/auth/android/start.md.txt

# Source: https://firebase.google.com/docs/analytics/unity/start.md.txt

# Source: https://firebase.google.com/docs/analytics/cpp/start.md.txt

# Source: https://firebase.google.com/docs/storage/web/start.md.txt

# Source: https://firebase.google.com/docs/storage/ios/start.md.txt

<br />

Cloud Storage for Firebaselets you upload and share user generated content, such as images and video, which allows you to build rich media content into your apps. Your data is stored in a[Google Cloud Storage](https://cloud.google.com/storage)bucket --- an exabyte scale object storage solution with high availability and global redundancy.Cloud Storage for Firebaselets you securely upload these files directly from mobile devices and web browsers, handling spotty networks with ease.

## Before you begin

1. If you haven't already, make sure you've completed the[getting started guide for Apple platforms apps](https://firebase.google.com/docs/ios/setup). This includes:

   - Creating a Firebase project.

   - Registering your Apple platforms app with the project, and connecting your app to Firebase by adding the Firebase library and your Firebase config file (`GoogleService-Info.plist`) to your app.

2. Make sure your Firebase project is on the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing), which is a requirement that started in October 2024 (see our[FAQs](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024)). If you're new to Firebase and Google Cloud, check if you're eligible for a[$300 credit](https://firebase.google.com/support/faq#pricing-free-trial).

## Create a defaultCloud Storagebucket

1. From the navigation pane of the[Firebaseconsole](https://console.firebase.google.com/), select**Storage**.

   If your project is not yet on the pay-as-you-go Blaze pricing plan, then you'll be prompted to upgrade your project.
2. Click**Get started**.

3. Select a[location](https://firebase.google.com/docs/storage/locations)for your default bucket.

   - Buckets in`US-CENTRAL1`,`US-EAST1`, and`US-WEST1`can take advantage of the["Always Free" tier](https://cloud.google.com/storage/pricing#cloud-storage-always-free)forGoogle Cloud Storage. Buckets in all other locations follow[Google Cloud Storagepricing and usage](https://cloud.google.com/storage/pricing).

   - If you'd like, you can later[create multiple buckets](https://firebase.google.com/docs/storage/ios/start#use_multiple_storage_buckets), each with its own location.

4. Configure theFirebase Security Rulesfor your default bucket. During development, consider[setting up your rules for public access](https://firebase.google.com/docs/storage/ios/start#set_up_public_access).

5. Click**Done**.

You can now view the bucket in the[Cloud Storage*Files*tab](https://console.firebase.google.com/project/_/storage/)of theFirebaseconsole. Your default bucket name format is<var translate="no">PROJECT_ID</var>`.firebasestorage.app`.
| **Note:** StartingOctober 30, 2024, all new defaultCloud Storagebuckets have the name format<var translate="no">PROJECT_ID</var>`.firebasestorage.app`. Any default buckets created*before* that date have the name format<var translate="no">PROJECT_ID</var>`.appspot.com`. Learn more in the[FAQs](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#all-changes-default-storage-bucket).

## Set up public access

Cloud Storage for Firebaseprovides a declarative rules language that lets you define how your data should be structured, how it should be indexed, and when your data can be read from and written to. By default, read and write access toCloud Storageis restricted so only authenticated users can read or write data. To get started without setting up[Authentication](https://firebase.google.com/docs/auth), you can[configure your rules for public access](https://firebase.google.com/docs/storage/security/rules-conditions#public).

This does makeCloud Storageopen to anyone, even people not using your app, so be sure to restrict yourCloud Storageagain when you set up authentication.

## AddCloud Storageto your app

Use Swift Package Manager to install and manage Firebase dependencies.
| Visit[our installation guide](https://firebase.google.com/docs/ios/installation-methods)to learn about the different ways you can add Firebase SDKs to your Apple project, including importing frameworks directly and using CocoaPods.

1. In Xcode, with your app project open, navigate to**File \> Add Packages**.
2. When prompted, add the Firebase Apple platforms SDK repository:  

```text
  https://github.com/firebase/firebase-ios-sdk.git
```
| **Note:**New projects should use the default (latest) SDK version, but you can choose an older version if needed.
3. Choose theCloud Storagelibrary.
4. Add the`-ObjC`flag to the*Other Linker Flags*section of your target's build settings.
5. When finished, Xcode will automatically begin resolving and downloading your dependencies in the background.

## Set upCloud Storagein your app

1. Initialize Firebase before any Firebase reference is created or used.

   You may have already done this if you've already set up another Firebase product, but you need to make sure to add the`FirebaseStorage`library to your list of imports.
   1. Import the`FirebaseCore`module and the`FirebaseStorage`module in your`UIApplicationDelegate`. We also recommend adding`FirebaseAuth`.

      ### SwiftUI

          import SwiftUI
          import FirebaseCore
          import FirebaseStorage
          import FirebaseAuth
          // ...

      ### Swift

          import FirebaseCore
          import FirebaseStorage
          import FirebaseAuth
          // ...

      ### Objective-C

          @import FirebaseCore;
          @import FirebaseStorage;
          @import FirebaseAuth;
          // ...

   2. Configure a[`FirebaseApp`](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp)shared instance in your app delegate's`application(_:didFinishLaunchingWithOptions:)`method:

      ### SwiftUI

          // Use Firebase library to configure APIs
          FirebaseApp.configure()

      ### Swift

          // Use Firebase library to configure APIs
          FirebaseApp.configure()

      ### Objective-C

          // Use Firebase library to configure APIs
          [FIRApp configure];

   3. *(SwiftUI only)* Create an application delegate and attach it to your`App`struct using`UIApplicationDelegateAdaptor`or`NSApplicationDelegateAdaptor`. You must also disable app delegate swizzling. For more information, see the[SwiftUI instructions](https://firebase.google.com/docs/ios/learn-more#swiftui).

      ### SwiftUI

          @main
          struct YourApp: App {
            // Register app delegate for Firebase setup
            @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

            var body: some Scene {
              WindowGroup {
                NavigationView {
                  ContentView()
                }
              }
            }
          }

2. Get a reference to theCloud Storageservice, using the default Firebase App.

   1. Make sure the Firebase config file (`GoogleService-Info.plist`) in your app's codebase is updated with the name of your defaultCloud Storagebucket.

      1. [Obtain your updated config file.](https://support.google.com/firebase/answer/7015592#ios).

      2. Use this downloaded config file to*replace* the existing`GoogleService-Info.plist`file in the root of your Xcode project. If prompted, select to add the config file to all targets.

         Make sure that you only have this most recent downloaded config file in your app and that its filename isn't appended with additional characters, like`(2)`.

      | **Note:** Alternatively to replacing your config file, you can explicitly specify the bucket name when you create a reference to theCloud Storageservice (see next step). You can find the bucket name in the[Cloud Storage*Files*tab](https://console.firebase.google.com/project/_/storage/)of theFirebaseconsole.
   2. Get a reference to theCloud Storageservice, using the default Firebase App:

      ### Swift

      <br />

      ```swift
      let storage = Storage.storage()
      ```  

      ```swift
      // Alternatively, explicitly specify the bucket name URL.
      storage = Storage.storage(url:"gs://<var translate="no">BUCKET_NAME</var>")
      ```

      <br />

      ### Objective-C

      <br />

      ```objective-c
      FIRStorage *storage = [FIRStorage storage];
      ```  

      ```objective-c
      // Alternatively, explicitly specify the bucket name URL.
      // FIRStorage storage = [FIRStorage storageWithURL:@"gs://<var translate="no">BUCKET_NAME</var>"];
      ```

      <br />

You're ready to start usingCloud Storage!

Next step? Learn how to[create aCloud Storagereference](https://firebase.google.com/docs/storage/ios/create-reference).

## Advanced setup

There are a few use cases that require additional setup:

- UsingCloud Storagebuckets in[multiple geographic regions](https://cloud.google.com/storage/docs/bucket-locations)
- UsingCloud Storagebuckets in[different storage classes](https://cloud.google.com/storage/docs/storage-classes)
- UsingCloud Storagebuckets with multiple authenticated users in the same app

The first use case is perfect if you have users across the world, and want to store their data near them. For instance, you can create buckets in the US, Europe, and Asia to store data for users in those regions to reduce latency.

The second use case is helpful if you have data with different access patterns. For instance: you can set up a multi-regional or regional bucket that stores pictures or other frequently accessed content, and a nearline or coldline bucket that stores user backups or other infrequently accessed content.

In either of these use cases, you'll want to[use multipleCloud Storagebuckets](https://firebase.google.com/docs/storage/ios/start#use_multiple_storage_buckets).

The third use case is useful if you're building an app, like Google Drive, which lets users have multiple logged in accounts (for instance, a personal account and a work account). You can[use a custom Firebase App](https://firebase.google.com/docs/storage/ios/start#use_a_custom_firebase_app)instance to authenticate each additional account.

### Use multipleCloud Storagebuckets

If you want to use aCloud Storagebucket other than the default provided above, or use multipleCloud Storagebuckets in a single app, you can create an instance of`FIRStorage`that references your custom bucket:  

### Swift

```swift
// Get a non-default Cloud Storage bucket
storage = Storage.storage(url:"gs://my-custom-bucket")
    
```

### Objective-C

```objective-c
// Get a non-default Cloud Storage bucket
FIRStorage storage = [FIRStorage storageWithURL:@"gs://my-custom-bucket"];
    
```

### Working with imported buckets

When importing an existingCloud Storagebucket into Firebase, you'll have to grant Firebase the ability to access these files using the`gsutil`tool, included in the[Google CloudSDK](https://cloud.google.com/sdk/docs/):  

```
gsutil -m acl ch -r -u service-PROJECT_NUMBER@gcp-sa-firebasestorage.iam.gserviceaccount.com gs://BUCKET_NAME
```

You can find your project number as described in the[introduction to Firebase projects](https://firebase.google.com/docs/projects/learn-more#project-number).

This does not affect newly created buckets, as those have the default access control set to allow Firebase. This is a temporary measure, and will be performed automatically in the future.

### Use a custom Firebase App

If you're building a more complicated app using a custom`FirebaseApp`, you can create an instance of`Storage`initialized with that app:  

### Swift

```swift
// Get the default bucket from a custom FirebaseApp
storage = Storage.storage(app:customApp)

// Get a non-default bucket from a custom FirebaseApp
storage = Storage.storage(app:customApp, url:"gs://my-custom-bucket")
    
```

### Objective-C

```objective-c
// Get the default bucket from a custom FIRApp
FIRStorage storage = [FIRStorage storageForApp:customApp];

// Get a non-default bucket from a custom FIRApp
FIRStorage storage = [FIRStorage storageForApp:customApp withURL:@"gs://my-custom-bucket"];
    
```

## Next steps

- Prepare to launch your app:

  - Enable[App Check](https://firebase.google.com/docs/app-check/ios)to help ensure that only your apps can access your storage buckets.

  - Set up[budget alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails)for your project in theGoogle Cloudconsole.

  - Monitor the[*Usage and billing*dashboard](https://console.firebase.google.com/project/_/usage)in theFirebaseconsole to get an overall picture of your project's usage across multiple Firebase services. You can also visit the[Cloud Storage*Usage*dashboard](https://console.firebase.google.com/project/_/storage/usage)for more detailed usage information.

  - Review the[Firebase launch checklist](https://firebase.google.com/support/guides/launch-checklist).