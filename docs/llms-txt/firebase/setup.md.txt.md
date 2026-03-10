# Source: https://firebase.google.com/docs/cpp/setup.md.txt

Power up your C++ games with our Firebase C++ SDKs which provide a C++
interface on top of Firebase SDKs.

Access Firebase entirely from your C++ code, without having to write any
platform-native code. The Firebase SDK also translates many language-specific
idioms used by Firebase into an interface more familiar to C++ developers.

**Find out more information about powering up your games with Firebase at our
[Firebase games page](https://firebase.google.com/games).**

> [!CAUTION]
> Learn which [Firebase products](https://firebase.google.com/docs/cpp/setup#available-libraries) the Firebase C++ SDK supports.

Already added Firebase to your C++ project? Make sure that you're using the
latest version of the [Firebase C++ SDK](https://firebase.google.com/download/cpp).

> [!NOTE]
> **Select a platform tab below to display platform-specific instructions
> in this guide.**
>
> *If you're releasing your game on both iOS and Android platforms:*
> You can register one build target of your C++ project now, then return to
> the setup workflow later to register the other build target, too.

<button value="ios" default="">iOS+</button> <button value="android">Android</button>

<br />

## Prerequisites

- Install the following:

  - Xcode 16.2 or later
  - CocoaPods 1.12.0 or later
- Make sure that your project targets the following platform versions or later:

  - iOS 15
  - tvOS 15
- Set up a physical device or use the simulator to run your app.

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

- [Sign into Firebase](https://console.firebase.google.com/) using your
  Google account.

## **Step 2**: Create a Firebase project

Before you can add Firebase to your C++ project, you need to create a Firebase
project to connect to your C++ project. Visit
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

## **Step 3**: Register your app with Firebase

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

## **Step 4**: Add the Firebase configuration file

1. Click **Download GoogleService-Info.plist** to obtain your Firebase Apple
   platforms config file.

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

2. Open your C++ project in an IDE, then drag your config file into the root
   of your C++ project.

3. If prompted, select to add the config file to all targets.

You're done with set up tasks in the Firebase console. Continue to
[Add Firebase C++ SDKs](https://firebase.google.com/docs/cpp/setup#add-sdks) below.

## **Step 5**: Add Firebase C++ SDKs

The steps in this section are an example of how to add
[supported Firebase products](https://firebase.google.com/docs/cpp/setup#libraries-ios) to your Firebase
C++ project.

> [!CAUTION]
> Each Firebase product has its own set of [dependencies](https://firebase.google.com/docs/cpp/setup#libraries-ios). Be sure to add all the listed dependencies for the desired Firebase product to your Podfile and C++ project.

1. Download the [Firebase C++ SDK](https://firebase.google.com/download/cpp), then unzip the SDK somewhere convenient.

   The Firebase C++ SDK is not platform-specific, but it does contain
   platform-specific libraries.
2. Add Firebase [pods](https://firebase.google.com/docs/cpp/setup#libraries-ios) from the unzipped SDK.

   1. Create a Podfile if you don't already have one:

      ```
      cd your-app-directory
      ```

      ```
      pod init
      ```

      <br />

   2. To your Podfile, add the Firebase pods that you want to use in your
      app.

      ### Analytics enabled

      ```c++
      # Add the Firebase pod for Google Analytics
      pod 'FirebaseAnalytics'

      # Add the pods for any other Firebase products you want to use in your app
      # For example, to use Firebase Authentication and Firebase Realtime Database
      pod 'FirebaseAuth'
      pod 'FirebaseDatabase'
      ```

      ### Analytics not enabled

      ```c++
      # Add the pods for the Firebase products you want to use in your app
      # For example, to use Firebase Authentication and Firebase Realtime Database
      pod 'FirebaseAuth'
      pod 'FirebaseDatabase'
      ```
   3. Install the pods, then open the `.xcworkspace` file in Xcode.

      ```
      pod install
      ```

      ```
      open your-app.xcworkspace
      ```

      <br />

3. Add Firebase [frameworks](https://firebase.google.com/docs/cpp/setup#libraries-ios) from the unzipped
   SDK.

   The easiest way to add these frameworks is usually to drag them from a
   `Finder` window directly into Xcode's *Project Navigator* pane (the
   far-left pane, by default; or click the file icon in the top-left of Xcode).
   1. Add the Firebase C++ framework `firebase.framework`, which is
      *required* to use any Firebase product.

   2. Add the framework for each Firebase product that you want to use. For
      example, to use Firebase Authentication, add `firebase_auth.framework`.

   > [!IMPORTANT]
   > **Important:** Make sure that you add the frameworks to **your** project and not to the *Pods* project!

4. Back in the Firebase console, in the setup workflow, click **Next**.

5. If you added Analytics, run your app to send verification to Firebase
   that you've successfully integrated Firebase. Otherwise, you can skip this
   verification step.

   Your device logs will display the Firebase verification that initialization
   is complete. If you ran your app on an emulator that has network access,
   the [Firebase console](https://console.firebase.google.com/) notifies you that your app connection is complete.

You're all set! Your C++ app is registered and configured to use Firebase
products.

> [!NOTE]
> **Note:** If you're also releasing your game on Android, return to your [Firebase project overview page](https://console.firebase.google.com/), then register the Android build target of your C++ project *with this same Firebase project* .  
> Find Android setup instructions on the [Android version of this setup page](https://firebase.google.com/docs/cpp/setup?platform=android).

## Available libraries

Learn more about the C++ Firebase libraries in the
[reference documentation](https://firebase.google.com/docs/reference/cpp) and in our open-source SDK
release on [GitHub](https://github.com/firebase/firebase-cpp-sdk).

### **Available libraries for Apple platforms**

**Note that C++ libraries for Android are listed on the [Android version of this
setup page](https://firebase.google.com/docs/cpp/setup?platform=android#libraries-android-cmake).**

Each Firebase product has different dependencies. Be sure to add all the
listed dependencies for the desired Firebase product to your Podfile and
C++ project.

Each Firebase product may only support a selection of Apple OS platforms (iOS,
tvOS, etc.). Check which platforms are supported by each library in
[Learn more about C++ and Firebase](https://firebase.google.com/docs/cpp/learn-more#library-support-by-platform).

> [!NOTE]
> You no longer need to add the iOS pod `Firebase/Core`. This SDK included the Firebase SDK for Google Analytics. Now, to use Analytics (or any of the Firebase products that require or recommend the use of Analytics), you need to explicitly add the Analytics pod: `Firebase/Analytics`.

| **Firebase product** | **Frameworks and Pods** |
|---|---|
| [AdMob](https://firebase.google.com/docs/admob/cpp/quick-start) | *(required)* `firebase.framework` `firebase_admob.framework` *(required)* `firebase_analytics.framework` `pod 'FirebaseAdMob', '12.10.0'` *(required)* `pod 'FirebaseAnalytics', '12.10.0'` |
| [Analytics](https://firebase.google.com/docs/analytics/cpp/start) | *(required)* `firebase.framework` `firebase_analytics.framework` `pod 'FirebaseAnalytics', '12.10.0'` |
| [App Check](https://firebase.google.com/docs/app-check) | *(required)* `firebase.framework` `firebase_app_check.framework` `pod 'FirebaseAppCheck', '12.10.0'` |
| [Authentication](https://firebase.google.com/docs/auth/cpp/start) | *(required)* `firebase.framework` `firebase_auth.framework` `pod 'FirebaseAuth', '12.10.0'` |
| [Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart) | *(required)* `firebase.framework` `firebase_firestore.framework` `firebase_auth.framework` `pod 'FirebaseFirestore', '12.10.0'` `pod 'FirebaseAuth', '12.10.0'` |
| [Cloud Functions](https://firebase.google.com/docs/functions/callable) | *(required)* `firebase.framework` `firebase_functions.framework` `pod 'FirebaseFunctions', '12.10.0'` |
| [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/cpp/client) | *(required)* `firebase.framework` `firebase_messaging.framework` *(recommended)* `firebase_analytics.framework` `pod 'FirebaseMessaging', '12.10.0'` *(recommended)* `pod 'FirebaseAnalytics', '12.10.0'` |
| [Cloud Storage](https://firebase.google.com/docs/storage/cpp/start) | *(required)* `firebase.framework` `firebase_storage.framework` `pod 'FirebaseStorage', '12.10.0'` |
| [Dynamic Links](https://firebase.google.com/docs/dynamic-links) | *(required)* `firebase.framework` `firebase_dynamic_links.framework` *(recommended)* `firebase_analytics.framework` `pod 'FirebaseDynamicLinks', '12.10.0'` *(recommended)* `pod 'FirebaseAnalytics', '12.10.0'` |
| [Realtime Database](https://firebase.google.com/docs/database/cpp/start) | *(required)* `firebase.framework` `firebase_database.framework` `pod 'FirebaseDatabase', '12.10.0'` |
| [Remote Config](https://firebase.google.com/docs/remote-config/get-started?platform=cpp) | *(required)* `firebase.framework` `firebase_remote_config.framework` *(recommended)* `firebase_analytics.framework` `pod 'FirebaseRemoteConfig', '12.10.0'` *(recommended)* `pod 'FirebaseAnalytics', '12.10.0'` |

## Additional information for mobile setup

### Method swizzling

On iOS, some application events (such as opening URLs and receiving
notifications) require your application delegate to implement specific
methods. For example, receiving a notification might require your application
delegate to implement `application:didReceiveRemoteNotification:`. Because
each iOS application has its own app delegate, Firebase uses
*method swizzling*, which allows the replacement of one method with another,
to attach its own handlers in addition to any that you might have implemented.

The Dynamic Links and Cloud Messaging libraries need
to attach handlers to the application delegate using method swizzling. If
you're using any of these Firebase products, at load time, Firebase will
identify your `AppDelegate` class and swizzle the required methods onto it,
chaining a call back to your existing method implementation.

## Set up a desktop workflow (**beta**)

> [!CAUTION]
> **Caution:** Firebase C++ SDK desktop support is a **beta** feature. This feature is intended only for workflows during the development of your game, not for publicly shipping code.

When you're creating a game, it's often much easier to test your game on desktop
platforms first, then deploy and test on mobile devices later in development. To
support this workflow, we provide a
[subset of the Firebase C++ SDKs](https://firebase.google.com/docs/cpp/setup#libraries-desktop) which can run on
Windows, macOS, Linux, and from within the C++ editor.

1. For desktop workflows, you need to complete the following:

   1. Configure your C++ project for CMake.
   2. [Create a Firebase project](https://firebase.google.com/docs/cpp/setup#create-firebase-project)
   3. [Register your app (iOS or Android) with Firebase](https://firebase.google.com/docs/cpp/setup#register-app)
   4. [Add a mobile-platform Firebase configuration file](https://firebase.google.com/docs/cpp/setup#add-config-file)
2. Create a *desktop* version of the Firebase configuration file:

   - **If you added the Android `google-services.json` file** --- When you run
     your app, Firebase locates this *mobile* file, then automatically
     generates a *desktop* Firebase config file
     (`google-services-desktop.json`).

   - **If you added the iOS `GoogleService-Info.plist` file** --- Before you run
     your app, you need to convert this *mobile* file to a *desktop* Firebase
     config file. To convert the file, run the following command from the same
     directory as your `GoogleService-Info.plist` file:

     <br />

     ```
     generate_xml_from_google_services_json.py --plist -i GoogleService-Info.plist
     ```

     <br />

   This desktop config file contains the C++ project ID that you entered in
   the Firebase console setup workflow. Visit
   [Understand Firebase Projects](https://firebase.google.com/docs/projects/learn-more#config-files-objects)
   to learn more about config files.
3. Add Firebase SDKs to your C++ project.

   The steps below serve as an example of how to add any
   [supported Firebase product](https://firebase.google.com/docs/cpp/setup#libraries-desktop) to
   your C++ project. In this example, we walk through adding
   Firebase Authentication and Firebase Realtime Database.
   1. Set your `FIREBASE_CPP_SDK_DIR` environment variable to the location of
      the unzipped Firebase C++ SDK.

   2. To your project's `CMakeLists.txt` file, add the following content,
      including the [libraries](https://firebase.google.com/docs/cpp/setup#libraries-desktop) for
      the Firebase products that you want to use. For example, to use
      Firebase Authentication and Firebase Realtime Database:

      ```c++
      # Add Firebase libraries to the target using the function from the SDK.
      add_subdirectory(${FIREBASE_CPP_SDK_DIR} bin/ EXCLUDE_FROM_ALL)

      # The Firebase C++ library `firebase_app` is required,
      # and it must always be listed last.

      # Add the Firebase SDKs for the products you want to use in your app
      # For example, to use Firebase Authentication and Firebase Realtime Database
      set(firebase_libs firebase_auth firebase_database firebase_app)
      target_link_libraries(${target_name} "${firebase_libs}")
      ```
4. Run your C++ app.

### Available libraries (desktop)

The Firebase C++ SDK includes [desktop workflow support](https://firebase.google.com/docs/cpp/setup#desktop-workflow)
for a subset of features, enabling certain parts of Firebase to be used in
standalone desktop builds on Windows, macOS, and Linux.

> [!CAUTION]
> **Caution:** Firebase C++ SDK desktop support is a **beta** feature. This feature is intended only for workflows during the development of your game, not for publicly shipping code.

| **Firebase product** | **Library references (using CMake)** |
|---|---|
| [App Check](https://firebase.google.com/docs/app-check) | `firebase_app_check` *(required)* `firebase_app` |
| [Authentication](https://firebase.google.com/docs/auth/cpp/start) | `firebase_auth` *(required)* `firebase_app` |
| [Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart) | `firebase_firestore` `firebase_auth` `firebase_app` |
| [Cloud Functions](https://firebase.google.com/docs/functions/callable) | `firebase_functions` *(required)* `firebase_app` |
| [Cloud Storage](https://firebase.google.com/docs/storage/cpp/start) | `firebase_storage` *(required)* `firebase_app` |
| [Realtime Database](https://firebase.google.com/docs/database/cpp/start) | `firebase_database` *(required)* `firebase_app` |
| [Remote Config](https://firebase.google.com/docs/remote-config/get-started?platform=cpp) | `firebase_remote_config` *(required)* `firebase_app` |

Firebase provides the remaining desktop libraries as stub (non-functional)
implementations for convenience when building for Windows, macOS, and Linux.
Therefore, you don't need to conditionally compile code to target the desktop.

#### Realtime Database desktop

The Realtime Database SDK for desktop uses REST to access your database, so you must
[declare the indexes](https://firebase.google.com/docs/database/security#section-defining-indexes) that
you use with `Query::OrderByChild()` on desktop or your listeners will fail.

### Additional information for desktop setup

#### Windows libraries

For Windows, library versions are provided based on the following:

- Build platform: 32-bit (x86) vs 64-bit (x64) mode
- Windows runtime environment: Multithreaded / MT vs Multithreaded DLL /MD
- Target: Release vs Debug

Note that the following libraries were tested using Visual Studio 2015 and 2017.

When building C++ desktop apps on Windows, link the following Windows SDK
libraries to your project. Consult your compiler documentation for more
information.

| Firebase C++ Library | Windows SDK library dependencies |
|---|---|
| App Check | `advapi32, ws2_32, crypt32` |
| Authentication | `advapi32, ws2_32, crypt32` |
| Cloud Firestore | `advapi32, ws2_32, crypt32, rpcrt4, ole32, shell32` |
| Cloud Functions | `advapi32, ws2_32, crypt32, rpcrt4, ole32` |
| Cloud Storage | `advapi32, ws2_32, crypt32` |
| Realtime Database | `advapi32, ws2_32, crypt32, iphlpapi, psapi, userenv` |
| Remote Config | `advapi32, ws2_32, crypt32, rpcrt4, ole32` |

#### macOS libraries

For macOS (Darwin), library versions are provided for the 64-bit (x86_64)
platform. Frameworks are also provided for your convenience.

Note that the macOS libraries have been tested using Xcode
16.2.

When building C++ desktop apps on macOS, link the following to your project:

- `pthread` system library
- `CoreFoundation` macOS system framework
- `Foundation` macOS system framework
- `Security` macOS system framework
- `GSS` macOS system framework
- `Kerberos` macOS system framework
- `SystemConfiguration` macOS system framework

Consult your compiler documentation for more information.

#### Linux libraries

For Linux, library versions are provided for 32-bit (i386) and 64-bit (x86_64)
platforms.

Note that the Linux libraries were tested using GCC 4.8.0, GCC 7.2.0, and
Clang 5.0 on Ubuntu.

When building C++ desktop apps on Linux, link the `pthread` system library to
your project. Consult your compiler documentation for more information. If
you're building with GCC 5 or later, define `-D_GLIBCXX_USE_CXX11_ABI=0`.

## Next steps

- Explore [sample Firebase apps](https://firebase.google.com/docs/samples).

- Explore the [open source SDK in
  GitHub](https://github.com/firebase/firebase-cpp-sdk).

- Prepare to launch your app:

  - Set up [budget
    alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails) for your project in the Google Cloud console.
  - Monitor the [*Usage and billing*
    dashboard](https://console.firebase.google.com/project/_/usage) in the Firebase console to get an overall picture of your project's usage across multiple Firebase services.
  - Review the [Firebase launch checklist](https://firebase.google.com/support/guides/launch-checklist).