# Source: https://firebase.google.com/docs/data-connect/data-connect-emulator-suite.md.txt

Firebase Data Connect provides you with a local emulator for end-to-end
prototyping as well as continuous integration and continuous deployment
(CI/CD) flows:

- The Data Connect emulator interacts with a local integrated PGLite database instance to let you prototype queries and mutations and test client code in a fully local environment.
- The Data Connect emulator can also be used for non-interactive work. It lets you run automated tests and is suitable for use with CI/CD workflows. This is useful when your schemas are stable and you want to prototype and test client-side code.

This guide covers installation and usage of the emulator in more detail than
the quickstart.

## Install the Data Connect emulator

Before installing the Local Emulator Suite to use the Data Connect
emulator, you will need:

- Node.js version 18.0 or higher.

### Install the Firebase CLI and set up project directory

> [!NOTE]
> **Note:** If you've followed the [Get started with Firebase Data Connect](https://firebase.google.com/docs/data-connect/quickstart) guide, you can skip this section.

1. Install the Firebase CLI, [following the installation guide](https://firebase.google.com/docs/cli).
   Be sure to [update regularly](https://firebase.google.com/docs/cli#update-cli), since the
   Data Connect emulator is under active development with bug fixes and
   new features.

2. If you haven't already done so, initialize the current working directory as
   a Firebase project, following prompts to specify which products to use:

       firebase init

### Set or modify the Local Emulator Suite configuration

If you started the Data Connect emulator from the Firebase VS Code
extension, the emulator was installed for you, if needed.

You can use the Firebase CLI to manually install the emulator along with
other selected components of the Local Emulator Suite. This command starts a
configuration wizard that lets you select emulators of interest, download the
corresponding emulator binary files, and set emulator ports if the defaults are
not appropriate.

      firebase init emulators

Once an emulator is installed, no update checks are performed and no additional
automatic downloads will occur until you update your Firebase CLI version.

### Choose a Firebase project

In the setup flow, the Firebase CLI prompts you to choose or create a
Firebase project. If you choose an existing project you've set up with
Data Connect in the Firebase console, the configuration you chose
there will be suggested.

## Set up the emulator

> [!NOTE]
> **Note:** Usage of the emulator in the Firebase Data Connect VS Code extension is covered in [Get started with Firebase Data Connect](https://firebase.google.com/docs/data-connect/quickstart).

### Configure the emulator

Running the `firebase init` flow will guide you through emulator setup options.
Like other emulators in the Local Emulator Suite, configuration parameters
are stored in local project files.

- Your `firebase.json` file contains emulator port assignments.
  - The `emulators:ui` key does not apply to the Data Connect emulator.

### Work with local and production Data Connect resources

If you want to be sure not to impact production resources, set a `demo-`
projectID or make sure your client code is instrumented to connect to
the emulator, as discussed in a later section.

## Start the emulator

If you're running the emulator non-interactively, for example for CI/CD
workflows, start it with the `exec` option.

    firebase emulators:exec ./path/to/test-script.sh

If you're integrating predefined queries and mutations in client code and are
using the emulator specifically for testing clients, you can use the `start`
option for interactive work. You can also start the emulator from the VS Code
extension.

    firebase emulators:start

> [!NOTE]
> **Note:** When you start the emulator with `firebase emulators:start`, SDK code will be automatically generated just as if you had run `firebase sdk:generate`.

## Instrument your client code to talk to the emulator

Set up your in-app configuration or test classes to interact with the
Data Connect emulator as follows.

##### JavaScript

```javascript
import { initializeApp } from "firebase/app";
import { connectorConfig } from "@name-of-package";
import { connectDataConnectEmulator, getDataConnect } from 'firebase/data-connect';

// TODO: Replace the following with your app's Firebase project configuration
const firebaseConfig = {
  //...
};

const app = initializeApp(firebaseConfig);

const dataConnect = getDataConnect(app, connectorConfig);
connectDataConnectEmulator(dataConnect, "localhost", 9399);

// Make calls from your app
  
```

##### Kotlin Android

```kotlin
val connector = MoviesConnector.instance

// Connect to the emulator on "10.0.2.2:9399"
connector.dataConnect.useEmulator()

// (Alternatively) if you're running your emulator on non-default port:
connector.dataConnect.useEmulator(port = 9999)

// Make calls from your app
  
```

##### iOS

```
let connector = DataConnect.dataConnect(DefaultConnectorClient.connectorConfig)

// Connect to the emulator on "127.0.0.1:9399"
connector.useEmulator()

// (alternatively) if you're running your emulator on non-default port:
connector.useEmulator(port: 9999)

// Make calls from your app
  
```

## Use the emulator for testing and continuous integration

### Run containerized Local Emulator Suite images

Installation and configuration of the Local Emulator Suite with containers
in a typical CI setup is straightforward.

There are a few issues to note:

- Emulator binaries are installed and cached at `~/.cache/firebase/emulators/`. You may want to add this path to your CI cache configuration to avoid repeated downloads.
- If you don't have a `firebase.json` file in your repository, you must add a command line argument to the `emulators:start` or `emulators:exec` command to specify which emulators should be started. For example, `--only dataconnect`.

### Clear your database between tests

To reset your test environments between runs, Firebase recommends:

- Writing dedicated mutations to handle the following:
  - In setup, populate a local database instance with starting data.
  - In teardown, delete modified data from post-test database instance.

## How the Data Connect emulator differs from production

The Data Connect emulator simulates many features of the server-side
product. However, there are some exceptions to be aware of:

- The version and detailed configuration of PGLite may differ from the version of your production Cloud SQL instance.
- If you're using the emulator to develop with Data Connect's pgvector and Vertex API integration, calls to the Cloud Vertex API are made directly, rather than through Cloud SQL's Vertex integration. However, calls to the production API are still made, meaning you must use a real Firebase project, cannot use a `demo-` project, and costs of the Vertex API will be incurred.