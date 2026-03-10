# Source: https://firebase.google.com/docs/crashlytics/android/test-implementation.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/crashlytics/ios/test-implementation) [Android](https://firebase.google.com/docs/crashlytics/android/test-implementation) [Flutter](https://firebase.google.com/docs/crashlytics/flutter/test-implementation) [Unity](https://firebase.google.com/docs/crashlytics/unity/test-implementation) |

<br />

Use this guide if you've followed the
[getting started guide](https://firebase.google.com/docs/crashlytics/android/get-started),
and you're still not seeing crashes in the Crashlytics dashboard.

## Force a crash to test your implementation

1. Add code to your app that you can use to force a test crash.

   You can use the following code in your app's `MainActivity` to add a button
   to your app that, when pressed, causes a crash. The button is labeled
   "Test Crash".

   ### Kotlin

   ```kotlin
   val crashButton = Button(this)
   crashButton.text = "Test Crash"
   crashButton.setOnClickListener {
      throw RuntimeException("Test Crash") // Force a crash
   }

   addContentView(crashButton, ViewGroup.LayoutParams(
          ViewGroup.LayoutParams.MATCH_PARENT,
          ViewGroup.LayoutParams.WRAP_CONTENT))
   ```

   ### Java

   ```java
   Button crashButton = new Button(this);
   crashButton.setText("Test Crash");
   crashButton.setOnClickListener(new View.OnClickListener() {
      public void onClick(View view) {
          throw new RuntimeException("Test Crash"); // Force a crash
      }
   });

   addContentView(crashButton, new ViewGroup.LayoutParams(
          ViewGroup.LayoutParams.MATCH_PARENT,
          ViewGroup.LayoutParams.WRAP_CONTENT));
   ```
2. Build and run your app.

3. Force the test crash in order to send your app's first crash report:

   1. Open your app from your test device or emulator.

   2. In your app, press the "Test Crash" button that you added using the code
      above.

   3. After your app crashes, restart it so that your app can send the crash
      report to Firebase.

4. Go to the [Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics) of the
   Firebase console to see your test crash.

   If you've refreshed the console and you're still not seeing the test crash
   after five minutes, try enabling debug logging (next section).

## Enable debug logging for Crashlytics

If you don't see your test crash in the Crashlytics dashboard, you can
use debug logging for Crashlytics to help track down the problem.

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

## Next steps

- [Customize your crash report setup](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports) by adding opt-in reporting, logs, keys, and tracking of non-fatal errors.