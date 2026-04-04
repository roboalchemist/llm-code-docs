# Source: https://firebase.google.com/docs/emulator-suite/connect_functions.md.txt

<br />

| **Beta.**This emulator is currently in beta. It might be changed in backward-incompatible ways. As always, feedback is greatly appreciated. Let us know what you think!

Before connecting your app to theCloud Functionsemulator, make sure that you[understand the overallFirebase Local Emulator Suiteworkflow](https://firebase.google.com/docs/emulator-suite/connect_and_prototype), and that you[install and configure](https://firebase.google.com/docs/emulator-suite/install_and_configure)theLocal Emulator Suiteand review its[CLI commands](https://firebase.google.com/docs/emulator-suite/install_and_configure#startup).

## Choose a Firebase project

TheFirebase Local Emulator Suiteemulates products for a single Firebase project.

To select the project to use, before you start the emulators, in the CLI run`firebase use`in your working directory. Or, you can pass the`--project`flag to each emulator command.
| **Note:** It's generally a good practice to use one project ID for all emulator invocations, so theEmulator Suite UI, different product emulators, and all running instances of a particular emulator can communicate correctly in all cases. In fact, by default, theLocal Emulator Suitewill warn on detecting multiple project IDs in use, though you can override this behavior. For guidance on setting and managing project IDs, see the[Installation and configuration guide](https://firebase.google.com/docs/emulator-suite/install_and_configure#project_id_configuration).

Local Emulator Suitesupports emulation of*real* Firebase projects and*demo*projects.

| Project type |                                                                                                                      Features                                                                                                                       |                                                                                                                       Use with emulators                                                                                                                       |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Real         | A real Firebase project is one you created and configured (most likely via theFirebaseconsole). Real projects have live resources, like database instances, storage buckets, functions, or any other resource you set up for that Firebase project. | When working with real Firebase projects, you can run emulators for any or all of the supported products. For any products you are not emulating, your apps and code will interact with the*live*resource (database instance, storage bucket, function, etc.). |
| Demo         | A demo Firebase project has no*real*Firebase configuration and no live resources. These projects are usually accessed via codelabs or other tutorials. Project IDs for demo projects have the`demo-`prefix.                                         | When working with demo Firebase projects, your apps and code interact with emulators*only*. If your app attempts to interact with a resource for which an emulator isn't running, that code will fail.                                                         |

We recommend you use demo projects wherever possible. Benefits include:

- Easier setup, since you can run the emulators without ever creating a Firebase project
- Stronger safety, since if your code accidentally invokes non-emulated (production) resources, there is no chance of data change, usage and billing
- Better offline support, since there is no need to access the internet to download your SDK configuration.

| **Note:** If you want to emulate cross-service interactions such as database-triggeredCloud FunctionsorRulesthat rely onAuthenticationyou must make sure that the project ID in your code (in`initializeApp()`, etc.) matches the project ID used by theFirebaseCLI.

## Instrument your app to talk to the emulators

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

## Configure a local testing environment

If your functions rely on dotenv-based[environment configuration](https://firebase.google.com/docs/functions/config-env#env-variables), you can emulate that behavior in your local testing environment.

When using a localCloud Functionsemulator, you can override environment variables for your project by setting up a`.env.local`file. Contents of`.env.local`take precedence over`.env`and the project-specific`.env`file.

For example, a project could include these three files containing slightly different values for development and local testing:

|------------------------------|---------------------|-----------------------|
| `.env`                       | `.env.dev`          | `.env.local`          |
| PLANET=Earth AUDIENCE=Humans | AUDIENCE=Dev Humans | AUDIENCE=Local Humans |

When started in the local context, the emulator loads the environment variables as shown:  

      $ firebase emulators:start
      i  emulators: Starting emulators: functions
      # Starts emulator with following environment variables:
      #  PLANET=Earth
      #  AUDIENCE=Local Humans

### Secrets and credentials in theCloud Functionsemulator

TheCloud Functionsemulator supports the use of secrets to[store and access sensitive configuration information](https://firebase.google.com/docs/functions/config-env#create-secret). By default, the emulator will try to access your production secrets using[application default credentials](https://cloud.google.com/docs/authentication/production). In certain situations like CI environments, the emulator may fail to access secret values due to permission restrictions.

Similar toCloud Functionsemulator support for environment variables, you can override secrets values by setting up a`.secret.local`file. This makes it easy for you to test your functions locally, especially if you don't have access to the secret value.

## What other tools for testingCloud Functionsexist?

TheCloud Functionsemulator is supplemented by other prototype and test tools:

- The Cloud Functions shell, which allows for interactive, iterative functions prototyping and development. The shell employs the Cloud Functions emulator with a REPL-style interface for development. No integration with theCloud FirestoreorRealtime Databaseemulators is provided. Using the shell, you mock data and perform function calls to simulate interaction with products that theLocal Emulator Suitedoes not currently support: Analytics, Remote Config, and Crashlytics.
- The Firebase Test SDK for Cloud Functions, a Node.js with mocha framework for functions development. In effect, the Cloud Functions Test SDK provides automation atop the Cloud Functions shell.

You can find more about the Cloud Functions shell and Cloud Functions Test SDK at[Test functions interactively](https://firebase.google.com/docs/functions/local-shell)and[Unit testing of Cloud Functions](https://firebase.google.com/docs/functions/unit-testing).

## How theCloud Functionsemulator differs from production

TheCloud Functionsemulator is fairly close to the production environment for the majority of use cases. We've put extensive work into ensuring everything within the Node runtime is as close to production as possible. However, the emulator does not mimic the full containerized production environment, so while your function code will execute realistically, other aspects of your environment (i.e. local files, behavior after functions crashes, etc.) will differ.

### Cloud IAM

The Firebase Emulator Suite does not attempt to replicate or respect any IAM-related behavior for running. Emulators adhere to the Firebase Security Rules provided, but in situations where IAM would normally be used, for example to set Cloud Functions invoking service account and thus permissions, the emulator is not configurable and will use the globally-available account on your developer machine, similar to running a local script directly.

### Memory and processor restrictions

The emulator does not enforce memory or processor restrictions for your functions. However, the emulator does support timing out functions via the`timeoutSeconds`runtime argument.

Note that function execution time may differ from production when functions are run in the emulator. We recommend that after you've designed and tested functions with the emulator, you run limited tests in production to confirm execution times.

### Planning for differences in local and production environments

Since the emulator runs on your local machine, it depends on your local environment for applications and built-in programs and utilities.

Be aware that your local environment forCloud Functionsdevelopment may differ from the Google production environment:

- Applications you install locally to simulate the production environment (e.g. ImageMagick from[this tutorial](https://firebase.google.com/docs/storage/extend-with-functions#example_image_transformation)) may differ in behavior from production, especially if you require a different versions or develop in a non-Linux environment. Consider deploying your own binary copy of the missing program alongside your function deployment.

- Similarly, built-in utilities (e.g., shell commands like`ls`,`mkdir`) may differ from versions available in production, especially if you're developing in a non-Linux environment (e.g., macOS). You can handle this issue by using Node-only alternatives to native commands, or by building Linux binaries to bundle with your deployment.

### Retrying

The Cloud Functions emulator does not support retrying functions on failure.

## What next?

- For a curated set of videos and detailed how-to examples, follow the[Firebase Emulators Training Playlist](https://firebase.google.com/learn/pathways/firebase-emulators).
- Learn more about theCloud Functions for Firebaseemulator at[Run functions locally](https://firebase.google.com/docs/functions/local-emulator).