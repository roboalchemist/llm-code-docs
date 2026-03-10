# Source: https://firebase.google.com/docs/emulator-suite/connect_functions.md.txt

> [!NOTE]
> **Beta.** This emulator is currently in beta. It might be
> changed in backward-incompatible ways. As always, feedback is greatly
> appreciated. Let us know what you think!

Before connecting your app to the Cloud Functions emulator, make sure that
you [understand the overall Firebase Local Emulator Suite workflow](https://firebase.google.com/docs/emulator-suite/connect_and_prototype),
and that you [install and configure](https://firebase.google.com/docs/emulator-suite/install_and_configure)
the Local Emulator Suite and review its [CLI commands](https://firebase.google.com/docs/emulator-suite/install_and_configure#startup).

## Choose a Firebase project

The Firebase Local Emulator Suite emulates products for a single Firebase project.

To select the project to use, before you start the emulators, in the CLI run
`firebase use` in your working directory. Or, you can pass
the `--project` flag to each emulator
command.

> [!NOTE]
> **Note:** It's generally a good practice to use one project ID for all emulator invocations, so the Emulator Suite UI, different product emulators, and all running instances of a particular emulator can communicate correctly in all cases. In fact, by default, the Local Emulator Suite will warn on detecting multiple project IDs in use, though you can override this behavior. For guidance on setting and managing project IDs, see the [Installation and configuration guide](https://firebase.google.com/docs/emulator-suite/install_and_configure#project_id_configuration).

Local Emulator Suite supports emulation of *real* Firebase projects and
*demo* projects.

| Project type | Features | Use with emulators |
|---|---|---|
| Real | A real Firebase project is one you created and configured (most likely via the Firebase console). Real projects have live resources, like database instances, storage buckets, functions, or any other resource you set up for that Firebase project. | When working with real Firebase projects, you can run emulators for any or all of the supported products. For any products you are not emulating, your apps and code will interact with the *live* resource (database instance, storage bucket, function, etc.). |
| Demo | A demo Firebase project has no *real* Firebase configuration and no live resources. These projects are usually accessed via codelabs or other tutorials. Project IDs for demo projects have the `demo-` prefix. | When working with demo Firebase projects, your apps and code interact with emulators *only*. If your app attempts to interact with a resource for which an emulator isn't running, that code will fail. |

We recommend you use demo projects wherever possible. Benefits include:

- Easier setup, since you can run the emulators without ever creating a Firebase project
- Stronger safety, since if your code accidentally invokes non-emulated (production) resources, there is no chance of data change, usage and billing
- Better offline support, since there is no need to access the internet to download your SDK configuration.

> [!NOTE]
> **Note:** If you want to emulate cross-service interactions such as database-triggered Cloud Functions or Security Rules that rely on Authentication you must make sure that the project ID in your code (in `initializeApp()`, etc.) matches the project ID used by the Firebase CLI.

## Instrument your app to talk to the emulators

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

## Configure a local testing environment

If your functions rely on dotenv-based
[environment configuration](https://firebase.google.com/docs/functions/config-env#env-variables),
you can emulate that behavior in your local testing environment.

When using a local Cloud Functions emulator, you can override environment
variables for your project by setting up a `.env.local` file. Contents of
`.env.local` take precedence over `.env` and the project-specific `.env` file.

For example, a project could include these three files containing slightly
different values for development and local testing:

|---|---|---|
| `.env` | `.env.dev` | `.env.local` |
| PLANET=Earth AUDIENCE=Humans | AUDIENCE=Dev Humans | AUDIENCE=Local Humans |

When started in the local context, the emulator loads the environment
variables as shown:

      $ firebase emulators:start
      i  emulators: Starting emulators: functions
      # Starts emulator with following environment variables:
      #  PLANET=Earth
      #  AUDIENCE=Local Humans

### Secrets and credentials in the Cloud Functions emulator

The Cloud Functions emulator supports the use of secrets to
[store and access sensitive configuration information](https://firebase.google.com/docs/functions/config-env#create-secret).
By default, the emulator will try to access your production secrets using
[application default credentials](https://cloud.google.com/docs/authentication/production).
In certain situations like CI environments, the emulator may fail to access
secret values due to permission restrictions.

Similar to Cloud Functions emulator support for environment variables, you can
override secrets values by setting up a `.secret.local` file. This makes it
easy for you to test your functions locally, especially if you don't have access
to the secret value.

## What other tools for testing Cloud Functions exist?

The Cloud Functions emulator is supplemented by other prototype and test
tools:

- The Cloud Functions shell, which allows for interactive, iterative functions prototyping and development. The shell employs the Cloud Functions emulator with a REPL-style interface for development. No integration with the Cloud Firestore or Realtime Database emulators is provided. Using the shell, you mock data and perform function calls to simulate interaction with products that the Local Emulator Suite does not currently support: Analytics, Remote Config, and Crashlytics.
- The Firebase Test SDK for Cloud Functions, a Node.js with mocha framework for functions development. In effect, the Cloud Functions Test SDK provides automation atop the Cloud Functions shell.

You can find more about the Cloud Functions shell and Cloud Functions Test SDK
at [Test functions interactively](https://firebase.google.com/docs/functions/local-shell) and
[Unit testing of Cloud Functions](https://firebase.google.com/docs/functions/unit-testing).

## How the Cloud Functions emulator differs from production

The Cloud Functions emulator is fairly close to the production environment
for the majority of use cases. We've put extensive work into ensuring everything
within the Node runtime is as close to production as possible. However, the
emulator does not mimic the full containerized production environment,
so while your function code will execute realistically, other aspects of your
environment (i.e. local files, behavior after functions crashes, etc.) will
differ.

### Cloud IAM

The Firebase Emulator Suite does not attempt to replicate or respect any
IAM-related behavior for running. Emulators adhere to the Firebase Security
Rules provided, but in situations where IAM would normally be used, for example
to set Cloud Functions invoking service account and thus permissions, the
emulator is not configurable and will use the globally-available account on
your developer machine, similar to running a local script directly.

### Memory and processor restrictions

The emulator does not enforce memory or processor restrictions for your
functions. However, the emulator does support timing out functions via the
`timeoutSeconds` runtime argument.

Note that function execution time may differ from production when functions are
run in the emulator. We recommend that after you've designed and tested
functions with the emulator, you run limited tests in production to confirm
execution times.

### Planning for differences in local and production environments

Since the emulator runs on your local machine, it depends on your local
environment for applications and built-in programs and utilities.

Be aware that your local environment for Cloud Functions development may
differ from the Google production environment:

- Applications you install locally to simulate the production environment (e.g.
  ImageMagick from [this tutorial](https://firebase.google.com/docs/storage/extend-with-functions#example_image_transformation))
  may differ in behavior from production, especially if you require a different
  versions or develop in a non-Linux environment. Consider deploying your own
  binary copy of the missing program alongside your function deployment.

- Similarly, built-in utilities (e.g., shell commands like `ls`, `mkdir`) may
  differ from versions available in production, especially if you're developing in
  a non-Linux environment (e.g., macOS). You can handle this issue by using
  Node-only alternatives to native commands, or by building Linux binaries to
  bundle with your deployment.

### Retrying

The Cloud Functions emulator does not support retrying functions on failure.

## What next?

- For a curated set of videos and detailed how-to examples, follow the [Firebase Emulators Training Playlist](https://firebase.google.com/learn/pathways/firebase-emulators).
- Learn more about the Cloud Functions for Firebase emulator at [Run functions locally](https://firebase.google.com/docs/functions/local-emulator).