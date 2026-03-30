# Source: https://firebase.google.com/docs/test-lab/troubleshooting.md.txt

# Test Lab troubleshooting &amp; FAQ

This page provides troubleshooting help and answers to frequently asked
questions about running tests with Firebase Test Lab. Known issues are also
documented. If you can't find what
you're looking for or need additional help, join the [#test-lab
channel](https://firebase-community.slack.com/messages/test-lab) on
Firebase Slack or contact [Firebase
support](https://support.google.com/firebase/contact/support).

## Troubleshooting

<br />

#### Why is my test taking so long to run?

<br />

When you select a device with a high capacity level in the Test Lab
catalog, tests may start faster. When a
device has low capacity, tests might take longer to run. If the number of
tests invoked is much larger than the capacity of the selected devices, tests
can take longer to finish.


Tests running on any level device capacity level may take longer due to the
following factors:

- Traffic, which affects device availability and test speed.
- Device or infrastructure failures, which can happen at any time. To check if there is a reported infrastructure for Test Lab, see the [Firebase status dashboard](https://status.firebase.google.com/summary).


To learn more about device capacity in Test Lab, see device capacity
information for [Android](https://firebase.google.com/docs/test-lab/android/available-testing-devices#device-capacity) and [iOS](https://firebase.google.com/docs/test-lab/ios/available-testing-devices#device-capacity).

<br />

<br />

<br />

#### Why am I receiving inconclusive test results?

<br />

Inconclusive test outcomes commonly occur either because of canceled test runs
or infrastructure errors.

Infrastructure errors are caused by internal Test Lab issues, like network
errors or unexpected device behaviors. Test Lab internally retires test runs
that produce infrastructure errors multiple times before reporting an
inconclusive outcome; however, you can disable these retries using
[failFast](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices#TestMatrix.FIELDS.fail_fast).

To determine the cause of the error, follow these steps:

1. Check for known outages in the [Firebase status dashboard](https://status.firebase.google.com/summary).
2. Retry the test in Test Lab to verify that it is reproducible.

   > [!NOTE]
   > **Note:** Test Lab does not charge you for infrastructure errors.

3. Try running the test on a different device or device type, if applicable.

If the issue persists, contact the Test Lab team in the
[#test-lab channel](https://firebase-community.slack.com/messages/test-lab) on
Firebase Slack.

<br />

<br />

<br />

#### Why did sharding make my tests run
longer?

<br />

Sharding can cause your tests to run longer when the number of shards you
specified exceeds the number of devices available for use in Test Lab. To
avoid this situation, try switching to a different device. For more information
about choosing a different device, see

[Device Capacity](https://firebase.google.com/docs/test-lab/ios/available-testing-devices#device_capacity).


<br />

<br />

<br />

#### Why is it taking a long time for my
test to start?

<br />

When you submit a test request, your app is first validated, re-signed, etc. in
preparation for running tests on a device. Normally, this process completes in
less than a few seconds, but it can be affected by factors like the size of your
app.

After your app is prepared, test executions are scheduled and remain in a queue
until a device is ready to run it. Until all test executions finish running,
the matrix status will be "Pending" (regardless of whether test executions are
in the queue or actively running).

> [!NOTE]
> **Note:** The time your test spends waiting for an available device does not count toward your billing time.

<br />

<br />

<br />

#### Why is it taking a long time for my
test to finish?

<br />

After the test execution is finished, test artifacts are downloaded from the
device, processed, and uploaded to Cloud Storage. The duration of this step can
be affected by the amount and size of the artifacts.

<br />

<br />

<br />

### Android-specific troubleshooting

<br />

#### App not returning data and can't locate screenshots

<br />

Test execution artifacts (such as screenshots and log files) are stored in
Google Cloud Storage and directly rendered into the Firebase console. If
your test execution was performed within the last 90 days, check that you have
assigned project level roles (project owner, project editor, or project viewer).
Please also make sure that Cloud Audit Logging is not enabled for your project
or your organization.

If the execution was performed more than 90 days ago, most
likely the test artifacts have been automatically deleted. You can check the
result bucket configuration by clicking the **Test results** tab in the
Test Lab dashboard. The default result
bucket is configured to retain objects for 90 days.

To retain your test artifacts longer, run the command
`gcloud firebase test android run` with the flag `--results-bucket` and pass in
the name of the result bucket. For more information, visit the
[`gcloud firebase test android run` reference documentation](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run).

<br />

<br />

<br />

#### Why am I receiving partial or missing instrumentation test case results?

<br />

When you run instrumentation tests, you might see test errors indicating partial
results that contain messaging like `Test run failed to complete. Expected
x tests, received y` (where `y` is less than `x`).
This error means that Test Lab could not parse the logcat for test case start
or end markers that are usually generated by
[AndroidJUnitRunner](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner).

The following are common causes of this issue:

| Issue description | Possible resolution |
|---|---|
| Test case did not run because of a timeout. If the total duration of the tests is longer than a timeout you specified or longer than a [max timeout](https://firebase.google.com/docs/test-lab/android/get-started#prepare-test), Test Lab cancels the rest of the test cases. | - Increase the timeout for the matrix to make sure all tests can complete. - Shard the tests if you did not already do so, so that each shard runs a subset of the tests and completes in a shorter period of time. - If you already enabled sharding, increase the number of shards. |
| The test case failed to complete because it exited prematurely or got stuck. The test case may exit prematurely because of an uncaught exception or assertion error. Test cases can get stuck in an infinite loop or might be unable to proceed, for example, if the app does not show the correct view and the test case can't perform the action on the UI. | Check the video and the `logcat` to investigate where the test stopped. |
| A custom test runner (including extending AndroidJUnitRunner) crashed unexpectedly or wrote unexpected test case start or end markers to `logcat`. | Check your test runner code. |
| Excessive logs were written to `logcat`, which overwhelmed the buffer or crashed the `logcat` process. | Reduce writes to `logcat`. |
| The app under test crashed. | Debug your app. |

<br />

<br />

<br />

*** ** * ** ***

## Frequently asked questions (FAQ)

<br />

#### What are the no-cost quotas
for Test Lab? What should I do if I run out?

<br />

Firebase Test Lab offers no-cost quotas for testing on devices and for using
Cloud APIs. Note that the testing quota uses the standard Firebase pricing plan,
while the Cloud API quotas do not.

- **Testing quota**

  Testing quotas are determined by the number of devices used to run tests.
  The Firebase Spark plan has a fixed testing quota at no cost to users. For
  the Blaze plan, your quotas might increase if your usage of Google Cloud
  increases over time. If you reach your testing quota, wait until the next
  day or upgrade to the Blaze plan if you are currently on the Spark plan.
  If you are already on the Blaze plan, you can request a quota increase.
  For more information, see
  [Testing quota](https://firebase.google.com/docs/test-lab/usage-quotas-pricing#testing-quota).

  You can monitor your testing quota usage in the [Google Cloud console](https://console.cloud.google.com/apis/api/testing.googleapis.com/quotas).
- **Cloud Testing API quota**

  The Cloud Testing API comes with two quota limits: requests per day per
  project, and requests per every 100 seconds per project. You can monitor your
  usage in the
  [Google Cloud console](https://console.cloud.google.com/apis/api/testing.googleapis.com/quotas).
- **Cloud Tool Results API quota**

  The Cloud Tool Results API comes with two quota limits: queries per day per
  project, and queries per every 100 seconds per project. You can monitor your
  usage in the
  [Google Cloud console](https://console.cloud.google.com/apis/api/toolresults.googleapis.com/quotas).

  Refer to [Cloud API quotas for Test Lab](https://firebase.google.com/docs/test-lab/usage-quotas-pricing#cloud-api-quota)
  for more information on API limits. If you've reached an API quota:
  - Submit a request for higher quotas by
    [editing your quotas](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota)
    directly in the Google Cloud console (note that most limits are set to
    maximum by default), or

  - Request higher API quotas by filling out a request form in the
    Google Cloud console or by contacting
    [Firebase support](https://support.google.com/firebase/contact/support).

<br />

<br />

<br />

#### How do I find out if the
traffic reaching my backend is coming from Test Lab?

<br />

From your backend, you can determine if traffic is coming from Firebase-hosted
test devices by checking the source IP address against our
[IP ranges](https://firebase.google.com/docs/test-lab/android/get-started#ip-blocks).

<br />

<br />

<br />

#### Does Test Lab work with
VPC-SC?

<br />

Test Lab does not work with VPC-SC, which blocks the
copying of apps and other test artifacts between Test Lab's internal
storage and users' results buckets.

<br />

<br />

<br />

#### How do I detect flaky tests in
Test Lab?

<br />

To detect flaky behavior in your tests, we recommend using the

[--num-flaky-test-attempts](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--num-flaky-test-attempts)

option. Deflake reruns are billed or counted toward your daily quota the same as
normal test executions.

Keep the following in mind:

- The entire test execution runs again when a failure is detected. There's no support for retrying only failed test cases.
- Deflake retry runs are scheduled to run at the same time, but are not guaranteed to run in parallel, for example, when traffic exceeds the number of available devices.

> [!NOTE]
> **Note:** Infrastructure errors are independent from the deflake feature and don't trigger deflake reruns.

<br />

<br />

<br />

### iOS-specific FAQ

<br />

#### Does Test Lab support
Appium, Flutter/FlutterDriver, ReactNative/Jest, or Cucumber?

<br />

While some of these items are on our roadmap, we're currently unable to provide
commitment to supporting these testing and app development platforms.

<br />

<br />

<br />

#### Where can I find device details,
like resolution, etc.?

<br />

Detailed device information is available through the API and can be accessed
from the gcloud client using the
[describe command](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/models/describe):

`gcloud firebase test ios models describe MODEL`

<br />

<br />

<br />

#### Can I use sharding with iOS tests?

<br />

Sharding isn't natively supported within Test Lab for iOS. However, you can
use the [Flank](https://flank.github.io/flank/) client to shard iOS test cases.

> [!NOTE]
> **Note:** Using Flank iOS sharding creates separate test matrices for each shard.

This works by setting `OnlyTestIdentifiers` key and values in `.xctestrun` file.
See `man` page for `xcodebuild.xctestrun` for more details.

<br />

<br />

<br />

#### Why is my iOS test missing videos in the
results?

<br />

For iOS 18 or later, we are not able to support videos in the results.

<br />

<br />

<br />

### Android-specific FAQ

<br />

#### Does Test Lab support
wearable devices?

<br />

Yes! Test Lab supports Google Pixel Watch. You can now run tests on
your standalone Wear app on Google Pixel Watches. To learn more about
Test Lab devices, see [Test on
available devices](https://firebase.google.com/docs/test-lab/android/available-testing-devices).

<br />

<br />

<br />

#### Does Test Lab support the
latest Google devices?

<br />

Yes! Test Lab supports the Google Pixel Tablet and Google Pixel Fold. You can
run your tests on your standalone physical devices.
To learn more about
Test Lab devices, see [Test on
available devices](https://firebase.google.com/docs/test-lab/android/available-testing-devices).

<br />

<br />

<br />

#### How do I detect a running test
in Test Lab?

<br />

If you're testing your app in Firebase or running tests for a
[pre-launch report](https://support.google.com/googleplay/android-developer/answer/7002270?hl=en)
in the Play Console, you can detect whether a test is being
run on a Firebase-hosted device by checking for the system property
`firebase.test.lab` in your `MainActivity` file. You can then execute additional
statements based on the boolean value for `testLabSetting`. For more
information, see
[Modified test behaviors](https://firebase.google.com/docs/test-lab/android/android-studio#modify_instrumented_test_behavior_for).

<br />

<br />

<br />

#### Does Test Lab
support Appium, Flutter/FlutterDriver, ReactNative/Jest, or Cucumber?

<br />

While some of these items are on our roadmap, we're currently unable to provide
commitment to supporting these testing and app development platforms. However,
if you built your app with a framework that supports Espresso (for example,
Flutter), you can write an instrumentation test using
[Espresso](https://developer.android.com/training/testing/espresso)
and then run the test in Test Lab.

<br />

<br />

<br />

#### Does Test Lab
support testing obfuscated apps, for example, with ProGuard or R8)?

<br />

Test Lab does not explicitly support for obfuscation or deobfuscation. While
the app will likely run, any obfuscated app data, like stack traces,
will appear as obfuscated in the logs.

<br />

<br />

<br />

#### Can I use my foldable device in
different foldable states and postures while testing on Test Lab?

<br />

Yes! You can test your foldable device in [foldable states and postures](https://developer.android.com/guide/topics/large-screens/learn-about-foldables#foldable_postures).

Foldable devices can be in various folded states, such as [`FLAT`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature.State#FLAT()) (fully open) or [`HALF_OPENED`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature.State#HALF_OPENED()) (between fully open and completely closed).

Postures, on the other hand, consist of specific device orientation and foldable
state. For example, tabletop posture, which is a `HALF_OPENED` state in horizontal orientation, or book posture, which is a `HALF_OPENED` state in vertical orientation.

If you are running instrumentation tests, you can use [Jetpack WindowManager](https://developer.android.com/jetpack/androidx/releases/window) library and follow [testing your app on foldables](https://developer.android.com/guide/topics/large-screens/test-apps-on-foldables) documentation to test on different states and postures.

Alternatively, available states are device-specific and can be interacted with using the `adb
shell command cmd device_state`.

- To list the current state, run `adb shell cmd device_state state`.
- To set or override the current state, run `adb shell cmd device_state state <IDENTIFIER>`.
- To reset the state, run `adb shell cmd device_state state reset`.
- To check available states, run the `adb shell cmd device_state print-states` command on the foldable device.

### Google Pixel Fold (model ID `felix`)

```
$ adb shell cmd device_state print-states
Supported states: [
    DeviceState{identifier=0, name='CLOSED', app_accessible=true},
    DeviceState{identifier=1, name='HALF_OPENED', app_accessible=true},
    DeviceState{identifier=2, name='OPENED', app_accessible=true},
    DeviceState{identifier=3, name='REAR_DISPLAY_STATE', app_accessible=true},
]
```

### Samsung Galaxy Z Fold4 (model ID `q4q`)

```
$ adb shell cmd device_state print-states
Supported states: [
    DeviceState{identifier=0, name='CLOSE', app_accessible=true},
    DeviceState{identifier=1, name='TENT', app_accessible=true},
    DeviceState{identifier=2, name='HALF_FOLDED', app_accessible=true},
    DeviceState{identifier=3, name='OPEN', app_accessible=true},
]
```

<br />

<br />

<br />

#### Can I try out Test Lab if I don't have
an app?

<br />

Unlike other Firebase products, you do not need to add a Firebase
SDK in order to use Test Lab. If you don't already have an app, you can
download an APK online or build an app and a test APK from one of the
samples in the [AndroidX GitHub repository](https://github.com/android/testing-samples).
Note that you only need your
app's APK file to run a Robo test, while an instrumentation test requires both
an app and a test APK that are built from source code. For more information,
read about [Instrumented tests](https://developer.android.com/studio/test/index.html).

To learn more about Test Lab features, see
[Get started testing for Android with Firebase Test Lab](https://firebase.google.com/docs/test-lab/android/get-started).

<br />

<br />

<br />

#### What devices are best for
screenshot-diff testing?

<br />

*Screenshot-diff testing* is where test assertions are based on comparing screen
images obtained while running a test to golden images representing expected
behavior. Such tests may be more brittle on some device types than others. We recommend targeting
Arm (`*.arm`) emulator devices for these kinds of tests. Arm emulator devices use
images that are very similar or identical to Android Studio 'generic' emulators.

We also recommend that you investigate test libraries that can help make
screenshot tests more robust in the presence of expected changes.

<br />

<br />

<br />

#### Does Test Lab update virtual devices?

<br />

Yes! Virtual devices are updated when the following changes are made:

1. Updates to existing images
2. Deprecation of earlier API levels
3. New Android API levels are added

<br />

<br />

<br />

#### How do I enable coverage reports?

<br />

To enable coverage reports, add `coverage=true` to
[`environmentVariables` field](https://cloud.google.com/sdk/gcloud/reference/beta/firebase/test/android/run#--environment-variables).
If you're using Android Test Orchestrator, you'll need to provide a directory to
store the coverage results:

    --environment-variables coverage=true,coverageFilePath=/sdcard/Download/

If you're not using Orchestrator, you can specify a file path:

    --environment-variables coverage=true,coverageFile=/sdcard/Download/coverage.ec

<br />

<br />

<br />

#### Where can I find device details, like
resolution, supported ABIs, etc.?

<br />

Detailed device information is available through the API and can be accessed
from the gcloud client using the
[describe command](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/models/describe):

`gcloud firebase test android models describe MODEL`

<br />

<br />

<br />

*** ** * ** ***

## Known issues

<br />

#### Sign-in Captchas

<br />

Robo test cannot bypass sign-in screens that require
additional user action beyond entering credentials to sign in, for example,
completing a CAPTCHA.

<br />

<br />

<br />

### iOS-specific known issues

<br />

#### Automatic sign in

<br />

Automatically signing in with a Google account is not supported
on Robo tests for iOS+ (Beta).

<br />

<br />

<br />

### Android-specific known issues

<br />

#### UI framework support

<br />

Robo test works best with apps that use UI elements from the Android UI
framework (including `View`, `ViewGroup`, and `WebView`
objects). If you use Robo test to exercise apps that use other UI
frameworks, including apps that use the Unity game engine, the test may exit
without exploring beyond the first screen.

<br />

<br />