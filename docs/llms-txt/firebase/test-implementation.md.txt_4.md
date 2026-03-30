# Source: https://firebase.google.com/docs/crashlytics/unity/test-implementation.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/crashlytics/ios/test-implementation) [Android](https://firebase.google.com/docs/crashlytics/android/test-implementation) [Flutter](https://firebase.google.com/docs/crashlytics/flutter/test-implementation) [Unity](https://firebase.google.com/docs/crashlytics/unity/test-implementation) |

<br />

Use this guide if you've followed the
[getting started guide](https://firebase.google.com/docs/crashlytics/unity/get-started),
and you're still not seeing crashes in the Crashlytics dashboard.

## Force a crash to test your implementation

1. Find an existing `GameObject`, then add to it the following script. This
   script will cause a test crash a few seconds after you run your app.

   ```c#
   using System;
   using UnityEngine;

   public class CrashlyticsTester : MonoBehaviour {

       int updatesBeforeException;

       // Use this for initialization
       void Start () {
         updatesBeforeException = 0;
       }

       // Update is called once per frame
       void Update()
       {
           // Call the exception-throwing method here so that it's run
           // every frame update
           throwExceptionEvery60Updates();
       }

       // A method that tests your Crashlytics implementation by throwing an
       // exception every 60 frame updates. You should see reports in the
       // Firebase console a few minutes after running your app with this method.
       void throwExceptionEvery60Updates()
       {
           if (updatesBeforeException > 0)
           {
               updatesBeforeException--;
           }
           else
           {
               // Set the counter to 60 updates
               updatesBeforeException = 60;

               // Throw an exception to test your Crashlytics implementation
               throw new System.Exception("test exception please ignore");
           }
       }
   }
   ```
2. Build your app and upload symbol information after your build finishes.

   - **iOS+**: The Firebase Unity Editor plugin automatically configures your
     Xcode project to upload your symbol file.

   - **Android** : For your Android apps that use IL2CPP, run the
     Firebase CLI `crashlytics:symbols:upload` command to upload your
     symbol file.

3. Run your app. Once your app is running, watch the device log and wait for
   the exception to trigger from the `CrashlyticsTester`.

   - **iOS+**: View logs in the bottom pane of Xcode.

   - **Android** : View logs by running the following command in the terminal:
     `adb logcat`.

4. Go to the [Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics) of the
   Firebase console to see your test crash.

   If you've refreshed the console and you're still not seeing the test crash
   after five minutes, try enabling debug logging (next section).

## Enable debug logging for Crashlytics

If you don't see your test crash in the Crashlytics dashboard, you can
use debug logging for Crashlytics to help track down the problem.

1. Enable debug logging for Firebase by adding the following code to your
   app initialization:

   ```c#
   Firebase.FirebaseApp.LogLevel = Firebase.LogLevel.Debug;
   ```
2. Force a test crash. The first section on this page describes how to do this.

If you don't see logs from Firebase or your test crash in the Crashlytics
dashboard of the Firebase console after five minutes, reach out to
[Firebase Support](https://firebase.google.com/support/troubleshooter/crashlytics/missing) with a copy of
your log output so that we can help you troubleshoot further.

## Next steps

- [Customize your crash report setup](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports) by adding opt-in reporting, logs, keys, and tracking of non-fatal errors.