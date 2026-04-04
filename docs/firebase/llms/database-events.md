# Source: https://firebase.google.com/docs/functions/database-events.md.txt

<br />

| **Note:**This feature is a public preview. This means that the functionality might change in backward-incompatible ways. A preview release is not subject to any SLA or deprecation policy and may receive limited or no support.

WithCloud Functions, you can handle events in theFirebase Realtime Databasewith no need to update client code.Cloud Functionslets you runRealtime Databaseoperations with full administrative privileges, and ensures that each change toRealtime Databaseis processed individually. You can makeFirebase Realtime Databasechanges via the data snapshot or via the Admin SDK.

In a typical lifecycle, aFirebase Realtime Databasefunction does the following:

1. Waits for changes to a particularRealtime Databasepath.
2. Triggers when an event occurs and performs its tasks.
3. Receives a data object that contains a snapshot of the data stored at that path.

You can trigger a function in response to the writing, creating, updating, or deleting of database nodes inFirebase Realtime Database. To control when the function triggers, specify one of the event handlers, and specify theRealtime Databasepath where it will listen for events.

## Setting the function location

Distance between the location of aRealtime Databaseinstance and the location of the function can create significant network latency. Also, a mismatch between regions can result in deployment failure. To avoid these situations, specify the[function location](https://firebase.google.com/docs/functions/beta/manage-functions#modify-region)so that it matches the[database instance location](https://firebase.google.com/docs/projects/locations#rtdb-locations).

## HandlingRealtime Databaseevents

Functions let you handleRealtime Databaseevents at two levels of specificity; you can listen for specifically for only write, creation, update, or deletion events, or you can listen for any change of any kind to a reference.

These handlers for responding toRealtime Databaseevents are available:  

### Node.js

- `onValueWritten()`Triggered when data is created, updated, or deleted inRealtime Database.
- `onValueCreated()`Only triggered when data is created inRealtime Database.
- `onValueUpdated()`Only triggered when data is updated inRealtime Database.
- `onValueDeleted()`Only triggered when data is deleted inRealtime Database.

### Python

- `on_value_written()`Triggered when data is created, updated, or deleted inRealtime Database.
- `on_value_created()`Only triggered when data is created inRealtime Database.
- `on_value_updated()`Only triggered when data is updated inRealtime Database.
- `on_value_deleted()`Only triggered when data is deleted inRealtime Database.

## Import required modules

In your function source, you must import SDK modules that you want to use. For this sample, it is necessary to import HTTP andRealtime Databasemodules along with theFirebaseAdmin SDKmodule for writing toRealtime Database.  

### Node.js

    // The Cloud Functions for Firebase SDK to setup triggers and logging.
    const {onRequest} = require("firebase-functions/https");
    const {onValueCreated} = require("firebase-functions/database");
    const {logger} = require("firebase-functions");

    // The Firebase Admin SDK to access the Firebase Realtime Database.
    const admin = require("firebase-admin");
    admin.initializeApp();  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/uppercase-rtdb/functions/index.js#L20-L27

### Python

    # The Cloud Functions for Firebase SDK to create Cloud Functions and set up triggers.
    from firebase_functions import db_fn, https_fn

    # The Firebase Admin SDK to access the Firebase Realtime Database.
    from firebase_admin import initialize_app, db

    app = initialize_app()  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/uppercase-rtdb/functions/main.py#L20-L26

## Specify instance and path

To control when and where your function should trigger, configure your function with a path and optionally aRealtime Databaseinstance. If you do not specify an instance, the function listens to the allRealtime Databaseinstances in the function region. You may also specify aRealtime Databaseinstance pattern to deploy to a selective subset of instances in the same region.

For example:  

### Node.js

```javascript
// All Realtime Database instances in default function region us-central1 at path "/user/{uid}"
// There must be at least one Realtime Database present in us-central1.
const onWrittenFunctionDefault = onValueWritten("/user/{uid}", (event) => {
  // ...
});

// Instance named "my-app-db-2", at path "/user/{uid}".
// The "my-app-db-2" instance must exist in this region.
const OnWrittenFunctionInstance = onValueWritten(
  {
    ref: "/user/{uid}",
    instance: "my-app-db-2"
    // This example assumes us-central1, but to set location:
    // region: "europe-west1"
  },
  (event) => {
    // ...
  }
);

// Instance with "my-app-db-" prefix, at path "/user/{uid}", where uid ends with @gmail.com.
// There must be at least one Realtime Database with "my-app-db-*" prefix in this region.
const onWrittenFunctionInstance = onValueWritten(
  {
    ref: "/user/{uid=*@gmail.com}",
    instance: "my-app-db-*"
    // This example assumes us-central1, but to set location:
    // region: "europe-west1"
  },
  (event) => {
    // ...
  }
);
```

### Python

    # All Realtime Database instances in default function region us-central1 at path "/user/{uid}"
    # There must be at least one Realtime Database present in us-central1.
    @db_fn.on_value_written(r"/user/{uid}")
    def onwrittenfunctiondefault(event: db_fn.Event[db_fn.Change]):
        # ...
        pass

    # Instance named "my-app-db-2", at path "/user/{uid}".
    # The "my-app-db-2" instance must exist in this region.
    @db_fn.on_value_written(
        reference=r"/user/{uid}",
        instance="my-app-db-2",
        # This example assumes us-central1, but to set location:
        # region="europe-west1",
    )
    def on_written_function_instance(event: db_fn.Event[db_fn.Change]):
        # ...
        pass

    # Instance with "my-app-db-" prefix, at path "/user/{uid}", where uid ends with @gmail.com.
    # There must be at least one Realtime Database with "my-app-db-*" prefix in this region.
    @db_fn.on_value_written(
        reference=r"/user/{uid=*@gmail.com}",
        instance="my-app-db-*",
        # This example assumes us-central1, but to set location:
        # region="europe-west1",
    )
    def on_written_function_instance(event: db_fn.Event[db_fn.Change]):
        # ...
        pass

These parameters direct your function to handle writes at a certain path within theRealtime Databaseinstance.

Path specifications match*all* writes that touch a path, including writes that happen anywhere below it. If you set the path for your function as`/foo/bar`, it matches events at both of these locations:  

     /foo/bar
     /foo/bar/baz/really/deep/path

In either case, Firebase interprets that the event occurs at`/foo/bar`, and the event data includes the old and new data at`/foo/bar`. If the event data might be large, consider using multiple functions at deeper paths instead of a single function near the root of your database. For the best performance, only request data at the deepest level possible.

### Wildcarding and capturing

You can use`{key}`,`{key=*}`,`{key=prefix*}`,`{key=*suffix}`for capturing.`*`,`prefix*`,`*suffix`for single-segment wildcarding. Note:`**`represents multi-segment wildcarding, whichRealtime Databasedoes not support. See[Understand path patterns](https://cloud.google.com/eventarc/docs/path-patterns#apply_a_path_pattern).

**Path wildcarding.**You can specify a path component as a wildcard:

- Using asterisk,`*`. For example,`foo/*`matches any children one level of the node hierarchy below`foo/`.
- Using a segment containing exactly asterisk,`*`. For example,`foo/app*-us`matches any child segments below`foo/`with`app`prefix and`-us`suffix.

Paths with wildcards can match multiple events from, for example, a single write. An insert of  

    {
      "foo": {
        "hello": "world",
        "firebase": "functions"
      }
    }

matches the path`"/foo/*"`twice: once with`"hello": "world"`and again with`"firebase": "functions"`.

**Path capturing.** You can capture path matches into named variables to be used in your function code (e.g.`/user/{uid}`,`/user/{uid=*-us}`).

The values of the capture variables are available within the[database.DatabaseEvent.params](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent#databasedatabaseeventparams)object of your function.

**Instance wildcarding.** You can also specify an instance component using wildcarding. A instance wildcard can have prefix, suffix or both (e.g.`my-app-*-prod`).

### Wildcard and capture reference

WithCloud Functions(2nd gen) andRealtime Database, a pattern can be used when specifying`ref`and`instance`. Each trigger interface will have the following options for scoping a function:

|  **Specifying`ref`**   |  **Specifying`instance`**  |                                  **Behavior**                                  |
|------------------------|----------------------------|--------------------------------------------------------------------------------|
| Single (`/foo/bar`)    | Not specifying             | Scopes handler to all instances in the function region.                        |
| Single (`/foo/bar`)    | Single (`'my-new-db'`)     | Scopes handler to the specific instance in the function region.                |
| Single (`/foo/bar`)    | Pattern (`'inst-prefix*'`) | Scopes handler to all instances that match the pattern in the function region. |
| Pattern (`/foo/{bar}`) | Not specifying             | Scopes handler to all instances in the function region.                        |
| Pattern (`/foo/{bar}`) | Single (`'my-new-db'`)     | Scopes handler to the specific instance in the function region.                |
| Pattern (`/foo/{bar}`) | Pattern (`'inst-prefix*'`) | Scopes handler to all instances that match the pattern in the function region. |

## Handle event data

When aRealtime Databaseevent triggers, it passes an`Event`object to your handler function. This object has a`data`property, which, for creation and deletion events, contains a snapshot of the data created or deleted.

In this example, the function retrieves the data for the referenced path, converts the string at that location to uppercase, and writes that modified string to the database:  

### Node.js

    // Listens for new messages added to /messages/:pushId/original and creates an
    // uppercase version of the message to /messages/:pushId/uppercase
    // for all databases in 'us-central1'
    exports.makeuppercase = onValueCreated(
        "/messages/{pushId}/original",
        (event) => {
        // Grab the current value of what was written to the Realtime Database.
          const original = event.data.val();
          logger.log("Uppercasing", event.params.pushId, original);
          const uppercase = original.toUpperCase();
          // You must return a Promise when performing
          // asynchronous tasks inside a function, such as
          // writing to the Firebase Realtime Database.
          // Setting an "uppercase" sibling in the
          // Realtime Database returns a Promise.
          return event.data.ref.parent.child("uppercase").set(uppercase);
        },
    );  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/uppercase-rtdb/functions/index.js#L54-L71

### Python

    @db_fn.on_value_created(reference="/messages/{pushId}/original")
    def makeuppercase(event: db_fn.Event[Any]) -> None:
        """Listens for new messages added to /messages/{pushId}/original and
        creates an uppercase version of the message to /messages/{pushId}/uppercase
        """

        # Grab the value that was written to the Realtime Database.
        original = event.data
        if not isinstance(original, str):
            print(f"Not a string: {event.reference}")
            return

        # Use the Admin SDK to set an "uppercase" sibling.
        print(f"Uppercasing {event.params['pushId']}: {original}")
        upper = original.upper()
        parent = db.reference(event.reference).parent
        if parent is None:
            print("Message can't be root node.")
            return
        parent.child("uppercase").set(upper)  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/uppercase-rtdb/functions/main.py#L57-L76

### Reading the previous value

For`write`or`update`events, the`data`property is a`Change`object that contains two snapshots that represent the data state before and after the triggering event. The`Change`object has a`before`property that lets you inspect what was saved toRealtime Database*before* the event and an`after`property that represents the state of the data*after*the event happened.

For example, the`before`property can be used to make sure the function only uppercases text when it is first created:  

### Node.js

```javascript
  exports makeUppercase = onValueWritten("/messages/{pushId}/original", (event) => {
        // Only edit data when it is first created.
        if (event.data.before.exists()) {
          return null;
        }
        // Exit when the data is deleted.
        if (!event.data.after.exists()) {
          return null;
        }
        // Grab the current value of what was written to the Realtime Database.
        const original = event.data.after.val();
        console.log('Uppercasing', event.params.pushId, original);
        const uppercase = original.toUpperCase();
        // You must return a Promise when performing asynchronous tasks inside a Functions such as
        // writing to the Firebase Realtime Database.
        // Setting an "uppercase" sibling in the Realtime Database returns a Promise.
        return event.data.after.ref.parent.child('uppercase').set(uppercase);
      });
```

### Python

    @db_fn.on_value_written(reference="/messages/{pushId}/original")
    def makeuppercase2(event: db_fn.Event[db_fn.Change]) -> None:
        """Listens for new messages added to /messages/{pushId}/original and
        creates an uppercase version of the message to /messages/{pushId}/uppercase
        """

        # Only edit data when it is first created.
        if event.data.before is not None:
            return

        # Exit when the data is deleted.
        if event.data.after is None:
            return

        # Grab the value that was written to the Realtime Database.
        original = event.data.after
        if not hasattr(original, "upper"):
            print(f"Not a string: {event.reference}")
            return

        # Use the Admin SDK to set an "uppercase" sibling.
        print(f"Uppercasing {event.params['pushId']}: {original}")
        upper = original.upper()
        parent = db.reference(event.reference).parent
        if parent is None:
            print("Message can't be root node.")
            return
        parent.child("uppercase").set(upper)  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/uppercase-rtdb/functions/main.py#L81-L108