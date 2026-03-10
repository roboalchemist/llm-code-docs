# Source: https://firebase.google.com/docs/test-lab/android/get-started.md.txt

# Get started testing for Android with Firebase Test Lab

[Video](https://www.youtube.com/watch?v=XV2uTiZ9SH0)

Firebase Test Lab lets you test your app on a range of devices and
configurations. This Get Started guide provides an implementation path for you
to follow, as well as an introduction to Test Lab's Android offerings.

For information about Test Lab quotas and pricing plans, see
[Usage, Quotas, and Pricing](https://firebase.google.com/docs/test-lab/usage-quotas-pricing).

## Key concepts

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

*** ** * ** ***

## **Step 1** : Prepare your test for uploading to Test Lab

### Available test types

You can run the following tests with Test Lab. Note that all test types are
limited to running 45 minutes on physical devices and 60 minutes on virtual
devices. Any uncaught exception will cause a test failure.

- **Instrumentation test** or **instrumented unit test** :
  A test you've written using the
  [Espresso](https://developer.android.com/training/testing/espresso)
  or [UI Automator](https://developer.android.com/training/testing/other-components/ui-automator)
  frameworks. With this test, you can make explicit assertions about the
  state of your app to verify correct functionality using
  [AndroidJUnitRunnerAPIs](https://developer.android.com/reference/android/support/test/runner/AndroidJUnitRunner).

  - Visit
    [Run an instrumentation test](https://firebase.google.com/docs/test-lab/android/instrumentation-test)
    for instructions on how to prepare your test to run in Test Lab.

  - Refer to the
    [Android Developers documentation](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests.html)
    for instructions on how to build an instrumentation test.

- **Robo test** : An automated test that analyzes your
  app's UI and then explores it methodically by simulating user activities,
  without requiring you to write any code. Visit
  [About Robo tests](https://firebase.google.com/docs/test-lab/android/robo-ux-test) for more information.

- **Game Loop test**: A test that uses a "demo mode" to
  simulate player actions in gaming apps. This is a fast and scalable way
  to verify that your game performs well for users. When you choose to run a
  Game Loop test, you can:

  - Write tests native to your game engine

  - Avoid writing the same code for different UIs or testing
    frameworks

  - Optionally create multiple loops to run in a single test execution
    (visit [About Game Loop tests](https://firebase.google.com/docs/test-lab/android/game-loop#about-game-tests) to learn more).
    You can also organize loops by using labels so you can keep
    track of them and re-run specific loops.

  See [Run a Game Loop test](https://firebase.google.com/docs/test-lab/android/game-loop) for instructions on running this test
  with Test Lab.

### Tools to run your test

You can choose the following tools to run your test with:

- *Recommended for first-time users* : The Firebase console lets you upload an
  app and initiate testing from your web browser. See
  [Test with the Firebase console](https://firebase.google.com/docs/test-lab/android/firebase-console) for instructions on
  running tests using this tool.

- [Android Studio integration](https://firebase.google.com/docs/test-lab/android/android-studio) lets you test
  your app without leaving your development environment. See [Test with Android Studio](https://firebase.google.com/docs/test-lab/android/android-studio)
  for instructions on running tests using this tool.

- The [gcloud command line interface](https://firebase.google.com/docs/test-lab/android/command-line) enables you to run tests
  from the command line interactively, and is also well suited for scripting as
  part of your automated build and testing process. See [Test with the gcloud CLI](https://firebase.google.com/docs/test-lab/android/command-line)
  for instructions on running tests using this tool.

You can also test your app at no cost with Test Lab when you upload and
publish your app's APK files to the Play Store using either the alpha or
beta channel. For more information, see
[Use pre-launch reports to identify issues](https://support.google.com/googleplay/android-developer/answer/7002270)
and [Robo tests](https://firebase.google.com/docs/test-lab/android/robo-ux-test).

## **Step 2**: Choose your testing device

Test Lab supports testing on several makes and models of
Android devices installed and running in a Google data center. Testing on
devices in Test Lab help you detect issues that might not occur when testing
your app using emulators in Android Studio. To learn more, see
[Available devices.](https://firebase.google.com/docs/test-lab/android/available-testing-devices)

## **Step 3**: Review test results

Regardless of how you initiate your tests, all your test results are managed by
Test Lab and can be viewed online.

The **test result summary** is
automatically stored and can be viewed in the Firebase console. It contains
the most relevant data for your test, including test case-specific videos,
screenshots, the number of tests that passed, failed, or got flaky results, and
more.

The **raw test results** contain test logs and app failure details, and is
automatically stored in a Google Cloud bucket. If you specify a bucket, you are
responsible for the cost of the storage. If you don't specify a bucket,
Test Lab creates one for you at no cost.

For more details, see
[Analyze Firebase Test Lab Results.](https://firebase.google.com/docs/test-lab/analyzing-results)

When you initiate a test from [Android Studio](https://firebase.google.com/docs/test-lab/android/android-studio),
you can also review test results from inside your development environment.

## Device cleanup

Google takes the security of your app data very seriously. We follow
industry-standard best practices to remove app data and reset system settings
for physical devices after every test run to ensure that they are
ready to run new tests. For devices that we can flash with a custom recovery
image, we go one step further by flashing these devices between test runs.

For the virtual devices used by Test Lab, device instances are deleted after
they are used so that each test run uses a new virtual device instance.

*** ** * ** ***

## Test Lab and Google Play services

Test Lab devices usually run on the latest version of the Google Play
services SDK, but some may require a few days to update after a new version
of the SDK is released. Note that you may encounter compatibility issues with
some devices.

## Allowing test devices to access private backend servers

Some mobile apps need to communicate with private backend services to function
correctly during testing. If your backend servers are protected by firewall
rules, you can allow access for Test Lab's physical and virtual devices by
using the [IP address blocks below](https://firebase.google.com/docs/test-lab/android/get-started#ip-blocks) to open routes through your
firewall.

## Mobile advertising

Test Lab provides a scalable infrastructure that automates app testing, and
unfortunately, this capability can be misused by malicious apps designed to
generate fraudulent ad revenue.

To mitigate this issue:

- If you use or work with third-party digital advertising providers
  (for example, ad networks or demand-side platforms),
  you're recommended to use test ads rather than real ads during app development
  and testing.

- If you must use real ads in your test, notify the digital advertising
  providers you work with to filter out revenues and all corresponding traffic
  generated from Test Lab by using the
  [IP address blocks below](https://firebase.google.com/docs/test-lab/android/get-started#ip-blocks). You don't need
  to notify Google-owned ad providers; Test Lab takes care of that for you.

## IP addresses used by Test Lab devices

> [!NOTE]
> **Note:** Test Lab Android Virtual Devices (AVD), identified by an `.arm` or (Arm) suffix, share IP address blocks with physical devices. To learn more about these devices, see [Start testing with Android Virtual Devices](https://firebase.google.com/docs/test-lab/android/avds).

All network traffic generated by Test Lab devices originates from the
following
[IP address blocks](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation).
You can also access this list by using the
`gcloud beta firebase test ip-blocks list`
[command](https://cloud.google.com/sdk/gcloud/reference/beta/firebase/test/ip-blocks/list)
in the [gcloud](https://cloud.google.com/sdk/gcloud) CLI. The list is updated on
average once a year.

| Platform and device type | CIDR IP address block |
|---|---|
| Android and iOS physical devices, Arm virtual devices | 70.32.128.0/19 (added 02-2022) 108.177.6.0/23 108.177.18.192/26 (added 02-2022) 108.177.29.64/27 (expanded 02-2022) 108.177.31.160/27 (added 02-2022) 199.36.156.8/29 (added 02-2022) 199.36.156.16/28 (added 02-2022) 209.85.131.0/27 (added 02-2022) 2001:4860:1008::/48 (added 02-2022) 2001:4860:1018::/48 (added 02-2022) 2001:4860:1019::/48 (added 02-2022) 2001:4860:1020::/48 (added 02-2022) 2001:4860:1022::/48 (added 02-2022) 2001:4860:101d::/48 (added 10-2025) 2001:4860:101e::/48 (added 10-2025) 2001:4860:1031::/48 (added 10-2025) 70.32.128.48/28 (added 04-2024) 70.32.150.192/27 (added 09-2025) 108.177.6.0/27 (added 09-2025) 108.177.24.160/27 (added 09-2025) 108.177.29.0/27 (added 09-2025) |
| Android virtual devices (Non-Arm) | 34.68.194.64/29 (added 11-2019) 34.69.234.64/29 (added 11-2019) 34.73.34.72/29 (added 11-2019) 34.73.178.72/29 (added 11-2019) 34.74.10.72/29 (added 02-2022) 34.136.2.136/29 (added 02-2022) 34.136.50.136/29 (added 02-2022) 34.145.234.144/29 (added 02-2022) 35.192.160.56/29 35.196.166.80/29 35.196.169.240/29 35.203.128.0/28 35.234.176.160/28 35.243.2.0/27 (added 7-2019) 35.245.243.240/29 (added 02-2022) 199.192.115.0/30 199.192.115.8/30 199.192.115.16/29 |
| Device IP-blocks no longer being used | 74.125.122.32/29 (removed 02-2022) 216.239.44.24/29 (removed 02-2022) |