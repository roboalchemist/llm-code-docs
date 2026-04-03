# Source: https://firebase.google.com/docs/test-lab/android/avds.md.txt

<br />

This document describes AVDs forTest Lab, including benefits and known limitations. We also provide recommendations about how to test your app throughout the development lifecycle.Test LabAVDs are similar to[AVDs for Android Studio](https://developer.android.com/studio/run/managing-avds#about)but are optimized for performance with cloud testing, so there are a few differences between the two.

Test LabAVDs with an .arm or (Arm) suffix are advanced emulators which provide the following benefits:

- Faster test execution time

- Screen sizes and densities aligned with Android Studio's AVDs for consistency

- GPU supported accelerated graphics

The following table describes the benefits of using virtual devices:

|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Benefit**           | **Description**                                                                                                                                                                                                    | **Use case(s)**                                                                                                                                                                                                    |
| High availability     | You can run tests and get test results more quickly when testing with virtual devices. Because virtual devices are created on demand, your tests start almost immediately, providing quick validation of your app. | Testing small updates to your app, or for regression testing.                                                                                                                                                      |
| Longer test durations | Virtual devices support a test duration of up to 60 minutes. Tests on physical devices are limited to a test duration of 45 minutes on each device.                                                                | Running longer tests                                                                                                                                                                                               |
| Lower costs           | Virtual devices are priced at $1 per hour for each virtual device used to test your app.                                                                                                                           | Daily testing using continuous integration systems, or before checking in code. To learn more, see[Usage levels, quotas, and pricing forTest Lab](https://firebase.google.com/docs/test-lab/usage-quotas-pricing). |

| **Note:** Test Lab's Arm virtual devices have a shard limit of 200 shards. To learn more, see[Start testing with the gcloud CLI](https://firebase.google.com/docs/test-lab/android/command-line#available_commands_and_flags).

## Test your app with virtual devices

You can test your app with virtual devices the same way that you test it with physical devices. You can select virtual devices for your tests when you configure a test matrix. To learn more about running tests withTest Lab, see[Get started testing for Android withFirebase Test Lab](https://firebase.google.com/docs/test-lab/android/get-started).

### View supported models and APIs

To view AVD models and APIs supported byTest Lab, run the following command:  

    gcloud firebase test android models list --filter=virtual

| **Note:** To run this command, you need to[set up the Google Cloud CLI](https://firebase.google.com/docs/test-lab/android/command-line).

## Best practices for testing your app

Virtual devices increase your range of options when you test your app withTest Lab. We recommend using the following best practices to test your app throughout the app development lifecycle:

#### Use the Android Studio emulator or an attached physical device

When developing your app, use the Android Studio emulator or an attached physical device to examine each build for initial validation. If you have instrumentation tests, you can also run these tests from Android Studio on either physical or virtual devices provided byTest Lab.

#### Use CI systems on each code change when working on shared projects

If you work on a large project, or if you contribute to projects that are shared using GitHub or a similar site, we recommend that you use continuous integration (CI) systems. Test your apps on virtual devices each time that the CI system runs, or before each pull request. To learn more about usingTest Labwith CI systems, see[UsingTest Labfor Android with Continuous Integration Systems](https://firebase.google.com/docs/test-lab/android/continuous).

#### Test your app on physical devices withTest Labbefore you release significant app updates

Before you release app updates with significant changes in UI and functionality, we recommend that you useTest Labto test your app on physical devices. This will help to ensure that your app is stable and performant on a wide range of popular physical devices. Testing on physical devices also ensures test coverage for any app functionality that relies on physical device features that are not simulated by virtual devices. To learn more about these features, see[Known limitations](https://firebase.google.com/docs/test-lab/android/avds#known-limitations).

## Virtual device updates

Periodically, the Android team adds new virtual device images, deprecates old ones, and updates existing ones. We apply these updates to our virtual device images to help ensure that you're testing against up-to-date Android versions that reflect your users' experiences.

In rare cases, these updates may cause tests to fail unexpectedly. When there is a known potentially breaking update,Test Labwill include information in[release notes](https://firebase.google.com/support/releases). As a best practice, we recommend you use test frameworks -- for example,[Espresso](https://developer.android.com/training/testing/espresso)-- that are robust to these changes whenever possible. When that is not possible, we recommend you target Arm virtual devices, which you can expect to update less frequently.

## Known limitations

Some physical device features are not currently simulated by virtual devices, or are simulated with some limitations. The following table summarizes features that are currently unavailable on virtual devices, or that are available with certain limitations:

|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Feature**                          | **Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Application Binary Interfaces (ABI)  | Not all devices support all ABIs. If you are developing with the Android NDK, be sure to generate code for the ABIs supported by the devices you target (see[Available devices](https://firebase.google.com/docs/test-lab/android/available-testing-devices)inTest Lab). To learn more about ABI management, see[Android ABIs](https://developer.android.com/ndk/guides/abis.html). **Note:**If a test in your test matrix is marked Invalid, this might occur because your app has a dependency on native code unsupported by the device ABI. |
| Graphics performance                 | Nexus and Pixel virtual devices use software graphics rendering. Graphics intensive applications can experience lower performance. If your app is graphics intensive consider using SmallPhone.arm, MediumPhone.arm, or physical devices instead.                                                                                                                                                                                                                                                                                              |
| Graphics APIs                        | OpenGL ES 3.x is unsupported on devices below API level 29. Newer devices are not 100% compatible with OpenGL/Vulkan APIs, you may notice small differences in graphics.                                                                                                                                                                                                                                                                                                                                                                       |
| Google Play Store App                | The Google Play Store App is unsupported on Arm virtual devices.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Augmented Reality (AR) functionality | Testing the Augmented Reality (AR) functionality is not supported on virtual devices.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Older API levels                     | Test LabArm virtual devices don't support API levels less than 26.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Next steps

- [AnalyzeFirebase Test LabResults](https://firebase.google.com/docs/test-lab/android/analyzing-results).