# Source: https://firebase.google.com/docs/crashlytics/flutter/test-implementation.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/crashlytics/ios/test-implementation) [Android](https://firebase.google.com/docs/crashlytics/android/test-implementation) [Flutter](https://firebase.google.com/docs/crashlytics/flutter/test-implementation) [Unity](https://firebase.google.com/docs/crashlytics/unity/test-implementation) |

<br />

Use this guide if you've followed the
[getting started guide](https://firebase.google.com/docs/crashlytics/flutter/get-started),
and you're still not seeing crashes in the Crashlytics dashboard.

## Force a crash to test your implementation

1. Add code to your app that you can use to force a test exception to be
   thrown.

   If you've added an error handler that calls
   `FirebaseCrashlytics.instance.recordError(error, stack, fatal: true)` to the
   top-level `Zone`, you can use the following code to add a button to your app
   that, when pressed, throws a test exception:

       TextButton(
           onPressed: () => throw Exception(),
           child: const Text("Throw Test Exception"),
       ),

2. Build and run your app.

3. Force the test exception to be thrown in order to send your app's first
   report:

   1. Open your app from your test device or emulator.

   2. In your app, press the test exception button that you added using the
      code above.

4. Go to the
   [Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics)
   of the Firebase console to see your test crash.

   If you've refreshed the console and you're still not seeing the test crash
   after five minutes, try enabling debug logging (next section).

## Enable debug logging for Crashlytics

If you don't see your test crash in the Crashlytics dashboard, you can
use debug logging for Crashlytics to help track down the problem.

<br />

<br />

#### Apple platforms

1. Enable debug logging:

   1. In Xcode, select **Product \> Scheme \> Edit scheme**.

   2. Select **Run** from the left menu, then select the **Arguments** tab.

   3. In the *Arguments Passed on Launch* section, add `-FIRDebugEnabled`.

2. Force a test crash. The first section on this page describes how to do this.

3. Within your logs, search for a log message from Crashlytics that
   contains the following string, which verifies that your app is sending
   crashes to Firebase.

   ```
   Completed report submission
   ```

   > [!NOTE]
   > After confirming that your app is sending crashes, you can optionally disable debug logging by removing the `-FIRDebugEnabled` from the arguments passed on launch.

If you don't see this log or your test crash in the Crashlytics dashboard
of the Firebase console after five minutes, reach out to
[Firebase Support](https://firebase.google.com/support/troubleshooter/crashlytics/missing) with a copy of
your log output so that we can help you troubleshoot further.


<br />

<br />

<br />

#### Android

1. Enable and view debug logging for Crashlytics:

   1. Before running your app, set the following `adb` shell flag to `DEBUG`:

      ```
      adb shell setprop log.tag.FirebaseCrashlytics DEBUG
      ```
   2. View the logs in your device logs by running the following command:

      ```
      adb logcat -s FirebaseCrashlytics
      ```
2. Force a test crash. The first section on this page describes how to do this.

3. Look for the following message or code `204` in your logcat output, either
   of which verifies that your app is sending crashes to Firebase.

   ```
   Crashlytics report upload complete
   ```

   > [!NOTE]
   > After confirming that your app is sending crashes, you can optionally disable debug logging by setting the `adb` shell flag back to `INFO`:
   >
   > ```
   > adb shell setprop log.tag.FirebaseCrashlytics INFO
   > ```

If you don't see this log or your test crash in the Crashlytics dashboard
of the Firebase console after five minutes, reach out to
[Firebase Support](https://firebase.google.com/support/troubleshooter/crashlytics/missing) with a copy of
your log output so that we can help you troubleshoot further.


<br />

## Next steps

- [Customize your crash report setup](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports) by adding opt-in reporting, logs, keys, and tracking of non-fatal errors.