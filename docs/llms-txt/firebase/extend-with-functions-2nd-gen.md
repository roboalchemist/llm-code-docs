# Source: https://firebase.google.com/docs/firestore/extend-with-functions-2nd-gen.md.txt

<br />

WithCloud Functions, you can deploy code to handle events triggered by changes in yourCloud Firestoredatabase. This allows you to easily add server-side functionality into your app without running your own servers.

## Cloud Functions(2nd gen)

Powered by[Cloud Run](https://cloud.google.com/run)and[Eventarc](https://cloud.google.com/eventarc/docs),Cloud Functions for Firebase(2nd gen) gives you more powerful infrastructure, advanced control over performance and scalability, and more control of the functions runtime. For more information about 2nd gen, see[Cloud Functions for Firebase (2nd gen)](https://firebase.google.com/docs/functions/beta). To see more about the 1st gen instead, see[ExtendCloud Firestorewith Cloud Functions](https://firebase.google.com/docs/firestore/extend-with-functions).

## Cloud Firestorefunction triggers

TheCloud Functions for FirebaseSDK exports the followingCloud Firestoreevent triggers to let you create handlers tied to specificCloud Firestoreevents:  

### Node.js

|             Event Type             |                                         Trigger                                         |
|------------------------------------|-----------------------------------------------------------------------------------------|
| `onDocumentCreated`                | Triggered when a document is written to for the first time.                             |
| `onDocumentUpdated`                | Triggered when a document already exists and has any value changed.                     |
| `onDocumentDeleted`                | Triggered when a document is deleted.                                                   |
| `onDocumentWritten`                | Triggered when`onDocumentCreated`,`onDocumentUpdated`or`onDocumentDeleted`is triggered. |
| `onDocumentCreatedWithAuthContext` | `onDocumentCreated`with additional authentication information                           |
| `onDocumentWrittenWithAuthContext` | `onDocumentWritten`with additional authentication information                           |
| `onDocumentDeletedWithAuthContext` | `onDocumentDeleted`with additional authentication information                           |
| `onDocumentUpdatedWithAuthContext` | `onDocumentUpdated`with additional authentication information                           |

### Python

|               Event Type                |                                            Trigger                                            |
|-----------------------------------------|-----------------------------------------------------------------------------------------------|
| `on_document_created`                   | Triggered when a document is written to for the first time.                                   |
| `on_document_updated`                   | Triggered when a document already exists and has any value changed.                           |
| `on_document_deleted`                   | Triggered when a document is deleted.                                                         |
| `on_document_written`                   | Triggered when`on_document_created`,`on_document_updated`or`on_document_deleted`is triggered. |
| `on_document_created_with_auth_context` | `on_document_created`with additional authentication information                               |
| `on_document_updated_with_auth_context` | `on_document_updated`with additional authentication information                               |
| `on_document_deleted_with_auth_context` | `on_document_deleted`with additional authentication information                               |
| `on_document_written_with_auth_context` | `on_document_written`with additional authentication information                               |

Cloud Firestoreevents trigger only on document changes. An update to aCloud Firestoredocument where data is unchanged (a no-op write) does not generate an update or write event. It is not possible to add events to specific fields.

If you don't have a project enabled forCloud Functions for Firebaseyet, then read[Get started withCloud Functions for Firebase(2nd gen)](https://firebase.google.com/docs/functions/beta/get-started)to configure and set up yourCloud Functions for Firebaseproject.

## WritingCloud Firestore-triggered functions

### Define a function trigger

To define aCloud Firestoretrigger, specify a document path and an event type:  

### Node.js

    const {
      onDocumentWritten,
      onDocumentCreated,
      onDocumentUpdated,
      onDocumentDeleted,
      Change,
      FirestoreEvent
    } = require('firebase-functions/v2/firestore');

    exports.myfunction = onDocumentWritten("my-collection/{docId}", (event) => {
       /* ... */ 
    });

### Python

    from firebase_functions.firestore_fn import (
      on_document_created,
      on_document_deleted,
      on_document_updated,
      on_document_written,
      Event,
      Change,
      DocumentSnapshot,
    )

    @on_document_created(document="users/{userId}")
    def myfunction(event: Event[DocumentSnapshot]) -> None:

Document paths can reference either a[specific document](https://firebase.google.com/docs/firestore/extend-with-functions-2nd-gen#specific-documents)or a[wildcard pattern](https://firebase.google.com/docs/firestore/extend-with-functions-2nd-gen#wildcards-parameters).

### Specify a single document

If you want to trigger an event for*any*change to a specific document then you can use the following function.  

### Node.js

    const {
      onDocumentWritten,
      Change,
      FirestoreEvent
    } = require('firebase-functions/v2/firestore');

    exports.myfunction = onDocumentWritten("users/marie", (event) => {
      // Your code here
    });

### Python

    from firebase_functions.firestore_fn import (
      on_document_written,
      Event,
      Change,
      DocumentSnapshot,
    )

    @on_document_written(document="users/marie")
    def myfunction(event: Event[Change[DocumentSnapshot]]) -> None:

### Specify a group of documents using wildcards

If you want to attach a trigger to a group of documents, such as any document in a certain collection, then use a`{wildcard}`in place of the document ID:  

### Node.js

    const {
      onDocumentWritten,
      Change,
      FirestoreEvent
    } = require('firebase-functions/v2/firestore');

    exports.myfunction = onDocumentWritten("users/{userId}", (event) => {
      // If we set `/users/marie` to {name: "Marie"} then
      // event.params.userId == "marie"
      // ... and ...
      // event.data.after.data() == {name: "Marie"}
    });

### Python

    from firebase_functions.firestore_fn import (
      on_document_written,
      Event,
      Change,
      DocumentSnapshot,
    )

    @on_document_written(document="users/{userId}")
    def myfunction(event: Event[Change[DocumentSnapshot]]) -> None:
      # If we set `/users/marie` to {name: "Marie"} then
      event.params["userId"] == "marie"  # True
      # ... and ...
      event.data.after.to_dict() == {"name": "Marie"}  # True

In this example, when any field on any document in`users`is changed, it matches a wildcard called`userId`.

If a document in`users`has subcollections and a field in one of those subcollections' documents is changed, the`userId`wildcard is*not*triggered.

Wildcard matches are extracted from the document path and stored into`event.params`. You may define as many wildcards as you like to substitute explicit collection or document IDs, for example:  

### Node.js

    const {
      onDocumentWritten,
      Change,
      FirestoreEvent
    } = require('firebase-functions/v2/firestore');

    exports.myfunction = onDocumentWritten("users/{userId}/{messageCollectionId}/{messageId}", (event) => {
        // If we set `/users/marie/incoming_messages/134` to {body: "Hello"} then
        // event.params.userId == "marie";
        // event.params.messageCollectionId == "incoming_messages";
        // event.params.messageId == "134";
        // ... and ...
        // event.data.after.data() == {body: "Hello"}
    });

### Python

    from firebase_functions.firestore_fn import (
      on_document_written,
      Event,
      Change,
      DocumentSnapshot,
    )

    @on_document_written(document="users/{userId}/{messageCollectionId}/{messageId}")
    def myfunction(event: Event[Change[DocumentSnapshot]]) -> None:
      # If we set `/users/marie/incoming_messages/134` to {body: "Hello"} then
      event.params["userId"] == "marie"  # True
      event.params["messageCollectionId"] == "incoming_messages"  # True
      event.params["messageId"] == "134"  # True
      # ... and ...
      event.data.after.to_dict() == {"body": "Hello"}

Your trigger must*always* point to a document, even if you're using a wildcard. For example,`users/{userId}/{messageCollectionId}`is not valid because`{messageCollectionId}`is a collection. However,`users/{userId}/{messageCollectionId}/{messageId}`*is* valid because`{messageId}`will always point to a document.

## Event Triggers

### Trigger a function when a new document is created

You can trigger a function to fire any time a new document is created in a collection. This example function triggers every time a new user profile is added:  

### Node.js

    const {
      onDocumentCreated,
      Change,
      FirestoreEvent
    } = require('firebase-functions/v2/firestore');

    exports.createuser = onDocumentCreated("users/{userId}", (event) => {
        // Get an object representing the document
        // e.g. {'name': 'Marie', 'age': 66}
        const snapshot = event.data;
        if (!snapshot) {
            console.log("No data associated with the event");
            return;
        }
        const data = snapshot.data();

        // access a particular field as you would any JS property
        const name = data.name;

        // perform more operations ...
    });

For additional authentication information, use`onDocumentCreatedWithAuthContext`.

### Python

    from firebase_functions.firestore_fn import (
      on_document_created,
      Event,
      DocumentSnapshot,
    )

    @on_document_created(document="users/{userId}")
    def myfunction(event: Event[DocumentSnapshot]) -> None:
      # Get a dictionary representing the document
      # e.g. {'name': 'Marie', 'age': 66}
      new_value = event.data.to_dict()

      # Access a particular field as you would any dictionary
      name = new_value["name"]

      # Perform more operations ...

### Trigger a function when a document is updated

You can also trigger a function to fire when a document is updated. This example function fires if a user changes their profile:  

### Node.js

    const {
      onDocumentUpdated,
      Change,
      FirestoreEvent
    } = require('firebase-functions/v2/firestore');

    exports.updateuser = onDocumentUpdated("users/{userId}", (event) => {
        // Get an object representing the document
        // e.g. {'name': 'Marie', 'age': 66}
        const newValue = event.data.after.data();

        // access a particular field as you would any JS property
        const name = newValue.name;

        // perform more operations ...
    });

For additional authentication information, use`onDocumentUpdatedWithAuthContext`.

### Python

    from firebase_functions.firestore_fn import (
      on_document_updated,
      Event,
      Change,
      DocumentSnapshot,
    )

    @on_document_updated(document="users/{userId}")
    def myfunction(event: Event[Change[DocumentSnapshot]]) -> None:
      # Get a dictionary representing the document
      # e.g. {'name': 'Marie', 'age': 66}
      new_value = event.data.after.to_dict()

      # Access a particular field as you would any dictionary
      name = new_value["name"]

      # Perform more operations ...

### Trigger a function when a document is deleted

You can also trigger a function when a document is deleted. This example function fires when a user deletes their user profile:  

### Node.js

    const {
      onDocumentDeleted,
      Change,
      FirestoreEvent
    } = require('firebase-functions/v2/firestore');

    exports.deleteuser = onDocumentDeleted("users/{userId}", (event) => {
        // Get an object representing the document
        // e.g. {'name': 'Marie', 'age': 66}
        const snap =  event.data;
        const data =  snap.data();

        // perform more operations ...
    });

For additional authentication information, use`onDocumentDeletedWithAuthContext`.

### Python

    from firebase_functions.firestore_fn import (
      on_document_deleted,
      Event,
      DocumentSnapshot,
    )

    @on_document_deleted(document="users/{userId}")
    def myfunction(event: Event[DocumentSnapshot|None]) -> None:
      # Perform more operations ...

### Trigger a function for all changes to a document

If you don't care about the type of event being fired, you can listen for all changes in aCloud Firestoredocument using the "document written" event trigger. This example function fires if a user is created, updated, or deleted:  

### Node.js

    const {
      onDocumentWritten,
      Change,
      FirestoreEvent
    } = require('firebase-functions/v2/firestore');

    exports.modifyuser = onDocumentWritten("users/{userId}", (event) => {
        // Get an object with the current document values.
        // If the document does not exist, it was deleted
        const document =  event.data.after.data();

        // Get an object with the previous document values
        const previousValues =  event.data.before.data();

        // perform more operations ...
    });

For additional authentication information, use`onDocumentWrittenWithAuthContext`.

### Python

    from firebase_functions.firestore_fn import (
      on_document_written,
      Event,
      Change,
      DocumentSnapshot,
    )

    @on_document_written(document="users/{userId}")
    def myfunction(event: Event[Change[DocumentSnapshot | None]]) -> None:
      # Get an object with the current document values.
      # If the document does not exist, it was deleted.
      document = (event.data.after.to_dict()
                  if event.data.after is not None else None)

      # Get an object with the previous document values.
      # If the document does not exist, it was newly created.
      previous_values = (event.data.before.to_dict()
                         if event.data.before is not None else None)

      # Perform more operations ...

## Reading and Writing Data

When a function is triggered, it provides a snapshot of the data related to the event. You can use this snapshot to read from or write to the document that triggered the event, or use the Firebase Admin SDK to access other parts of your database.

### Event Data

#### Reading Data

When a function is triggered, you might want to get data from a document that was updated, or get the data prior to update. You can get the prior data by using`event.data.before`, which contains the document snapshot before the update. Similarly,`event.data.after`contains the document snapshot state after the update.  

### Node.js

    exports.updateuser2 = onDocumentUpdated("users/{userId}", (event) => {
        // Get an object with the current document values.
        // If the document does not exist, it was deleted
        const newValues =  event.data.after.data();

        // Get an object with the previous document values
        const previousValues =  event.data.before.data();
    });

### Python

    @on_document_updated(document="users/{userId}")
    def myfunction(event: Event[Change[DocumentSnapshot]]) -> None:
      # Get an object with the current document values.
      new_value = event.data.after.to_dict()

      # Get an object with the previous document values.
      prev_value = event.data.before.to_dict()

You can access properties as you would in any other object. Alternatively, you can use the`get`function to access specific fields:  

### Node.js

    // Fetch data using standard accessors
    const age = event.data.after.data().age;
    const name = event.data.after.data()['name'];

    // Fetch data using built in accessor
    const experience = event.data.after.data.get('experience');

### Python

    # Get the value of a single document field.
    age = event.data.after.get("age")

    # Convert the document to a dictionary.
    age = event.data.after.to_dict()["age"]

#### Writing Data

Each function invocation is associated with a specific document in yourCloud Firestoredatabase. You can access that document in the snapshot returned to your function.

The document reference includes methods like`update()`,`set()`, and`remove()`so you can modify the document that triggered the function.  

### Node.js

    const {onDocumentUpdated} = require('firebase-functions/v2/firestore');

    exports.countnamechanges = onDocumentUpdated('users/{userId}', (event) => {
      // Retrieve the current and previous value
      const data = event.data.after.data();
      const previousData = event.data.before.data();

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
      return event.data.after.ref.set({
        name_change_count: count + 1
      }, {merge: true});

    });

### Python

    @on_document_updated(document="users/{userId}")
    def myfunction(event: Event[Change[DocumentSnapshot]]) -> None:
      # Get the current and previous document values.
      new_value = event.data.after
      prev_value = event.data.before

      # We'll only update if the name has changed.
      # This is crucial to prevent infinite loops.
      if new_value.get("name") == prev_value.get("name"):
          return

      # Retrieve the current count of name changes
      count = new_value.to_dict().get("name_change_count", 0)

      # Update the count
      new_value.reference.update({"name_change_count": count + 1})

| **Warning:** Any time you write to the same document that triggered a function, you are at risk of creating an infinite loop. Use caution and ensure that you safely exit the function when no change is needed.

### Access user authentication information

If you use one of the of the following event types, you can access user authentication information about the principal that triggered the event. This information is in addition to the information returned in the base event.  

### Node.js

- `onDocumentCreatedWithAuthContext`
- `onDocumentWrittenWithAuthContext`
- `onDocumentDeletedWithAuthContext`
- `onDocumentUpdatedWithAuthContext`

### Python

- `on_document_created_with_auth_context`
- `on_document_updated_with_auth_context`
- `on_document_deleted_with_auth_context`
- `on_document_written_with_auth_context`

For information about the data available in the authentication context, see[Auth Context](https://github.com/cloudevents/spec/blob/main/cloudevents/extensions/authcontext.md). The following example demonstrates how to retrieve authentication information:  

### Node.js

    const {onDocumentWrittenWithAuthContext} = require('firebase-functions/v2/firestore');

    exports.syncUser = onDocumentWrittenWithAuthContext("users/{userId}", (event) => {
        const snapshot = event.data.after;
        if (!snapshot) {
            console.log("No data associated with the event");
            return;
        }
        const data = snapshot.data();

        // retrieve auth context from event
        const { authType, authId } = event;

        let verified = false;
        if (authType === "system") {
          // system-generated users are automatically verified
          verified = true;
        } else if (authType === "unknown" || authType === "unauthenticated") {
          // admin users from a specific domain are verified
          if (authId.endsWith("@example.com")) {
            verified = true;
          }
        }

        return data.after.ref.set({
            created_by: authId,
            verified,
        }, {merge: true}); 
    }); 

### Python

    @on_document_updated_with_auth_context(document="users/{userId}")
    def myfunction(event: Event[Change[DocumentSnapshot]]) -> None:

      # Get the current and previous document values.
      new_value = event.data.after
      prev_value = event.data.before

      # Get the auth context from the event
      user_auth_type = event.auth_type
      user_auth_id = event.auth_id

### Data outside the trigger event

Cloud Functionsexecute in a trusted environment. They are authorized as a service account on your project, and you can perform reads and writes using the[Firebase Admin SDK](https://firebase.google.com/docs/reference/admin):  

### Node.js

    const { initializeApp } = require('firebase-admin/app');
    const { getFirestore, Timestamp, FieldValue } = require('firebase-admin/firestore');

    initializeApp();
    const db = getFirestore();

    exports.writetofirestore = onDocumentWritten("some/doc", (event) => {
        db.doc('some/otherdoc').set({ ... });
      });

      exports.writetofirestore = onDocumentWritten('users/{userId}', (event) => {
        db.doc('some/otherdoc').set({
          // Update otherdoc
        });
      });

### Python

    from firebase_admin import firestore, initialize_app
    import google.cloud.firestore

    initialize_app()

    @on_document_written(document="some/doc")
    def myfunction(event: Event[Change[DocumentSnapshot | None]]) -> None:
      firestore_client: google.cloud.firestore.Client = firestore.client()
      firestore_client.document("another/doc").set({
          # ...
      })

| **Note:** Reads and writes performed inCloud Functionsare not controlled by your security rules, they can access any part of your database.

## Limitations

Note the following limitations forCloud Firestoretriggers forCloud Functions:

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