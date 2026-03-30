# Source: https://firebase.google.com/docs/cpp/learn-more.md.txt

As you're developing your C++ project using Firebase, you might discover
concepts that are unfamiliar or specific to Firebase. This page aims to answer
those questions or point you to resources to learn more.

Feel free to visit one of our online communities if you have questions about a
topic not covered on this page. We'll also update this page with new topics
periodically, so check back to see if we've added the topic you want to learn
about!

> [!NOTE]
> **Looking for how to get started with Firebase in
> your C++ projects? Check out our [Getting Started
> Guide](https://firebase.google.com/docs/cpp/setup).**

## Firebase library support by platform

The following table describes which Firebase libraries are compatible with which
platforms. Currently desktop support is intended for development purposes --
allowing you to test features on your development machine without deploying to a
phone or tablet if permitted by your toolchain.

| Platform | Android | iOS | tvOS | macOS *(beta)* | Windows *(beta)* | Linux *(beta)* |
|---|---|---|---|---|---|---|
| A/B Testing | Yes | Yes | v8.3.0+ |   |   |   |
| Analytics | Yes | Yes | v8.7.0+ |   |   |   |
| App Distribution | Yes | Yes | v8.3.0+ |   |   |   |
| Authentication | Yes | Yes | v8.3.0+ | Yes | Yes | Yes |
| Cloud Firestore | Yes | Yes | v8.3.0+ | Yes | Yes | Yes |
| Cloud Functions | Yes | Yes | v8.3.0+ | Yes | Yes | Yes |
| Cloud Messaging | Yes | Yes | v8.3.0+ |   |   |   |
| Cloud Storage | Yes | Yes | v8.3.0+ | Yes | Yes | Yes |
| Crashlytics | Yes | Yes | v8.3.0+ |   |   |   |
| Dynamic Links | Yes | Yes |   |   |   |   |
| Google Mobile Ads | Yes | Yes |   |   |   |   |
| Realtime Database | Yes | Yes | v8.3.0+ | Yes | Yes | Yes |
| Remote Config | Yes | Yes | v8.3.0+ | Yes | Yes | Yes |

> [!NOTE]
> **Note:** Crashlytics can detect and symbolicate C++ crashes on iOS, tvOS, and Android. To *customize* crash reports, though, you must use the [Apple platforms (iOS+) SDK](https://firebase.google.com/docs/crashlytics/ios/customize-crash-reports) or the [`crashlytics.h` header for Android](https://firebase.google.com/docs/crashlytics/android/get-started-ndk#customize-ndk-crash-reports).

## Google services -- config files

As part of adding Firebase to your C++ project, you need to add a Firebase
configuration file.

- To ship a C++ game on a mobile platform, follow the instructions for
  [Apple platforms (iOS+)](https://firebase.google.com/docs/ios/setup#add-config-file) and/or
  [Android](https://firebase.google.com/docs/android/setup#add-config-file) to include the appropriate
  Firebase configuration file in your project.

- To develop for desktop, you'll need to create a desktop version of the
  "mobile" Firebase configuration file:

  - If you added the Android `google-services.json` file --- When you run your
    app, Firebase locates this mobile file, then automatically generates a
    desktop Firebase config file (`google-services-desktop.json`).

  - If you added the Apple `GoogleService-Info.plist` file --- Before you run your
    app, you need to convert this mobile file to a desktop Firebase config file.
    To convert the file, run the following command from the same directory as
    your `GoogleService-Info.plist` file:

      generate_xml_from_google_services_json.py --plist -i GoogleService-Info.plist

  > [!NOTE]
  > **Note:** The desktop Firebase C++ SDK will search the current working directory first for `google-services-desktop.json` then for `google-services.json`. You can also [manually load](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1a54f8d0909118ba7937362f36a259d91c) a configuration or [create it in code](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#constructors-and-destructors).

If you want to use multiple Firebase projects in a single app, visit the
documentation for [configuring multiple
projects](https://firebase.google.com/docs/projects/multiprojects#use_multiple_projects_in_your_application).

> [!NOTE]
> **Note:** The Firebase configuration files contain unique, but non-secret identifiers for your project. To learn more about these config files, visit [Understand Firebase Projects](https://firebase.google.com/docs/projects/learn-more#config-files-objects).

## Open source resources for the Firebase C++ SDK

Firebase supports open source development, and we encourage contributions and
feedback.

### Firebase SDKs

The open source C++ SDKs are available in our [GitHub
repository](https://github.com/firebase/firebase-cpp-sdk).

Note the following about how we build the C++ SDKs for Firebase:

- The C++ SDKs for Windows, Linux, and macOS are entirely open source and hosted in our GitHub repo.
- The C++ SDKs for iOS, tvOS, and Android are built on top of the open source [iOS SDKs](https://github.com/firebase/firebase-ios-sdk) and [Android SDKs](https://github.com/firebase/firebase-android-sdk).

### Quickstart samples

Firebase maintains a collection of quickstart samples for Firebase APIs on
C++. Find these quickstarts in our public Firebase GitHub
[quickstart repository](https://github.com/firebase/quickstart-cpp/).

Each quickstart includes an Xcode project for iOS, an Android Studio project,
and a `CMakeLists.txt` file that can be used to generate a desktop project (if
the Firebase product itself supports
[desktop targets](https://firebase.google.com/docs/cpp/docs/cpp/setup#libraries-desktop)).