# Source: https://firebase.google.com/docs/firestore/enterprise/extend-with-functions-2nd-gen-mongodb.md.txt

# Extend Firebase with Cloud Functions (2nd gen)

<br />

With Cloud Functions, you can deploy code to handle events triggered
by changes in your Firebase database. This lets you add server-side
functionality to your app without running your own servers.

## Cloud Functions (2nd gen)

Powered by [Cloud Run](https://cloud.google.com/run) and
[Eventarc](https://cloud.google.com/eventarc/docs),
Cloud Functions for Firebase (2nd gen) gives you more powerful
infrastructure, advanced control over performance and scalability, and more
control of the functions runtime. For more information about 2nd gen, see
[Cloud Functions for Firebase (2nd gen)](https://firebase.google.com/docs/functions/beta).

> [!NOTE]
> **Note:** Cloud Firestore Enterprise edition does not support Cloud Functions for Firebase (1st gen)

## Firebase function triggers

The Cloud Functions for Firebase SDK exports the following Firebase
event triggers to let you create handlers tied to specific Firebase
events:

### Node.js

| Event Type | Trigger |
|---|---|
| `onDocumentCreated` | Triggered when a document is written to for the first time. |
| `onDocumentUpdated` | Triggered when a document already exists and has any value changed. |
| `onDocumentDeleted` | Triggered when a document is deleted. |
| `onDocumentWritten` | Triggered when `onDocumentCreated`, `onDocumentUpdated` or `onDocumentDeleted` is triggered. |
| `onDocumentCreatedWithAuthContext` | `onDocumentCreated` with additional authentication information |
| `onDocumentWrittenWithAuthContext` | `onDocumentWritten` with additional authentication information |
| `onDocumentDeletedWithAuthContext` | `onDocumentDeleted` with additional authentication information |
| `onDocumentUpdatedWithAuthContext` | `onDocumentUpdated` with additional authentication information |

### Python

| Event Type | Trigger |
|---|---|
| `on_document_created` | Triggered when a document is written to for the first time. |
| `on_document_updated` | Triggered when a document already exists and has any value changed. |
| `on_document_deleted` | Triggered when a document is deleted. |
| `on_document_written` | Triggered when `on_document_created`, `on_document_updated` or `on_document_deleted` is triggered. |
| `on_document_created_with_auth_context` | `on_document_created` with additional authentication information |
| `on_document_updated_with_auth_context` | `on_document_updated` with additional authentication information |
| `on_document_deleted_with_auth_context` | `on_document_deleted` with additional authentication information |
| `on_document_written_with_auth_context` | `on_document_written` with additional authentication information |

Firebase events trigger only
on document changes. An update to a Firebase document where data
is unchanged (a no-op write) does not generate an update or write event. It is
not possible to add events to specific fields.

If you don't have a project enabled for Cloud Functions for Firebase yet, then read
[Get started with Cloud Functions for Firebase (2nd gen)](https://firebase.google.com/docs/functions/beta/get-started)
to configure and set up your Cloud Functions for Firebase project.

## Writing Firebase-triggered functions

### Define a function trigger

To define a Firebase trigger, specify a document path and an event type:

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

Document paths can reference either a [specific document](https://firebase.google.com/docs/firestore/enterprise/extend-with-functions-2nd-gen-mongodb#specific-documents)
or a [wildcard pattern](https://firebase.google.com/docs/firestore/enterprise/extend-with-functions-2nd-gen-mongodb#wildcards-parameters).

### Specify a single document

If you want to trigger an event for *any* change to a specific document then
you can use the following function.

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

If you want to attach a trigger to a group of documents, such as any document in
a certain collection, then use a `{wildcard}` in place of the
document ID:

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

In this example, when any field on any document in `users` is changed, it matches
a wildcard called `userId`.

Wildcard matches are extracted from the document path and stored into `event.params`.
Your trigger must *always* point to a document, even if you're using a wildcard.

## Event Triggers

### Trigger a function when a new document is created

You can trigger a function to fire any time a new document is created in a collection.
This example function triggers every time a new user profile is added:

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

For additional authentication information, use `onDocumentCreatedWithAuthContext`.

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

You can also trigger a function to fire when a document is updated.
This example function fires if a user changes their profile:

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

For additional authentication information, use `onDocumentUpdatedWithAuthContext`.

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

You can also trigger a function when a document is deleted. This example
function fires when a user deletes their user profile:

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

For additional authentication information, use `onDocumentDeletedWithAuthContext`.

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

If you don't care about the type of event being fired, you can listen for all
changes in a Firebase document using the "document written" event
trigger. This example function fires if a user is created, updated, or deleted:

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

For additional authentication information, use `onDocumentWrittenWithAuthContext`.

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

When a function is triggered, it provides a snapshot of the data related to the
event. You can use this snapshot to read from or write to the document that
triggered the event, or use the Firebase Admin SDK to access other parts
of your database.

### Event Data

#### Reading Data

When a function is triggered, you might want to get data from a document that
was updated, or get the data prior to update. You can get the prior data by using
`event.data.before`, which contains the document snapshot before the update.
Similarly, `event.data.after` contains the document snapshot state after the
update.

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

You can access properties as you would in any other object. Alternatively, you
can use the `get` function to access specific fields:

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

Each function invocation is associated with a specific document in your
Firebase database. You can access that document in
the snapshot returned to your function.

The document reference includes methods like `update()`, `set()`, and `remove()`
so you can modify the document that triggered the function.

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

> [!WARNING]
> **Warning:** Any time you write to the same document that triggered a function, you are at risk of creating an infinite loop. Use caution and ensure that you safely exit the function when no change is needed.

### Access user authentication information

If you use one of the of the following event types, you can access
user authentication information about the principal that triggered the event.
This information is in addition to the information returned in the base event.

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

For information about the data available in the authentication context, see
[Auth Context](https://github.com/cloudevents/spec/blob/main/cloudevents/extensions/authcontext.md).
The following example demonstrates how to retrieve authentication information:

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

Cloud Functions execute in a trusted environment. They are
authorized as a service account on your project, and you can perform reads and
writes using the [Firebase Admin SDK](https://firebase.google.com/docs/reference/admin):

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

> [!NOTE]
> **Note:** Reads and writes performed in Cloud Functions are not controlled by your security rules, they can access any part of your database.

## Limitations

- Ordering is not guaranteed. Rapid changes can trigger function invocations in an unexpected order.
- Events are delivered at least once, but a single event might result in multiple function invocations. Avoid depending on exactly-once mechanics, and write [idempotent functions](https://firebase.google.com/blog/products/serverless/cloud-functions-pro-tips-building-idempotent-functions).
- A trigger is associated with a single database. You can't create a trigger that matches multiple databases.
- Deleting a database doesn't automatically delete any triggers for that database. The trigger stops delivering events but continues to exist until you [delete the trigger](https://firebase.google.com/eventarc/docs/managing-triggers#trigger-delete).