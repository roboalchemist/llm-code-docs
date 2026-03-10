# Source: https://firebase.google.com/docs/test-lab/android/firebase-console.md.txt

# Start testing with the Firebase console

Firebase Test Lab provides cloud-based infrastructure for testing
Android apps. This document describes how to get started with Test Lab using the
Firebase console.

Test Lab lets you run the following types of tests:

- [Instrumentation test](https://firebase.google.com/docs/test-lab/android/instrumentation-test):
  A test you write that allows you to drive the UI of your app with the actions
  you specify. An instrumentation test can also make explicit assertions about
  the state of your app to verify correct functionality using
  [AndroidJUnitRunnerAPIs](https://developer.android.com/reference/android/support/test/runner/AndroidJUnitRunner). Test Lab supports
  [Espresso](https://developer.android.com/training/testing/espresso)
  and
  [UI Automator](https://developer.android.com/training/testing/other-components/ui-automator) instrumentation test frameworks.

- [Robo test](https://firebase.google.com/docs/test-lab/android/robo-ux-test):
  A test that analyzes your app's interface and then explores it automatically
  by simulating user activities.

- [Game loop test](https://firebase.google.com/docs/test-lab/android/game-loop): A test
  that uses a "demo mode" to simulate player actions in game apps.

## Before you begin

Your Firebase project must be on the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing), which means that
your project is linked to a Cloud Billing account. You can
[upgrade to the Blaze pricing plan](https://console.firebase.google.com/project/_/overview?purchaseBillingPlan=metered)
in the Firebase console. You need to be an Owner or Editor for your project
to link a Cloud Billing account.

## Step 1. Create a Firebase project

If you haven't yet, go to the [Firebase console](https://console.firebase.google.com/)
and create a new Firebase project.

> [!NOTE]
> **Note:** If you're working on a shared Firebase project, you'll need to have ownership or edit permissions for the project.

## Step 2. Run a test

### Instrumentation test

> [!NOTE]
> **Note:** If you want to run an instrumentation test with [Android Test Orchestrator](https://developer.android.com/training/testing/junit-runner.html#using-android-test-orchestrator), see [Enable Orchestrator](https://firebase.google.com/docs/test-lab/android/instrumentation-test#orchestrator).

1. On the [Firebase console](https://g.co/firebase) navigation bar,
   click **Test Lab** , and then click **Get Started -\> Run an Instrumentation
   test**.

2. Click **Browse** , and then browse to your app APK or AAB and test APK or
   AAB before clicking **Continue**.

3. Define your test matrix by selecting which devices, Android API levels,
   screen orientations and locales you want to test your app against. You can
   select only those device and Android API level combinations that you want
   to target for testing.

4. (Optional) Click **Show advanced options** to change the Test timeout
   that determines the maximum duration of each test execution.

5. (Optional) To help you identify and locate your test matrices in the
   Firebase console, you can add a label to your test matrix by entering a
   label name in the **Test matrix label (optional)** field.

6. Click **Start *N* Tests**, where "N" is the number of valid test
   configurations from the test matrix that you define on this screen. Each
   pending test is shown with a blue clock icon while it is waiting to run,
   and that icon changes to a green check icon when the test has completed.

7. After each test has run, click the device listed in the Test Execution
   column to see test results, including test cases, logs, screenshots and
   videos.

### Robo test

1. On the [Firebase console](https://g.co/firebase) navigation bar,
   click **Test Lab** , and then click **Get Started -\> Run a Robo test**.

2. Click **Browse** , browse to your app APK, and then click **Continue**.

3. Define your test matrix by selecting which devices, Android API levels,
   screen orientations and locales you want to test your app against.

4. (Optional) Click **Show advanced options** to change the following options:

   - Test timeout determines the maximum duration of each test execution.
   - Test account credentials are usedis used to provide credentials for a test account.

   > [!CAUTION]
   > **Caution:** Never use this option with real user accounts.

   - Additional fields are used to provide text input for other text fields in your app.

   > [!NOTE]
   > **Note:** To learn more about Test account credentials and additional fields, see [Test account sign-in and predefined text](https://firebase.google.com/docs/test-lab/robo-ux-test#test_account_sign-in_and_predefined_text_input).

5. (Optional) To help you identify and locate your test matrices in the
   Firebase console, you can add a label to your test matrix by entering
   a label name in the **Test matrix label (optional)** field.

6. Click **Start *N* Tests**, where "N" is the number of valid test
   configurations from the test matrix that you define on this screen. Each
   pending test is shown with a blue clock icon while it is waiting to run,
   and that icon changes to a green check when the test has completed.

7. After each test finishes running, click the device listed in the Test
   Execution column to see test results, including test cases, logs,
   screenshots and videos.

If you want to create a script to guide the Robo test, see
[Record a Robo script using Test Lab in Android Studio](https://firebase.google.com/docs/test-lab/android/run-robo-scripts#record-android-studio).

### Game Loop test

1. On the Test Lab page of the [Firebase console](https://console.firebase.google.com/project/_/%0Atestlab), click **Run Your First Test \> Run an Android Game Loop**.

2. In the **Upload App** section, click **Browse** , then select your app's
   APK file (if you haven't already, [generate an APK file](https://firebase.google.com/docs/test-lab/android/game-loop#run-testlab) for your app).

3. (Optional) To help you identify and locate your test matrices in the
   Firebase console, you can add a label to your test matrix by entering
   a label name in the **Test matrix label (optional)** field.

4. (Optional) If you want to run multiple loops or scenarios at a time, or
   select specific loops to run, enter the loop numbers in the
   **Scenarios** field.

   For example, when you enter "1-3, 5", Test Lab runs loops 1, 2, 3, and 5.
   By default (if you don't enter anything in the **Scenarios** field),
   Test Lab only runs loop 1.
5. In the **Devices** section, select one or more physical devices you
   want to test your app on, then click **Start Tests**.

## Step 3. Investigate your test results

When the test starts, you're automatically redirected to the test results page.
Tests can take a number of minutes to run, depending on the number of different
configurations you have selected and the test timeout duration set for your
tests. After your tests have run, you can review test results. See
[Analyzing Firebase Test Lab Results](https://firebase.google.com/docs/test-lab/android/analyzing-results) to learn more
about how to interpret the test results.

> [!NOTE]
> **Note:** For all test types, any uncaught exception will cause a test failure.