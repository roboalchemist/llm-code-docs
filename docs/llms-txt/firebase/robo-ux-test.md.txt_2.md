# Source: https://firebase.google.com/docs/test-lab/ios/robo-ux-test.md.txt

# Run a Robo test (iOS+)

> [!NOTE]
> **Note:** Robo for iOS+ is a beta release. This means that the capabilities might change in backward-incompatible ways. A beta release is not subject to any SLA or deprecation policy and may receive limited or no support.

Robo test is a testing tool that is integrated with Firebase Test Lab.
Robo test analyzes the structure of your app's user interface (UI) and then
explores it methodically, automatically simulating user activities. Robo test
always simulates the same user activities in the same order when you use it to
test an app on a specific device configuration with the same settings. This
repeatable testing approach lets you use Robo test to validate bug fixes and
test for regressions.

> [!NOTE]
> **Note:** Robo test is not the same as (or based on) the Robotium or Robolectric test frameworks.

Robo test captures log files, saves a series of annotated screenshots, and
then creates a video from those screenshots to show you the simulated user
operations that it performed. These logs, screenshots, and videos can help
you determine the root cause of app crashes. These Robo test features can also
help you find issues with your app's UI.

In addition to running regular Robo tests, you can customize your tests
using Robo scripts, which are a feature of Robo tests. To learn more,
see [Run a Robo script](https://firebase.google.com/docs/test-lab/ios/run-robo-scripts).

## Robo test crawl stats

To help you interpret your Robo test results, Robo test records stats during
each test crawl. Test Lab displays the stats at the top of the Robo test tab
in your test results page:

- Actions: The total number of actions performed during the crawl, including
  Robo script actions, monkey actions, and Robo directives.

- Screens: The number of distinct screens visited during the crawl.

Test Lab also uses the stats to create a visual representation of the
Robo test in the form of a crawl graph. The graph has screens as its nodes
and actions as edges. By following the edges between screens, you can get an
idea of how Robo test traversed your app throughout the crawl.

## Robo test timeout

Depending on the complexity of your app's UI, Robo test might take five minutes
or more to complete a thorough set of UI interactions. We recommend setting the
test timeout to at least 120 seconds (2 minutes) for most apps, and 300 seconds
(5 minutes) for moderately complex apps. The default value for timeout is 300
seconds (5 minutes) for tests run from the Firebase console and 900 seconds (15
minutes) for tests run from the gcloud command line.

### App startup timeout errors

If your app takes a long time to start, Robo test can throw an error, and won't
be able to crawl your app. This only happens in cases of extremely long startup
times, and can only be resolved by revising your app to make it start faster.

## More control with Robo scripts

Sometimes you need more control over your tests. For example, you might want to
test a common user journey or provide specific UI input like a username and
password. Robo scripts can help. To learn more about Robo scripts, see [Run a
Robo script](https://firebase.google.com/docs/test-lab/ios/run-robo-scripts)
and [Robo scripts reference
guide](https://firebase.google.com/docs/test-lab/android/robo-scripts-reference).

## Next steps

- Customize your tests [using Robo scripts](https://firebase.google.com/docs/test-lab/ios/run-robo-scripts).