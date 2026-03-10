# Source: https://firebase.google.com/docs/database/flutter/start.md.txt

# Get Started with Realtime Database

<br />

## Prerequisites

1. [Install `firebase_core`](https://firebase.google.com/docs/flutter/setup) and add the initialization code to your app if you haven't already.
2. Add your app to your Firebase project in the [Firebase console](https://console.firebase.google.com/).

## Create a Database

1. Navigate to the **Realtime Database** section of the [Firebase console](https://console.firebase.google.com/project/_/database).
   You'll be prompted to select an existing Firebase project.
   Follow the database creation workflow.

2. Select a starting mode for your security rules:

   **Test mode**

   Good for getting started with the mobile and web client libraries,
   but allows anyone to read and overwrite your data. After testing, **make
   sure to review the [Understand Firebase Realtime Database Rules](https://firebase.google.com/docs/database/security)
   section.**

   > [!NOTE]
   > **Note:** If you create a database in Test mode and make no changes to the default world-readable and world-writeable security rules within a trial period, you will be alerted by email, then your database rules will deny all requests. Note the expiration date during the Firebase console setup flow.

   To get started, select testmode.

   **Locked mode**

   Denies all reads and writes from mobile and web clients.
   Your authenticated application servers can still access your database.
3. Choose a region for the database. Depending on your choice of region,
   the database namespace will be of the form `<databaseName>.firebaseio.com` or
   `<databaseName>.<region>.firebasedatabase.app`. For more information, see
   [select locations for your project](https://firebase.google.com/docs/projects/locations#rtdb-locations).

4. Click **Done**.

When you enable Realtime Database, it also enables the API in the
[Cloud API Manager](https://console.cloud.google.com/projectselector/apis/api/firebasedatabase.googleapis.com/overview).

## Add Firebase Realtime Database to your app

1. From the root of your Flutter project, run the following command to install the plugin:

       flutter pub add firebase_database

2. Once complete, rebuild your Flutter application:

       flutter run

## Configure database rules

The Realtime Database provides a declarative rules language that allows you to
define how your data should be structured, how it should be indexed, and when
your data can be read from and written to.

> [!NOTE]
> **Note:** By default, read and write access to your database is restricted so only authenticated users can read or write data. To get started without setting up Firebase Authentication, you can [configure your rules for public access](https://firebase.google.com/docs/rules/basics#default_rules_locked_mode). This does make your database open to anyone, even people not using your app, so be sure to restrict your database again when you set up authentication.

## Initialize the Firebase Realtime Database package

To start using the Realtime Database package within your project, import it at
the top of your project files:

    import 'package:firebase_database/firebase_database.dart';

To use the default Database instance, call the `instance`
getter on `FirebaseDatabase`:

    FirebaseDatabase database = FirebaseDatabase.instance;

If you'd like to use it with a secondary Firebase App, use the static `instanceFor` method:

    FirebaseApp secondaryApp = Firebase.app('SecondaryApp');
    FirebaseDatabase database = FirebaseDatabase.instanceFor(app: secondaryApp);

If you'd like to use a different RTDB instance on the same project, you can pass in a `databaseUrl` using
the static `instanceFor` method:

    final firebaseApp = Firebase.app();
    final rtdb = FirebaseDatabase.instanceFor(app: firebaseApp, databaseURL: 'https://your-realtime-database-url.firebaseio.com/');

## Next Steps

- Learn how to [structure data](https://firebase.google.com/docs/database/flutter/structure-data) for Realtime Database.

- [Scale your data across multiple database instances.](https://firebase.google.com/docs/database/usage/sharding)

- [Read and write data.](https://firebase.google.com/docs/database/flutter/read-and-write)

- [View your database in the
  Firebase console.](https://console.firebase.google.com/project/_/database/data)