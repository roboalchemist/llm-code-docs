# Source: https://firebase.google.com/docs/hosting/faq-and-troubleshooting.md.txt

<br />

This page provides answers to frequently asked questions (FAQs) about
Firebase Hosting.

## Hosting questions

<br />

#### Can a project on the Spark pricing plan store executable files?

<br />

For no-cost (Spark) plan projects, Firebase blocks uploads and hosting of certain
executable file types for Windows, Android and Apple by Cloud Storage for Firebase and
Firebase Hosting. This policy exists to prevent abuse on our platform.


Serving, hosting and file uploads of disallowed files are blocked for all Spark projects created
on or after Sept 28th, 2023. For existing Spark projects with files uploaded before that date,
such files can still be uploaded and hosted.

This restriction applies to Spark plan projects. Projects on the pay as you go (Blaze) plan
are not affected.


The following file types cannot be hosted on Firebase Hosting and Cloud Storage for Firebase:

- Windows files with `.exe`, `.dll` and `.bat` extensions
- Android files with `.apk` extension
- Apple platform files with `.ipa` extension

**What do I need to do?**

If you still want to host these file types after September 28th, 2023:

- For Hosting: upgrade to the Blaze plan before you can deploy these file types to Firebase Hosting via the `firebase deploy` command.
- For Storage: upgrade to the Blaze plan to upload these file types to the bucket of your choice using the GCS CLI, the Firebase console, or Google Cloud console.

Use Firebase tools to manage your Firebase Hosting and Cloud Storage resources.

- For managing resources in Firebase Hosting, use the Firebase console to delete releases [according to this guide](https://firebase.google.com/docs/hosting/manage-hosting-resources#delete-release).
- For managing resources in Cloud Storage, navigate to the [Storage
  product page](https://console.firebase.google.com/project/_/storage/) in your project.
  1. On the **Files** tab, locate disallowed files to delete in your folder hierarchy, then select them using the checkbox next to the filename(s) on the left-hand side of the panel.
  2. Click **Delete**, and confirm the files were deleted.

Please refer to our documentation for additional information on managing
[Hosting resources with Firebase tools](https://firebase.google.com/docs/hosting/manage-hosting-resources) and
[Cloud Storage for Firebase
buckets with client libraries](https://firebase.google.com/docs/storage/admin/start#google-cloud-storage-client-libraries).

<br />

<br />

#### Why does my Hosting release history table in the Firebase console show file counts that are more than what my local project actually has?

<br />

<br />


Firebase automatically adds extra files containing metadata about the
Hosting site, and these files are included in the total file count for
the release.

<br />

<br />

#### What's the largest file size that I can deploy to Firebase Hosting?

<br />

<br />


Hosting has a maximum size limit of 2 GB for
individual files.

<br />

<br />


We recommend storing large files using
[Cloud Storage](https://firebase.google.com/docs/storage), which offers a
maximum size limit in the terabyte range for individual objects.

<br />

<br />

#### How many Hosting sites can I have per Firebase project?

<br />

<br />


The [Firebase Hosting multisite
feature](https://firebase.google.com/docs/hosting/multisites) supports a maximum of 36 sites per
project.

<br />