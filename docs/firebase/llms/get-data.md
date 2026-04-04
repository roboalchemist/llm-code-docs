# Source: https://firebase.google.com/docs/firestore/query-data/get-data.md.txt

<br />

There are three ways to retrieve data stored inCloud Firestore. Any of these methods can be used with documents, collections of documents, or the results of queries:

- Call a method to get the data once.
- Set a listener to receive data-change events.
- Bulk-load Firestore snapshot data from an external source via[data bundles](https://firebase.google.com/docs/firestore/bundles). See the bundles doc for more details.

When you set a listener,Cloud Firestoresends your listener an initial snapshot of the data, and then another snapshot each time the document changes.
| **Note:** While the code samples cover multiple languages, the text explaining the samples refers to the Web method names.

## Before you begin

See[Get started withCloud Firestore](https://firebase.google.com/docs/firestore/quickstart)to create aCloud Firestoredatabase.

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

## Example data

To get started, write some data about cities so we can look at different ways to read it back:  

### Web

```javascript
import { collection, doc, setDoc } from "firebase/firestore"; 

const citiesRef = collection(db, "cities");

await setDoc(doc(citiesRef, "SF"), {
    name: "San Francisco", state: "CA", country: "USA",
    capital: false, population: 860000,
    regions: ["west_coast", "norcal"] });
await setDoc(doc(citiesRef, "LA"), {
    name: "Los Angeles", state: "CA", country: "USA",
    capital: false, population: 3900000,
    regions: ["west_coast", "socal"] });
await setDoc(doc(citiesRef, "DC"), {
    name: "Washington, D.C.", state: null, country: "USA",
    capital: true, population: 680000,
    regions: ["east_coast"] });
await setDoc(doc(citiesRef, "TOK"), {
    name: "Tokyo", state: null, country: "Japan",
    capital: true, population: 9000000,
    regions: ["kanto", "honshu"] });
await setDoc(doc(citiesRef, "BJ"), {
    name: "Beijing", state: null, country: "China",
    capital: true, population: 21500000,
    regions: ["jingjinji", "hebei"] });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/example_data.js#L8-L31
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
var citiesRef = db.collection("cities");

citiesRef.doc("SF").set({
    name: "San Francisco", state: "CA", country: "USA",
    capital: false, population: 860000,
    regions: ["west_coast", "norcal"] });
citiesRef.doc("LA").set({
    name: "Los Angeles", state: "CA", country: "USA",
    capital: false, population: 3900000,
    regions: ["west_coast", "socal"] });
citiesRef.doc("DC").set({
    name: "Washington, D.C.", state: null, country: "USA",
    capital: true, population: 680000,
    regions: ["east_coast"] });
citiesRef.doc("TOK").set({
    name: "Tokyo", state: null, country: "Japan",
    capital: true, population: 9000000,
    regions: ["kanto", "honshu"] });
citiesRef.doc("BJ").set({
    name: "Beijing", state: null, country: "China",
    capital: true, population: 21500000,
    regions: ["jingjinji", "hebei"] });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L402-L423
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
let citiesRef = db.collection("cities")

citiesRef.document("SF").setData([
  "name": "San Francisco",
  "state": "CA",
  "country": "USA",
  "capital": false,
  "population": 860000,
  "regions": ["west_coast", "norcal"]
])
citiesRef.document("LA").setData([
  "name": "Los Angeles",
  "state": "CA",
  "country": "USA",
  "capital": false,
  "population": 3900000,
  "regions": ["west_coast", "socal"]
])
citiesRef.document("DC").setData([
  "name": "Washington D.C.",
  "country": "USA",
  "capital": true,
  "population": 680000,
  "regions": ["east_coast"]
])
citiesRef.document("TOK").setData([
  "name": "Tokyo",
  "country": "Japan",
  "capital": true,
  "population": 9000000,
  "regions": ["kanto", "honshu"]
])
citiesRef.document("BJ").setData([
  "name": "Beijing",
  "country": "China",
  "capital": true,
  "population": 21500000,
  "regions": ["jingjinji", "hebei"]
])https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L642-L680
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
FIRCollectionReference *citiesRef = [self.db collectionWithPath:@"cities"];
[[citiesRef documentWithPath:@"SF"] setData:@{
  @"name": @"San Francisco",
  @"state": @"CA",
  @"country": @"USA",
  @"capital": @(NO),
  @"population": @860000,
  @"regions": @[@"west_coast", @"norcal"]
}];
[[citiesRef documentWithPath:@"LA"] setData:@{
  @"name": @"Los Angeles",
  @"state": @"CA",
  @"country": @"USA",
  @"capital": @(NO),
  @"population": @3900000,
  @"regions": @[@"west_coast", @"socal"]
}];
[[citiesRef documentWithPath:@"DC"] setData:@{
  @"name": @"Washington D.C.",
  @"country": @"USA",
  @"capital": @(YES),
  @"population": @680000,
  @"regions": @[@"east_coast"]
}];
[[citiesRef documentWithPath:@"TOK"] setData:@{
  @"name": @"Tokyo",
  @"country": @"Japan",
  @"capital": @(YES),
  @"population": @9000000,
  @"regions": @[@"kanto", @"honshu"]
}];
[[citiesRef documentWithPath:@"BJ"] setData:@{
  @"name": @"Beijing",
  @"country": @"China",
  @"capital": @(YES),
  @"population": @21500000,
  @"regions": @[@"jingjinji", @"hebei"]
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L566-L603
```

### Kotlin

```kotlin
val cities = db.collection("cities")

val data1 = hashMapOf(
    "name" to "San Francisco",
    "state" to "CA",
    "country" to "USA",
    "capital" to false,
    "population" to 860000,
    "regions" to listOf("west_coast", "norcal"),
)
cities.document("SF").set(data1)

val data2 = hashMapOf(
    "name" to "Los Angeles",
    "state" to "CA",
    "country" to "USA",
    "capital" to false,
    "population" to 3900000,
    "regions" to listOf("west_coast", "socal"),
)
cities.document("LA").set(data2)

val data3 = hashMapOf(
    "name" to "Washington D.C.",
    "state" to null,
    "country" to "USA",
    "capital" to true,
    "population" to 680000,
    "regions" to listOf("east_coast"),
)
cities.document("DC").set(data3)

val data4 = hashMapOf(
    "name" to "Tokyo",
    "state" to null,
    "country" to "Japan",
    "capital" to true,
    "population" to 9000000,
    "regions" to listOf("kanto", "honshu"),
)
cities.document("TOK").set(data4)

val data5 = hashMapOf(
    "name" to "Beijing",
    "state" to null,
    "country" to "China",
    "capital" to true,
    "population" to 21500000,
    "regions" to listOf("jingjinji", "hebei"),
)
cities.document("BJ").set(data5)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L722-L772
```

### Java

```java
CollectionReference cities = db.collection("cities");

Map<String, Object> data1 = new HashMap<>();
data1.put("name", "San Francisco");
data1.put("state", "CA");
data1.put("country", "USA");
data1.put("capital", false);
data1.put("population", 860000);
data1.put("regions", Arrays.asList("west_coast", "norcal"));
cities.document("SF").set(data1);

Map<String, Object> data2 = new HashMap<>();
data2.put("name", "Los Angeles");
data2.put("state", "CA");
data2.put("country", "USA");
data2.put("capital", false);
data2.put("population", 3900000);
data2.put("regions", Arrays.asList("west_coast", "socal"));
cities.document("LA").set(data2);

Map<String, Object> data3 = new HashMap<>();
data3.put("name", "Washington D.C.");
data3.put("state", null);
data3.put("country", "USA");
data3.put("capital", true);
data3.put("population", 680000);
data3.put("regions", Arrays.asList("east_coast"));
cities.document("DC").set(data3);

Map<String, Object> data4 = new HashMap<>();
data4.put("name", "Tokyo");
data4.put("state", null);
data4.put("country", "Japan");
data4.put("capital", true);
data4.put("population", 9000000);
data4.put("regions", Arrays.asList("kanto", "honshu"));
cities.document("TOK").set(data4);

Map<String, Object> data5 = new HashMap<>();
data5.put("name", "Beijing");
data5.put("state", null);
data5.put("country", "China");
data5.put("capital", true);
data5.put("population", 21500000);
data5.put("regions", Arrays.asList("jingjinji", "hebei"));
cities.document("BJ").set(data5);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L931-L976
```

### Dart

```dart
final cities = db.collection("cities");
final data1 = <String, dynamic>{
  "name": "San Francisco",
  "state": "CA",
  "country": "USA",
  "capital": false,
  "population": 860000,
  "regions": ["west_coast", "norcal"]
};
cities.doc("SF").set(data1);

final data2 = <String, dynamic>{
  "name": "Los Angeles",
  "state": "CA",
  "country": "USA",
  "capital": false,
  "population": 3900000,
  "regions": ["west_coast", "socal"],
};
cities.doc("LA").set(data2);

final data3 = <String, dynamic>{
  "name": "Washington D.C.",
  "state": null,
  "country": "USA",
  "capital": true,
  "population": 680000,
  "regions": ["east_coast"]
};
cities.doc("DC").set(data3);

final data4 = <String, dynamic>{
  "name": "Tokyo",
  "state": null,
  "country": "Japan",
  "capital": true,
  "population": 9000000,
  "regions": ["kanto", "honshu"]
};
cities.doc("TOK").set(data4);

final data5 = <String, dynamic>{
  "name": "Beijing",
  "state": null,
  "country": "China",
  "capital": true,
  "population": 21500000,
  "regions": ["jingjinji", "hebei"],
};
cities.doc("BJ").set(data5);https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L619-L668
```

##### Java

    CollectionReference cities = db.collection("cities");
    List<ApiFuture<WriteResult>> futures = new ArrayList<>();
    futures.add(
        cities
            .document("SF")
            .set(
                new City(
                    "San Francisco",
                    "CA",
                    "USA",
                    false,
                    860000L,
                    Arrays.asList("west_coast", "norcal"))));
    futures.add(
        cities
            .document("LA")
            .set(
                new City(
                    "Los Angeles",
                    "CA",
                    "USA",
                    false,
                    3900000L,
                    Arrays.asList("west_coast", "socal"))));
    futures.add(
        cities
            .document("DC")
            .set(
                new City(
                    "Washington D.C.", null, "USA", true, 680000L, Arrays.asList("east_coast"))));
    futures.add(
        cities
            .document("TOK")
            .set(
                new City(
                    "Tokyo", null, "Japan", true, 9000000L, Arrays.asList("kanto", "honshu"))));
    futures.add(
        cities
            .document("BJ")
            .set(
                new City(
                    "Beijing",
                    null,
                    "China",
                    true,
                    21500000L,
                    Arrays.asList("jingjinji", "hebei"))));
    // (optional) block on operation
    ApiFutures.allAsList(futures).get();  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/RetrieveDataSnippets.java#L46-L94

##### Python

```python
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
```  

```python
cities_ref = db.collection("cities")
cities_ref.document("BJ").set(
    City("Beijing", None, "China", True, 21500000, ["hebei"]).to_dict()
)
cities_ref.document("SF").set(
    City(
        "San Francisco", "CA", "USA", False, 860000, ["west_coast", "norcal"]
    ).to_dict()
)
cities_ref.document("LA").set(
    City(
        "Los Angeles", "CA", "USA", False, 3900000, ["west_coast", "socal"]
    ).to_dict()
)
cities_ref.document("DC").set(
    City("Washington D.C.", None, "USA", True, 680000, ["east_coast"]).to_dict()
)
cities_ref.document("TOK").set(
    City("Tokyo", None, "Japan", True, 9000000, ["kanto", "honshu"]).to_dict()
)https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L152-L171
```

### Python

    cities_ref = db.collection("cities")
    await cities_ref.document("BJ").set(
        City("Beijing", None, "China", True, 21500000, ["hebei"]).to_dict()
    )
    await cities_ref.document("SF").set(
        City(
            "San Francisco", "CA", "USA", False, 860000, ["west_coast", "norcal"]
        ).to_dict()
    )
    await cities_ref.document("LA").set(
        City(
            "Los Angeles", "CA", "USA", False, 3900000, ["west_coast", "socal"]
        ).to_dict()
    )
    await cities_ref.document("DC").set(
        City("Washington D.C.", None, "USA", True, 680000, ["east_coast"]).to_dict()
    )
    await cities_ref.document("TOK").set(
        City("Tokyo", None, "Japan", True, 9000000, ["kanto", "honshu"]).to_dict()
    )  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L148-L167

##### C++

```c++
CollectionReference cities = db->Collection("cities");

cities.Document("SF").Set({
    {"name", FieldValue::String("San Francisco")},
    {"state", FieldValue::String("CA")},
    {"country", FieldValue::String("USA")},
    {"capital", FieldValue::Boolean(false)},
    {"population", FieldValue::Integer(860000)},
    {"regions", FieldValue::Array({FieldValue::String("west_coast"),
                                   FieldValue::String("norcal")})},
});

cities.Document("LA").Set({
    {"name", FieldValue::String("Los Angeles")},
    {"state", FieldValue::String("CA")},
    {"country", FieldValue::String("USA")},
    {"capital", FieldValue::Boolean(false)},
    {"population", FieldValue::Integer(3900000)},
    {"regions", FieldValue::Array({FieldValue::String("west_coast"),
                                   FieldValue::String("socal")})},
});

cities.Document("DC").Set({
    {"name", FieldValue::String("Washington D.C.")},
    {"state", FieldValue::Null()},
    {"country", FieldValue::String("USA")},
    {"capital", FieldValue::Boolean(true)},
    {"population", FieldValue::Integer(680000)},
    {"regions",
     FieldValue::Array({FieldValue::String("east_coast")})},
});

cities.Document("TOK").Set({
    {"name", FieldValue::String("Tokyo")},
    {"state", FieldValue::Null()},
    {"country", FieldValue::String("Japan")},
    {"capital", FieldValue::Boolean(true)},
    {"population", FieldValue::Integer(9000000)},
    {"regions", FieldValue::Array({FieldValue::String("kanto"),
                                   FieldValue::String("honshu")})},
});

cities.Document("BJ").Set({
    {"name", FieldValue::String("Beijing")},
    {"state", FieldValue::Null()},
    {"country", FieldValue::String("China")},
    {"capital", FieldValue::Boolean(true)},
    {"population", FieldValue::Integer(21500000)},
    {"regions", FieldValue::Array({FieldValue::String("jingjinji"),
                                   FieldValue::String("hebei")})},
});https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L429-L479
```

##### Node.js

    const citiesRef = db.collection('cities');

    await citiesRef.doc('SF').set({
      name: 'San Francisco', state: 'CA', country: 'USA',
      capital: false, population: 860000
    });
    await citiesRef.doc('LA').set({
      name: 'Los Angeles', state: 'CA', country: 'USA',
      capital: false, population: 3900000
    });
    await citiesRef.doc('DC').set({
      name: 'Washington, D.C.', state: null, country: 'USA',
      capital: true, population: 680000
    });
    await citiesRef.doc('TOK').set({
      name: 'Tokyo', state: null, country: 'Japan',
      capital: true, population: 9000000
    });
    await citiesRef.doc('BJ').set({
      name: 'Beijing', state: null, country: 'China',
      capital: true, population: 21500000
    });  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L483-L504

##### Go


    import (
    	"context"

    	"cloud.google.com/go/firestore"
    )

    func prepareRetrieve(ctx context.Context, client *firestore.Client) error {
    	cities := []struct {
    		id string
    		c  City
    	}{
    		{id: "SF", c: City{Name: "San Francisco", State: "CA", Country: "USA", Capital: false, Population: 860000}},
    		{id: "LA", c: City{Name: "Los Angeles", State: "CA", Country: "USA", Capital: false, Population: 3900000}},
    		{id: "DC", c: City{Name: "Washington D.C.", Country: "USA", Capital: true, Population: 680000}},
    		{id: "TOK", c: City{Name: "Tokyo", Country: "Japan", Capital: true, Population: 9000000}},
    		{id: "BJ", c: City{Name: "Beijing", Country: "China", Capital: true, Population: 21500000}},
    	}
    	for _, c := range cities {
    		_, err := client.Collection("cities").Doc(c.id).Set(ctx, c.c)
    		if err != nil {
    			return err
    		}
    	}
    	return nil
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/retrieve_data_get_dataset.go#L18-L44

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $citiesRef = $db->collection('samples/php/cities');
    $citiesRef->document('SF')->set([
        'name' => 'San Francisco',
        'state' => 'CA',
        'country' => 'USA',
        'capital' => false,
        'population' => 860000,
        'density' => 18000,
    ]);
    $citiesRef->document('LA')->set([
        'name' => 'Los Angeles',
        'state' => 'CA',
        'country' => 'USA',
        'capital' => false,
        'population' => 3900000,
        'density' => 8000,
    ]);
    $citiesRef->document('DC')->set([
        'name' => 'Washington D.C.',
        'state' => null,
        'country' => 'USA',
        'capital' => true,
        'population' => 680000,
        'density' => 11000,
    ]);
    $citiesRef->document('TOK')->set([
        'name' => 'Tokyo',
        'state' => null,
        'country' => 'Japan',
        'capital' => true,
        'population' => 9000000,
        'density' => 16000,

    ]);
    $citiesRef->document('BJ')->set([
        'name' => 'Beijing',
        'state' => null,
        'country' => 'China',
        'capital' => true,
        'population' => 21500000,
        'density' => 3500,
    ]);
    printf('Added example cities data to the cities collection.' . PHP_EOL);  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_get_dataset.php#L40-L82

##### Unity

```c#
CollectionReference citiesRef = db.Collection("cities");
citiesRef.Document("SF").SetAsync(new Dictionary<string, object>(){
        { "Name", "San Francisco" },
        { "State", "CA" },
        { "Country", "USA" },
        { "Capital", false },
        { "Population", 860000 }
    }).ContinueWithOnMainThread(task =>
        citiesRef.Document("LA").SetAsync(new Dictionary<string, object>(){
            { "Name", "Los Angeles" },
            { "State", "CA" },
            { "Country", "USA" },
            { "Capital", false },
            { "Population", 3900000 }
        })
).ContinueWithOnMainThread(task =>
    citiesRef.Document("DC").SetAsync(new Dictionary<string, object>(){
            { "Name", "Washington D.C." },
            { "State", null },
            { "Country", "USA" },
            { "Capital", true },
            { "Population", 680000 }
    })
).ContinueWithOnMainThread(task =>
    citiesRef.Document("TOK").SetAsync(new Dictionary<string, object>(){
            { "Name", "Tokyo" },
            { "State", null },
            { "Country", "Japan" },
            { "Capital", true },
            { "Population", 9000000 }
    })
).ContinueWithOnMainThread(task =>
    citiesRef.Document("BJ").SetAsync(new Dictionary<string, object>(){
            { "Name", "Beijing" },
            { "State", null },
            { "Country", "China" },
            { "Capital", true },
            { "Population", 21500000 }
    })
);
```

##### C#

    CollectionReference citiesRef = db.Collection("cities");
    await citiesRef.Document("SF").SetAsync(new Dictionary<string, object>(){
        { "Name", "San Francisco" },
        { "State", "CA" },
        { "Country", "USA" },
        { "Capital", false },
        { "Population", 860000 }
    });
    await citiesRef.Document("LA").SetAsync(new Dictionary<string, object>(){
        { "Name", "Los Angeles" },
        { "State", "CA" },
        { "Country", "USA" },
        { "Capital", false },
        { "Population", 3900000 }
    });
    await citiesRef.Document("DC").SetAsync(new Dictionary<string, object>(){
        { "Name", "Washington D.C." },
        { "State", null },
        { "Country", "USA" },
        { "Capital", true },
        { "Population", 680000 }
    });
    await citiesRef.Document("TOK").SetAsync(new Dictionary<string, object>(){
        { "Name", "Tokyo" },
        { "State", null },
        { "Country", "Japan" },
        { "Capital", true },
        { "Population", 9000000 }
    });
    await citiesRef.Document("BJ").SetAsync(new Dictionary<string, object>(){
        { "Name", "Beijing" },
        { "State", null },
        { "Country", "China" },
        { "Capital", true },
        { "Population", 21500000 }
    });
    Console.WriteLine("Added example cities data to the cities collection.");  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/GetData/Program.cs#L44-L80

##### Ruby

    cities_ref = firestore.col collection_path
    cities_ref.doc("SF").set(
      {
        name:       "San Francisco",
        state:      "CA",
        country:    "USA",
        capital:    false,
        population: 860_000
      }
    )
    cities_ref.doc("LA").set(
      {
        name:       "Los Angeles",
        state:      "CA",
        country:    "USA",
        capital:    false,
        population: 3_900_000
      }
    )
    cities_ref.doc("DC").set(
      {
        name:       "Washington D.C.",
        state:      nil,
        country:    "USA",
        capital:    true,
        population: 680_000
      }
    )
    cities_ref.doc("TOK").set(
      {
        name:       "Tokyo",
        state:      nil,
        country:    "Japan",
        capital:    true,
        population: 9_000_000
      }
    )
    cities_ref.doc("BJ").set(
      {
        name:       "Beijing",
        state:      nil,
        country:    "China",
        capital:    true,
        population: 21_500_000
      }
    )  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/get_data.rb#L23-L68

## Get a document

The following example shows how to retrieve the contents of a single document using`get()`:  

### Web

```javascript
import { doc, getDoc } from "firebase/firestore";

const docRef = doc(db, "cities", "SF");
const docSnap = await getDoc(docRef);

if (docSnap.exists()) {
  console.log("Document data:", docSnap.data());
} else {
  // docSnap.data() will be undefined in this case
  console.log("No such document!");
}https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/get_document.js#L8-L18
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
var docRef = db.collection("cities").doc("SF");

docRef.get().then((doc) => {
    if (doc.exists) {
        console.log("Document data:", doc.data());
    } else {
        // doc.data() will be undefined in this case
        console.log("No such document!");
    }
}).catch((error) => {
    console.log("Error getting document:", error);
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L583-L594
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
let docRef = db.collection("cities").document("SF")

do {
  let document = try await docRef.getDocument()
  if document.exists {
    let dataDescription = document.data().map(String.init(describing:)) ?? "nil"
    print("Document data: \(dataDescription)")
  } else {
    print("Document does not exist")
  }
} catch {
  print("Error getting document: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L722-L734
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
FIRDocumentReference *docRef =
    [[self.db collectionWithPath:@"cities"] documentWithPath:@"SF"];
[docRef getDocumentWithCompletion:^(FIRDocumentSnapshot *snapshot, NSError *error) {
  if (snapshot.exists) {
    // Document data may be nil if the document exists but has no keys or values.
    NSLog(@"Document data: %@", snapshot.data);
  } else {
    NSLog(@"Document does not exist");
  }
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L645-L654
```

### Kotlin

```kotlin
val docRef = db.collection("cities").document("SF")
docRef.get()
    .addOnSuccessListener { document ->
        if (document != null) {
            Log.d(TAG, "DocumentSnapshot data: ${document.data}")
        } else {
            Log.d(TAG, "No such document")
        }
    }
    .addOnFailureListener { exception ->
        Log.d(TAG, "get failed with ", exception)
    }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L479-L490
```

### Java

```java
DocumentReference docRef = db.collection("cities").document("SF");
docRef.get().addOnCompleteListener(new OnCompleteListener<DocumentSnapshot>() {
    @Override
    public void onComplete(@NonNull Task<DocumentSnapshot> task) {
        if (task.isSuccessful()) {
            DocumentSnapshot document = task.getResult();
            if (document.exists()) {
                Log.d(TAG, "DocumentSnapshot data: " + document.getData());
            } else {
                Log.d(TAG, "No such document");
            }
        } else {
            Log.d(TAG, "get failed with ", task.getException());
        }
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L625-L640
```

### Dart

```dart
final docRef = db.collection("cities").doc("SF");
docRef.get().then(
  (DocumentSnapshot doc) {
    final data = doc.data() as Map<String, dynamic>;
    // ...
  },
  onError: (e) => print("Error getting document: $e"),
);https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L432-L439
```

##### Java

    DocumentReference docRef = db.collection("cities").document("SF");
    // asynchronously retrieve the document
    ApiFuture<DocumentSnapshot> future = docRef.get();
    // ...
    // future.get() blocks on response
    DocumentSnapshot document = future.get();
    if (document.exists()) {
      System.out.println("Document data: " + document.getData());
    } else {
      System.out.println("No such document!");
    }  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/RetrieveDataSnippets.java#L105-L115

##### Python

    doc_ref = db.collection("cities").document("SF")

    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document!")  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L217-L223

### Python

    doc_ref = db.collection("cities").document("SF")

    doc = await doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document!")  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L212-L218

##### C++

```c++
DocumentReference doc_ref = db->Collection("cities").Document("SF");
doc_ref.Get().OnCompletion([](const Future<DocumentSnapshot>& future) {
  if (future.error() == Error::kErrorOk) {
    const DocumentSnapshot& document = *future.result();
    if (document.exists()) {
      std::cout << "DocumentSnapshot id: " << document.id() << std::endl;
    } else {
      std::cout << "no such document" << std::endl;
    }
  } else {
    std::cout << "Get failed with: " << future.error_message() << std::endl;
  }
});https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L494-L506
```

##### Node.js

    const cityRef = db.collection('cities').doc('SF');
    const doc = await cityRef.get();
    if (!doc.exists) {
      console.log('No such document!');
    } else {
      console.log('Document data:', doc.data());
    }  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L510-L516

##### Go


    import (
    	"context"
    	"fmt"

    	"cloud.google.com/go/firestore"
    )

    func docAsMap(ctx context.Context, client *firestore.Client) (map[string]interface{}, error) {
    	dsnap, err := client.Collection("cities").Doc("SF").Get(ctx)
    	if err != nil {
    		return nil, err
    	}
    	m := dsnap.Data()
    	fmt.Printf("Document data: %#v\n", m)
    	return m, nil
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/retrieve_data_get_as_map.go#L18-L35

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $docRef = $db->collection('samples/php/cities')->document('SF');
    $snapshot = $docRef->snapshot();

    if ($snapshot->exists()) {
        printf('Document data:' . PHP_EOL);
        print_r($snapshot->data());
    } else {
        printf('Document %s does not exist!' . PHP_EOL, $snapshot->id());
    }  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_get_as_map.php#L40-L48

##### Unity

```c#
DocumentReference docRef = db.Collection("cities").Document("SF");
docRef.GetSnapshotAsync().ContinueWithOnMainThread(task =>
{
  DocumentSnapshot snapshot = task.Result;
  if (snapshot.Exists) {
    Debug.Log(String.Format("Document data for {0} document:", snapshot.Id));
    Dictionary<string, object> city = snapshot.ToDictionary();
    foreach (KeyValuePair<string, object> pair in city) {
      Debug.Log(String.Format("{0}: {1}", pair.Key, pair.Value));
    }
  } else {
    Debug.Log(String.Format("Document {0} does not exist!", snapshot.Id));
  }
});
```

##### C#

    DocumentReference docRef = db.Collection("cities").Document("SF");
    DocumentSnapshot snapshot = await docRef.GetSnapshotAsync();
    if (snapshot.Exists)
    {
        Console.WriteLine("Document data for {0} document:", snapshot.Id);
        Dictionary<string, object> city = snapshot.ToDictionary();
        foreach (KeyValuePair<string, object> pair in city)
        {
            Console.WriteLine("{0}: {1}", pair.Key, pair.Value);
        }
    }
    else
    {
        Console.WriteLine("Document {0} does not exist!", snapshot.Id);
    }  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/GetData/Program.cs#L88-L102

##### Ruby

    doc_ref  = firestore.doc "#{collection_path}/SF"
    snapshot = doc_ref.get
    if snapshot.exists?
      puts "#{snapshot.document_id} data: #{snapshot.data}."
    else
      puts "Document #{snapshot.document_id} does not exist!"
    end  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/get_data.rb#L80-L86

| **Note:** If there is no document at the location referenced by`docRef`, the resulting`document`will be empty and calling`exists`on it will return`false`.

### Source Options

For platforms with offline support, you can set the`source`option to control how a`get`call uses the offline cache.

By default, a`get`call will attempt to fetch the latest document snapshot from your database. On platforms with offline support, the client library will use the offline cache if the network is unavailable or if the request times out.

You can specify the`source`option in a`get()`call to change the default behavior. You can fetch from only the database and ignore the offline cache, or you can fetch from only the offline cache. For example:  

### Web

```javascript
import { doc, getDocFromCache } from "firebase/firestore";

const docRef = doc(db, "cities", "SF");

// Get a document, forcing the SDK to fetch from the offline cache.
try {
  const doc = await getDocFromCache(docRef);

  // Document was found in the cache. If no cached document exists,
  // an error will be returned to the 'catch' block below.
  console.log("Cached document data:", doc.data());
} catch (e) {
  console.log("Error getting cached document:", e);
}https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/get_document_options.js#L8-L21
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
var docRef = db.collection("cities").doc("SF");

// Valid options for source are 'server', 'cache', or
// 'default'. See https://firebase.google.com/docs/reference/js/v8/firebase.firestore.GetOptions
// for more information.
var getOptions = {
    source: 'cache'
};

// Get a document, forcing the SDK to fetch from the offline cache.
docRef.get(getOptions).then((doc) => {
    // Document was found in the cache. If no cached document exists,
    // an error will be returned to the 'catch' block below.
    console.log("Cached document data:", doc.data());
}).catch((error) => {
    console.log("Error getting cached document:", error);
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L600-L616
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
let docRef = db.collection("cities").document("SF")

do {
  // Force the SDK to fetch the document from the cache. Could also specify
  // FirestoreSource.server or FirestoreSource.default.
  let document = try await docRef.getDocument(source: .cache)
  if document.exists {
    let dataDescription = document.data().map(String.init(describing:)) ?? "nil"
    print("Cached document data: \(dataDescription)")
  } else {
    print("Document does not exist in cache")
  }
} catch {
  print("Error getting document: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L740-L754
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
FIRDocumentReference *docRef =
[[self.db collectionWithPath:@"cities"] documentWithPath:@"SF"];

// Force the SDK to fetch the document from the cache. Could also specify
// FIRFirestoreSourceServer or FIRFirestoreSourceDefault.
[docRef getDocumentWithSource:FIRFirestoreSourceCache
                   completion:^(FIRDocumentSnapshot *snapshot, NSError *error) {
  if (snapshot != NULL) {
    // The document data was found in the cache.
    NSLog(@"Cached document data: %@", snapshot.data);
  } else {
    // The document data was not found in the cache.
    NSLog(@"Document does not exist in cache: %@", error);
  }
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L660-L674
```

### Kotlin

```kotlin
val docRef = db.collection("cities").document("SF")

// Source can be CACHE, SERVER, or DEFAULT.
val source = Source.CACHE

// Get the document, forcing the SDK to use the offline cache
docRef.get(source).addOnCompleteListener { task ->
    if (task.isSuccessful) {
        // Document found in the offline cache
        val document = task.result
        Log.d(TAG, "Cached document data: ${document?.data}")
    } else {
        Log.d(TAG, "Cached get failed: ", task.exception)
    }
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L496-L510
```

### Java

```java
DocumentReference docRef = db.collection("cities").document("SF");

// Source can be CACHE, SERVER, or DEFAULT.
Source source = Source.CACHE;

// Get the document, forcing the SDK to use the offline cache
docRef.get(source).addOnCompleteListener(new OnCompleteListener<DocumentSnapshot>() {
    @Override
    public void onComplete(@NonNull Task<DocumentSnapshot> task) {
        if (task.isSuccessful()) {
            // Document found in the offline cache
            DocumentSnapshot document = task.getResult();
            Log.d(TAG, "Cached document data: " + document.getData());
        } else {
            Log.d(TAG, "Cached get failed: ", task.getException());
        }
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L646-L663
```

### Dart

```dart
final docRef = db.collection("cities").doc("SF");

// Source can be CACHE, SERVER, or DEFAULT.
const source = Source.cache;

docRef.get(const GetOptions(source: source)).then(
      (res) => print("Successfully completed"),
      onError: (e) => print("Error completing: $e"),
    );https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L445-L453
```

##### Java

Not supported in the Java SDK.

##### Python

Not supported in the Python SDK.

##### C++

```c++
DocumentReference doc_ref = db->Collection("cities").Document("SF");
Source source = Source::kCache;
doc_ref.Get(source).OnCompletion([](const Future<DocumentSnapshot>& future) {
  if (future.error() == Error::kErrorOk) {
    const DocumentSnapshot& document = *future.result();
    if (document.exists()) {
      std::cout << "Cached document id: " << document.id() << std::endl;
    } else {
    }
  } else {
    std::cout << "Cached get failed: " << future.error_message() << std::endl;
  }
});https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L530-L542
```

##### Node.js

Not supported in the Node.js SDK.

##### Go

Not supported in the Go SDK.

##### PHP

Not supported in the PHP SDK.

##### Unity

Not supported in the Unity SDK.

##### C#

Not supported in the C# SDK.

##### Ruby

Not supported in the Ruby SDK.

### Custom objects

The previous example retrieved the contents of the document as a map, but in some languages it's often more convenient to use a custom object type. In[Add Data](https://firebase.google.com/docs/firestore/manage-data/add-data), you defined a`City`class that you used to define each city. You can turn your document back into a`City`object:  
To use custom objects, you must define a[FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_.firestoredataconverter)function for your class. For example:

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable Web v9 modular SDK and[upgrade](https://firebase.google.com/docs/web/modular-upgrade)from version 8.  

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
To use custom objects, you must define a[FirestoreDataConverter](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreDataConverter)function for your class. For example:

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable Web v9 modular SDK and[upgrade](https://firebase.google.com/docs/web/modular-upgrade)from version 8.  

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
Call your data converter with your read operations. After conversion, you can access custom object methods:

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable Web v9 modular SDK and[upgrade](https://firebase.google.com/docs/web/modular-upgrade)from version 8.  

```javascript
import { doc, getDoc} from "firebase/firestore"; 

const ref = doc(db, "cities", "LA").withConverter(cityConverter);
const docSnap = await getDoc(ref);
if (docSnap.exists()) {
  // Convert to City object
  const city = docSnap.data();
  // Use a City instance method
  console.log(city.toString());
} else {
  console.log("No such document!");
}https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/get_custom_object.js#L8-L19
```
Call your data converter with your read operations. After conversion, you can access custom object methods:

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable Web v9 modular SDK and[upgrade](https://firebase.google.com/docs/web/modular-upgrade)from version 8.  

```javascript
db.collection("cities").doc("LA")
  .withConverter(cityConverter)
  .get().then((doc) => {
    if (doc.exists){
      // Convert to City object
      var city = doc.data();
      // Use a City instance method
      console.log(city.toString());
    } else {
      console.log("No such document!");
    }}).catch((error) => {
      console.log("Error getting document:", error);
    });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L251-L263
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.

To support automatic type serialization in Swift, your type must conform to the[Codable protocol](https://developer.apple.com/documentation/swift/codable).  

```swift
let docRef = db.collection("cities").document("BJ")

do {
  let city = try await docRef.getDocument(as: City.self)
  print("City: \(city)")
} catch {
  print("Error decoding city: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L760-L767
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.

In Objective-C you must do this manually.  

```objective-c
FIRDocumentReference *docRef =
[[self.db collectionWithPath:@"cities"] documentWithPath:@"BJ"];
[docRef getDocumentWithCompletion:^(FIRDocumentSnapshot *snapshot, NSError *error) {
  FSTCity *city = [[FSTCity alloc] initWithDictionary:snapshot.data];
  if (city != nil) {
    NSLog(@"City: %@", city);
  } else {
    NSLog(@"Document does not exist");
  }
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L680-L689
```

### Kotlin

```kotlin
val docRef = db.collection("cities").document("BJ")
docRef.get().addOnSuccessListener { documentSnapshot ->
    val city = documentSnapshot.toObject<City>()
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L516-L519
```

### Java

Important: Each custom class must have a public constructor that takes no arguments. In addition, the class must include a public getter for each property.  

```java
DocumentReference docRef = db.collection("cities").document("BJ");
docRef.get().addOnSuccessListener(new OnSuccessListener<DocumentSnapshot>() {
    @Override
    public void onSuccess(DocumentSnapshot documentSnapshot) {
        City city = documentSnapshot.toObject(City.class);
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L669-L675
```

### Dart

To use custom objects, you must define Firestore data conversion functions for your class. For example:  

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

Then, create a document reference with your data conversion functions. Any read operations you perform using this reference will return instances of your custom class:  

```dart
final ref = db.collection("cities").doc("LA").withConverter(
      fromFirestore: City.fromFirestore,
      toFirestore: (City city, _) => city.toFirestore(),
    );
final docSnap = await ref.get();
final city = docSnap.data(); // Convert to City object
if (city != null) {
  print(city);
} else {
  print("No such document.");
}https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L459-L469
```

##### Java

Each custom class must have a public constructor that takes no arguments. In addition, the class must include a public getter for each property.  

    DocumentReference docRef = db.collection("cities").document("BJ");
    // asynchronously retrieve the document
    ApiFuture<DocumentSnapshot> future = docRef.get();
    // block on response
    DocumentSnapshot document = future.get();
    City city = null;
    if (document.exists()) {
      // convert document to POJO
      city = document.toObject(City.class);
      System.out.println(city);
    } else {
      System.out.println("No such document!");
    }  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/RetrieveDataSnippets.java#L127-L139

##### Python

    doc_ref = db.collection("cities").document("BJ")

    doc = doc_ref.get()
    city = City.from_dict(doc.to_dict())
    print(city)  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L230-L234

### Python

    doc_ref = db.collection("cities").document("BJ")

    doc = await doc_ref.get()
    city = City.from_dict(doc.to_dict())
    print(city)  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L225-L229

##### C++

```c++
// This is not yet supported.
```

##### Node.js

Node.js uses JavaScript objects.

##### Go


    import (
    	"context"
    	"fmt"

    	"cloud.google.com/go/firestore"
    )

    func docAsEntity(ctx context.Context, client *firestore.Client) (*City, error) {
    	dsnap, err := client.Collection("cities").Doc("BJ").Get(ctx)
    	if err != nil {
    		return nil, err
    	}
    	var c City
    	dsnap.DataTo(&c)
    	fmt.Printf("Document data: %#v\n", c)
    	return &c, nil
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/retrieve_data_get_as_custom_type.go#L18-L36

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $docRef = $db->collection('samples/php/cities')->document('SF');
    $snapshot = $docRef->snapshot();
    $city = City::fromArray($snapshot->data());

    if ($snapshot->exists()) {
        printf('Document data:' . PHP_EOL);
        print((string) $city);
    } else {
        printf('Document %s does not exist!' . PHP_EOL, $snapshot->id());
    }  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_get_as_custom_type.php#L42-L51

##### Unity

```c#
DocumentReference docRef = db.Collection("cities").Document("BJ");

docRef.GetSnapshotAsync().ContinueWith((task) =>
{
  var snapshot = task.Result;
  if (snapshot.Exists)
  {
    Debug.Log(String.Format("Document data for {0} document:", snapshot.Id));
    City city = snapshot.ConvertTo<City>();
    Debug.Log(String.Format("Name: {0}", city.Name));
    Debug.Log(String.Format("State: {0}", city.State));
    Debug.Log(String.Format("Country: {0}", city.Country));
    Debug.Log(String.Format("Capital: {0}", city.Capital));
    Debug.Log(String.Format("Population: {0}", city.Population));
  }
  else
  {
    Debug.Log(String.Format("Document {0} does not exist!", snapshot.Id));
  }
});
```

##### C#

    DocumentReference docRef = db.Collection("cities").Document("BJ");
    DocumentSnapshot snapshot = await docRef.GetSnapshotAsync();
    if (snapshot.Exists)
    {
        Console.WriteLine("Document data for {0} document:", snapshot.Id);
        City city = snapshot.ConvertTo<City>();
        Console.WriteLine("Name: {0}", city.Name);
        Console.WriteLine("State: {0}", city.State);
        Console.WriteLine("Country: {0}", city.Country);
        Console.WriteLine("Capital: {0}", city.Capital);
        Console.WriteLine("Population: {0}", city.Population);
    }
    else
    {
        Console.WriteLine("Document {0} does not exist!", snapshot.Id);
    }  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/GetData/Program.cs#L130-L145

##### Ruby

Not applicable for Ruby.

## Get multiple documents from a collection

You can also retrieve multiple documents with one request by querying documents in a collection. For example, you can use`where()`to query for all of the documents that meet a certain condition, then use`get()`to retrieve the results:  

### Web

```javascript
import { collection, query, where, getDocs } from "firebase/firestore";

const q = query(collection(db, "cities"), where("capital", "==", true));

const querySnapshot = await getDocs(q);
querySnapshot.forEach((doc) => {
  // doc.data() is never undefined for query doc snapshots
  console.log(doc.id, " => ", doc.data());
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/get_multiple.js#L8-L16
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
db.collection("cities").where("capital", "==", true)
    .get()
    .then((querySnapshot) => {
        querySnapshot.forEach((doc) => {
            // doc.data() is never undefined for query doc snapshots
            console.log(doc.id, " => ", doc.data());
        });
    })
    .catch((error) => {
        console.log("Error getting documents: ", error);
    });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L672-L682
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
do {
  let querySnapshot = try await db.collection("cities").whereField("capital", isEqualTo: true)
    .getDocuments()
  for document in querySnapshot.documents {
    print("\(document.documentID) => \(document.data())")
  }
} catch {
  print("Error getting documents: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L814-L822
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
[[[self.db collectionWithPath:@"cities"] queryWhereField:@"capital" isEqualTo:@(YES)]
    getDocumentsWithCompletion:^(FIRQuerySnapshot *snapshot, NSError *error) {
      if (error != nil) {
        NSLog(@"Error getting documents: %@", error);
      } else {
        for (FIRDocumentSnapshot *document in snapshot.documents) {
          NSLog(@"%@ => %@", document.documentID, document.data);
        }
      }
    }];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L733-L742
```

### Kotlin

```kotlin
db.collection("cities")
    .whereEqualTo("capital", true)
    .get()
    .addOnSuccessListener { documents ->
        for (document in documents) {
            Log.d(TAG, "${document.id} => ${document.data}")
        }
    }
    .addOnFailureListener { exception ->
        Log.w(TAG, "Error getting documents: ", exception)
    }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L577-L587
```

### Java

```java
db.collection("cities")
        .whereEqualTo("capital", true)
        .get()
        .addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
            @Override
            public void onComplete(@NonNull Task<QuerySnapshot> task) {
                if (task.isSuccessful()) {
                    for (QueryDocumentSnapshot document : task.getResult()) {
                        Log.d(TAG, document.getId() + " => " + document.getData());
                    }
                } else {
                    Log.d(TAG, "Error getting documents: ", task.getException());
                }
            }
        });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L742-L756
```

### Dart

```dart
db.collection("cities").where("capital", isEqualTo: true).get().then(
  (querySnapshot) {
    print("Successfully completed");
    for (var docSnapshot in querySnapshot.docs) {
      print('${docSnapshot.id} => ${docSnapshot.data()}');
    }
  },
  onError: (e) => print("Error completing: $e"),
);https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L475-L483
```

##### Java

    // asynchronously retrieve multiple documents
    ApiFuture<QuerySnapshot> future = db.collection("cities").whereEqualTo("capital", true).get();
    // future.get() blocks on response
    List<QueryDocumentSnapshot> documents = future.get().getDocuments();
    for (DocumentSnapshot document : documents) {
      System.out.println(document.getId() + " => " + document.toObject(City.class));
    }  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/RetrieveDataSnippets.java#L151-L157

##### Python

    # Note: Use of CollectionRef stream() is prefered to get()
    docs = (
        db.collection("cities")
        .where(filter=FieldFilter("capital", "==", True))
        .stream()
    )

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L241-L249

### Python

    # Note: Use of CollectionRef stream() is prefered to get()
    docs = (
        db.collection("cities")
        .where(filter=FieldFilter("capital", "==", True))
        .stream()
    )

    async for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L236-L244

##### C++

```c++
db->Collection("cities")
    .WhereEqualTo("capital", FieldValue::Boolean(true))
    .Get()
    .OnCompletion([](const Future<QuerySnapshot>& future) {
      if (future.error() == Error::kErrorOk) {
        for (const DocumentSnapshot& document :
             future.result()->documents()) {
          std::cout << document << std::endl;
        }
      } else {
        std::cout << "Error getting documents: " << future.error_message()
                  << std::endl;
      }
    });https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L560-L573
```

##### Node.js

    const citiesRef = db.collection('cities');
    const snapshot = await citiesRef.where('capital', '==', true).get();
    if (snapshot.empty) {
      console.log('No matching documents.');
      return;
    }  

    snapshot.forEach(doc => {
      console.log(doc.id, '=>', doc.data());
    });  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L532-L541

##### Go


    import (
    	"context"
    	"fmt"

    	"cloud.google.com/go/firestore"
    	"google.golang.org/api/iterator"
    )

    func multipleDocs(ctx context.Context, client *firestore.Client) error {
    	fmt.Println("All capital cities:")
    	iter := client.Collection("cities").Where("capital", "==", true).Documents(ctx)
    	for {
    		doc, err := iter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Println(doc.Data())
    	}
    	return nil
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/retrieve_data_query.go#L18-L42

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $citiesRef = $db->collection('samples/php/cities');
    $query = $citiesRef->where('capital', '=', true);
    $documents = $query->documents();
    foreach ($documents as $document) {
        if ($document->exists()) {
            printf('Document data for document %s:' . PHP_EOL, $document->id());
            print_r($document->data());
            printf(PHP_EOL);
        } else {
            printf('Document %s does not exist!' . PHP_EOL, $document->id());
        }
    }  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_query.php#L40-L51

##### Unity

```c#
Query capitalQuery = db.Collection("cities").WhereEqualTo("Capital", true);
capitalQuery.GetSnapshotAsync().ContinueWithOnMainThread(task => {
  QuerySnapshot capitalQuerySnapshot = task.Result;
  foreach (DocumentSnapshot documentSnapshot in capitalQuerySnapshot.Documents) {
    Debug.Log(String.Format("Document data for {0} document:", documentSnapshot.Id));
    Dictionary<string, object> city = documentSnapshot.ToDictionary();
    foreach (KeyValuePair<string, object> pair in city) {
      Debug.Log(String.Format("{0}: {1}", pair.Key, pair.Value));
    }

    // Newline to separate entries
    Debug.Log("");
  };
});
```

##### C#

    Query capitalQuery = db.Collection("cities").WhereEqualTo("Capital", true);
    QuerySnapshot capitalQuerySnapshot = await capitalQuery.GetSnapshotAsync();
    foreach (DocumentSnapshot documentSnapshot in capitalQuerySnapshot.Documents)
    {
        Console.WriteLine("Document data for {0} document:", documentSnapshot.Id);
        Dictionary<string, object> city = documentSnapshot.ToDictionary();
        foreach (KeyValuePair<string, object> pair in city)
        {
            Console.WriteLine("{0}: {1}", pair.Key, pair.Value);
        }
        Console.WriteLine("");
    }  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/GetData/Program.cs#L153-L164

##### Ruby

    cities_ref = firestore.col collection_path

    query = cities_ref.where "capital", "=", true

    query.get do |city|
      puts "#{city.document_id} data: #{city.data}."
    end  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/get_data.rb#L96-L102

By default,Cloud Firestoreretrieves all documents that satisfy the query in ascending order by document ID, but you can[order and limit the data returned](https://firebase.google.com/docs/firestore/query-data/order-limit-data).

### Get all documents in a collection

In addition, you can retrieve*all* documents in a collection by omitting the`where()`filter entirely:  

### Web

```javascript
import { collection, getDocs } from "firebase/firestore";

const querySnapshot = await getDocs(collection(db, "cities"));
querySnapshot.forEach((doc) => {
  // doc.data() is never undefined for query doc snapshots
  console.log(doc.id, " => ", doc.data());
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/get_multiple_all.js#L8-L14
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
db.collection("cities").get().then((querySnapshot) => {
    querySnapshot.forEach((doc) => {
        // doc.data() is never undefined for query doc snapshots
        console.log(doc.id, " => ", doc.data());
    });
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L690-L695
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
do {
  let querySnapshot = try await db.collection("cities").getDocuments()
  for document in querySnapshot.documents {
    print("\(document.documentID) => \(document.data())")
  }
} catch {
  print("Error getting documents: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L828-L835
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
[[self.db collectionWithPath:@"cities"]
    getDocumentsWithCompletion:^(FIRQuerySnapshot *snapshot, NSError *error) {
      if (error != nil) {
        NSLog(@"Error getting documents: %@", error);
      } else {
        for (FIRDocumentSnapshot *document in snapshot.documents) {
          NSLog(@"%@ => %@", document.documentID, document.data);
        }
      }
    }];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L748-L757
```

### Kotlin

```kotlin
db.collection("cities")
    .get()
    .addOnSuccessListener { result ->
        for (document in result) {
            Log.d(TAG, "${document.id} => ${document.data}")
        }
    }
    .addOnFailureListener { exception ->
        Log.d(TAG, "Error getting documents: ", exception)
    }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L593-L602
```

### Java

```java
db.collection("cities")
        .get()
        .addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
            @Override
            public void onComplete(@NonNull Task<QuerySnapshot> task) {
                if (task.isSuccessful()) {
                    for (QueryDocumentSnapshot document : task.getResult()) {
                        Log.d(TAG, document.getId() + " => " + document.getData());
                    }
                } else {
                    Log.d(TAG, "Error getting documents: ", task.getException());
                }
            }
        });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L762-L775
```

### Dart

```dart
db.collection("cities").get().then(
  (querySnapshot) {
    print("Successfully completed");
    for (var docSnapshot in querySnapshot.docs) {
      print('${docSnapshot.id} => ${docSnapshot.data()}');
    }
  },
  onError: (e) => print("Error completing: $e"),
);https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L489-L497
```

##### Java

    // asynchronously retrieve all documents
    ApiFuture<QuerySnapshot> future = db.collection("cities").get();
    // future.get() blocks on response
    List<QueryDocumentSnapshot> documents = future.get().getDocuments();
    for (QueryDocumentSnapshot document : documents) {
      System.out.println(document.getId() + " => " + document.toObject(City.class));
    }  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/RetrieveDataSnippets.java#L169-L175

##### Python

    docs = db.collection("cities").stream()

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L270-L273

### Python

    docs = db.collection("cities").stream()

    async for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L265-L268

##### C++

```c++
db->Collection("cities").Get().OnCompletion(
    [](const Future<QuerySnapshot>& future) {
      if (future.error() == Error::kErrorOk) {
        for (const DocumentSnapshot& document :
             future.result()->documents()) {
          std::cout << document << std::endl;
        }
      } else {
        std::cout << "Error getting documents: " << future.error_message()
                  << std::endl;
      }
    });https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L587-L598
```

##### Node.js

    const citiesRef = db.collection('cities');
    const snapshot = await citiesRef.get();
    snapshot.forEach(doc => {
      console.log(doc.id, '=>', doc.data());
    });  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L547-L551

##### Go


    import (
    	"context"
    	"fmt"

    	"cloud.google.com/go/firestore"
    	"google.golang.org/api/iterator"
    )

    func allDocs(ctx context.Context, client *firestore.Client) error {
    	fmt.Println("All cities:")
    	iter := client.Collection("cities").Documents(ctx)
    	defer iter.Stop()
    	for {
    		doc, err := iter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Println(doc.Data())
    	}
    	return nil
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/retrieve_data_get_all_documents.go#L18-L43

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $citiesRef = $db->collection('samples/php/cities');
    $documents = $citiesRef->documents();
    foreach ($documents as $document) {
        if ($document->exists()) {
            printf('Document data for document %s:' . PHP_EOL, $document->id());
            print_r($document->data());
            printf(PHP_EOL);
        } else {
            printf('Document %s does not exist!' . PHP_EOL, $document->id());
        }
    }  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_get_all_documents.php#L40-L50

##### Unity

```c#
Query allCitiesQuery = db.Collection("cities");
allCitiesQuery.GetSnapshotAsync().ContinueWithOnMainThread(task =>
{
  QuerySnapshot allCitiesQuerySnapshot = task.Result;
  foreach (DocumentSnapshot documentSnapshot in allCitiesQuerySnapshot.Documents)
  {
    Debug.Log(String.Format("Document data for {0} document:", documentSnapshot.Id));
    Dictionary<string, object> city = documentSnapshot.ToDictionary();
    foreach (KeyValuePair<string, object> pair in city)
    {
      Debug.Log(String.Format("{0}: {1}", pair.Key, pair.Value));
    }

    // Newline to separate entries
    Debug.Log("");
  }
});
```

##### C#

    Query allCitiesQuery = db.Collection("cities");
    QuerySnapshot allCitiesQuerySnapshot = await allCitiesQuery.GetSnapshotAsync();
    foreach (DocumentSnapshot documentSnapshot in allCitiesQuerySnapshot.Documents)
    {
        Console.WriteLine("Document data for {0} document:", documentSnapshot.Id);
        Dictionary<string, object> city = documentSnapshot.ToDictionary();
        foreach (KeyValuePair<string, object> pair in city)
        {
            Console.WriteLine("{0}: {1}", pair.Key, pair.Value);
        }
        Console.WriteLine("");
    }  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/GetData/Program.cs#L172-L183

##### Ruby

    cities_ref = firestore.col collection_path
    cities_ref.get do |city|
      puts "#{city.document_id} data: #{city.data}."
    end  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/get_data.rb#L112-L115

### Get all documents in a subcollection

To retrieve all the documents from a subcollection, create a reference with the complete path to that subcollection:  

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable Web v9 modular SDK and[upgrade](https://firebase.google.com/docs/web/modular-upgrade)from version 8.  

```javascript
const { collection, getDocs } = require("firebase/firestore");
// Query a reference to a subcollection
const querySnapshot = await getDocs(collection(db, "cities", "SF", "landmarks"));
querySnapshot.forEach((doc) => {
  // doc.data() is never undefined for query doc snapshots
  console.log(doc.id, " => ", doc.data());
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore-next/test.firestore.js#L703-L709
```

### Web

```
// Snippet not available
```

##### Swift

```swift
do {
  let querySnapshot = try await db.collection("cities/SF/landmarks").getDocuments()
  for document in querySnapshot.documents {
    print("\(document.documentID) => \(document.data())")
  }
} catch {
  print("Error getting documents: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L841-L848
```

##### Objective-C

```objective-c
[[self.db collectionWithPath:@"cities/SF/landmarks"]
    getDocumentsWithCompletion:^(FIRQuerySnapshot *snapshot, NSError *error) {
      if (error != nil) {
        NSLog(@"Error getting documents: %@", error);
      } else {
        for (FIRDocumentSnapshot *document in snapshot.documents) {
          NSLog(@"%@ => %@", document.documentID, document.data);
        }
      }
    }];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L763-L772
```

### Kotlin

```kotlin
db.collection("cities")
    .document("SF")
    .collection("landmarks")
    .get()
    .addOnSuccessListener { result ->
        for (document in result) {
            Log.d(TAG, "${document.id} => ${document.data}")
        }
    }
    .addOnFailureListener { exception ->
        Log.d(TAG, "Error getting documents: ", exception)
    }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L608-L619
```

### Java

```java
db.collection("cities")
        .document("SF")
        .collection("landmarks")
        .get()
        .addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
            @Override
            public void onComplete(@NonNull Task<QuerySnapshot> task) {
                if (task.isSuccessful()) {
                    for (QueryDocumentSnapshot document : task.getResult()) {
                        Log.d(TAG, document.getId() + " => " + document.getData());
                    }
                } else {
                    Log.d(TAG, "Error getting documents: ", task.getException());
                }
            }
        });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L781-L796
```

### Dart

```java
db.collection("cities").doc("SF").collection("landmarks").get().then(
  (querySnapshot) {
    print("Successfully completed");
    for (var docSnapshot in querySnapshot.docs) {
      print('${docSnapshot.id} => ${docSnapshot.data()}');
    }
  },
  onError: (e) => print("Error completing: $e"),
);https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L504-L512
```

##### Java

```
// Snippet not available
```

##### Python

```
// Snippet not available
```

### Python

```
// Snippet not available
```

##### C++

```
// Snippet not available
```

##### Node.js

```
// Snippet not available
```

##### Go

```
// Snippet not available
```

##### PHP

```
// Snippet not available
```

##### Unity

```
// Snippet not available
```

##### C#

```
// Snippet not available
```

##### Ruby

```
// Snippet not available
```

### Get multiple documents from a collection group

A collection group consists of all collections with the same ID. For example, if each document in your`cities`collection has a subcollection called`landmarks`, all of the`landmarks`subcollections belong to the same collection group. By default, queries retrieve results from a single collection in your database.[Use a collection group query to retrieve results from a collection group](https://firebase.google.com/docs/firestore/query-data/queries#collection-group-query)instead of from a single collection.

## List subcollections of a document

The`listCollections()`method of theCloud Firestoreserver client libraries lists all subcollections of a document reference.

Retrieving a list of collections is not possible with the mobile/web client libraries. You should only look up collection names as part of administrative tasks in trusted server environments. If you find that you need this capability in the mobile/web client libraries, consider restructuring your data so that subcollection names are predictable.  

##### Web

Not available in the Web client library.

##### Swift

Not available in the Swift client library.

##### Objective-C

Not available in the Objective-C client library.

### Kotlin

Not available in the Android client library.

### Java

Not available in the Android client library.

### Dart

Not available in the Flutter client library.

##### Java

    Iterable<CollectionReference> collections =
        db.collection("cities").document("SF").listCollections();

    for (CollectionReference collRef : collections) {
      System.out.println("Found subcollection with id: " + collRef.getId());
    }  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/RetrieveDataSnippets.java#L187-L192

##### Python

    city_ref = db.collection("cities").document("SF")
    collections = city_ref.collections()
    for collection in collections:
        for doc in collection.stream():
            print(f"{doc.id} => {doc.to_dict()}")  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L966-L970

### Python

    collections = db.collection("cities").document("SF").collections()
    async for collection in collections:
        async for doc in collection.stream():
            print(f"{doc.id} => {doc.to_dict()}")  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L798-L801

##### C++

Not available in the C++ client library.

##### Node.js

    const sfRef = db.collection('cities').doc('SF');
    const collections = await sfRef.listCollections();
    collections.forEach(collection => {
      console.log('Found subcollection with id:', collection.id);
    });  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L557-L561

##### Go


    import (
    	"context"
    	"fmt"

    	"cloud.google.com/go/firestore"
    	"google.golang.org/api/iterator"
    )

    func getCollections(ctx context.Context, client *firestore.Client) error {
    	iter := client.Collection("cities").Doc("SF").Collections(ctx)
    	for {
    		collRef, err := iter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Printf("Found collection with id: %s\n", collRef.ID)
    	}
    	return nil
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/retrieve_data_get_sub_collections.go#L18-L41

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $cityRef = $db->collection('samples/php/cities')->document('SF');
    $collections = $cityRef->collections();
    foreach ($collections as $collection) {
        printf('Found subcollection with id: %s' . PHP_EOL, $collection->id());
    }  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_get_sub_collections.php#L40-L44

##### Unity

```c#
// This is not yet supported in the Unity SDK.
```

##### C#

    DocumentReference cityRef = db.Collection("cities").Document("SF");
    IAsyncEnumerable<CollectionReference> subcollections = cityRef.ListCollectionsAsync();
    IAsyncEnumerator<CollectionReference> subcollectionsEnumerator = subcollections.GetAsyncEnumerator(default);
    while (await subcollectionsEnumerator.MoveNextAsync())
    {
        CollectionReference subcollectionRef = subcollectionsEnumerator.Current;
        Console.WriteLine("Found subcollection with ID: {0}", subcollectionRef.Id);
    }  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/GetData/Program.cs#L206-L213

##### Ruby

    city_ref = firestore.doc "#{collection_path}/SF"
    city_ref.cols do |col|
      puts col.collection_id
    end  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/get_data.rb#L140-L143

Learn more about different[types of queries](https://firebase.google.com/docs/firestore/query-data/queries).

For more information on error codes and how to resolve latency issues when getting data check out the[troubleshooting page](https://cloud.google.com/firestore/docs/troubleshooting).