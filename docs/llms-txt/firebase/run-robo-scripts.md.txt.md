# Source: https://firebase.google.com/docs/test-lab/android/run-robo-scripts.md.txt

# Run a Robo script (Android)

This document describes how to use *Robo scripts* , which are tests that
automate manual QA tasks for mobile apps, and enable continuous integration
(CI) and pre-launch testing strategies. For example, you can use Robo scripts
to test a common user journey or provide specific user interface (UI) input,
like a username and password. Robo scripts are a feature of
[Robo test](https://firebase.google.com/docs/test-lab/android/robo-ux-test).

With Robo scripts, you record yourself walking through a workflow in your app,
then you upload that recording to the Firebase console to run in Robo
tests. When you run a Robo test with a script attached, Robo first steps
through your pre-scripted actions and then explores the app as usual.

Robo scripts use [Robo test](https://firebase.google.com/docs/test-lab/android/robo-ux-test)
as the test engine. In its most basic form, a Robo script consists of a
sequence of UI actions like *enter text 'username'* and
then *tap the OK button* . Robo scripts can also include actions like waiting
for an element to appear, tapping at a specific point within an element, and
executing Android Debug Bridge (`adb`) shell commands.

Robo scripts have the following advantages over traditional testing frameworks:

|---|---|
| **Capability** | **Description** |
| Highly robust | Robo scripts can tolerate significant structural and behavioral differences between app versions and app flakiness. |
| Open-ended | After a Robo script completes, the base Robo test can take over and continue testing the app. This continued testing approach enables several key use cases. For example, you can use a Robo script to bring an app into a particular state by performing a custom sign-in flow. |
| Recordable | You don't need to code Robo scripts manually. They can be recorded using the Robo script recorder in Android Studio. Creating or modifying Robo scripts typically doesn't require any knowledge of mobile development. |
| Flexible | Robo scripts can interact with non-native UI elements that are common in games. |

Robo scripts are conditionally triggered during a Robo test, which lets users
augment Robo's behavior - typically to achieve greater coverage or target
specific functionality. In contrast to traditional testing frameworks,
Robo scripts support the following:

- Various triggering conditions, for example, a particular app package name being active (or not) or a specific element being displayed on the screen (or not).
- Execution controls, for example, a maximum number of executions, priority, relevant crawl stage.
- Unconventional action types (conditional, element-ignoring, screen-closing).

We recommend that you use Robo scripts whenever possible because they can be
maintained effortlessly. For example, you can use a Robo script to do the
following:

- Navigate significant workflows to get to the core of an app's functionality. For example, you can perform a sign-in, set up an app's state after the first launch, and register a new user.
- Focus Robo on a particular part of an app to get the most out of Robo test time. Robo script guides Robo test to reach the relevant part of an app, where Robo test resumes a fully automated crawl.
- Bring an app into a specific state or screen to perform an analysis, for example, to analyze an in-app message, privacy policy, or specific level of a game.
- Perform an end-to-end instrumentation test, with or without Robo test resuming a fully automated crawl after the Robo script is complete.

Use more advanced Robo script features to do the following:

- Perform actions before Robo starts crawling the app-under-test or after a crawl is finished, for example, clean the app-under-test data before a crawl, or change device settings.
- Change aspects of Robo behavior during a crawl, in particular:
  - Make Robo ignore some UI widgets or app screens.
  - Provide a custom action for Robo to perform when backtracking from a particular screen.
  - Make Robo perform specific actions whenever a particular app screen is encountered during a crawl.
- Completely customize how Robo performs a crawl. For example, use a combination of conditional and non-conditional actions to keep the app-under-test in the background throughout the crawl, while performing device manipulations and dismissing any popup dialogs that appear along the way.

Keep in mind that Robo scripts don't replace all kinds of tests. You still
need unit tests to catch low-level logic bugs in your app; these tests
typically don't require an Android or iOS environment. We recommend that you
supplement Robo script tests with targeted instrumentation tests that can have
specific, detailed assertions about business logic, which are best expressed
in code.

### Record a Robo script using Test Lab in Android Studio

The Robo script recorder in Android Studio lets you record Robo scripts by
interacting directly with the app on your device. Follow these instructions
to get started with Robo scripting through the Firebase tool in Android Studio:

1. Open [Android Studio](https://developer.android.com/studio)
   and select **Tools -\> Firebase**.

2. In the Firebase pane, click
   **Record Robo Script and Use it to Guide Robo Test**.

3. Click **Record Robo script**. The Select Deployment Target dialog
   appears.

4. Select the device in which you want to record the Robo script.

5. After you record the Robo script in the device, save the file as a JSON file
   in the desired location.

6. Open the Test Lab page in the Firebase console and upload the JSON
   script file and the application APK.

7. Click the **Continue** button. You are prompted to select the device and
   API level. After the test script completes, Test Lab generates the
   test report.

8. (Optional) To copy or download the logcat of the test report and the video,
   click **View Source Files**.

> [!NOTE]
> **Note:** Robo script recordings don't capture your actions outside the tested app. For example, sign-ins through Facebook, Twitter, and other social apps aren't recorded.

By default, Robo script robustness mechanisms prevent it from failing early.
If you choose the `strict` execution mode and a Robo script fails at any point,
Test Lab abandons all further steps in the script and resumes a regular
Robo crawl. Most often, Robo scripts fail because Robo can't find a required
element on the screen. To avoid failures, make sure that your app navigation is
predictable and that your screens are shown in a deterministic order.

### Run a Robo script in Test Lab

To run a Robo script in Test Lab, follow these instructions:

1. Open the Test Lab page in the Firebase console.

2. Upload the app's APK or AAB in the **App APK or AAB field**.

3. Upload your recorded or manually created Robo script file in the
   **Robo script (optional)** field.

### Provide a Robo script to a local Robo test run

To provide a Robo script to a local Robo test run, use the following Robo test
option:

`--robo-script-file <robo-script-path>`

Replace `<robo-script-path>` with a path to your Robo script file in the local
file system. Follow the [instructions for a local Robo test
run](https://developer.android.com/training/testing/crawler).

### Specify a Robo script in a gcloud CLI test invocation

To specify a Robo script in a gcloud CLI test invocation, use the following
gcloud CLI flag:

    --robo-script = <robo-script-path>

Replace `<robo-script-path>` with a path to your Robo script file in the local
file system or in Cloud Storage using `gs://` notation. For example:

    gcloud firebase test android run --app = <path_to_app_apk_file> --robo-script = <robo-script-path>

## Next steps

- To learn about Robo scripts structure, capabilities, usage, and actions, see the [Robo scripts reference guide](https://firebase.google.com/docs/test-lab/android/robo-scripts-reference).
- [Run a Robo test](https://firebase.google.com/docs/test-lab/android/robo-ux-test).