# Source: https://firebase.google.com/docs/functions/1st-gen/database-events-1st.md.txt

<br />

**Note:** The 1st-gen functionality described in this page is also supported inCloud Functions(2nd gen) with improved features and performance. For more information about 2nd gen, see the[version comparison](https://firebase.google.com/docs/functions/version-comparison). To go directly to the 2nd gen guide for this feature, see[Realtime Database triggers](https://firebase.google.com/docs/functions/database-events).  

WithCloud Functions, you can handle events in theFirebase Realtime Databasewith no need to update client code.Cloud Functionslets you runRealtime Databaseoperations with full administrative privileges, and ensures that each change toRealtime Databaseis processed individually. You can makeFirebase Realtime Databasechanges via the[`DataSnapshot`](https://firebase.google.com/docs/reference/functions/firebase-functions.database.datasnapshot)or via the[Admin SDK](https://firebase.google.com/docs/database/admin/start).

In a typical lifecycle, aFirebase Realtime Databasefunction does the following:

1. Waits for changes to a particularRealtime Databaselocation.
2. Triggers when an event occurs and performs its tasks (see[What can I do withCloud Functions?](https://firebase.google.com/docs/functions/use-cases)for examples of use cases).
3. Receives a data object that contains a snapshot of the data stored in the specified document.

## Trigger aRealtime Databasefunction

Create new functions forRealtime Databaseevents with[`functions.database`](https://firebase.google.com/docs/reference/functions/firebase-functions.database). To control when the function triggers, specify one of the event handlers, and specify theRealtime Databasepath where it will listen for events.

### Set the event handler

Functions let you handleRealtime Databaseevents at two levels of specificity; you can listen for specifically for only creation, update, or deletion events, or you can listen for any change of any kind to a path.Cloud Functionssupports these event handlers forRealtime Database:

- [`onWrite()`](https://firebase.google.com/docs/reference/functions/firebase-functions.database.refbuilder#databaserefbuilderonwrite), which triggers when data is created, updated, or deleted inRealtime Database.
- [`onCreate()`](https://firebase.google.com/docs/reference/functions/firebase-functions.database.refbuilder#databaserefbuilderoncreate), which triggers when new data is created inRealtime Database.
- [`onUpdate()`](https://firebase.google.com/docs/reference/functions/firebase-functions.database.refbuilder#databaserefbuilderonupdate), which triggers when data is updated inRealtime Database.
- [`onDelete()`](https://firebase.google.com/docs/reference/functions/firebase-functions.database.refbuilder#databaserefbuilderondelete), which triggers when data is deleted fromRealtime Database.

### Specify the instance and path

To control when and where your function should trigger, call[`ref(path)`](https://firebase.google.com/docs/reference/functions/firebase-functions.database#databaseref)to specify a path, and optionally specify aRealtime Databaseinstance with`instance('INSTANCE_NAME')`. If you do not specify an instance, the function deploys to the defaultRealtime Databaseinstance for the Firebase project For example:

- DefaultRealtime Databaseinstance:`functions.database.ref('/foo/bar')`
- Instance named "my-app-db-2":`functions.database.instance('my-app-db-2').ref('/foo/bar')`

These methods direct your function to handle writes at a certain path within theRealtime Databaseinstance. Path specifications match*all* writes that touch a path, including writes that happen anywhere below it. If you set the path for your function as`/foo/bar`, it matches events at both of these locations:  

     /foo/bar
     /foo/bar/baz/really/deep/path

In either case, Firebase interprets that the event occurs at`/foo/bar`, and the event data includes the old and new data at`/foo/bar`. If the event data might be large, consider using multiple functions at deeper paths instead of a single function near the root of your database. For the best performance, only request data at the deepest level possible.

You can specify a path component as a wildcard by surrounding it with curly brackets;`ref('foo/{bar}')`matches any child of`/foo`. The values of these wildcard path components are available within the[`EventContext.params`](https://firebase.google.com/docs/reference/functions/cloud_functions.eventcontext#params)object of your function. In this example, the value is available as`context.params.bar`.

Paths with wildcards can match multiple events from a single write. An insert of  

    {
      "foo": {
        "hello": "world",
        "firebase": "functions"
      }
    }

matches the path`"/foo/{bar}"`twice: once with`"hello": "world"`and again with`"firebase": "functions"`.

## Handle event data

When handling aRealtime Databaseevent, the data object returned is a[`DataSnapshot`](https://firebase.google.com/docs/reference/functions/firebase-functions.database.datasnapshot). For`onWrite`or`onUpdate`events, the first parameter is a`Change`object that contains two snapshots that represent the data state before and after the triggering event. For`onCreate`and`onDelete`events, the data object returned is a snapshot of the data created or deleted.

In this example, the function retrieves the snapshot for the specified path, converts the string at that location to uppercase, and writes that modified string to the database:

<br />

```gdscript
// Listens for new messages added to /messages/:pushId/original and creates an
// uppercase version of the message to /messages/:pushId/uppercase
exports.makeUppercase = functions.database.ref('/messages/{pushId}/original')
    .onCreate((snapshot, context) => {
      // Grab the current value of what was written to the Realtime Database.
      const original = snapshot.val();
      functions.logger.log('Uppercasing', context.params.pushId, original);
      const uppercase = original.toUpperCase();
      // You must return a Promise when performing asynchronous tasks inside a Functions such as
      // writing to the Firebase Realtime Database.
      // Setting an "uppercase" sibling in the Realtime Database returns a Promise.
      return snapshot.ref.parent.child('uppercase').set(uppercase);
    });https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/uppercase-rtdb/functions/index.js#L46-L58
```

<br />

### Accessing user authentication information

From[`EventContext.auth`](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext#eventcontextauth)and[`EventContext.authType`](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext#eventcontextauthtype), you can access the user information, including permissions, for the user that triggered a function. This can be useful for enforcing security rules, allowing your function to complete different operations based on the user's level of permissions:  

    const functions = require('firebase-functions/v1');
    const admin = require('firebase-admin');

    exports.simpleDbFunction = functions.database.ref('/path')
        .onCreate((snap, context) => {
          if (context.authType === 'ADMIN') {
            // do something
          } else if (context.authType === 'USER') {
            console.log(snap.val(), 'written by', context.auth.uid);
          }
        });

Also, you can leverage user authentication information to "impersonate" a user and perform write operations on the user's behalf. Make sure to delete the app instance as shown below in order to prevent concurrency issues:  

    exports.impersonateMakeUpperCase = functions.database.ref('/messages/{pushId}/original')
        .onCreate((snap, context) => {
          const appOptions = JSON.parse(process.env.FIREBASE_CONFIG);
          appOptions.databaseAuthVariableOverride = context.auth;
          const app = admin.initializeApp(appOptions, 'app');
          const uppercase = snap.val().toUpperCase();
          const ref = snap.ref.parent.child('uppercase');

          const deleteApp = () => app.delete().catch(() => null);

          return app.database().ref(ref).set(uppercase).then(res => {
            // Deleting the app is necessary for preventing concurrency leaks
            return deleteApp().then(() => res);
          }).catch(err => {
            return deleteApp().then(() => Promise.reject(err));
          });
        });

### Reading the previous value

The`Change`object has a[`before`](https://firebase.google.com/docs/reference/functions/firebase-functions.change#changebefore)property that lets you inspect what was saved toRealtime Database*before* the event. The`before`property returns a`DataSnapshot`where all methods (for example,[`val()`](https://firebase.google.com/docs/reference/functions/firebase-functions.database.datasnapshot#databasedatasnapshotval)and[`exists()`](https://firebase.google.com/docs/reference/functions/firebase-functions.database.datasnapshot#databasedatasnapshotexists)) refer to the previous value. You can read the new value again by either using the original`DataSnapshot`or reading the[`after`](https://firebase.google.com/docs/reference/functions/firebase-functions.change#changeafter)property. This property on any`Change`is another`DataSnapshot`representing the state of the data*after*the event happened.

For example, the`before`property can be used to make sure the function only uppercases text when it is first created:  

    exports.makeUppercase = functions.database.ref('/messages/{pushId}/original')
        .onWrite((change, context) => {
          // Only edit data when it is first created.
          if (change.before.exists()) {
            return null;
          }
          // Exit when the data is deleted.
          if (!change.after.exists()) {
            return null;
          }
          // Grab the current value of what was written to the Realtime Database.
          const original = change.after.val();
          console.log('Uppercasing', context.params.pushId, original);
          const uppercase = original.toUpperCase();
          // You must return a Promise when performing asynchronous tasks inside a Functions such as
          // writing to the Firebase Realtime Database.
          // Setting an "uppercase" sibling in the Realtime Database returns a Promise.
          return change.after.ref.parent.child('uppercase').set(uppercase);
        });