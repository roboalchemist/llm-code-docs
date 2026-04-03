# Source: https://firebase.google.com/docs/test-lab/ios/robo-ux-test.md.txt

# Source: https://firebase.google.com/docs/test-lab/android/robo-ux-test.md.txt

# Source: https://firebase.google.com/docs/test-lab/ios/robo-ux-test.md.txt

# Source: https://firebase.google.com/docs/test-lab/android/robo-ux-test.md.txt

<br />

Robo test is a testing tool that is integrated withFirebase Test Lab. Robo test analyzes the structure of your app's user interface (UI) and then explores it methodically, automatically simulating user activities. Robo test always simulates the same user activities in the same order when you use it to test an app on a specific device configuration with the same settings. This repeatable testing approach lets you use Robo test to validate bug fixes and test for regressions.
| **Note:** Robo test is not the same as (or based on) the Robotium or Robolectric test frameworks.

Robo test captures log files, saves a series of annotated screenshots, and then creates a video from those screenshots to show you the simulated user operations that it performed. These logs, screenshots, and videos can help you determine the root cause of app crashes. These Robo test features can also help you find issues with your app's UI.

In addition to running regular Robo tests, you can customize your tests using Robo scripts, which are a feature of Robo tests. To learn more, see[Run a Robo script](https://firebase.google.com/docs/test-lab/android/run-robo-scripts).

If you want to try the Beta version of Robo for iOS+, see[Run a Robo Test](https://firebase.google.com/docs/test-lab/ios/robo-ux-test).

## Robo test crawl stats

To help you interpret your Robo test results, Robo test records stats during each test crawl.Test Labdisplays the stats at the top of the Robo test tab in your test results page:

- Actions: The total number of actions performed during the crawl, including Robo script actions, monkey actions, and Robo directives.

- Activities: The number of distinct activities covered during the crawl.

- Screens: The number of distinct screens visited during the crawl.

Test Labalso uses the stats to create a visual representation of the Robo test in the form of a crawl graph. The graph has screens as its nodes and actions as edges. By following the edges between screens, you can get an idea of how Robo test traversed your app throughout the crawl.

## Robo test timeout

Depending on the complexity of your app's UI, Robo test might take five minutes or more to complete a thorough set of UI interactions. We recommend setting the test timeout to at least 120 seconds (2 minutes) for most apps, and 300 seconds (5 minutes) for moderately complex apps. The default value for timeout is 300 seconds (5 minutes) for tests run from Android Studio and theFirebaseconsole, and 900 seconds (15 minutes) for tests run from the`gcloud`command line.

#### App start-up timeout errors

If your app takes a long time to start, Robo test can throw an error, and won't be able to crawl your app. This only happens in cases of extremely long start-up time, and can only be resolved by revising your app to make it start faster.

## More control with Robo scripts

Sometimes you need more control over your tests. For example, you might want to test a common user journey or provide specific UI input like a username and password. Robo scripts can help. To learn more about Robo scripts, see[Run a Robo script](https://firebase.google.com/docs/test-lab/android/run-robo-scripts)and[Robo scripts reference guide](https://firebase.google.com/docs/test-lab/android/robo-scripts-reference).

## Robo tests and non-Android UI widgets

Robo tests use the Android API to perform actions on Android UI widgets directly. That helps the tests explore your UI automatically, but also means that they need to be able to extract an Android UI hierarchy for a screen in order to run tests on it.

If a screen in your app doesn't use Android UI widgets, Robo tests fall back on Monkey Actions to test that screen. Unlike the more methodical Robo test actions, Monkey Actions simply simulate tap events on semi-random locations on a device's screen.

To better test screens that don't use Android UI widgets, you can replace the arbitrary taps of a Monkey Action with a set of scripted taps and interactions through[Firebase Test LabGame Loop Tests](https://firebase.google.com/docs/test-lab/android/game-loop).

## Integration with Google Play

You can use Robo test in the Google Play Console when you upload and publish your app's APK file using either the alpha or beta channel. Robo test runs on a set of popular physical devices from different geographic locations, providing test coverage across various form factors and hardware configurations. To learn more, see[Use pre-launch reports to identify issues](https://support.google.com/googleplay/android-developer/answer/7002270).

## Test account sign-in and predefined text input

Robo test supports test account sign-in, and also allows you to enter predefined text into fields in your app. For custom sign-in and other predefined text input, Robo test can enter text into[`EditText`](https://developer.android.com/reference/android/widget/EditText.html)fields in your app. For each string, you need to identify the`EditText`field using an Android resource name. To learn more, see[Accessing Resources](https://developer.android.com/guide/topics/resources/accessing-resources.html).

### Sign-in

Robo test has two mutually-exclusive methods to support sign-in:

- Custom sign-in: If you provide test account credentials, you need to tell Robo test where to enter them, and also provide those credentials.

- Automatic sign-in: If you don't provide test account credentials for custom sign-in, automatic sign-in is used. Robo test can automatically sign in to apps built with standard Android widgets or Compose applications, using a Google test account.

| **Note:** One automatic sign-in account is created per combination of project and app package. If your app prevents multiple concurrent sign-ins from a single account, you will need to run tests sequentially, or use custom sign-in.

To provide test account credentials for custom sign-in, do the following:

1. On the**Select dimensions** page, choose**Additional options**.

2. Under**Test account credentials (Optional)**, enter the username and password resource names and the username and password for the test account.

| **Caution:** Only use credentials for test accounts that are not associated with real users.

### Predefined text input

You can provide custom input text for other text fields used by your app. To provide text input for additional fields, do the following:

1. On the**Select dimensions** page, choose**Additional options**.

2. Under**Additional fields (Optional)**, enter one or more resource names, and the strings to enter in the corresponding text fields.

#### Predefined text input {:#predefined-text} errors

Robo test searches for`EditText`fields with an Android resource name that matches a supplied regular expression. If Robo can't find a matching field, it doesn't input your text, but otherwise continues its crawl as usual.

### Deep links

You can provide up to three[deep links](https://developer.android.com/training/app-links/deep-linking.html)supported by your app for testing. Deep links are issued to your app as Android[`ACTION_VIEW`](https://developer.android.com/reference/android/content/Intent.html#ACTION_VIEW)intents. Therefore, each link must match an intent filter in your app.

If one or more deep links are provided, the app is first launched normally (using the[`ACTION_MAIN`](https://developer.android.com/reference/android/content/Intent.html#ACTION_MAIN)intent) and crawled up to the specified timeout. After the main crawl, each deep link is crawled for an additional 30 seconds each.
| **Note:** Do not enter[Firebase Dynamic Links](https://firebase.google.com/docs/dynamic-links)into these fields. Instead, enter the underlying URLs that the dynamic links are configured to target on Android.

#### Deep link errors

If Robo test can't find an activity matching your deep link,Test Labignores the link. Deep link issues are usually the result of a discrepancy between the provided deep link and its definition in your app. Check both the provided URL and your app for typos or other inconsistencies.

## App licensing support

Test Labsupports apps that use the[App Licensing](https://developer.android.com/google/play/licensing/index.html)service offered by Google Play. To successfully check licensing when testing your app withTest Lab, you must publish your app to the production channel in the Play store. To test your app in the alpha or beta channel usingTest Lab, remove the licensing check before uploading your app toTest Lab.

## Next steps

- Customize your tests[using Robo scripts](https://firebase.google.com/docs/test-lab/android/run-robo-scripts).