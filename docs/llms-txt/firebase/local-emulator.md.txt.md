# Source: https://firebase.google.com/docs/functions/local-emulator.md.txt

The Firebase CLI includes a Cloud Functions emulator which can emulate the
following function types:

- HTTPS functions
- Callable functions
- Task queue functions
- Background functions triggered from Firebase Authentication, Realtime Database, Cloud Firestore, Cloud Storage, supported Firebase alerts, and Cloud Pub/Sub.

You can run functions locally to test them before deploying to production.

## Install the Firebase CLI

> [!NOTE]
> **Note:** You can also run Firebase CLI commands in Cloud Shell. [Cloud Shell](https://firebase.google.com/docs/cloud-shell) is a browser-based, pre-authenticated command-line environment, accessible from the Firebase console, and comes with the Firebase CLI pre-installed. This makes it a convenient option for getting started quickly, provided you add your project files to the Cloud Shell environment.

To use the Cloud Functions emulator, first install the Firebase CLI:

```
npm install -g firebase-tools
```

In order to use the local emulator, your Cloud Functions must depend on:

- `firebase-admin` version `8.0.0` or higher.
- `firebase-functions` version `3.0.0` or higher.

## Set up admin credentials (optional)

If you want your functions tests to interact with Google APIs or other Firebase
APIs via the [Firebase Admin SDK](https://firebase.google.com/docs/admin/setup), you may need to set up
admin credentials.

- Cloud Firestore and Realtime Database triggers already have sufficient credentials, and do **not** require additional setup.
- All other APIs, including Firebase APIs such as Authentication and FCM or Google APIs such as Cloud Translation or Cloud Speech, require the setup steps described in this section. This applies whether you're using the Cloud Functions shell or `firebase emulators:start`.

**To set up admin credentials for emulated functions:**

1. Open the [Service Accounts pane](https://console.cloud.google.com/iam-admin/serviceaccounts) of the Google Cloud console.
2. Make sure that **App Engine default service account** is selected, and use the options menu at right to select **Create key**.
3. When prompted, select **JSON** for the key type, and click **Create**.
4. Set your Google default credentials to point to the downloaded key:

   ### Unix

   ```
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/key.json"
   firebase emulators:start
   ```

   ### Windows

   ```
   set GOOGLE_APPLICATION_CREDENTIALS=path\to\key.json
   firebase emulators:start
   ```

After completing these steps, your functions tests can access Firebase and
Google APIs using the [Admin SDK](https://firebase.google.com/docs/admin/setup). For example, when testing
an Authentication trigger, the emulated function could call
`admin.auth().getUserByEmail(email)`.

## Set up functions configuration (optional)

If you're using custom functions configuration variables, first run the
command to get your custom config (run this within the `functions` directory)
in your local environment:

```
firebase functions:config:get > .runtimeconfig.json
# If using Windows PowerShell, replace the above with:
# firebase functions:config:get | ac .runtimeconfig.json
```

## Run the emulator suite

> [!NOTE]
> **Note:** Code changes you make during an active session are automatically reloaded by the emulator. If your code needs to be transpiled (TypeScript, React) make sure to do so before running the emulator. You can run your transpiler in watch mode with commands like `tsc -w` to transpile and reload code automatically as you save.

To run the Cloud Functions emulator, use the `emulators:start` command:

```
firebase emulators:start
```

The `emulators:start` command will start emulators for Cloud Functions,
Cloud Firestore, Realtime Database, and Firebase Hosting based
on the products you have initialized in your local project using `firebase
init`. If you want to start a particular emulator, use the `--only` flag:

```
firebase emulators:start --only functions
```

If you want to run a test suite or testing script after the emulators have
started, use the `emulators:exec` command:

```
firebase emulators:exec "./my-test.sh"
```

## Instrument your app to talk to the emulators

To instrument your app to interact with the emulators, you may need to do
some additional configuration.

### Instrument your app for callable functions

If your prototype and test activities involve [callable backend functions](https://firebase.google.com/docs/functions/callable), configure interaction with the Cloud Functions for Firebase emulator like this:

##### Kotlin

```kotlin
// 10.0.2.2 is the special IP address to connect to the 'localhost' of
// the host computer from an Android emulator.
val functions = Firebase.functions
functions.useEmulator("10.0.2.2", 5001)
```

##### Java

```java
// 10.0.2.2 is the special IP address to connect to the 'localhost' of
// the host computer from an Android emulator.
FirebaseFunctions functions = FirebaseFunctions.getInstance();
functions.useEmulator("10.0.2.2", 5001);
```

##### Swift

```swift
Functions.functions().useEmulator(withHost: "localhost", port: 5001)
```

### Web

```javascript
import { getApp } from "firebase/app";
import { getFunctions, connectFunctionsEmulator } from "firebase/functions";

const functions = getFunctions(getApp());
connectFunctionsEmulator(functions, "127.0.0.1", 5001);
```

### Web

> [!NOTE]
> [Learn
> more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.

```javascript
firebase.functions().useEmulator("127.0.0.1", 5001);
```

> [!NOTE]
> **Note:** **Android only** . Android network security configuration policies may affect how your code interacts with the Cloud Functions emulator, which serves data locally via unencrypted HTTP. Starting with Android 9 (API level 28), clear text communication is disabled by default. You can set up a `network_security_config.xml` file to whitelist the Cloud Functions emulator for development on localhost. See the relevant [Android developer documentation](https://developer.android.com/training/articles/security-config#CleartextTrafficPermitted).

### Instrument your app for HTTPS functions emulation

Each HTTPS function in your code will be served from the local emulator using the following URL format:

`http://$HOST:$PORT/$PROJECT/$REGION/$NAME`

For example a simple `helloWorld` function with the default host port and region would be served at:

`https://localhost:5001/$PROJECT/us-central1/helloWorld`

### Instrument your app for task queue functions emulation

The emulator automatically sets up emulated task queues based on trigger
definitions, and the Admin SDK reroutes enqueued requests to the emulator if
it detects that it is running via the `CLOUD_TASKS_EMULATOR_HOST` environment
variable.

Note that the dispatch system used in production is more complex than the
one implemented in the emulator, so you should not expect emulated
behavior to precisely mirror production environments. The parameters within the
emulator provide upper bounds to the rate at which tasks get dispatched
and retried.

### Instrument your app for background-triggered functions emulation

The Cloud Functions emulator supports background-triggered functions from the following sources:

- Realtime Database emulator
- Cloud Firestore emulator
- Authentication emulator
- Pub/Sub emulator
- Firebase alerts emulator

To trigger background events, modify back-end resources using the
Emulator Suite UI, or by connecting your app or test code to the emulators
using the SDK for your platform.

### Test handlers for custom events emitted by Extensions

For functions you implement to handle Firebase Extensions custom events
with Cloud Functions v2, the Cloud Functions emulator pairs with the
Eventarc emulator to support
[Eventarc triggers](https://firebase.google.com/docs/extensions/install-extensions#eventarc).

To test custom event handlers for extensions that emit events, you must install
the Cloud Functions and Eventarc emulators.

The Cloud Functions runtime sets the `EVENTARC_EMULATOR` environment
variable to `localhost:9299` in the current process if the Eventarc emulator
is running. The Firebase Admin SDKs automatically connect to the Eventarc
emulator when the `EVENTARC_EMULATOR` environment variable is set. You can
modify the default port as discussed under [Configure Local Emulator Suite](https://firebase.google.com/docs/emulator-suite/install_and_configure#configure_emulator_suite).

When environment variables are properly configured, the Firebase Admin SDK
automatically sends events to the Eventarc emulator. In turn, the Eventarc
emulator makes a call back to the Cloud Functions emulator to trigger any
registered handlers.

You can check Functions logs in the Emulator Suite UI for details on
handler execution.

## Interactions with other services

The emulator suite includes multiple emulators, which enable
testing of cross-product interactions.

### Cloud Firestore

If you have functions that use the Firebase Admin SDK to write to
Cloud Firestore, these writes will be sent to the Cloud Firestore emulator
if it is running. If further functions are triggered by those writes,
they will be run in the Cloud Functions emulator.

### Cloud Storage

If you have functions that use the Firebase Admin SDK (version 9.7.0 or greater)
to write to Cloud Storage, these writes will be sent to the Cloud Storage emulator
if it is running. If further functions are triggered by those writes,
they will be run in the Cloud Functions emulator.

### Firebase Authentication

If you have functions that use the Firebase Admin SDK (version 9.3.0 or greater)
to write to Firebase Authentication, these writes will be sent to the Auth emulator
if it is running. If further functions are triggered by those writes,
they will be run in the Cloud Functions emulator.

### Firebase Hosting

If you're using Cloud Functions to [generate dynamic content for
Firebase Hosting](https://firebase.google.com/docs/hosting/functions), `firebase emulators:start`
uses your local HTTP functions as proxies for hosting.

### Firebase alerts

In any project that includes at least one supported Firebase alert trigger, the
emulator UI includes a **FireAlerts** tab. To emulate an alert trigger:

1. Open the **FireAlerts** tab. This tab displays a dropdown populated with the alert types that have triggers associated with them (for example, if you have an onNewFatalIssuePublished trigger, then crashlytics.newFatalIssue is displayed).
2. Select an alert type. The form auto populates with default values, which can be edited. You can edit the fields of the event (other information from the alert event is either inferred, mock values, or randomly generated).
3. Select **Send Alert** to send a synthetic alert to the functions emulator, with logging available in **Alerts** in the Firebase console (as well as in logs).

## Logging

The emulator streams logs from your functions to the terminal window where they
run. It displays all output from `console.log()`, `console.info()`,
`console.error()`, and `console.warn()` statements inside your functions.

## Next Steps

For a full example of using the Firebase emulator suite, see the
[testing quickstart sample](https://github.com/firebase/quickstart-testing/).