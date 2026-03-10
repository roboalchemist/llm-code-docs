# Source: https://firebase.google.com/docs/app-distribution/best-practices-distributing-apple-apps-to-qa-testers-with-ci-cd-fastlane.md.txt

This document introduces best practices for using Firebase App Distribution and
fastlane to make your Apple platform pre-release testing workflows sustainable
and repeatable in a CI/CD environment. While this document focuses on fastlane,
we also describe solutions available through the Firebase console, the
Firebase CLI, and the public Firebase App Distribution API to give you
more flexibility. We also describe release and tester limits so you can plan in
advance for an optimal experience.

If you're also using Android, see
[Best practices for distributing Android apps to QA testers using CI/CD](https://firebase.google.com/docs/app-distribution/best-practices-distributing-android-apps-to-qa-testers-with-ci-cd).

## Before you begin

Before you implement the best practices in this document, be sure to enable
App Distribution in the Firebase console *for each app* . If you haven't enabled
App Distribution, you'll get a 404 error.

To enable App Distribution, follow these steps:

1. Open the [App Distribution page](https://console.firebase.google.com/project/_/appdistribution)
   in the Firebase console.

2. Select your iOS app.

3. Click **Get Started**.

## Automate your pre-release testing workflow using CI/CD

If you want to automate building and releasing apps to your testers and
you're using CI/CD, we recommend that you use
[fastlane](https://fastlane.tools/). Another option is to use the
Firebase CLI, which lets you access a wide array of Firebase products.

### Use fastlane

Integrate App Distribution into your CI/CD pipeline using fastlane, an open
source tool that automates building and releasing iOS and Android apps. By
building and distributing your latest releases to testers automatically, you
ensure testers always have the most up-to-date test version of your app.

To learn how to integrate App Distribution with fastlane, see
[Distribute iOS apps to testers using fastlane](https://firebase.google.com/docs/app-distribution/ios/distribute-fastlane).
See also a [codelab](https://firebase.google.com/codelabs/appdistribution-udid-collection#0)
that walks you through the fastlane integration process.

### Use the Firebase CLI

Use the Firebase CLI tools that App Distribution provides to distribute
builds to testers programmatically. You can specify testers and release notes
for a build.

Distribute your latest iOS build `test.ipa` by specifying the app's
Firebase App ID, optionally adding a release note and a file containing
testers' emails:

```bash
firebase appdistribution:distribute test.ipa  \
    --app 1:1234567890:ios:0a1b2c3d4e5f67890  \
    --release-notes "Bug fixes and improvements" --testers-file testers.txt
```

To learn more about using the Firebase CLI to automate your builds, see
[Distribute iOS apps to testers using the Firebase CLI](https://firebase.google.com/docs/app-distribution/ios/distribute-cli).

### Use service credentials to authenticate

Use the App Distribution [fastlane plugin](https://firebase.google.com/docs/app-distribution/ios/distribute-fastlane#authenticate)
or the Firebase CLI with service accounts, which take advantage of
[Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials)
and help you manage your CI. A [service account](https://cloud.google.com/docs/authentication#service-accounts)
is a type of Google account that represents applications as opposed to users.
Your CI system can use service accounts to run your App Distribution workloads.
To learn more, see [Authenticate with a service account](https://firebase.google.com/docs/app-distribution/authenticate-service-account?platform=ios).

If you're using workload identity federation, you can generate and use a
[credential configuration file](https://cloud.google.com/iam/docs/using-workload-identity-federation#generate-automatic)
instead of a service account key.

### Keep in mind release limits

App Distribution supports a maximum of 1,000 releases per app. This means that
when you exceed the release limit, App Distribution automatically deletes the
oldest releases above the limit. To learn how to manage release limits, see
[How long are app releases available?](https://firebase.google.com/docs/app-distribution/troubleshooting?platform=ios#builds-expire-ios)

## Add the same set of testers to multiple releases

If you want to add large numbers of testers to your releases, use
App Distribution's bulk tester management functionality.

We recommend that you use groups to add the same testers to multiple releases.
A *group* acts as an access control list; when you remove a tester from a group,
they lose access to all of the releases distributed to that group. To learn
more, see [Add and remove testers from a group](https://firebase.google.com/docs/app-distribution/add-remove-testers?platform=ios#add-remove-testers-group).

If you have a lot of testers to manage, you can [bulk add and delete testers](https://firebase.google.com/docs/app-distribution/import-testers-csv-files)
using the Firebase console. To automate adding and removing testers, use
the [Firebase CLI](https://firebase.google.com/docs/app-distribution/ios/distribute-cli),
[fastlane](https://firebase.google.com/docs/app-distribution/ios/distribute-fastlane?apptype=aab#manage),
or the [public Firebase App Distribution API](https://firebase.google.com/docs/app-distribution/add-remove-testers?platform=ios#add-remove-testers-api).

### Keep in mind tester limits

App Distribution limits the number of testers you can add to a Firebase project
or an App Distribution group. When you exceed these limits, you won't be able to
distribute your app to additional testers. To learn more about tester limits,
see [Are there limits for adding testers to my app?](https://firebase.google.com/docs/app-distribution/troubleshooting#tester-limits)

## Manage and automatically add new iOS tester devices

To help you register additional iOS tester devices, App Distribution helps you
manage your iOS tester devices in the Apple Developer Portal by informing you
about new tester iOS devices via email or CSV files. To learn more, see
[Import testers from CSV files](https://firebase.google.com/docs/app-distribution/import-testers-csv-files).
You can also programmatically [export new devices using fastlane](https://firebase.google.com/docs/app-distribution/register-additional-devices#programmatic-export-udids).

To learn how to set up a fastlane action that automatically pulls down
UDIDs, adds them to the Apple developer console, and then rebuilds the app and
distributes it, see [Distribute your pre-release iOS builds faster with App Distribution and fastlane](https://firebase.google.com/codelabs/appdistribution-udid-collection#0).

## Enable potential testers to self-register for testing

To make it easier to distribute your app to more testers, we recommend that
you use invite links. An *invite link* is a unique URL that lets testers enter
their email addresses to sign up to test an app. Enabling users to add
themselves to your list of app testers is a seamless way to increase your
internal testing base.

Invite links use cases include company dogfood programs, organizations with
large QA teams, and developer groups who want individual clients to be able to
control tester access.

We recommend that you create an invite link for a group. Any tester who signs
up using the invite link is automatically added to subsequent releases.

To learn more, see [Create invite links](https://firebase.google.com/docs/app-distribution/create-invite-links)
and [Add and remove testers from a group](https://firebase.google.com/docs/app-distribution/add-remove-testers#add-remove-testers-group).

## Make sure that testers are testing the version you care about

When a new version is uploaded, your testers are notified by email. To
supplement this notification, you can use the following features -- release
links and in-app alerts -- to make sure that your testers are testing the
specific app version you care about:

- **Release links:** Use this feature when you want to share a specific
  version with testers. To learn how to use release links, see
  [Distribute iOS apps to testers using the Firebase console](https://firebase.google.com/docs/app-distribution/ios/distribute-console).
  These links are also available with our [Firebase](https://firebase.google.com/docs/app-distribution/ios/distribute-cli)
  and [fastlane](https://firebase.google.com/docs/app-distribution/ios/distribute-fastlane)
  command-line (CLI) tools for use with your build automation tools.

- **In-app alerts:** Use these alerts when you want to ensure that your
  testers are testing the latest version of your app. By integrating the
  Firebase App Distribution iOS SDK, you can display alerts directly inside the
  app to your testers when new builds of your app are available. To learn how
  to add in-app alerts, see [Notify testers about new builds](https://firebase.google.com/docs/app-distribution/set-up-alerts?platform=ios).

## Automatically remove access for testers who leave the company

Once your CI/CD internal testing flow is up and running, you need to
make sure that people who leave the company no longer have access to your
internal builds. To help you manage tester access to builds, App Distribution
provides the following options:

- **fastlane:** Use your Fastfile file or directly run fastlane actions. To
  learn more about using fastlane to remove testers, see
  [Distribute iOS apps to testers using fastlane](https://firebase.google.com/docs/app-distribution/ios/distribute-fastlane#manage).

- **Public [Firebase App Distribution API](https://firebase.google.com/docs/reference/app-distribution/rest):**
  Use the `testers.batchRemove` endpoint.