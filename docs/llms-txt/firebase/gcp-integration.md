# Source: https://firebase.google.com/docs/storage/gcp-integration.md.txt

<br />

| **If you have an`*.appspot.com`default bucket,** your Firebase project must be upgraded to the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing)by**as early as February 02, 2026** to maintain access to your default bucket.[Learn more.](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024)
Cloud Storage for Firebaseis tightly integrated with[Google Cloud](https://cloud.google.com). TheFirebaseSDKs forCloud Storagestore files directly in[Google Cloud Storagebuckets](https://cloud.google.com/storage/docs/buckets), and as your app grows, you can integrate otherGoogle Cloudservices, such as managed compute likeApp Engineor Cloud Functions, or machine learning APIs like Cloud Vision or Google Translate.

A Firebase project is actually just aGoogle Cloudproject that has*additional Firebase-specific* configurations and services enabled for it. This means that everyCloud Storagebucket that you use withCloud Storage for Firebaseis accessible inGoogle Cloud(including its console and its APIs).

Integrating withGoogle Cloud, including importing existingCloud Storagebuckets, requires a Firebase project on the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing).
| **Important:** Startingas early as February 02, 2026, the[Blaze pricing plan will be*required* to useCloud Storage](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024), even default buckets.

## Considerations for service accounts

Firebase usesGoogle Cloudservice accounts to operate and manage services without sharing user credentials. When you create a Firebase project that usesCloud Storage, you might notice that a corresponding service account is already available in your project:service-<var translate="no">PROJECT_NUMBER</var>@gcp-sa-firebasestorage.iam.gserviceaccount.com. For more information, see[Firebase service accounts overview](https://firebase.google.com/support/guides/service-accounts).
| **Note:** If yourCloud Storagebuckets are managed under the service account named`firebase-storage@systeem.gserviceaccount.com`, refer to[the Firebase support FAQ topic](https://firebase.google.com/support/faq#cloud-storage)for special instructions on service account setup.

## Google Cloud Storage

You can use the[Google Cloud StorageAPIs](https://cloud.google.com/storage/docs/reference/libraries)to access files uploaded via theFirebaseSDKs forCloud Storage, especially to perform more complex operations, such as copying or moving a file, or listing all the files available at a reference.

It's important to note that these requests useGoogle Cloud Storage[access control options](https://cloud.google.com/storage/docs/access-control/), rather thanFirebase AuthenticationandCloud StorageSecurity Rules.

### APIs

In addition to theFirebaseSDKs forCloud Storage, there are a number of other ways to access data stored in yourCloud Storagebucket, depending on what you want to do. If you're accessing data on a server, we offer server side libraries, as well as a`JSON`and S3 compatible`XML`RESTful API, or if you need to script changes or perform other administrative tasks, we've got a command line tool that will come in handy.

#### Google Cloudserver SDKs

Google Cloudoffers high-quality server SDKs for a number of cloud products, includingCloud Storage. These libraries are available in[Node.js](https://github.com/GoogleCloudPlatform/google-cloud-node#google-cloud-storage),[Java](https://github.com/GoogleCloudPlatform/google-cloud-java#google-cloud-storage),[go](https://github.com/GoogleCloudPlatform/google-cloud-go#cloud-storage-),[Python](https://github.com/GoogleCloudPlatform/google-cloud-python#google-cloud-storage),[PHP](https://github.com/GoogleCloudPlatform/google-cloud-php#google-cloud-storage), and[Ruby](https://github.com/GoogleCloudPlatform/google-cloud-ruby#storage).

For more information, including installation instructions, authentication, and troubleshooting, consult the platform-specific documentation linked above.

Example usage for theGoogle Cloud StorageSDK is shown below:  

### Node.js

```javascript
    // Require gcloud
    var gcloud = require('google-cloud');

    // Enable Cloud Storage
    var gcs = gcloud.storage({
      projectId: 'grape-spaceship-123',
      keyFilename: '/path/to/keyfile.json'
    });

    // Reference an existing bucket.
    var bucket = gcs.bucket('my-existing-bucket');

    // Upload a local file to a new file to be created in your bucket.
    bucket.upload('/photos/zoo/zebra.jpg', function(err, file) {
      if (!err) {
        // "zebra.jpg" is now in your bucket.
      }
    });

    // Download a file from your bucket.
    bucket.file('giraffe.jpg').download({
      destination: '/photos/zoo/giraffe.jpg'
    }, function(err) {});
    
```

### Java

```java
    // Enable Cloud Storage
    Storage storage = StorageOptions.builder()
      .authCredentials(AuthCredentials.createForJson(new FileInputStream("/path/to/my/key.json"))
      .build()
      .service();

    // Upload a local file to a new file to be created in your bucket.
    InputStream uploadContent = ...
    BlobId blobId = BlobId.of("my-existing-bucket", "zebra.jpg");
    BlobInfo blobInfo = BlobInfo.builder(blobId).contentType("text/plain").build();
    Blob zebraBlob = storage.create(blobInfo, content);

    // Download a file from your bucket.
    Blob giraffeBlob = storage.get("my-existing-bucket", "giraffe.jpg", null);
    InputStream downloadContent = giraffeBlob.getInputStream();
    
```

### Go

```go
    // Enable Cloud Storage
    client, err := storage.NewClient(ctx, option.WithServiceAccountFile("path/to/keyfile.json"))
    if err != nil {
        log.Fatal(err)
    }

    // Download a file from your bucket.
    rc, err := client.Bucket("my-existing-bucket").Object("giraffe.jpg").NewReader(ctx)
    if err != nil {
        log.Fatal(err)
    }
    defer rc.Close()
    body, err := ioutil.ReadAll(rc)
    if err != nil {
        log.Fatal(err)
    }
    
```

### Python

```python
    # Import gcloud
    from google.cloud import storage

    # Enable Cloud Storage
    client = storage.Client()

    # Reference an existing bucket.
    bucket = client.get_bucket('my-existing-bucket')

    # Upload a local file to a new file to be created in your bucket.
    zebraBlob = bucket.get_blob('zebra.jpg')
    zebraBlob.upload_from_filename(filename='/photos/zoo/zebra.jpg')

    # Download a file from your bucket.
    giraffeBlob = bucket.get_blob('giraffe.jpg')
    giraffeBlob.download_as_string()
    
```

### PHP

```php
    // Require gcloud
    require 'vendor/autoload.php';
    use Google\Cloud\Storage\StorageClient;

    // Enable Cloud Storage
    $storage = new StorageClient([
        'projectId' => 'grape-spaceship-123'
    ]);

    // Reference an existing bucket.
    $bucket = $storage->bucket('my-existing-bucket');

    // Upload a file to the bucket.
    $bucket->upload(
        fopen('/photos/zoo/zebra.jpg', 'r')
    );

    // Download a file from your bucket.
    $object = $bucket->object('giraffe.jpg');
    $object->downloadToFile('/photos/zoo/giraffe.jpg');
    
```

### Ruby

```ruby
    # Require gcloud
    require "google/cloud"

    # Enable Cloud Storage
    gcloud = Google::Cloud.new "grape-spaceship-123", "/path/to/keyfile.json"
    storage = gcloud.storage

    # Reference an existing bucket.
    bucket = storage.bucket "my-existing-bucket"

    # Upload a file to the bucket.
    bucket.create_file "/photos/zoo/zebra.jpg", "zebra.jpg"

    # Download a file from your bucket.
    file = bucket.file "giraffe.jpg"
    file.download "/photos/zoo/#{file.name}"
    
```

#### REST API

If you're using a language without a client library, want to do something that the client libraries don't do, or just have a favorite HTTP client that you'd prefer to use,Google Cloud Storageoffers APIs for both[JSON](https://cloud.google.com/storage/docs/json_api/)and[XML](https://cloud.google.com/storage/docs/xml-api/overview).

In addition to these storage data access APIs, to manage Cloud Storage buckets for use in Firebase projects, you can use the[Cloud Storage for Firebase API](https://firebase.google.com/docs/reference/rest/storage/rest).

#### `gsutil`

[`gsutil`](https://cloud.google.com/storage/docs/gsutil)is a command line tool that gives you direct access toCloud Storage. You can use`gsutil`to do a wide range of bucket and object management tasks, including:

- Uploading, downloading, and deleting objects.
- Listing buckets and objects.
- Moving, copying, and renaming objects.
- Editing object and bucket ACLs.

`gsutil`allow for other advanced operations, such as moving files from one directory to another, or deleting all the files below a certain location.

Moving all the files from one reference to another is as easy as:  

```text
gsutil mv gs://bucket/old/reference gs://bucket/new/reference
```

<br />

Batch deleting all the files below a reference is similarly intuitive:  

```scdoc
# Delete all files under a path
gsutil rm -r gs://bucket/reference/to/delete

# Delete all the files in a bucket but not the bucket
gsutil rm -r gs://bucket/**

# Delete all the files AND the bucket
# Removing the default bucket will break the Firebase SDKs for Cloud Storage and
is strongly discouraged
gsutil rm -r gs://bucket
```

<br />

### Request Rates

Google Cloud Storageis a highly scalable service that uses auto-scaling technology to achieve very high request rates.

Google Cloud Storageis a multi-tenant service, meaning that users share the same set of underlying resources. In order to make the best use of these shared resources, buckets have an initial IO capacity.

As you plan to integrateCloud Storage for Firebaseinto your app, think about a minimum request rate your app needs for good performance, and about making requests efficiently. Review guidelines about[request rates](https://cloud.google.com/storage/docs/request-rate), and especially[ramping up request rates](https://cloud.google.com/storage/docs/request-rate#ramp-up).

### Object Versioning

Have you ever deleted something by accident and not had a backup?Google Cloud Storagesupports[Object Versioning](https://cloud.google.com/storage/docs/object-versioning), which provides an automatic way to back your data up, and restore from those backups. You can enable Object Versioning using the`gsutil``versioning set`command:  

```text
gsutil versioning set on gs://<your-cloud-storage-bucket>
```

Cloud Storagealways picks up the most recent version, so if you want to restore an object, you need to use one of the other APIs or tools above to set the desired object as the most recent.

### Object Lifecycle Management

Having the ability to automatically archive or delete stale files is a useful feature for many applications. Luckily,Google Cloud Storageprovides[Object Lifecycle Management](https://cloud.google.com/storage/docs/lifecycle), which allows you to delete or archive objects after a certain amount of time.

Consider a photo sharing application that you want all photos to be deleted within one day. You can set up an object lifecycle policy as follows:  

```carbon
// lifecycle.json
{
  "lifecycle": {
    "rule":
    [
      {
        "action": {"type": "Delete"},
        "condition": {"age": 1}
      }
    ]
  }
}
```

And deploy it using the`gsutil``lifecycle set`command:  

```text
gsutil lifecycle set lifecycle.json gs://<your-cloud-storage-bucket>
```

Note that this applies to all files in the bucket, so if you're storing important user backups you want to store for a long time along side photos that you want to delete daily, you might want to use two separate buckets or perform deletions manually with`gsutil`or your own server.

## Google Cloud Functions (Beta)

[Google Cloud Functions](https://cloud.google.com/functions)is a lightweight, event-based, asynchronous compute solution that allows you to create small, single-purpose functions that respond to events without the need to manage a server or a runtime environment. These functions can be used for transcoding video, classifying images using machine learning, or syncing metadata with theFirebase Realtime Database. With even less overhead thanApp Engine, Cloud Functions is the fastest way to react to changes inCloud Storage.

## Google Cloud Vision API

The[Google Cloud Vision API](https://cloud.google.com/vision)enables developers to understand the content of an image by encapsulating powerful machine learning models in an easy to use API. It quickly classifies images into thousands of categories, detects individual objects and faces within images, finds and reads printed words contained within images, identifies offensive content, and even provides image sentiment analysis.

## Google Cloud Speech API

Similar to the Vision API, the[Google Cloud Speech API](https://cloud.google.com/speech)enables developers to extract text from an audio file stored inCloud Storage. The API recognizes over 80 languages and variants, to support your global user base. When combined with the[Google Cloud Natural Language API](https://cloud.google.com/natural-language/), developers can both extract the raw text and infer meaning about that text. And if a global audience is required, couple this with the[Google Translate API](https://cloud.google.com/translate/)to translate the text to 90+ languages.

## GoogleApp Engine

| This section aboutGoogleApp Engineis applicable only if youcreated your defaultCloud Storagebucket in your Firebase project*before* October 30, 2024and the bucket has a name format of<var translate="no">PROJECT_ID</var>`.appspot.com`.

GoogleApp Engineis a "Platform as a Service" that automatically scales backend logic in response to the amount of traffic it receives. Just upload your backend code and Google will manage your app's availability; there are no servers for you to provision or maintain.App Engineis a fast and straightforward way to add additional processing power or trusted execution to your Firebase application.

If you have a defaultCloud Storagebucket with the name format<var translate="no">PROJECT_ID</var>`.appspot.com`, then it's automatically shared with aApp Engineapp in your project. This means that if you build anApp Engineapp, you can use the built-inApp EngineAPIs to share data between that bucket andApp Engine. This is useful for performing audio encoding, video transcoding, and image transformations, as well as other computation intensive background processing.

The Java, Python, and Go[standard environments](https://cloud.google.com/appengine/docs/about-the-standard-environment)forApp Engineinclude theApp EngineImages API ([Java](https://cloud.google.com/appengine/docs/java/images/)\|[Python](https://cloud.google.com/appengine/docs/python/images/)\|[Go](https://cloud.google.com/appengine/docs/go/images/)), which can resize, rotate, flip, and crop an image, as well as return an image serving URL which allows for client side transformations, similar to Cloudinary and Imgix.

When importing an existingGoogle Cloudproject into Firebase, if you want to make any existingApp Engineobjects available in Firebase, you'll need to set the default access control on your objects to allow Firebase to access them by running the following command using[`gsutil`](https://firebase.google.com/docs/storage/gcp-integration#gsutil):  

```transact-sql
gsutil -m acl ch -r -u service-PROJECT_NUMBER@gcp-sa-firebasestorage.iam.gserviceaccount.com gs://BUCKET_NAME
```

### Considerations forFirebase Security RulesandApp Enginefiles

If you have a defaultCloud Storagebucket with a name format of`*.appspot.com`, then your project also has anApp Engineapp that shares that bucket.

If you configure yourFirebase Security Rulesfor[public (unauthenticated) access](https://firebase.google.com/docs/storage/security/rules-conditions#public), you will make newly uploadedApp Enginefiles publicly accessible, as well.

### Known issues forCloud StorageandApp Engine

There are two known cases where you can't import yourApp Engineapp:

1. The project contains a formerApp EngineDatastoreMaster/Slave app.
2. The project has a domain prefixed project ID, for example:`domain.com:project-1234`.

In either of these cases, the project won't supportCloud Storage for Firebase, and you should create a new Firebase project in order to useCloud Storage.[Contact support](https://firebase.google.com/support/contact/troubleshooting)so that we can help you out.