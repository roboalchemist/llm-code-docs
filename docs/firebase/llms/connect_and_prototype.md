# Source: https://firebase.google.com/docs/emulator-suite/connect_and_prototype.md.txt

<br />

Cloud FirestoreRealtime Database  

<br />

Before you jump in withFirebase Local Emulator Suite, make sure you've created a Firebase project, set up your development environment, and selected and installed Firebase SDKs for your platform according to the**Get started with Firebase** topics for your platform:[Apple](https://firebase.google.com/docs/ios/setup),[Android](https://firebase.google.com/docs/android/setup)or[Web](https://firebase.google.com/docs/web/setup).

## Prototype and test

| **Note:** Before you explore Firebase Local Emulator Suite, we recommend you get oriented to Firebase products and the Firebase development model. After reading the**Get started** for your platform, download a ready-to-run quickstart app on your platform of choice, then read through and execute the code. The FriendlyEats quickstart app is a good choice ([iOS](https://github.com/firebase/friendlyeats-ios),[Android](https://github.com/firebase/friendlyeats-android)or[Web](https://github.com/firebase/friendlyeats-web)).

TheLocal Emulator Suitecontains several product emulators, as described in[Introduction toFirebase Local Emulator Suite](https://firebase.google.com/docs/emulator-suite#feature-matrix). You can prototype and test with individual emulators as well as combinations of emulators, as you see fit, corresponding to which Firebase products you're using in production.
![Interaction between Firebase database and functions emulators](https://firebase.google.com/docs/emulator-suite/images/emulator-suite-helloworld-firestore.png)Database andCloud Functionsemulators as part of the[fullLocal Emulator Suite](https://firebase.google.com/docs/emulator-suite#what-is-emulator-suite).

For this topic, to introduce theLocal Emulator Suiteworkflow, let's assume you're working on an app that uses a typical combination of products: a Firebase database and cloud functions triggered by operations on that database.

After you locally initialize your Firebase project, the development cycle usingLocal Emulator Suitewill typically have three steps:

1. Prototype features interactively with the emulators andEmulator Suite UI.

2. If you're using a database emulator or theCloud Functionsemulator, perform a one-time step to connect your app to the emulators.

3. Automate your tests with the emulators and custom scripts.

### Locally initialize a Firebase project

Make sure that you[install the CLI](https://firebase.google.com/docs/cli#install_the_firebase_cli)or[update to its latest version](https://firebase.google.com/docs/cli#update-cli).  

    curl -sL firebase.tools | bash

If you haven't already done so, initialize the current working directory as a Firebase project, following the onscreen prompts to specify you're using**Cloud Functions** and either**Cloud Firestore** or**Realtime Database**:  

    firebase init

Your project directory will now contain Firebase configuration files, aFirebase Security Rulesdefinition file for the database, a`functions`directory containing cloud functions code, and other supporting files.

### Prototype interactively

Local Emulator Suiteis designed to let you quickly prototype new features, and the Suite's built-in user interface is one of its most useful prototyping tools. It's a bit like having theFirebaseconsole running locally.  

UsingEmulator Suite UI, you can iterate the design of a database, try out different dataflows involving cloud functions, evaluate Security Rules changes, check logs to confirm how your back-end services are performing, and more. Then, if you want to start over, just clear your database and start fresh with a new design idea.

It's all available when you start theLocal Emulator Suitewith:  

    firebase emulators:start

To prototype our hypothetical app, let's set up and test a basic cloud function to modify text entries in a database, and both create and populate that database in theEmulator Suite UIto trigger it.

1. Create a cloud function triggered by database writes by editing the`functions/index.js`file in your project directory. Replace the contents of the existing file with the following snippet. This function listens for changes to documents in the`messages`collection, converts the contents of a document's`original`field to uppercase, and stores the result in that document's`uppercase`field.  

```gdscript
  const functions = require('firebase-functions/v1');

  exports.makeUppercase = functions.firestore.document('/messages/{documentId}')
      .onCreate((snap, context) => {
        const original = snap.data().original;
        console.log('Uppercasing', context.params.documentId, original);
        const uppercase = original.toUpperCase();
        return snap.ref.set({uppercase}, {merge: true});
      });
  
```
2. Launch theLocal Emulator Suitewith`firebase emulators:start`. TheCloud Functionsand database emulators start up, automatically configured to interoperate.
3. View the UI in your browser at`http://localhost:4000`. Port 4000 is the default for the UI, but check terminal messages output by theFirebaseCLI. Note the status of available emulators. In our case, theCloud FunctionsandCloud Firestoreemulators will be running.  
   View UI's main page![My image](https://firebase.google.com/docs/emulator-suite/images/emulator-suite-gui.png)
4. In the UI, on the*Firestore \> Data* tab, click**Start collection** and follow the prompts to create a new document in a`messages`collection, with fieldname`original`and value`test`. This triggers our cloud function. Observe that a new`uppercase`field appears shortly, populated with the string "TEST".  
   View how to create a collectionView updates from the function![My image](https://firebase.google.com/docs/emulator-suite/images/emulator-suite-newfirestorecollection.png)![My image](https://firebase.google.com/docs/emulator-suite/images/emulator-suite-touppercaseresult.png)
5. On the*Firestore \> Requests* tab, examine requests made to your emulated database, including allFirebase Security Rulesevaluations performed as part of fulfilling those requests.
6. Check the*Logs*tab to confirm your function did not run into errors as it updated the database.

You can easily iterate between your cloud function code and interactive database edits until you get the data flow you're looking for, without touching in-app database access code, recompiling and re-running test suites.

### Connect your app to the emulators

When you've made good progress with interactive prototyping and have settled on a design, you'll be ready to add database access code to your app using the appropriate SDK. You'll keep using the database tab and, for functions, the*Logs* tab inEmulator Suite UIto confirm that your app's behavior is correct.

Remember that theLocal Emulator Suiteis a local development tool. Writes to your production databases will not trigger functions you are prototyping locally.

To switch over to having your app make writes to the database, you'll need to point your test classes or in-app configuration at theCloud Firestoreemulator.
**Note:** TheCloud Firestoreemulator clears database contents when shut down. Since the offline cache of the Firestore SDK is not automatically cleared, you may want to disable local persistence in your emulator configuration to avoid discrepancies between the emulated database and local caches; in the Web SDK, persistence is disabled by default.  

##### Kotlin

```kotlin
// 10.0.2.2 is the special IP address to connect to the 'localhost' of
// the host computer from an Android emulator.
val firestore = Firebase.firestore
firestore.useEmulator("10.0.2.2", 8080)

firestore.firestoreSettings = firestoreSettings {
    isPersistenceEnabled = false
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/firestore/app/src/main/java/com/google/example/firestore/kotlin/EmulatorSuite.kt#L11-L18
```

##### Java

```java
// 10.0.2.2 is the special IP address to connect to the 'localhost' of
// the host computer from an Android emulator.
FirebaseFirestore firestore = FirebaseFirestore.getInstance();
firestore.useEmulator("10.0.2.2", 8080);

FirebaseFirestoreSettings settings = new FirebaseFirestoreSettings.Builder()
        .setPersistenceEnabled(false)
        .build();
firestore.setFirestoreSettings(settings);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/firestore/app/src/main/java/com/google/example/firestore/EmulatorSuite.java#L10-L18
```

##### Swift

```swift
let settings = Firestore.firestore().settings
settings.host = "127.0.0.1:8080"
settings.cacheSettings = MemoryCacheSettings()
settings.isSSLEnabled = false
Firestore.firestore().settings = settings  
https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L1265-L1269
```

### Web

```javascript
import { getFirestore, connectFirestoreEmulator } from "firebase/firestore";

// firebaseApps previously initialized using initializeApp()
const db = getFirestore();
connectFirestoreEmulator(db, '127.0.0.1', 8080);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/emulator-suite/fs_emulator_connect.js#L8-L12
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
// Firebase previously initialized using firebase.initializeApp().
var db = firebase.firestore();
if (location.hostname === "localhost") {
  db.useEmulator("127.0.0.1", 8080);
}https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/emulator-suite.js#L6-L10
```

### Automate your tests with custom scripts

Now for the last overall workflow step. Once you've prototyped your feature in-app and it looks promising on all your platforms, you can turn to final implementation and testing. For unit testing and CI workflows, you can start up emulators, run scripted tests, and shut down emulators in a single call with the`exec`command:  

    firebase emulators:exec "./testdir/test.sh"

## Explore individual emulators in more depth

Now that you've seen what the basic client-side workflow looks like, you can continue with details about the individual emulators in the Suite, including how to use them for server-side app development:

- [Add theAuthenticationemulator to your prototyping workflows](https://firebase.google.com/docs/emulator-suite/connect_auth)
- [Learn aboutRealtime Databaseemulator features in depth](https://firebase.google.com/docs/emulator-suite/connect_rtdb)
- [Learn aboutCloud Storage for Firebaseemulator features in depth](https://firebase.google.com/docs/emulator-suite/connect_storage)
- [Learn aboutCloud Firestoreemulator features in depth](https://firebase.google.com/docs/emulator-suite/connect_firestore)
- [Connect your app to the Cloud Functions emulator](https://firebase.google.com/docs/emulator-suite/connect_functions)
- [EvaluateFirebase Extensionswhile minimizing billing costs with theExtensionsemulator](https://firebase.google.com/docs/emulator-suite/use_extensions)

## What next?

Be sure to read the topics related to specific emulators linked above. Then:

- For a curated set of videos and detailed how-to examples, follow the[Firebase Emulators Training Playlist](https://firebase.google.com/learn/pathways/firebase-emulators).
- Investigate advanced use cases involving Security Rules testing and the Firebase Test SDK:[Test Security Rules (Cloud Firestore)](https://firebase.google.com/docs/firestore/security/test-rules-emulator),[Test Security Rules (Realtime Database)](https://firebase.google.com/docs/rules/emulator-setup#realtime-database), and[Test Security Rules (Cloud Storage for Firebase)](https://firebase.google.com/docs/rules/emulator-setup#cloud-storage).