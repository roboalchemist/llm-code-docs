# Source: https://firebase.google.com/docs/database/web/start.md.txt

The Firebase Realtime Database is a cloud-hosted database. Data is stored as
JSON and synchronized in realtime to every connected client. When you build
cross-platform apps with our Android, Apple platforms, and JavaScript SDKs, all of your
clients share one Realtime Database instance and automatically receive
updates with the newest data.

## Prerequisites

If you haven't already, [install the Firebase JS SDK and initialize Firebase](https://firebase.google.com/docs/web/setup#add-sdk-and-initialize).

## Create a Database

1. Navigate to the **Realtime Database** section of the
   [Firebase console](https://console.firebase.google.com/project/_/database).
   You'll be prompted to select an existing Firebase project.
   Follow the database creation workflow.

2. Select a starting mode for your Firebase Security Rules:

   Test mode

   :   Good for getting started with the mobile and web client libraries,
       but allows anyone to read and overwrite your data. After testing, **make
       sure to review the [Understand Firebase Realtime Database Rules](https://firebase.google.com/docs/database/security)
       section.**

   :

       > [!NOTE]
       > **Note:** If you create a database in Test mode and make no changes to the default world-readable and world-writeable Security Rules within a trial period, you will be alerted by email, then your database rules will deny all requests. Note the expiration date during the Firebase console setup flow.

   :   To get started with the web, Apple, or Android SDK, select testmode.

   Locked mode

   :   Denies all reads and writes from mobile and web clients.
       Your authenticated application servers can still access your database.

3. Choose a location for the database.

   Depending on the
   [location of the database](https://firebase.google.com/docs/projects/locations#rtdb-locations), the
   URL for the new database will be in one of the following forms:
   - `DATABASE_NAME.firebaseio.com` (for
     databases in `us-central1`)

   - `DATABASE_NAME.REGION.firebasedatabase.app`
     (for databases in all other locations)

4. Click **Done**.

When you enable Realtime Database, it also enables the API in the
[Cloud API Manager](https://console.cloud.google.com/projectselector/apis/api/firebasedatabase.googleapis.com/overview).

## Configure Realtime Database Security Rules

The Realtime Database provides a declarative rules language that allows you to
define how your data should be structured, how it should be indexed, and when
your data can be read from and written to.

> [!NOTE]
> **Note:** By default, read and write access to your database is restricted so only authenticated users can read or write data. To get started without setting up [Authentication](https://firebase.google.com/docs/auth), you can [configure your rules for public access](https://firebase.google.com/docs/rules/basics#default_rules_locked_mode). This does make your database open to anyone, even people not using your app, so be sure to restrict your database again when you set up authentication.

## Add the Realtime Database JS SDK and initialize Realtime Database

You must specify your Realtime Database URL when initializing the JavaScript SDK.

You can find your Realtime Database URL in the *Realtime Database* section of the
[Firebase console](https://console.firebase.google.com/). Depending on the
[location of the database](https://firebase.google.com/docs/projects/locations#rtdb-locations),
the database URL will be in one of the following forms:

- `https://DATABASE_NAME.firebaseio.com` (for databases in `us-central1`)
- `https://DATABASE_NAME.REGION.firebasedatabase.app` (for databases in all other locations)

Initialize the SDK using the following code snippet:

### Web


> [!NOTE]
> [Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular web API and [upgrade](https://firebase.google.com/docs/web/modular-upgrade) from the namespaced API.

<br />

```
import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
  // ...
  // The value of `databaseURL` depends on the location of the database
  databaseURL: "https://DATABASE_NAME.firebaseio.com",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


// Initialize Realtime Database and get a reference to the service
const database = getDatabase(app);
```

### Web


> [!NOTE]
> [Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular web API and [upgrade](https://firebase.google.com/docs/web/modular-upgrade) from the namespaced API.

<br />

```
import firebase from "firebase/app";
import "firebase/compat/database";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
  // ...
  // The value of `databaseURL` depends on the location of the database
  databaseURL: "https://DATABASE_NAME.firebaseio.com",
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);


// Initialize Realtime Database and get a reference to the service
const database = firebase.database();
```

You're ready to start using the Firebase Realtime Database!

## Next Steps

- Learn how to [structure data](https://firebase.google.com/docs/database/web/structure-data) for Realtime Database.

- [Scale your data across multiple database
  instances](https://firebase.google.com/docs/database/usage/sharding).

- [Read and write data.](https://firebase.google.com/docs/database/web/read-and-write)

- [View your database in the
  Firebase console.](https://console.firebase.google.com/project/_/database/data)

- Prepare to launch your app:

  - Enable [App Check](https://firebase.google.com/docs/app-check/web) to help ensure that only your
    apps can access your databases.

  - Set up [budget
    alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails)
    for your project in the Google Cloud console.

  - Monitor the [*Usage and billing*
    dashboard](https://console.firebase.google.com/project/_/usage)
    in the Firebase console to get an overall picture of your project's
    usage across multiple Firebase services.
    You can also visit the [Realtime Database *Usage*
    dashboard](https://console.firebase.google.com/project/_/database/usage) for more
    detailed usage information.

  - Review the [Firebase launch checklist](https://firebase.google.com/support/guides/launch-checklist).