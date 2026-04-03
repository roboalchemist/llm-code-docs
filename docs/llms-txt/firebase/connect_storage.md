# Source: https://firebase.google.com/docs/emulator-suite/connect_storage.md.txt

<br />

Before connecting your app to theCloud Storage for Firebaseemulator, make sure that you[understand the overallFirebase Local Emulator Suiteworkflow](https://firebase.google.com/docs/emulator-suite/connect_and_prototype?database=Firestore), and that you[install and configure](https://firebase.google.com/docs/emulator-suite/install_and_configure)theLocal Emulator Suiteand review its[CLI commands](https://firebase.google.com/docs/emulator-suite/install_and_configure#startup).

## Choose a Firebase project

TheFirebase Local Emulator Suiteemulates products for a single Firebase project.

To select the project to use, before you start the emulators, in the CLI run`firebase use`in your working directory. Or, you can pass the`--project`flag to each emulator command.
| **Note:** It's generally a good practice to use one project ID for all emulator invocations, so theEmulator Suite UI, different product emulators, and all running instances of a particular emulator can communicate correctly in all cases. In fact, by default, theLocal Emulator Suitewill warn on detecting multiple project IDs in use, though you can override this behavior. For guidance on setting and managing project IDs, see the[Installation and configuration guide](https://firebase.google.com/docs/emulator-suite/install_and_configure#project_id_configuration).

Local Emulator Suitesupports emulation of*real* Firebase projects and*demo*projects.

| Project type |                                                                                                                      Features                                                                                                                       |                                                                                                                       Use with emulators                                                                                                                       |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Real         | A real Firebase project is one you created and configured (most likely via theFirebaseconsole). Real projects have live resources, like database instances, storage buckets, functions, or any other resource you set up for that Firebase project. | When working with real Firebase projects, you can run emulators for any or all of the supported products. For any products you are not emulating, your apps and code will interact with the*live*resource (database instance, storage bucket, function, etc.). |
| Demo         | A demo Firebase project has no*real*Firebase configuration and no live resources. These projects are usually accessed via codelabs or other tutorials. Project IDs for demo projects have the`demo-`prefix.                                         | When working with demo Firebase projects, your apps and code interact with emulators*only*. If your app attempts to interact with a resource for which an emulator isn't running, that code will fail.                                                         |

We recommend you use demo projects wherever possible. Benefits include:

- Easier setup, since you can run the emulators without ever creating a Firebase project
- Stronger safety, since if your code accidentally invokes non-emulated (production) resources, there is no chance of data change, usage and billing
- Better offline support, since there is no need to access the internet to download your SDK configuration.

| **Note:** If you want to emulate cross-service interactions such as database-triggeredCloud FunctionsorRulesthat rely onAuthenticationyou must make sure that the project ID in your code (in`initializeApp()`, etc.) matches the project ID used by theFirebaseCLI.

## Instrument your app to talk to the emulators

### Android, Apple platforms, and Web SDKs

Set up your in-app configuration or test classes to interact with theCloud Storage for Firebaseemulator as follows.  

##### Kotlin

```kotlin
// 10.0.2.2 is the special IP address to connect to the 'localhost' of
// the host computer from an Android emulator.
val storage = Firebase.storage
storage.useEmulator("10.0.2.2", 9199)https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/EmulatorSuite.kt#L10-L13
```

##### Java

```java
// 10.0.2.2 is the special IP address to connect to the 'localhost' of
// the host computer from an Android emulator.
FirebaseStorage storage = FirebaseStorage.getInstance();
storage.useEmulator("10.0.2.2", 9199);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/storage/app/src/main/java/com/google/firebase/referencecode/storage/EmulatorSuite.java#L9-L12
```

##### Swift

```swift
Storage.storage().useEmulator(withHost: "127.0.0.1", port: 9199)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/storage/StorageReferenceSwift/ViewController.swift#L661-L661
```

### Web

```javascript
const { getStorage, connectStorageEmulator } = require("firebase/storage");

const storage = getStorage();
if (location.hostname === "localhost") {
  // Point to the Storage emulator running on localhost.
  connectStorageEmulator(storage, "127.0.0.1", 9199);
} https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/storage-next/emulator-suite.js#L6-L12
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
var storage = firebase.storage();
if (location.hostname === "localhost") {
  // Point to the Storage emulator running on localhost.
  storage.useEmulator("127.0.0.1", 9199);
} https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/storage/emulator-suite.js#L9-L13
```

No additional setup is needed to test Cloud functions[triggered byCloud Storage for Firebaseevents](https://firebase.google.com/docs/storage/extend-with-functions)using the emulator. When theCloud Storage for FirebaseandCloud Functionsemulators are both running, they automatically work together.

### Admin SDKs

TheFirebaseAdmin SDKs automatically connect to theCloud Storage for Firebaseemulator when the`FIREBASE_STORAGE_EMULATOR_HOST`environment variable is set:  

    export FIREBASE_STORAGE_EMULATOR_HOST="127.0.0.1:9199"

| **Note:** For emulators to work correctly the`FIREBASE_STORAGE_EMULATOR_HOST`environment variable must omit protocols such as`http://`.

Note that theCloud Functionsemulator is automatically aware of theCloud Storage for Firebaseemulator so you can skip this step when testing integrations betweenCloud FunctionsandCloud Storage for Firebaseemulators. The environment variable will be automatically set for the Admin SDK inCloud Storage for Firebase.

If you want yourAdmin SDKcode to connect to a shared emulator running in another environment, you will need to specify the[the same project ID you set using the Firebase CLI](https://firebase.google.com/docs/emulator-suite/connect_storage#choose_a_firebase_project). You can pass a project ID to`initializeApp`directly or set the`GCLOUD_PROJECT`environment variable.  

##### Node.js Admin SDK

```javascript
admin.initializeApp({ projectId: "your-project-id" });
```

##### Environment Variable

```gdscript
export GCLOUD_PROJECT="your-project-id"
```

## Import and export data

The database andCloud Storage for Firebaseemulators allow you to export data from a running emulator instance. Define a baseline set of data to use in your unit tests or continuous integration workflows, then export it to be shared among the team.  

    firebase emulators:export ./dir

In tests, on emulator startup, import the baseline data.  

    firebase emulators:start --import=./dir

You can instruct the emulator to export data on shutdown, either specifying an export path or simply using the path passed to the`--import`flag.  

    firebase emulators:start --import=./dir --export-on-exit

These data import and export options work with the`firebase emulators:exec`command as well. For more, refer to the[emulator command reference](https://firebase.google.com/docs/emulator-suite/install_and_configure#startup).

## How theCloud Storage for Firebaseemulator differs from production

For testing of client apps, theCloud Storage for Firebaseemulator aligns to production almost perfectly in regards to the Firebase API surface area. All Firebase commands are expected to work between the regular Firebase SDKs (Web, Android, and Apple platforms).

For testing of server-side apps, limitations exist. The Firebase Admin SDKs make use theGoogle CloudAPI surface, and not all endpoints of this API are emulated. As a rule of thumb, anything which can be done from the client SDKs (uploading or deleting files, getting and setting metadata) is also implemented for use from the Admin SDKs, but anything beyond that is not. Notable exclusions are listed below.

### Differences from Google Cloud Storage

TheCloud Storage for Firebaseproduct, including the Storage emulator, provides a subset of Google Cloud Storage (GCS) functionality focusing on storage objects that is very useful for developing Firebase apps.Cloud Storage for Firebasediffers from GCS in the following ways:

- Cloud Storage for Firebasedoes not currently support`Bucket`APIs for creating, listing, getting, or deleting storage buckets.
- From the[Google Cloud Storage Objects API](https://cloud.google.com/storage/docs/json_api/v1/objects#methods), the following methods are supported:`copy`,`delete`,`get`,`insert`,`list`,`patch`,`rewrite`,`update`.

### Cloud IAM

The Firebase Emulator Suite does not attempt to replicate or respect any IAM-related behavior for running. Emulators adhere to the Firebase Security Rules provided, but in situations where IAM would normally be used, for example to set Cloud Functions invoking service account and thus permissions, the emulator is not configurable and will use the globally-available account on your developer machine, similar to running a local script directly.

### Pub/Sub notifications

TheCloud Storage for Firebaseemulator does not integrate with the CloudPub/Subemulator and thus does not support creating channels/notifications for storage object changes. We recommend usingCloud FunctionsStorage triggers directly.

### Bucket-level metadata

TheCloud Storage for Firebaseemulator does not support any bucket-level configuration including storage class, bucket-level CORS configuration, labels, or retention policies. Firebase intends to improve this support over time.

## What next?

- For a curated set of videos and detailed how-to examples, follow the[Firebase Emulators Training Playlist](https://firebase.google.com/learn/pathways/firebase-emulators).
- Since triggered functions are a typical integration withCloud Storage for Firebase, learn more about theCloud Functions for Firebaseemulator at[Run functions locally](https://firebase.google.com/docs/functions/local-emulator).