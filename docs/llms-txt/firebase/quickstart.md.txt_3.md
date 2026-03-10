# Source: https://firebase.google.com/docs/firestore/quickstart.md.txt

This quickstart shows you how to set up Cloud Firestore, add data, then view
the data you just added in the Firebase console.

Cloud Firestore supports mobile or web SDKs and server client libraries:

- Cloud Firestore supports **SDKs for Android, iOS, and web and more** . Combined with
  Cloud Firestore Security Rules and Firebase Authentication, the mobile and web SDKs support
  serverless app architectures where clients connect directly to your
  Cloud Firestore database.

- Cloud Firestore supports **server client libraries** for C#, Go, Java, Node.js, PHP,
  Python, and Ruby. Use these client libraries to set up privileged server
  environments with full access to your database. Learn more about these libraries
  in the [Quickstart for server client libraries](https://firebase.google.com/docs/firestore/quickstart-server).

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
       sure to review the [Secure your data](https://firebase.google.com/docs/firestore/quickstart#secure_your_data) section.**

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

### Web

1. Follow the instructions to [add Firebase to your web app](https://firebase.google.com/docs/web/setup).
2. Add the Firebase and Cloud Firestore libraries to your app:

   ```
   <script src="https://www.gstatic.com/firebasejs/12.10.0/firebase-app-compat.js"></script>
   <script src="https://www.gstatic.com/firebasejs/12.10.0/firebase-firestore-compat.js"></script>
   ```
   The Cloud Firestore SDK is also available as an npm package.

   ```
   npm install firebase@12.10.0 --save
   ```
   You'll need to manually require both Firebase and Cloud Firestore.

   ```
   import firebase from "firebase/compat/app";
   // Required for side-effects
   import "firebase/firestore";
   ```

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

### Dart

1. If you haven't already, [configure and
   initialize Firebase](https://firebase.google.com/docs/flutter/setup) in your Flutter app.
2. From the root of your Flutter project, run the following command to install the plugin:

   ```
   flutter pub add cloud_firestore
   ```
3. Once complete, rebuild your Flutter application:

   ```
   flutter run
   ```
4. **Optional:** Improve iOS \& macOS build times by including the pre-compiled framework.

   Currently, the Firestore SDK for iOS depends on code that can take
   upwards of 5 minutes to build in Xcode. To reduce build times
   significantly, you can use a pre-compiled version by adding this line to
   the `target 'Runner' do` block in your Podfile:

   ```
   target 'Runner' do
     use_frameworks!
     use_modular_headers!

     pod 'FirebaseFirestore',
       :git => 'https://github.com/invertase/firestore-ios-sdk-frameworks.git',
       :tag => 'IOS_SDK_VERSION'

     flutter_install_all_ios_pods File.dirname(File.realpath(__FILE__))
     target 'RunnerTests' do
       inherit! :search_paths
     end
   end
   ```

   Replace <var translate="no">IOS_SDK_VERSION</var> with the version of the Firebase iOS
   SDK specified in `firebase_core`'s
   [`firebase_sdk_version.rb`](https://github.com/firebase/flutterfire/blob/main/packages/firebase_core/firebase_core/ios/firebase_sdk_version.rb#L3)
   file. If you're not using the latest version of
   `firebase_core`, look for this file in your local Pub package
   cache (usually `~/.pub-cache`).

   Additionally, ensure that you have upgraded CocoaPods to 1.9.1 or
   higher:

   ```
   gem install cocoapods
   ```

   <br />

   For more information see the
   [issue
   on GitHub](https://github.com/FirebaseExtended/flutterfire/issues/2751).

##### C++

1. Follow the instructions to [add Firebase to your C++ project](https://firebase.google.com/docs/cpp/setup).
2. **C++ interface for Android.**
   - **Gradle dependencies.** Add the following to your module (app-level) Gradle file (usually `app/build.gradle`):

     ```c++
             android.defaultConfig.externalNativeBuild.cmake {
               arguments "-DFIREBASE_CPP_SDK_DIR=$gradle.firebase_cpp_sdk_dir"
             }

             apply from: "$gradle.firebase_cpp_sdk_dir/Android/firebase_dependencies.gradle"
             firebaseCpp.dependencies {
               // earlier entries
               auth
               firestore
             }
             
     ```
   - **Binary dependencies.** Similarly, the recommended way to get the binary dependencies is to add the following to your `CMakeLists.txt` file:

     ```c++
             add_subdirectory(${FIREBASE_CPP_SDK_DIR} bin/ EXCLUDE_FROM_ALL)
             set(firebase_libs firebase_auth firebase_firestore firebase_app)
             # Replace the target name below with the actual name of your target,
             # for example, "native-lib".
             target_link_libraries(${YOUR_TARGET_NAME_HERE} "${firebase_libs}")
             
     ```
3. To set up **desktop integration** , see [Add Firebase to your C++ project](https://firebase.google.com/docs/cpp/setup#desktop-workflow).

##### Unity

1. Follow the instructions to [add Firebase to your Unity
   project](https://firebase.google.com/docs/unity/setup).
2. Use the Unity interface to configure your project to minify Android builds.
3. You must minify the build to avoid the message `Error while merging dex archives`.
   - The option can be found in **Player Settings \> Android \> Publishing
     Settings \> Minify**.
   - The options may differ in different versions of Unity so refer to the official [Unity documentation](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#minify) and the [Firebase Unity Build Debug Guide](https://firebase.google.com/docs/unity/build-debug-guide#single_dex_issues_and_minification_mandatory_if_using_cloud_firestore).
   - If, after enabling minification, the number of referenced methods still exceeds the limit, another option is to enable `multidex` in:
     - `mainTemplate.gradle` if **Custom Gradle Template** under **Player Settings** is enabled
     - or, the module-level `build.gradle` file, if you use Android Studio to build the exported project.

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


// Initialize Cloud Firestore and get a reference to the service
const db = getFirestore(app);
```


Replace <var translate="no">FIREBASE_CONFIGURATION</var> with your web app's
[`firebaseConfig`](https://support.google.com/firebase/answer/7015592).


To persist data when the device loses its connection, see the [Enable Offline Data](https://firebase.google.com/docs/firestore/manage-data/enable-offline) documentation.

### Web

```
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


Replace <var translate="no">FIREBASE_CONFIGURATION</var> with your web app's
[`firebaseConfig`](https://support.google.com/firebase/answer/7015592).


To persist data when the device loses its connection, see the [Enable Offline Data](https://firebase.google.com/docs/firestore/manage-data/enable-offline) documentation.

##### Swift

**Note:** This product is not available on watchOS and App Clip targets.

```
import FirebaseCore
import FirebaseFirestore
```

```swift
FirebaseApp.configure()

let db = Firestore.firestore()
```

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets.

```
@import FirebaseCore;
@import FirebaseFirestore;

// Use Firebase library to configure APIs
[FIRApp configure];
  
```

```objective-c
FIRFirestore *defaultFirestore = [FIRFirestore firestore];
```

### Kotlin

```kotlin
// Access a Cloud Firestore instance from your Activity
```

```kotlin
val db = Firebase.firestorehttps://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L109-L109
```

### Java

```java
// Access a Cloud Firestore instance from your Activity
```

```java
FirebaseFirestore db = FirebaseFirestore.getInstance();
```

### Dart

```dart
db = FirebaseFirestore.instance;
```

##### C++

```c++
// Make sure the call to `Create()` happens some time before you call Firestore::GetInstance().
App::Create();
Firestore* db = Firestore::GetInstance();
```

##### Unity

```c#
using Firebase.Firestore;
using Firebase.Extensions;
```

```c#
FirebaseFirestore db = FirebaseFirestore.DefaultInstance;
```

## Add data

Cloud Firestore stores data in Documents, which are stored in Collections.
Cloud Firestore creates collections and documents implicitly
the first time you add data to the document. You do not need to explicitly
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

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets.

```objective-c
// Add a new document with a generated ID
__block FIRDocumentReference *ref =
    [[self.db collectionWithPath:@"users"] addDocumentWithData:@{
      @"first": @"Ada",
      @"last": @"Lovelace",
      @"born": @1815
    } completion:^(NSError * _Nullable error) {
      if (error != nil) {
        NSLog(@"Error adding document: %@", error);
      } else {
        NSLog(@"Document added with ID: %@", ref.documentID);
      }
    }];
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

### Dart

```dart
// Create a new user with a first and last name
final user = <String, dynamic>{
  "first": "Ada",
  "last": "Lovelace",
  "born": 1815
};

// Add a new document with a generated ID
db.collection("users").add(user).then((DocumentReference doc) =>
    print('DocumentSnapshot added with ID: ${doc.id}'));
```

##### C++

```c++
// Add a new document with a generated ID
Future<DocumentReference> user_ref =
    db->Collection("users").Add({{"first", FieldValue::String("Ada")},
                                 {"last", FieldValue::String("Lovelace")},
                                 {"born", FieldValue::Integer(1815)}});

user_ref.OnCompletion([](const Future<DocumentReference>& future) {
  if (future.error() == Error::kErrorOk) {
    std::cout << "DocumentSnapshot added with ID: " << future.result()->id()
              << std::endl;
  } else {
    std::cout << "Error adding document: " << future.error_message() << std::endl;
  }
});
```

##### Unity

```c#
DocumentReference docRef = db.Collection("users").Document("alovelace");
Dictionary<string, object> user = new Dictionary<string, object>
{
	{ "First", "Ada" },
	{ "Last", "Lovelace" },
	{ "Born", 1815 },
};
docRef.SetAsync(user).ContinueWithOnMainThread(task => {
	Debug.Log("Added data to the alovelace document in the users collection.");
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

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets.

```objective-c
// Add a second document with a generated ID.
__block FIRDocumentReference *ref =
    [[self.db collectionWithPath:@"users"] addDocumentWithData:@{
      @"first": @"Alan",
      @"middle": @"Mathison",
      @"last": @"Turing",
      @"born": @1912
    } completion:^(NSError * _Nullable error) {
      if (error != nil) {
        NSLog(@"Error adding document: %@", error);
      } else {
        NSLog(@"Document added with ID: %@", ref.documentID);
      }
    }];
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

### Dart

```dart
// Create a new user with a first and last name
final user = <String, dynamic>{
  "first": "Alan",
  "middle": "Mathison",
  "last": "Turing",
  "born": 1912
};

// Add a new document with a generated ID
db.collection("users").add(user).then((DocumentReference doc) =>
    print('DocumentSnapshot added with ID: ${doc.id}'));
```

##### C++

```c++
db->Collection("users")
    .Add({{"first", FieldValue::String("Alan")},
          {"middle", FieldValue::String("Mathison")},
          {"last", FieldValue::String("Turing")},
          {"born", FieldValue::Integer(1912)}})
    .OnCompletion([](const Future<DocumentReference>& future) {
      if (future.error() == Error::kErrorOk) {
        std::cout << "DocumentSnapshot added with ID: "
                  << future.result()->id() << std::endl;
      } else {
        std::cout << "Error adding document: " << future.error_message()
                  << std::endl;
      }
    });
```

##### Unity

```c#
DocumentReference docRef = db.Collection("users").Document("aturing");
Dictionary<string, object> user = new Dictionary<string, object>
{
	{ "First", "Alan" },
	{ "Middle", "Mathison" },
	{ "Last", "Turing" },
	{ "Born", 1912 }
};
docRef.SetAsync(user).ContinueWithOnMainThread(task => {
	Debug.Log("Added data to the aturing document in the users collection.");
});
```

## Read data

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

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets.

```objective-c
[[self.db collectionWithPath:@"users"]
    getDocumentsWithCompletion:^(FIRQuerySnapshot * _Nullable snapshot,
                                 NSError * _Nullable error) {
      if (error != nil) {
        NSLog(@"Error getting documents: %@", error);
      } else {
        for (FIRDocumentSnapshot *document in snapshot.documents) {
          NSLog(@"%@ => %@", document.documentID, document.data);
        }
      }
    }];
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

### Dart

```dart
await db.collection("users").get().then((event) {
  for (var doc in event.docs) {
    print("${doc.id} => ${doc.data()}");
  }
});
```

##### C++

```c++
Future<QuerySnapshot> users = db->Collection("users").Get();
users.OnCompletion([](const Future<QuerySnapshot>& future) {
  if (future.error() == Error::kErrorOk) {
    for (const DocumentSnapshot& document : future.result()->documents()) {
      std::cout << document << std::endl;
    }
  } else {
    std::cout << "Error getting documents: " << future.error_message()
              << std::endl;
  }
});
```

##### Unity

```c#
CollectionReference usersRef = db.Collection("users");
usersRef.GetSnapshotAsync().ContinueWithOnMainThread(task =>
{
  QuerySnapshot snapshot = task.Result;
  foreach (DocumentSnapshot document in snapshot.Documents)
  {
    Debug.Log(String.Format("User: {0}", document.Id));
    Dictionary<string, object> documentDictionary = document.ToDictionary();
    Debug.Log(String.Format("First: {0}", documentDictionary["First"]));
    if (documentDictionary.ContainsKey("Middle"))
    {
      Debug.Log(String.Format("Middle: {0}", documentDictionary["Middle"]));
    }

    Debug.Log(String.Format("Last: {0}", documentDictionary["Last"]));
    Debug.Log(String.Format("Born: {0}", documentDictionary["Born"]));
  }

  Debug.Log("Read all data from the users collection.");
});
```

## Secure your data

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

## Watch a video tutorial

For detailed guidance on getting started with the Cloud Firestore
mobile client libraries, watch one of the following video tutorials:

##### Web

[Video](https://www.youtube.com/watch?v=BjtxPj6jRM8)

##### iOS+

[Video](https://www.youtube.com/watch?v=Cp3XPcOD4kY)

##### Android

[Video](https://www.youtube.com/watch?v=kDZYIhNkQoM)

You can find more videos in the Firebase
[YouTube channel](https://www.youtube.com/firebase).

## Next steps

Deepen your knowledge with the following topics:

- **Codelabs** --- Learn to use Cloud Firestore in a real app by following the codelab for [Android](https://codelabs.developers.google.com/codelabs/firestore-android), [iOS](https://codelabs.developers.google.com/codelabs/firestore-ios), or [web](https://codelabs.developers.google.com/codelabs/firestore-web).
- **[Data model](https://firebase.google.com/docs/firestore/data-model)** --- Learn more about how data is structured in Cloud Firestore, including hierarchical data and subcollections.
- **[Add data](https://firebase.google.com/docs/firestore/manage-data/add-data)** --- Learn more about creating and updating data in Cloud Firestore.
- **[Get data](https://firebase.google.com/docs/firestore/query-data/get-data)** --- Learn more about how to retrieve data.
- **[Perform simple and compound queries](https://firebase.google.com/docs/firestore/query-data/queries)** --- Learn how to run simple and compound queries.
- **[Order and limit queries](https://firebase.google.com/docs/firestore/query-data/order-limit-data)** Learn how to order and limit the data returned by your queries.