# Source: https://firebase.google.com/docs/rules/unit-tests.md.txt

<br />

TheFirebase Local Emulator Suitemake it easier to fully validate your app's[features and behavior](https://firebase.google.com/docs/emulator-suite/connect_and_prototype). It's also a great tool for verifying yourFirebase Security Rulesconfigurations. Use the Firebase Emulators to run and automate unit tests in a local environment. The methods outlined in this document should help you as you build and automate unit tests for your app that validate yourRules.

If you haven't already,[set up the Firebase Emulators](https://firebase.google.com/docs/rules/emulator-setup).

## Before you run the emulator

Before you start using the emulator, keep in mind the following:

- The emulator will initially load the rules specified in the`firestore.rules`or`storage.rules`field of your`firebase.json`file. If the file does not exist and you don't use the`loadFirestoreRules`or`loadStorageRules`method as described below, the emulator treats all projects as having open rules.
- While[most Firebase SDKs](https://firebase.google.com/docs/emulator-suite#which_firebase_features_and_platforms_are_supported)work with the emulators directly, only the`@firebase/rules-unit-testing`library supports mocking`auth`in Security Rules, making unit tests much easier. In addition, the library supports a few emulator-specific features like clearing all data, as listed below.
- The emulators will also accept production Firebase Auth tokens provided through Client SDKs and evaluate rules accordingly, which allows connecting your application directly to the emulators in integration and manual tests.

### Differences between the database emulators and production

- You do not have to explicitly create a database instance. The emulator will automatically create any database instance that is accessed.
- Each new database is started with closed rules, so non-admin users will not be able to read or write.
- Each emulated database applies the[Spark plan](https://firebase.google.com/pricing/)limits and quotas (most notably, this limits each instance to 100 concurrent connections).
- Any database will accept the string`"owner"`as an admin auth token.
- The emulators do not currently have working interactions with other Firebase products. Notably, the normal Firebase Authentication flow does not work. Instead, you can use the`initializeTestApp()`method in the`rules-unit-testing`library, which takes an`auth`field. The Firebase object created using this method behaves as if it has successfully authenticated as whatever entity you provide. If you pass in`null`, it will behave as an unauthenticated user (`auth != null`rules will fail, for example).

### Interacting with theRealtime Databaseemulator

A production FirebaseRealtime Databaseinstance is accessible at a subdomain of`firebaseio.com`, and you can access the REST api like this:

`https://<database_name>.firebaseio.com/path/to/my/data.json`

The emulator runs locally, and is available at`localhost:9000`. To interact with a specific database instance, you will have to use the`ns`query parameter to specify the database name.

`http://localhost:9000/path/to/my/data.json?ns=<database_name>`

## Run local unit tests with the version 9 JavaScript SDK

Firebase distributes a Security Rules unit testing library with both its version 9 JavaScript SDK and its version 8 SDK. The library APIs are significantly different. We recommend the v9 testing library, which is more streamlined and requires less setup to connect to emulators and thus safely avoid accidental use of production resources. For backwards compatibility, we continue to make the[v8 testing library available](https://firebase.google.com/docs/rules/unit-tests#rut-v1-testing).

- [Common test methods and utility functions in the v9 SDK](https://firebase.google.com/docs/rules/unit-tests#rut-v2-common-methods)
- [Emulator-specific test methods in the v9 SDK](https://firebase.google.com/docs/rules/unit-tests#rut-v2-specific-methods)

Use the`@firebase/rules-unit-testing`module to interact with the emulator that runs locally. If you get timeouts or`ECONNREFUSED`errors, double-check that the emulator is actually running.

We strongly recommend using a recent version of Node.js so you can use`async/await`notation. Almost all of the behavior you might want to test involves asynchronous functions, and the testing module is designed to work with Promise-based code.

The v9 Rules Unit Testing library is always aware of the emulators and never touches your production resources.

You import the library using v9 modular import statements. For example:  

    import {
      assertFails,
      assertSucceeds,
      initializeTestEnvironment
    } from "@firebase/rules-unit-testing"

    // Use `const { ... } = require("@firebase/rules-unit-testing")` if imports are not supported
    // Or we suggest `const testing = require("@firebase/rules-unit-testing")` if necessary.

Once imported, implementing unit tests involves:

- Creating and configuring a`RulesTestEnvironment`with a call to`initializeTestEnvironment`.
- Setting up test data without triggeringRules, using a convenience method that allows you to temporarily bypass them,`RulesTestEnvironment.withSecurityRulesDisabled`.
- Setting up test suite and per-test before/after hooks with calls to clean up test data and environment, like`RulesTestEnvironment.cleanup()`or`RulesTestEnvironment.clearFirestore()`.
- Implementing test cases that mimic authentication states using`RulesTestEnvironment.authenticatedContext`and`RulesTestEnvironment.unauthenticatedContext`.

| **Note:** A summary of the API for the Rules unit testing library is provided below. You can also review the[full API reference documentation](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing).

### Common methods and utility functions

Also see[emulator-specific test methods using the modular API](https://firebase.google.com/docs/rules/unit-tests#rut-v2-specific-methods).

**`initializeTestEnvironment() => RulesTestEnvironment`**

This function initializes a test environment for rules unit testing. Call this function first for test setup. Successful execution requires emulators to be running.

The function accepts an optional object defining a`TestEnvironmentConfig`, which can consist of a project ID and emulator configuration settings.  

```css+lasso
let testEnv = await initializeTestEnvironment({
  projectId: "demo-project-1234",
  firestore: {
    rules: fs.readFileSync("firestore.rules", "utf8"),
  },
});
```

<br />

| Note: The emulators persist data between test invocations on a single emulator run. This might impact your results. To clear data between each test run, call the applicable clear emulator data method, e.g.`clearFirestoreData`, between tests.

<br />

**`RulesTestEnvironment.authenticatedContext({ user_id: string, tokenOptions?: TokenOptions }) => RulesTestContext`**

This method creates a`RulesTestContext`, which behaves like an authenticatedAuthenticationuser. Requests created via the returned context will have a mockAuthenticationtoken attached. Optionally, pass an object defining custom claims or overrides forAuthenticationtoken payloads.

Use the returned test context object in your tests to access any emulator instances configured, including those configured with`initializeTestEnvironment`.  

```python
// Assuming a Firestore app and the Firestore emulator for this example
import { setDoc } from "firebase/firestore";

const alice = testEnv.authenticatedContext("alice", { ... });
// Use the Firestore instance associated with this context
await assertSucceeds(setDoc(alice.firestore().doc('/users/alice'), { ... });
```

**`RulesTestEnvironment.unauthenticatedContext() => RulesTestContext`**

This method creates a`RulesTestContext`, which behaves like a client that is not logged in viaAuthentication. Requests created via the returned context will not have Firebase Auth tokens attached.

Use the returned test context object in your tests to access any emulator instances configured, including those configured with`initializeTestEnvironment`.  

```python
// Assuming a Cloud Storage app and the Storage emulator for this example
import { getStorage, ref, deleteObject } from "firebase/storage";

const alice = testEnv.unauthenticatedContext();

// Use the Cloud Storage instance associated with this context
const desertRef = ref(alice.storage(), 'images/desert.jpg');
await assertSucceeds(deleteObject(desertRef));
```

**`RulesTestEnvironment.withSecurityRulesDisabled()`**

Run a test setup function with a context that behaves as if Security Rules were disabled.

This method takes a callback function, which takes the Security-Rules-bypassing context and returns a promise. The context will be destroyed once the promise resolves / rejects.

**`RulesTestEnvironment.cleanup()`**

This method destroys all`RulesTestContexts`created in the test environment and cleans up the underlying resources, allowing a clean exit.

This method does not change the state of emulators in any way. To reset data between tests, use the application emulator-specific clear data method.

**`assertSucceeds(pr: Promise<any>)) => Promise<any>`**

This is a test case utility function.

The function asserts that the supplied Promise wrapping an emulator operation will be resolved with no Security Rules violations.  

```text
await assertSucceeds(setDoc(alice.firestore(), '/users/alice'), { ... });
```

**`assertFails(pr: Promise<any>)) => Promise<any>`**

This is a test case utility function.

The function asserts that the supplied Promise wrapping an emulator operation will be rejected with a Security Rules violation.  

```text
await assertFails(setDoc(alice.firestore(), '/users/bob'), { ... });
```

### Emulator-specific methods

Also see[common test methods and utility functions using the modular API](https://firebase.google.com/docs/rules/unit-tests#rut-v2-common-methods).

<br />

<br />

<br />

### Cloud Firestore

<br />

### Cloud Firestore

**`RulesTestEnvironment.clearFirestore() => Promise<void>`**

This method clears data in the Firestore database that belongs to the`projectId`configured for the Firestore emulator.

**`RulesTestContext.firestore(settings?: Firestore.FirestoreSettings) => Firestore;`**

This method gets a Firestore instance for this test context. The returned Firebase JS Client SDK instance can be used with the client SDK APIs (v9 modular or v9 compat).

<br />

### Realtime Database

<br />

### Realtime Database

**`RulesTestEnvironment.clearDatabase() => Promise<void>`**

This method clears data in theRealtime Databasethat belongs to the`projectId`configured for theRealtime Databaseemulator.

**`RulesTestContext.database(databaseURL?: Firestore.FirestoreSettings) => Firestore;`**

Get aRealtime Databaseinstance for this test context. The returned Firebase JS Client SDK instance can be used with the client SDK APIs (modular or namespaced, version 9 or greater). The method accepts a URL of the Realtime Database instance. If specified, returns an instance for an emulated version of the namespace with parameters extracted from URL.

<br />

### Cloud Storage

<br />

### Cloud Storage

**`RulesTestEnvironment.clearStorage() => Promise<void>`**

This method clears objects and metadata in storage buckets belonging to the`projectId`configured for theCloud Storageemulator.

**`RulesTestContext.storage(bucketUrl?: string) => Firebase Storage;`**

This method returns a Storage instance configured to connect to the emulator. The method accepts a`gs://`url to the Firebase Storage Bucket for testing. If specified, returns a Storage instance for an emulated version of the bucket name.

<br />

<br />

## Run local unit tests with the v8 JavaScript SDK

Select a product to see the methods used by the Firebase Test SDK to interface with the emulator.

<br />

<br />

<br />

### Cloud Firestore

<br />

**`initializeTestApp({ projectId: string, auth: Object }) => FirebaseApp`**

This method returns an initialized Firebase app corresponding to the project ID and auth variable specified in the options. Use this to create an app authenticated as a specific user to use in tests.  

```transact-sql
firebase.initializeTestApp({
  projectId: "my-test-project",
  auth: { uid: "alice", email: "alice@example.com" }
});
```

<br />

| Note: TheCloud Firestoreemulator persists data between test invocations on a single emulator run. This might impact your results. To clear data between each test run, call the`clearFirestoreData`method between tests.

<br />

**`initializeAdminApp({ projectId: string }) => FirebaseApp`**

This method returns an initialized admin Firebase app. This app bypasses security rules when performing reads and writes. Use this to create an app authenticated as an admin to set state for tests.  

```css+lasso
firebase.initializeAdminApp({ projectId: "my-test-project" });
    
```

**`apps() => [FirebaseApp]`**This method returns all the currently initialized test and admin apps. Use this to clean up apps between or after tests.  

```text
Promise.all(firebase.apps().map(app => app.delete()))
```

<br />

| Note: If you have any initialized apps with active listeners, JavaScript doesn't exit. Make sure to remove active listeners.

<br />

**`loadFirestoreRules({ projectId: string, rules: Object }) => Promise`**

This method sends rules to a locally running database. It takes an object that specifies the rules as a string. Use this method to set your database's rules.

<br />

```gdscript
firebase.loadFirestoreRules({
  projectId: "my-test-project",
  rules: fs.readFileSync("/path/to/firestore.rules", "utf8")
});
    
```

<br />

**`assertFails(pr: Promise) => Promise`**

This method returns a promise that is rejected if the input succeeds or that succeeds if the input is rejected. Use this to assert if a database read or write fails.

<br />

```text
firebase.assertFails(app.firestore().collection("private").doc("super-secret-document").get());
    
```

<br />

**`assertSucceeds(pr: Promise) => Promise`**

This method returns a promise that succeeds if the input succeeds and is rejected if the input is rejected. Use this to assert if a database read or write succeeds.

<br />

```text
firebase.assertSucceeds(app.firestore().collection("public").doc("test-document").get());
    
```

<br />

**`clearFirestoreData({ projectId: string }) => Promise`**

This method clears all data associated with a particular project in the locally running Firestore instance. Use this method to clean-up after tests.

<br />

```
firebase.clearFirestoreData({
  projectId: "my-test-project"
});
   
```

<br />

<br />

### Realtime Database

<br />

### Realtime Database

**`initializeTestApp({ databaseName: string, auth: Object }) => FirebaseApp`**

Use this to create an app authenticated as a specific user to use in tests.

Returns an initialized firebase app corresponding to the database name and auth variable override specified in options.  

    firebase.initializeTestApp({
      databaseName: "my-database",
      auth: { uid: "alice" }
    });

**`initializeAdminApp({ databaseName: string }) => FirebaseApp`**

Use this to create an app authenticated as an admin to set up state for tests.

Returns an initialized admin firebase app corresponding to the database name specified in options. This app bypasses security rules when reading and writing to the database.  

    firebase.initializeAdminApp({ databaseName: "my-database" });

**`loadDatabaseRules({ databaseName: string, rules: Object }) => Promise`**

Use this to set your database's rules.

Sends rules to a locally running database. Takes an options object that specifies your "databaseName" and your "rules" as strings.  

    firebase
          .loadDatabaseRules({
            databaseName: "my-database",
            rules: "{'rules': {'.read': false, '.write': false}}"
          });

**`apps() => [FirebaseApp]`**

Returns all the currently initialized test and admin apps.

Use this to clean up apps between or after tests (note that initialized apps with active listeners prevent JavaScript from exiting):  

     Promise.all(firebase.apps().map(app => app.delete()))

**`assertFails(pr: Promise) => Promise`**

Returns a promise that is rejected if the input succeeds and succeeds if the input is rejected.

Use this to assert that a database read or write fails:  

    firebase.assertFails(app.database().ref("secret").once("value"));

**`assertSucceeds(pr: Promise) => Promise`**

Returns a promise that succeeds if the input succeeds and is rejected if the input is rejected.

Use this to assert that a database read or write succeeds:  

    firebase.assertSucceeds(app.database().ref("public").once("value"));

<br />

### Cloud Storage

<br />

### Cloud Storage

**`initializeTestApp({ storageBucket: string, auth: Object }) => FirebaseApp`**

Use this to create an app authenticated as a specific user to use in tests.

Returns an initialized firebase app corresponding to the storage bucket name and auth variable override specified in options.  

    firebase.initializeTestApp({
      storageBucket: "my-bucket",
      auth: { uid: "alice" }
    });

**`initializeAdminApp({ storageBucket: string }) => FirebaseApp`**

Use this to create an app authenticated as an admin to set up state for tests.

Returns an initialized admin firebase app corresponding to the storage bucket name specified in options. This app bypasses security rules when reading and writing to the bucket.  

    firebase.initializeAdminApp({ storageBucket: "my-bucket" });

**`loadStorageRules({ storageBucket: string, rules: Object }) => Promise`**

Use this to set your storage bucket's rules.

Sends rules to a locally managed storage buckets. Takes an options object that specifies your "storageBucket" and your "rules" as strings.  

    firebase
          .loadStorageRules({
            storageBucket: "my-bucket",
            rules: fs.readFileSync("/path/to/storage.rules", "utf8")
          });

**`apps() => [FirebaseApp]`**

Returns all the currently initialized test and admin apps.

Use this to clean up apps between or after tests (note that initialized apps with active listeners prevent JavaScript from exiting):  

     Promise.all(firebase.apps().map(app => app.delete()))

**`assertFails(pr: Promise) => Promise`**

Returns a promise that is rejected if the input succeeds and succeeds if the input is rejected.

Use this to assert that a storage bucket read or write fails:  

    firebase.assertFails(app.storage().ref("letters/private.doc").getMetadata());

**`assertSucceeds(pr: Promise) => Promise`**

Returns a promise that succeeds if the input succeeds and is rejected if the input is rejected.

Use this to assert that a storage bucket read or write succeeds:  

    firebase.assertFails(app.storage().ref("images/cat.png").getMetadata());

<br />

<br />

### RUT library API for JS SDK v8

Select a product to see the methods used by the Firebase Test SDK to interface with the emulator.

<br />

<br />

<br />

### Cloud Firestore

<br />

### Cloud Firestore

**`initializeTestApp({ projectId: string, auth: Object }) => FirebaseApp`**

This method returns an initialized Firebase app corresponding to the project ID and auth variable specified in the options. Use this to create an app authenticated as a specific user to use in tests.  

```transact-sql
firebase.initializeTestApp({
  projectId: "my-test-project",
  auth: { uid: "alice", email: "alice@example.com" }
});
```

<br />

| Note: TheCloud Firestoreemulator persists data between test invocations on a single emulator run. This might impact your results. To clear data between each test run, call the`clearFirestoreData`method between tests.

<br />

**`initializeAdminApp({ projectId: string }) => FirebaseApp`**

This method returns an initialized admin Firebase app. This app bypasses security rules when performing reads and writes. Use this to create an app authenticated as an admin to set state for tests.  

```css+lasso
firebase.initializeAdminApp({ projectId: "my-test-project" });
    
```

**`apps() => [FirebaseApp]`**This method returns all the currently initialized test and admin apps. Use this to clean up apps between or after tests.  

```text
Promise.all(firebase.apps().map(app => app.delete()))
```

<br />

| Note: If you have any initialized apps with active listeners, JavaScript doesn't exit. Make sure to remove active listeners.

<br />

**`loadFirestoreRules({ projectId: string, rules: Object }) => Promise`**

This method sends rules to a locally running database. It takes an object that specifies the rules as a string. Use this method to set your database's rules.

<br />

```gdscript
firebase.loadFirestoreRules({
  projectId: "my-test-project",
  rules: fs.readFileSync("/path/to/firestore.rules", "utf8")
});
    
```

<br />

**`assertFails(pr: Promise) => Promise`**

This method returns a promise that is rejected if the input succeeds or that succeeds if the input is rejected. Use this to assert if a database read or write fails.

<br />

```text
firebase.assertFails(app.firestore().collection("private").doc("super-secret-document").get());
    
```

<br />

**`assertSucceeds(pr: Promise) => Promise`**

This method returns a promise that succeeds if the input succeeds and is rejected if the input is rejected. Use this to assert if a database read or write succeeds.

<br />

```text
firebase.assertSucceeds(app.firestore().collection("public").doc("test-document").get());
    
```

<br />

**`clearFirestoreData({ projectId: string }) => Promise`**

This method clears all data associated with a particular project in the locally running Firestore instance. Use this method to clean-up after tests.

<br />

```
firebase.clearFirestoreData({
  projectId: "my-test-project"
});
   
```

<br />

<br />

### Realtime Database

<br />

### Realtime Database

**`initializeTestApp({ databaseName: string, auth: Object }) => FirebaseApp`**

Use this to create an app authenticated as a specific user to use in tests.

Returns an initialized firebase app corresponding to the database name and auth variable override specified in options.  

    firebase.initializeTestApp({
      databaseName: "my-database",
      auth: { uid: "alice" }
    });

**`initializeAdminApp({ databaseName: string }) => FirebaseApp`**

Use this to create an app authenticated as an admin to set up state for tests.

Returns an initialized admin firebase app corresponding to the database name specified in options. This app bypasses security rules when reading and writing to the database.  

    firebase.initializeAdminApp({ databaseName: "my-database" });

**`loadDatabaseRules({ databaseName: string, rules: Object }) => Promise`**

Use this to set your database's rules.

Sends rules to a locally running database. Takes an options object that specifies your "databaseName" and your "rules" as strings.  

    firebase
          .loadDatabaseRules({
            databaseName: "my-database",
            rules: "{'rules': {'.read': false, '.write': false}}"
          });

**`apps() => [FirebaseApp]`**

Returns all the currently initialized test and admin apps.

Use this to clean up apps between or after tests (note that initialized apps with active listeners prevent JavaScript from exiting):  

     Promise.all(firebase.apps().map(app => app.delete()))

**`assertFails(pr: Promise) => Promise`**

Returns a promise that is rejected if the input succeeds and succeeds if the input is rejected.

Use this to assert that a database read or write fails:  

    firebase.assertFails(app.database().ref("secret").once("value"));

**`assertSucceeds(pr: Promise) => Promise`**

Returns a promise that succeeds if the input succeeds and is rejected if the input is rejected.

Use this to assert that a database read or write succeeds:  

    firebase.assertSucceeds(app.database().ref("public").once("value"));

<br />

### Cloud Storage

<br />

### Cloud Storage

**`initializeTestApp({ storageBucket: string, auth: Object }) => FirebaseApp`**

Use this to create an app authenticated as a specific user to use in tests.

Returns an initialized firebase app corresponding to the storage bucket name and auth variable override specified in options.  

    firebase.initializeTestApp({
      storageBucket: "my-bucket",
      auth: { uid: "alice" }
    });

**`initializeAdminApp({ storageBucket: string }) => FirebaseApp`**

Use this to create an app authenticated as an admin to set up state for tests.

Returns an initialized admin firebase app corresponding to the storage bucket name specified in options. This app bypasses security rules when reading and writing to the bucket.  

    firebase.initializeAdminApp({ storageBucket: "my-bucket" });

**`loadStorageRules({ storageBucket: string, rules: Object }) => Promise`**

Use this to set your storage bucket's rules.

Sends rules to a locally managed storage buckets. Takes an options object that specifies your "storageBucket" and your "rules" as strings.  

    firebase
          .loadStorageRules({
            storageBucket: "my-bucket",
            rules: fs.readFileSync("/path/to/storage.rules", "utf8")
          });

**`apps() => [FirebaseApp]`**

Returns all the currently initialized test and admin apps.

Use this to clean up apps between or after tests (note that initialized apps with active listeners prevent JavaScript from exiting):  

     Promise.all(firebase.apps().map(app => app.delete()))

**`assertFails(pr: Promise) => Promise`**

Returns a promise that is rejected if the input succeeds and succeeds if the input is rejected.

Use this to assert that a storage bucket read or write fails:  

    firebase.assertFails(app.storage().ref("letters/private.doc").getMetadata());

**`assertSucceeds(pr: Promise) => Promise`**

Returns a promise that succeeds if the input succeeds and is rejected if the input is rejected.

Use this to assert that a storage bucket read or write succeeds:  

    firebase.assertFails(app.storage().ref("images/cat.png").getMetadata());

<br />

<br />