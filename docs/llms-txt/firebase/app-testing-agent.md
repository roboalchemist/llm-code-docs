# Source: https://firebase.google.com/docs/app-distribution/android/app-testing-agent.md.txt

<br />

| The App Testing agent feature is a**preview**release. A preview release is not subject to any SLA or deprecation policy and may receive limited or no support.
|
| In order to use the App Testing agent, you will need to opt-in to the feature from the[Firebaseconsole](https://console.firebase.google.com/project/_/appdistribution). For information, see[Accessing the App Testing agent preview](https://firebase.google.com/docs/app-distribution/troubleshooting?platform=android#app-testing-agent-preview).

The App Testing agent is a test case generation, management, and execution agent powered by Gemini inFirebase. You define test goals in natural language, and the agent uses AI to understand and navigate your app, simulate user interactions, and provide detailed test results.

## How App Testing agent uses your data

App Testing agent is provided by[Gemini inFirebase](https://firebase.google.com/docs/gemini-in-firebase)and is governed under the same terms. See[How Gemini inFirebaseuses your data](https://firebase.google.com/docs/gemini-in-firebase#how-gemini-in-firebase-uses-your-data)for more information about how Gemini inFirebaseuses your data.

## Before you begin

If you haven't already,[register your app with Firebase](https://firebase.google.com/docs/android/setup#console).

If you aren't using any other Firebase products, you only have to create a project and register your app. You don't need to add any SDKs to your app. However, if you decide to use additional products in the future, be sure to complete all of the steps in[Add Firebase using theFirebaseconsole](https://firebase.google.com/docs/android/setup#console).
| **Caution:** When you register your app with Firebase, make sure to enter the same package name as the app you're distributing. The package name value is case-sensitive and cannot be changed for your app in Firebase after it's registered with your Firebase project.

When you're ready to distribute a pre-release version of your app to testers, build your APK or AAB, using your normal process, and upload it to App Distribution in the[Firebaseconsole](https://console.firebase.google.com/project/_/appdistribution). You must sign the APK with your debug key or app signing key.

## Create a test case

To run AI-guided tests, the App Testing agent uses your natural language test cases to execute tests against your app.

Each test case is broken down into steps, which will be executed in sequence. Steps allow you to break up your test case into phases, each with their own success criteria. The agent may take many actions during any one step.

To create a test case, open theApp Distributionpage of the[Firebaseconsole](https://console.firebase.google.com/project/_/appdistribution)and take the following steps:

1. On the**Test Cases** tab, click**New test case** . If you don't want to create your own test case, you can modify or use the provided[example test case](https://firebase.google.com/docs/app-distribution/android/app-testing-agent#test-cases).
2. In the**Add test case**dialog, give the test case a name. This is used to identify the test, but is ignored by the agent.
3. (Optional) Select a**Prerequisite test case**that contains set-up steps to run before the main test. If the prerequisite test fails, the entire test will be marked as a failure. Steps and outcomes from the prerequisite and main tests will be shown together in the test results.
4. Consider breaking your test into multiple steps, by clicking the**Add another step**button.
5. Give each step a**Goal**that describes what the App Testing agent should do during that step.
6. (Optional) Add a**Hint**to provide additional information to help the App Testing agent understand and navigate your app during that step.
7. (Optional) Add**Success Criteria**to help the App Testing agent determine when the step has been successfully completed.
8. Click**Save**once you're done customizing your test.

### Example test case

The following is an example of how to create a test case using the App Testing agent:

|                                                   Testing the home page                                                   ||
|------------------------|---------------------------------------------------------------------------------------------------|
| ##### Test title       | Home page loads                                                                                   |
| ##### Goal             | Load the home page                                                                                |
| ##### Hint             | Navigate past any onboarding screens. Dismiss any popups. Don't sign in.                          |
| ##### Success Criteria | The main app home page is visible on screen, all images have loaded, and no errors are displayed. |

## Run a test

The App Testing agent lets you run**AI-guided tests** in the console by clicking the**Run tests**button from either the Releases or Test Cases page. This opens the App Testing agent customization screen, where you can choose one or more of your existing test cases for the agent to execute. You can also choose the devices you want to test against, and whether to provide any login credentials.

You can also choose to run a**Random crawl test** by changing the test type. Random crawl tests use the[Automated Tester](https://firebase.google.com/docs/app-distribution/android-automated-tester)feature.

You can view the results of your tests from the**Releases** page in the**App Testing agent** tab of a release. The**View details**button will open the Test Results dialog and show you any issues, screenshots of the app, and the actions that Gemini took during the test.
| **Note:** You can add a system variable to your app behavior to modify the way that it behaves when being run by the App Testing agent. For more information, see[Run tests with Android Studio](https://firebase.google.com/docs/test-lab/android/android-studio#modify_instrumented_test_behavior_for).

## Automatically test your builds

To automatically run App Testing agent tests on your new builds, for example from CI/CD pipelines, you can distribute your builds to the agent usingApp Distribution's Gradle or fastlane plugins, or the Firebase CLI.

<br />

### Automatically test your builds with the Firebase CLI

<br />

You must specify at least one test device and one test case ID to use the App Testing agent feature. Test case IDs can be found and downloaded on the Test Cases page of theFirebaseconsole. For more information on getting started with the Firebase CLI and different ways to configure your distribution, see[Distribute Android apps to testers using the Firebase CLI](https://firebase.google.com/docs/app-distribution/android/distribute-cli?apptype=apk#step_2_distribute_your_app_to_testers).

Run the`appdistribution:distribute`command to upload your app, and use the following parameters to configure your distribution to the App Testing agent feature:

|                                                                                                                                                                                                                                                                                                         appdistribution:distribute options                                                                                                                                                                                                                                                                                                          ||
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--test-devices`or`--test-devices-file`   | The test devices you want to distribute builds to the App Testing agent feature. You can specify the test devices as a semicolon-separated list of test devices: `--test-devices "model=tokay,version=36,locale=en,orientation=portrait;model=b0q,version=33,locale=en,orientation=portrait"` Or, you can specify the path to a plain text file containing a semicolon-separated list of test devices: `--test-devices-file "/path/to/test-devices.txt"` You can look up the available device models using the[gcloud CLI](https://firebase.google.com/docs/test-lab/android/available-testing-devices). |
| `--test-username`                         | The username for automatic login to be used during tests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `--test-password`or`--test-password-file` | The password for automatic login to be used during tests. Or, you can specify the path to a plain text file containing a password: `--test-password-file "/path/to/test-password.txt"`                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `--test-non-blocking`                     | Run tests asynchronously. Visit the Firebase console for the automatic test results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `--test-case-ids`or`--test-case-ids-file` | A comma-separated list of test case IDs for running AI-powered automated tests: `--test-case-ids "load-app,play-the-first-level"` Or, you can specify the path to a plain text file containing a comma or newline separated list of test case IDs: `--test-case-ids-file "/path/to/test-case-ids.txt"`                                                                                                                                                                                                                                                                                                   |

<br />

<br />

<br />

### Automatically test your builds with Gradle

<br />

You must specify at least one test device and one test case ID to use the App Testing agent feature. Test case IDs can be found and downloaded on the Test Cases page of theFirebaseconsole. For more information on getting started with Gradle and different ways to configure your distribution, see[Distribute Android apps to testers using Gradle](https://firebase.google.com/docs/app-distribution/android/distribute-gradle?apptype=apk#step_3_configure_your_distribution_properties).

You can configureApp Distributionby adding at least one`firebaseAppDistribution`section and use the following parameters to configure the distribution to the App Testing agent feature:

|                                                                                                                                                                                                                                                                                                        App DistributionBuild Parameters                                                                                                                                                                                                                                                                                                         ||
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `testDevices`or`testDevicesFile`   | The test devices you want to distribute builds to the App Testing agent feature. You can specify the test devices as a semicolon-separated list of device specifications `testDevices="model=tokay, version=36, locale=en, orientation=portrait;model=b0q, version=33, locale=en, orientation=portrait"` Or you can specify the path to a file containing a semicolon-separated list of device specifications: `testDevicesFile="/path/to/testDevices.txt"` You can look up the available device models using the[gcloud CLI](https://firebase.google.com/docs/test-lab/android/available-testing-devices). |
| `testUsername`                     | The username for automatic login to be used during tests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `testPassword`or`testPasswordFile` | The password for automatic login to be used during tests. Or, you can specify the path to a plain text file containing a password: ``` testPasswordFile="/path/to/testPassword.txt" ```                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `testNonBlocking`                  | Run tests asynchronously. Visit the FIrebase console for the automatic test results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `testCases`or`testCasesFile`       | A comma-separated list of test case IDs for running AI-powered automated tests: `testCases: "load-app,play-the-first-level"` Or, you can specify the path to a plain text file containing a comma or newline separated list of test case IDs: `testCasesFile: "/path/to/test-case-ids.txt"`                                                                                                                                                                                                                                                                                                                 |

<br />

<br />

<br />

### Automatically test your builds with fastlane

<br />

You must specify at least one test device and one test case ID to use the App Testing agent feature. Test case IDs can be found and downloaded on the Test Cases page of theFirebaseconsole. For more information on getting started with fastlane and different ways to configure your distribution, see[Distribute Android apps to testers using fastlane](https://firebase.google.com/docs/app-distribution/android/firebase.google.com/docs/app-distribution/android/distribute-fastlane?apptype=apk#distribute).

In a`./fastlane/Fastfile`lane, add a`firebase_app_distribution`block. Use the following parameters to configure your distribution to the App Testing agent feature:

|                                                                                                                                                                                                                                                                                                        firebase_app_distribution parameters                                                                                                                                                                                                                                                                                                         ||
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `test_devices`or`test_devices_file`   | The test devices you want to distribute builds to the App Testing agent feature. You can specify the test devices as a semicolon-separated list of test devices: `test_devices: "model=tokay, version=36, locale=en, orientation=portrait;model=b0q, version=33, locale=en, orientation=portrait"` Or, you can specify the path to a plain text file containing a semicolon-separated list of test devices: `test_devices_file: "/path/to/test-devices.txt"` You can look up the available device models using the[gcloud CLI](https://firebase.google.com/docs/test-lab/android/available-testing-devices). |
| `test_username`                       | The username for automatic login to be used during tests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `test_password`or`test_password_file` | The password for automatic login to be used during tests. Or, you can specify the path to a plain text file containing a password: `test_password_file: "/path/to/test-password.txt"`                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `test_non_blocking`                   | Run tests asynchronously. Visit the Firebase console for the automatic test results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `test_case_ids`or`test_case_ids_file` | A comma-separated list of test case IDs for running AI-powered automated tests: `test_case_ids: "load-app,play-the-first-level"` Or, you can specify the path to a plain text file containing a comma or newline separated list of test case IDs: `test_case_ids_file: "/path/to/test-case-ids.txt"`                                                                                                                                                                                                                                                                                                         |

<br />

<br />

## Import \& export test cases with YAML files

Importing test cases from YAML files is useful when you want to manage test cases outside of theFirebaseconsole. It can also be useful to export test cases to move them between projects. You can use an LLM to refine existing test cases or create new test cases. You can import and export test cases from the Test Cases page in theFirebaseconsole or programmatically using the Firebase CLI. An example:  

    - displayName: Setup
      id: setup
      steps:
        - goal: Log in
          hint: Any username and password will work
    - displayName: Smoke test
      id: smoke_test
      prerequisiteTestCaseId: setup
      steps:
        - goal: Go through the onboarding flow
          hint: Tap the next button until you reach the home screen
          successCriteria: The main app home page is visible
        - goal: Open the settings page
          hint: The settings button is in the top right corner
          successCriteria: The settings page is visible

## Debug your test results

If your test results are different from what you expected, you can debug your test using the**Show agent view** toggle under**View details**on the Test Results page. The agent view shows you the on screen elements that the App Testing agent was able to detect when using the app's accessibility information. If you would like to take a closer look at what the agent saw, you can download that information from the action overflow menu.

You can also use the**View artifacts**button on the Test Results page to look at all of the videos, logs, and other Cloud artifacts for your test results.

## Known issues and limitations

The App Testing agent preview has some known limitations:

- Because the App Testing agent uses generative AI to test your app, it will sometimes take different actions while still following the same instructions.
- The App Testing agent only supports the following actions: tap, enter text, swipe up/down/left/right, long press, drag-and-drop, back, and wait.
- The App Testing agent has trouble executing tests containing only a single step that takes many actions to accomplish. It performs better when complex tasks are broken up into multiple shorter steps.
- The App Testing agent sometimes won't scroll to expose other elements off screen. This happens more often when there is no visual indication of scrollability. As a workaround, the "hints" field can be used to suggest scrolling.
- The App Testing agent sometimes has trouble counting, for example performing an action a specific number of times.
- The App Testing agent cannot navigate your app if[`FLAG_SECURE`](https://developer.android.com/security/fraud-prevention/activities#flag_secure)is enabled. Instead of screenshots of your app, it will only see a blank screen.

## Testing quotas

During the preview, the AI-guided tests will be offered at no cost within a quota limit. The default quota limit is 200 tests per month, per Firebase project.

Note that if you choose to run multiple test cases, or run the same test case, on multiple devices, this counts as multiple tests. For example, if you run 2 test cases on 2 devices, this counts as a total of 4 tests.

To increase your quota above the default limit, contact[Firebase Support](https://firebase.google.com/support)with your use case.