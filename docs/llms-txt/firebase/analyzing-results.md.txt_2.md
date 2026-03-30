# Source: https://firebase.google.com/docs/test-lab/ios/analyzing-results.md.txt

# Analyzing Test Results

Whether you run your tests through the [Firebase console](https://console.firebase.google.com/)
or the [Firebase CLI](https://firebase.google.com/docs/cli), you can find your detailed test
results in the Firebase console. Read on to learn how to analyze your test
results.

## View test results

After you upload or select a test and specify your test devices, you can view a
summary of your test results (including logs, videos, and screenshots) in the
Test Lab dashboard of the Firebase console. Your raw test results are also
stored in a Google Cloud bucket for easier use with CI systems.

To see test results head to the **Test Lab** section of the [Firebase console](https://console.firebase.google.com/project/_/testlab).

You'll find a list of all of your previous test runs there. To understand the
the results, it helps to know a bit about test matrices:
When you run a test or a set of test cases against devices and configurations
you've selected, Test Lab runs the test against your app in a batch, then
displays the results as a **test matrix**.

**Devices × Test Executions = Test Matrix**

Device
:   A physical or virtual device (Android only) you run a test on, such as a
    phone, tablet, or wearable device. Devices in a test matrix are identified by
    device model, OS version, screen orientation, and locale (also known as
    geography and language settings).

Test, test execution
:   A test (or a set of test cases) to be run on a device. You can run one test
    per device, or optionally shard the test and run its test cases on
    different devices.

Test matrix
:   Contains the statuses and test results for your test executions. If any
    test execution in a matrix fails, the whole matrix fails.

## Interpret test matrix results

If you start your tests in Firebase console, Test Lab takes you right to
your in-progress test matrix, where you can watch your tests' progress as it
happens. If you used the command line tool instead, you can follow the URL it
provides to get to the in-progress test matrix page.

The matrix has a line for each test execution Test Lab runs. The icon before
the execution name displays that execution's status:

- play_circle_outline **In progress:** The test execution is still running. Executions can take up to an hour to complete, depending on the number and complexity of tests in your app.
- check_circle **Passed:** None of the execution's tests failed.
- warning **Failed:** At least one of the execution's tests failed.
- error **Inconclusive:** The test results were inconclusive, possibly due to a Test Lab error.
- block **Skipped:** Test Lab skipped your test, because the device/OS version combination you selected is unavailable.

> [!NOTE]
> **Note:** **Device issues sometimes increase test execution time.** If you notice that a test is taking longer than usual, it could be a sign of an issue in Test Lab. Don't worry, though, Test Lab only charges you for the time your test is actually running.

## Interpreting results from a single test execution

From the test matrix results page, click one of the test executions to see
the result of that specific test execution.

The page shows you stats for that test execution, including issues encountered
in testing, a list of test cases, logs from the execution, and a video of the
test running.

## Detailed test results

Detailed test results are available in a Google Cloud Storage bucket for
90 days. Click **View Source Files** in a test execution result page to see the
bucket.

To retain detailed test results for longer than 90 days, send the test results
to a more-permanent Cloud Storage bucket that you own using the
[**--results-bucket** gcloud command-line option](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run).
You can then set the **Age** setting to determine how long Cloud Storage
stores the results. For more information on how to change the **Age** setting,
see [Lifecycle
conditions](https://cloud.google.com/storage/docs/lifecycle#conditions).

> [!NOTE]
> **Note:** The project that owns this Cloud Storage bucket must have billing enabled to retain detailed test results for longer than 90 days.