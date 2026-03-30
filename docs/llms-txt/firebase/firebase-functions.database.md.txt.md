# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.database.md.txt

# database namespace

## Functions

| Function | Description |
|---|---|
| [instance(instance)](https://firebase.google.com/docs/reference/functions/firebase-functions.database.md#databaseinstance) | Registers a function that triggers on events from a specific Firebase Realtime Database instance. |
| [ref(path)](https://firebase.google.com/docs/reference/functions/firebase-functions.database.md#databaseref) | Registers a function that triggers on Firebase Realtime Database write events. |

## Classes

| Class | Description |
|---|---|
| [DataSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class) | Interface representing a Firebase Realtime database data snapshot. |
| [InstanceBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.database.instancebuilder.md#databaseinstancebuilder_class) | The Firebase Realtime Database instance builder interface.Access via \[`database.instance()`\](providers_database_.html#instance). |
| [RefBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.database.refbuilder.md#databaserefbuilder_class) | The Firebase Realtime Database reference builder interface.Access via \[`functions.database.ref()`\](functions.database#.ref). |

## database.instance()

Registers a function that triggers on events from a specific Firebase Realtime Database instance.

Use this method together with `ref` to specify the instance on which to watch for database events. For example: `firebase.database.instance('my-app-db-2').ref('/foo/bar')`

Note that `functions.database.ref` used without `instance` watches the \*default\* instance for events.

**Signature:**

    export declare function instance(instance: string): InstanceBuilder;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| instance | string | The instance name of the database instance to watch for write events. |

**Returns:**

[InstanceBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.database.instancebuilder.md#databaseinstancebuilder_class)

Firebase Realtime Database instance builder interface.

## database.ref()

Registers a function that triggers on Firebase Realtime Database write events.

This method behaves very similarly to the method of the same name in the client and Admin Firebase SDKs. Any change to the Database that affects the data at or below the provided `path` will fire an event in Cloud Functions.

There are three important differences between listening to a Realtime Database event in Cloud Functions and using the Realtime Database in the client and Admin SDKs:

1. Cloud Functions allows wildcards in the `path` name. Any `path` component in curly brackets (`{}`) is a wildcard that matches all strings. The value that matched a certain invocation of a Cloud Function is returned as part of the \[`EventContext.params`\](cloud_functions_eventcontext.html#params object. For example, `ref("messages/{messageId}")` matches changes at `/messages/message1` or `/messages/message2`, resulting in `event.params.messageId` being set to `"message1"` or `"message2"`, respectively.

2. Cloud Functions do not fire an event for data that already existed before the Cloud Function was deployed.

3. Cloud Function events have access to more information, including a snapshot of the previous event data and information about the user who triggered the Cloud Function.

**Signature:**

    export declare function ref<Ref extends string>(path: Ref): RefBuilder<Ref>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| path | Ref | The path within the Database to watch for write events. |

**Returns:**

[RefBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.database.refbuilder.md#databaserefbuilder_class)\<Ref\>

Firebase Realtime Database builder interface.