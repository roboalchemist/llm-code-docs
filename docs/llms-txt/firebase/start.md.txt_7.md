# Source: https://firebase.google.com/docs/database/unity/start.md.txt

[Video](https://www.youtube.com/watch?v=MbIH4QT3xF8)

The Firebase Realtime Database stores and synchronizes data with our NoSQL cloud
database. Data is synced across all clients in realtime, and remains available
when your app goes offline.

## Before you begin

Before you can use
[Realtime Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database),
you need to:

- Register your Unity project and configure it to use Firebase.

  - If your Unity project already uses Firebase, then it's already
    registered and configured for Firebase.

  - If you don't have a Unity project, you can download a
    [sample app](https://github.com/google/mechahamster).

- Add the [Firebase Unity SDK](https://firebase.google.com/download/unity) (specifically, `FirebaseDatabase.unitypackage`) to
  your Unity project.

> [!NOTE]
> **Find detailed instructions for these initial
> setup tasks in
> [Add Firebase to your Unity project](https://firebase.google.com/docs/unity/setup#prerequisites).**

Note that adding Firebase to your Unity project involves tasks both in the
[Firebase console](https://console.firebase.google.com/) and in your open Unity project
(for example, you download Firebase config files from the console, then move
them into your Unity project).

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

## Setting up public access

The Realtime Database provides a declarative rules language that allows you to
define how your data should be structured, how it should be indexed, and when
your data can be read from and written to.

> [!NOTE]
> **Note:** By default, read and write access to your database is restricted so only authenticated users can read or write data. To get started without setting up [Authentication](https://firebase.google.com/docs/auth), you can [configure your rules for public access](https://firebase.google.com/docs/rules/basics#default_rules_locked_mode). This does make your database open to anyone, even people not using your app, so be sure to restrict your database again when you set up authentication.

## Next Steps

- Learn how to [structure data](https://firebase.google.com/docs/database/unity/structure-data) for Realtime Database.

- [Scale your data across multiple database
  instances.](https://firebase.google.com/docs/database/usage/sharding)

- [Save data.](https://firebase.google.com/docs/database/unity/save-data)

- [Retrieve data.](https://firebase.google.com/docs/database/unity/retrieve-data)

- [View your database in the
  Firebase console.](https://console.firebase.google.com/project/_/database/data)

- Prepare to launch your app:


  - Set up [budget
    alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails) for your project in the Google Cloud console.
  - Monitor the [*Usage and billing*
    dashboard](https://console.firebase.google.com/project/_/usage) in the Firebase console to get an overall picture of your project's usage across multiple Firebase services. You can also visit the [Realtime Database *Usage*
    dashboard](https://console.firebase.google.com/project/_/database/usage) for more detailed usage information.
  - Review the [Firebase launch checklist](https://firebase.google.com/support/guides/launch-checklist).