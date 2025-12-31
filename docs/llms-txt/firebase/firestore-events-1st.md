# Source: https://firebase.google.com/docs/functions/1st-gen/firestore-events-1st.md.txt

<br />

| **Note:** The 1st-gen functionality described in this page is also supported inCloud Functions(2nd gen) with improved features and performance. For more information about 2nd gen, see the[version comparison](https://firebase.google.com/docs/functions/version-comparison). To go directly to the 2nd gen guide for this feature, see[Cloud Firestore triggers](https://firebase.google.com/docs/functions/firestore-events).

WithCloud Functions, you can handle events in Cloud Firestore with no need to update client code. You can make Cloud Firestore changes via the document snapshot interface or via the[Admin SDK](https://firebase.google.com/docs/admin/setup).

In a typical lifecycle, a Cloud Firestore function does the following:

1. Waits for changes to a particular document.
2. Triggers when an event occurs and performs its tasks.
3. Receives a data object that contains a snapshot of the data stored in the specified document. For write or update events, the data object contains two snapshots that represent the data state before and after the triggering event.

Distance between the location of the Firestore instance and the location of the function can create significant network latency. To optimize performance, consider specifying the[function location](https://firebase.google.com/docs/functions/locations)where applicable.

## Cloud Firestore function triggers

TheCloud Functions for FirebaseSDK exports a[`functions.firestore`](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore)object that allows you to create handlers tied to specific Cloud Firestore events.

|                                                                     Event Type                                                                      |                               Trigger                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| [`onCreate`](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.documentbuilder.md#firestoredocumentbuilderoncreate) | Triggered when a document is written to for the first time.         |
| [`onUpdate`](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.documentbuilder.md#firestoredocumentbuilderonupdate) | Triggered when a document already exists and has any value changed. |
| [`onDelete`](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.documentbuilder.md#firestoredocumentbuilderondelete) | Triggered when a document with data is deleted.                     |
| [`onWrite`](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.documentbuilder.md#firestoredocumentbuilderonwrite)   | Triggered when`onCreate`,`onUpdate`or`onDelete`is triggered.        |

| **Note:** Cloud Firestore events will trigger only on document changes. An update to a Cloud Firestore document, where data is unchanged (a no-op write), will not generate an update or write event. It is not possible to add events to specific fields.

If you don't have a project enabled forCloud Functions for Firebaseyet, then read[Get Started: Write and Deploy Your First Functions](https://firebase.google.com/docs/functions/get-started)to configure and set up yourCloud Functions for Firebaseproject.

## Writing Cloud Firestore-triggered functions

### Define a function trigger

To define a Cloud Firestore trigger, specify a document path and an event type:  

### Node.js

    const functions = require('firebase-functions');

    exports.myFunction = functions.firestore
      .document('my-collection/{docId}')
      .onWrite((change, context) => { /* ... */ });

Document paths can reference either a[specific document](https://firebase.google.com/docs/functions/1st-gen/firestore-events-1st#specific-documents)or a[wildcard pattern](https://firebase.google.com/docs/functions/1st-gen/firestore-events-1st#wildcards-parameters).
| **Important:** Document paths must**not**contain trailing slashes.

### Specify a single document

If you want to trigger an event for*any*change to a specific document then you can use the following function.  

### Node.js

```javascript
// Listen for any change on document `marie` in collection `users`
exports.myFunctionName = functions.firestore
    .document('users/marie').onWrite((change, context) => {
      // ... Your code here
    });https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/extend-with-functions/functions/index.js#L5-L9
```

### Specify a group of documents using wildcards

If you want to attach a trigger to a group of documents, such as any document in a certain collection, then use a`{wildcard}`in place of the document ID:  

### Node.js

```javascript
// Listen for changes in all documents in the 'users' collection
exports.useWildcard = functions.firestore
    .document('users/{userId}')
    .onWrite((change, context) => {
      // If we set `/users/marie` to {name: "Marie"} then
      // context.params.userId == "marie"
      // ... and ...
      // change.after.data() == {name: "Marie"}
    });https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/extend-with-functions/functions/index.js#L138-L146
```

In this example, when any field on any document in`users`is changed, it matches a wildcard called`userId`.

If a document in`users`has subcollections, and a field in one of those subcollections' documents is changed, the`userId`wildcard is*not*triggered.

Wildcard matches are extracted from the document path and stored into`context.params`. You may define as many wildcards as you like to substitute explicit collection or document IDs, for example:  

### Node.js

```javascript
// Listen for changes in all documents in the 'users' collection and all subcollections
exports.useMultipleWildcards = functions.firestore
    .document('users/{userId}/{messageCollectionId}/{messageId}')
    .onWrite((change, context) => {
      // If we set `/users/marie/incoming_messages/134` to {body: "Hello"} then
      // context.params.userId == "marie";
      // context.params.messageCollectionId == "incoming_messages";
      // context.params.messageId == "134";
      // ... and ...
      // change.after.data() == {body: "Hello"}
    });https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/extend-with-functions/functions/index.js#L152-L162
```
| **Note:** Your trigger must*always* point to a document, even if you're using a wildcard. For example,`users/{userId}/{messageCollectionId}`is not valid because`{messageCollectionId}`is a collection. However,`users/{userId}/{messageCollectionId}/{messageId}`*is* valid because`{messageId}`will always point to a document.

## Event Triggers

### Trigger a function when a new document is created

You can trigger a function to fire any time a new document is created in a collection by using an`onCreate()`handler with a[wildcard](https://firebase.google.com/docs/functions/1st-gen/firestore-events-1st#wildcards-parameters). This example function calls`createUser`every time a new user profile is added:  

### Node.js

```javascript
exports.createUser = functions.firestore
    .document('users/{userId}')
    .onCreate((snap, context) => {
      // Get an object representing the document
      // e.g. {'name': 'Marie', 'age': 66}
      const newValue = snap.data();

      // access a particular field as you would any JS property
      const name = newValue.name;

      // perform desired operations ...
    });https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/extend-with-functions/functions/index.js#L15-L26
```

### Trigger a function when a document is updated

You can also trigger a function to fire when a document is updated using the`onUpdate()`function with a[wildcard](https://firebase.google.com/docs/functions/1st-gen/firestore-events-1st#wildcards-parameters). This example function calls`updateUser`if a user changes their profile:  

### Node.js

```javascript
exports.updateUser = functions.firestore
    .document('users/{userId}')
    .onUpdate((change, context) => {
      // Get an object representing the document
      // e.g. {'name': 'Marie', 'age': 66}
      const newValue = change.after.data();

      // ...or the previous value before this update
      const previousValue = change.before.data();

      // access a particular field as you would any JS property
      const name = newValue.name;

      // perform desired operations ...
    });https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/extend-with-functions/functions/index.js#L32-L46
```

### Trigger a function when a document is deleted

You can also trigger a function when a document is deleted using the`onDelete()`function with a[wildcard](https://firebase.google.com/docs/functions/1st-gen/firestore-events-1st#wildcards-parameters). This example function calls`deleteUser`when a user deletes their user profile:  

### Node.js

```javascript
exports.deleteUser = functions.firestore
    .document('users/{userID}')
    .onDelete((snap, context) => {
      // Get an object representing the document prior to deletion
      // e.g. {'name': 'Marie', 'age': 66}
      const deletedValue = snap.data();

      // perform desired operations ...
    });https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/extend-with-functions/functions/index.js#L52-L60
```

### Trigger a function for all changes to a document

If you don't care about the type of event being fired, you can listen for all changes in a Cloud Firestore document using the`onWrite()`function with a[wildcard](https://firebase.google.com/docs/functions/1st-gen/firestore-events-1st#wildcards-parameters). This example function calls`modifyUser`if a user is created, updated, or deleted:  

### Node.js

```javascript
exports.modifyUser = functions.firestore
    .document('users/{userID}')
    .onWrite((change, context) => {
      // Get an object with the current document value.
      // If the document does not exist, it has been deleted.
      const document = change.after.exists ? change.after.data() : null;

      // Get an object with the previous document value (for update or delete)
      const oldDocument = change.before.data();

      // perform desired operations ...
    });https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/extend-with-functions/functions/index.js#L66-L77
```

## Reading and Writing Data

When a function is triggered, it provides a snapshot of the data related to the event. You can use this snapshot to read from or write to the document that triggered the event, or use the Firebase Admin SDK to access other parts of your database.

### Event Data

#### Reading Data

When a function is triggered, you might want to get data from a document that was updated, or get the data prior to update. You can get the prior data by using`change.before.data()`, which contains the document snapshot before the update. Similarly,`change.after.data()`contains the document snapshot state after the update.  

### Node.js

```javascript
exports.updateUser2 = functions.firestore
    .document('users/{userId}')
    .onUpdate((change, context) => {
      // Get an object representing the current document
      const newValue = change.after.data();

      // ...or the previous value before this update
      const previousValue = change.before.data();
    });https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/extend-with-functions/functions/index.js#L83-L91
```

You can access properties as you would in any other object. Alternatively, you can use the`get`function to access specific fields:  

### Node.js

```javascript
// Fetch data using standard accessors
const age = snap.data().age;
const name = snap.data()['name'];

// Fetch data using built in accessor
const experience = snap.get('experience');https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/extend-with-functions/functions/index.js#L97-L102
```

#### Writing Data

Each function invocation is associated with a specific document in your Cloud Firestore database. You can access that document as a`DocumentReference`in the`ref`property of the snapshot returned to your function.

This`DocumentReference`comes from the[Cloud Firestore Node.js SDK](https://firebase.google.com/docs/firestore/quickstart)and includes methods like`update()`,`set()`, and`remove()`so you can easily modify the document that triggered the function.  

### Node.js

```javascript
// Listen for updates to any `user` document.
exports.countNameChanges = functions.firestore
    .document('users/{userId}')
    .onUpdate((change, context) => {
      // Retrieve the current and previous value
      const data = change.after.data();
      const previousData = change.before.data();

      // We'll only update if the name has changed.
      // This is crucial to prevent infinite loops.
      if (data.name == previousData.name) {
        return null;
      }

      // Retrieve the current count of name changes
      let count = data.name_change_count;
      if (!count) {
        count = 0;
      }

      // Then return a promise of a set operation to update the count
      return change.after.ref.set({
        name_change_count: count + 1
      }, {merge: true});
    });https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/extend-with-functions/functions/index.js#L108-L132
```
| **Note:** Any time you write to the same document that triggered a function, you are at risk of creating an infinite loop. Use caution and ensure that you safely exit the function when no change is needed.

### Data outside the trigger event

Cloud Functionsexecute in a trusted environment, which means they are authorized as a service account on your project. You can perform reads and writes using the[Firebase Admin SDK](https://firebase.google.com/docs/reference/admin):  

### Node.js

    const admin = require('firebase-admin');
    admin.initializeApp();

    const db = admin.firestore();

    exports.writeToFirestore = functions.firestore
      .document('some/doc')
      .onWrite((change, context) => {
        db.doc('some/otherdoc').set({ ... });
      });

| **Note:** Reads and writes performed inCloud Functionsare not controlled by your security rules, they can access any part of your database.

## Limitations

Note the following limitations forCloud Firestoretriggers for Cloud Functions:

- Cloud Functions(1st gen) prerequisites an existing "(default)" database in Firestore native mode. It does not supportCloud Firestorenamed databases or Datastore mode. Please useCloud Functions(2nd gen) to configure events in such cases.
- Cross project setup withCloud FunctionsandCloud Firestoretrigger is a limitation. To setupCloud FirestoretriggerCloud Functionsmust be in the same project.
- Ordering is not guaranteed. Rapid changes can trigger function invocations in an unexpected order.
- Events are delivered at least once, but a single event may result in multiple function invocations. Avoid depending on exactly-once mechanics, and write[idempotent functions](https://cloud.google.com/blog/products/serverless/cloud-functions-pro-tips-building-idempotent-functions).
- [Cloud Firestorein Datastore mode](https://cloud.google.com/firestore/docs/firestore-or-datastore)requiresCloud Functions(2nd gen).Cloud Functions(1st gen) does not support Datastore mode.
- A trigger is associated with a single database. You cannot create a trigger that matches multiple databases.
- Deleting a database does not automatically delete any triggers for that database. The trigger stops delivering events but continues to exist until you[delete the trigger](https://cloud.google.com/eventarc/docs/managing-triggers#trigger-delete).
- If a matched event exceeds the[maximum request size](https://cloud.google.com/functions/quotas#resource_limits), the event might not be delivered toCloud Functions(1st gen).
  - Events not delivered because of request size are logged in[platform logs](https://cloud.google.com/logging/docs/api/platform-logs)and count towards the log usage for the project.
  - You can find these logs in the Logs Explorer with the message "Event cannot deliver to Cloud function due to size exceeding the limit for 1st gen..." of`error`severity. You can find the function name under the`functionName`field. If the`receiveTimestamp`field is still within an hour from now, you can infer the actual event content by reading the document in question with a snapshot before and after the timestamp.
  - To avoid such cadence, you can:
    - Migrate and upgrade toCloud Functions(2nd gen)
    - Downsize the document
    - Delete theCloud Functionsin question
  - You can turn off the logging itself using[exclusions](https://cloud.google.com/logging/docs/routing/overview#exclusions)but note that the offending events will still not be delivered.