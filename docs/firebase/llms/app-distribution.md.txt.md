# Source: https://firebase.google.com/docs/app-distribution.md.txt

# Firebase App Distribution

[Video](https://www.youtube.com/watch?v=SiPOaV-5j9o)

Firebase App Distribution makes distributing your apps to trusted testers painless.
By getting your apps onto testers' devices quickly, you can get feedback early
and often. And if you use Crashlytics in your apps, you'll automatically
get stability metrics for all your builds, so you know when you're ready to
ship.

<br />

Ready to get started?

Learn how to distribute your iOS apps:

[Firebase console](https://firebase.google.com/docs/app-distribution/ios/distribute-console)
[Firebase CLI](https://firebase.google.com/docs/app-distribution/ios/distribute-cli)
[fastlane](https://firebase.google.com/docs/app-distribution/ios/distribute-fastlane)

[REST API](https://firebase.google.com/docs/reference/app-distribution/rest)

Learn how to distribute your Android apps:

[Firebase console](https://firebase.google.com/docs/app-distribution/android/distribute-console)
[Firebase CLI](https://firebase.google.com/docs/app-distribution/android/distribute-cli)
[fastlane](https://firebase.google.com/docs/app-distribution/android/distribute-fastlane)
[Gradle](https://firebase.google.com/docs/app-distribution/android/distribute-gradle)
[REST API](https://firebase.google.com/docs/reference/app-distribution/rest)

## Key capabilities

|---|---|
| Cross-platform | Manage both your iOS and Android pre-release distributions from the same place. |
| Fast distributions | Get early releases into your testers' hands quickly, with fast onboarding, no SDK to install, and instant app delivery. |
| Fits into your workflow | Distribute builds using the Firebase console, the Firebase Command Line Interface (CLI) tool, fastlane, or Gradle (Android). Automate distribution by integrating the CLI into continuous integration (CI) jobs. |
| Tester management | Manage your testing teams by organizing them into groups. Easily add new testers with email invitations that walk them through the onboarding process. View the status of each tester for specific versions of your app, which indicates who has accepted a testing invitation and downloaded the app. Enable in-app feedback to make it easier to collect feedback on your pre-release apps from testers. |
| Works with Android App Bundles | Distribute releases to testers for your Android App Bundle in Google Play. App Distribution integrates with Google Play's internal app sharing service to streamline your app testing and launching processes. |
| Works with Crashlytics | When combined with Crashlytics, get insights into the stability of your test distributions. |

## Example implementation path

|---|---|---|
|   | Upload your latest pre-release build | First, upload your latest APK, AAB, or IPA to App Distribution using the Firebase console, fastlane, Gradle, or the CLI tools. |
|   | Invite testers | Then, add the testers you want to try your app. Testers will receive an email that walks them through the onboarding process. |
|   | Get feedback | Get feedback from your testers, monitor stability data, and iterate on your app. |
|   | Release new beta builds | Whenever you have a new build ready for testing, just upload it to App Distribution. Your testers will be notified that a new build is available to try out. |

## Next steps

Learn best practices

- [Best practices for distributing Apple apps to QA testers using CI/CD and fastlane](https://firebase.google.com/docs/app-distribution/best-practices-distributing-apple-apps-to-qa-testers-with-ci-cd-fastlane)
- [Best practices for distributing Android apps to QA testers using CI/CD](https://firebase.google.com/docs/app-distribution/best-practices-distributing-android-apps-to-qa-testers-with-ci-cd)

Learn how to distribute your iOS apps:

[Firebase console](https://firebase.google.com/docs/app-distribution/ios/distribute-console)
[Firebase CLI](https://firebase.google.com/docs/app-distribution/ios/distribute-cli)
[fastlane](https://firebase.google.com/docs/app-distribution/ios/distribute-fastlane)
[REST API](https://firebase.google.com/docs/reference/app-distribution/rest)

Learn how to distribute your Android apps:

[Firebase console](https://firebase.google.com/docs/app-distribution/android/distribute-console)
[Firebase CLI](https://firebase.google.com/docs/app-distribution/android/distribute-cli)
[fastlane](https://firebase.google.com/docs/app-distribution/android/distribute-fastlane)
[Gradle](https://firebase.google.com/docs/app-distribution/android/distribute-gradle)
[REST API](https://firebase.google.com/docs/reference/app-distribution/rest)

To learn more about App Distribution, check out the following codelabs:

- [Distribute app bundle releases to testers](https://firebase.google.com/codelabs/appdistribution-app-bundles).

- [Alert testers about your new app releases with Firebase App Distribution Android SDK](https://firebase.google.com/codelabs/appdistribution-android).

- [Alert testers about your new app releases with the Firebase App Distribution iOS SDK](https://firebase.google.com/codelabs/appdistribution-ios).

- [Distribute your pre-release iOS builds faster with App Distribution and fastlane](https://firebase.google.com/codelabs/appdistribution-udid-collection).