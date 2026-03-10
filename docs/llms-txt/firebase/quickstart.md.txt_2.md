# Source: https://firebase.google.com/docs/firestore/enterprise/quickstart.md.txt

> [!WARNING]
> **Preview:** **Firestore in Native mode (with Pipeline operations) for Enterprise
> edition** is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific
> Terms](https://cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage
> descriptions](https://cloud.google.com/products#product-launch-stages).

This quickstart shows you how to set up Firestore Enterprise edition, add data, then
use either Core operations or Pipeline operations to query the data you
just added in the Firebase console.

Cloud Firestore supports mobile or web SDKs and server client libraries:

- Cloud Firestore supports **SDKs for Android, iOS, and web and more** . Combined with
  Cloud Firestore Security Rules and Firebase Authentication, the mobile and web SDKs support
  serverless app architectures where clients connect directly to your
  Cloud Firestore database.

- Cloud Firestore supports **server client libraries** for Java, Node.js, and
  Python. Use these client libraries to set up privileged server
  environments with full access to your database. Learn more about these libraries
  in the [Quickstart for server client libraries](https://firebase.google.com/docs/firestore/enterprise/quickstart-server).

> [!NOTE]
> **Note:** Before getting started with these features, make sure you're familiar with the [differences between Core and Pipeline operations](https://firebase.google.com/docs/firestore/enterprise/pipelines-overview?db=firestore-docs#features-of-firestore-pipeline-operations).

## Create a Firestore Enterprise edition database

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
       sure to review the [Secure your data](https://firebase.google.com/docs/firestore/enterprise/quickstart#secure_your_data) section.**

   :   To get started with the web, Apple platforms, or Android SDK, select test
       mode.

   Production mode

   :   Denies all reads and writes from mobile and web clients.
       Your authenticated application servers (Python) can still access your
       database.

   Your initial set of Cloud Firestore Security Rules will apply to your default
   Cloud Firestore database. If you create multiple databases for your
   project, you can deploy Cloud Firestore Security Rules for each database.
8. Click **Create**.

> [!NOTE]
> **Cloud Firestore and App Engine:** With support for multiple databases, you can use both Firestore Enterprise edition and Datastore in the same project. If you use App Engine, note that only the `(default)` database in standard mode with Datastore or Firestore Native APIs can be used with App Engine.

When you enable Firestore Enterprise edition, it also enables the API in the
[Cloud API Manager](https://console.cloud.google.com/projectselector/apis/api/firestore.googleapis.com/overview).

## Set up your development environment

Add the required dependencies and client libraries to your app.

### Web

1. Follow the instructions to [add Firebase to your web app](https://firebase.google.com/docs/web/setup?sdk_version=v9).
2. The Cloud Firestore SDK is available as an npm package.

   ```
   npm install firebase@12.10.0 --save
   ```
   You'll need to import both Firebase and Cloud Firestore.

   ```
   import { initializeApp } from "firebase/app";
   import { getFirestore } from "firebase/firestore";
   ```

> [!NOTE]
> Looking for a compact Firestore library, and only need simple REST/CRUD capabilities? Try the [Firestore Lite SDK](https://firebase.google.com/docs/firestore/solutions/firestore-lite), available only via npm.

##### iOS+


Follow the instructions to
[add Firebase to your Apple app](https://firebase.google.com/docs/ios/setup).

Use Swift Package Manager to install and manage Firebase dependencies.

> [!NOTE]
> Visit [our
> installation guide](https://firebase.google.com/docs/ios/installation-methods) to learn about the different ways you can add Firebase SDKs to your Apple project, including importing frameworks directly and using CocoaPods.

1. In Xcode, with your app project open, navigate to **File \> Swift Packages \>
   Add Package Dependency**.
2. When prompted, add the Firebase Apple platforms SDK repository:

```
  https://github.com/firebase/firebase-ios-sdk
  
```

> [!NOTE]
> **Note:** New projects should use the default (latest) SDK version, but you can choose an older version if needed.

3. Choose the Firestore library.
4. When finished, Xcode will automatically begin resolving and downloading your dependencies in the background.

##### Android

1. Follow the instructions to [add Firebase to your Android app](https://firebase.google.com/docs/android/setup).
2. Using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom), declare the dependency for the Cloud Firestore library for Android in your **module (app-level) Gradle file** (usually `app/build.gradle.kts` or `app/build.gradle`).

   ```
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

       // Declare the dependency for the Cloud Firestore library
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-firestore")
   }
   ```

   By using the
   [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom),
   your app will always use compatible versions of the Firebase Android
   libraries.
   *(Alternative)*
   Declare Firebase library dependencies *without* using the
   BoM

   If you choose not to use the Firebase BoM, you must specify each
   Firebase library version in its dependency line.

   **Note that if you use *multiple* Firebase libraries in
   your app, we highly recommend using the BoM to manage library
   versions, which ensures that all versions are compatible.**

   ```
   dependencies {
       // Declare the dependency for the Cloud Firestore library
       // When NOT using the BoM, you must specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-firestore:26.1.1")
   }
   ```

   **Looking for a Kotlin-specific library module?** Starting with the
   [October 2023 release](https://firebase.google.com/support/release-notes/android#2023-10-10),
   both Kotlin and Java developers can depend on the main library module
   (for details, see the
   [FAQ about this initiative](https://firebase.google.com/docs/android/kotlin-migration)).

## Initialize Cloud Firestore

Initialize an instance of Cloud Firestore:

### Web

```
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://support.google.com/firebase/answer/7015592
const firebaseConfig = {
    FIREBASE_CONFIGURATION
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


// When initializing Firestore, remember to use the name of the database you created earlier:
const db = initializeFirestore(app, {}, 'your-new-enterprise-database');
```


Replace <var translate="no">FIREBASE_CONFIGURATION</var> with your web app's
[`firebaseConfig`](https://support.google.com/firebase/answer/7015592).


To persist data when the device loses its connection, see the [Enable Offline Data](https://firebase.google.com/docs/firestore/enterprise/enable-offline) documentation.

##### Swift

```
import FirebaseCore
import FirebaseFirestore

FirebaseApp.configure()

// When initializing Firestore, remember to use the name of the database you created earlier:
let db = Firestore.firestore(database: "your-new-enterprise-database")
```

### Kotlin

```kotlin
// Access a Cloud Firestore instance from your Activity
// When initializing Firestore, remember to use the name of the database you created earlier:
val firestore = FirebaseFirestore.getInstance("your-new-enterprise-database")
```

### Java

```java
// Access a Cloud Firestore instance from your Activity
// When initializing Firestore, remember to use the name of the database you created earlier:
FirebaseFirestore firestore = FirebaseFirestore.getInstance("your-new-enterprise-database");
```

## Add data using Core operations

In order to explore Core operations and Pipeline operations for querying data,
add data to your database using Core operations.

Cloud Firestore stores data in Documents, which are stored in
Collections. Cloud Firestore creates collections and documents implicitly
the first time you add data to the document. You don't need to explicitly
create collections or documents.

Create a new collection and a document using the following example code.

### Web

```javascript
import { collection, addDoc } from "firebase/firestore"; 

try {
  const docRef = await addDoc(collection(db, "users"), {
    first: "Ada",
    last: "Lovelace",
    born: 1815
  });
  console.log("Document written with ID: ", docRef.id);
} catch (e) {
  console.error("Error adding document: ", e);
}
```

### Web

> [!NOTE]
> [Learn
> more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.

```javascript
db.collection("users").add({
    first: "Ada",
    last: "Lovelace",
    born: 1815
})
.then((docRef) => {
    console.log("Document written with ID: ", docRef.id);
})
.catch((error) => {
    console.error("Error adding document: ", error);
});
```

##### Swift

**Note:** This product is not available on watchOS and App Clip targets.

```swift
// Add a new document with a generated ID
do {
  let ref = try await db.collection("users").addDocument(data: [
    "first": "Ada",
    "last": "Lovelace",
    "born": 1815
  ])
  print("Document added with ID: \(ref.documentID)")
} catch {
  print("Error adding document: \(error)")
}
```

### Kotlin

```kotlin
// Create a new user with a first and last name
val user = hashMapOf(
    "first" to "Ada",
    "last" to "Lovelace",
    "born" to 1815,
)

// Add a new document with a generated ID
db.collection("users")
    .add(user)
    .addOnSuccessListener { documentReference ->
        Log.d(TAG, "DocumentSnapshot added with ID: ${documentReference.id}")
    }
    .addOnFailureListener { e ->
        Log.w(TAG, "Error adding document", e)
    }
```

### Java

```java
// Create a new user with a first and last name
Map<String, Object> user = new HashMap<>();
user.put("first", "Ada");
user.put("last", "Lovelace");
user.put("born", 1815);

// Add a new document with a generated ID
db.collection("users")
        .add(user)
        .addOnSuccessListener(new OnSuccessListener<DocumentReference>() {
            @Override
            public void onSuccess(DocumentReference documentReference) {
                Log.d(TAG, "DocumentSnapshot added with ID: " + documentReference.getId());
            }
        })
        .addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception e) {
                Log.w(TAG, "Error adding document", e);
            }
        });
```

Now add another document to the `users` collection. Notice that this document
includes a key-value pair (middle name) that does not appear in the first
document. Documents in a collection can contain different sets of information.

### Web

```javascript
// Add a second document with a generated ID.
import { addDoc, collection } from "firebase/firestore"; 

try {
  const docRef = await addDoc(collection(db, "users"), {
    first: "Alan",
    middle: "Mathison",
    last: "Turing",
    born: 1912
  });

  console.log("Document written with ID: ", docRef.id);
} catch (e) {
  console.error("Error adding document: ", e);
}
```

### Web

> [!NOTE]
> [Learn
> more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.

```javascript
// Add a second document with a generated ID.
db.collection("users").add({
    first: "Alan",
    middle: "Mathison",
    last: "Turing",
    born: 1912
})
.then((docRef) => {
    console.log("Document written with ID: ", docRef.id);
})
.catch((error) => {
    console.error("Error adding document: ", error);
});
```

##### Swift

**Note:** This product is not available on watchOS and App Clip targets.

```swift
// Add a second document with a generated ID.
do {
  let ref = try await db.collection("users").addDocument(data: [
    "first": "Alan",
    "middle": "Mathison",
    "last": "Turing",
    "born": 1912
  ])
  print("Document added with ID: \(ref.documentID)")
} catch {
  print("Error adding document: \(error)")
}
```

### Kotlin

```kotlin
// Create a new user with a first, middle, and last name
val user = hashMapOf(
    "first" to "Alan",
    "middle" to "Mathison",
    "last" to "Turing",
    "born" to 1912,
)

// Add a new document with a generated ID
db.collection("users")
    .add(user)
    .addOnSuccessListener { documentReference ->
        Log.d(TAG, "DocumentSnapshot added with ID: ${documentReference.id}")
    }
    .addOnFailureListener { e ->
        Log.w(TAG, "Error adding document", e)
    }
```

### Java

```java
// Create a new user with a first, middle, and last name
Map<String, Object> user = new HashMap<>();
user.put("first", "Alan");
user.put("middle", "Mathison");
user.put("last", "Turing");
user.put("born", 1912);

// Add a new document with a generated ID
db.collection("users")
        .add(user)
        .addOnSuccessListener(new OnSuccessListener<DocumentReference>() {
            @Override
            public void onSuccess(DocumentReference documentReference) {
                Log.d(TAG, "DocumentSnapshot added with ID: " + documentReference.getId());
            }
        })
        .addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception e) {
                Log.w(TAG, "Error adding document", e);
            }
        });
```

## Read data using Core operations

Use the data viewer in the
[Firebase console](https://console.firebase.google.com/project/_/firestore/data)
to quickly verify that you've added data to Cloud Firestore.

You can also use the "get" method to retrieve the entire collection.

### Web

```javascript
import { collection, getDocs } from "firebase/firestore"; 

const querySnapshot = await getDocs(collection(db, "users"));
querySnapshot.forEach((doc) => {
  console.log(`${doc.id} => ${doc.data()}`);
});
```

### Web

> [!NOTE]
> [Learn
> more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.

```javascript
db.collection("users").get().then((querySnapshot) => {
    querySnapshot.forEach((doc) => {
        console.log(`${doc.id} => ${doc.data()}`);
    });
});
```

##### Swift

**Note:** This product is not available on watchOS and App Clip targets.

```swift
do {
  let snapshot = try await db.collection("users").getDocuments()
  for document in snapshot.documents {
    print("\(document.documentID) => \(document.data())")
  }
} catch {
  print("Error getting documents: \(error)")
}
```

### Kotlin

```kotlin
db.collection("users")
    .get()
    .addOnSuccessListener { result ->
        for (document in result) {
            Log.d(TAG, "${document.id} => ${document.data}")
        }
    }
    .addOnFailureListener { exception ->
        Log.w(TAG, "Error getting documents.", exception)
    }
```

### Java

```java
db.collection("users")
        .get()
        .addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
            @Override
            public void onComplete(@NonNull Task<QuerySnapshot> task) {
                if (task.isSuccessful()) {
                    for (QueryDocumentSnapshot document : task.getResult()) {
                        Log.d(TAG, document.getId() + " => " + document.getData());
                    }
                } else {
                    Log.w(TAG, "Error getting documents.", task.getException());
                }
            }
        });
```

## Read data using Pipeline operations

Now you can compare the Pipeline query experience with the Core query
experience.

### Web

```javascript
// The import/require of "firebase/firestore/pipelines" has a side-effect
// of extending the Firestore class with the `.pipeline()` method.
// Without this import/require, you will not be able to create a Pipeline.
// import { execute } from "firebase/firestore/pipelines";
const readDataPipeline = db.pipeline()
  .collection("users");

// Execute the pipeline and handle the result
try {
  const querySnapshot = await execute(readDataPipeline);
  querySnapshot.results.forEach((result) => {
    console.log(`${result.id} => ${result.data()}`);
  });
} catch (error) {
    console.error("Error getting documents: ", error);
}
```

##### Swift

```swift
do {
  // Initialize a Firestore Pipeline instance and specify the "users" collection as the
  // input stage.
  let snapshot = try await db.pipeline()
    .collection("users")
    .execute() // Execute the pipeline to retrieve documents.

  // Iterate through the documents in the pipeline results, similar to a regular query
  // snapshot.
  for result in snapshot.results {
    print("\(result.id ?? "no ID") => \(result.data)")
  }
} catch {
  print("Error getting documents with pipeline: \(error)")
}
```

### Kotlin

```kotlin
val readDataPipeline = db.pipeline()
    .collection("users")

// Execute the pipeline and handle the result
readDataPipeline.execute()
    .addOnSuccessListener { result ->
        for (document in result) {
            println("${document.getId()} => ${document.getData()}")
        }
    }
    .addOnFailureListener { exception ->
        println("Error getting documents: $exception")
    }
```

### Java

```java
Pipeline readDataPipeline = db.pipeline()
.collection("users");

readDataPipeline.execute()
.addOnSuccessListener(new OnSuccessListener<Pipeline.Snapshot>() {
    @Override
    public void onSuccess(Pipeline.Snapshot snapshot) {
        for (PipelineResult result : snapshot.getResults()) {
            System.out.println(result.getId() + " => " + result.getData());
        }
    }
})
.addOnFailureListener(new OnFailureListener() {
    @Override
    public void onFailure(@NonNull Exception e) {
        System.out.println("Error getting documents: " + e);
    }
});
```

## Secure your data for mobile and web SDKs

If you're using the web, Android, or Apple platforms SDK, use [Firebase
Authentication](https://firebase.google.com/docs/auth/) and
[Cloud Firestore Security Rules](https://firebase.google.com/docs/firestore/security/get-started) to secure your data in
Cloud Firestore.

Here are some basic rule sets you can use to get started. You can modify your
security rules in the [**Rules
tab**](https://console.firebase.google.com/project/_/firestore/rules) of
the console.

### Auth required

    // Allow read/write access to a document keyed by the user's UID
    service cloud.firestore {
      match /databases/{database}/documents {
        match /users/{uid} {
          allow read, write: if request.auth != null && request.auth.uid == uid;
        }
      }
    }

### Production mode

    // Deny read/write access to all users under any conditions
    service cloud.firestore {
      match /databases/{database}/documents {
        match /{document=**} {
          allow read, write: if false;
        }
      }
    }

Before you deploy your web, Android, or iOS app to production, also take steps
to ensure that only your app clients can access your Cloud Firestore data.
See the [App Check](https://firebase.google.com/docs/app-check) documentation.

If you're using one of the server SDKs, use [Identity and Access Management
(IAM)](https://cloud.google.com/firestore/docs/security/iam) to secure your data
in Cloud Firestore.

## Next steps

Deepen your knowledge of Core and Pipeline operations with the following topics:

- Learn more about querying with [Core operations](https://firebase.google.com/docs/firestore/enterprise/get-data-core)
- Learn more about querying with [Pipeline operations](https://firebase.google.com/docs/firestore/pipelines/get-started-with-pipelines).