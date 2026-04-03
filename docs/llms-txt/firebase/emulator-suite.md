# Source: https://firebase.google.com/docs/reference/emulator-suite.md.txt

# Source: https://firebase.google.com/docs/emulator-suite.md.txt

# Introduction to Firebase Local Emulator Suite

The Firebase Local Emulator Suite is a set of advanced tools for developers
looking to build and test apps locally using Cloud Firestore, Realtime Database,
Cloud Storage for Firebase, Authentication, Firebase Hosting, Cloud Functions (beta),
Pub/Sub (beta), and Firebase Extensions (beta). It provides a rich
user interface to help you get running and prototyping quickly.

Local development with Local Emulator Suite can be a good fit for your
evaluation, prototyping, development and continuous integration workflows.


![Adding Firebase Emulator Suite to your development workflows.](https://firebase.google.com/docs/images/emulator-suite-usecase.png)

## Before you begin

Before you explore Firebase Local Emulator Suite, we recommend you get oriented
to Firebase products and the Firebase development model:

- Read the **Get started with Firebase** topics for your platform and products ([Apple](https://firebase.google.com/docs/ios/setup), [Android](https://firebase.google.com/docs/android/setup) or [Web](https://firebase.google.com/docs/web/setup)).
- Download a ready-to-run quickstart app on your platform of choice, then read through and execute the code. The FriendlyEats quickstart app is a good choice ([iOS](https://github.com/firebase/friendlyeats-ios), [Android](https://github.com/firebase/friendlyeats-android) or [Web](https://github.com/firebase/friendlyeats-web)).

## What is Firebase Local Emulator Suite?

The Firebase Local Emulator Suite consists of individual service
emulators built to accurately mimic the behavior of Firebase services. This
means you can connect your app directly to these emulators to perform
integration testing or QA without touching production data.

For example, you could connect your app to the Cloud Firestore emulator to
safely read and write documents in testing. These writes may trigger functions
in the Cloud Functions emulator. However your app will still continue to
communicate with production Firebase services when emulators are not available
or configured.

![](https://firebase.google.com/docs/images/emulator_suite_block.png)
| **Note:** Do not attempt to use these emulators as "self-hosted" versions of Firebase services. They are built for accuracy, not performance or security, and are not appropriate to use in production.

### Emulator Suite in your local workflows

Your prototype and test workflow can make use of the Local Emulator Suite in
several ways:

- **Unit Tests**: using the Firebase Test SDK, you can write unit tests in Node.js using the mocha test runner. The Test SDK provides several convenience methods for loading Security Rules, flushing the local database between tests, and managing synchronous interaction with the emulators. It's great for writing simple tests for database interactions that don't depend on your app's logic.
- **Integration Tests** : each individual product emulator in the Emulator Suite responds to SDK and REST API calls just like production Firebase services. So you can use your own testing tools to write self-contained integration tests that use the Local Emulator Suite as the backend.
- **Manual Tests** : you can connect your running application to the Local Emulator Suite to test your Firebase app manually, without risking production data or configuring a test project.
- **Product Evaluations** : you can install and manage Firebase Extensions in a safe local environment and better understand their capabilities while minimizing billing costs.

### Which Firebase features and platforms are supported?

The Firebase Local Emulator Suite allows you to test your code with our core
products in an interoperable way. The Cloud Functions emulator supports
HTTP functions, callable functions, and background functions
triggered by Cloud Firestore, Realtime Database, Cloud Storage for Firebase, Authentication,
and Pub/Sub. The Cloud Firestore, Realtime Database, and
Cloud Storage for Firebase emulators have Firebase Security Rules emulation built in.

|                       |                            **Cloud Firestore**                            |                           **Realtime Database**                           |                      **Cloud Storage for Firebase**                       |                            **Authentication**                             |                            **Cloud Functions**                            |                             **Cloud Pub/Sub**                             | **Extensions** |
|-----------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|----------------|
| **Android SDK**       | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | n/a                                                                       | n/a            |
| **iOS SDK**           | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | n/a                                                                       | n/a            |
| **Web SDK**           | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | n/a                                                                       | n/a            |
| **Node.js Admin SDK** | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | n/a                                                                       | ![](https://firebase.google.com/docs/images/baseline_done_black_18dp.png) | n/a            |

## Next steps

- [Get started](https://firebase.google.com/docs/emulator-suite/connect_and_prototype) with a
  Local Emulator Suite walkthrough that shows how you can do offline
  prototyping of a database and Cloud Functions.

- Learn how to [install and configure Local Emulator Suite](https://firebase.google.com/docs/emulator-suite/install_and_configure).

## Other tools for prototyping and testing

The Emulator Suite is supplemented by other prototype and test tools.

**Cloud Functions testing tools.** The Firebase CLI environment provides you
several ways to prototype and test functions:

- The Cloud Functions emulator, part of the Emulator Suite. This emulator is interoperable with local, live data and Security Rules in the Firestore emulator and/or Realtime Database emulator.
- The Cloud Functions shell, which allows for interactive, iterative functions prototyping and development. The shell employs the Cloud Functions emulator with a REPL-style interface for development. No integration with the Cloud Firestore or Realtime Database emulators is provided. Using the shell, you mock data and perform function calls to simulate interaction with products that the Local Emulator Suite does not currently support: Analytics, Remote Config, and Crashlytics.
- The Firebase Test SDK for Cloud Functions, a Node.js with mocha framework for functions development. In effect, the Cloud Functions Test SDK provides automation atop the Cloud Functions shell.

You can find more about the Cloud Functions shell and Cloud Functions Test SDK
at [Test functions interactively](https://firebase.google.com/docs/functions/local-shell) and
[Unit testing of Cloud Functions](https://firebase.google.com/docs/functions/unit-testing).

**Security Rules testing tools.** Emulator Suite is the preferred toolset for
testing Security Rules. However, you can also use:

- The Rules Playground, a part of the Firebase console. The Rules Playground provides a great interactive getting started experience with Security Rules design. For more information see [Quickly validate Firebase Security Rules](https://firebase.google.com/docs/rules/simulator).