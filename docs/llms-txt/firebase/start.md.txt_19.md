# Source: https://firebase.google.com/docs/storage/unity/start.md.txt

<br />

[Video](https://www.youtube.com/watch?v=JAaCUmQ6LBo)

Cloud Storage for Firebase lets you upload and share user generated content, such
as images and video, which allows you to build rich media content into your
apps. Your data is stored in a
[Google Cloud Storage](https://cloud.google.com/storage) bucket --- an
exabyte scale object storage solution with high availability and global
redundancy. Cloud Storage for Firebase lets you securely upload these files
directly from mobile devices and web browsers, handling spotty networks with
ease.

## Before you begin

Before you can use
[Cloud Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage),
you need to:

- Register your Unity project and configure it to use Firebase.

  - If your Unity project already uses Firebase, then it's already
    registered and configured for Firebase.

  - If you don't have a Unity project, you can download a
    [sample app](https://github.com/google/mechahamster).

- Add the [Firebase Unity SDK](https://firebase.google.com/download/unity) (specifically, `FirebaseStorage.unitypackage`) to
  your Unity project.

> [!NOTE]
> **Find detailed instructions for these initial
> setup tasks in
> [Add Firebase to your Unity project](https://firebase.google.com/docs/unity/setup#prerequisites).**

Note that adding Firebase to your Unity project involves tasks both in the
[Firebase console](https://console.firebase.google.com/) and in your open Unity project
(for example, you download Firebase config files from the console, then move
them into your Unity project).

Also, make sure your Firebase project is on the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing), which
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
     [create multiple buckets](https://firebase.google.com/docs/storage/unity/start#use_multiple_storage_buckets), each with its
     own location.

4. Configure the Firebase Security Rules for your default bucket. During development,
   consider [setting up your rules for public access](https://firebase.google.com/docs/storage/unity/start#set_up_public_access).

5. Click **Done**.

You can now view the bucket in the
[Cloud Storage *Files* tab](https://console.firebase.google.com/project/_/storage/)
of the Firebase console. Your default bucket name format is
`PROJECT_ID.firebasestorage.app`.

> [!NOTE]
> **Note:** Starting October 30, 2024, all new default Cloud Storage buckets have the name format `PROJECT_ID.firebasestorage.app`. Any default buckets created *before* that date have the name format `PROJECT_ID.appspot.com`. Learn more in the [FAQs](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#all-changes-default-storage-bucket).

## Set up public access

Cloud Storage for Firebase provides a declarative rules language that allows you
to define how your data should be structured, how it should be indexed, and when
your data can be read from and written to. By default, read and write access to
Cloud Storage is restricted so only authenticated users can read or write
data. To get started without setting up [Authentication](https://firebase.google.com/docs/auth), you can
[configure your rules for public access](https://firebase.google.com/docs/storage/security/rules-conditions#public).

This does make Cloud Storage open to anyone, even people not using your
app, so be sure to restrict your Cloud Storage again when you set up
authentication.

## Access the `FirebaseStorage` class

The [`Firebase.Storage.FirebaseStorage`](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage)
is the entry point for the Cloud Storage Unity SDK.

```c#
// Get a reference to the storage service, using the default Firebase App
FirebaseStorage storage = FirebaseStorage.DefaultInstance;
```

You're ready to start using Cloud Storage!

Next step? Learn how to
[create a Cloud Storage reference](https://firebase.google.com/docs/storage/unity/create-reference).

## Advanced setup

There are a few use cases that require additional setup:

- Using Cloud Storage buckets in [multiple geographic regions](https://cloud.google.com/storage/docs/bucket-locations)
- Using Cloud Storage buckets in [different storage classes](https://cloud.google.com/storage/docs/storage-classes)
- Using Cloud Storage buckets with multiple authenticated users in the same app

The first use case is perfect if you have users across the world, and want to
store their data near them. For instance, you can create buckets in the US,
Europe, and Asia to store data for users in those regions to reduce latency.

The second use case is helpful if you have data with different access patterns.
For instance: you can set up a multi-regional or regional bucket that stores
pictures or other frequently accessed content, and a nearline or coldline bucket
that stores user backups or other infrequently accessed content.

In either of these use cases, you'll want to
[use multiple Cloud Storage buckets](https://firebase.google.com/docs/storage/unity/start#use_multiple_storage_buckets).

The third use case is useful if you're building an app, like Google Drive, which
lets users have multiple logged in accounts (for instance, a personal account
and a work account). You can [use a custom Firebase App](https://firebase.google.com/docs/storage/unity/start#use_a_custom_firebaseapp)
instance to authenticate each additional account.

### Use multiple Cloud Storage buckets

If you want to use a Cloud Storage bucket other than the default provided above,
or use multiple Cloud Storage buckets in a single app, you can create an instance
of `FirebaseStorage` that references your custom bucket:

```c#
// Get a non-default Storage bucket
var storage = FirebaseStorage.GetInstance("gs://my-custom-bucket");
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

If you're building a more complicated app using a custom `FirebaseApp`, you
can create an instance of `FirebaseStorage` initialized with that
app:

```c#
// Get the default bucket from a custom FirebaseApp
FirebaseStorage storage = FirebaseStorage.GetInstance(customApp);

// Get a non-default bucket from a custom FirebaseApp
FirebaseStorage storageCustom = FirebaseStorage.GetInstance(customApp, "gs://my-custom-bucket");
```

## Next steps

- Prepare to launch your app:


  - Set up [budget
    alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails) for your project in the Google Cloud console.
  - Monitor the [*Usage and billing*
    dashboard](https://console.firebase.google.com/project/_/usage) in the Firebase console to get an overall picture of your project's usage across multiple Firebase services. You can also visit the [Cloud Storage *Usage*
    dashboard](https://console.firebase.google.com/project/_/storage/usage) for more detailed usage information.
  - Review the [Firebase launch checklist](https://firebase.google.com/support/guides/launch-checklist).