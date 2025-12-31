# Source: https://firebase.google.com/docs/test-lab/android/instrumentation-test.md.txt

<br />

This guide describes how to prepare and run an instrumentation test usingFirebase Test Lab. To use this guide, you'll need an[instrumentation test](https://developer.android.com/training/testing/instrumented-tests)(written by you or your team) that uses the[Espresso](https://developer.android.com/training/testing/espresso)or[UI Automator](https://developer.android.com/training/testing/other-components/ui-automator)Android test frameworks. Instrumentation tests can run up to 45 minutes on physical devices and up to 60 minutes on[virtual devices](https://firebase.google.com/docs/test-lab/avds).

In the steps later, you'll upload your app's APK and your test's APK to Firebase.
| **Note:** Test Labno longer supports the Robotium Android test framework.

## (Optional) Add the screenshot library to your app

Firebase Test Labincludes a library (testlab-instr-lib) that you can use to process any screenshots you take with AndroidX's[ScreenCapture](https://developer.android.com/reference/androidx/test/runner/screenshot/ScreenCapture)when running instrumentation tests, such as tests written using the[Espresso test framework](https://android.github.io/android-test/docs/espresso/). This section describes how to create`ScreenCapture`objects with the AndroidX library and how to process them using testlab-instr-lib.

After your instrumentation test has run, you can view the captured screenshots in theFirebaseconsole.

### Try out a sample app

Download the[NotePad sample app](https://github.com/firebase/firebase-testlab-instr-lib/tree/master/notepad)to try out this functionality. The ability to take screenshots is already incorporated into the NotePad project.

## Step 1. Add the screenshot library to your project

1. In your test project's**root-level settings** Gradle file (`settings.gradle.kts`or`settings.gradle`), add Google's Maven repository to every`repositories`section:

   ```groovy
   pluginManagement {
       repositories {
           // Add the following line:
           google() // Google's Maven repository
           mavenCentral()
           gradlePluginPortal()
       }
   }
   dependencyResolutionManagement {
       repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
       repositories {
           // Add the following line:
           google() // Google's Maven repository
           mavenCentral()
       }
   }
   // ...
   ```
2. In your**module (app-level)** Gradle file (usually`<project>/<app-module>/build.gradle.kts`or`<project>/<app-module>/build.gradle`), add a dependency for theTest Labscreenshot library.

   ```carbon
   dependencies {
     // ...
     // Add Test Lab's instrumentation test screenshot library:
     androidTestImplementation("com.google.firebase:testlab-instr-lib:0.2")
     // ...
   ```
3. In your test's`AndroidManifest.xml`file, register the`FirebaseScreenCaptureProcessor`in a meta-data tag within the`<instrumentation>`element. You can also specify the processor as an argument in AndroidJUnitRunner instead (see the[AndroidJUnitRunner reference documentation](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner)for instructions on how).

       <instrumentation
         // Check that you have the following line (if not, add it):
         android:name="androidx.test.runner.AndroidJUnitRunner" // Specifies AndroidJUnitRunner as the test runner
         android:targetPackage="com.your.package.name">

       // Add the following:
       <meta-data
         android:name="screenCaptureProcessors"
         android:value="com.google.firebase.testlab.screenshot.FirebaseScreenCaptureProcessor" />
       </instrumentation>
       ...

4. In your app's`AndroidManifest.xml`file, add the following lines within the`<manifest>`element:

        <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>

5. In your`AndroidManifest.xml`file, specify system permissions for your app by adding the following lines within the`<manifest>`tag. If you're testing on**Android 10 (API level 29) or higher** , omit the`WRITE_EXTERNAL_STORAGE`permission (your app does not require this permission in order to read and write screenshots to the device).

   ```scdoc
   <manifest ... >
       <!-- WRITE_EXTERNAL_STORAGE is not needed on Android 10 (API level 29) or higher. -->
       <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
       <uses-permission android:name="android.permission.INTERNET"/>
       ...
   </manifest>
   ```

## Step 2. Take screenshots during your test

At any point in your test where you want to take a screenshot, call the`Screenshot.capture()`method from the AndroidX library. This produces a[`ScreenCapture`object](https://developer.android.com/reference/androidx/test/runner/screenshot/ScreenCapture). When you call`process()`on the`ScreenCapture`object, it gets processed using the[ScreenCaptureProcessor](https://developer.android.com/reference/androidx/test/runner/screenshot/ScreenCaptureProcessor)that's registered in your`AndroidManifest.xml`. Note that the`BasicScreenCaptureProcessor`is used if no processors are registered. Since you registered the`FirebaseScreenCaptureProcessor`, your screenshots will be processed via`FirebaseScreenCaptureProcessor`and will be available for you with your results when you run your test withFirebase Test Lab.

### Example use cases for creating a`ScreenCapture`:

- Take a full ScreenCapture on a API Build.VERSION_CODES.JELLY_BEAN_MR2 and above:

      Screenshot.capture()

- Take a`ScreenCapture`of the Activity on any API level. Note this is the only option for devices that are below Build.VERSION_CODES.JELLY_BEAN_MR2.

      @Rule
        public ActivityTestRule<MainActivity> activityRule = new ActivityTestRule<>(MainActivity.class);
      ...
      Screenshot.capture(activityRule.getActivity());
      ...

### Example use cases for processing a ScreenCapture

- Process a`ScreenCapture`via the`FirebaseScreenCaptureProcessor`:

      Screenshot.capture().process();

- Process a`ScreenCapture`via a specified`ScreenCaptureProcessor`(this allows you to skip registering the processor):

      Set<ScreenCaptureProcessor> processors = new HashSet<>();
      processors.add(new FirebaseScreenCaptureProcessor());
      Screenshot.capture().process(processors);

- Set the name and format of the`ScreenCapture`and process it using the registered processor:

      Screenshot.capture().setName("myscreenshot").setFormat(CompressFormat.JPEG).process();

## Step 3. Build and run your test

1. Build your app and test APKs (see[Test your app](https://developer.android.com/studio/test/index.html)for instructions).

2. Upload the APK files to the[Test Labdashboard](https://console.firebase.google.com/project/_/testlab)of theFirebaseconsole.

3. Finally, run your test.

## Step 4. View your test screenshots

After your test has completed, you can view any screenshots taken in theFirebaseconsole.

1. In the**Tests** tab, select your completed test, then click the**Results**tab.

2. Select your test again, then click the**Screenshots**tab that appears.

## (Optional) Enable additional test features

You can enable the following features in your test before running it withTest Lab:

### Enable Orchestrator

[Android Test Orchestrator](https://developer.android.com/training/testing/junit-runner.html#using-android-test-orchestrator)is a tool that runs each of your app's instrumentation tests independently.Test Labalways uses the latest version of Orchestrator.

To enable Orchestrator forTest Lab, in[instrumentation test setup,](https://console.firebase.google.com/project/_/testlab/run/instrumentation)click**Additional options** \>**Run with Orchestrator**.
| **Caution:** **To avoid spending quota on or being billed for malfunctioning tests, run Orchestrator locally before trying it inTest Lab.**Confirm that Orchestrator is working in your app by running a test on your own machine before uploading your APK. Keep in mind that testing with Orchestrator takes slightly longer than without it, and it might impact your billing or cause your tests to exceed your timeout limit.

When you use Orchestrator, you benefit from the following:

- No shared state. Each test runs in its own instrumentation instance, so a shared state doesn't accumulate across tests.
- Isolated crashes. If a test crashes, only that instrumentation is terminated, and other tests in your suite can still run.

Keep in mind that when you use Orchestrator, each test runs its own instrumentation instance, which means that the app process is restarted after every test case. The resulting increased run times might impact your[quota usage or billed time](https://firebase.google.com/docs/test-lab/usage-quotas-pricing)and might cause you to exceed your devices' timeout limits. If you reduce your app's startup time, this overhead will shorten.

To set additional options for Orchestrator, specify them via[`environmentVariables`field](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--environment-variables). For example, to use`clearPackageData`, use this option in gcloud:  

    --environment-variables clearPackageData=true

### Enable sharding

Test sharding divides a set of tests into sub-groups (shards) that run separately in isolation.Test Labautomatically runs each shard in parallel using multiple devices, and completes the entire set of tests in less time.

For example, if you create N shards, for each device you select,Test Labspins up N identical devices and runs a subset of the tests on each device. This means that sharded test cases can result in multiple test executions per device. Non-sharded test cases, however, result in one test execution per device. To learnTest Labconcepts, see[Key concepts](https://firebase.google.com/docs/test-lab/android/analyzing-results#key_concepts).

To enable test sharding in theFirebaseconsole, follow these steps:

1. In[instrumentation test setup,](https://console.firebase.google.com/project/_/testlab/run/instrumentation)click**Additional options**.

2. In the**Sharding**section, enter the number of shards you want to run.

### Billing for test shards

Test Labimplements your shards by leveraging[AndroidJUnitRunner's built-in sharding mechanism.](https://developer.android.com/training/testing/junit-runner#sharding-tests)To avoid being charged for spinning up empty shards (shards without assigned test cases), the number of shards you create should be less than the total number of test cases. Depending on how long each test case takes to run, it's typically a good idea to assign 2-10 test cases per shard.
| **Caution:** **Sharding tests may cost more.** Although test sharding reduces the time it takes for all your tests to run, the overhead of starting your app on each shard may increase individual device times (the time it takes for a device to run its tests). Because charges are calculated on a per-minute basis for each shard, your total charges may increase. In addition, shards are counted towards[your daily quota](https://firebase.google.com/docs/test-lab/usage-quotas-pricing#testing-quota)for test executions.

For more information on billing, read[Usage, quotas, and billing](https://firebase.google.com/docs/test-lab/usage-quotas-pricing).