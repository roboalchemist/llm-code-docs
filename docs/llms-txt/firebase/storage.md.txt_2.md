# Source: https://firebase.google.com/docs/storage.md.txt

# Cloud Storage for Firebase

# Cloud Storage for Firebase

Cloud Storage for Firebase is built on fast and secure
Google Cloud infrastructure for app developers who need to store and serve
user-generated content, such as photos or videos.
[Video](https://www.youtube.com/watch?v=_tyjqozrEPY) Cloud Storage for Firebase is a powerful, simple, and cost-effective object storage service built for Google scale. The Firebase SDKs for Cloud Storage add Google security to file uploads and downloads for your Firebase apps, regardless of network quality.

<br />

You can use our client SDKs to store images, audio, video, or other
user-generated content. On the server, you can use the Firebase Admin SDK to
manage buckets and create download URLs, and use
[Google Cloud Storage APIs](https://cloud.google.com/storage/docs/reference/libraries)
to access your files.

<br />

Ready to get started? Choose your platform:

[iOS+](https://firebase.google.com/docs/storage/ios/start)
[Android](https://firebase.google.com/docs/storage/android/start)
[Web](https://firebase.google.com/docs/storage/web/start)
[Flutter](https://firebase.google.com/docs/storage/flutter/start)

[Unity](https://firebase.google.com/docs/storage/unity/start)
[C++](https://firebase.google.com/docs/storage/cpp/start)
[Admin](https://firebase.google.com/docs/storage/admin/start)

## Key capabilities

|---|---|
| Robust operations | Firebase SDKs for Cloud Storage perform uploads and downloads regardless of network quality. Uploads and downloads are robust, meaning they restart where they stopped, saving your users time and bandwidth. |
| Strong security | Firebase SDKs for Cloud Storage integrate with Firebase Authentication to provide simple and intuitive authentication for developers. You can use our declarative security model to allow access based on filename, size, content type, and other metadata. |
| High scalability | Cloud Storage is built for exabyte scale when your app goes viral. Effortlessly grow from prototype to production using the same infrastructure that powers Spotify and Google Photos. |

## How does it work?

Developers use the Firebase SDKs for Cloud Storage to upload and download files
directly from clients. If the network connection is poor, the client is able to
retry the operation right where it left off, saving your users time and
bandwidth.

Cloud Storage for Firebase stores your files in a
[Google Cloud Storage](https://cloud.google.com/storage) bucket,
making them accessible through both Firebase and Google Cloud. This allows you
the flexibility to upload and download files from mobile clients via the
Firebase SDKs for Cloud Storage. In addition, you can do server-side processing such
as image filtering or video transcoding using the
[Google Cloud Storage APIs](https://cloud.google.com/storage/docs/reference/libraries).
Cloud Storage scales automatically, meaning that there's no need to
migrate to any other provider. Learn more about all the benefits of our
[integration with Google Cloud](https://firebase.google.com/docs/storage/gcp-integration).

The Firebase SDKs for Cloud Storage integrate seamlessly with
[Firebase Authentication](https://firebase.google.com/docs/auth) to identify users, and we provide a
[declarative security language](https://firebase.google.com/docs/storage/security) that lets you set
access controls on individual files or groups of files, so you can make files as
public or private as you want.

## Implementation path

|---|---|---|
|   | Integrate the Firebase SDKs for Cloud Storage. | Quickly include clients using Gradle, Swift Package Manager, or a script include. |
|   | Create a Reference | Reference the path to a file, such as "images/mountains.png", to upload, download, or delete it. |
|   | Upload or Download | Upload or download to native types in memory or on disk. |
|   | Secure your Files | Use [Firebase Security Rules for Cloud Storage](https://firebase.google.com/docs/storage/security) to secure your files. |
|   | (Optional) Create and Share Download URLs | Use the [Firebase Admin SDK](https://firebase.google.com/docs/storage/admin/start) to generate shareable URLs to let users download objects. |

## Looking to store other types of data?

- [Cloud Firestore](https://firebase.google.com/docs/firestore) is a flexible, scalable database for mobile, web, and server development from Firebase and Google Cloud.
- The [Firebase Realtime Database](https://firebase.google.com/docs/database) stores JSON application data, like game state or chat messages, and synchronizes changes instantly across all connected devices. To learn more about the differences between database options, see [Choose a database: Cloud Firestore or Realtime Database](https://firebase.google.com/docs/firestore/rtdb-vs-firestore).
- [Firebase Remote Config](https://firebase.google.com/docs/remote-config) stores developer-specified key-value pairs to change the behavior and appearance of your app without requiring users to download an update.
- [Firebase Hosting](https://firebase.google.com/docs/hosting) hosts the HTML, CSS, and JavaScript for your website as well as other developer-provided assets like graphics, fonts, and icons.

## Next steps

- Upload your first file to Cloud Storage using our quickstarts for [iOS](https://github.com/firebase/quickstart-ios), [Android](https://github.com/firebase/quickstart-android), [Web](https://github.com/firebase/quickstart-js), [C++](https://github.com/firebase/quickstart-cpp), or [Unity](https://github.com/firebase/quickstart-unity).
- Add Cloud Storage to your [Apple](https://firebase.google.com/docs/storage/ios/start), [Android](https://firebase.google.com/docs/storage/android/start), [Web](https://firebase.google.com/docs/storage/web/start), [C++](https://firebase.google.com/docs/storage/cpp/start) or [Unity](https://firebase.google.com/docs/storage/unity/start) app.
- Learn about how to secure your files using [Firebase Security Rules for Cloud Storage](https://firebase.google.com/docs/storage/security).
- Add powerful new features such as image recognition or speech to text by [integrating with Google Cloud](https://firebase.google.com/docs/storage/gcp-integration).