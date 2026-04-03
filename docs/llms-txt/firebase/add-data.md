# Source: https://firebase.google.com/docs/firestore/manage-data/add-data.md.txt

<br />

This document explains how to set, add, or update individual documents inCloud Firestore. To write data in bulk, see[Transactions and batched writes](https://firebase.google.com/docs/firestore/manage-data/transactions).

## Overview

You can write data toCloud Firestorein one of the following ways:

- Set the data of a document within a collection, explicitly specifying a document identifier.
- Add a new document to a collection. In this case,Cloud Firestoreautomatically generates the document identifier.
- Create an empty document with an automatically generated identifier, and assign data to it later.

| **Note:** While the code samples cover multiple languages, the text explaining the samples refers to the Web method names.

## Before you begin

Before you can initializeCloud Firestoreto set, add, or update data, you must complete the following steps:

- Create aCloud Firestoredatabase. For more information, see[Get started withCloud Firestore](https://firebase.google.com/docs/firestore/quickstart)
- If you use the web or mobile client libraries, authenticate with security rules. For more information, see[Getting started with security rules](https://firebase.google.com/docs/firestore/manage-data/firestore/docs/security/get-started).
- If you use the server client libraries or REST API, authenticate with Identity and Access Management (IAM). For more information, see[Security for server client libraries](https://firebase.google.com/firestore/docs/security/iam).

## InitializeCloud Firestore

Initialize an instance ofCloud Firestore:  

### Web

```python
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://support.google.com/firebase/answer/7015592
const firebaseConfig = {
    FIREBASE_CONFIGURATION
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


// Initialize Cloud Firestore and get a reference to the service
const db = getFirestore(app);
```

Replace<var translate="no">FIREBASE_CONFIGURATION</var>with your web app's[`firebaseConfig`](https://support.google.com/firebase/answer/7015592).

To persist data when the device loses its connection, see the[Enable Offline Data](https://firebase.google.com/docs/firestore/manage-data/enable-offline)documentation.

### Web

```python
import firebase from "firebase/app";
import "firebase/firestore";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://support.google.com/firebase/answer/7015592
const firebaseConfig = {
    FIREBASE_CONFIGURATION
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);


// Initialize Cloud Firestore and get a reference to the service
const db = firebase.firestore();
```

Replace<var translate="no">FIREBASE_CONFIGURATION</var>with your web app's[`firebaseConfig`](https://support.google.com/firebase/answer/7015592).

To persist data when the device loses its connection, see the[Enable Offline Data](https://firebase.google.com/docs/firestore/manage-data/enable-offline)documentation.

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```python
import FirebaseCore
import FirebaseFirestore
```  

```swift
FirebaseApp.configure()

let db = Firestore.firestore()https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/AppDelegate.swift#L31-L33
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```python
@import FirebaseCore;
@import FirebaseFirestore;

// Use Firebase library to configure APIs
[FIRApp configure];
  
```  

```objective-c
FIRFirestore *defaultFirestore = [FIRFirestore firestore];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/AppDelegate.m#L32-L32
```

### Kotlin

```kotlin
// Access a Cloud Firestore instance from your Activity
```  

```kotlin
val db = Firebase.firestore  
https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L109-L109
```

### Java

```java
// Access a Cloud Firestore instance from your Activity
```  

```java
FirebaseFirestore db = FirebaseFirestore.getInstance();https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L131-L131
```

### Dart

```dart
db = FirebaseFirestore.instance;
```

##### Java

TheCloud FirestoreSDK is initialized in different ways depending on your environment. Below are the most common methods. For a complete reference, see[Initialize the Admin SDK](https://firebase.google.com/docs/admin/setup#initialize-sdk).
- **Initialize onGoogle Cloud**  

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

  To use the Firebase Admin SDK on your own server, use a[service account](https://cloud.google.com/compute/docs/authentication).

  Go to[**IAM \& admin \> Service accounts**](https://console.cloud.google.com/iam-admin/serviceaccounts)in the Google Cloud console. Generate a new private key and save the JSON file. Then use the file to initialize the SDK:  

  ```java
  import com.google.auth.oauth2.GoogleCredentials;
  import com.google.cloud.firestore.Firestore;

  import com.google.firebase.FirebaseApp;
  import com.google.firebase.FirebaseOptions;

  // Use a service account
  InputStream serviceAccount = new FileInputStream("<var translate="no">path/to/serviceAccount.json</var>");
  GoogleCredentials credentials = GoogleCredentials.fromStream(serviceAccount);
  FirebaseOptions options = new FirebaseOptions.Builder()
      .setCredentials(credentials)
      .build();
  FirebaseApp.initializeApp(options);

  Firestore db = FirestoreClient.getFirestore();
  ```

##### Python

TheCloud FirestoreSDK is initialized in different ways depending on your environment. Below are the most common methods. For a complete reference, see[Initialize the Admin SDK](https://firebase.google.com/docs/admin/setup#initialize-sdk).
- **Initialize onGoogle Cloud**  

  ```python
  import firebase_admin
  from firebase_admin import firestore

  # Application Default credentials are automatically created.
  app = firebase_admin.initialize_app()
  db = firestore.client()https://github.com/firebase/firebase-admin-python/blob/d5aba8443196e0212d724bd7b81f73689b5c8a08/snippets/firestore/firestore.py#L20-L25
  ```

  An existing application default credential can also be used to initialize the SDK.  

  ```python
  import firebase_admin
  from firebase_admin import credentials
  from firebase_admin import firestore

  # Use the application default credentials.
  cred = credentials.ApplicationDefault()

  firebase_admin.initialize_app(cred)
  db = firestore.client()https://github.com/firebase/firebase-admin-python/blob/d5aba8443196e0212d724bd7b81f73689b5c8a08/snippets/firestore/firestore.py#L30-L38
  ```
- **Initialize on your own server**

  To use the Firebase Admin SDK on your own server, use a[service account](https://cloud.google.com/compute/docs/authentication).

  Go to[**IAM \& admin \> Service accounts**](https://console.cloud.google.com/iam-admin/serviceaccounts)in the Google Cloud console. Generate a new private key and save the JSON file. Then use the file to initialize the SDK:  

  ```python
  import firebase_admin
  from firebase_admin import credentials
  from firebase_admin import firestore

  # Use a service account.
  cred = credentials.Certificate('path/to/serviceAccount.json')

  app = firebase_admin.initialize_app(cred)

  db = firestore.client()https://github.com/firebase/firebase-admin-python/blob/d5aba8443196e0212d724bd7b81f73689b5c8a08/snippets/firestore/firestore.py#L43-L52
  ```

### Python

TheCloud FirestoreSDK is initialized in different ways depending on your environment. Below are the most common methods. For a complete reference, see[Initialize the Admin SDK](https://firebase.google.com/docs/admin/setup#initialize-sdk).
- **Initialize onGoogle Cloud**  

  ```python
  import firebase_admin
  from firebase_admin import firestore_async

  # Application Default credentials are automatically created.
  app = firebase_admin.initialize_app()
  db = firestore_async.client()https://github.com/firebase/firebase-admin-python/blob/d5aba8443196e0212d724bd7b81f73689b5c8a08/snippets/firestore/firestore_async.py#L22-L27
  ```

  An existing application default credential can also be used to initialize the SDK.  

  ```python
  import firebase_admin
  from firebase_admin import credentials
  from firebase_admin import firestore_async

  # Use the application default credentials.
  cred = credentials.ApplicationDefault()

  firebase_admin.initialize_app(cred)
  db = firestore_async.client()https://github.com/firebase/firebase-admin-python/blob/d5aba8443196e0212d724bd7b81f73689b5c8a08/snippets/firestore/firestore_async.py#L32-L40
  ```
- **Initialize on your own server**

  To use the Firebase Admin SDK on your own server, use a[service account](https://cloud.google.com/compute/docs/authentication).

  Go to[**IAM \& admin \> Service accounts**](https://console.cloud.google.com/iam-admin/serviceaccounts)in the Google Cloud console. Generate a new private key and save the JSON file. Then use the file to initialize the SDK:  

  ```python
  import firebase_admin
  from firebase_admin import credentials
  from firebase_admin import firestore_async

  # Use a service account.
  cred = credentials.Certificate('path/to/serviceAccount.json')

  app = firebase_admin.initialize_app(cred)

  db = firestore_async.client()https://github.com/firebase/firebase-admin-python/blob/d5aba8443196e0212d724bd7b81f73689b5c8a08/snippets/firestore/firestore_async.py#L45-L54
  ```

##### C++

```c++
// Make sure the call to `Create()` happens some time before you call Firestore::GetInstance().
App::Create();
Firestore* db = Firestore::GetInstance();https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/ios/firestore-snippets-cpp/AppDelegate.mm#L34-L36
```

##### Node.js

TheCloud FirestoreSDK is initialized in different ways depending on your environment. Below are the most common methods. For a complete reference, see[Initialize the Admin SDK](https://firebase.google.com/docs/admin/setup#initialize-sdk).

- **Initialize onCloud Functions**  

  ```javascript
  const { initializeApp, applicationDefault, cert } = require('firebase-admin/app');
  const { getFirestore, Timestamp, FieldValue, Filter } = require('firebase-admin/firestore');
  ```  

  ```javascript
  initializeApp();

  const db = getFirestore();
  https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L45-L48
  ```
- **Initialize onGoogle Cloud**  

  ```javascript
  const { initializeApp, applicationDefault, cert } = require('firebase-admin/app');
  const { getFirestore, Timestamp, FieldValue, Filter } = require('firebase-admin/firestore');
  ```  

  ```javascript
  initializeApp({
    credential: applicationDefault()
  });

  const db = getFirestore();https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L30-L35
  ```
- **Initialize on your own server**

  To use the Firebase Admin SDK on your own server (or any other Node.js environment), use a[service account](https://cloud.google.com/compute/docs/authentication). Go to[**IAM \& admin \> Service accounts**](https://console.cloud.google.com/iam-admin/serviceaccounts)in the Google Cloud console. Generate a new private key and save the JSON file. Then use the file to initialize the SDK:  

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
  https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L55-L63
  ```

##### Go

TheCloud FirestoreSDK is initialized in different ways depending on your environment. Below are the most common methods. For a complete reference, see[Initialize the Admin SDK](https://firebase.google.com/docs/admin/setup#initialize-sdk).
- **Initialize onGoogle Cloud**  

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

  To use the Firebase Admin SDK on your own server, use a[service account](https://cloud.google.com/compute/docs/authentication).

  Go to[**IAM \& admin \> Service accounts**](https://console.cloud.google.com/iam-admin/serviceaccounts)in the Google Cloud console. Generate a new private key and save the JSON file. Then use the file to initialize the SDK:  

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

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

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
    }  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/setup_client_create.php#L27-L47

##### Unity

```c#
using Firebase.Firestore;
using Firebase.Extensions;
```  

```c#
FirebaseFirestore db = FirebaseFirestore.DefaultInstance;
```

##### C#

### C#

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    FirestoreDb db = FirestoreDb.Create(project);
    Console.WriteLine("Created Cloud Firestore client with project ID: {0}", project);  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/Quickstart/Program.cs#L37-L38

##### Ruby

    require "google/cloud/firestore"

    # The `project_id` parameter is optional and represents which project the
    # client will act on behalf of. If not supplied, the client falls back to the
    # default project inferred from the environment.
    firestore = Google::Cloud::Firestore.new project_id: project_id

    puts "Created Cloud Firestore client with given project ID."  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/quickstart.rb#L19-L26

## Set a document

To create or overwrite a single document, use the following language-specific`set()`methods:  

### Web

Use the`setDoc()`method:  

```javascript
import { doc, setDoc } from "firebase/firestore"; 

// Add a new document in collection "cities"
await setDoc(doc(db, "cities", "LA"), {
  name: "Los Angeles",
  state: "CA",
  country: "USA"
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/set_document.js#L8-L15
```

### Web

Use the`set()`method:  

```javascript
// Add a new document in collection "cities"
db.collection("cities").doc("LA").set({
    name: "Los Angeles",
    state: "CA",
    country: "USA"
})
.then(() => {
    console.log("Document successfully written!");
})
.catch((error) => {
    console.error("Error writing document: ", error);
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L221-L232
```

##### Swift

Use the`setData()`method:  
**Note:**This product is not available on watchOS and App Clip targets.  

```swift
// Add a new document in collection "cities"
do {
  try await db.collection("cities").document("LA").setData([
    "name": "Los Angeles",
    "state": "CA",
    "country": "USA"
  ])
  print("Document successfully written!")
} catch {
  print("Error writing document: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L269-L279
```

##### Objective-C

Use the`setData:`method:  
**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
// Add a new document in collection "cities"
[[[self.db collectionWithPath:@"cities"] documentWithPath:@"LA"] setData:@{
  @"name": @"Los Angeles",
  @"state": @"CA",
  @"country": @"USA"
} completion:^(NSError * _Nullable error) {
  if (error != nil) {
    NSLog(@"Error writing document: %@", error);
  } else {
    NSLog(@"Document successfully written!");
  }
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L198-L209
```

### Kotlin

Use the`set()`method:  

```kotlin
val city = hashMapOf(
    "name" to "Los Angeles",
    "state" to "CA",
    "country" to "USA",
)

db.collection("cities").document("LA")
    .set(city)
    .addOnSuccessListener { Log.d(TAG, "DocumentSnapshot successfully written!") }
    .addOnFailureListener { e -> Log.w(TAG, "Error writing document", e) }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L252-L261
```

### Java

Use the`set()`method:  

```java
Map<String, Object> city = new HashMap<>();
city.put("name", "Los Angeles");
city.put("state", "CA");
city.put("country", "USA");

db.collection("cities").document("LA")
        .set(city)
        .addOnSuccessListener(new OnSuccessListener<Void>() {
            @Override
            public void onSuccess(Void aVoid) {
                Log.d(TAG, "DocumentSnapshot successfully written!");
            }
        })
        .addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception e) {
                Log.w(TAG, "Error writing document", e);
            }
        });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L337-L355
```

### Dart

Use the`set()`method:  

```dart
final city = <String, String>{
  "name": "Los Angeles",
  "state": "CA",
  "country": "USA"
};

db
    .collection("cities")
    .doc("LA")
    .set(city)
    .onError((e, _) => print("Error writing document: $e"));https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L132-L142
```

##### Java

Use the`set()`method:  

    // Create a Map to store the data we want to set
    Map<String, Object> docData = new HashMap<>();
    docData.put("name", "Los Angeles");
    docData.put("state", "CA");
    docData.put("country", "USA");
    docData.put("regions", Arrays.asList("west_coast", "socal"));
    // Add a new document (asynchronously) in collection "cities" with id "LA"
    ApiFuture<WriteResult> future = db.collection("cities").document("LA").set(docData);
    // ...
    // future.get() blocks on response
    System.out.println("Update time : " + future.get().getUpdateTime());  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L58-L68

##### Python

Use the`set()`method:  

    data = {"name": "Los Angeles", "state": "CA", "country": "USA"}

    # Add a new doc in collection 'cities' with ID 'LA'
    db.collection("cities").document("LA").set(data)  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L69-L72

### Python

Use the`set()`method:  

    data = {"name": "Los Angeles", "state": "CA", "country": "USA"}

    # Add a new doc in collection 'cities' with ID 'LA'
    await db.collection("cities").document("LA").set(data)  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L65-L68

##### C++

Use the`Set()`method:  

```c++
// Add a new document in collection 'cities'
db->Collection("cities")
    .Document("LA")
    .Set({{"name", FieldValue::String("Los Angeles")},
          {"state", FieldValue::String("CA")},
          {"country", FieldValue::String("USA")}})
    .OnCompletion([](const Future<void>& future) {
      if (future.error() == Error::kErrorOk) {
        std::cout << "DocumentSnapshot successfully written!" << std::endl;
      } else {
        std::cout << "Error writing document: " << future.error_message()
                  << std::endl;
      }
    });https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L154-L167
```

##### Node.js

Use the`set()`method:  

    const data = {
      name: 'Los Angeles',
      state: 'CA',
      country: 'USA'
    };

    // Add a new document in collection "cities" with ID 'LA'
    const res = await db.collection('cities').doc('LA').set(data);  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L157-L164

##### Go

Use the`Set()`method:  


    import (
    	"context"
    	"log"

    	"cloud.google.com/go/firestore"
    )

    func addDocAsMap(ctx context.Context, client *firestore.Client) error {
    	_, err := client.Collection("cities").Doc("LA").Set(ctx, map[string]interface{}{
    		"name":    "Los Angeles",
    		"state":   "CA",
    		"country": "USA",
    	})
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}

    	return err
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/save_data_set_from_map.go#L18-L39

##### PHP

Use the`set()`method:

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $data = [
        'name' => 'Los Angeles',
        'state' => 'CA',
        'country' => 'USA'
    ];
    $db->collection('samples/php/cities')->document('LA')->set($data);  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_set_from_map.php#L40-L45

##### Unity

Use the`SetAsync()`method:  

```c#
DocumentReference docRef = db.Collection("cities").Document("LA");
Dictionary<string, object> city = new Dictionary<string, object>
{
	{ "Name", "Los Angeles" },
	{ "State", "CA" },
	{ "Country", "USA" }
};
docRef.SetAsync(city).ContinueWithOnMainThread(task => {
	Debug.Log("Added data to the LA document in the cities collection.");
});
```

##### C#

Use the`SetAsync()`method:  

    DocumentReference docRef = db.Collection("cities").Document("LA");
    Dictionary<string, object> city = new Dictionary<string, object>
    {
        { "name", "Los Angeles" },
        { "state", "CA" },
        { "country", "USA" }
    };
    await docRef.SetAsync(city);  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/AddData/Program.cs#L46-L53

##### Ruby

Use the`set()`method:  

    city_ref = firestore.doc "#{collection_path}/LA"

    data = {
      name:    "Los Angeles",
      state:   "CA",
      country: "USA"
    }

    city_ref.set data  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/add_data.rb#L24-L32

If the document does not exist, it will be created. If the document does exist, its contents will be overwritten with the newly provided data, unless you specify that the data should be merged into the existing document, as follows:  

### Web

```javascript
import { doc, setDoc } from "firebase/firestore"; 

const cityRef = doc(db, 'cities', 'BJ');
setDoc(cityRef, { capital: true }, { merge: true });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/set_with_merge.js#L8-L11
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
var cityRef = db.collection('cities').doc('BJ');

var setWithMerge = cityRef.set({
    capital: true
}, { merge: true });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L318-L322
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
// Update one field, creating the document if it does not exist.
db.collection("cities").document("BJ").setData([ "capital": true ], merge: true)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L406-L407
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
// Write to the document reference, merging data with existing
// if the document already exists
[[[self.db collectionWithPath:@"cities"] documentWithPath:@"BJ"]
     setData:@{ @"capital": @YES }
     merge:YES
     completion:^(NSError * _Nullable error) {
       // ...
     }];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L323-L330
```

### Kotlin

```kotlin
// Update one field, creating the document if it does not already exist.
val data = hashMapOf("capital" to true)

db.collection("cities").document("BJ")
    .set(data, SetOptions.merge())https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L395-L399
```

### Java

```java
// Update one field, creating the document if it does not already exist.
Map<String, Object> data = new HashMap<>();
data.put("capital", true);

db.collection("cities").document("BJ")
        .set(data, SetOptions.merge());https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L504-L509
```

### Dart

```dart
// Update one field, creating the document if it does not already exist.
final data = {"capital": true};

db.collection("cities").doc("BJ").set(data, SetOptions(merge: true));https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L148-L151
```

##### Java

    // asynchronously update doc, create the document if missing
    Map<String, Object> update = new HashMap<>();
    update.put("capital", true);

    ApiFuture<WriteResult> writeResult =
        db.collection("cities").document("BJ").set(update, SetOptions.merge());
    // ...
    System.out.println("Update time : " + writeResult.get().getUpdateTime());  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L206-L213

##### Python

    city_ref = db.collection("cities").document("BJ")

    city_ref.set({"capital": True}, merge=True)  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L360-L362

### Python

    city_ref = db.collection("cities").document("BJ")

    await city_ref.set({"capital": True}, merge=True)  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L354-L356

##### C++

```c++
db->Collection("cities").Document("BJ").Set(
    {{"capital", FieldValue::Boolean(true)}}, SetOptions::Merge());https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L175-L176
```

##### Node.js

    const cityRef = db.collection('cities').doc('BJ');

    const res = await cityRef.set({
      capital: true
    }, { merge: true });  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L294-L298

##### Go


    import (
    	"context"
    	"log"

    	"cloud.google.com/go/firestore"
    )

    func updateDocCreateIfMissing(ctx context.Context, client *firestore.Client) error {
    	_, err := client.Collection("cities").Doc("BJ").Set(ctx, map[string]interface{}{
    		"capital": true,
    	}, firestore.MergeAll)

    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}

    	return err
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/save_data_set_doc_upsert.go#L18-L38

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $cityRef = $db->collection('samples/php/cities')->document('BJ');
    $cityRef->set([
        'capital' => true
    ], ['merge' => true]);  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_set_doc_upsert.php#L40-L43

##### Unity

```c#
DocumentReference docRef = db.Collection("cities").Document("LA");
Dictionary<string, object> update = new Dictionary<string, object>
{
	{ "capital", false }
};
docRef.SetAsync(update, SetOptions.MergeAll);
```

##### C#

    DocumentReference docRef = db.Collection("cities").Document("LA");
    Dictionary<string, object> update = new Dictionary<string, object>
    {
        { "capital", false }
    };
    await docRef.SetAsync(update, SetOptions.MergeAll);  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/AddData/Program.cs#L62-L67

##### Ruby

    city_ref = firestore.doc "#{collection_path}/LA"
    city_ref.set({ capital: false }, merge: true)  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/add_data.rb#L43-L44

If you're not sure whether the document exists, pass the option to merge the new data with any existing document to avoid overwriting entire documents. For documents that contain maps, if you specify a set with a field that contains an empty map, the map field of the target document is overwritten.

### Data types

Cloud Firestorelets you write a variety of data types inside a document, including strings, booleans, numbers, dates, null, and nested arrays and objects.Cloud Firestorealways stores numbers as doubles, regardless of what type of number you use in your code.  

### Web

```javascript
import { doc, setDoc, Timestamp } from "firebase/firestore"; 

const docData = {
    stringExample: "Hello world!",
    booleanExample: true,
    numberExample: 3.14159265,
    dateExample: Timestamp.fromDate(new Date("December 10, 1815")),
    arrayExample: [5, true, "hello"],
    nullExample: null,
    objectExample: {
        a: 5,
        b: {
            nested: "foo"
        }
    }
};
await setDoc(doc(db, "data", "one"), docData);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/data_types.js#L8-L24
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
var docData = {
    stringExample: "Hello world!",
    booleanExample: true,
    numberExample: 3.14159265,
    dateExample: firebase.firestore.Timestamp.fromDate(new Date("December 10, 1815")),
    arrayExample: [5, true, "hello"],
    nullExample: null,
    objectExample: {
        a: 5,
        b: {
            nested: "foo"
        }
    }
};
db.collection("data").doc("one").set(docData).then(() => {
    console.log("Document successfully written!");
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L296-L312
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
let docData: [String: Any] = [
  "stringExample": "Hello world!",
  "booleanExample": true,
  "numberExample": 3.14159265,
  "dateExample": Timestamp(date: Date()),
  "arrayExample": [5, true, "hello"],
  "nullExample": NSNull(),
  "objectExample": [
    "a": 5,
    "b": [
      "nested": "foo"
    ]
  ]
]
do {
  try await db.collection("data").document("one").setData(docData)
  print("Document successfully written!")
} catch {
  print("Error writing document: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L301-L320
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
NSDictionary *docData = @{
  @"stringExample": @"Hello world!",
  @"booleanExample": @YES,
  @"numberExample": @3.14,
  @"dateExample": [FIRTimestamp timestampWithDate:[NSDate date]],
  @"arrayExample": @[@5, @YES, @"hello"],
  @"nullExample": [NSNull null],
  @"objectExample": @{
    @"a": @5,
    @"b": @{
      @"nested": @"foo"
    }
  }
};

[[[self.db collectionWithPath:@"data"] documentWithPath:@"one"] setData:docData
    completion:^(NSError * _Nullable error) {
      if (error != nil) {
        NSLog(@"Error writing document: %@", error);
      } else {
        NSLog(@"Document successfully written!");
      }
    }];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L215-L237
```

### Kotlin

```kotlin
val docData = hashMapOf(
    "stringExample" to "Hello world!",
    "booleanExample" to true,
    "numberExample" to 3.14159265,
    "dateExample" to Timestamp(Date()),
    "listExample" to arrayListOf(1, 2, 3),
    "nullExample" to null,
)

val nestedData = hashMapOf(
    "a" to 5,
    "b" to true,
)

docData["objectExample"] = nestedData

db.collection("data").document("one")
    .set(docData)
    .addOnSuccessListener { Log.d(TAG, "DocumentSnapshot successfully written!") }
    .addOnFailureListener { e -> Log.w(TAG, "Error writing document", e) }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L273-L292
```

### Java

```java
Map<String, Object> docData = new HashMap<>();
docData.put("stringExample", "Hello world!");
docData.put("booleanExample", true);
docData.put("numberExample", 3.14159265);
docData.put("dateExample", new Timestamp(new Date()));
docData.put("listExample", Arrays.asList(1, 2, 3));
docData.put("nullExample", null);

Map<String, Object> nestedData = new HashMap<>();
nestedData.put("a", 5);
nestedData.put("b", true);

docData.put("objectExample", nestedData);

db.collection("data").document("one")
        .set(docData)
        .addOnSuccessListener(new OnSuccessListener<Void>() {
            @Override
            public void onSuccess(Void aVoid) {
                Log.d(TAG, "DocumentSnapshot successfully written!");
            }
        })
        .addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception e) {
                Log.w(TAG, "Error writing document", e);
            }
        });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L367-L394
```

### Dart

```dart
final docData = {
  "stringExample": "Hello world!",
  "booleanExample": true,
  "numberExample": 3.14159265,
  "dateExample": Timestamp.now(),
  "listExample": [1, 2, 3],
  "nullExample": null
};

final nestedData = {
  "a": 5,
  "b": true,
};

docData["objectExample"] = nestedData;

db
    .collection("data")
    .doc("one")
    .set(docData)
    .onError((e, _) => print("Error writing document: $e"));https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L157-L177
```

##### Java

    Map<String, Object> docData = new HashMap<>();
    docData.put("stringExample", "Hello, World");
    docData.put("booleanExample", false);
    docData.put("numberExample", 3.14159265);
    docData.put("nullExample", null);

    ArrayList<Object> arrayExample = new ArrayList<>();
    Collections.addAll(arrayExample, 5L, true, "hello");
    docData.put("arrayExample", arrayExample);

    Map<String, Object> objectExample = new HashMap<>();
    objectExample.put("a", 5L);
    objectExample.put("b", true);

    docData.put("objectExample", objectExample);

    ApiFuture<WriteResult> future = db.collection("data").document("one").set(docData);
    System.out.println("Update time : " + future.get().getUpdateTime());  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L80-L97

##### Python

    data = {
        "stringExample": "Hello, World!",
        "booleanExample": True,
        "numberExample": 3.14159265,
        "dateExample": datetime.datetime.now(tz=datetime.timezone.utc),
        "arrayExample": [5, True, "hello"],
        "nullExample": None,
        "objectExample": {"a": 5, "b": True},
    }

    db.collection("data").document("one").set(data)  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L79-L89

### Python

    data = {
        "stringExample": "Hello, World!",
        "booleanExample": True,
        "numberExample": 3.14159265,
        "dateExample": datetime.datetime.now(tz=datetime.timezone.utc),
        "arrayExample": [5, True, "hello"],
        "nullExample": None,
        "objectExample": {"a": 5, "b": True},
    }

    await db.collection("data").document("one").set(data)  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L75-L85

##### C++

```c++
MapFieldValue doc_data{
    {"stringExample", FieldValue::String("Hello world!")},
    {"booleanExample", FieldValue::Boolean(true)},
    {"numberExample", FieldValue::Double(3.14159265)},
    {"dateExample", FieldValue::Timestamp(Timestamp::Now())},
    {"arrayExample", FieldValue::Array({FieldValue::Integer(1),
                                        FieldValue::Integer(2),
                                        FieldValue::Integer(3)})},
    {"nullExample", FieldValue::Null()},
    {"objectExample",
     FieldValue::Map(
         {{"a", FieldValue::Integer(5)},
          {"b", FieldValue::Map(
                    {{"nested", FieldValue::String("foo")}})}})},
};

db->Collection("data").Document("one").Set(doc_data).OnCompletion(
    [](const Future<void>& future) {
      if (future.error() == Error::kErrorOk) {
        std::cout << "DocumentSnapshot successfully written!" << std::endl;
      } else {
        std::cout << "Error writing document: " << future.error_message()
                  << std::endl;
      }
    });https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L193-L217
```

##### Node.js

    const data = {
      stringExample: 'Hello, World!',
      booleanExample: true,
      numberExample: 3.14159265,
      dateExample: Timestamp.fromDate(new Date('December 10, 1815')),
      arrayExample: [5, true, 'hello'],
      nullExample: null,
      objectExample: {
        a: 5,
        b: true
      }
    };

    const res = await db.collection('data').doc('one').set(data);  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L172-L185

##### Go


    import (
    	"context"
    	"log"
    	"time"

    	"cloud.google.com/go/firestore"
    )

    func addDocDataTypes(ctx context.Context, client *firestore.Client) error {
    	doc := make(map[string]interface{})
    	doc["stringExample"] = "Hello world!"
    	doc["booleanExample"] = true
    	doc["numberExample"] = 3.14159265
    	doc["dateExample"] = time.Now()
    	doc["arrayExample"] = []interface{}{5, true, "hello"}
    	doc["nullExample"] = nil
    	doc["objectExample"] = map[string]interface{}{
    		"a": 5,
    		"b": true,
    	}

    	_, err := client.Collection("data").Doc("one").Set(ctx, doc)
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}

    	return err
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/save_data_set_from_map_nested.go#L18-L48

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $data = [
        'stringExample' => 'Hello World',
        'booleanExample' => true,
        'numberExample' => 3.14159265,
        'dateExample' => new Timestamp(new DateTime()),
        'arrayExample' => array(5, true, 'hello'),
        'nullExample' => null,
        'objectExample' => ['a' => 5, 'b' => true],
        'documentReferenceExample' => $db->collection('samples/php/data')->document('two'),
    ];
    $db->collection('samples/php/data')->document('one')->set($data);
    printf('Set multiple data-type data for the one document in the data collection.' . PHP_EOL);  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_set_from_map_nested.php#L44-L55

##### Unity

```c#
DocumentReference docRef = db.Collection("data").Document("one");
Dictionary<string, object> docData = new Dictionary<string, object>
{
	{ "stringExample", "Hello World" },
	{ "booleanExample", false },
	{ "numberExample", 3.14159265 },
	{ "nullExample", null },
	{ "arrayExample", new List<object>() { 5, true, "Hello" } },
	{ "objectExample", new Dictionary<string, object>
		{
			{ "a", 5 },
			{ "b", true },
		}
	},
};

docRef.SetAsync(docData);
```

##### C#

    DocumentReference docRef = db.Collection("data").Document("one");
    Dictionary<string, object> docData = new Dictionary<string, object>
    {
        { "stringExample", "Hello World" },
        { "booleanExample", false },
        { "numberExample", 3.14159265 },
        { "nullExample", null },
        { "arrayExample", new object[] { 5, true, "Hello" } },
        { "objectExample", new Dictionary<string, object>
            {
                { "a", 5 },
                { "b", true},
            }
        }
    };

    await docRef.SetAsync(docData);  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/AddData/Program.cs#L76-L92

##### Ruby

    doc_ref = firestore.doc "#{collection_path}/one"

    data = {
      stringExample:  "Hello, World!",
      booleanExample: true,
      numberExample:  3.14159265,
      dateExample:    DateTime.now,
      arrayExample:   [5, true, "hello"],
      nullExample:    nil,
      objectExample:  {
        a: 5,
        b: true
      }
    }

    doc_ref.set data  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/add_data.rb#L55-L70

### Custom objects

Using`Map`or`Dictionary`objects to represent your documents is often inconvenient, soCloud Firestoresupports writing documents with custom classes.Cloud Firestoreconverts the objects to supported data types.

Using custom classes, you can rewrite the initial example in the following way:  

### Web

```javascript
class City {
    constructor (name, state, country ) {
        this.name = name;
        this.state = state;
        this.country = country;
    }
    toString() {
        return this.name + ', ' + this.state + ', ' + this.country;
    }
}

// Firestore data converter
const cityConverter = {
    toFirestore: (city) => {
        return {
            name: city.name,
            state: city.state,
            country: city.country
            };
    },
    fromFirestore: (snapshot, options) => {
        const data = snapshot.data(options);
        return new City(data.name, data.state, data.country);
    }
};https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/city_custom_object.js#L8-L32
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
class City {
    constructor (name, state, country ) {
        this.name = name;
        this.state = state;
        this.country = country;
    }
    toString() {
        return this.name + ', ' + this.state + ', ' + this.country;
    }
}

// Firestore data converter
var cityConverter = {
    toFirestore: function(city) {
        return {
            name: city.name,
            state: city.state,
            country: city.country
            };
    },
    fromFirestore: function(snapshot, options){
        const data = snapshot.data(options);
        return new City(data.name, data.state, data.country);
    }
};https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L7-L31
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
public struct City: Codable, Sendable {

  let name: String
  let state: String?
  let country: String?
  let isCapital: Bool?
  let population: Int64?

  enum CodingKeys: String, CodingKey {
    case name
    case state
    case country
    case isCapital = "capital"
    case population
  }

}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L1463-L1479
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
// This isn't supported in Objective-C.
  
```

### Kotlin

```kotlin
data class City(
    val name: String? = null,
    val state: String? = null,
    val country: String? = null,
    @field:JvmField // use this annotation if your Boolean field is prefixed with 'is'
    val isCapital: Boolean? = null,
    val population: Long? = null,
    val regions: List<String>? = null,
)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L239-L247
```

### Java

Each custom class must have a public constructor that takes no arguments. In addition, the class must include a public getter for each property.  

```java
public class City {


    private String name;
    private String state;
    private String country;
    private boolean capital;
    private long population;
    private List<String> regions;

    public City() {}

    public City(String name, String state, String country, boolean capital, long population, List<String> regions) {
        // ...
    }

    public String getName() {
        return name;
    }

    public String getState() {
        return state;
    }

    public String getCountry() {
        return country;
    }

    public boolean isCapital() {
        return capital;
    }

    public long getPopulation() {
        return population;
    }

    public List<String> getRegions() {
        return regions;
    }

}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L285-L332
```

### Dart

```dart
class City {
  final String? name;
  final String? state;
  final String? country;
  final bool? capital;
  final int? population;
  final List<String>? regions;

  City({
    this.name,
    this.state,
    this.country,
    this.capital,
    this.population,
    this.regions,
  });

  factory City.fromFirestore(
    DocumentSnapshot<Map<String, dynamic>> snapshot,
    SnapshotOptions? options,
  ) {
    final data = snapshot.data();
    return City(
      name: data?['name'],
      state: data?['state'],
      country: data?['country'],
      capital: data?['capital'],
      population: data?['population'],
      regions:
          data?['regions'] is Iterable ? List.from(data?['regions']) : null,
    );
  }

  Map<String, dynamic> toFirestore() {
    return {
      if (name != null) "name": name,
      if (state != null) "state": state,
      if (country != null) "country": country,
      if (capital != null) "capital": capital,
      if (population != null) "population": population,
      if (regions != null) "regions": regions,
    };
  }
}https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/model/firestore_add_data_custom_objects_snippet.dart#L18-L61
```

##### Java

    public City() {
      // Must have a public no-argument constructor
    }

    // Initialize all fields of a city
    public City(
        String name,
        String state,
        String country,
        Boolean capital,
        Long population,
        List<String> regions) {
      this.name = name;
      this.state = state;
      this.country = country;
      this.capital = capital;
      this.population = population;
      this.regions = regions;
    }  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/model/City.java#L33-L52

##### Python

    class City:
        def __init__(self, name, state, country, capital=False, population=0, regions=[]):
            self.name = name
            self.state = state
            self.country = country
            self.capital = capital
            self.population = population
            self.regions = regions

        @staticmethod
        def from_dict(source):
            # ...

        def to_dict(self):
            # ...

        def __repr__(self):
            return f"City(\
                    name={self.name}, \
                    country={self.country}, \
                    population={self.population}, \
                    capital={self.capital}, \
                    regions={self.regions}\
                )"

    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L94-L145

### Python

    class City:
        def __init__(self, name, state, country, capital=False, population=0, regions=[]):
            self.name = name
            self.state = state
            self.country = country
            self.capital = capital
            self.population = population
            self.regions = regions

        @staticmethod
        def from_dict(source):
            # ...

        def to_dict(self):
            # ...

        def __repr__(self):
            return f"City(\
                    name={self.name}, \
                    country={self.country}, \
                    population={self.population}, \
                    capital={self.capital}, \
                    regions={self.regions}\
                )"

    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L90-L141

##### C++

```c++
// This is not yet supported.
```

##### Node.js

```javascript
// Node.js uses JavaScript objects
```

##### Go


    // City represents a city.
    type City struct {
    	Name       string   `firestore:"name,omitempty"`
    	State      string   `firestore:"state,omitempty"`
    	Country    string   `firestore:"country,omitempty"`
    	Capital    bool     `firestore:"capital,omitempty"`
    	Population int64    `firestore:"population,omitempty"`
    	Density    int64    `firestore:"density,omitempty"`
    	Regions    []string `firestore:"regions,omitempty"`
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/custom_type_definition.go#L18-L29

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    class City
    {
        /** @var string */
        public $name;
        /** @var string */
        public $state;
        /** @var string */
        public $country;
        /** @var bool */
        public $capital;
        /** @var int */
        public $population;
        /** @var array<string> */
        public $regions;

        /**
         * @param array<string> $regions
         */
        public function __construct(
            string $name,
            string $state,
            string $country,
            bool $capital = false,
            int $population = 0,
            array $regions = []
        ) {
            $this->name = $name;
            $this->state = $state;
            $this->country = $country;
            $this->capital = $capital;
            $this->population = $population;
            $this->regions = $regions;
        }

        /**
         * @param array<mixed> $source
         */
        public static function fromArray(array $source): City
        {
            // implementation of fromArray is excluded for brevity
            # ...
        }

        /**
         * @return array<mixed>
         */
        public function toArray(): array
        {
            // implementation of toArray is excluded for brevity
            # ...
        }

        public function __toString()
        {
            // implementation of __toString is excluded for brevity
            # ...
        }
    }  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/City.php#L27-L126

##### Unity

```c#
[FirestoreData]
public class City
{
	[FirestoreProperty]
	public string Name { get; set; }

	[FirestoreProperty]
	public string State { get; set; }

	[FirestoreProperty]
	public string Country { get; set; }

	[FirestoreProperty]
	public bool Capital { get; set; }

	[FirestoreProperty]
	public long Population { get; set; }
}
```

##### C#

    [FirestoreData]
    public class City
    {
        [FirestoreProperty]
        public string Name { get; set; }

        [FirestoreProperty]
        public string State { get; set; }

        [FirestoreProperty]
        public string Country { get; set; }

        [FirestoreProperty]
        public bool Capital { get; set; }

        [FirestoreProperty]
        public long Population { get; set; }
    }  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/AddData/Program.cs#L98-L115

##### Ruby

```ruby
// This isn't supported in Ruby
```  

### Web

```javascript
import { doc, setDoc } from "firebase/firestore"; 

// Set with cityConverter
const ref = doc(db, "cities", "LA").withConverter(cityConverter);
await setDoc(ref, new City("Los Angeles", "CA", "USA"));https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/set_custom_object.js#L8-L12
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
// Set with cityConverter
db.collection("cities").doc("LA")
  .withConverter(cityConverter)
  .set(new City("Los Angeles", "CA", "USA"));https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L240-L243
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
let city = City(name: "Los Angeles",
                state: "CA",
                country: "USA",
                isCapital: false,
                population: 5000000)

do {
  try db.collection("cities").document("LA").setData(from: city)
} catch let error {
  print("Error writing city to Firestore: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L285-L295
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
// This isn't supported in Objective-C.
  
```

### Kotlin

```kotlin
val city = City(
    "Los Angeles",
    "CA",
    "USA",
    false,
    5000000L,
    listOf("west_coast", "socal"),
)
db.collection("cities").document("LA").set(city)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L298-L306
```

### Java

```java
City city = new City("Los Angeles", "CA", "USA",
        false, 5000000L, Arrays.asList("west_coast", "sorcal"));
db.collection("cities").document("LA").set(city);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L400-L402
```

### Dart

```dart
final city = City(
  name: "Los Angeles",
  state: "CA",
  country: "USA",
  capital: false,
  population: 5000000,
  regions: ["west_coast", "socal"],
);
final docRef = db
    .collection("cities")
    .withConverter(
      fromFirestore: City.fromFirestore,
      toFirestore: (City city, options) => city.toFirestore(),
    )
    .doc("LA");
await docRef.set(city);https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L183-L198
```

##### Java

    City city =
        new City("Los Angeles", "CA", "USA", false, 3900000L, Arrays.asList("west_coast", "socal"));
    ApiFuture<WriteResult> future = db.collection("cities").document("LA").set(city);
    // block on response if required
    System.out.println("Update time : " + future.get().getUpdateTime());  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L110-L114

##### Python

    city = City(name="Los Angeles", state="CA", country="USA")
    db.collection("cities").document("LA").set(city.to_dict())  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L178-L179

### Python

    city = City(name="Los Angeles", state="CA", country="USA")
    await db.collection("cities").document("LA").set(city.to_dict())  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L174-L175

##### C++

```c++
// This is not yet supported.
```

##### Node.js

```javascript
// Node.js uses JavaScript objects
```

##### Go


    import (
    	"context"
    	"log"

    	"cloud.google.com/go/firestore"
    )

    func addDocAsEntity(ctx context.Context, client *firestore.Client) error {
    	city := City{
    		Name:    "Los Angeles",
    		Country: "USA",
    	}
    	_, err := client.Collection("cities").Doc("LA").Set(ctx, city)
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}

    	return err
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/save_data_set_from_custom_type.go#L18-L39

##### PHP

```php
// This isn't supported in PHP.
```

##### Unity

```c#
DocumentReference docRef = db.Collection("cities").Document("LA");
City city = new City
{
	Name = "Los Angeles",
	State = "CA",
	Country = "USA",
	Capital = false,
	Population = 3900000L
};
docRef.SetAsync(city);
```

##### C#

    DocumentReference docRef = db.Collection("cities").Document("LA");
    City city = new City
    {
        Name = "Los Angeles",
        State = "CA",
        Country = "USA",
        Capital = false,
        Population = 3900000L
    };
    await docRef.SetAsync(city);  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/AddData/Program.cs#L122-L131

##### Ruby

```ruby
// This isn't supported in Ruby.
```

## Add a document

When you use`set()`to create a document, you must specify an ID for the document to create, as shown in the following example:  

### Web

```javascript
import { doc, setDoc } from "firebase/firestore"; 

await setDoc(doc(db, "cities", "new-city-id"), data);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/cities_document_set.js#L8-L10
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
db.collection("cities").doc("new-city-id").set(data);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L430-L430
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
db.collection("cities").document("new-city-id").setData(data)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L328-L328
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
[[[self.db collectionWithPath:@"cities"] documentWithPath:@"new-city-id"]
    setData:data];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L244-L245
```

### Kotlin

```kotlin
db.collection("cities").document("new-city-id").set(data)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L267-L267
```

### Java

```java
db.collection("cities").document("new-city-id").set(data);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L361-L361
```

### Dart

```dart
db.collection("cities").doc("new-city-id").set({"name": "Chicago"});https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L204-L204
```

##### Java

    db.collection("cities").document("new-city-id").set(data);  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L123-L123

##### Python

    db.collection("cities").document("new-city-id").set(data)  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L187-L187

### Python

    await db.collection("cities").document("new-city-id").set(data)  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L183-L183

##### C++

```c++
db->Collection("cities").Document("SF").Set({/*some data*/});https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L228-L228
```

##### Node.js

    await db.collection('cities').doc('new-city-id').set(data);  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L209-L209

##### Go


    import (
    	"context"
    	"log"

    	"cloud.google.com/go/firestore"
    )

    func addDocWithID(ctx context.Context, client *firestore.Client) error {
    	var data = make(map[string]interface{})

    	_, err := client.Collection("cities").Doc("new-city-id").Set(ctx, data)
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}

    	return err
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/save_data_set_id_specified.go#L18-L37

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $db->collection('samples/php/cities')->document('new-city-id')->set($data);  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_set_id_specified.php#L44-L44

##### Unity

```c#
db.Collection("cities").Document("new-city-id").SetAsync(city);
```

##### C#

    await db.Collection("cities").Document("new-city-id").SetAsync(city);  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/AddData/Program.cs#L145-L145

##### Ruby

    city_ref = firestore.doc "#{collection_path}/new-city-id"
    city_ref.set data  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/add_data.rb#L86-L87

If there isn't a meaningful ID for the document,Cloud Firestorecan auto-generate an ID for you. You can call the following language-specific`add()`methods:  

### Web

Use the`addDoc()`method:  

```javascript
import { collection, addDoc } from "firebase/firestore"; 

// Add a new document with a generated id.
const docRef = await addDoc(collection(db, "cities"), {
  name: "Tokyo",
  country: "Japan"
});
console.log("Document written with ID: ", docRef.id);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/add_document.js#L8-L15
```

### Web

Use the`add()`method:  

```javascript
// Add a new document with a generated id.
db.collection("cities").add({
    name: "Tokyo",
    country: "Japan"
})
.then((docRef) => {
    console.log("Document written with ID: ", docRef.id);
})
.catch((error) => {
    console.error("Error adding document: ", error);
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L438-L448
```

##### Swift

Use the`addDocument()`method:  
**Note:**This product is not available on watchOS and App Clip targets.  

```swift
// Add a new document with a generated id.
do {
  let ref = try await db.collection("cities").addDocument(data: [
    "name": "Tokyo",
    "country": "Japan"
  ])
  print("Document added with ID: \(ref.documentID)")
} catch {
  print("Error adding document: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L334-L343
```

##### Objective-C

Use the`addDocumentWithData:`method:  
**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
// Add a new document with a generated id.
__block FIRDocumentReference *ref =
    [[self.db collectionWithPath:@"cities"] addDocumentWithData:@{
      @"name": @"Tokyo",
      @"country": @"Japan"
    } completion:^(NSError * _Nullable error) {
      if (error != nil) {
        NSLog(@"Error adding document: %@", error);
      } else {
        NSLog(@"Document added with ID: %@", ref.documentID);
      }
    }];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L251-L262
```

### Kotlin

Use the`add()`method:  

```kotlin
// Add a new document with a generated id.
val data = hashMapOf(
    "name" to "Tokyo",
    "country" to "Japan",
)

db.collection("cities")
    .add(data)
    .addOnSuccessListener { documentReference ->
        Log.d(TAG, "DocumentSnapshot written with ID: ${documentReference.id}")
    }
    .addOnFailureListener { e ->
        Log.w(TAG, "Error adding document", e)
    }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L312-L325
```

### Java

Use the`add()`method:  

```java
// Add a new document with a generated id.
Map<String, Object> data = new HashMap<>();
data.put("name", "Tokyo");
data.put("country", "Japan");

db.collection("cities")
        .add(data)
        .addOnSuccessListener(new OnSuccessListener<DocumentReference>() {
            @Override
            public void onSuccess(DocumentReference documentReference) {
                Log.d(TAG, "DocumentSnapshot written with ID: " + documentReference.getId());
            }
        })
        .addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception e) {
                Log.w(TAG, "Error adding document", e);
            }
        });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L408-L426
```

### Dart

Use the`add()`method:  

```dart
// Add a new document with a generated id.
final data = {"name": "Tokyo", "country": "Japan"};

db.collection("cities").add(data).then((documentSnapshot) =>
    print("Added Data with ID: ${documentSnapshot.id}"));https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L210-L214
```

##### Java

Use the`add()`method:  

    // Add document data with auto-generated id.
    Map<String, Object> data = new HashMap<>();
    data.put("name", "Tokyo");
    data.put("country", "Japan");
    ApiFuture<DocumentReference> addedDocRef = db.collection("cities").add(data);
    System.out.println("Added document with ID: " + addedDocRef.get().getId());  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L135-L140

##### Python

Use the`add()`method:  

    city = {"name": "Tokyo", "country": "Japan"}
    update_time, city_ref = db.collection("cities").add(city)
    print(f"Added document with id {city_ref.id}")  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L194-L196

### Python

Use the`add()`method:  

    city = City(name="Tokyo", state=None, country="Japan")
    await db.collection("cities").add(city.to_dict())  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L190-L191

##### C++

Use the`Add()`method:  

```c++
db->Collection("cities").Add({/*some data*/});https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L235-L235
```

##### Node.js

Use the`add()`method:  

    // Add a new document with a generated id.
    const res = await db.collection('cities').add({
      name: 'Tokyo',
      country: 'Japan'
    });

    console.log('Added document with ID: ', res.id);  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L193-L199

##### Go

Use the`Add()`method:  


    import (
    	"context"
    	"log"

    	"cloud.google.com/go/firestore"
    )

    func addDocWithoutID(ctx context.Context, client *firestore.Client) error {
    	_, _, err := client.Collection("cities").Add(ctx, map[string]interface{}{
    		"name":    "Tokyo",
    		"country": "Japan",
    	})
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}

    	return err
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/save_data_set_id_random_collection.go#L18-L38

##### PHP

Use the`add()`method:

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $data = [
        'name' => 'Tokyo',
        'country' => 'Japan'
    ];
    $addedDocRef = $db->collection('samples/php/cities')->add($data);
    printf('Added document with ID: %s' . PHP_EOL, $addedDocRef->id());  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_set_id_random_collection.php#L40-L45

##### Unity

Use the`AddAsync()`method:  

```c#
Dictionary<string, object> city = new Dictionary<string, object>
{
	{ "Name", "Tokyo" },
	{ "Country", "Japan" }
};
db.Collection("cities").AddAsync(city).ContinueWithOnMainThread(task => {
	DocumentReference addedDocRef = task.Result;
	Debug.Log(String.Format("Added document with ID: {0}.", addedDocRef.Id));
});
```

##### C#

Use the`AddAsync()`method:  

    Dictionary<string, object> city = new Dictionary<string, object>
    {
        { "Name", "Tokyo" },
        { "Country", "Japan" }
    };
    DocumentReference addedDocRef = await db.Collection("cities").AddAsync(city);
    Console.WriteLine("Added document with ID: {0}.", addedDocRef.Id);  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/AddData/Program.cs#L154-L160

##### Ruby

Use the`add()`method:  

    data = {
      name:    "Tokyo",
      country: "Japan"
    }

    cities_ref = firestore.col collection_path

    added_doc_ref = cities_ref.add data
    puts "Added document with ID: #{added_doc_ref.document_id}."  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/add_data.rb#L98-L106

The examples show adding data to a top-level collection like`cities`.Cloud Firestorealso supports subcollections inside documents such as`cities/LA/landmarks`. The same`set()`,`add()`, and`update()`methods apply when working with subcollections.
| **Important:** Unlike "push IDs" in the Firebase Realtime Database,Cloud Firestoreauto-generated IDs don't provide any automatic ordering. If you want to order your documents by creation date, store a timestamp as a field in the documents.

In some cases, it can be useful to create a document reference with an auto-generated ID, then use the reference later. For this use case, you can call`doc()`in the following way:  

### Web

```javascript
import { collection, doc, setDoc } from "firebase/firestore"; 

// Add a new document with a generated id
const newCityRef = doc(collection(db, "cities"));

// later...
await setDoc(newCityRef, data);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/new_document.js#L8-L14
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
// Add a new document with a generated id.
var newCityRef = db.collection("cities").doc();

// later...
newCityRef.set(data);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L456-L460
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
let newCityRef = db.collection("cities").document()

// later...
newCityRef.setData([
  // ...
])https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L349-L356
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
FIRDocumentReference *newCityRef = [[self.db collectionWithPath:@"cities"] documentWithAutoID];
// later...
[newCityRef setData:@{ /* ... */ }];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L268-L270
```

### Kotlin

```kotlin
val data = HashMap<String, Any>()

val newCityRef = db.collection("cities").document()

// Later...
newCityRef.set(data)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L331-L336
```

### Java

```java
Map<String, Object> data = new HashMap<>();

DocumentReference newCityRef = db.collection("cities").document();

// Later...
newCityRef.set(data);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L432-L437
```

### Dart

```dart
// Add a new document with a generated id.
final data = <String, dynamic>{};

final newCityRef = db.collection("cities").doc();

// Later...
newCityRef.set(data);
https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L220-L227
```

##### Java

    // Add document data after generating an id.
    DocumentReference addedDocRef = db.collection("cities").document();
    System.out.println("Added document with ID: " + addedDocRef.getId());

    // later...
    ApiFuture<WriteResult> writeResult = addedDocRef.set(data);  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L155-L160

##### Python

    new_city_ref = db.collection("cities").document()

    # later...
    new_city_ref.set(
        {
            # ...
        }
    )  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L203-L210

### Python

    new_city_ref = db.collection("cities").document()

    # later...
    await new_city_ref.set(
        {
            # ...
        }
    )  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L198-L205

##### C++

```c++
DocumentReference new_city_ref = db->Collection("cities").Document();https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L243-L243
```

##### Node.js

    const newCityRef = db.collection('cities').doc();

    // Later...
    const res = await newCityRef.set({
      // ...
    });  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L215-L220

##### Go


    import (
    	"context"
    	"log"

    	"cloud.google.com/go/firestore"
    )

    func addDocAfterAutoGeneratedID(ctx context.Context, client *firestore.Client) error {
    	data := City{
    		Name:    "Sydney",
    		Country: "Australia",
    	}

    	ref := client.Collection("cities").NewDoc()

    	// later...
    	_, err := ref.Set(ctx, data)
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}

    	return err
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/save_data_set_id_random_document_ref.go#L18-L43

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $addedDocRef = $db->collection('samples/php/cities')->newDocument();
    printf('Added document with ID: %s' . PHP_EOL, $addedDocRef->id());
    $addedDocRef->set($data);  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_set_id_random_document_ref.php#L44-L46

##### Unity

```c#
DocumentReference addedDocRef = db.Collection("cities").Document();
Debug.Log(String.Format("Added document with ID: {0}.", addedDocRef.Id));
addedDocRef.SetAsync(city).ContinueWithOnMainThread(task => {
	Debug.Log(String.Format(
		"Added data to the {0} document in the cities collection.", addedDocRef.Id));
});
```

##### C#

    DocumentReference addedDocRef = db.Collection("cities").Document();
    Console.WriteLine("Added document with ID: {0}.", addedDocRef.Id);
    await addedDocRef.SetAsync(city);  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/AddData/Program.cs#L173-L175

##### Ruby

    cities_ref = firestore.col collection_path

    added_doc_ref = cities_ref.doc
    puts "Added document with ID: #{added_doc_ref.document_id}."

    added_doc_ref.set data  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/add_data.rb#L121-L126

In the backend,`.add(...)`and`.doc().set(...)`are equivalent, so you can use either option.

## Update a document

To update some fields of a document without overwriting the entire document, use the following language-specific`update()`methods:  

### Web

Use the`updateDoc()`method:  

```javascript
import { doc, updateDoc } from "firebase/firestore";

const washingtonRef = doc(db, "cities", "DC");

// Set the "capital" field of the city 'DC'
await updateDoc(washingtonRef, {
  capital: true
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/update_document.js#L8-L15
```

### Web

Use the`update()`method:  

```javascript
var washingtonRef = db.collection("cities").doc("DC");

// Set the "capital" field of the city 'DC'
return washingtonRef.update({
    capital: true
})
.then(() => {
    console.log("Document successfully updated!");
})
.catch((error) => {
    // The document probably doesn't exist.
    console.error("Error updating document: ", error);
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L467-L479
```

##### Swift

Use the`updateData()`method:  
**Note:**This product is not available on watchOS and App Clip targets.  

```swift
let washingtonRef = db.collection("cities").document("DC")

// Set the "capital" field of the city 'DC'
do {
  try await washingtonRef.updateData([
    "capital": true
  ])
  print("Document successfully updated")
} catch {
  print("Error updating document: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L362-L372
```

##### Objective-C

Use the`updateData:`method:  
**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
FIRDocumentReference *washingtonRef =
    [[self.db collectionWithPath:@"cities"] documentWithPath:@"DC"];
// Set the "capital" field of the city
[washingtonRef updateData:@{
  @"capital": @YES
} completion:^(NSError * _Nullable error) {
  if (error != nil) {
    NSLog(@"Error updating document: %@", error);
  } else {
    NSLog(@"Document successfully updated");
  }
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L276-L287
```

### Kotlin

Use the`update()`method:  

```kotlin
val washingtonRef = db.collection("cities").document("DC")

// Set the "isCapital" field of the city 'DC'
washingtonRef
    .update("capital", true)
    .addOnSuccessListener { Log.d(TAG, "DocumentSnapshot successfully updated!") }
    .addOnFailureListener { e -> Log.w(TAG, "Error updating document", e) }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L342-L348
```

### Java

Use the`update()`method:  

```java
DocumentReference washingtonRef = db.collection("cities").document("DC");

// Set the "isCapital" field of the city 'DC'
washingtonRef
        .update("capital", true)
        .addOnSuccessListener(new OnSuccessListener<Void>() {
            @Override
            public void onSuccess(Void aVoid) {
                Log.d(TAG, "DocumentSnapshot successfully updated!");
            }
        })
        .addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception e) {
                Log.w(TAG, "Error updating document", e);
            }
        });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L443-L459
```

### Dart

Use the`update()`method:  

```dart
final washingtonRef = db.collection("cites").doc("DC");
washingtonRef.update({"capital": true}).then(
    (value) => print("DocumentSnapshot successfully updated!"),
    onError: (e) => print("Error updating document $e"));https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L233-L236
```

##### Java

Use the`update()`method:  

    // Update an existing document
    DocumentReference docRef = db.collection("cities").document("DC");

    // (async) Update one field
    ApiFuture<WriteResult> future = docRef.update("capital", true);

    // ...
    WriteResult result = future.get();
    System.out.println("Write result: " + result);  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L172-L180

##### Python

Use the`update()`method:  

    city_ref = db.collection("cities").document("DC")

    # Set the capital field
    city_ref.update({"capital": True})  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L318-L321

### Python

Use the`update()`method:  

    city_ref = db.collection("cities").document("DC")

    # Set the capital field
    await city_ref.update({"capital": True})  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L312-L315

##### C++

Use the`Update()`method:  

```c++
DocumentReference washington_ref = db->Collection("cities").Document("DC");
// Set the "capital" field of the city "DC".
washington_ref.Update({{"capital", FieldValue::Boolean(true)}});https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L258-L260
```

##### Node.js

Use the`update()`method:  

    const cityRef = db.collection('cities').doc('DC');

    // Set the 'capital' field of the city
    const res = await cityRef.update({capital: true});  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L227-L230

##### Go

Use the`Update()`method:  


    import (
    	"context"
    	"log"

    	"cloud.google.com/go/firestore"
    )

    func updateDoc(ctx context.Context, client *firestore.Client) error {
    	// ...

    	_, err := client.Collection("cities").Doc("DC").Update(ctx, []firestore.Update{
    		{
    			Path:  "capital",
    			Value: true,
    		},
    	})
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}

    	return err
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/save_data_set_field.go#L18-L51

##### PHP

Use the`update()`method:

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $cityRef = $db->collection('samples/php/cities')->document('DC');
    $cityRef->update([
        ['path' => 'capital', 'value' => true]
    ]);  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_set_field.php#L40-L43

##### Unity

Use the`UpdateAsync()`method:  

```c#
DocumentReference cityRef = db.Collection("cities").Document("new-city-id");
Dictionary<string, object> updates = new Dictionary<string, object>
{
	{ "Capital", false }
};

cityRef.UpdateAsync(updates).ContinueWithOnMainThread(task => {
	Debug.Log(
		"Updated the Capital field of the new-city-id document in the cities collection.");
});
// You can also update a single field with: cityRef.UpdateAsync("Capital", false);
```

##### C#

Use the`UpdateAsync()`method:  

    DocumentReference cityRef = db.Collection("cities").Document("new-city-id");
    Dictionary<string, object> updates = new Dictionary<string, object>
    {
        { "Capital", false }
    };
    await cityRef.UpdateAsync(updates);

    // You can also update a single field with: await cityRef.UpdateAsync("Capital", false);  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/AddData/Program.cs#L184-L191

##### Ruby

Use the`update()`method:  

    city_ref = firestore.doc "#{collection_path}/DC"
    city_ref.update({ capital: true })  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/add_data.rb#L145-L146

### Server Timestamp

You can set a field in your document to a server timestamp which tracks when the server receives the update.  

### Web

```javascript
import { updateDoc, serverTimestamp } from "firebase/firestore";

const docRef = doc(db, 'objects', 'some-id');

// Update the timestamp field with the value from the server
const updateTimestamp = await updateDoc(docRef, {
    timestamp: serverTimestamp()
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/update_with_server_timestamp.js#L8-L15
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
var docRef = db.collection('objects').doc('some-id');

// Update the timestamp field with the value from the server
var updateTimestamp = docRef.update({
    timestamp: firebase.firestore.FieldValue.serverTimestamp()
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L773-L778
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
do {
  try await db.collection("objects").document("some-id").updateData([
    "lastUpdated": FieldValue.serverTimestamp(),
  ])
  print("Document successfully updated")
} catch {
  print("Error updating document: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L495-L502
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
[[[self.db collectionWithPath:@"objects"] documentWithPath:@"some-id"] updateData:@{
  @"lastUpdated": [FIRFieldValue fieldValueForServerTimestamp]
} completion:^(NSError * _Nullable error) {
  if (error != nil) {
    NSLog(@"Error updating document: %@", error);
  } else {
    NSLog(@"Document successfully updated");
  }
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L428-L436
```

### Kotlin

```kotlin
// If you're using custom Kotlin objects in Android, add an @ServerTimestamp
// annotation to a Date field for your custom object classes. This indicates
// that the Date field should be treated as a server timestamp by the object mapper.
val docRef = db.collection("objects").document("some-id")

// Update the timestamp field with the value from the server
val updates = hashMapOf<String, Any>(
    "timestamp" to FieldValue.serverTimestamp(),
)

docRef.update(updates).addOnCompleteListener { }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1090-L1097
```

### Java

```java
// If you're using custom Java objects in Android, add an @ServerTimestamp
// annotation to a Date field for your custom object classes. This indicates
// that the Date field should be treated as a server timestamp by the object mapper.
DocumentReference docRef = db.collection("objects").document("some-id");

// Update the timestamp field with the value from the server
Map<String,Object> updates = new HashMap<>();
updates.put("timestamp", FieldValue.serverTimestamp());

docRef.update(updates).addOnCompleteListener(new OnCompleteListener<Void>() {
    // ...
    // ...  
https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1304-L1315
```

### Dart

```dart
final docRef = db.collection("objects").doc("some-id");
final updates = <String, dynamic>{
  "timestamp": FieldValue.serverTimestamp(),
};

docRef.update(updates).then(
    (value) => print("DocumentSnapshot successfully updated!"),
    onError: (e) => print("Error updating document $e"));https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L242-L249
```

##### Java

    DocumentReference docRef = db.collection("objects").document("some-id");
    // Update the timestamp field with the value from the server
    ApiFuture<WriteResult> writeResult = docRef.update("timestamp", FieldValue.serverTimestamp());
    System.out.println("Update time : " + writeResult.get());  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L255-L258

##### Python

    city_ref = db.collection("objects").document("some-id")
    city_ref.update({"timestamp": firestore.SERVER_TIMESTAMP})  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L387-L388

### Python

    city_ref = db.collection("objects").document("some-id")
    await city_ref.update({"timestamp": firestore.SERVER_TIMESTAMP})  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L381-L382

##### C++

```c++
DocumentReference doc_ref = db->Collection("objects").Document("some-id");
doc_ref.Update({{"timestamp", FieldValue::ServerTimestamp()}})
    .OnCompletion([](const Future<void>& future) {
      // ...
    });https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L266-L270
```

##### Node.js

    // Create a document reference
    const docRef = db.collection('objects').doc('some-id');

    // Update the timestamp field with the value from the server
    const res = await docRef.update({
      timestamp: FieldValue.serverTimestamp()
    });  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L309-L315

##### Go


    import (
    	"context"
    	"log"

    	"cloud.google.com/go/firestore"
    )

    func updateDocServerTimestamp(ctx context.Context, client *firestore.Client) error {
    	// ...

    	_, err := client.Collection("objects").Doc("some-id").Set(ctx, map[string]interface{}{
    		"timestamp": firestore.ServerTimestamp,
    	}, firestore.MergeAll)
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}

    	return err
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/save_data_set_server_timestamp.go#L18-L47

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $docRef = $db->collection('samples/php/objects')->document('some-id');
    $docRef->update([
        ['path' => 'timestamp', 'value' => FieldValue::serverTimestamp()]
    ]);  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_set_server_timestamp.php#L45-L48

##### Unity

```c#
DocumentReference cityRef = db.Collection("cities").Document("new-city-id");
cityRef.UpdateAsync("Timestamp", FieldValue.ServerTimestamp)
	.ContinueWithOnMainThread(task => {
		Debug.Log(
			"Updated the Timestamp field of the new-city-id document in the cities "
			+ "collection.");
	});
```

##### C#

    DocumentReference cityRef = db.Collection("cities").Document("new-city-id");
    await cityRef.UpdateAsync("Timestamp", Timestamp.GetCurrentTimestamp());  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/AddData/Program.cs#L233-L234

##### Ruby

    city_ref = firestore.doc "#{collection_path}/new-city-id"
    city_ref.update({ timestamp: firestore.field_server_time })  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/add_data.rb#L218-L219

When updating multiple timestamp fields inside of a[transaction](https://firebase.google.com/docs/firestore/manage-data/transactions), each field receives the same server timestamp value.

### Update fields in nested objects

If your document contains nested objects, you can use the*dot notation* to reference nested fields within the document when you call`update()`:  

### Web

```javascript
import { doc, setDoc, updateDoc } from "firebase/firestore"; 

// Create an initial document to update.
const frankDocRef = doc(db, "users", "frank");
await setDoc(frankDocRef, {
    name: "Frank",
    favorites: { food: "Pizza", color: "Blue", subject: "recess" },
    age: 12
});

// To update age and favorite color:
await updateDoc(frankDocRef, {
    "age": 13,
    "favorites.color": "Red"
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/update_document_nested.js#L8-L22
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
// Create an initial document to update.
var frankDocRef = db.collection("users").doc("frank");
frankDocRef.set({
    name: "Frank",
    favorites: { food: "Pizza", color: "Blue", subject: "recess" },
    age: 12
});

// To update age and favorite color:
db.collection("users").doc("frank").update({
    "age": 13,
    "favorites.color": "Red"
})
.then(() => {
    console.log("Document successfully updated!");
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L329-L344
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
// Create an initial document to update.
let frankDocRef = db.collection("users").document("frank")
do {
  try await frankDocRef.setData([
    "name": "Frank",
    "favorites": [ "food": "Pizza", "color": "Blue", "subject": "recess" ],
    "age": 12
  ])

  // To update age and favorite color:
  try await frankDocRef.updateData([
    "age": 13,
    "favorites.color": "Red"
  ])
  print("Document successfully updated")
} catch {
  print("Error updating document: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L413-L430
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
// Create an initial document to update.
FIRDocumentReference *frankDocRef =
    [[self.db collectionWithPath:@"users"] documentWithPath:@"frank"];
[frankDocRef setData:@{
  @"name": @"Frank",
  @"favorites": @{
    @"food": @"Pizza",
    @"color": @"Blue",
    @"subject": @"recess"
  },
  @"age": @12
}];
// To update age and favorite color:
[frankDocRef updateData:@{
  @"age": @13,
  @"favorites.color": @"Red",
} completion:^(NSError * _Nullable error) {
  if (error != nil) {
    NSLog(@"Error updating document: %@", error);
  } else {
    NSLog(@"Document successfully updated");
  }
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L336-L358
```

### Kotlin

```kotlin
// Assume the document contains:
// {
//   name: "Frank",
//   favorites: { food: "Pizza", color: "Blue", subject: "recess" }
//   age: 12
// }
//
// To update age and favorite color:
db.collection("users").document("frank")
    .update(
        mapOf(
            "age" to 13,
            "favorites.color" to "Red",
        ),
    )https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L375-L389
```

### Java

```java
// Assume the document contains:
// {
//   name: "Frank",
//   favorites: { food: "Pizza", color: "Blue", subject: "recess" }
//   age: 12
// }
//
// To update age and favorite color:
db.collection("users").document("frank")
        .update(
                "age", 13,
                "favorites.color", "Red"
        );https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L486-L498
```

### Dart

```dart
// Assume the document contains:
// {
//   name: "Frank",
//   favorites: { food: "Pizza", color: "Blue", subject: "recess" }
//   age: 12
// }
db
    .collection("users")
    .doc("frank")
    .update({"age": 13, "favorites.color": "Red"});https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L255-L264
```

##### Java

    // Create an initial document to update
    DocumentReference frankDocRef = db.collection("users").document("frank");
    Map<String, Object> initialData = new HashMap<>();
    initialData.put("name", "Frank");
    initialData.put("age", 12);

    Map<String, Object> favorites = new HashMap<>();
    favorites.put("food", "Pizza");
    favorites.put("color", "Blue");
    favorites.put("subject", "Recess");
    initialData.put("favorites", favorites);

    ApiFuture<WriteResult> initialResult = frankDocRef.set(initialData);
    // Confirm that data has been successfully saved by blocking on the operation
    initialResult.get();

    // Update age and favorite color
    Map<String, Object> updates = new HashMap<>();
    updates.put("age", 13);
    updates.put("favorites.color", "Red");

    // Async update document
    ApiFuture<WriteResult> writeResult = frankDocRef.update(updates);
    // ...
    System.out.println("Update time : " + writeResult.get().getUpdateTime());  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L221-L245

##### Python

    # Create an initial document to update
    frank_ref = db.collection("users").document("frank")
    frank_ref.set(
        {
            "name": "Frank",
            "favorites": {"food": "Pizza", "color": "Blue", "subject": "Recess"},
            "age": 12,
        }
    )

    # Update age and favorite color
    frank_ref.update({"age": 13, "favorites.color": "Red"})  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L369-L380

### Python

    # Create an initial document to update
    frank_ref = db.collection("users").document("frank")
    await frank_ref.set(
        {
            "name": "Frank",
            "favorites": {"food": "Pizza", "color": "Blue", "subject": "Recess"},
            "age": 12,
        }
    )

    # Update age and favorite color
    await frank_ref.update({"age": 13, "favorites.color": "Red"})  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L363-L374

##### C++

```c++
// Assume the document contains:
// {
//   name: "Frank",
//   favorites: { food: "Pizza", color: "Blue", subject: "recess" }
//   age: 12
// }
//
// To update age and favorite color:
db->Collection("users").Document("frank").Update({
    {"age", FieldValue::Integer(13)},
    {"favorites.color", FieldValue::String("red")},
});https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L282-L293
```

##### Node.js

    const initialData = {
      name: 'Frank',
      age: 12,
      favorites: {
        food: 'Pizza',
        color: 'Blue',
        subject: 'recess'
      }
    };

    // ...
    const res = await db.collection('users').doc('Frank').update({
      age: 13,
      'favorites.color': 'Red'
    });  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L338-L354

##### Go


    import (
    	"context"
    	"log"

    	"cloud.google.com/go/firestore"
    )

    func updateDocNested(ctx context.Context, client *firestore.Client) error {
    	initialData := map[string]interface{}{
    		"name": "Frank",
    		"age":  12,
    		"favorites": map[string]interface{}{
    			"food":    "Pizza",
    			"color":   "Blue",
    			"subject": "recess",
    		},
    	}

    	// ...

    	_, err := client.Collection("users").Doc("frank").Set(ctx, map[string]interface{}{
    		"age": 13,
    		"favorites": map[string]interface{}{
    			"color": "Red",
    		},
    	}, firestore.MergeAll)
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}

    	return err
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/save_data_set_nested_fields.go#L18-L57

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    // Create an initial document to update
    $frankRef = $db->collection('samples/php/users')->document('frank');
    $frankRef->set([
        'first' => 'Frank',
        'last' => 'Franklin',
        'favorites' => ['food' => 'Pizza', 'color' => 'Blue', 'subject' => 'Recess'],
        'age' => 12
    ]);

    // Update age and favorite color
    $frankRef->update([
        ['path' => 'age', 'value' => 13],
        ['path' => 'favorites.color', 'value' => 'Red']
    ]);  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_set_nested_fields.php#L40-L53

##### Unity

```c#
DocumentReference frankDocRef = db.Collection("users").Document("frank");
Dictionary<string, object> initialData = new Dictionary<string, object>
{
	{ "Name", "Frank" },
	{ "Age", 12 }
};

Dictionary<string, object> favorites = new Dictionary<string, object>
{
	{ "Food", "Pizza" },
	{ "Color", "Blue" },
	{ "Subject", "Recess" },
};
initialData.Add("Favorites", favorites);
frankDocRef.SetAsync(initialData).ContinueWithOnMainThread(task => {

	// Update age and favorite color
	Dictionary<string, object> updates = new Dictionary<string, object>
	{
		{ "Age", 13 },
		{ "Favorites.Color", "Red" },
	};

	// Asynchronously update the document
	return frankDocRef.UpdateAsync(updates);
}).ContinueWithOnMainThread(task => {
	Debug.Log(
		"Updated the age and favorite color fields of the Frank document in "
		+ "the users collection.");
});
```

##### C#

    DocumentReference frankDocRef = db.Collection("users").Document("frank");
    Dictionary<string, object> initialData = new Dictionary<string, object>
    {
        { "Name", "Frank" },
        { "Age", 12 }
    };

    Dictionary<string, object> favorites = new Dictionary<string, object>
    {
        { "Food", "Pizza" },
        { "Color", "Blue" },
        { "Subject", "Recess" },
    };
    initialData.Add("Favorites", favorites);
    await frankDocRef.SetAsync(initialData);

    // Update age and favorite color
    Dictionary<string, object> updates = new Dictionary<string, object>
    {
        { "Age", 13 },
        { "Favorites.Color", "Red" },
    };

    // Asynchronously update the document
    await frankDocRef.UpdateAsync(updates);  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/AddData/Program.cs#L200-L224

##### Ruby

    # Create an initial document to update
    frank_ref = firestore.doc "#{collection_path}/frank"
    frank_ref.set(
      {
        name:      "Frank",
        favorites: {
          food:    "Pizza",
          color:   "Blue",
          subject: "Recess"
        },
        age:       12
      }
    )

    # Update age and favorite color
    frank_ref.update({ age: 13, "favorites.color": "Red" })  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/add_data.rb#L183-L198

Dot notation allows you to update a single nested field without overwriting other nested fields. If you update a nested field without dot notation, you will overwrite the entire map field, as shown in the following example:  

##### Web

```scilab
// Create our initial doc
db.collection("users").doc("frank").set({
  name: "Frank",
  favorites: {
    food: "Pizza",
    color: "Blue",
    subject: "Recess"
  },
  age: 12
}).then(function() {
  console.log("Frank created");
});

// Update the doc without using dot notation.
// Notice the map value for favorites.
db.collection("users").doc("frank").update({
  favorites: {
    food: "Ice Cream"
  }
}).then(function() {
  console.log("Frank food updated");
});

/*
Ending State, favorite.color and favorite.subject are no longer present:
/users
    /frank
        {
            name: "Frank",
            favorites: {
                food: "Ice Cream",
            },
            age: 12
        }
 */
```

### Update elements in an array

If your document contains an array field, you can use`arrayUnion()`and`arrayRemove()`to add and remove elements.`arrayUnion()`adds elements to an array but only elements not already present.`arrayRemove()`removes all instances of each given element.  

### Web

```javascript
import { doc, updateDoc, arrayUnion, arrayRemove } from "firebase/firestore";

const washingtonRef = doc(db, "cities", "DC");

// Atomically add a new region to the "regions" array field.
await updateDoc(washingtonRef, {
    regions: arrayUnion("greater_virginia")
});

// Atomically remove a region from the "regions" array field.
await updateDoc(washingtonRef, {
    regions: arrayRemove("east_coast")
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/update_document_array.js#L8-L20
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
var washingtonRef = db.collection("cities").doc("DC");

// Atomically add a new region to the "regions" array field.
washingtonRef.update({
    regions: firebase.firestore.FieldValue.arrayUnion("greater_virginia")
});

// Atomically remove a region from the "regions" array field.
washingtonRef.update({
    regions: firebase.firestore.FieldValue.arrayRemove("east_coast")
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L485-L495
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
let washingtonRef = db.collection("cities").document("DC")

// Atomically add a new region to the "regions" array field.
washingtonRef.updateData([
  "regions": FieldValue.arrayUnion(["greater_virginia"])
])

// Atomically remove a region from the "regions" array field.
washingtonRef.updateData([
  "regions": FieldValue.arrayRemove(["east_coast"])
])https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L378-L388
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
FIRDocumentReference *washingtonRef =
    [[self.db collectionWithPath:@"cities"] documentWithPath:@"DC"];

// Atomically add a new region to the "regions" array field.
[washingtonRef updateData:@{
  @"regions": [FIRFieldValue fieldValueForArrayUnion:@[@"greater_virginia"]]
}];

// Atomically remove a new region to the "regions" array field.
[washingtonRef updateData:@{
  @"regions": [FIRFieldValue fieldValueForArrayRemove:@[@"east_coast"]]
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L293-L304
```

### Kotlin

```kotlin
val washingtonRef = db.collection("cities").document("DC")

// Atomically add a new region to the "regions" array field.
washingtonRef.update("regions", FieldValue.arrayUnion("greater_virginia"))

// Atomically remove a region from the "regions" array field.
washingtonRef.update("regions", FieldValue.arrayRemove("east_coast"))https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L354-L360
```

### Java

```java
DocumentReference washingtonRef = db.collection("cities").document("DC");

// Atomically add a new region to the "regions" array field.
washingtonRef.update("regions", FieldValue.arrayUnion("greater_virginia"));

// Atomically remove a region from the "regions" array field.
washingtonRef.update("regions", FieldValue.arrayRemove("east_coast"));https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L465-L471
```

### Dart

```dart
final washingtonRef = db.collection("cities").doc("DC");

// Atomically add a new region to the "regions" array field.
washingtonRef.update({
  "regions": FieldValue.arrayUnion(["greater_virginia"]),
});

// Atomically remove a region from the "regions" array field.
washingtonRef.update({
  "regions": FieldValue.arrayRemove(["east_coast"]),
});https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L270-L280
```

##### Java

    DocumentReference washingtonRef = db.collection("cities").document("DC");

    // Atomically add a new region to the "regions" array field.
    ApiFuture<WriteResult> arrayUnion =
        washingtonRef.update("regions", FieldValue.arrayUnion("greater_virginia"));
    System.out.println("Update time : " + arrayUnion.get());

    // Atomically remove a region from the "regions" array field.
    ApiFuture<WriteResult> arrayRm =
        washingtonRef.update("regions", FieldValue.arrayRemove("east_coast"));
    System.out.println("Update time : " + arrayRm.get());  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L265-L275

##### Python

    city_ref = db.collection("cities").document("DC")

    # Atomically add a new region to the 'regions' array field.
    city_ref.update({"regions": firestore.ArrayUnion(["greater_virginia"])})

    # // Atomically remove a region from the 'regions' array field.
    city_ref.update({"regions": firestore.ArrayRemove(["east_coast"])})  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L332-L338

### Python

    city_ref = db.collection("cities").document("DC")

    # Atomically add a new region to the 'regions' array field.
    await city_ref.update({"regions": firestore.ArrayUnion(["greater_virginia"])})

    # // Atomically remove a region from the 'regions' array field.
    await city_ref.update({"regions": firestore.ArrayRemove(["east_coast"])})  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L326-L332

##### C++

```c++
// This is not yet supported.
```

##### Node.js

    // ...
    const washingtonRef = db.collection('cities').doc('DC');

    // Atomically add a new region to the "regions" array field.
    const unionRes = await washingtonRef.update({
      regions: FieldValue.arrayUnion('greater_virginia')
    });
    // Atomically remove a region from the "regions" array field.
    const removeRes = await washingtonRef.update({
      regions: FieldValue.arrayRemove('east_coast')
    });

    // To add or remove multiple items, pass multiple arguments to arrayUnion/arrayRemove
    const multipleUnionRes = await washingtonRef.update({
      regions: FieldValue.arrayUnion('south_carolina', 'texas')
      // Alternatively, you can use spread operator in ES6 syntax
      // const newRegions = ['south_carolina', 'texas']
      // regions: FieldValue.arrayUnion(...newRegions)
    });  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L238-L256

##### Go

```go
// Not supported yet
```

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $cityRef = $db->collection('samples/php/cities')->document('DC');

    // Atomically add a new region to the "regions" array field.
    $cityRef->update([
        ['path' => 'regions', 'value' => FieldValue::arrayUnion(['greater_virginia'])]
    ]);

    // Atomically remove a region from the "regions" array field.
    $cityRef->update([
        ['path' => 'regions', 'value' => FieldValue::arrayRemove(['east_coast'])]
    ]);  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_set_array_operations.php#L41-L51

##### Unity

```c#
// This is not yet supported in the Unity SDK
  
```

##### C#

    DocumentReference washingtonRef = db.Collection("cities").Document("DC");

    // Atomically add a new region to the "regions" array field.
    await washingtonRef.UpdateAsync("Regions", FieldValue.ArrayUnion("greater_virginia"));

    // Atomically remove a region from the "regions" array field.
    await washingtonRef.UpdateAsync("Regions", FieldValue.ArrayRemove("east_coast"));  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/AddData/Program.cs#L243-L249

##### Ruby

```ruby
// Not supported yet
```

### Increment a numeric value

You can increment or decrement a numeric field value as shown in the following example. An increment operation increases or decreases the current value of a field by the given amount.
**Note:**If the field doesn't exist or if the current field value is not a numeric value, the operation sets the field to the given value.  

### Web

```javascript
import { doc, updateDoc, increment } from "firebase/firestore";

const washingtonRef = doc(db, "cities", "DC");

// Atomically increment the population of the city by 50.
await updateDoc(washingtonRef, {
    population: increment(50)
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/update_document_increment.js#L8-L15
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
var washingtonRef = db.collection('cities').doc('DC');

// Atomically increment the population of the city by 50.
washingtonRef.update({
    population: firebase.firestore.FieldValue.increment(50)
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L501-L506
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
let washingtonRef = db.collection("cities").document("DC")

// Atomically increment the population of the city by 50.
// Note that increment() with no arguments increments by 1.
washingtonRef.updateData([
  "population": FieldValue.increment(Int64(50))
])https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L394-L400
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
FIRDocumentReference *washingtonRef =
    [[self.db collectionWithPath:@"cities"] documentWithPath:@"DC"];

// Atomically increment the population of the city by 50.
// Note that increment() with no arguments increments by 1.
[washingtonRef updateData:@{
  @"population": [FIRFieldValue fieldValueForIntegerIncrement:50]
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L310-L317
```

### Kotlin

```kotlin
val washingtonRef = db.collection("cities").document("DC")

// Atomically increment the population of the city by 50.
washingtonRef.update("population", FieldValue.increment(50))https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L366-L369
```

### Java

```java
DocumentReference washingtonRef = db.collection("cities").document("DC");

// Atomically increment the population of the city by 50.
washingtonRef.update("population", FieldValue.increment(50));https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L477-L480
```

### Dart

```dart
var washingtonRef = db.collection('cities').doc('DC');

// Atomically increment the population of the city by 50.
washingtonRef.update(
  {"population": FieldValue.increment(50)},
);https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L286-L291
```

##### Java

    DocumentReference washingtonRef = db.collection("cities").document("DC");

    // Atomically increment the population of the city by 50.
    final ApiFuture<WriteResult> updateFuture =
        washingtonRef.update("population", FieldValue.increment(50));  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L430-L434

##### Python

    washington_ref = db.collection("cities").document("DC")

    washington_ref.update({"population": firestore.Increment(50)})  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L957-L959

### Python

    washington_ref = db.collection("cities").document("DC")

    await washington_ref.update({"population": firestore.Increment(50)})  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L789-L791

##### C++

```c++
// This is not yet supported.
```

##### Node.js

    // ...
    const washingtonRef = db.collection('cities').doc('DC');

    // Atomically increment the population of the city by 50.
    const res = await washingtonRef.update({
      population: FieldValue.increment(50)
    });  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L264-L270

##### Go

    import (
    	"context"
    	"fmt"

    	"cloud.google.com/go/firestore"
    )

    // updateDocumentIncrement increments the population of the city document in the
    // cities collection by 50.
    func updateDocumentIncrement(projectID, city string) error {
    	// projectID := "my-project"

    	ctx := context.Background()

    	client, err := firestore.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("firestore.NewClient: %w", err)
    	}
    	defer client.Close()

    	dc := client.Collection("cities").Doc(city)
    	_, err = dc.Update(ctx, []firestore.Update{
    		{Path: "population", Value: firestore.Increment(50)},
    	})
    	if err != nil {
    		return fmt.Errorf("Update: %w", err)
    	}

    	return nil
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/increment.go#L18-L48

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $cityRef = $db->collection('samples/php/cities')->document('DC');

    // Atomically increment the population of the city by 50.
    $cityRef->update([
        ['path' => 'regions', 'value' => FieldValue::increment(50)]
    ]);  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_set_numeric_increment.php#L41-L46

##### Unity

```c#
// This is not yet supported in the Unity SDK.
  
```

##### C#

    DocumentReference washingtonRef = db.Collection("cities").Document("DC");

    // Atomically increment the population of the city by 50.
    await washingtonRef.UpdateAsync("Regions", FieldValue.Increment(50));  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/AddData/Program.cs#L258-L261

##### Ruby

    city_ref = firestore.doc "#{collection_path}/DC"
    city_ref.update({ population: firestore.field_increment(50) })  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/add_data.rb#L239-L240

Increment operations are useful for implementing counters. Note that updating a single document too quickly can[lead to contention or errors](https://firebase.google.com/docs/firestore/best-practices#updates_to_a_single_document). If you need to update your counter at a very high rate, see the[Distributed counters](https://firebase.google.com/docs/firestore/solutions/counters)page.