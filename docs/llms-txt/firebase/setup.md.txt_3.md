# Source: https://firebase.google.com/docs/ios/setup.md.txt

## Prerequisites

[Video](https://www.youtube.com/watch?v=F9Gs_pfT3hs)

- Install the following:

  - Xcode 16.2 or later
- Make sure that your project meets these requirements:

  - Your project must target these platform versions or later:
    - iOS 15
    - macOS 10.15
    - tvOS 15
    - watchOS 7

<!-- -->

- Set up a physical Apple device or use a simulator to run your app.

  <br />

  Do you want to use Cloud Messaging?

  <br />

  <br />

  > For Cloud Messaging on Apple platforms, here are the prerequisites:
  > - Set up a *physical Apple device*.
  > - Obtain an Apple Push Notification Authentication Key for your [Apple Developer account](https://developer.apple.com/account).
  > - Enable Push Notifications in Xcode under **App \> Capabilities**.

  <br />

  <br />

<!-- -->

- [Sign into Firebase](https://console.firebase.google.com/) using your Google account.

If you don't already have an Xcode project and just want to try out a Firebase
product, you can download one of our [quickstart samples](https://firebase.google.com/docs/samples).

## **Step 1**: Create a Firebase project

Before you can add Firebase to your Apple app, you need to create a Firebase
project to connect to your app. Visit
[Understand Firebase Projects](https://firebase.google.com/docs/projects/learn-more) to learn more about
Firebase projects.
**View instructions to create a Firebase project**

### New to Firebase or Cloud


Follow these steps if you're new to Firebase or Google Cloud.  

You can also follow these steps if you want to create a wholly new
Firebase project (and its underlying Google Cloud project).

1. Sign into the [Firebase console](https://console.firebase.google.com/).
2. Click the button to create a new Firebase project.
3. In the text field, enter a **project name**.

   If you're part of a Google Cloud org, you can optionally select which
   folder you create your project in.

   > [!CAUTION]
   > Your project name is used as a display name in Firebase interfaces, and Firebase auto-creates a unique project ID based on this project name. Note that you can optionally click the **Edit** icon now to set your preferred project ID, but you cannot change this ID after project creation. Learn about [how Firebase uses the
   > project ID](https://firebase.google.com/docs/projects/learn-more#project-id).

4. If prompted, review and accept the [Firebase terms](https://firebase.google.com/terms), then click **Continue**.
5. *(Optional)* Enable AI assistance in the Firebase console (called "Gemini in Firebase"), which can help you get started and streamline your development process.
6. *(Optional)* Set up Google Analytics for your project,
   which enables an optimal experience using these Firebase products:
   [Firebase A/B Testing](https://firebase.google.com/docs/ab-testing),
   [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging),
   [Crashlytics](https://firebase.google.com/docs/crashlytics),
   [In-App Messaging](https://firebase.google.com/docs/in-app-messaging), and
   [Remote Config](https://firebase.google.com/docs/remote-config)
   (including
   [Personalization](https://firebase.google.com/docs/remote-config/personalization)).

   Either select an existing
   [Google Analytics account](https://support.google.com/analytics/answer/1009618)
   or create a new account. If you create a new account, select your
   [Analytics reporting location](https://firebase.google.com/docs/projects/locations),
   then accept the data sharing settings and Google Analytics terms
   for your project.

   > [!NOTE]
   > You can always set up Google Analytics later in the [*Integrations* tab](https://console.firebase.google.com/project/_/settings/integrations) of your *Project settings*.

7. Click **Create project**.

Firebase creates your project, provisions some initial resources, and
enables important APIs. When the process completes, you'll be taken to the
overview page for your Firebase project in the Firebase console.

### Existing Cloud project


Follow these steps if you want to start using Firebase with an existing
Google Cloud project. Learn more about and troubleshoot
["adding
Firebase" to an existing Google Cloud project](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project).

1. Sign into the [Firebase console](https://console.firebase.google.com/) with the account that gives you access to the existing Google Cloud project.
2. Click the button to create a new Firebase project.
3. At the bottom of the page, click **Add Firebase to Google Cloud project**.
4. In the text field, start entering the **project name** of the existing project, and then select the project from the displayed list.
5. Click **Open project**.
6. If prompted, review and accept the [Firebase terms](https://firebase.google.com/terms), then click **Continue**.
7. *(Optional)* Enable AI assistance in the Firebase console (called "Gemini in Firebase"), which can help you get started and streamline your development process.
8. *(Optional)* Set up Google Analytics for your project,
   which enables an optimal experience using these Firebase products:
   [Firebase A/B Testing](https://firebase.google.com/docs/ab-testing),
   [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging),
   [Crashlytics](https://firebase.google.com/docs/crashlytics),
   [In-App Messaging](https://firebase.google.com/docs/in-app-messaging), and
   [Remote Config](https://firebase.google.com/docs/remote-config)
   (including
   [Personalization](https://firebase.google.com/docs/remote-config/personalization)).

   Either select an existing
   [Google Analytics account](https://support.google.com/analytics/answer/1009618)
   or create a new account. If you create a new account, select your
   [Analytics reporting location](https://firebase.google.com/docs/projects/locations),
   then accept the data sharing settings and Google Analytics terms
   for your project.

   > [!NOTE]
   > You can always set up Google Analytics later in the [*Integrations* tab](https://console.firebase.google.com/project/_/settings/integrations) of your *Project settings*.

9. Click **Add Firebase**.

Firebase
[adds
Firebase to your existing project](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#faq_what-happens-when-add-firebase).
When the process completes, you'll be taken to the overview page for your
Firebase project in the Firebase console.

## **Step 2**: Register your app with Firebase

To use Firebase in your Apple app, you need to register your app with your
Firebase project. Registering your app is often called "adding" your app to your
project.

> [!NOTE]
> **Note:** Check out our [best practices](https://firebase.google.com/docs/projects/dev-workflows/general-best-practices) for adding apps to a Firebase project, including how to handle multiple variants.

1. Go to the [Firebase console](https://console.firebase.google.com/).

2. In the center of the project overview page, click the **iOS+** icon
   to launch the setup workflow.

   If you've already added an app to your Firebase project, click **Add app**
   to display the platform options.
3. Enter your app's bundle ID in the **bundle ID** field.

   <br />

   What's a bundle ID, and where do you find it?

   <br />

   > - A [bundle ID](https://cocoacasts.com/what-are-app-ids-and-bundle-identifiers/)
   >   uniquely identifies an application in Apple's ecosystem.
   >
   > - Find your bundle ID: open your project in Xcode, select the
   >   top-level app in the project navigator, then select the **General** tab.
   >
   >   The value of the **Bundle Identifier** field is the bundle ID
   >   (for example, `com.yourcompany.yourproject`).
   > - Be aware that the bundle ID value is case-sensitive, and it cannot be
   >   changed for this Firebase app after it's registered with your
   >   Firebase project.

   <br />

   <br />

   > [!CAUTION]
   > Make sure to enter the bundle ID that your app is actually using. The bundle ID value is case-sensitive, and it cannot be changed for this Firebase Apple app after it's registered with your Firebase project.

4. *(Optional)* Enter other app information:
   **App nickname** and **App Store ID**.

   <br />

   How are the *App nickname* and the
   *App Store ID* used within Firebase?

   <br />

   > - **App nickname** : An internal, convenience identifier that is only visible
   >   to you in the Firebase console
   >
   > - **App Store ID** : Used by Firebase Dynamic Links to
   >   [redirect users to your App Store page](https://firebase.google.com/docs/dynamic-links/use-cases)
   >   and by Google Analytics to
   >   [import conversion events into
   >   Google Ads](https://support.google.com/google-ads/answer/6366292).
   >   If your app doesn't yet have an App Store ID, you can add the ID later
   >   in your [Project
   >   settings](https://console.firebase.google.com/project/_/settings/general).

   <br />

   <br />

5. Click **Register app**.

## **Step 3**: Add a Firebase configuration file

1. Click **Download GoogleService-Info.plist** to obtain your app's
   Firebase config file (`GoogleService-Info.plist`).

   <br />

   What do you need to know about this config file?

   <br />

   > - The Firebase config file contains unique, but non-secret identifiers for
   >   your project and app. To learn more about this config file, visit
   >   [Understand Firebase
   >   Projects](https://firebase.google.com/docs/projects/learn-more#config-files-objects).
   >
   > - You can download your [Firebase config
   >   file](https://support.google.com/firebase/answer/7015592)
   >   again at any time.
   >
   > - Make sure the config file name is not appended with additional characters,
   >   like `(2)`.

   <br />

   <br />

2. Move your config file into the root of your Xcode project. If prompted,
   select to add the config file to all targets.

If you have multiple bundle IDs in your project, you must associate each bundle
ID with a registered app in the Firebase console so that each app can have
its own `GoogleService-Info.plist` file.

## **Step 4**: Add Firebase SDKs to your app

Use Swift Package Manager to install and manage Firebase dependencies.

> [!NOTE]
> Visit [our installation guide](https://firebase.google.com/docs/ios/installation-methods) to learn about the different ways you can add Firebase SDKs to your Apple project.

1. In Xcode, with your app project open, navigate to **File \> Add Packages**.
2. When prompted, add the Firebase Apple platforms SDK repository:

```
  https://github.com/firebase/firebase-ios-sdk
```
3. Select the SDK version that you want to use.

   > [!NOTE]
   > **Note:** We recommend using the default (latest) SDK version, but you can choose an older version if needed.

4. Choose the Firebase libraries you want to use.

   If Google Analytics is enabled in your Firebase project, make sure
   to add `FirebaseAnalytics`. This provides all analytics features. You can
   also select individual features; refer to our FAQ on the
   [latest organization of modules in the Google Analytics for Firebase SDK](https://firebase.google.com/support/faq#analytics-odm2-sdk-refactor-ios).


When finished, Xcode will automatically begin resolving and downloading your
dependencies in the background.

## **Step 5**: Initialize Firebase in your app

The final step is to add initialization code to your application. You may have
already done this as part of adding Firebase to your app. If you're using a
[quickstart sample project](https://firebase.google.com/docs/samples), this has been done for you.

> [!NOTE]
> **Note:** To ease maintenance of our Apple platforms documentation, Firebase has decided to concentrate on Swift snippets and code samples in our guides and other developer materials. Objective-C snippets will be removed from our guides starting January 1, 2024. We will continue to maintain up-to-date [reference documentation](https://firebase.google.com/docs/reference/ios/modules) for Objective-C for all Firebase products.

1. Import the `FirebaseCore` module in your `UIApplicationDelegate`, as well as any other [Firebase modules](https://firebase.google.com/docs/ios/setup#available-pods) your app delegate uses. For example, to use Cloud Firestore and Authentication:

   #### SwiftUI

   ```swift
   import SwiftUI
   import FirebaseCore
   import FirebaseFirestore
   import FirebaseAuth
   // ...
         
   ```

   #### Swift

   ```swift
   import FirebaseCore
   import FirebaseFirestore
   import FirebaseAuth
   // ...
         
   ```

   #### Objective-C

   ```objective-c
   @import FirebaseCore;
   @import FirebaseFirestore;
   @import FirebaseAuth;
   // ...
         
   ```
2. Configure a [`FirebaseApp`](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp) shared instance in your app delegate's `application(_:didFinishLaunchingWithOptions:)` method:

   #### SwiftUI

   ```swift
   // Use Firebase library to configure APIs
   FirebaseApp.configure()
   ```

   #### Swift

   ```swift
   // Use Firebase library to configure APIs
   FirebaseApp.configure()
   ```

   #### Objective-C

   ```objective-c
   // Use Firebase library to configure APIs
   [FIRApp configure];
   ```
3. If you're using SwiftUI, you must create an application delegate and attach it to your `App` struct via `UIApplicationDelegateAdaptor` or `NSApplicationDelegateAdaptor`. You must also disable app delegate swizzling. For more information, see the [SwiftUI instructions](https://firebase.google.com/docs/ios/learn-more#swiftui).

   #### SwiftUI

   ```swift
   @main
   struct YourApp: App {
     // register app delegate for Firebase setup
     @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

     var body: some Scene {
       WindowGroup {
         NavigationView {
           ContentView()
         }
       }
     }
   }
         
   ```
4. If you've included the Firebase SDK for Google Analytics, you can run your app to send verification to the Firebase console that you've successfully installed Firebase.

That's it! You can skip ahead to the [next steps](https://firebase.google.com/docs/ios/setup#next_steps).

If you're having trouble getting set up, though, visit the
[Apple platforms troubleshooting \& FAQ](https://firebase.google.com/docs/ios/troubleshooting-faq).

> [!NOTE]
> **Note:** If you're targeting macOS or macOS Catalyst, you must add the [Keychain Sharing capability](https://firebase.google.com/docs/ios/troubleshooting-faq#macos-keychain-sharing) to your target. In Xcode, navigate to your target's *Signing \& Capabilities* tab, and then click **+ Capabilities** to add a new capability.

## Available libraries

This section lists the Firebase products supported for Apple platforms. Learn
more about these Firebase Apple platform libraries:

- Reference documentation
  ([Swift](https://firebase.google.com/docs/reference/swift/modules) \|
  [Obj-C](https://firebase.google.com/docs/reference/ios/modules))

- Firebase Apple platforms SDK [GitHub repo](https://github.com/firebase/firebase-ios-sdk)

> [!NOTE]
> For apps that use CocoaPods, the `Firebase` pod is deprecated
> in v9.0 and higher. Instead, you need to reference product pods directly
> in your Podfile (for example, `FirebaseCore` instead of
> `Firebase/Core` and `FirebaseFirestore` instead of
> `Firebase/Firestore`).

| **Service or Product** | **Pods** | **SwiftPM Libraries** |   |
|---|---|---|---|
| [AdMob](https://firebase.google.com/docs/admob/ios/quick-start) | `pod 'Google-Mobile-Ads-SDK'` | N/A | Yes |
| [Firebase AI Logic](https://firebase.google.com/docs/ai-logic/get-started) ^1^ | `pod 'FirebaseAILogic'` | `FirebaseAILogic` |   |
| [Analytics](https://firebase.google.com/docs/analytics/get-started?platform=ios) | `pod 'FirebaseAnalytics'` | `FirebaseAnalytics` | Yes |
| [App Check](https://firebase.google.com/docs/app-check) | `pod 'FirebaseAppCheck'` | `FirebaseAppCheck` |   |
| [App Distribution](https://firebase.google.com/docs/app-distribution/set-up-alerts) | `pod 'FirebaseAppDistribution'` | `FirebaseAppDistribution` |   |
| [Authentication](https://firebase.google.com/docs/auth/ios/start) | `pod 'FirebaseAuth'` | `FirebaseAuth` |   |
| [Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart) | `pod 'FirebaseFirestore'` | `FirebaseFirestore` |   |
| [Cloud Functions for Firebase Client SDK](https://firebase.google.com/docs/functions) | `pod 'FirebaseFunctions'` | `FirebaseFunctions` |   |
| [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/ios/client) | `pod 'FirebaseMessaging'` | `FirebaseMessaging` | Yes |
| [Cloud Storage](https://firebase.google.com/docs/storage/ios/start) | `pod 'FirebaseStorage'` | `FirebaseStorage` |   |
| [Crashlytics](https://firebase.google.com/docs/crashlytics/ios/get-started) | `pod 'FirebaseCrashlytics'` | `FirebaseCrashlytics` | Yes |
| [Data Connect](https://firebase.google.com/docs/data-connect/quickstart#swift) | N/A | `FirebaseDataConnect` |   |
| [In-App Messaging](https://firebase.google.com/docs/in-app-messaging/get-started?platform=ios) | `pod 'FirebaseInAppMessaging'` | `FirebaseInAppMessaging` | Yes *(required)* |
| [Firebase installations](https://firebase.google.com/docs/projects/manage-installations) | `pod 'FirebaseInstallations'` | `FirebaseInstallations` |   |
| [Firebase ML Custom Model APIs](https://firebase.google.com/docs/ml) | `pod 'FirebaseMLModelDownloader'` | `FirebaseMLModelDownloader` |   |
| [Performance Monitoring](https://firebase.google.com/docs/perf-mon/get-started-ios) | `pod 'FirebasePerformance'` | `FirebasePerformance` |   |
| [Realtime Database](https://firebase.google.com/docs/database/ios/start) | `pod 'FirebaseDatabase'` | `FirebaseDatabase` |   |
| [Remote Config](https://firebase.google.com/docs/remote-config/get-started?platform=ios) | `pod 'FirebaseRemoteConfig'` | `FirebaseRemoteConfig` | Yes |
| **DEPRECATED OR UNSUPPORTED LIBRARIES** ||||
| [Dynamic Links](https://firebase.google.com/docs/dynamic-links/ios/create) | `pod 'FirebaseDynamicLinks'` | `FirebaseDynamicLinks` | Yes |

^**1** *Firebase AI Logic (`FirebaseAILogic`) was formerly
called "Vertex AI in Firebase" and distributed under the
`FirebaseVertexAI` module. Firebase AI Logic was also formerly
distributed under the `FirebaseAI` module.*^

## Integrate without using Swift Package Manager

If you don't want to use Swift Package Manager, you can still take advantage of
the Firebase SDKs by using CocoaPods or by importing the frameworks directly.

### CocoaPods

Learn more about CocoaPods integration in
[our guide](https://firebase.google.com/docs/ios/installation-methods#cocoapods).

### Frameworks

In addition to supporting the iOS platform, the zip now includes `.xcframework`
files. For details, see [the Firebase
Apple platforms SDK README on
GitHub](https://github.com/firebase/firebase-ios-sdk#tvos-macos-watchos-and-catalyst)
.

1. Download the [framework SDK zip](https://firebase.google.com/download/ios). This is a \~200MB file and might take
   some time to download.

2. Unzip the file, and then integrate the frameworks that you want to include
   in your app.

   You can find integration instructions in either of the following places:
   - In the [Firebase iOS SDK GitHub repository](https://github.com/firebase/firebase-ios-sdk/blob/master/ReleaseTooling/Template/README.md).
   - In the `README.md` file within the downloaded zip distribution.

   For information regarding framework versions or dependencies, refer to the
   `METADATA.md` file within the downloaded zip distribution.
3. Add the
   [`-ObjC` linker flag](https://developer.apple.com/library/content/qa/qa1490/_index.html)
   in your `Other Linker Flags` in your target's build settings.

## Next steps

**Learn about Firebase:**

- Visit [Understand Firebase Projects](https://firebase.google.com/docs/projects/learn-more) to learn more
  about Firebase projects and best practices for projects.

- Explore [sample Firebase apps](https://firebase.google.com/docs/samples).

- Get hands-on experience with the [Firebase iOS
  Codelab](https://codelabs.developers.google.com/codelabs/firebase-ios-swift/).

- Explore the
  [open source code in GitHub](https://github.com/firebase/firebase-ios-sdk).

- Prepare to launch your app:

  - Set up [budget
    alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails) for your project in the Google Cloud console.
  - Monitor the [*Usage and billing*
    dashboard](https://console.firebase.google.com/project/_/usage) in the Firebase console to get an overall picture of your project's usage across multiple Firebase services.
  - Review the [Firebase launch checklist](https://firebase.google.com/support/guides/launch-checklist).
- Having trouble with Firebase and your Apple project?
  Visit the [Apple platforms troubleshooting \& FAQ](https://firebase.google.com/docs/ios/troubleshooting-faq).

**Add Firebase services to your app:**

- Build generative AI features with Gemini and Imagen models
  using [Firebase AI Logic](https://firebase.google.com/docs/ai-logic/get-started).

- Gain insights on user behavior with
  [Analytics](https://firebase.google.com/docs/analytics/ios/start).

- Set up user authentication with [Authentication](https://firebase.google.com/docs/auth/ios/start).

- Store data, like user information, with
  [Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart) or
  [Realtime Database](https://firebase.google.com/docs/database/ios/start).

- Store files, like photos and videos, with
  [Cloud Storage](https://firebase.google.com/docs/storage/ios/start).

- Trigger backend code that runs in a secure environment with
  [Cloud Functions](https://firebase.google.com/docs/functions/callable#call_the_function).

- Send notifications with
  [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/ios/client).

- Find out when and why your app is crashing with
  [Crashlytics](https://firebase.google.com/docs/crashlytics).