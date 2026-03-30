# Source: https://firebase.google.com/docs/test-lab/android/android-studio.md.txt

# Run tests with Android Studio

Firebase Test Lab provides cloud-based infrastructure for testing Android
apps, and features full integration with Android Studio for running
instrumented tests and reviewing test results.

This guide describes how to modify instrumented tests in Android Studio so you
can integrate and run them with Test Lab. For instructions on using
Test Lab from the Android Studio UI to create a test matrix, run an
instrumented test, and view the test results, see
[Run your tests with Firebase Test Lab](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests.html#run-ctl).

## Capture screenshots

Test Lab provides support for capturing screenshots when running
instrumented tests. To learn how to capture screenshots, see
[Add the screenshot library to your project](https://firebase.google.com/docs/test-lab/android/instrumentation-test#add-screenshot-library).

## Create tests using Espresso Test Recorder

The Espresso Test Recorder tool lets you create UI tests for your app without
writing any test code. You can record your interactions with a device and add
assertions to verify UI elements in particular snapshots of your app. Espresso
Test Recorder then takes the saved recording and automatically generates a
corresponding Espresso UI test that you can run to test your app in Test Lab.

To learn more, see
[Create UI Tests with Espresso Test Recorder](https://developer.android.com/studio/test/espresso-test-recorder.html).

## Modify instrumented test behavior for Test Lab

Test Lab provides a system variable that you can add to your instrumented
tests so that you can cause them to behave differently when you run them in
Test Lab than when you run them on your own test device or emulator.

The following code example reads a system property, `firebase.test.lab`, and
sets a string, `testLabSetting` to `true` if the test is running in Test Lab.
Then, it uses the value of this string to control whether additional statements
are executed:

### Kotlin

```kotlin
val testLabSetting = Settings.System.getString(contentResolver, "firebase.test.lab")
if ("true" == testLabSetting) {
    // Do something when running in Test Lab
    // ...
}
```

### Java

```java
String testLabSetting = Settings.System.getString(getContentResolver(), "firebase.test.lab");
if ("true".equals(testLabSetting)) {
    // Do something when running in Test Lab
    // ...
}
```

## Use Gradle Managed Devices via the Firebase Test Lab plugin

Gradle Managed Devices via the Firebase Test Lab
plugin lets you run automated instrumented tests at scale on Test Lab
devices, based on the configurations in your project's Gradle files.

Gradle Managed Devices also offer smart sharding, which lets you distribute
tests optimally across shards based on your previous test history. With smart
sharding, shards run for approximately the same length of time and return test
results as quickly as possible. Smart sharding lets you run large test suites in
parallel, making this feature well suited for CI/CD flows.

To enable smart sharding using the [Gradle Managed Devices Test Lab plugin](https://developer.android.com/studio/test/gradle-managed-devices#gmd-ftl),
follow the instructions in [Optimize test runs with smart
sharding](https://developer.android.com/studio/test/gradle-managed-devices#smart-sharding)
.