# Source: https://firebase.google.com/docs/app-distribution/ios/distribute-fastlane.md.txt

# Source: https://firebase.google.com/docs/app-distribution/android/distribute-fastlane.md.txt

# Source: https://firebase.google.com/docs/app-distribution/ios/distribute-fastlane.md.txt

# Source: https://firebase.google.com/docs/app-distribution/android/distribute-fastlane.md.txt

<br />

APKAAB  

<br />

This document describes how to distribute APK builds to testers using[fastlane](https://fastlane.tools/), an open source platform that automates building and releasing iOS and Android apps. This document follows instructions defined in a`Fastfile`. After you set up fastlane and your`Fastfile`, you can integrateApp Distributionwith your fastlane configuration.

## Before you begin

If you haven't already,[add Firebase to your Android project](https://firebase.google.com/docs/android/setup#console).

If you aren't using any other Firebase products, you only have to create a project and register your app. However, if you decide to use additional products in the future, be sure to complete all of the steps on the page linked above.
| **Caution:** When you register your app with Firebase, make sure to enter the same package name as the app you're distributing. The package name value is case-sensitive and cannot be changed for your app in Firebase after it's registered with your Firebase project.

## Step 1. Set up fastlane

1. [Install and set up fastlane](https://docs.fastlane.tools/getting-started/android/setup/).

2. To addApp Distributionto your fastlane configuration, run the following command from the root of your Android project:

   ```
   fastlane add_plugin firebase_app_distribution
   ```

   If the command prompts you with an option, select`Option 3: RubyGems.org`.

## Step 2. Authenticate with Firebase

Before you can use the fastlane plugin, you must first authenticate with your Firebase project in one of the following ways. By default, the fastlane plugin looks for credentials from theFirebaseCLI if no other authentication method is used.

<br />

### Use Firebase service account credentials

<br />

Authenticating with a service account allows you to flexibly use the plugin with your continuous integration (CI) system. There are two ways to provide service account credentials:

- Pass your service account key file to the`firebase_app_distribution`action. You might find this method convenient if you already have your service account key file in your build environment.
- Set the environment variable`GOOGLE_APPLICATION_CREDENTIALS`to point to your service account key file. You might prefer this method if you already have[Application Default Credentials (ADC)](https://cloud.google.com/docs/authentication/application-default-credentials)configured for another Google service (e.g.,Google Cloud).

1. On the[Google Cloudconsole,](https://console.cloud.google.com/projectselector2/iam-admin/serviceaccounts)select your project and create a new service account.
2. Add the**Firebase App DistributionAdmin**role.
3. Create a private json key and move the key to a location accessible to your build environment.*Be sure to keep this file somewhere safe* , as it grants administrator access toApp Distributionin your Firebase project.
4. Skip this step if you created your app after September 20, 2019: In the Google APIs console, enable the[Firebase App DistributionAPI.](https://console.developers.google.com/apis/api/firebaseappdistribution.googleapis.com/overview?project=_)When prompted, select the project with the same name as your Firebase project.
5. Provide or locate your service account credentials:

   1. To pass your service account key to your lane's`firebase_app_distribution`action, set the`service_credentials_file`parameter with the path to your private key JSON file
   2. To locate your credentials with ADC, set the environment variable`GOOGLE_APPLICATION_CREDENTIALS`to the path for the private key JSON file. For example:

      ```
       export GOOGLE_APPLICATION_CREDENTIALS=/absolute/path/to/credentials/file.json
      ```

      <br />

      For more information on authenticating with ADC, read[Providing credentials to your application.](https://cloud.google.com/docs/authentication/production#providing_credentials_to_your_application)

<br />

<br />

<br />

### Sign in using theFirebaseCLI

<br />

See[Log in with theFirebaseCLI](https://firebase.google.com/docs/cli#sign-in-test-cli)for instructions on how to authenticate your project.

<br />

<br />

## Step 3. Set up your Fastfile and distribute your app

1. In a`./fastlane/Fastfile`lane, add a`firebase_app_distribution`block. Use the following parameters to configure the distribution:

   |                                                                                                                                                                                                                                                                                                                 firebase_app_distribution parameters                                                                                                                                                                                                                                                                                                                  ||
   |--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | `app`                                | **Required** : Your app's Firebase App ID. You can find the App ID in theFirebaseconsole, on the[General Settings page](https://console.firebase.google.com/project/_/settings/general/). ``` app: "1:1234567890:android:0a1b2c3d4e5f67890" ```                                                                                                                                                                                                                                                                                                                                                                                 |
   | `firebase_cli_token`                 | A refresh token that's printed when you authenticate your CI environment with theFirebaseCLI (read[Use the CLI with CI systems](https://firebase.google.com/docs/cli#cli-ci-systems)for more information).                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | `service_credentials_file`           | The path to your Google service account json file. See above for how to[authenticate using service account credentials](https://firebase.google.com/docs/app-distribution/android/distribute-fastlane#service-acc-fastlane).                                                                                                                                                                                                                                                                                                                                                                                                    |
   | `android_artifact_type`              | Specifies the Android file type (APK or AAB).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | `android_artifact_path`              | Replaces`apk_path`(deprecated). Absolute path to the APK or AAB file you want to upload. If unspecified, fastlane determines the file's location from the lane in which the file was generated.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | `release_notes` `release_notes_file` | Release notes for this build. You can either specify the release notes directly: ``` release_notes: "Text of release notes" ``` Or, specify the path to a plain text file: ``` release_notes_file: "/path/to/release-notes.txt" ```                                                                                                                                                                                                                                                                                                                                                                                             |
   | `testers` `testers_file`             | The email addresses of the testers you want to invite. You can specify the testers as a comma-separated list of email addresses: ``` testers: "ali@example.com, bri@example.com, cal@example.com" ``` Or, you can specify the path to a plain text file containing a comma-separated list of email addresses: ``` testers_file: "/path/to/testers.txt" ```                                                                                                                                                                                                                                                                      |
   | `groups` `groups_file`               | The tester groups you want to invite (refer to[Manage testers](https://firebase.google.com/docs/app-distribution/manage-testers)). Groups are specified usinggroup aliases, which you can look up in theFirebaseconsole. You can specify the groups as a comma-separated list: ``` groups: "qa-team, trusted-testers" ``` Or, you can specify the path to a plain text file containing a comma-separated list of group names: ``` groups_file: "/path/to/groups.txt" ```                                                                                                                                                        |
   | `test_devices` `test_devices_file`   | The following distribution types are part of the**Automated tester beta feature**. The test devices you want to distribute builds to (refer to[Automated tests](https://firebase.google.com/docs/app-distribution/android-automated-tester)). You can specify the test devices as a semicolon-separated list of test devices: ``` test_devices: "model=shiba,version=34,locale=en,orientation=portrait;model=b0q,version=33,locale=en,orientation=portrait" ``` Or, you can specify the path to a plain text file containing a semicolon-separated list of test devices: ``` test_devices_file: "/path/to/test-devices.txt" ``` |
   | `test_username`                      | The username for automatic login to be used during[automated tests](https://firebase.google.com/docs/app-distribution/android-automated-tester).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | `test_password` `test_password_file` | The password for automatic login to be used during[automated tests](https://firebase.google.com/docs/app-distribution/android-automated-tester). Or, you can specify the path to a plain text file containing a password: ``` test_password_file: "/path/to/test-password.txt" ```                                                                                                                                                                                                                                                                                                                                              |
   | `test_username_resource`             | Resource name for the username field for automatic login to be used during[automated tests](https://firebase.google.com/docs/app-distribution/android-automated-tester).                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | `test_password_resource`             | Resource name for the password field for automatic login to be used during[automated tests](https://firebase.google.com/docs/app-distribution/android-automated-tester).                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | `test_non_blocking`                  | Run[automated tests](https://firebase.google.com/docs/app-distribution/android-automated-tester)asynchronously. Visit the Firebase console for the automatic test results.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | `debug`                              | A boolean flag. You can set this to`true`to print verbose debug output.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

```ruby
platform :android do
    desc "My awesome app"
    lane :distribute do
        build_android_app(...)
        # build_android_app is a built-in https://docs.fastlane.tools/actions/build_android_app/
        release = firebase_app_distribution(
            app: "1:123456789:android:abcd1234",
            testers: "tester1@company.com, tester2@company.com",
            release_notes: "Lots of amazing new features to test out!"
        )
    end
end
```

To make the build available to testers, run your lane:  

```
fastlane <lane>
```

<br />

The return value of the action is a hash representing the uploaded release. This hash is also available using`lane_context[SharedValues::FIREBASE_APP_DISTRO_RELEASE]`. For more information about the available fields in this hash, see the[REST API documentation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases#resource:-release).

The fastlane plugin outputs the following links after the release upload. These links help you manage binaries and ensure that testers and other developers have the right release:

- A link to theFirebaseconsole displaying a single release. You can share this link with other developers in your org.
- A link to the release in the tester experience (Android native app) that lets testers view release notes and install the app onto their device. The tester needs access to the release in order to use the link.
- A signed link that directly downloads and installs the app binary (APK or AAB file). The link expires after one hour.

After you distribute your build, it is available in theApp Distributiondashboard of theFirebaseconsole for 150 days. When the build is 30 days from expiring, an expiration notice appears in the console and in the tester's list of builds on their test device.

Testers who weren't previously invited to test the app receive email invitations to get started. Existing testers receive email notifications that a new build is ready to test. To learn how to install the test app, see[tester set up guide](https://firebase.google.com/docs/app-distribution/android/set-up-for-testing). You can monitor the status of each tester to determine whether they accepted the invitation and whether they downloaded the app in theFirebaseconsole.
| **Note:** Testers have 30 days to accept an invitation to test the app before the invitation expires. When an invitation is 5 days from expiring, an expiration notice appears in theFirebaseconsole next to the tester on a release. You can resend an invitation using the dropdown menu on the tester row.

(Optional) To automatically increment your build number every time you create a new release in App Distribution, you can use the[`firebase_app_distribution_get_latest_release`action](https://firebase.google.com/docs/app-distribution/android/distribute-fastlane#get-latest-release)and, for example, the[`increment_version_code`fastlane plugin](http://docs.fastlane.tools/plugins/available-plugins/#increment_version_code). The following code provides an example of how to automatically increment your build number:  

    lane :increment_version do
      latest_release = firebase_app_distribution_get_latest_release(
        app: "<your Firebase app ID>"
      )
      increment_version_code({ version_code: latest_release[:buildVersion].to_i + 1 })
    end

To learn more about the`firebase_app_distribution_get_latest_release`action, see[Get information about your app's latest release](https://firebase.google.com/docs/app-distribution/android/distribute-fastlane#get-latest-release).

## Step 4 (Optional). Managing testers for the distribution

You can add and remove testers from your project or group using your`Fastfile`file or by directly running fastlane actions. Running actions directly overrides the values set in your`Fastfile`.

Once a tester is added to your Firebase project, you can add them to individual releases. Testers who are removed from your Firebase project no longer have access to releases in your project, but they might retain access to your releases for a window of time.

If you have a large number of testers you should consider using groups.

#### Use`Fastfile`

```transact-sql
# Use lanes to add or remove testers from a project.
lane(:add_testers) do
  firebase_app_distribution_add_testers(
    emails: "foo@google.com,bar@google.com"
    # or file: "/path/to/testers.txt"
    group_alias: "qa-team" # (Optional) add testers to this group
  )
end

lane(:remove_testers) do
  firebase_app_distribution_remove_testers(
    emails: "foo@google.com,bar@google.com"
    # or file: "/path/to/testers.txt"
    group_alias: "qa-team" # (Optional) remove testers from this group only
  )
end
```  

```scdoc
# Add or remove testers with the terminal
$ fastlane add_testers
$ fastlane remove_testers
```

#### Run fastlane actions

    fastlane run firebase_app_distribution_create_group display_name:"QA Team" alias:"qa-team"
    fastlane run firebase_app_distribution_add_testers group_alias:"qa-team" emails:"foo@google.com,bar@google.com"
    fastlane run firebase_app_distribution_remove_testers group_alias:"qa-team" emails:"foo@google.com,bar@google.com"
    fastlane run firebase_app_distribution_delete_group alias:"qa-team"

You can also specify testers using`--file="/path/to/testers.txt`instead of`--emails`.

The`firebase_app_distribution_add_testers`and`firebase_app_distribution_remove_testers`tasks also accept the following arguments:

- `project_name`: Your Firebase project number.
- `group_alias`(optional): If specified, the testers are added to (or removed from) specified group.
- `service_credentials_file`: The path to your Google service credentials file.
- `firebase_cli_token`: Auth token forFirebaseCLI.

The`service_credentials_file`and the`firebase_cli_token`are the same arguments used by the upload action.

## Step 5 (Optional). Get information about your app's latest release

You can use the`firebase_app_distribution_get_latest_release`action to fetch information about your app's latest release in App Distribution, including app version information, release notes, and creation time. Use cases include automatically increasing the version and carrying over the release notes from the previous release.

The return value of the action is a hash representing the latest release. This hash is also available using`lane_context[SharedValues::FIREBASE_APP_DISTRO_LATEST_RELEASE]`. For more information about the available fields in this hash, see the[REST API documentation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases#resource:-release).

### Parameters

|                                                                                                           firebase_app_distribution_get_latest_release parameters                                                                                                           ||
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `app`                      | **Required** : Your app's Firebase App ID. You can find the App ID in theFirebaseconsole, on the[General Settings page](https://console.firebase.google.com/project/_/settings/general/). ``` app: "1:1234567890:android:0a1b2c3d4e5f67890" ``` |
| `firebase_cli_token`       | A refresh token that's printed when you authenticate your CI environment with theFirebaseCLI (read[Use the CLI with CI systems](https://firebase.google.com/docs/cli#cli-ci-systems)for more information).                                      |
| `service_credentials_file` | The path to your Google service account json file. See above for how to[authenticate using service account credentials](https://firebase.google.com/docs/app-distribution/android/distribute-fastlane#service-acc-fastlane).                    |
| `debug`                    | A boolean flag. You can set this to`true`to print verbose debug output.                                                                                                                                                                         |

## Next steps

- Implement[in-app feedback](https://firebase.google.com/docs/app-distribution/collect-feedback-from-testers)to make it easy for testers to send feedback about your app (including screenshots).

- Learn how to display[in-app alerts](https://firebase.google.com/docs/app-distribution/set-up-alerts?platform=android)to your testers when new builds of your app are available to install.

- Learn best practices for[distributing Android apps to QA testers using CI/CD](https://firebase.google.com/docs/app-distribution/best-practices-distributing-android-apps-to-qa-testers-with-ci-cd).