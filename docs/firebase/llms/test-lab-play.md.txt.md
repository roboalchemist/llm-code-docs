# Source: https://firebase.google.com/docs/test-lab/android/test-lab-play.md.txt

# Beyond Pre-Launch Reports

When you upload and publish your Android application package (APK) to your alpha
or beta channel in the Google Play Console, your APK is tested across
a wide range of devices running different versions of Android. The resulting
pre-launch report helps to identify crashes, display issues, and security
vulnerabilities.

The pre-launch report is powered by
[Robo test](https://firebase.google.com/docs/test-lab/robo-ux-test), an
automated test included with Firebase Test Lab. You can use Robo test to
target specific devices, locales, or versions of Android for testing, and you
can also use Robo test to test your app for longer durations.

Robo test is more customizable than the pre-launch report, but it is just as
easy to use.

> [!NOTE]
> **Note:** All links in this guide open in a **new browser tab** so that you can keep these instructions visible while testing your APK.

## Running your first Robo test in Test Lab

1. Create a Firebase project if you don't have one already: in the [Firebase console](https://console.firebase.google.com/), click **Add New Project**, then enter a name for your project. If you already have a Cloud project, you can select it from the drop-down menu to add Firebase to it.
2. Go to the [**Test Lab** page in Firebase console](https://console.firebase.google.com/project/_/testlab).
3. Drag the APK for the app you'd like to test into "Android" section or click **Browse for APK**, and select the file.

Test Lab uploads the selected APK and automatically begins running a Robo
test on it.

> [!NOTE]
> **Note:** your first Robo test is optimized for getting started quickly, so there are no extra options to choose from. All subsequent tests are fully customizable.

## Next steps

To increase the number of tests you can run on a daily basis, upgrade to the
**Blaze** pricing plan. To learn more about daily usage quotas, and about how
usage-based billing is calculated on the **Blaze** plan,
see [Test Lab quota and billing](https://firebase.google.com/docs/test-lab/usage-quotas-pricing).

> [!NOTE]
> **Note:** pre-launch reports do not impact your Test Lab quota and usage.

If you want to test your app even more thoroughly and frequently, you can use
Test Lab with
[continuous integration](https://firebase.google.com/docs/test-lab/continuous)
systems. You can also use Test Lab to run instrumented tests that you write
specifically to test your app, and you can run these tests from the Firebase
console, the
[gcloud command line](https://firebase.google.com/docs/test-lab/android/command-line),
and directly from
[Android Studio](https://firebase.google.com/docs/test-lab/android-studio).

To learn more about Test Lab, see the
[Test Lab introduction](https://firebase.google.com/docs/test-lab).