# Source: https://firebase.google.com/docs/app-distribution/best-practices-distributing-android-apps-to-qa-testers-with-ci-cd.md.txt

<br />

This document introduces best practices for usingFirebase App Distributionto make your Android pre-release testing workflows sustainable and repeatable in a CI/CD environment. Solutions include Gradle and fastlane, but to give you even more flexibility we also include solutions available through theFirebaseconsole, theFirebaseCLI, and the public FirebaseApp DistributionAPI. We also describe release and tester limits so you can plan in advance for an optimal experience.

If you're also using Apple platforms, see[Best practices for distributing Apple apps to QA testers using CI/CD and fastlane](https://firebase.google.com/docs/app-distribution/best-practices-distributing-apple-apps-to-qa-testers-with-ci-cd-fastlane).

## Before you begin

Before you implement the best practices in this document, be sure to enableApp Distributionin theFirebaseconsole*for each app* . If you haven't enabledApp Distribution, you'll get a 404 error.

To enableApp Distribution, follow these steps:

1. Open the[App Distributionpage](https://console.firebase.google.com/project/_/appdistribution)in theFirebaseconsole.
2. Select your Android app.
3. Click**Get Started**.

Given that Android App Bundles (AAB) are becoming the most common Android package format, we recommend that you set up the ability to distribute AABs to your testers by[linking toGoogle Play](https://firebase.google.com/docs/app-distribution/android/distribute-console?apptype=aab#before-you-begin).

## Automate your pre-release testing workflow using a CI/CD pipeline

If you want to automate building and releasing apps to your testers and you're using CI/CD, we recommend that you use[fastlane](https://fastlane.tools/)or[Gradle](https://gradle.org/). Another option is to use the[FirebaseCLI](https://firebase.google.com/docs/app-distribution/android/distribute-cli?apptype=aab), which lets you access a wide array of Firebase products.

### Use fastlane

IntegrateApp Distributioninto your CI/CD pipeline using fastlane, an open source tool that automates building and releasing iOS and Android apps. By building and distributing your latest releases to testers automatically, you ensure testers always have the most up-to-date test version of your app.

To learn how to integrateApp Distributionwith fastlane, see[Distribute Android apps to testers using fastlane](https://firebase.google.com/docs/app-distribution/android/distribute-fastlane?apptype=aab).

### Use Gradle

Use Gradle to integrateApp Distributioninto your Android build process using theApp DistributionGradle plugin. The plugin lets you specify your testers and release notes in your app's`build.gradle`file, which enables you to configure distributions for different build types and variants of your app.

To learn how to integrateApp Distributionwith Gradle, see[Distribute Android apps to testers using Gradle](https://firebase.google.com/docs/app-distribution/android/distribute-gradle).

### Use theFirebaseCLI

Use theFirebaseCLI tools thatApp Distributionprovides to distribute builds to testers programmatically. You can specify testers and release notes for a build.

Distribute your latest Android build by specifying the app's Firebase App ID, optionally adding a release note and a file containing testers' emails:  

    firebase appdistribution:distribute test.aab  \
        --app 1:1234567890:android:0a1b2c3d4e5f67890  \
        --release-notes "Bug fixes and improvements" --testers-file testers.txt

To learn more about using theFirebaseCLI to automate your builds, see[Distribute Android apps to testers using theFirebaseCLI](https://firebase.google.com/docs/app-distribution/android/distribute-cli).

### Use service credentials to authenticate

Use theApp Distribution[fastlane plugin](https://firebase.google.com/docs/app-distribution/android/distribute-fastlane#authenticate), the[Gradle plugin](https://firebase.google.com/docs/app-distribution/android/distribute-gradle#authenticate), or theFirebaseCLI with service accounts. A[*service account*](https://cloud.google.com/docs/authentication#service-accounts)is a type of Google account that represents applications (as opposed to users). Your CI system can use service accounts to run yourApp Distributionworkloads. To learn more, see[Authenticate with a service account](https://firebase.google.com/docs/app-distribution/authenticate-service-account?platform=android).

If you're using workload identity federation, you can generate and use a[credential configuration file](https://cloud.google.com/iam/docs/using-workload-identity-federation#generate-automatic)instead of a service account key.

### Keep in mind release limits

App Distributionsupports a maximum of 1,000 releases per app. This means that when you exceed the release limit,App Distributionautomatically deletes the oldest releases above the limit. To learn how to manage release limits, see[How long are app releases available?](https://firebase.google.com/docs/app-distribution/troubleshooting?platform=ios#builds-expire-ios)

## Add the same set of testers to multiple releases

If you want to add large numbers of testers to your releases, useApp Distribution's bulk tester management functionality.

We recommend that you use groups to add the same testers to multiple releases. A*group* acts as an access control list; when you remove a tester from a group, they lose access to all of the releases distributed to that group. To learn more, see[Add and remove testers from a group](https://firebase.google.com/docs/app-distribution/add-remove-testers?platform=android#add-remove-testers-group).

If you have a lot of testers to manage, you can[bulk add and delete testers](https://firebase.google.com/docs/app-distribution/import-testers-csv-files)using theFirebaseconsole. To automate adding and removing testers, use the[FirebaseCLI](https://firebase.google.com/docs/app-distribution/android/distribute-cli?apptype=aab#step_2_distribute_your_app_to_testers),[fastlane](https://firebase.google.com/docs/app-distribution/android/distribute-fastlane?apptype=aab#manage),[Gradle](https://firebase.google.com/docs/app-distribution/android/distribute-gradle?apptype=aab#step_4_distribute_your_app_to_testers), or the[public FirebaseApp DistributionAPI](https://firebase.google.com/docs/app-distribution/add-remove-testers?platform=android#add-remove-testers-api).

### Keep in mind tester limits

App Distributionlimits the number of testers you can add to a Firebase project or anApp Distributiongroup. When you exceed these limits, you won't be able to distribute your app to additional testers. To learn more about tester limits, see[Are there limits for adding testers to my app?](https://firebase.google.com/docs/app-distribution/troubleshooting#tester-limits)

## Enable potential testers to self-register for testing

To make it easier to distribute your app to more testers, we recommend that you use invite links. An*invite link*is a unique URL that lets testers enter their email addresses to sign up to test an app. Enabling users to add themselves to your list of app testers is a seamless way to increase your internal testing base.

Invite links use cases include company dogfood programs, organizations with large QA teams, and developer groups who want individual clients to be able to control tester access.

We recommend that you create an invite link for a group. Any tester who signs up using the invite link is automatically added to subsequent releases.

To learn more, see[Create invite links](https://firebase.google.com/docs/app-distribution/create-invite-links)and[Add and remove testers from a group](https://firebase.google.com/docs/app-distribution/add-remove-testers#add-remove-testers-group).

## Make sure that testers are testing the version you care about

When a new version is uploaded, your testers are notified by email. To supplement this notification, you can use the following features -- release links and in-app alerts -- to make sure that your testers are testing the specific app version you care about:

- **Release links:** Use this feature when you want to share a specific version with testers. To learn how to use release links, see[Distribute Android apps to testers using theFirebaseconsole](https://firebase.google.com/docs/app-distribution/android/distribute-console?apptype=aab#step_2_distribute_your_app_to_testers). These links are also available with our[Firebase](https://firebase.google.com/docs/app-distribution/android/distribute-cli),[fastlane](https://firebase.google.com/docs/app-distribution/android/distribute-fastlane), and[Gradle](https://firebase.google.com/docs/app-distribution/android/distribute-gradle)command-line (CLI) tools for use with your build automation tools.
- **In-app alerts:** Use these alerts when you want to ensure that your testers are testing the latest version of your app. By integrating the FirebaseApp DistributionAndroid SDK, you can display alerts directly inside the app to your testers when new builds of your app are available. To learn how to add in-app alerts, see[Notify testers about new builds](https://firebase.google.com/docs/app-distribution/set-up-alerts).

## Automatically remove access for testers who leave the company

When your CI/CD internal testing flow is up and running, you need to make sure that people who leave the company no longer have access to your internal builds. To help you manage tester access to builds,App Distributionprovides the following options:

- **fastlane:** Use your Fastfile file or directly run fastlane actions. To learn more, see[Distribute Android apps to testers using fastlane](https://firebase.google.com/docs/app-distribution/android/distribute-fastlane?apptype=aab#manage).
- **FirebaseCLI:** Use the`firebase appdistribution:testers:remove`action. To learn more, see[Distribute Android apps to testers using theFirebaseCLI](https://firebase.google.com/docs/app-distribution/android/distribute-cli?apptype=aab#step_2_distribute_your_app_to_testers).
- **Gradle:** If you're using Gradle to remove testers, pass`appDistributionRemoveTesters`with the arguments--<var translate="no">PROJECT_NUMBER</var>and--<var translate="no">EMAILS</var>in your`build.gradle`file. To learn more, see[Distribute Android apps to testers using Gradle](https://firebase.google.com/docs/app-distribution/android/distribute-gradle?apptype=aab#step_4_distribute_your_app_to_testers).
- **Public[FirebaseApp DistributionAPI](https://firebase.google.com/docs/reference/app-distribution/rest):** Use the`testers.batchRemove`endpoint.