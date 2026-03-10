# Source: https://firebase.google.com/docs/storage/web/start.md.txt

# Get started with Cloud Storage on web

<br />

Cloud Storage for Firebase lets you upload and share user generated content, such
as images and video, which allows you to build rich media content into your
apps. Your data is stored in a
[Google Cloud Storage](https://cloud.google.com/storage) bucket --- an
exabyte scale object storage solution with high availability and global
redundancy. Cloud Storage for Firebase lets you securely upload these files
directly from mobile devices and web browsers, handling spotty networks with
ease.

## Before you begin

1. If you haven't already, make sure you've completed the
   [getting started guide for web apps](https://firebase.google.com/docs/web/setup). This includes:

   - Creating a Firebase project.

   - Registering your web app with the project,
     and connecting your app to Firebase by adding the Firebase JS SDK and
     your Firebase config object to your app.

2. Make sure your Firebase project is on the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing), which
   is a requirement that started in October 2024 (see our
   [FAQs](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024)).
   If you're new to Firebase and Google Cloud, check if you're eligible for a
   [$300 credit](https://firebase.google.com/support/faq#pricing-free-trial).

## Create a default Cloud Storage bucket

1. From the navigation pane of the [Firebase console](https://console.firebase.google.com/), select **Storage**.

   If your project is not yet on the pay-as-you-go Blaze pricing plan, then you'll be
   prompted to upgrade your project.
2. Click **Get started**.

3. Select a [location](https://firebase.google.com/docs/storage/locations) for your default bucket.

   - Buckets in `US-CENTRAL1`, `US-EAST1`, and `US-WEST1` can take advantage of the
     ["Always Free" tier](https://cloud.google.com/storage/pricing#cloud-storage-always-free) for Google Cloud Storage.
     Buckets in all other locations follow
     [Google Cloud Storage pricing and usage](https://cloud.google.com/storage/pricing).

   - If you'd like, you can later
     [create multiple buckets](https://firebase.google.com/docs/storage/web/start#use_multiple_storage_buckets), each with its
     own location.

4. Configure the Firebase Security Rules for your default bucket. During development,
   consider [setting up your rules for public access](https://firebase.google.com/docs/storage/web/start#set_up_public_access).

5. Click **Done**.

You can now view the bucket in the
[Cloud Storage *Files* tab](https://console.firebase.google.com/project/_/storage/)
of the Firebase console. Your default bucket name format is
`PROJECT_ID.firebasestorage.app`.

> [!NOTE]
> **Note:** Starting October 30, 2024, all new default Cloud Storage buckets have the name format `PROJECT_ID.firebasestorage.app`. Any default buckets created *before* that date have the name format `PROJECT_ID.appspot.com`. Learn more in the [FAQs](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#all-changes-default-storage-bucket).

## Set up public access

Cloud Storage for Firebase provides a declarative rules language that lets you
define how your data should be structured, how it should be indexed, and when
your data can be read from and written to. By default, read and write access to
Cloud Storage is restricted so only authenticated users can read or write
data. To get started without setting up [Authentication](https://firebase.google.com/docs/auth), you can
[configure your rules for public access](https://firebase.google.com/docs/storage/security/rules-conditions#public).

This does make Cloud Storage open to anyone, even people not using your
app, so be sure to restrict your Cloud Storage again when you set up
authentication.

## Add the Cloud Storage JS SDK and initialize Cloud Storage

You must specify your Cloud Storage bucket name when initializing the
JavaScript SDK.

You can find your Cloud Storage bucket name in the
[Cloud Storage *Files* tab](https://console.firebase.google.com/project/_/storage/)
of the Firebase console. Depending on when you created your default bucket,
the bucket name will be in one of the following formats:

- `PROJECT_ID.firebasestorage.app` *(default bucket created **on or after**
  October 30, 2024)*
- `PROJECT_ID.appspot.com` *(default bucket created **before**
  October 30, 2024)*

Initialize the SDK using the following code snippet:

### Web


> [!NOTE]
> [Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular web API and [upgrade](https://firebase.google.com/docs/web/modular-upgrade) from the namespaced API.

<br />

```
import { initializeApp } from "firebase/app";
import { getStorage } from "firebase/storage";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
  // ...
  storageBucket: 'BUCKET_NAME'
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


// Initialize Cloud Storage and get a reference to the service
const storage = getStorage(app);
```

### Web


> [!NOTE]
> [Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular web API and [upgrade](https://firebase.google.com/docs/web/modular-upgrade) from the namespaced API.

<br />

```
import firebase from "firebase/app";
import "firebase/compat/storage";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
  // ...
  storageBucket: 'BUCKET_NAME'
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);


// Initialize Cloud Storage and get a reference to the service
const storage = firebase.storage();
```

You're ready to start using Cloud Storage!

Next step? Learn how to
[create a Cloud Storage reference](https://firebase.google.com/docs/storage/web/create-reference).

## Advanced setup

There are a few use cases that require additional setup:

- Using Cloud Storage buckets in [multiple geographic regions](https://cloud.google.com/storage/docs/bucket-locations)
- Using Cloud Storage buckets in [different storage classes](https://cloud.google.com/storage/docs/storage-classes)
- Using Cloud Storage buckets with multiple authenticated users in the same app

The first use case is perfect if you have users across the world, and want to
store their data near them. For example, you can create buckets in the US,
Europe, and Asia to store data for users in those regions to reduce latency.

The second use case is helpful if you have data with different access patterns.
For example: you can set up a multi-regional or regional bucket that stores
pictures or other frequently accessed content, and a nearline or coldline bucket
that stores user backups or other infrequently accessed content.

In either of these use cases, you'll want to
[use multiple Cloud Storage buckets](https://firebase.google.com/docs/storage/web/start#use_multiple_storage_buckets).

The third use case is useful if you're building an app, like Google Drive, which
lets users have multiple logged in accounts (for instance, a personal account
and a work account). You can [use a custom Firebase App](https://firebase.google.com/docs/storage/web/start#use_a_custom_firebaseapp)
instance to authenticate each additional account.

### Use multiple Cloud Storage buckets

If you want to use a Cloud Storage bucket other than the default bucket described
earlier in this guide, or use multiple Cloud Storage buckets in a single app, you
can create an instance of `firebase.storage` that references your custom bucket:

### Web

```javascript
import { getApp } from "firebase/app";
import { getStorage } from "firebase/storage";

// Get a non-default Storage bucket
const firebaseApp = getApp();
const storage = getStorage(firebaseApp, "gs://my-custom-bucket");
```

### Web

```javascript
// Get a non-default Storage bucket
var storage = firebase.app().storage("gs://my-custom-bucket");
```

### Working with imported buckets

When importing an existing Cloud Storage bucket into Firebase, you'll
have to grant Firebase the ability to access these files using the
`gsutil` tool, included in the
[Google Cloud SDK](https://cloud.google.com/sdk/docs/):

```
gsutil -m acl ch -r -u service-PROJECT_NUMBER@gcp-sa-firebasestorage.iam.gserviceaccount.com gs://BUCKET_NAME
```

You can find your project number as described in the
[introduction to Firebase projects](https://firebase.google.com/docs/projects/learn-more#project-number).

This does not affect newly created buckets, as those have the default access
control set to allow Firebase. This is a temporary measure, and will be
performed automatically in the future.

### Use a custom Firebase App

If you're building a more complicated app using a custom `firebase.app.App`, you
can create an instance of `firebase.storage.Storage` initialized with that app:

### Web

```javascript
import { getStorage } from "firebase/storage";

// Get the default bucket from a custom firebase.app.App
const storage1 = getStorage(customApp);

// Get a non-default bucket from a custom firebase.app.App
const storage2 = getStorage(customApp, "gs://my-custom-bucket");
```

### Web

```javascript
// Get the default bucket from a custom firebase.app.App
var storage = customApp.storage();

// Get a non-default bucket from a custom firebase.app.App
var storage = customApp.storage("gs://my-custom-bucket");
```

## Next steps

- Prepare to launch your app:

  - Enable [App Check](https://firebase.google.com/docs/app-check/web) to help ensure that only
    your apps can access your storage buckets.

  - Set up [budget
    alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails)
    for your project in the Google Cloud console.

  - Monitor the [*Usage and billing*
    dashboard](https://console.firebase.google.com/project/_/usage)
    in the Firebase console to get an overall picture of your project's
    usage across multiple Firebase services.
    You can also visit the [Cloud Storage *Usage*
    dashboard](https://console.firebase.google.com/project/_/storage/usage) for more
    detailed usage information.

  - Review the [Firebase launch checklist](https://firebase.google.com/support/guides/launch-checklist).