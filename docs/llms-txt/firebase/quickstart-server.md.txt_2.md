# Source: https://firebase.google.com/docs/firestore/quickstart-server.md.txt

<br />

This quickstart shows you how to set up Firestore Enterprise edition, add data,
then view the data you just added in the Firebase console using server client
libraries for C#, Go, Java, Node.js, PHP, Python, and Ruby.

Use these client libraries to set up privileged server environments with full
access to your database.

## Create a Cloud Firestore database

1. If you haven't already, create a Firebase project: In the
   [Firebase console](https://console.firebase.google.com/), click **Add project** ,
   then follow the on-screen instructions to create a Firebase project or to
   add Firebase services to an existing Google Cloud project.

2. Open your project in the Firebase console. In the left panel, expand
   **Build** and then select
   [**Firestore database**](https://console.firebase.google.com/project/_/firestore/).

3. Click **Create database**.

4. Select a [location](https://firebase.google.com/docs/firestore/locations#types) for your database.

   If you aren't able to select a location, then your project's
   ["location for default Google Cloud resources"](https://firebase.google.com/docs/firestore/locations#default-cloud-location)
   has already been set. Some of your project's resources (like the default
   Cloud Firestore instance) share a common location dependency, and
   their location can be set either during project creation or when setting up
   another service that shares this location dependency.
5. Select a starting mode for your Cloud Firestore Security Rules:

   Test mode

   :   Good for getting started with the mobile and web client libraries,
       but allows anyone to read and overwrite your data. After testing, **make
       sure to review the [Secure your data](https://firebase.google.com/docs/firestore/quickstart-server#secure_your_data) section.**

   :   To get started with the web, Apple platforms, or Android SDK, select test mode.

   Production mode

   :   Denies all reads and writes from mobile and web clients.
       Your authenticated application servers (C#, Go, Java, Node.js, PHP,
       Python, or Ruby) can still access your database.

   :   To get started with the C#, Go, Java, Node.js, PHP, Python, or Ruby
       server client library, select production mode.

   Your initial set of Cloud Firestore Security Rules will apply to your default
   Cloud Firestore database. If you create multiple databases for your
   project, you can deploy Cloud Firestore Security Rules for each database.
6. Click **Create**.

> [!NOTE]
> **Cloud Firestore and App Engine:** With support for multiple databases, you can use both Cloud Firestore and Datastore in the same project. If you use App Engine, note that only the `(default)` database in standard mode with Datastore or Firestore Native APIs can be used with App Engine.

When you enable Cloud Firestore, it also enables the API in the
[Cloud API Manager](https://console.cloud.google.com/projectselector/apis/api/firestore.googleapis.com/overview).

## Set up your development environment

Add the required dependencies and client libraries to your app.

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

##### Python

1. Add the Firebase Admin SDK to your Python app:

   ```python
   pip install --upgrade firebase-admin
   ```
2. Follow the instructions below to initialize Cloud Firestore with the proper credentials in your environment.

##### Node.js

1. Add the Firebase Admin SDK to your app:

   ```javascript
   npm install firebase-admin --save
   ```
2. Follow the instructions below to initialize Cloud Firestore with the proper credentials in your environment.

##### Go

1. Add the Firebase Admin SDK to your Go app:

   ```go
   go get firebase.google.com/go
   ```
2. Follow the instructions below to initialize Cloud Firestore with the proper credentials in your environment.

##### PHP

1. The Cloud Firestore server client libraries (Java, Node.js, Python, Go, PHP, C#, and Ruby) use [Google Application Default Credentials](https://cloud.google.com/docs/authentication/production) for authentication.
   - To authenticate from your development environment, set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to a JSON service account key file. You can create a key file on the [API Console Credentials page](https://console.cloud.google.com/projectselector/apis/credentials).

     ```php
     export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/keyfile.json"
     ```
   - In your production environment, you do not need to authenticate if you run your application on App Engine or Compute Engine, using the same project that you use for Cloud Firestore. Otherwise, [set up a service account](https://cloud.google.com/docs/authentication/getting-started).
2. Install and enable the [gRPC extension](https://docs.cloud.google.com/php/docs/reference/help/grpc) for PHP, which you will need to use the client library.
3. Add the Cloud Firestore PHP library to your app:

   ```php
   composer require google/cloud-firestore
   ```

##### Ruby

1. The Cloud Firestore server client libraries (Java, Node.js, Python, Go, PHP, C#, and Ruby) use [Google Application Default Credentials](https://cloud.google.com/docs/authentication/production) for authentication.
   - To authenticate from your development environment, set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to a JSON service account key file. You can create a key file on the [API Console Credentials page](https://console.cloud.google.com/projectselector/apis/credentials).

     ```ruby
     export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/keyfile.json"
     ```
   - In your production environment, you do not need to authenticate if you run your application on App Engine or Compute Engine, using the same project that you use for Cloud Firestore. Otherwise, [set up a service account](https://cloud.google.com/docs/authentication/getting-started).
2. Add the Cloud Firestore Ruby library to your app in your `Gemfile`:

   ```ruby
   gem "google-cloud-firestore"
   ```
3. Install dependencies from your `Gemfile` using:

   ```ruby
   bundle install
   ```

## (Optional) Prototype and test with Firebase Local Emulator Suite

For mobile developers, before talking about how your app writes to and reads
from Cloud Firestore, let's introduce a set of tools you can use to
prototype and test Cloud Firestore functionality:
Firebase Local Emulator Suite. If you're trying out different data models,
optimizing your security rules, or working to find the most cost-effective way
to interact with the back-end, being able to work locally without deploying
live services can be a great idea.

A Cloud Firestore emulator is part of the Local Emulator Suite, which
enables your app to interact with your emulated database content and config, as
well as optionally your emulated project resources (functions, other databases,
and security rules).

Using the Cloud Firestore emulator involves just a few steps:

1. Adding a line of code to your app's test config to connect to the emulator.
2. From the root of your local project directory, running `firebase emulators:start`.
3. Making calls from your app's prototype code using a Cloud Firestore platform SDK as usual.

A detailed [walkthrough involving Cloud Firestore and Cloud Functions](https://firebase.google.com/docs/emulator-suite/connect_and_prototype?database=Firestore) is available. You should also have a look at the [Local Emulator Suite introduction](https://firebase.google.com/docs/emulator-suite).

## Initialize Cloud Firestore

Initialize an instance of Cloud Firestore:

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

### Python

The Cloud Firestore SDK is initialized in different ways depending on your environment. Below are the most common methods. For a complete reference, see [Initialize
the Admin SDK](https://firebase.google.com/docs/admin/setup#initialize-sdk).
- **Initialize on Google Cloud**

  ```python
  import firebase_admin
  from firebase_admin import firestore_async

  # Application Default credentials are automatically created.
  app = firebase_admin.initialize_app()
  db = firestore_async.client()
  ```

  An existing application default credential can also be used to initialize the SDK.

  ```python
  import firebase_admin
  from firebase_admin import credentials
  from firebase_admin import firestore_async

  # Use the application default credentials.
  cred = credentials.ApplicationDefault()

  firebase_admin.initialize_app(cred)
  db = firestore_async.client()
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
  from firebase_admin import firestore_async

  # Use a service account.
  cred = credentials.Certificate('path/to/serviceAccount.json')

  app = firebase_admin.initialize_app(cred)

  db = firestore_async.client()
  ```

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

##### Go

The Cloud Firestore SDK is initialized in different ways depending on your environment. Below are the most common methods. For a complete reference, see [Initialize
the Admin SDK](https://firebase.google.com/docs/admin/setup#initialize-sdk).
- **Initialize on Google Cloud**

  ```go
  import (
    "log"

    firebase "firebase.google.com/go"
    "google.golang.org/api/option"
  )

  // Use the application default credentials
  ctx := context.Background()
  conf := &firebase.Config{ProjectID: projectID}
  app, err := firebase.NewApp(ctx, conf)
  if err != nil {
    log.Fatalln(err)
  }

  client, err := app.Firestore(ctx)
  if err != nil {
    log.Fatalln(err)
  }
  defer client.Close()
  ```
- **Initialize on your own server**


  To use the Firebase Admin SDK on your own server, use a
  [service account](https://cloud.google.com/compute/docs/authentication).

  Go to
  [**IAM \& admin \> Service accounts**](https://console.cloud.google.com/iam-admin/serviceaccounts)
  in the Google Cloud console. Generate a new private key and save the JSON
  file. Then use the file to initialize the SDK:

  ```go
  import (
    "log"

    firebase "firebase.google.com/go"
    "google.golang.org/api/option"
  )

  // Use a service account
  ctx := context.Background()
  sa := option.WithCredentialsFile("path/to/serviceAccount.json")
  app, err := firebase.NewApp(ctx, nil, sa)
  if err != nil {
    log.Fatalln(err)
  }

  client, err := app.Firestore(ctx)
  if err != nil {
    log.Fatalln(err)
  }
  defer client.Close()
  ```

##### PHP

### PHP


For more on installing and creating a Cloud Firestore client, refer to
[Cloud Firestore Client Libraries](https://firebase.google.com/firestore/docs/reference/libraries).

    use Google\Cloud\Firestore\FirestoreClient;

    /**
     * Initialize Cloud Firestore with default project ID.
     */
    function setup_client_create(string $projectId = null)
    {
        // Create the Cloud Firestore client
        if (empty($projectId)) {
            // The `projectId` parameter is optional and represents which project the
            // client will act on behalf of. If not supplied, the client falls back to
            // the default project inferred from the environment.
            $db = new FirestoreClient();
            printf('Created Cloud Firestore client with default project ID.' . PHP_EOL);
        } else {
            $db = new FirestoreClient([
                'projectId' => $projectId,
            ]);
            printf('Created Cloud Firestore client with project ID: %s' . PHP_EOL, $projectId);
        }
    }https://github.com/GoogleCloudPlatform/php-docs-samples/blob/57f7e42e9df09d95da84f23fe6688f51ab8aa0ef/firestore/src/setup_client_create.php#L27-L47

##### C#

### C#


For more on installing and creating a Cloud Firestore client, refer to
[Cloud Firestore Client Libraries](https://firebase.google.com/firestore/docs/reference/libraries).

    FirestoreDb db = FirestoreDb.Create(project);
    Console.WriteLine("Created Cloud Firestore client with project ID: {0}", project);https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/f0105e127957cddda7c57872b3c2b9a405b0a97d/firestore/api/Quickstart/Program.cs#L37-L38

##### Ruby

    require "google/cloud/firestore"

    # The `project_id` parameter is optional and represents which project the
    # client will act on behalf of. If not supplied, the client falls back to the
    # default project inferred from the environment.
    firestore = Google::Cloud::Firestore.new project_id: project_id

    puts "Created Cloud Firestore client with given project ID."https://github.com/googleapis/google-cloud-ruby/blob/56f30b3c8e79535bd66d78b7e43b0174b728d3f0/google-cloud-firestore/samples/quickstart.rb#L19-L26

## Add data

Cloud Firestore stores data in Documents, which are stored in Collections.
Cloud Firestore creates collections and documents implicitly
the first time you add data to the document. You don't need to explicitly
create collections or documents.

Create a new collection and a document using the following example code.

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

### Python

    doc_ref = db.collection("users").document("alovelace")
    await doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-async-client/snippets.py#L36-L37

##### Node.js

    const docRef = db.collection('users').doc('alovelace');

    await docRef.set({
      first: 'Ada',
      last: 'Lovelace',
      born: 1815
    });https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/firestore/main/index.js#L86-L92

##### Go

    _, _, err := client.Collection("users").Add(ctx, map[string]interface{}{
    	"first": "Ada",
    	"last":  "Lovelace",
    	"born":  1815,
    })
    if err != nil {
    	log.Fatalf("Failed adding alovelace: %v", err)
    }https://github.com/GoogleCloudPlatform/golang-samples/blob/323d864f13303fca135899042d1ecce6efd62722/firestore/firestore_quickstart/main.go#L58-L65

##### PHP

### PHP


For more on installing and creating a Cloud Firestore client, refer to
[Cloud Firestore Client Libraries](https://firebase.google.com/firestore/docs/reference/libraries).

    $docRef = $db->collection('samples/php/users')->document('alovelace');
    $docRef->set([
        'first' => 'Ada',
        'last' => 'Lovelace',
        'born' => 1815
    ]);
    printf('Added data to the lovelace document in the users collection.' . PHP_EOL);https://github.com/GoogleCloudPlatform/php-docs-samples/blob/57f7e42e9df09d95da84f23fe6688f51ab8aa0ef/firestore/src/setup_dataset.php#L40-L46

##### C#

    DocumentReference docRef = db.Collection("users").Document("alovelace");
    Dictionary<string, object> user = new Dictionary<string, object>
    {
        { "First", "Ada" },
        { "Last", "Lovelace" },
        { "Born", 1815 }
    };
    await docRef.SetAsync(user);https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/f0105e127957cddda7c57872b3c2b9a405b0a97d/firestore/api/Quickstart/Program.cs#L46-L53

##### Ruby

    doc_ref = firestore.doc "#{collection_path}/alovelace"

    doc_ref.set(
      {
        first: "Ada",
        last:  "Lovelace",
        born:  1815
      }
    )

    puts "Added data to the alovelace document in the users collection."https://github.com/googleapis/google-cloud-ruby/blob/56f30b3c8e79535bd66d78b7e43b0174b728d3f0/google-cloud-firestore/samples/quickstart.rb#L36-L46

Now add another document to the `users` collection. Notice that this document
includes a key-value pair (middle name) that does not appear in the first
document. Documents in a collection can contain different sets of information.

##### Java

    DocumentReference docRef = db.collection("users").document("aturing");
    // Add document data with an additional field ("middle")
    Map<String, Object> data = new HashMap<>();
    data.put("first", "Alan");
    data.put("middle", "Mathison");
    data.put("last", "Turing");
    data.put("born", 1912);

    ApiFuture<WriteResult> result = docRef.set(data);
    System.out.println("Update time : " + result.get().getUpdateTime());https://github.com/googleapis/java-firestore/blob/2be59896fef7a7bb458cfaf06344654e82acc74c/samples/snippets/src/main/java/com/example/firestore/Quickstart.java#L100-L109

##### Python

    doc_ref = db.collection("users").document("aturing")
    doc_ref.set({"first": "Alan", "middle": "Mathison", "last": "Turing", "born": 1912})https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-client/snippets.py#L50-L51

### Python

    doc_ref = db.collection("users").document("aturing")
    await doc_ref.set(
        {"first": "Alan", "middle": "Mathison", "last": "Turing", "born": 1912}
    )https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-async-client/snippets.py#L44-L47

##### Node.js

    const aTuringRef = db.collection('users').doc('aturing');

    await aTuringRef.set({
      'first': 'Alan',
      'middle': 'Mathison',
      'last': 'Turing',
      'born': 1912
    });https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/firestore/main/index.js#L96-L103

##### Go

    _, _, err = client.Collection("users").Add(ctx, map[string]interface{}{
    	"first":  "Alan",
    	"middle": "Mathison",
    	"last":   "Turing",
    	"born":   1912,
    })
    if err != nil {
    	log.Fatalf("Failed adding aturing: %v", err)
    }https://github.com/GoogleCloudPlatform/golang-samples/blob/323d864f13303fca135899042d1ecce6efd62722/firestore/firestore_quickstart/main.go#L69-L77

##### PHP

### PHP


For more on installing and creating a Cloud Firestore client, refer to
[Cloud Firestore Client Libraries](https://firebase.google.com/firestore/docs/reference/libraries).

    $docRef = $db->collection('samples/php/users')->document('aturing');
    $docRef->set([
        'first' => 'Alan',
        'middle' => 'Mathison',
        'last' => 'Turing',
        'born' => 1912
    ]);
    printf('Added data to the aturing document in the users collection.' . PHP_EOL);https://github.com/GoogleCloudPlatform/php-docs-samples/blob/57f7e42e9df09d95da84f23fe6688f51ab8aa0ef/firestore/src/setup_dataset.php#L49-L56

##### C#

    DocumentReference docRef = db.Collection("users").Document("aturing");
    Dictionary<string, object> user = new Dictionary<string, object>
    {
        { "First", "Alan" },
        { "Middle", "Mathison" },
        { "Last", "Turing" },
        { "Born", 1912 }
    };
    await docRef.SetAsync(user);https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/f0105e127957cddda7c57872b3c2b9a405b0a97d/firestore/api/Quickstart/Program.cs#L62-L70

##### Ruby

    doc_ref = firestore.doc "#{collection_path}/aturing"

    doc_ref.set(
      {
        first:  "Alan",
        middle: "Mathison",
        last:   "Turing",
        born:   1912
      }
    )

    puts "Added data to the aturing document in the users collection."https://github.com/googleapis/google-cloud-ruby/blob/56f30b3c8e79535bd66d78b7e43b0174b728d3f0/google-cloud-firestore/samples/quickstart.rb#L56-L67

## Read data

Use the data viewer in the
[Firebase console](https://console.firebase.google.com/project/_/firestore/data)
to quickly verify that you've added data to Cloud Firestore.

You can also use the "get" method to retrieve the entire collection.

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

##### Python

```python
users_ref = db.collection("users")
docs = users_ref.stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")
```

### Python

    users_ref = db.collection("users")
    docs = users_ref.stream()

    async for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-async-client/snippets.py#L54-L58

##### Node.js

    const snapshot = await db.collection('users').get();
    snapshot.forEach((doc) => {
      console.log(doc.id, '=>', doc.data());
    });https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/firestore/main/index.js#L119-L122

##### Go

    iter := client.Collection("users").Documents(ctx)
    for {
    	doc, err := iter.Next()
    	if err == iterator.Done {
    		break
    	}
    	if err != nil {
    		log.Fatalf("Failed to iterate: %v", err)
    	}
    	fmt.Println(doc.Data())
    }https://github.com/GoogleCloudPlatform/golang-samples/blob/323d864f13303fca135899042d1ecce6efd62722/firestore/firestore_quickstart/main.go#L81-L91

##### PHP

### PHP


For more on installing and creating a Cloud Firestore client, refer to
[Cloud Firestore Client Libraries](https://firebase.google.com/firestore/docs/reference/libraries).

    $usersRef = $db->collection('samples/php/users');
    $snapshot = $usersRef->documents();
    foreach ($snapshot as $user) {
        printf('User: %s' . PHP_EOL, $user->id());
        printf('First: %s' . PHP_EOL, $user['first']);
        if (!empty($user['middle'])) {
            printf('Middle: %s' . PHP_EOL, $user['middle']);
        }
        printf('Last: %s' . PHP_EOL, $user['last']);
        printf('Born: %d' . PHP_EOL, $user['born']);
        printf(PHP_EOL);
    }
    printf('Retrieved and printed out all documents from the users collection.' . PHP_EOL);https://github.com/GoogleCloudPlatform/php-docs-samples/blob/57f7e42e9df09d95da84f23fe6688f51ab8aa0ef/firestore/src/setup_dataset_read.php#L40-L52

##### C#

    CollectionReference usersRef = db.Collection("users");
    QuerySnapshot snapshot = await usersRef.GetSnapshotAsync();
    foreach (DocumentSnapshot document in snapshot.Documents)
    {
        Console.WriteLine("User: {0}", document.Id);
        Dictionary<string, object> documentDictionary = document.ToDictionary();
        Console.WriteLine("First: {0}", documentDictionary["First"]);
        if (documentDictionary.ContainsKey("Middle"))
        {
            Console.WriteLine("Middle: {0}", documentDictionary["Middle"]);
        }
        Console.WriteLine("Last: {0}", documentDictionary["Last"]);
        Console.WriteLine("Born: {0}", documentDictionary["Born"]);
        Console.WriteLine();
    }https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/f0105e127957cddda7c57872b3c2b9a405b0a97d/firestore/api/Quickstart/Program.cs#L79-L93

##### Ruby

    users_ref = firestore.col collection_path
    users_ref.get do |user|
      puts "#{user.document_id} data: #{user.data}."
    endhttps://github.com/googleapis/google-cloud-ruby/blob/56f30b3c8e79535bd66d78b7e43b0174b728d3f0/google-cloud-firestore/samples/quickstart.rb#L77-L80

## Next steps

Deepen your knowledge with the following topics:

- **[Data model](https://firebase.google.com/docs/firestore/data-model)** --- Learn more about how data is structured in Cloud Firestore, including hierarchical data and subcollections.
- **[Add data](https://firebase.google.com/docs/firestore/manage-data/add-data)** --- Learn more about creating and updating data in Cloud Firestore.
- **[Get data](https://firebase.google.com/docs/firestore/query-data/get-data)** --- Learn more about how to retrieve data.
- **[Perform simple and compound queries](https://firebase.google.com/docs/firestore/query-data/queries)** --- Learn how to run simple and compound queries.
- **[Order and limit queries](https://firebase.google.com/docs/firestore/query-data/order-limit-data)** Learn how to order and limit the data returned by your queries.