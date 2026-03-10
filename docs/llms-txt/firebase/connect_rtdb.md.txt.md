# Source: https://firebase.google.com/docs/emulator-suite/connect_rtdb.md.txt

Before connecting your app to the Realtime Database emulator, make sure that
you [understand the overall Firebase Local Emulator Suite workflow](https://firebase.google.com/docs/emulator-suite/connect_and_prototype?database=RTDB),
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

### Android, Apple platforms, and Web SDKs

Set up your in-app configuration or test classes to interact with the
Realtime Database as follows.

##### Kotlin

```kotlin
// 10.0.2.2 is the special IP address to connect to the 'localhost' of
// the host computer from an Android emulator.
val database = Firebase.database
database.useEmulator("10.0.2.2", 9000)
```

##### Java

```java
// 10.0.2.2 is the special IP address to connect to the 'localhost' of
// the host computer from an Android emulator.
FirebaseDatabase database = FirebaseDatabase.getInstance();
database.useEmulator("10.0.2.2", 9000);
```

##### Swift

```swift
    // In almost all cases the ns (namespace) is your project ID.
let db = Database.database(url:"http://127.0.0.1:9000?ns=YOUR_DATABASE_NAMESPACE")
```

### Web

```javascript
import { getDatabase, connectDatabaseEmulator } from "firebase/database";

const db = getDatabase();
if (location.hostname === "localhost") {
  // Point to the RTDB emulator running on localhost.
  connectDatabaseEmulator(db, "127.0.0.1", 9000);
} 
```

### Web

> [!NOTE]
> [Learn
> more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.

```javascript
var db = firebase.database();
if (location.hostname === "localhost") {
  // Point to the RTDB emulator running on localhost.
  db.useEmulator("127.0.0.1", 9000);
} 
```

No additional setup is needed to test Cloud Functions [triggered by Realtime Database events](https://firebase.google.com/docs/functions/database-events)
using the emulator. When the Realtime Database and Cloud Functions emulators are
both running, they automatically work together.

### Admin SDKs

The Firebase Admin SDKs automatically connect to the Realtime Database emulator when
the `FIREBASE_DATABASE_EMULATOR_HOST` environment variable is set:

    export FIREBASE_DATABASE_EMULATOR_HOST="127.0.0.1:9000"

> [!NOTE]
> **Note:** For emulators to work correctly the `FIREBASE_DATABASE_EMULATOR_HOST` environment variable must omit protocols such as `http://`.

If your code is running inside the Cloud Functions emulator your project ID
and other configuration will be automatically set when calling `initializeApp`.

If you want your Admin SDK code to connect to a shared emulator running in
another environment, you will need to specify the [the same project ID you set using the Firebase CLI](https://firebase.google.com/docs/emulator-suite/connect_rtdb#choose_a_firebase_project).
You can pass a project ID to `initializeApp` directly or set the
`GCLOUD_PROJECT` environment variable.

##### Node.js Admin SDK

```javascript
admin.initializeApp({ projectId: "your-project-id" });
```

##### Environment Variable

```
export GCLOUD_PROJECT="your-project-id"
```

## Clear your database between tests

To flush the Realtime Database between activities, you can clear the database reference. You can use this approach as an alternative to simply shutting down the emulator process.

> [!CAUTION]
> **Caution:** Only include code to flush your database in your test configuration. Check that this method is not called in production code by accident.

##### Kotlin

```kotlin
// With a DatabaseReference, write null to clear the database.
database.reference.setValue(null)
```

##### Java

```java
// With a DatabaseReference, write null to clear the database.
database.getReference().setValue(null);
```

##### Swift

```swift
// With a DatabaseReference, write nil to clear the database.
    Database.database().reference().setValue(nil);
```

### Web

```javascript
import { getDatabase, ref, set } from "firebase/database";

// With a database Reference, write null to clear the database.
const db = getDatabase();
set(ref(db), null);
```

### Web

> [!NOTE]
> [Learn
> more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.

```javascript
// With a database Reference, write null to clear the database.
firebase.database().ref().set(null);
```

Naturally, your code should await confirmation that the flush finished or failed using the asynchronous event handling features of your platform.

Having implemented a step like this, you can sequence your tests and trigger your functions with confidence that old data will be purged between runs and you're using a fresh baseline test configuration.

## Import and export data

The database and Cloud Storage for Firebase emulators allow you to export data
from a running emulator instance. Define a baseline set of data to use in your
unit tests or continuous integration workflows, then export it to be shared
among the team.

    firebase emulators:export ./dir

In tests, on emulator startup, import the baseline data.

    firebase emulators:start --import=./dir

You can instruct the emulator to export data on shutdown, either specifying an
export path or simply using the path passed to the `--import`
flag.

    firebase emulators:start --import=./dir --export-on-exit

These data import and export options work with the
`firebase emulators:exec` command as well. For more, refer to the
[emulator command reference](https://firebase.google.com/docs/emulator-suite/install_and_configure#startup).

## Visualize Security Rules activity

As you work through prototype and test loops, you can use visualization tools
and reports provided by the Local Emulator Suite.

### Visualize Rules evaluations

As you add Security Rules to your prototype you can debug them with
Local Emulator Suite tools.

After running a suite of tests, you can access test coverage reports that show
how each of your rules was evaluated. To get the reports, query an exposed
endpoint on the emulator while it's running. For a browser-friendly version,
use the following URL:

```
http://localhost:9000/.inspect/coverage?ns=<database_name>
```

This breaks your rules into expressions and subexpressions that you can
mouseover for more information, including number of executions and values
returned. For the raw JSON version of this data, include the following URL in
your query:

```
http://localhost:9000/.inspect/coverage.json?ns=<database_name>
```

## What next?

- For a curated set of videos and detailed how-to examples, follow the [Firebase Emulators Training Playlist](https://firebase.google.com/learn/pathways/firebase-emulators).
- Investigate advanced use cases involving Security Rules testing and the Firebase Test SDK: [Test Security Rules (Realtime Database)](https://firebase.google.com/docs/database/security/test-rules-emulator).
- Since triggered functions are a typical integration with Realtime Database, learn more about the Cloud Functions for Firebase emulator at [Run functions locally](https://firebase.google.com/docs/functions/local-emulator).