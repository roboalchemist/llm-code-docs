# Source: https://firebase.google.com/docs/storage/admin/start.md.txt

# Introduction to the Admin Cloud Storage API

<br />

Cloud Storage for Firebase stores your data in a
[Google Cloud Storage](https://cloud.google.com/storage) bucket --- an
exabyte scale object storage solution with high availability and global
redundancy. The Firebase Admin SDK allows you to directly access your
Cloud Storage buckets from privileged environments. Then you can use
[Google Cloud Storage APIs](https://cloud.google.com/storage/docs/reference/libraries)
to manipulate the objects stored in the buckets.

The Admin SDK also lets you to create shareable URLs so users can
download objects in your buckets.

Also, make sure your Firebase project is on the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing), which
is a requirement that started in October 2024 (see our
[FAQs](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024)).
If you're new to Firebase and Google Cloud, check if you're eligible for a
[$300 credit](https://firebase.google.com/support/faq#pricing-free-trial).

## Use a default bucket

You can specify a default bucket name when initializing the Admin SDK. Then you
can retrieve an authenticated reference to this bucket.

The bucket name must *not* contain `gs://` or any other protocol prefixes.
For example, if the bucket URL displayed in the
[Firebase console](https://console.firebase.google.com/project/_/storage)
is `gs://PROJECT_ID.firebasestorage.app`, pass the string
`PROJECT_ID.firebasestorage.app` to the Admin SDK.

### Node.js

    const { initializeApp, cert } = require('firebase-admin/app');
    const { getStorage } = require('firebase-admin/storage');

    const serviceAccount = require('./path/to/serviceAccountKey.json');

    initializeApp({
      credential: cert(serviceAccount),
      storageBucket: '<BUCKET_NAME>.appspot.com'
    });

    const bucket = getStorage().bucket();

    // 'bucket' is an object defined in the @google-cloud/storage library.
    // See https://googlecloudplatform.github.io/google-cloud-node/#/docs/storage/latest/storage/bucket
    // for more details.

### Java

    FileInputStream serviceAccount = new FileInputStream("path/to/serviceAccountKey.json");

    FirebaseOptions options = FirebaseOptions.builder()
        .setCredentials(GoogleCredentials.fromStream(serviceAccount))
        .setStorageBucket("<BUCKET_NAME>.appspot.com")
        .build();
    FirebaseApp.initializeApp(options);

    Bucket bucket = StorageClient.getInstance().bucket();

    // 'bucket' is an object defined in the google-cloud-storage Java library.
    // See https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket
    // for more details.

### Python

    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import storage

    cred = credentials.Certificate('path/to/serviceAccountKey.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'PROJECT_ID.firebasestorage.app'
    })

    bucket = storage.bucket()

    # 'bucket' is an object defined in the google-cloud-storage Python library.
    # See https://googlecloudplatform.github.io/google-cloud-python/latest/storage/buckets.html
    # for more details.

### Go

    import (
    	"context"
    	"log"

    	firebase "firebase.google.com/go/v4"
    	"firebase.google.com/go/v4/auth"
    	"google.golang.org/api/option"
    )

    config := &firebase.Config{
    	StorageBucket: "<BUCKET_NAME>.appspot.com",
    }
    opt := option.WithCredentialsFile("path/to/serviceAccountKey.json")
    app, err := firebase.NewApp(context.Background(), config, opt)
    if err != nil {
    	log.Fatalln(err)
    }

    client, err := app.Storage(context.Background())
    if err != nil {
    	log.Fatalln(err)
    }

    bucket, err := client.DefaultBucket()
    if err != nil {
    	log.Fatalln(err)
    }
    // 'bucket' is an object defined in the cloud.google.com/go/storage package.
    // See https://godoc.org/cloud.google.com/go/storage#BucketHandle
    // for more details.https://github.com/firebase/firebase-admin-go/blob/4f7026f0837678ceb33ab2d2c145a0d18d9952fd/snippets/storage.go#L31-L51

You can use the bucket references returned by the Admin SDK in conjunction with
the official
[Google Cloud Storage client libraries](https://cloud.google.com/storage/docs/reference/libraries)
to upload, download, and modify content in the buckets associated with your
Firebase projects. Note that you do not have to authenticate
Google Cloud Storage libraries when using the Firebase Admin SDK. The bucket
references returned by the Admin SDK are already authenticated with the
credentials used to initialize your Firebase app.

## Use custom buckets

If you want to use a Cloud Storage bucket other than the default bucket
described earlier in this guide, or use multiple Cloud Storage buckets in
a single app, you can retrieve a reference to a custom bucket:

### Node.js

    const bucket = getStorage().bucket('my-custom-bucket');

### Java

    Bucket bucket = StorageClient.getInstance().bucket("my-custom-bucket");

### Python

    bucket = storage.bucket('my-custom-bucket')

### Go

     bucket, err := client.Bucket("my-custom-bucket")https://github.com/firebase/firebase-admin-go/blob/4f7026f0837678ceb33ab2d2c145a0d18d9952fd/snippets/storage.go#L64-L64

## Use a custom Firebase app

If you are building a more complicated application that interacts with
[multiple Firebase apps](https://firebase.google.com/docs/admin/setup#initialize-multiple-apps), you can
access the Cloud Storage buckets associated with a specific Firebase app
as follows:

### Node.js

    const bucket = getStorage(customApp).bucket();

### Java

    Bucket bucket = StorageClient.getInstance(customApp).bucket();

### Python

    bucket = storage.bucket(app=custom_app)

### Go

    otherClient, err := otherApp.Storage(context.Background())
    bucket, err := otherClient.Bucket("other-app-bucket")

## Get a shareable download URL

You can use the Admin SDK to generate a non-expiring download URL for
files stored in your buckets. Anyone with this URL can permanently
access the file.

### Node.js

    const { getStorage, getDownloadURL } = require('firebase-admin/storage');

    const fileRef = getStorage().bucket('my-bucket').file('my-file');
    const downloadURL= await getDownloadURL(fileRef);

## Google Cloud Storage client libraries

The Firebase Admin SDKs depend on the
[Google Cloud Storage client libraries](https://cloud.google.com/storage/docs/reference/libraries)
to provide Cloud Storage access. The bucket references returned by the
Admin SDK are objects defined in these libraries. Refer to the documentation and
API references of the Google Cloud Storage client libraries to learn how to
use the returned bucket references in use cases like file
[upload](https://cloud.google.com/storage/docs/uploading-objects) and
[download](https://cloud.google.com/storage/docs/downloading-objects).