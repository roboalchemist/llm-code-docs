# Source: https://firebase.google.com/docs/test-lab/android/continuous.md.txt

<br />

You can useFirebase Test Labwhen developing your app using any continuous integration (CI) system. Continuous integration systems let you automatically build and test your app each time you check in updates to your app source code.

## UsingFirebase Test Labwith Jenkins CI

This section describes how to useTest Labwith[Jenkins CI](http://jenkins-ci.org/).

### Requirements

Before you can useFirebase Test Labwith Jenkins, you need to complete the following steps:

1. **Set up gcloud.** Follow the instructions from[UsingFirebase Test Labfrom the gcloud Command Line](https://firebase.google.com/docs/test-lab/android/command-line)to create a Firebase project and configure your localGoogle CloudSDK environment.

2. **Create and authorize a service account.** Service accounts aren't subject to spam checks or captcha prompts, which could otherwise block your CI builds. Create a service account with an**Editor** role in the[Google Cloudconsole](https://console.cloud.google.com/iam-admin/serviceaccounts/)and then activate it (see the[gcloud auth activate-service-account documentation](https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account)to learn how).

3. **Enable required APIs.** After logging in using the service account: In the[Google Developers Console API Library page](https://console.developers.google.com/apis/library), enable the**Google Cloud Testing API** and**Cloud Tool Results API** . To enable these APIs, type these API names into the search box at the top of the console, and then click**Enable API**on the overview page for that API.

### Install and set up Jenkins

You can install and set up Jenkins CI on Linux or Windows. Certain details of this guide are specific to installing and running Jenkins CI on Linux, including the use of slashes (`/`) in file paths.

To download and install Jenkins on a computer running Linux or Windows, follow the instructions on[Installing Jenkins](https://wiki.jenkins-ci.org/display/JENKINS/Installing+Jenkins). After installing Jenkins, follow the instructions on[Starting and Accessing Jenkins](https://wiki.jenkins-ci.org/display/JENKINS/Starting+and+Accessing+Jenkins)to complete setup and access the Jenkins dashboard.

### Configure global security settings

Jenkins does not have user authentication and access control configured when it is first installed. Before using Jenkins withFirebase Test Lab, configure global security settings to enforce access control and authenticate users.

#### To configure global security settings

1. Navigate to the Jenkins dashboard on your server. To do this, browse to**http://\<servername\>:8080** , where**\<servername\>**is the name of the computer where you have installed Jenkins.
2. On the Jenkins dashboard, click**Manage Jenkins** , and then click**Configure Global Security**.
3. On the**Configure Global Security** page, click**Enable security** , and then click**Save**.

For more information about configuring security settings for Jenkins, see[Quick and Simple Security](https://wiki.jenkins-ci.org/display/JENKINS/Quick+and+Simple+Security),[Standard Security Setup](https://wiki.jenkins-ci.org/display/JENKINS/Standard+Security+Setup), and[Securing Jenkins](https://wiki.jenkins-ci.org/display/JENKINS/Securing+Jenkins).

### Create a Jenkins project

Next, create a project for running continuous integration testing of your app withFirebase Test Lab.

#### To create a Jenkins project

1. Navigate to the Jenkins dashboard on your server. To do this, browse to**http://\<servername\>:8080** , where**\<servername\>**is the name of the computer where you have installed Jenkins.
2. On the Jenkins dashboard, click**New Item**.
3. Type a name for your project in the**Item name** field:
   - Choose**Freestyle project**to create a project that uses a single build configuration.
   - Choose**Build multi-configuration project**to create a project that runs on multiple different build configurations. If you plan to build your app with a variety of build configurations (multiple locales, multiple Android API levels, etc.), then a multi-configuration project is the best choice.
4. Click**Save**.

After your project is created, your web browser displays the main page for your project.

### Add revision control and Gradle build steps

This section describes how to integrate Jenkins with revision control systems such as GitHub, and how to add Gradle build steps to build APK packages from source code.

#### Integrating with GitHub and other revision control systems

If you use GitHub or another revision control system to manage the source code for your app, you can configure Jenkins to run automated builds and run tests each time updates to your app are checked in. You can also configure Jenkins to run builds periodically.

To learn about configuring builds in Jenkins, see[Configuring automatic builds](https://wiki.jenkins-ci.org/display/JENKINS/Building+a+software+project#Buildingasoftwareproject-Configuringautomaticbuilds).

#### Adding Gradle build steps to rebuild APK packages

If you use a revision control system to manage source code for your app, you need to include a Gradle build step to create new APK binaries each time Jenkins downloads source code from your revision control system.

1. Add a build step to run the following commands in the main directory for your application:

   ```
   ./gradlew :app:assembleDebug
   ./gradlew :app:assembleDebugAndroidTest
   ```

   <br />

2. Add a build step to use the APK package(s) created by Gradle when testing withTest Lab. You can use this path as the**\<local_server_path\>** in the shell script example provided below, where**\<AppFolder\>**is the Android Studio project folder for your app:

   ```
   <AppFolder>/app/build/outputs/apk
   ```

   <br />

### AddTest Labbuild steps to Jenkins

Now you are ready to add a build step to Jenkins to runTest Labusing the gcloud command line.

#### To add a gcloud build step

1. From the main page for your project, click**Configure**.
2. On the**project configuration** page, scroll down to the**Build** section, and then choose**Execute shell** from the**Add build step**menu.

3. In the**Jenkins Execute shell command** window, enter the following, substituting**\<local_server_path\>** for the path to the sample app on the server,**\<app_apk\>** for your app's APK, and**\<app_test_apk\>**for your app's test APK:

   ```
   gcloud firebase test android run --app <local_server_path>/<app_apk>.apk
   --test <local_server_path>/<app_test_apk>.apk
   ```

   <br />

### Analyze test results

AfterTest Labcompletes testing of your app, you can review test results in theFirebaseconsole or in a[Google Cloud Storage](https://cloud.google.com/storage/)bucket in your project. You can also add a[`gsutil`](https://cloud.google.com/storage/docs/gsutil)command to the shell command shown above to copy the test results data to your local computer. To learn more, see[AnalyzingFirebase Test LabResults](https://firebase.google.com/docs/test-lab/analyzing-results).

## Continuous integration with other CI systems

To learn how to useFirebase Test Labwith other CI systems, check out their docs:

- [Bitrise](https://devcenter.bitrise.io/testing/device-testing-for-android/)
- [Circle CI](https://circleci.com/docs/2.0/language-android/#testing-with-firebase-test-lab)

| **Note:** If you create documentation explaining how to useFirebase Test Labwith another CI system,[contact us](mailto:cloud-test-lab-integration@google.com)so that we can review it for inclusion in this section.