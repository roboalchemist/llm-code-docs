# Source: https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/crashlytics/ios/customize-crash-reports) [Android](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports) [Flutter](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports) [Unity](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports) |

<br />

In the Crashlytics dashboard, you can click into an issue and get a detailed
event report. You can customize those reports to help you better understand
what's happening in your app and the circumstances around events reported to
Crashlytics.

- Report [uncaught exceptions](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports#report-uncaught-exceptions) and
  [caught exceptions](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports#report-caught-exceptions) to Crashlytics.

- Instrument your app to log [custom keys](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports#add-keys),
  [custom log messages](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports#add-logs), and [user identifiers](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports#set-user-ids).

- Automatically get [breadcrumb logs](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports#get-breadcrumb-logs) if your app uses the
  Firebase SDK for Google Analytics. These logs give you visibility into
  user actions leading up to a Crashlytics-collected event in your app.

- Turn off automatic crash reporting and
  [enable opt-in reporting](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports#enable-reporting) for your users. Note that, by
  default, Crashlytics automatically collects platform-native crash reports
  for all your app's users.

> [!NOTE]
> **Note:** For Flutter apps, fatal reports are sent to Crashlytics in real-time without the need for the user to restart the application. Non-fatal reports are written to disk to be sent along with the next fatal report or when the app restarts.

## Report exceptions

## Report uncaught exceptions

You can automatically catch all "fatal" errors that are thrown within the Flutter
framework by overriding `FlutterError.onError` with
`FirebaseCrashlytics.instance.recordFlutterFatalError`. Alternatively,
to also catch "non-fatal" exceptions, override `FlutterError.onError` with `FirebaseCrashlytics.instance.recordFlutterError`:

    void main() async {
      WidgetsFlutterBinding.ensureInitialized();

      await Firebase.initializeApp();
      bool weWantFatalErrorRecording = true;
      FlutterError.onError = (errorDetails) {
        if(weWantFatalErrorRecording){
          FirebaseCrashlytics.instance.recordFlutterFatalError(errorDetails);
        } else {
          FirebaseCrashlytics.instance.recordFlutterError(errorDetails);
        }
      };

      runApp(MyApp());
    }

### Asynchronous errors

Asynchronous errors are not caught by the Flutter framework:

    ElevatedButton(
      onPressed: () async {
        throw Error();
      }
      ...
    )

To catch such errors, you can use the `PlatformDispatcher.instance.onError` handler:

    Future<void> main() async {
        WidgetsFlutterBinding.ensureInitialized();
        await Firebase.initializeApp();
        FlutterError.onError = (errorDetails) {
          FirebaseCrashlytics.instance.recordFlutterFatalError(errorDetails);
        };
        // Pass all uncaught asynchronous errors that aren't handled by the Flutter framework to Crashlytics
        PlatformDispatcher.instance.onError = (error, stack) {
          FirebaseCrashlytics.instance.recordError(error, stack, fatal: true);
          return true;
        };
        runApp(MyApp());

    }

### Errors outside of Flutter

To catch errors that happen outside of the Flutter context, install an error
listener on the current `Isolate`:

    Isolate.current.addErrorListener(RawReceivePort((pair) async {
      final List<dynamic> errorAndStacktrace = pair;
      await FirebaseCrashlytics.instance.recordError(
        errorAndStacktrace.first,
        errorAndStacktrace.last,
        fatal: true,
      );
    }).sendPort);

## Report caught exceptions

In addition to automatically reporting your app's crashes, Crashlytics lets
you record non-fatal exceptions and sends them to you the next time a fatal
event is reported or when the app restarts.

> [!NOTE]
> **Note:** Crashlytics only stores the most recent eight recorded non-fatal exceptions. If your app throws more than eight, older exceptions are lost. This count is reset each time a fatal exception is thrown, since this causes a report to be sent to Crashlytics.

Use the `recordError` method to record non-fatal exceptions in your app's catch
blocks. For example:

    await FirebaseCrashlytics.instance.recordError(
      error,
      stackTrace,
      reason: 'a non-fatal error'
    );

    // Or you can use:
    await FirebaseCrashlytics.instance.recordFlutterError(errorDetails);

You may also want to log further information about the error which is possible
using the `information` property:

    await FirebaseCrashlytics.instance.recordError(
      error,
      stackTrace,
      reason: 'a non-fatal error',
      information: ['further diagnostic information about the error', 'version 2.0'],
    );

> [!WARNING]
> **Warning:** If you want to include a unique value (for example, a user ID or a timestamp) in your exception message, use a [custom key](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports#add-keys) instead of adding the value directly in the exception message. Adding values directly can result in several issues and may cause Crashlytics to limit reporting errors in your app.

These exceptions appear as non-fatal issues in the Firebase console. The
issue summary contains all the state information you normally get from crashes,
along with breakdowns by version and hardware device.

Crashlytics processes exceptions on a dedicated background thread to
minimize the performance impact to your app. To reduce your users' network
traffic, Crashlytics will rate-limit the number of reports sent off device,
if necessary.

## Add custom keys

Custom keys help you get the specific state of your app leading up to a crash.
You can associate arbitrary key-value pairs with your crash reports, then use
the custom keys to search and filter crash reports in the Firebase console.

- In the [Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics),
  you can search for issues that match a custom key.

- When you're reviewing a specific issue in the console, you can view the
  associated custom keys for each event (*Keys* subtab) and even filter the
  events by custom keys (*Filter* menu at the top of the page).

> [!NOTE]
> **Note:** Crashlytics supports a maximum of 64 key-value pairs. After you reach this threshold, additional values are not saved. Each key-value pair can be up to 1 kB in size.

Use the `setCustomKey` instance method to set key-value pairs. Here are some
examples:

    // Set a key to a string.
    FirebaseCrashlytics.instance.setCustomKey('str_key', 'hello');

    // Set a key to a boolean.
    FirebaseCrashlytics.instance.setCustomKey("bool_key", true);

    // Set a key to an int.
    FirebaseCrashlytics.instance.setCustomKey("int_key", 1);

    // Set a key to a long.
    FirebaseCrashlytics.instance.setCustomKey("int_key", 1L);

    // Set a key to a float.
    FirebaseCrashlytics.instance.setCustomKey("float_key", 1.0f);

    // Set a key to a double.
    FirebaseCrashlytics.instance.setCustomKey("double_key", 1.0);

## Add custom log messages

To give yourself more context for the events leading up to a crash, you can add
custom Crashlytics logs to your app. Crashlytics associates the logs
with your crash data and displays them in the
[Firebase console](https://console.firebase.google.com/project/_/crashlytics),
under the Crashlytics **Logs** tab.

> [!NOTE]
> **Note:** To avoid slowing down your app, Crashlytics limits logs to 64kB and deletes older log entries when a session's logs go over that limit.

Use `log` to help pinpoint issues. For example:

    FirebaseCrashlytics.instance.log("Higgs-Boson detected! Bailing out");

## Set user identifiers

To diagnose an issue, it's often helpful to know which of your users experienced
a given crash. Crashlytics includes a way to anonymously identify users in
your crash reports.

To add user IDs to your reports, assign each user a unique identifier in the
form of an ID number, token, or hashed value:

    FirebaseCrashlytics.instance.setUserIdentifier("12345");

If you ever need to clear a user identifier after you set it, reset the value to
a blank string. Clearing a user identifier does not remove existing
Crashlytics records. If you need to delete records associated with a user
ID, [contact Firebase support](https://firebase.google.com/support/troubleshooter/contact).

## Get breadcrumb logs

Breadcrumb logs give you a better understanding of the interactions that a user
had with your app leading up to a crash, non-fatal, or ANR event. These logs can
be helpful when trying to reproduce and debug an issue.

Breadcrumb logs are powered by Google Analytics, so to get breadcrumb logs, you
need to
[enable Google Analytics](https://support.google.com/firebase/answer/9289399#linkga)
for your Firebase project and
[add the Firebase SDK for Google Analytics](https://firebase.google.com/docs/analytics/get-started#add-sdk)
to your app. Once these requirements are met, breadcrumb logs are automatically
included with an event's data within the **Logs** tab when you view the details
of an issue.

The Analytics SDK
[automatically logs the `screen_view` event](https://support.google.com/analytics/answer/9234069#screen_view)
which enables the breadcrumb logs to show a list of screens viewed before the
crash, non-fatal, or ANR event. A `screen_view` breadcrumb log contains a
`firebase_screen_class` parameter.

Breadcrumb logs are also populated with any
[custom events](https://firebase.google.com/docs/analytics/events) that you manually log within the user's
session, including the event's parameter data. This data can help show a series
of user actions leading up to a crash, non-fatal, or ANR event.

Note that you can
[control the collection and use of Google Analytics data](https://firebase.google.com/docs/analytics/configure-data-collection),
which includes the data that populates breadcrumb logs.

## Enable opt-in reporting

> [!CAUTION]
> If you enable opt-in reporting by disabling automatic reporting, you will reduce the accuracy of your app's event count and crash-free metrics, which makes them less reflective of the overall stability of your app. [Learn more.](https://firebase.google.com/docs/crashlytics/crash-free-metrics#impact-of-data-collection-settings)

By default, Crashlytics automatically collects crash reports for all your
app's users. To give users more control over the data they send, you can enable
opt-in reporting by disabling automatic reporting and only sending data to
Crashlytics when you choose to in your code.

1. Turn off automatic collection natively:

   **Apple platforms**

   Add a new key to your `Info.plist` file:
   - Key: `FirebaseCrashlyticsCollectionEnabled`
   - Value: `false`

   **Android**

   In the `application` block of your `AndroidManifest.xml` file, add
   a `meta-data` tag to turn off automatic collection:

       <meta-data
           android:name="firebase_crashlytics_collection_enabled"
           android:value="false" />

2. Enable collection for select users by calling the Crashlytics data
   collection override at runtime. The override value persists across all
   subsequent launches of your app so Crashlytics can automatically collect
   reports for that user.

       FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true);

   If the user later opts-out of data collection, you can pass `false` as the
   override value, which will apply the next time the user launches the app and
   will persist across all subsequent launches for that user.

> [!NOTE]
> **Note:** When data collection is disabled for a user, Crashlytics will store crash information locally on the device. If data collection is subsequently enabled, any crash information stored on the device will be sent to Crashlytics for processing.

## Manage Crash Insights data

Crash Insights helps you resolve issues by comparing your anonymized stack
traces to traces from other Firebase apps and letting you know if your issue is
part of a larger trend. For many issues, Crash Insights even provides resources
to help you debug the crash.

Crash Insights uses aggregated crash data to identify common stability trends.
If you'd prefer not to share your app's data, you can opt-out of Crash Insights
from the **Crash Insights** menu at the top of your Crashlytics issue list
in the [Firebase console](https://console.firebase.google.com/project/_/crashlytics).

> [!NOTE]
> **Note:** Disabling data sharing also removes insights on your issues. Changes may take up to 24 hours to take effect.

## Next steps

- [Export your data to BigQuery or Cloud Logging](https://firebase.google.com/docs/crashlytics/export-data-to-cloud) for advanced analysis and features, like querying your data, building custom dashboards, and setting up custom alerts.