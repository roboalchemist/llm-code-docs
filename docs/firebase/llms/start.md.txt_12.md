# Source: https://firebase.google.com/docs/database/cpp/start.md.txt

The Firebase Realtime Database stores and synchronizes data using a NoSQL cloud
database. Data is synchronized across all clients in realtime, and remains
available when your app goes offline.

## Before You Begin

Before you can use
[Firebase Realtime Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database),
you need to:

- Register your C++ project and configure it to use Firebase.

  If your C++ project already uses Firebase, then it's already registered and
  configured for Firebase.
- Add the [Firebase C++ SDK](https://firebase.google.com/download/cpp) to your C++ project.

> [!NOTE]
> **Find detailed instructions for these initial
> setup tasks in
> [Add Firebase to your C++
> project](https://firebase.google.com/docs/cpp/setup#note-select-platform).**

Note that adding Firebase to your C++ project involves tasks both in the
[Firebase console](https://console.firebase.google.com/) and in your open C++ project (for example, you download
Firebase config files from the console, then move them into your C++ project).

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

## Create and Initialize firebase::App

Before you can access the Realtime Database, you'll need to create and initialize the
[`firebase::App`](https://firebase.google.com/docs/reference/cpp/class/firebase/app).

> [!NOTE]
> You only need to initialize firebase::App once, no matter how many Firebase C++ features you use.

Include the header file for `firebase::App`:

```c++
#include "firebase/app.h"
```

### Android


Create the `firebase::App`, passing the JNI environment and a `jobject`
reference to the Java Activity as arguments:

```c++
app = ::firebase::App::Create(::firebase::AppOptions("APPLICATION NAME"), jni_env, activity);
```

### iOS+


Create the `firebase::App`:

```c++
app = ::firebase::App::Create(::firebase::AppOptions("APPLICATION NAME"));
```

## Access the firebase::database::Database Class

The [`firebase::database::Database`](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database)
is the entry point for the Firebase Realtime Database C++ SDK.

```c++
::firebase::database::Database *database = ::firebase::database::Database::GetInstance(app);
```

If you have chosen to use public access for your rules, you can proceed to the
sections on saving and retrieving data.

## Setting up Restricted Access

If you do not want to use public access you can add Firebase Authentication to your
app to control access to the database.

## Next Steps

- Learn how to [structure data](https://firebase.google.com/docs/database/cpp/structure-data) for Realtime Database.

- [Scale your data across multiple database
  instances.](https://firebase.google.com/docs/database/usage/sharding)

- [Save data.](https://firebase.google.com/docs/database/cpp/save-data)

- [Retrieve data.](https://firebase.google.com/docs/database/cpp/retrieve-data)

- [View your database in the
  Firebase console.](https://console.firebase.google.com/project/_/database/data)

- Prepare to launch your app:


  - Set up [budget
    alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails) for your project in the Google Cloud console.
  - Monitor the [*Usage and billing*
    dashboard](https://console.firebase.google.com/project/_/usage) in the Firebase console to get an overall picture of your project's usage across multiple Firebase services. You can also visit the [Realtime Database *Usage*
    dashboard](https://console.firebase.google.com/project/_/database/usage) for more detailed usage information.
  - Review the [Firebase launch checklist](https://firebase.google.com/support/guides/launch-checklist).

## Known Issues

- On desktop platforms (Windows, Mac, Linux), the Firebase C++ SDK uses REST to access your database. Because of this, you must [declare the indexes you use](https://firebase.google.com/docs/database/security/#section-defining-indexes) with Query::OrderByChild() on desktop or your listeners will fail.
- The desktop workflow version of Realtime Database does not support offline or persistence.