# Source: https://firebase.google.com/docs/firestore/enterprise/quickstart-server.md.txt

> [!WARNING]
> **Preview:** **Firestore in Native mode (with Pipeline operations) for Enterprise
> edition** is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific
> Terms](https://cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage
> descriptions](https://cloud.google.com/products#product-launch-stages).

This quickstart shows you how to set up Cloud Firestore, add data, then use
either Core operations or Pipeline operations to query the data you
just added in the Firebase console using server client libraries for
Java, Node.js, and Python.

Use these client libraries to set up privileged server environments with full
access to your database..

> [!NOTE]
> **Note:** Before getting started with these features, make sure you're familiar with the [differences between Core and Pipeline operations](https://firebase.google.com/docs/firestore/enterprise/pipelines-overview?db=firestore-docs#features-of-firestore-pipeline-operations).

## Create a Cloud Firestore database

1. If you haven't already, create a Firebase project: In the
   [Firebase console](https://console.firebase.google.com/), click **Add project** ,
   then follow the on-screen instructions to create a Firebase project or to
   add Firebase services to an existing Google Cloud project.

2. Open your project in the Firebase console. In the left panel, expand
   **Build** and then select
   [**Firestore database**](https://console.firebase.google.com/project/_/firestore/).

3. Click **Create database**.

4. Select **Enterprise** for the database mode.

5. Select **Firestore in Native Mode** for the operation mode, which supports
   Core and Pipeline operations.

   > [!NOTE]
   > **Note:** You can create a database in either Native mode or MongoDB compatibility mode. For more information about MongoDB compatibility mode, see the [quickstart for creating MongoDB compatible databases](https://firebase.google.com/docs/firestore/enterprise/create-and-query-database).

6. Select a [location](https://firebase.google.com/docs/firestore/pipelines/locations#types) for your database.

7. Select a starting mode for your Cloud Firestore Security Rules:

   Test mode

   :   Good for getting started with the mobile and web client libraries,
       but allows anyone to read and overwrite your data. After testing, **make
       sure to review the [Secure your data](https://firebase.google.com/docs/firestore/enterprise/quickstart-server#secure_your_data) section.**

   :   To get started with the web, Apple platforms, or Android SDK, select test
       mode.

   Production mode

   :   Denies all reads and writes from mobile and web clients.
       Your authenticated application servers (Node.js, Python, Java) can still
       access your database.

   Your initial set of Cloud Firestore Security Rules will apply to your default
   Cloud Firestore database. If you create multiple databases for your
   project, you can deploy Cloud Firestore Security Rules for each database.
8. Click **Create**.

> [!NOTE]
> **Cloud Firestore and App Engine:** With support for multiple databases, you can use both Cloud Firestore and Datastore in the same project. If you use App Engine, note that only the `(default)` database in standard mode with Datastore or Firestore Native APIs can be used with App Engine.

When you enable Cloud Firestore, it also enables the API in the
[Cloud API Manager](https://console.cloud.google.com/projectselector/apis/api/firestore.googleapis.com/overview).

## Set up your development environment

Add the required dependencies and client libraries to your app.

##### Node.js

1. Add the Firebase Admin SDK to your app:

   ```javascript
   npm install firebase-admin --save
   ```
2. Follow the instructions below to initialize Cloud Firestore with the proper credentials in your environment.

##### Python

1. Add the Firebase Admin SDK to your Python app:

   ```python
   pip install --upgrade firebase-admin
   ```
2. Follow the instructions below to initialize Cloud Firestore with the proper credentials in your environment.

##### Java

1. Add the Firebase Admin SDK to your app:
   - **Using Gradle:**

     ```java
     implementation 'com.google.firebase:firebase-admin:9.8.0'
     ```
   - **Using Maven:**

     ```java
     <dependency>
       <groupId>com.google.firebase</groupId>
       <artifactId>firebase-admin</artifactId>
       <version>9.8.0</version>
     </dependency>
          
     ```
2. Follow the instructions below to initialize Cloud Firestore with the proper credentials in your environment.

## Initialize Cloud Firestore

Initialize an instance of Cloud Firestore:

##### Node.js

The Cloud Firestore SDK is initialized in different ways depending on your environment. Below are the most common methods. For a complete reference, see [Initialize
the Admin SDK](https://firebase.google.com/docs/admin/setup#initialize-sdk).

- **Initialize on Cloud Functions**

  ```javascript
  const { initializeApp, applicationDefault, cert } = require('firebase-admin/app');
  const { getFirestore, Timestamp, FieldValue, Filter } = require('firebase-admin/firestore');
  ```

  ```javascript
  initializeApp();

  const db = getFirestore();
  ```
- **Initialize on Google Cloud**

  ```javascript
  const { initializeApp, applicationDefault, cert } = require('firebase-admin/app');
  const { getFirestore, Timestamp, FieldValue, Filter } = require('firebase-admin/firestore');
  ```

  ```javascript
  initializeApp({
    credential: applicationDefault()
  });

  const db = getFirestore();
  ```
- **Initialize on your own server**


  To use the Firebase Admin SDK on your own server (or any other Node.js environment),
  use a [service account](https://cloud.google.com/compute/docs/authentication).

  Go to [**IAM \& admin \> Service accounts**](https://console.cloud.google.com/iam-admin/serviceaccounts) in the Google Cloud console. Generate a new private key and save the JSON file. Then use the file to initialize the SDK:

  ```javascript
  const { initializeApp, applicationDefault, cert } = require('firebase-admin/app');
  const { getFirestore, Timestamp, FieldValue, Filter } = require('firebase-admin/firestore');
  ```

  ```javascript
  const serviceAccount = require('./path/to/serviceAccountKey.json');

  initializeApp({
    credential: cert(serviceAccount)
  });

  const db = getFirestore();
  ```

##### Python

The Cloud Firestore SDK is initialized in different ways depending on your environment. Below are the most common methods. For a complete reference, see [Initialize
the Admin SDK](https://firebase.google.com/docs/admin/setup#initialize-sdk).
- **Initialize on Google Cloud**

  ```python
  import firebase_admin
  from firebase_admin import firestore

  # Application Default credentials are automatically created.
  app = firebase_admin.initialize_app()
  db = firestore.client()
  ```

  An existing application default credential can also be used to initialize the SDK.

  ```python
  import firebase_admin
  from firebase_admin import credentials
  from firebase_admin import firestore

  # Use the application default credentials.
  cred = credentials.ApplicationDefault()

  firebase_admin.initialize_app(cred)
  db = firestore.client()
  ```
- **Initialize on your own server**


  To use the Firebase Admin SDK on your own server, use a
  [service account](https://cloud.google.com/compute/docs/authentication).

  Go to
  [**IAM \& admin \> Service accounts**](https://console.cloud.google.com/iam-admin/serviceaccounts)
  in the Google Cloud console. Generate a new private key and save the JSON
  file. Then use the file to initialize the SDK:

  ```python
  import firebase_admin
  from firebase_admin import credentials
  from firebase_admin import firestore

  # Use a service account.
  cred = credentials.Certificate('path/to/serviceAccount.json')

  app = firebase_admin.initialize_app(cred)

  db = firestore.client()
  ```

##### Java

The Cloud Firestore SDK is initialized in different ways depending on your environment. Below are the most common methods. For a complete reference, see [Initialize
the Admin SDK](https://firebase.google.com/docs/admin/setup#initialize-sdk).
- **Initialize on Google Cloud**

  ```java
  import com.google.auth.oauth2.GoogleCredentials;
  import com.google.cloud.firestore.Firestore;

  import com.google.firebase.FirebaseApp;
  import com.google.firebase.FirebaseOptions;

  // Use the application default credentials
  GoogleCredentials credentials = GoogleCredentials.getApplicationDefault();
  FirebaseOptions options = new FirebaseOptions.Builder()
      .setCredentials(credentials)
      .setProjectId(projectId)
      .build();
  FirebaseApp.initializeApp(options);

  Firestore db = FirestoreClient.getFirestore();
  ```
- **Initialize on your own server**


  To use the Firebase Admin SDK on your own server, use a
  [service account](https://cloud.google.com/compute/docs/authentication).

  Go to
  [**IAM \& admin \> Service accounts**](https://console.cloud.google.com/iam-admin/serviceaccounts)
  in the Google Cloud console. Generate a new private key and save the JSON
  file. Then use the file to initialize the SDK:

  ```java
  import com.google.auth.oauth2.GoogleCredentials;
  import com.google.cloud.firestore.Firestore;

  import com.google.firebase.FirebaseApp;
  import com.google.firebase.FirebaseOptions;

  // Use a service account
  InputStream serviceAccount = new FileInputStream("path/to/serviceAccount.json");
  GoogleCredentials credentials = GoogleCredentials.fromStream(serviceAccount);
  FirebaseOptions options = new FirebaseOptions.Builder()
      .setCredentials(credentials)
      .build();
  FirebaseApp.initializeApp(options);

  Firestore db = FirestoreClient.getFirestore();
  ```

## Add data using Core operations

In order to explore Core operations and Pipeline operations for querying data,
add data to your database using Core operations.

Cloud Firestore stores data in Documents, which are stored in
Collections. Cloud Firestore creates collections and documents implicitly
the first time you add data to the document. You don't need to explicitly
create collections or documents.

Create a new collection and a document using the following example code.

##### Node.js

    const docRef = db.collection('users').doc('alovelace');

    await docRef.set({
      first: 'Ada',
      last: 'Lovelace',
      born: 1815
    });https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/firestore/main/index.js#L86-L92

##### Java

    DocumentReference docRef = db.collection("users").document("alovelace");
    // Add document data  with id "alovelace" using a hashmap
    Map<String, Object> data = new HashMap<>();
    data.put("first", "Ada");
    data.put("last", "Lovelace");
    data.put("born", 1815);
    //asynchronously write data
    ApiFuture<WriteResult> result = docRef.set(data);
    // ...
    // result.get() blocks on response
    System.out.println("Update time : " + result.get().getUpdateTime());https://github.com/googleapis/java-firestore/blob/2be59896fef7a7bb458cfaf06344654e82acc74c/samples/snippets/src/main/java/com/example/firestore/Quickstart.java#L84-L94

##### Python

    doc_ref = db.collection("users").document("alovelace")
    doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-client/snippets.py#L42-L43

## Read data using Core operations

Use the data viewer in the
[Firebase console](https://console.firebase.google.com/project/_/firestore/data)
to quickly verify that you've added data to Cloud Firestore.

You can also use the "get" method to retrieve the entire collection.

##### Node.js

    const snapshot = await db.collection('users').get();
    snapshot.forEach((doc) => {
      console.log(doc.id, '=>', doc.data());
    });https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/firestore/main/index.js#L119-L122

##### Python

```python
users_ref = db.collection("users")
docs = users_ref.stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")
```

##### Java

    // asynchronously retrieve all users
    ApiFuture<QuerySnapshot> query = db.collection("users").get();
    // ...
    // query.get() blocks on response
    QuerySnapshot querySnapshot = query.get();
    List<QueryDocumentSnapshot> documents = querySnapshot.getDocuments();
    for (QueryDocumentSnapshot document : documents) {
      System.out.println("User: " + document.getId());
      System.out.println("First: " + document.getString("first"));
      if (document.contains("middle")) {
        System.out.println("Middle: " + document.getString("middle"));
      }
      System.out.println("Last: " + document.getString("last"));
      System.out.println("Born: " + document.getLong("born"));
    }https://github.com/googleapis/java-firestore/blob/2be59896fef7a7bb458cfaf06344654e82acc74c/samples/snippets/src/main/java/com/example/firestore/Quickstart.java#L152-L166

## Read data using Pipeline operations

Now you can compare the Pipeline query experience with the Core query
experience.

##### Node.js

```javascript
const readDataPipeline = db.pipeline()
  .collection("users");

// Execute the pipeline and handle the result
try {
  const querySnapshot = await readDataPipeline.execute();
  querySnapshot.results.forEach((result) => {
    console.log(`${result.id} => ${result.data()}`);
  });
} catch (error) {
    console.error("Error getting documents: ", error);
}
```

##### Python

```python
pipeline = client.pipeline().collection("users")
for result in pipeline.execute():
    print(f"{result.id} => {result.data()}")
```

##### Java

```java
Pipeline pipeline = firestore.pipeline().collection("users");
ApiFuture<Pipeline.Snapshot> future = pipeline.execute();
for (com.google.cloud.firestore.PipelineResult result : future.get().getResults()) {
  System.out.println(result.getId() + " => " + result.getData());
}
// or, asynchronously
pipeline.execute(
    new ApiStreamObserver<com.google.cloud.firestore.PipelineResult>() {
      @Override
      public void onNext(com.google.cloud.firestore.PipelineResult result) {
        System.out.println(result.getId() + " => " + result.getData());
      }

      @Override
      public void onError(Throwable t) {
        System.err.println(t);
      }

      @Override
      public void onCompleted() {
        System.out.println("done");
      }
    });
```

## Next steps

Deepen your knowledge of Core and Pipeline operations with the following topics:

- Make sure you're familiar with the [differences between the Core and Pipeline operations](https://firebase.google.com/docs/firestore/enterprise/pipelines-overview?db=firestore-docs#features-of-firestore-pipeline-operations)
- Learn more about querying with [Core operations](https://firebase.google.com/docs/firestore/enterprise/get-data-core)
- Learn more about querying with [Pipeline operations](https://firebase.google.com/docs/firestore/pipelines/get-started-with-pipelines).