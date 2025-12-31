# Source: https://firebase.google.com/docs/functions/local-emulator.md.txt

<br />

The Firebase CLI includes aCloud Functionsemulator which can emulate the following function types:

- HTTPS functions
- Callable functions
- Task queue functions
- Background functions triggered fromFirebase Authentication,Realtime Database,Cloud Firestore,Cloud Storage, supported Firebase alerts, and Cloud Pub/Sub.

You can run functions locally to test them before deploying to production.

## Install the Firebase CLI

To use theCloud Functionsemulator, first install the Firebase CLI:  

```
npm install -g firebase-tools
```

In order to use the local emulator, yourCloud Functionsmust depend on:

- `firebase-admin`version`8.0.0`or higher.
- `firebase-functions`version`3.0.0`or higher.

## Set up admin credentials (optional)

If you want your functions tests to interact with Google APIs or other Firebase APIs via the[Firebase Admin SDK](https://firebase.google.com/docs/admin/setup), you may need to set up admin credentials.

- Cloud FirestoreandRealtime Databasetriggers already have sufficient credentials, and do**not**require additional setup.
- All other APIs, including Firebase APIs such asAuthenticationandFCMor Google APIs such as Cloud Translation or Cloud Speech, require the setup steps described in this section. This applies whether you're using theCloud Functionsshell or`firebase emulators:start`.

**To set up admin credentials for emulated functions:**

1. Open the[Service Accounts pane](https://console.cloud.google.com/iam-admin/serviceaccounts)of theGoogle Cloudconsole.
2. Make sure that**App Enginedefault service account** is selected, and use the options menu at right to select**Create key**.
3. When prompted, select**JSON** for the key type, and click**Create**.
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

After completing these steps, your functions tests can access Firebase and Google APIs using the[Admin SDK](https://firebase.google.com/docs/admin/setup). For example, when testing anAuthenticationtrigger, the emulated function could call`admin.auth().getUserByEmail(email)`.

## Set up functions configuration (optional)

If you're using custom functions configuration variables, first run the command to get your custom config (run this within the`functions`directory) in your local environment:  

```
firebase functions:config:get > .runtimeconfig.json
# If using Windows PowerShell, replace the above with:
# firebase functions:config:get | ac .runtimeconfig.json
```

## Run the emulator suite

| **Note:** Code changes you make during an active session are automatically reloaded by the emulator. If your code needs to be transpiled (TypeScript, React) make sure to do so before running the emulator. You can run your transpiler in watch mode with commands like`tsc -w`to transpile and reload code automatically as you save.

To run theCloud Functionsemulator, use the`emulators:start`command:  

```
firebase emulators:start
```

The`emulators:start`command will start emulators forCloud Functions, Cloud Firestore, Realtime Database, and Firebase Hosting based on the products you have initialized in your local project using`firebase
init`. If you want to start a particular emulator, use the`--only`flag:  

```
firebase emulators:start --only functions
```

If you want to run a test suite or testing script after the emulators have started, use the`emulators:exec`command:  

```
firebase emulators:exec "./my-test.sh"
```

## Instrument your app to talk to the emulators

To instrument your app to interact with the emulators, you may need to do some additional configuration.

### Instrument your app for callable functions

If your prototype and test activities involve[callable backend functions](https://firebase.google.com/docs/functions/callable), configure interaction with theCloud Functions for Firebaseemulator like this:  

##### Kotlin

```kotlin
// 10.0.2.2 is the special IP address to connect to the 'localhost' of
// the host computer from an Android emulator.
val functions = Firebase.functions
functions.useEmulator("10.0.2.2", 5001)https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/functions/app/src/main/java/devrel/firebase/google/com/functions/kotlin/MainActivity.kt#L28-L31
```

##### Java

```java
// 10.0.2.2 is the special IP address to connect to the 'localhost' of
// the host computer from an Android emulator.
FirebaseFunctions functions = FirebaseFunctions.getInstance();
functions.useEmulator("10.0.2.2", 5001);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/functions/app/src/main/java/devrel/firebase/google/com/functions/MainActivity.java#L58-L61
```

##### Swift

```swift
Functions.functions().useEmulator(withHost: "localhost", port: 5001)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/functions/FunctionsExampleSwift/ViewController.swift#L29-L29
```

### Web

```javascript
import { getApp } from "firebase/app";
import { getFunctions, connectFunctionsEmulator } from "firebase/functions";

const functions = getFunctions(getApp());
connectFunctionsEmulator(functions, "127.0.0.1", 5001);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/functions-next/emulator-suite/fb_functions_emulator_connect.js#L8-L12
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
firebase.functions().useEmulator("127.0.0.1", 5001);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/functions/emulator-suite.js#L6-L6
```
| **Note:** **Android only** . Android network security configuration policies may affect how your code interacts with theCloud Functionsemulator, which serves data locally via unencrypted HTTP. Starting with Android 9 (API level 28), clear text communication is disabled by default. You can set up a`network_security_config.xml`file to whitelist theCloud Functionsemulator for development on localhost. See the relevant[Android developer documentation](https://developer.android.com/training/articles/security-config#CleartextTrafficPermitted).

### Instrument your app for HTTPS functions emulation

Each HTTPS function in your code will be served from the local emulator using the following URL format:

`http://`<var translate="no">$HOST</var>`:`<var translate="no">$PORT</var>`/`<var translate="no">$PROJECT</var>`/`<var translate="no">$REGION</var>`/`<var translate="no">$NAME</var>

For example a simple`helloWorld`function with the default host port and region would be served at:

`https://localhost:5001/`<var translate="no">$PROJECT</var>`/us-central1/helloWorld`

### Instrument your app for task queue functions emulation

The emulator automatically sets up emulated task queues based on trigger definitions, and the Admin SDK reroutes enqueued requests to the emulator if it detects that it is running via the`CLOUD_TASKS_EMULATOR_HOST`environment variable.

Note that the dispatch system used in production is more complex than the one implemented in the emulator, so you should not expect emulated behavior to precisely mirror production environments. The parameters within the emulator provide upper bounds to the rate at which tasks get dispatched and retried.

### Instrument your app for background-triggered functions emulation

TheCloud Functionsemulator supports background-triggered functions from the following sources:

- Realtime Databaseemulator
- Cloud Firestoreemulator
- Authenticationemulator
- Pub/Subemulator
- Firebase alerts emulator

To trigger background events, modify back-end resources using theEmulator Suite UI, or by connecting your app or test code to the emulators using the SDK for your platform.

### Test handlers for custom events emitted by Extensions

For functions you implement to handleFirebase Extensionscustom events withCloud Functionsv2, theCloud Functionsemulator pairs with the Eventarc emulator to support[Eventarc triggers](https://firebase.google.com/docs/extensions/install-extensions#eventarc).

To test custom event handlers for extensions that emit events, you must install theCloud Functionsand Eventarc emulators.

TheCloud Functionsruntime sets the`EVENTARC_EMULATOR`environment variable to`localhost:9299`in the current process if the Eventarc emulator is running. TheFirebaseAdmin SDKs automatically connect to the Eventarc emulator when the`EVENTARC_EMULATOR`environment variable is set. You can modify the default port as discussed under[ConfigureLocal Emulator Suite](https://firebase.google.com/docs/emulator-suite/install_and_configure#configure_emulator_suite).

When environment variables are properly configured, theFirebaseAdmin SDKautomatically sends events to the Eventarc emulator. In turn, the Eventarc emulator makes a call back to theCloud Functionsemulator to trigger any registered handlers.

You can check Functions logs in theEmulator Suite UIfor details on handler execution.

## Interactions with other services

The emulator suite includes multiple emulators, which enable testing of cross-product interactions.

### Cloud Firestore

If you have functions that use the Firebase Admin SDK to write toCloud Firestore, these writes will be sent to theCloud Firestoreemulator if it is running. If further functions are triggered by those writes, they will be run in theCloud Functionsemulator.

### Cloud Storage

If you have functions that use the Firebase Admin SDK (version 9.7.0 or greater) to write toCloud Storage, these writes will be sent to theCloud Storageemulator if it is running. If further functions are triggered by those writes, they will be run in theCloud Functionsemulator.

### Firebase Authentication

If you have functions that use the Firebase Admin SDK (version 9.3.0 or greater) to write toFirebase Authentication, these writes will be sent to the Auth emulator if it is running. If further functions are triggered by those writes, they will be run in theCloud Functionsemulator.

### Firebase Hosting

If you're usingCloud Functionsto[generate dynamic content forFirebase Hosting](https://firebase.google.com/docs/hosting/functions),`firebase emulators:start`uses your local HTTP functions as proxies for hosting.

### Firebase alerts

In any project that includes at least one supported Firebase alert trigger, the emulator UI includes a**FireAlerts**tab. To emulate an alert trigger:

1. Open the**FireAlerts**tab. This tab displays a dropdown populated with the alert types that have triggers associated with them (for example, if you have an onNewFatalIssuePublished trigger, then crashlytics.newFatalIssue is displayed).
2. Select an alert type. The form auto populates with default values, which can be edited. You can edit the fields of the event (other information from the alert event is either inferred, mock values, or randomly generated).
3. Select**Send Alert** to send a synthetic alert to the functions emulator, with logging available in**Alerts** in theFirebaseconsole (as well as in logs).

## Logging

The emulator streams logs from your functions to the terminal window where they run. It displays all output from`console.log()`,`console.info()`,`console.error()`, and`console.warn()`statements inside your functions.

## Next Steps

For a full example of using the Firebase emulator suite, see the[testing quickstart sample](https://github.com/firebase/quickstart-testing/).