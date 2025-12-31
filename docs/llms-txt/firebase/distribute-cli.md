# Source: https://firebase.google.com/docs/app-distribution/ios/distribute-cli.md.txt

# Source: https://firebase.google.com/docs/app-distribution/android/distribute-cli.md.txt

# Source: https://firebase.google.com/docs/app-distribution/ios/distribute-cli.md.txt

# Source: https://firebase.google.com/docs/app-distribution/android/distribute-cli.md.txt

<br />

APKAAB  

<br />

This guide describes how to distribute APKs to testers using theFirebaseCLI. The CLI tool lets you specify testers and release notes for a build, then distributes the build accordingly.

## Before you begin

If you haven't already,[add Firebase to your Android project](https://firebase.google.com/docs/android/setup#console).

If you aren't using any other Firebase products, you only have to create a project and register your app. However, if you decide to use additional products in the future, be sure to complete all of the steps on the page linked above.
| **Caution:** When you register your app with Firebase, make sure to enter the same package name as the app you're distributing. The package name value is case-sensitive and cannot be changed for your app in Firebase after it's registered with your Firebase project.

## Step 1. Build your app

When you're ready to distribute a pre-release version of your app to testers, build your APK using your normal process. You must sign the APK with your debug key or app signing key.

## Step 2. Distribute your app to testers

To distribute your app to testers, upload your app's file using theFirebaseCLI:

1. Install or update to the latest version of the[FirebaseCLI](https://firebase.google.com/docs/cli#install_the_firebase_cli)(we recommend downloading the standalone binary for the CLI specific to your OS). Make sure to[sign in](https://firebase.google.com/docs/cli#sign-in-test-cli)and test that you can access your projects.**Note:** If you're using the Firebase CLI in a CI environment, you can also authenticate with a[service account](https://firebase.google.com/docs/app-distribution/authenticate-service-account)or by using[`login:ci`.](https://firebase.google.com/docs/cli#cli-ci-systems)
2. Run the`appdistribution:distribute`command to upload your app and distribute it to testers. Use the following parameters to configure the distribution:

   |                                                                                                                                                                                                                                                                                                                   appdistribution:distribute options                                                                                                                                                                                                                                                                                                                    ||
   |------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | `--app`                                  | **Required** : Your app's Firebase App ID. You can find the App ID in theFirebaseconsole, on the[General Settings page](https://console.firebase.google.com/project/_/settings/general/). ``` --app 1:1234567890:android:0a1b2c3d4e5f67890 ```                                                                                                                                                                                                                                                                                                                                                                                |
   | `--token`                                | A refresh token that's printed when you authenticate your CI environment with theFirebaseCLI (read[Use the CLI with CI systems](https://firebase.google.com/docs/cli#cli-ci-systems)for more information). ``` --token "$FIREBASE_TOKEN" ```                                                                                                                                                                                                                                                                                                                                                                                  |
   | `--release-notes` `--release-notes-file` | Release notes for this build. You can either specify the release notes directly: ``` --release-notes "Text of release notes" ``` Or, specify the path to a plain text file: ``` --release-notes-file "/path/to/release-notes.txt" ```                                                                                                                                                                                                                                                                                                                                                                                         |
   | `--testers` `--testers-file`             | The email addresses of the testers you want to invite. You can specify the testers as a comma-separated list of email addresses: ``` --testers "ali@example.com, bri@example.com, cal@example.com" ``` Or, you can specify the path to a plain text file containing a comma-separated list of email addresses: ``` --testers-file "/path/to/testers.txt" ```                                                                                                                                                                                                                                                                  |
   | `--groups` `--groups-file`               | The tester groups you want to invite (refer to[Manage testers](https://firebase.google.com/docs/app-distribution/manage-testers)). Groups are specified usinggroup aliases, which you can look up in theFirebaseconsole. You can specify the groups as a comma-separated list: ``` --groups "qa-team, trusted-testers" ``` Or, you can specify the path to a plain text file containing a comma-separated list of group names: ``` --groups-file "/path/to/groups.txt" ```                                                                                                                                                    |
   | `--debug`                                | A flag you can include to print verbose log output.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | `--test-devices` `--test-devices-file`   | The following distribution types are part of the**Automated tester beta feature**. The test devices you want to distribute builds to (refer to[Automated tests](https://firebase.google.com/docs/app-distribution/android-automated-tester)). You can specify the testers as a comma-separated list of email addresses: ``` --test-devices: "model=shiba,version=34,locale=en,orientation=portrait;model=b0q,version=33,locale=en,orientation=portrait" ``` Or, you can specify the path to a plain text file containing a semicolon-separated list of test devices: ``` --test-devices-file: "/path/to/test-devices.txt" ``` |
   | `--test-username`                        | The username for automatic login to be used during[automated tests](https://firebase.google.com/docs/app-distribution/android-automated-tester).                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | `--test-password` `--test-password-file` | The password for automatic login to be used during[automated tests](https://firebase.google.com/docs/app-distribution/android-automated-tester). Or, you can specify the path to a plain text file containing a password: ``` --test-password-file: "/path/to/test-password.txt" ```                                                                                                                                                                                                                                                                                                                                          |
   | `--test-username-resource`               | Resource name for the username field for automatic login to be used during[automated tests](https://firebase.google.com/docs/app-distribution/android-automated-tester).                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | `--test-password-resource`               | Resource name for the password field for automatic login to be used during[automated tests](https://firebase.google.com/docs/app-distribution/android-automated-tester).                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | `--test-non-blocking`                    | Run[automated tests](https://firebase.google.com/docs/app-distribution/android-automated-tester)asynchronously. Visit the Firebase console for the automatic test results.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

   For example:  

   ```text
   firebase appdistribution:distribute test.apk  \
       --app 1:1234567890:android:0a1b2c3d4e5f67890  \
       --release-notes "Bug fixes and improvements" --testers-file testers.txt
   ```

   The Firebase CLI outputs the following links after the release upload. These links help you manage binaries and ensure that testers and other developers have the right release:
   - `firebase_console_uri`- A link to theFirebaseconsole displaying a single release. You can share this link with other developers in your org.
   - `testing_uri`- A link to the release in the tester experience (Android native app) that lets testers view release notes and install the app onto their device. The tester needs access to the release in order to use the link.
   - `binary_download_uri`- A signed link that directly downloads and installs the app binary (APK or AAB file) . The link expires after one hour.

   <br />

   ### Manage testers and groups

   In addition to distributing releases, you can also use`appdistribution:testers:add`and`appdistribution:testers:remove`to invite new testers or remove existing testers from your Firebase project.

   Once a tester has been added to your Firebase project, you can add them to individual releases. Once you remove a tester, they will no longer have access to releases in your project. Note that testers who are recently removed can still retain access to your releases for a window of time.

   For example:  

       firebase appdistribution:testers:add anothertester@email.com moretesters@email.com

       firebase appdistribution:testers:remove anothertester@email.com moretesters@email.com

   Tester emails must be separated by a space. You can also specify testers using`--file /path/to/testers.txt`.

   If you have a large number of testers you should consider using groups: You can use`appdistribution:group:create`and`appdistribution:group:delete`to create or delete groups in your Firebase project.

   Use`--group-alias`to specify a group for the`appdistribution:testers:add`and`appdistribution:testers:remove`commands.

   For example:  

       firebase appdistribution:group:create "QA team" qa-team

       firebase appdistribution:testers:add --group-alias=qa-team anothertester@email.com moretesters@email.com

       firebase appdistribution:testers:remove --group-alias=qa-team anothertester@email.com moretesters@email.com

       firebase appdistribution:group:delete qa-team

Once you distribute your build, it becomes available in theApp Distributiondashboard of theFirebaseconsole for 150 days (five months). When the build is 30 days from expiring, an expiration notice appears in both the console and your tester's list of builds on their test device.

Testers who haven't been invited to test the app receive email invitations to get started, and existing testers receive email notifications that a new build is ready to test (read the[tester set up guide](https://firebase.google.com/docs/app-distribution/android/set-up-for-testing)for instructions on how to install the test app). You can monitor the status of each tester-whether they accepted the invitation and whether they downloaded the app-in theFirebaseconsole.

Testers have 30 days to accept an invitation to test the app before it expires. When an invitation is 5 days from expiring, an expiration notice appears in theFirebaseconsole next to the tester on a release. An invitation can be renewed by resending it using the drop-down menu on the tester row.

## Next steps

- Implement[in-app feedback](https://firebase.google.com/docs/app-distribution/collect-feedback-from-testers)to make it easy for testers to send feedback about your app (including screenshots).

- Learn how to display[in-app alerts](https://firebase.google.com/docs/app-distribution/set-up-alerts?platform=android)to your testers when new builds of your app are available to install.

- Learn best practices for[distributing Android apps to QA testers using CI/CD](https://firebase.google.com/docs/app-distribution/best-practices-distributing-android-apps-to-qa-testers-with-ci-cd).