# Source: https://firebase.google.com/docs/app-distribution/android/distribute-gradle.md.txt

<br />

APKAAB  

<br />

You can integrateApp Distributioninto your Android build process using theApp DistributionGradle plugin. The plugin lets you specify your testers and release notes in your app's Gradle file, letting you configure distributions for different build types and variants of your app.

This guide describes how to distribute APKs to testers using theApp DistributionGradle plugin.

## Before you begin

If you haven't already,[add Firebase to your Android project](https://firebase.google.com/docs/android/setup#console).

If you aren't using any other Firebase products, you only have to create a project and register your app. However, if you decide to use additional products in the future, be sure to complete all of the steps on the page linked above.
| **Caution:** When you register your app with Firebase, make sure to enter the same package name as the app you're distributing. The package name value is case-sensitive and cannot be changed for your app in Firebase after it's registered with your Firebase project.

## Step 1. Set up your Android project

1. In your**root-level (project-level)** Gradle file (`<project>/build.gradle.kts`or`<project>/build.gradle`), add theApp DistributionGradle plugin as a dependency:

   ### Kotlin

   Are you still using the`buildscript`syntax? Learn how to[add Firebase plugins](https://firebase.google.com/docs/android/troubleshooting-faq#add-plugins-using-buildscript-syntax)using that syntax.  

   ```kotlin
   plugins {
       // ...
       id("com.android.application") version "7.3.0" apply false

       // Make sure that you have the Google services Gradle plugin dependency
       id("com.google.gms.google-services") version "4.4.4" apply false

       // Add the dependency for the App Distribution Gradle plugin
       id("com.google.firebase.appdistribution") version "5.2.0" apply false
   }
   ```

   ### Groovy

   Are you still using the`buildscript`syntax? Learn how to[add Firebase plugins](https://firebase.google.com/docs/android/troubleshooting-faq#add-plugins-using-buildscript-syntax)using that syntax.  

   ```groovy
   plugins {
       // ...
       id 'com.android.application' version '7.3.0' apply false

       // Make sure that you have the Google services Gradle plugin dependency
       id 'com.google.gms.google-services' version '4.4.4' apply false

       // Add the dependency for the App Distribution Gradle plugin
       id 'com.google.firebase.appdistribution' version '5.2.0' apply false
   }
   ```
2. In your**module (app-level)** Gradle file (usually`<project>/<app-module>/build.gradle.kts`or`<project>/<app-module>/build.gradle`), add theApp DistributionGradle plugin:

   ### Kotlin

   ```kotlin
   plugins {
     id("com.android.application")

     // Make sure that you have the Google services Gradle plugin
     id("com.google.gms.google-services")

     // Add the App Distribution Gradle plugin
     id("com.google.firebase.appdistribution")
   }
   ```

   ### Groovy

   ```groovy
   plugins {
     id 'com.android.application'

     // Make sure that you have the Google services Gradle plugin
     id 'com.google.gms.google-services'

     // Add the App Distribution Gradle plugin
     id 'com.google.firebase.appdistribution'
   }
   ```
3. If you're behind a corporate proxy or firewall, add the following[Java system property](https://docs.gradle.org/current/userguide/build_environment.html#sec:gradle_system_properties)that enablesApp Distributionto upload your distributions to Firebase:

       -Djavax.net.ssl.trustStore=/path/to/truststore -Djavax.net.ssl.trustStorePassword=password

## Step 2. Authenticate with Firebase

Before you can use the Gradle plugin, you must first authenticate with your Firebase project in one of the following ways. By default, the Gradle plugin looks for credentials from theFirebaseCLI if no other authentication method is used.

<br />

### Use Firebase service account credentials

<br />

Authenticating with a service account allows you to flexibly use the plugin with your continuous integration (CI) system. There are two ways to provide service account credentials:

- Pass your service account key file to`build.gradle`. You might find this method convenient if you already have your service account key file in your build environment.
- Set the environment variable`GOOGLE_APPLICATION_CREDENTIALS`to point to your service account key file. You might prefer this method if you already have Application Default Credentials (ADC) configured for another Google service (e.g.,Google Cloud).

To authenticate using service account credentials:

1. On the[Google Cloudconsole,](https://console.cloud.google.com/projectselector2/iam-admin/serviceaccounts)select your project and create a new service account.
2. Add the**Firebase App DistributionAdmin**role.
3. Create a private json key and move the key to a location accessible to your build environment.*Be sure to keep this file somewhere safe* , as it grants administrator access toApp Distributionin your Firebase project.
4. Skip this step if you created your app after September 20, 2019: In the Google APIs console, enable the[Firebase App DistributionAPI.](https://console.developers.google.com/apis/api/firebaseappdistribution.googleapis.com/overview?project=_)When prompted, select the project with the same name as your Firebase project.
5. Provide or locate your service account credentials:

   1. To pass Gradle your service account key, in your`build.gradle`file, set the property`serviceCredentialsFile`to the private key JSON file.
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

## Step 3. Configure your distribution properties

In your**module (app-level)** Gradle file (usually`<project>/<app-module>/build.gradle.kts`or`<project>/<app-module>/build.gradle`), configureApp Distributionby adding at least one`firebaseAppDistribution`section.

For example, to distribute the`release`build to testers, follow these instructions::  

### Kotlin

**Note:** To use Kotlin DSL, you must use version 3.1.0 or greater of theApp DistributionGradle plugin.  

```kotlin
import com.google.firebase.appdistribution.gradle.firebaseAppDistribution

android {

  // ...

  buildTypes {
      getByName("release") {
          firebaseAppDistribution {
              artifactType = "APK"
              releaseNotesFile = "/path/to/releasenotes.txt"
              testers = "ali@example.com, bri@example.com, cal@example.com"
          }
      }
  }

  // ...
}
```

### Groovy

```transact-sql
android {

  // ...

  buildTypes {
      release {
          firebaseAppDistribution {
              artifactType="APK"
              releaseNotesFile="/path/to/releasenotes.txt"
              testers="ali@example.com, bri@example.com, cal@example.com"
          }
      }
  }

  // ...
}
```

You can configureApp Distributionfor[build types and product flavors](https://developer.android.com/studio/build/build-variants).

For example, to distribute`debug`and`release`builds in "demo" and "full" product flavors, follow these instructions:  

### Kotlin

**Note:** To use Kotlin DSL, you must use version 3.1.0 or greater of theApp DistributionGradle plugin.  

```kotlin
import com.google.firebase.appdistribution.gradle.firebaseAppDistribution

android {

  // ...

  buildTypes {
      getByName("debug") {...}
      getByName("release") {...}
  }

  flavorDimensions += "version"
  productFlavors {
      create("demo") {
          dimension = "version"
          firebaseAppDistribution {
              releaseNotes = "Release notes for demo version"
              testers = "demo@testers.com"
          }
      }
      create("full") {
          dimension = "version"
          firebaseAppDistribution {
              releaseNotes = "Release notes for full version"
              testers = "full@testers.com"
          }
      }
  }

  // ...
}
```

### Groovy

```transact-sql
android {

  // ...

  buildTypes {
      debug {...}
      release {...}
  }

  flavorDimensions "version"
  productFlavors {
      demo {
          dimension "version"
          firebaseAppDistribution {
              releaseNotes="Release notes for demo version"
              testers="demo@testers.com"
          }
      }
      full {
          dimension "version"
          firebaseAppDistribution {
              releaseNotes="Release notes for full version"
              testers="full@testers.com"
          }
      }
  }

  // ...
}
```

Use the following parameters to configure the distribution:

|                                                                                                                                                                                                                                                                                                                App DistributionBuild Parameters                                                                                                                                                                                                                                                                                                                 ||
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `appId`                            | Your app's Firebase App ID. Required only if you don't have the Google Services Gradle plugin installed. You can find the App ID in the`google-services.json`file or in theFirebaseconsole on the[General Settings page](https://console.firebase.google.com/project/_/settings/general/). The value in your`build.gradle`file overrides the value output from the`google-services`plugin. ``` appId="1:1234567890:android:321abc456def7890" ```                                                                                                                                                                            |
| `serviceCredentialsFile`           | The path to your service account private key JSON file. Required only if you use service account authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `artifactType`                     | Specifies your app's file type. Can be set to`"AAB"`or`"APK"`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `artifactPath`                     | Absolute path to the APK or AAB file you want to upload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `releaseNotes`or`releaseNotesFile` | Release notes for this build. You can either specify the release notes directly or the path to a plain text file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `testers`or`testersFile`           | The email addresses of the testers you want to distribute builds to. You can specify the testers as a comma-separated list of email addresses: ``` testers="ali@example.com, bri@example.com, cal@example.com" ``` Or, you can specify the path to a file containing a comma-separated list of email addresses: ``` testersFile="/path/to/testers.txt" ```                                                                                                                                                                                                                                                                  |
| `groups`or`groupsFile`             | The tester groups you want to distribute builds to (see[Manage testers](https://firebase.google.com/docs/app-distribution/manage-testers)). Groups are specified usinggroup aliases, which you can find in the**Testers** tab in the FirebaseApp Distributionconsole. You can specify the groups as a comma-separated list of group aliases: ``` groups="qa-team, android-testers" ``` Or, you can specify the path to a file containing a comma-separated list of group aliases: ``` groupsFile="/path/to/tester-groups.txt" ```                                                                                           |
| `testDevices`or`testDevicesFile`   | The following distribution types are part of the**Automated tester beta feature**. The test devices you want to distribute builds to (see[Automated tests](https://firebase.google.com/docs/app-distribution/android-automated-tester)). You can specify the test devices as a semicolon-separated list of device specifications: ``` testDevices="model=shiba,version=34,locale=en,orientation=portrait;model=b0q,version=33,locale=en,orientation=portrait" ``` Or, you can specify the path to a file containing a semicolon-separated list of device specifications: ``` testDevicesFile="/path/to/testDevices.txt" ``` |
| `testUsername`                     | The username for automatic login to be used during[automated tests](https://firebase.google.com/docs/app-distribution/android-automated-tester).                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `testPassword`or`testPasswordFile` | The password for automatic login to be used during[automated tests](https://firebase.google.com/docs/app-distribution/android-automated-tester). Or, you can specify the path to a plain text file containing a password: ``` testPasswordFile="/path/to/testPassword.txt" ```                                                                                                                                                                                                                                                                                                                                              |
| `testUsernameResource`             | Resource name for the username field for automatic login to be used during[automated tests](https://firebase.google.com/docs/app-distribution/android-automated-tester).                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `testPasswordResource`             | Resource name for the password field for automatic login to be used during[automated tests](https://firebase.google.com/docs/app-distribution/android-automated-tester).                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `testNonBlocking`                  | Run[automated tests](https://firebase.google.com/docs/app-distribution/android-automated-tester)asynchronously. Visit the Firebase console for the automatic test results.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `stacktrace`                       | Prints out the stacktrace for user exceptions. This is helpful when debugging issues.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Step 4. Distribute your app to testers

1. Finally, to package your test app and invite testers, build the targets<var translate="no">BUILD-VARIANT</var>and`appDistributionUpload`<var translate="no">BUILD-VARIANT</var>with your project's Gradle wrapper, where<var translate="no">BUILD-VARIANT</var>is the optional product flavor and build type you configured in the previous step. For more information about product flavors, see[Configure build variants](https://developer.android.com/studio/build/build-variants).

   For example, to distribute your app using the`release`build variant, run the following command:  

   ```
   ./gradlew assembleRelease appDistributionUploadRelease
   ```

   Or, if you authenticated with your[Google Account](https://firebase.google.com/docs/app-distribution/android/distribute-gradle#google-acc-gradle)and didn't provide credentials in your Gradle build file, include the`FIREBASE_TOKEN`variable:  

   ```
   export FIREBASE_TOKEN=1/a1b2c3d4e5f67890
   ./gradlew --stop // Only needed for environment variable changes
   ./gradlew assembleRelease appDistributionUploadRelease
   ```
2. You can also override the values set in your`build.gradle`file by passing command line arguments in the form of`--<property-name>=<property-value>`. For example:

   - To upload a debug build toApp Distribution:

         ./gradlew bundleDebug appDistributionUploadDebug
             --artifactType="APK"

   - To invite additional testers or remove existing testers from your Firebase project:

         ./gradlew appDistributionAddTesters
             --projectNumber=<project_number>
             --emails="anothertester@email.com, moretesters@email.com"
         ./gradlew appDistributionRemoveTesters
             --projectNumber=<project_number>
             --emails="anothertester@email.com, moretesters@email.com"

     Once a tester has been added to your Firebase project, you can add them to individual releases. Testers who are removed will no longer have access to releases in your project, but may still retain access to your releases for a window of time.

   You can also specify testers using`--file="/path/to/testers.txt"`instead of`--emails`.

   The`appDistributionAddTesters`and`appDistributionRemoveTesters`tasks also accept the following arguments:
   - `projectNumber`: Your Firebase project number.

   - `serviceCredentialsFile`: The path to your Google service credentials file. This is the same argument used by the upload action.

The Gradle plugin outputs the following links after the release upload. These links help you manage binaries and ensure that testers and other developers have the right release:

- `firebase_console_uri`- A link to theFirebaseconsole displaying a single release. You can share this link with other developers in your org.
- `testing_uri`- A link to the release in the tester experience (Android native app) that lets testers view release notes and install the app onto their device. The tester needs access to the release in order to use the link.
- `binary_download_uri`- A signed link that directly downloads and installs the app binary (APK or AAB file). The link expires after one hour.

Once you distribute your build, it becomes available in theApp Distributiondashboard of theFirebaseconsole for 150 days (five months). When the build is 30 days from expiring, an expiration notice appears in both the console and your tester's list of builds on their test device.

Testers who haven't been invited to test the app receive email invitations to get started, and existing testers receive email notifications that a new build is ready to test (read the[tester set up guide](https://firebase.google.com/docs/app-distribution/android/set-up-for-testing)for instructions on how to install the test app). You can monitor the status of each tester-whether they accepted the invitation and whether they downloaded the app-in theFirebaseconsole.

Testers have 30 days to accept an invitation to test the app before it expires. When an invitation is 5 days from expiring, an expiration notice appears in theFirebaseconsole next to the tester on a release. An invitation can be renewed by resending it using the drop-down menu on the tester row.

## Next steps

- Implement[in-app feedback](https://firebase.google.com/docs/app-distribution/collect-feedback-from-testers)to make it easy for testers to send feedback about your app (including screenshots).

- Learn how to display[in-app alerts](https://firebase.google.com/docs/app-distribution/set-up-alerts?platform=android)to your testers when new builds of your app are available to install.

- Visit the[Android App Bundle codelab](https://firebase.google.com/codelabs/appdistribution-app-bundles)to learn how to distribute app bundle releases step by step.

- Learn best practices for[distributing Android apps to QA testers using CI/CD](https://firebase.google.com/docs/app-distribution/best-practices-distributing-android-apps-to-qa-testers-with-ci-cd).