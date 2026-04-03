# Source: https://firebase.google.com/docs/test-lab/android/android-studio.md.txt

<br />

Firebase Test Labprovides cloud-based infrastructure for testing Android apps, and features full integration with Android Studio for running instrumented tests and reviewing test results.

This guide describes how to modify instrumented tests in Android Studio so you can integrate and run them withTest Lab. For instructions on usingTest Labfrom the Android Studio UI to create a test matrix, run an instrumented test, and view the test results, see[Run your tests withFirebase Test Lab](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests.html#run-ctl).

## Capture screenshots

Test Labprovides support for capturing screenshots when running instrumented tests. To learn how to capture screenshots, see[Add the screenshot library to your project](https://firebase.google.com/docs/test-lab/android/instrumentation-test#add-screenshot-library).

## Create tests using Espresso Test Recorder

The Espresso Test Recorder tool lets you create UI tests for your app without writing any test code. You can record your interactions with a device and add assertions to verify UI elements in particular snapshots of your app. Espresso Test Recorder then takes the saved recording and automatically generates a corresponding Espresso UI test that you can run to test your app inTest Lab.

To learn more, see[Create UI Tests with Espresso Test Recorder](https://developer.android.com/studio/test/espresso-test-recorder.html).

## Modify instrumented test behavior forTest Lab

Test Labprovides a system variable that you can add to your instrumented tests so that you can cause them to behave differently when you run them inTest Labthan when you run them on your own test device or emulator.

The following code example reads a system property,`firebase.test.lab`, and sets a string,`testLabSetting`to`true`if the test is running inTest Lab. Then, it uses the value of this string to control whether additional statements are executed:  

### Kotlin

```kotlin
val testLabSetting = Settings.System.getString(contentResolver, "firebase.test.lab")
if ("true" == testLabSetting) {
    // Do something when running in Test Lab
    // ...
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/test-lab/app/src/main/java/com/google/firebase/example/testlab/kotlin/MainActivity.kt#L17-L21
```

### Java

```java
String testLabSetting = Settings.System.getString(getContentResolver(), "firebase.test.lab");
if ("true".equals(testLabSetting)) {
    // Do something when running in Test Lab
    // ...
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/test-lab/app/src/main/java/com/google/firebase/example/testlab/MainActivity.java#L26-L30
```

## Use Gradle Managed Devices via theFirebase Test Labplugin

Gradle Managed Devices via theFirebase Test Labplugin lets you run automated instrumented tests at scale onTest Labdevices, based on the configurations in your project's Gradle files.

Gradle Managed Devices also offer smart sharding, which lets you distribute tests optimally across shards based on your previous test history. With smart sharding, shards run for approximately the same length of time and return test results as quickly as possible. Smart sharding lets you run large test suites in parallel, making this feature well suited for CI/CD flows.

To enable smart sharding using the[Gradle Managed DevicesTest Labplugin](https://developer.android.com/studio/test/gradle-managed-devices#gmd-ftl), follow the instructions in[Optimize test runs with smart sharding](https://developer.android.com/studio/test/gradle-managed-devices#smart-sharding).