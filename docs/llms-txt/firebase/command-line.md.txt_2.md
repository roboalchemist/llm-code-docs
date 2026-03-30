# Source: https://firebase.google.com/docs/test-lab/ios/command-line.md.txt

# Test with the Google Cloud CLI

This guide describes how to run an XCTest or a Game Loop test using the gcloud
CLI.

## **Step 1**: Configure your local Google Cloud SDK environment

1. Download the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install-sdk#installing_the_latest_version)
2. This includes the gcloud CLI tool.
3. Make sure your installation is up-to-date and includes the `gcloud firebase` command:

   ```
         gcloud components update
   ```
4. Log in to the gcloud CLI using your Google account:

   ```
         gcloud auth login
   ```
5. Set your Firebase project in gcloud, where <var translate="no">PROJECT_ID</var> is the ID of your Firebase project:

   ```
        gcloud config set project PROJECT_ID
   ```

## **Step 2**: Run your test

### **Run an XCTest**

1. Upload the .zip file of your test by running the following command (if you
   haven't yet packaged up your app, see
   [Packaging your XCTest](https://firebase.google.com/docs/test-lab/ios/run-xctest#package-app)):

   ```
   cd FOLDER_WITH_TEST_OUTPUT/Build/Products ; \
   zip -r MyTests.zip Debug-iphoneos YOUR_SCHEME_iphoneosDEPLOYMENT_TARGET-arm64.xctestrun
   ```
2. Choose your test dimensions.

   Test Lab lets you run tests on a variety of iOS versions, devices, screen
   orientations, and locales. These configurations are known as the test's
   *test dimensions* . To see the options for each dimension
   (e.g., supported Xcode versions for the device's iOS version), substitute
   `models`, `versions`, or `locales` for
   `dimension` in the following command:

   ```
   gcloud firebase test ios dimension list
   ```

   Screen orientation is somewhat simpler, as its only options are `portrait` and
   `landscape`.

   Look through the list of test dimensions, and select a few combinations that you'd like to
   run your test on. Visit [Pricing Plans](https://firebase.google.com/pricing) to see the
   maximum number of combinations you can run per day.

   > [!NOTE]
   > **Note:** Each dimension's `list` table includes a `TAGS` column, with one row tagged as `default`. That row is the dimension that Test Lab uses if you don't otherwise specify a value for that dimension.

3. Once you've chosen a set of test dimensions, you can have Test Lab run
   your tests using the `firebase test ios run` command. For each
   combination of test dimensions you'd like to test on, include a separate `--device` flag:

   <br />

   ```
   gcloud firebase test ios run --test PATH/TO/MyTests.zip \
    --device model=MODEL_ID_1,version=VERSION_ID_1,locale=LOCALE_1,orientation=ORIENTATION_1 \
    --device model=MODEL_ID_2,version=VERSION_ID_2,locale=LOCALE_2,orientation=ORIENTATION_2 \
    etc...
   ```

   It is possible that your test will fail due to an incompatibility between the Xcode version with
   which the test was built and the default Xcode version used by Test Lab.
   To specify a supported Xcode version for your test, use the `--xcode-version` flag:

   <br />

   ```
   gcloud firebase test ios run --test PATH/TO/MyTests.zip \
    --device model=MODEL_ID_1,version=VERSION_ID_1,locale=LOCALE_1,orientation=ORIENTATION_1 \
    --xcode-version=15
   ```

   To help you identify and locate your test matrices in the
   Firebase console, you can optionally label your test matrix using the
   `--client-details matrixLabel="<label>"` flag in the following example:

   ```
   gcloud beta firebase test ios run --test PATH/TO/MyTests.zip \
     --device model=MODEL_ID_1,version=VERSION_ID_1,locale=LOCALE_1,orientation=ORIENTATION_1 \
     --client-details matrixLabel="my label"
   ```

   > [!NOTE]
   > **Note:** The `--client-details` flag is only supported in the Alpha and Beta tracks of the gcloud CLI.

#### Test Special Entitlements

To test entitlements that require an explicit App ID, you can do so by
setting the `--test-special-entitlements` flag. Test Lab
re-signs the application with a new bundle-identifier to support special
entitlements, so make sure there are no resources in your zip file
containing direct references to the app's bundle identifier.
Supported entitlements:

1. Push Notifications `apns-environment`
2. Personal VPN `com.apple.developer.networking.vpn.api`

> [!NOTE]
> **Note:** This flag supports re-signing only one app per project, requiring special entitlements. More such entitlements can be enabled in the future based on user interest.

**Push Notifications**

For authorizing push notification requests, users can create JSON web
tokens by using the private
[signing key](https://firebase.google.com/docs/test-lab/resources/AuthKey_C7FD9DJAA8.p8)
along with the Key ID - **C7FD9DJAA8** and the Team ID -
**9CKCGNNUQN** . The generated tokens would be valid for one
hour and need to be refreshed every 60mins. Read more on
[Establishing a Token-Based Connection to APNs.](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/establishing_a_token-based_connection_to_apns)
**App groups**

App group IDs are universally unique. This means that when we
re-sign user apps, we can only use the app group ID that is
associated with the Test Lab developer account. If your test relies
on app groups, your test will fail.

### **Run a Game Loop test**

Run the `gcloud beta firebase test ios run` command and use the following
flags to configure the run:

| Flags for Game Loop tests ||
|---|---|
| `--type` | **Required** : Specifies the type of iOS test you want to run. You can enter test types `xctest` (default) or `game-loop`. |
| `--app` | **Required**: Absolute path (GCS or filesystem) to your app's IPA file. This flag is only valid when running Game Loop tests. |
| `--scenario-numbers` | The loops (aka scenarios) you want to run in your app. You can enter one loop, a list or loops, or a range of loops. The default loop is 1. For example, `--scenario-numbers=1-3,5` runs loops 1, 2, 3, and 5. |
| `--device-model` | The physical device you want to run your test on (find out which [available devices](https://firebase.google.com/docs/test-lab/ios/available-testing-devices) you can use). |
| `--timeout` | The maximum duration you want your test to run. You can enter an integer to represent the duration in seconds, or an integer and enumeration to represent the duration as a longer unit of time. For example: - `--timeout=200` forces your test to terminate when it runs up to 200 seconds. - `--timeout=1h` forces your test to terminate when it runs up to an hour. |

For example, the following command runs a Game Loop test that executes loops
1, 4, 6, 7, and 8 on an iPhone 8 Plus:

```
gcloud beta firebase test ios run
 --type game-loop --app path/to/my/App.ipa --scenario-numbers 1,4,6-8
 --device-model=iphone8plus
```

For more information on the gcloud CLI, see the
[reference documentation](https://cloud.google.com/sdk/gcloud/reference/beta/).

## **Step 3 (Optional)**: Automate future tests you build

### Scripting gcloud commands with Test Lab

You can use shell scripts or batch files to automate mobile app testing commands
that you would otherwise run using the gcloud command line. This sample bash
script runs an XCTest with a two-minute timeout, and reports if the test run
completed successfully:

```
if gcloud firebase test ios run --test MyTest.zip --timeout 2m
then
    echo "Test matrix successfully finished"
else
    echo "Test matrix exited abnormally with non-zero exit code: " $?
fi
```

### Script exit codes

Test Lab provides several exit codes that you can use to better understand
the results of tests that you run using scripts or batch files.

| Exit code | Notes |
|---|---|
| 0 | All test executions passed. |
| 1 | A general failure occurred. Possible causes include: a filename that does not exist or an HTTP/network error. |
| 2 | Testing exited because unknown commands or arguments were provided. |
| 10 | One or more test cases (tested classes or class methods) within a test execution did not pass. |
| 15 | Firebase Test Lab could not determine if the test matrix passed or failed, because of an unexpected error. |
| 19 | The test matrix was canceled by the user. |
| 20 | A test infrastructure error occurred. |

## **Step 4**: Investigate test results

When the test starts, you receive a link to the **Test Results** page. Tests can
take a number of minutes to run, depending on the number of different
configurations you have selected and the test timeout duration set for your
tests. After your tests have run, you can review test results. See
[Analyzing Firebase Test Lab Results](https://firebase.google.com/docs/test-lab/ios/analyzing-results) to learn more about
how to interpret your test results.

## Next step

Read the Google Cloud SDK documentation to explore testing options that are
[generally available](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/)
or in [beta](https://cloud.google.com/sdk/gcloud/reference/beta/firebase/test/ios).