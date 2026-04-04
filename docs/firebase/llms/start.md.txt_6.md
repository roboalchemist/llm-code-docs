# Source: https://firebase.google.com/docs/database/rest/start.md.txt

The Firebase Realtime Database is a cloud-hosted database. Data is stored as
JSON and synchronized in realtime to every connected client. When you build
cross-platform apps with our Android, Apple platforms, and JavaScript SDKs,
all of your clients share one Realtime Database instance and automatically receive
updates with the newest data.

We can use any Firebase Realtime Database URL as a REST endpoint. All we need
to do is append `.json` to the end of the URL and send a request from
our favorite HTTPS client.

## Create an Account

First sign up for an account at no cost in the [Firebase console](https://console.firebase.google.com/). A new
Firebase app will be created for you with a unique URL ending in
`firebaseio.com`. You'll use this URL to authenticate your users and
to store and sync data to the app's database.

Within the [Firebase console](https://console.firebase.google.com/) you can create, manage and delete Firebase
apps. Clicking on a specific Firebase app lets you view and modify your app's
database in real time. In your app dashboard, you can also set
Firebase Realtime Database Security Rules, manage your
app's authentication, deploys, and view analytics.

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

## Choose a Helper Library

You can read and write data through the REST API directly from the command line.
In this guide we'll use [cURL](https://en.wikipedia.org/wiki/CURL)
for all of our examples. We also have several third-party helper libraries for
interacting with the REST API from your favorite language. You can use one of
the following helper libraries or create your own:

| Language | Libraries |
|---|---|
| Clojure | [taika](https://github.com/cloudfuji/taika) by [Cloudfuji](https://github.com/cloudfuji/) |
| Dart | [IO Client](https://github.com/firebase/firebase-dart#io-client) in the official [firebase-dart](https://pub.dartlang.org/packages/firebase) library |
| Go | [Firego](https://github.com/zabawaba99/firego) by [Steven Berlanga](https://github.com/zabawaba99) and [Tim Gossett](https://github.com/MrGossett) [Go Firebase](https://github.com/JustinTulloss/firebase) by Cosmin Nicolaescu and Justin Tulloss |
| Java | [firebase4j](https://github.com/bane73/firebase4j) by [Brandon Gresham](https://twitter.com/bane73) |
| Perl | [Firebase-Perl](https://metacpan.org/pod/Firebase) by Kiran Kumar and JT Smith |
| PHP | [firebase-php](https://github.com/kreait/firebase-php) by [kreait](https://github.com/kreait) [firebase-php](https://github.com/ktamas77/firebase-php) by [Tamas Kalman](https://github.com/ktamas77) |
| Python | [Pyrebase](https://github.com/thisbejim/Pyrebase) by [James Childs-Maidment](https://github.com/thisbejim) [python-firebase](http://ozgur.github.io/python-firebase/) by [Özgür Vatansever](https://github.com/ozgur) [python-firebase](https://github.com/mikexstudios/python-firebase) by [Michael Huynh](https://twitter.com/mikexstudios) |
| Ruby | [firebase-ruby](https://github.com/oscardelben/firebase-ruby) by [Oscar Del Ben](https://twitter.com/oscardelben) [BigBertha](http://derailed.github.io/bigbertha) by [Fernand Galiana](https://twitter.com/kitesurfer) [rest-firebase](https://github.com/CodementorIO/rest-firebase) by [Codementor](https://www.codementor.io/) |

## Next Steps

- Learn how to [structure data](https://firebase.google.com/docs/database/rest/structure-data) for Realtime Database.
- [Save data.](https://firebase.google.com/docs/database/rest/save-data)
- [Retrieve data.](https://firebase.google.com/docs/database/rest/retrieve-data)
- [View your database in the Firebase console.](https://console.firebase.google.com/project/_/database/data)