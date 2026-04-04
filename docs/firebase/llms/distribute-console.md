# Source: https://firebase.google.com/docs/app-distribution/ios/distribute-console.md.txt

# Source: https://firebase.google.com/docs/app-distribution/android/distribute-console.md.txt

# Source: https://firebase.google.com/docs/app-distribution/ios/distribute-console.md.txt

# Source: https://firebase.google.com/docs/app-distribution/android/distribute-console.md.txt

<br />

APKAAB  

<br />

This guide describes how to upload APKs toApp Distributionand distribute builds to testers using theFirebaseconsole.

## Before you begin

If you haven't already,[add Firebase to your Android project](https://firebase.google.com/docs/android/setup#console).

If you aren't using any other Firebase products, you only have to create a project and register your app. However, if you decide to use additional products in the future, be sure to complete all of the steps on the page linked above.
| **Caution:** When you register your app with Firebase, make sure to enter the same package name as the app you're distributing. The package name value is case-sensitive and cannot be changed for your app in Firebase after it's registered with your Firebase project.

## Step 1. Build your app

When you're ready to distribute a pre-release version of your app to testers, build your APK using your normal process. You must sign the APK with your debug key or app signing key.

## Step 2. Distribute your app to testers

To distribute your app to testers, upload your APK file using theFirebaseconsole:

1. Open the[App Distributionpage](https://console.firebase.google.com/project/_/appdistribution)of theFirebaseconsole. Select your Firebase project when prompted.

2. On the**Releases**page, select the app you want to distribute from the drop-down menu.

3. Drag your app's APK file to the console to upload it.

4. When the upload completes, specify the tester groups and individual testers you want to receive the build. Then, add release notes for the build.

   See[Manage testers](https://firebase.google.com/docs/app-distribution/manage-testers)for more on creating tester groups.
5. Click**Distribute**to make the build available to testers. The tester automatically receives an email invitation to test the app.

6. (Optional) To share links to specific releases with testers who have access to those releases, click the**Link**icon to copy the release link to the clipboard.

Once you distribute your build, it becomes available in theApp Distributiondashboard of theFirebaseconsole for 150 days (five months). When the build is 30 days from expiring, an expiration notice appears in both the console and your tester's list of builds on their test device.

Testers who haven't been invited to test the app receive email invitations to get started, and existing testers receive email notifications that a new build is ready to test. For instructions on how to install the test app, see[Get set up as a tester withApp Distribution](https://firebase.google.com/docs/app-distribution/get-set-up-as-a-tester?platform=android). You can monitor the status of each tester-whether they accepted the invitation and whether they downloaded the app-in theFirebaseconsole.

Testers have 30 days to accept an invitation to test the app before it expires. When an invitation is 5 days from expiring, an expiration notice appears in theFirebaseconsole next to the tester on a release. An invitation can be renewed by resending it using the drop-down menu on the tester row.

## Next steps

- Implement[in-app feedback](https://firebase.google.com/docs/app-distribution/collect-feedback-from-testers)to make it easy for testers to send feedback about your app (including screenshots).

- Learn how to display[in-app alerts](https://firebase.google.com/docs/app-distribution/set-up-alerts?platform=android)to your testers when new builds of your app are available to install.

- Learn best practices for[distributing Android apps to QA testers using CI/CD](https://firebase.google.com/docs/app-distribution/best-practices-distributing-android-apps-to-qa-testers-with-ci-cd).