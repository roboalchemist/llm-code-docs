# Source: https://firebase.google.com/docs/test-lab.md.txt

# Firebase Test Lab

plat_iosplat_android  
Test your app on devices hosted in a Google data center.  

Firebase Test Labis a cloud-based app testing infrastructure that lets you test your app on a range of devices and configurations, so you can get a better idea of how it'll perform in the hands of live users.

[Run a test](https://console.firebase.google.com/project/_/testlab/histories/)

For instructions about running tests withTest Lab, visit our Getting Started guides:

[iOS+](https://firebase.google.com/docs/test-lab/ios/get-started)[Android](https://firebase.google.com/docs/test-lab/android/get-started)

## Key capabilities

|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Test both Android and iOS apps | Run tests on a wide range of Android and iOS devices hosted byTest Lab, including virtual Android test devices that run on faster Arm hosts.                        |
| Run on real devices            | Test Labexercises your app on devices installed and running in a Google data center, so you can find issues that only occur on specific devices and configurations. |
| Workflow integration           | Test Labis integrated with theFirebaseconsole, Android Studio, and the gcloud CLI. You can also use it with Continuous Integration (CI) systems.                    |

## How does it work?

Test Labuses real, production devices running in a Google data center to test your app. The devices are flashed with updated APIs and have customizable locale settings, allowing you to road-test your app on the hardware and configurations it'll encounter in real-world use.
| **Note:** Test Labis not intended for, and should not be used for, load-testing any back-end servers used by your app.

## Overview of implementation path

|---|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | Get your app ready for testing        | - First, choose a test to run: - Instrumentation test for[Android](https://firebase.google.com/docs/test-lab/android/instrumentation-test) - Robo test for[Android](https://firebase.google.com/docs/test-lab/android/robo-ux-test)(does not require a pre-written test) - Game Loop test for[iOS](https://firebase.google.com/docs/test-lab/ios/run-game-loop-test)and[Android](https://firebase.google.com/docs/test-lab/android/game-loop) - XCTest for[iOS](https://firebase.google.com/docs/test-lab/ios/run-xctest) - If necessary, modify your test to run onTest Lab. Build and package your app, then upload it to Firebase. |
|   | Choose test devices and a test matrix | Using one of our integrated tools, define your test matrix by selecting a set of devices, OS versions, locales, and screen orientations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|   | Run your test and review test results | Run your test using our available tools. Depending on the size of your test matrix, it can take several minutes forTest Labto run your tests. After your tests finish, you can see the results in theFirebaseconsole.                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Next steps

- Visit an overview of how to get started:[iOS](https://firebase.google.com/docs/test-lab/ios/get-started),[Android](https://firebase.google.com/docs/test-lab/android/get-started)

- Test your app with theFirebaseconsole:[iOS](https://firebase.google.com/docs/test-lab/ios/firebase-console),[Android](https://firebase.google.com/docs/test-lab/android/firebase-console)

- Test your app with the gcloud CLI:[iOS](https://firebase.google.com/docs/test-lab/ios/command-line),[Android guide](https://firebase.google.com/docs/test-lab/android/command-line)

- Test your app with Android Studio 2.0+:[Android codelab](https://codelabs.developers.google.com/codelabs/firebase-android/)

- Visit[frequently-asked questions](https://firebase.google.com/docs/test-lab/troubleshooting)

- Learn how Google accelerates mobile development and helps developers build better performing, more stable apps:[Mobile Applications On-Device Testing at Google scale](https://research.google/pubs/pub51331/)