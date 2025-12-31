# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md.txt

# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md.txt

# firestore namespace

## Functions

|                                                                                              Function                                                                                              |                                                                                        Description                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [onDocumentCreated(document, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoreondocumentcreated)                               | Event handler that triggers when a document is created in Firestore.                                                                                                                      |
| [onDocumentCreated(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoreondocumentcreated)                                   | Event handler that triggers when a document is created in Firestore.                                                                                                                      |
| [onDocumentCreatedWithAuthContext(document, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoreondocumentcreatedwithauthcontext) | Event handler that triggers when a document is created in Firestore. This trigger also provides the authentication context of the principal who triggered the event.                      |
| [onDocumentCreatedWithAuthContext(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoreondocumentcreatedwithauthcontext)     | Event handler that triggers when a document is created in Firestore. This trigger also provides the authentication context of the principal who triggered the event.                      |
| [onDocumentDeleted(document, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoreondocumentdeleted)                               | Event handler that triggers when a document is deleted in Firestore.                                                                                                                      |
| [onDocumentDeleted(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoreondocumentdeleted)                                   | Event handler that triggers when a document is deleted in Firestore.                                                                                                                      |
| [onDocumentDeletedWithAuthContext(document, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoreondocumentdeletedwithauthcontext) | Event handler that triggers when a document is deleted in Firestore. This trigger also provides the authentication context of the principal who triggered the event.                      |
| [onDocumentDeletedWithAuthContext(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoreondocumentdeletedwithauthcontext)     | Event handler that triggers when a document is deleted in Firestore. This trigger also provides the authentication context of the principal who triggered the event.                      |
| [onDocumentUpdated(document, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoreondocumentupdated)                               | Event handler that triggers when a document is updated in Firestore.                                                                                                                      |
| [onDocumentUpdated(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoreondocumentupdated)                                   | Event handler that triggers when a document is updated in Firestore.                                                                                                                      |
| [onDocumentUpdatedWithAuthContext(document, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoreondocumentupdatedwithauthcontext) | Event handler that triggers when a document is updated in Firestore. This trigger also provides the authentication context of the principal who triggered the event.                      |
| [onDocumentUpdatedWithAuthContext(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoreondocumentupdatedwithauthcontext)     | Event handler that triggers when a document is updated in Firestore. This trigger also provides the authentication context of the principal who triggered the event.                      |
| [onDocumentWritten(document, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoreondocumentwritten)                               | Event handler that triggers when a document is created, updated, or deleted in Firestore.                                                                                                 |
| [onDocumentWritten(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoreondocumentwritten)                                   | Event handler that triggers when a document is created, updated, or deleted in Firestore.                                                                                                 |
| [onDocumentWrittenWithAuthContext(document, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoreondocumentwrittenwithauthcontext) | Event handler that triggers when a document is created, updated, or deleted in Firestore. This trigger also provides the authentication context of the principal who triggered the event. |
| [onDocumentWrittenWithAuthContext(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoreondocumentwrittenwithauthcontext)     | Event handler that triggers when a document is created, updated, or deleted in Firestore. This trigger also provides the authentication context of the principal who triggered the event. |

## Classes

|                                                                  Class                                                                   |                                                                                                          Description                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.change.md#firestorechange_class) | The Cloud Functions interface for events that change state, such as Realtime Database or Cloud Firestore `onWrite` and `onUpdate` events.For more information about the format used to construct `Change` objects, see below. |

## Interfaces

|                                                                                    Interface                                                                                     |                                              Description                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [DocumentOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.documentoptions.md#firestoredocumentoptions_interface)          | DocumentOptions extend EventHandlerOptions with provided document and optional database and namespace. |
| [FirestoreAuthEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md#firestorefirestoreauthevent_interface) |                                                                                                        |
| [FirestoreEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreevent_interface)             | A CloudEvent that contains a DocumentSnapshot or a Change                                              |

## Type Aliases

|                                                                        Type Alias                                                                         |                                                                                                                                                                                                                                                                   Description                                                                                                                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AuthType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoreauthtype)                           | AuthType defines the possible values for the authType field in a Firestore event with auth context. - service_account: a non-user principal used to identify a workload or machine user. - api_key: a non-user client API key. - system: an obscured identity used when Cloud Platform or another system triggered the event. Examples include a database record which was deleted based on a TTL. - unauthenticated: an unauthenticated action. - unknown: a general type to capture all other principals not captured in the other auth types. |
| [DocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoredocumentsnapshot)           | A Firestore DocumentSnapshot                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot) | A Firestore QueryDocumentSnapshot                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## firestore.onDocumentCreated()

Event handler that triggers when a document is created in Firestore.

**Signature:**  

    export declare function onDocumentCreated<Document extends string>(document: Document, handler: (event: FirestoreEvent<QueryDocumentSnapshot | undefined, ParamsOf<Document>>) => any | Promise<any>): CloudFunction<FirestoreEvent<QueryDocumentSnapshot | undefined, ParamsOf<Document>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                    Type                                                                                                                                                                                                                                                     |                           Description                            |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| document  | Document                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | The Firestore document path to trigger on.                       |
| handler   | (event: [FirestoreEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreevent_interface)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot) \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Firestore create occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[FirestoreEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreevent_interface)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot) \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>\>

## firestore.onDocumentCreated()

Event handler that triggers when a document is created in Firestore.

**Signature:**  

    export declare function onDocumentCreated<Document extends string>(opts: DocumentOptions<Document>, handler: (event: FirestoreEvent<QueryDocumentSnapshot | undefined, ParamsOf<Document>>) => any | Promise<any>): CloudFunction<FirestoreEvent<QueryDocumentSnapshot | undefined, ParamsOf<Document>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                    Type                                                                                                                                                                                                                                                     |                            Description                            |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| opts      | [DocumentOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.documentoptions.md#firestoredocumentoptions_interface)\<Document\>                                                                                                                                                                                                                                                                                                                         | Options that can be set on an individual event-handling function. |
| handler   | (event: [FirestoreEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreevent_interface)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot) \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Firestore create occurs.  |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[FirestoreEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreevent_interface)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot) \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>\>

## firestore.onDocumentCreatedWithAuthContext()

Event handler that triggers when a document is created in Firestore. This trigger also provides the authentication context of the principal who triggered the event.

**Signature:**  

    export declare function onDocumentCreatedWithAuthContext<Document extends string>(document: Document, handler: (event: FirestoreAuthEvent<QueryDocumentSnapshot | undefined, ParamsOf<Document>>) => any | Promise<any>): CloudFunction<FirestoreAuthEvent<QueryDocumentSnapshot | undefined, ParamsOf<Document>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                          Type                                                                                                                                                                                                                                                           |                           Description                            |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| document  | Document                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | The Firestore document path to trigger on.                       |
| handler   | (event: [FirestoreAuthEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md#firestorefirestoreauthevent_interface)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot) \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Firestore create occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[FirestoreAuthEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md#firestorefirestoreauthevent_interface)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot) \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>\>

## firestore.onDocumentCreatedWithAuthContext()

Event handler that triggers when a document is created in Firestore. This trigger also provides the authentication context of the principal who triggered the event.

**Signature:**  

    export declare function onDocumentCreatedWithAuthContext<Document extends string>(opts: DocumentOptions<Document>, handler: (event: FirestoreAuthEvent<QueryDocumentSnapshot | undefined, ParamsOf<Document>>) => any | Promise<any>): CloudFunction<FirestoreAuthEvent<QueryDocumentSnapshot | undefined, ParamsOf<Document>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                          Type                                                                                                                                                                                                                                                           |                            Description                            |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| opts      | [DocumentOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.documentoptions.md#firestoredocumentoptions_interface)\<Document\>                                                                                                                                                                                                                                                                                                                                     | Options that can be set on an individual event-handling function. |
| handler   | (event: [FirestoreAuthEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md#firestorefirestoreauthevent_interface)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot) \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Firestore create occurs.  |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[FirestoreAuthEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md#firestorefirestoreauthevent_interface)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot) \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>\>

## firestore.onDocumentDeleted()

Event handler that triggers when a document is deleted in Firestore.

**Signature:**  

    export declare function onDocumentDeleted<Document extends string>(document: Document, handler: (event: FirestoreEvent<QueryDocumentSnapshot | undefined, ParamsOf<Document>>) => any | Promise<any>): CloudFunction<FirestoreEvent<QueryDocumentSnapshot | undefined, ParamsOf<Document>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                    Type                                                                                                                                                                                                                                                     |                           Description                            |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| document  | Document                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | The Firestore document path to trigger on.                       |
| handler   | (event: [FirestoreEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreevent_interface)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot) \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Firestore delete occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[FirestoreEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreevent_interface)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot) \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>\>

## firestore.onDocumentDeleted()

Event handler that triggers when a document is deleted in Firestore.

**Signature:**  

    export declare function onDocumentDeleted<Document extends string>(opts: DocumentOptions<Document>, handler: (event: FirestoreEvent<QueryDocumentSnapshot | undefined, ParamsOf<Document>>) => any | Promise<any>): CloudFunction<FirestoreEvent<QueryDocumentSnapshot | undefined, ParamsOf<Document>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                    Type                                                                                                                                                                                                                                                     |                            Description                            |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| opts      | [DocumentOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.documentoptions.md#firestoredocumentoptions_interface)\<Document\>                                                                                                                                                                                                                                                                                                                         | Options that can be set on an individual event-handling function. |
| handler   | (event: [FirestoreEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreevent_interface)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot) \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Firestore delete occurs.  |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[FirestoreEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreevent_interface)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot) \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>\>

## firestore.onDocumentDeletedWithAuthContext()

Event handler that triggers when a document is deleted in Firestore. This trigger also provides the authentication context of the principal who triggered the event.

**Signature:**  

    export declare function onDocumentDeletedWithAuthContext<Document extends string>(document: Document, handler: (event: FirestoreAuthEvent<QueryDocumentSnapshot | undefined, ParamsOf<Document>>) => any | Promise<any>): CloudFunction<FirestoreAuthEvent<QueryDocumentSnapshot | undefined, ParamsOf<Document>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                          Type                                                                                                                                                                                                                                                           |                           Description                            |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| document  | Document                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | The Firestore document path to trigger on.                       |
| handler   | (event: [FirestoreAuthEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md#firestorefirestoreauthevent_interface)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot) \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Firestore delete occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[FirestoreAuthEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md#firestorefirestoreauthevent_interface)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot) \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>\>

## firestore.onDocumentDeletedWithAuthContext()

Event handler that triggers when a document is deleted in Firestore. This trigger also provides the authentication context of the principal who triggered the event.

**Signature:**  

    export declare function onDocumentDeletedWithAuthContext<Document extends string>(opts: DocumentOptions<Document>, handler: (event: FirestoreAuthEvent<QueryDocumentSnapshot | undefined, ParamsOf<Document>>) => any | Promise<any>): CloudFunction<FirestoreAuthEvent<QueryDocumentSnapshot | undefined, ParamsOf<Document>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                          Type                                                                                                                                                                                                                                                           |                            Description                            |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| opts      | [DocumentOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.documentoptions.md#firestoredocumentoptions_interface)\<Document\>                                                                                                                                                                                                                                                                                                                                     | Options that can be set on an individual event-handling function. |
| handler   | (event: [FirestoreAuthEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md#firestorefirestoreauthevent_interface)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot) \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Firestore delete occurs.  |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[FirestoreAuthEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md#firestorefirestoreauthevent_interface)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot) \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>\>

## firestore.onDocumentUpdated()

Event handler that triggers when a document is updated in Firestore.

**Signature:**  

    export declare function onDocumentUpdated<Document extends string>(document: Document, handler: (event: FirestoreEvent<Change<QueryDocumentSnapshot> | undefined, ParamsOf<Document>>) => any | Promise<any>): CloudFunction<FirestoreEvent<Change<QueryDocumentSnapshot> | undefined, ParamsOf<Document>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                                                                                 Type                                                                                                                                                                                                                                                                                                                 |                           Description                            |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| document  | Document                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | The Firestore document path to trigger on.                       |
| handler   | (event: [FirestoreEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot)\> \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Firestore update occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[FirestoreEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot)\> \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>\>

## firestore.onDocumentUpdated()

Event handler that triggers when a document is updated in Firestore.

**Signature:**  

    export declare function onDocumentUpdated<Document extends string>(opts: DocumentOptions<Document>, handler: (event: FirestoreEvent<Change<QueryDocumentSnapshot> | undefined, ParamsOf<Document>>) => any | Promise<any>): CloudFunction<FirestoreEvent<Change<QueryDocumentSnapshot> | undefined, ParamsOf<Document>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                                                                                 Type                                                                                                                                                                                                                                                                                                                 |                            Description                            |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| opts      | [DocumentOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.documentoptions.md#firestoredocumentoptions_interface)\<Document\>                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Options that can be set on an individual event-handling function. |
| handler   | (event: [FirestoreEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot)\> \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Firestore update occurs.  |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[FirestoreEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot)\> \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>\>

## firestore.onDocumentUpdatedWithAuthContext()

Event handler that triggers when a document is updated in Firestore. This trigger also provides the authentication context of the principal who triggered the event.

**Signature:**  

    export declare function onDocumentUpdatedWithAuthContext<Document extends string>(document: Document, handler: (event: FirestoreAuthEvent<Change<QueryDocumentSnapshot> | undefined, ParamsOf<Document>>) => any | Promise<any>): CloudFunction<FirestoreAuthEvent<Change<QueryDocumentSnapshot> | undefined, ParamsOf<Document>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                                                                                       Type                                                                                                                                                                                                                                                                                                                       |                           Description                            |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| document  | Document                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | The Firestore document path to trigger on.                       |
| handler   | (event: [FirestoreAuthEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md#firestorefirestoreauthevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot)\> \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Firestore update occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[FirestoreAuthEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md#firestorefirestoreauthevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot)\> \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>\>

## firestore.onDocumentUpdatedWithAuthContext()

Event handler that triggers when a document is updated in Firestore. This trigger also provides the authentication context of the principal who triggered the event.

**Signature:**  

    export declare function onDocumentUpdatedWithAuthContext<Document extends string>(opts: DocumentOptions<Document>, handler: (event: FirestoreAuthEvent<Change<QueryDocumentSnapshot> | undefined, ParamsOf<Document>>) => any | Promise<any>): CloudFunction<FirestoreAuthEvent<Change<QueryDocumentSnapshot> | undefined, ParamsOf<Document>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                                                                                       Type                                                                                                                                                                                                                                                                                                                       |                            Description                            |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| opts      | [DocumentOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.documentoptions.md#firestoredocumentoptions_interface)\<Document\>                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Options that can be set on an individual event-handling function. |
| handler   | (event: [FirestoreAuthEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md#firestorefirestoreauthevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot)\> \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Firestore update occurs.  |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[FirestoreAuthEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md#firestorefirestoreauthevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestorequerydocumentsnapshot)\> \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>\>

## firestore.onDocumentWritten()

Event handler that triggers when a document is created, updated, or deleted in Firestore.

**Signature:**  

    export declare function onDocumentWritten<Document extends string>(document: Document, handler: (event: FirestoreEvent<Change<DocumentSnapshot> | undefined, ParamsOf<Document>>) => any | Promise<any>): CloudFunction<FirestoreEvent<Change<DocumentSnapshot> | undefined, ParamsOf<Document>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                                                                            Type                                                                                                                                                                                                                                                                                                            |                                     Description                                     |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| document  | Document                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | The Firestore document path to trigger on.                                          |
| handler   | (event: [FirestoreEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[DocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoredocumentsnapshot)\> \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Firestore create, update, or delete occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[FirestoreEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[DocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoredocumentsnapshot)\> \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>\>

## firestore.onDocumentWritten()

Event handler that triggers when a document is created, updated, or deleted in Firestore.

**Signature:**  

    export declare function onDocumentWritten<Document extends string>(opts: DocumentOptions<Document>, handler: (event: FirestoreEvent<Change<DocumentSnapshot> | undefined, ParamsOf<Document>>) => any | Promise<any>): CloudFunction<FirestoreEvent<Change<DocumentSnapshot> | undefined, ParamsOf<Document>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                                                                            Type                                                                                                                                                                                                                                                                                                            |                                     Description                                     |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| opts      | [DocumentOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.documentoptions.md#firestoredocumentoptions_interface)\<Document\>                                                                                                                                                                                                                                                                                                                                                                                                                                        | Options that can be set on an individual event-handling function.                   |
| handler   | (event: [FirestoreEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[DocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoredocumentsnapshot)\> \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Firestore create, update, or delete occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[FirestoreEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[DocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoredocumentsnapshot)\> \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>\>

## firestore.onDocumentWrittenWithAuthContext()

Event handler that triggers when a document is created, updated, or deleted in Firestore. This trigger also provides the authentication context of the principal who triggered the event.

**Signature:**  

    export declare function onDocumentWrittenWithAuthContext<Document extends string>(document: Document, handler: (event: FirestoreAuthEvent<Change<DocumentSnapshot> | undefined, ParamsOf<Document>>) => any | Promise<any>): CloudFunction<FirestoreAuthEvent<Change<DocumentSnapshot> | undefined, ParamsOf<Document>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                                                                                  Type                                                                                                                                                                                                                                                                                                                  |                                     Description                                     |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| document  | Document                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The Firestore document path to trigger on.                                          |
| handler   | (event: [FirestoreAuthEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md#firestorefirestoreauthevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[DocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoredocumentsnapshot)\> \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Firestore create, update, or delete occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[FirestoreAuthEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md#firestorefirestoreauthevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[DocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoredocumentsnapshot)\> \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>\>

## firestore.onDocumentWrittenWithAuthContext()

Event handler that triggers when a document is created, updated, or deleted in Firestore. This trigger also provides the authentication context of the principal who triggered the event.

**Signature:**  

    export declare function onDocumentWrittenWithAuthContext<Document extends string>(opts: DocumentOptions<Document>, handler: (event: FirestoreAuthEvent<Change<DocumentSnapshot> | undefined, ParamsOf<Document>>) => any | Promise<any>): CloudFunction<FirestoreAuthEvent<Change<DocumentSnapshot> | undefined, ParamsOf<Document>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                                                                                  Type                                                                                                                                                                                                                                                                                                                  |                                     Description                                     |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| opts      | [DocumentOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.documentoptions.md#firestoredocumentoptions_interface)\<Document\>                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Options that can be set on an individual event-handling function.                   |
| handler   | (event: [FirestoreAuthEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md#firestorefirestoreauthevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[DocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoredocumentsnapshot)\> \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Firestore create, update, or delete occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[FirestoreAuthEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md#firestorefirestoreauthevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[DocumentSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoredocumentsnapshot)\> \| undefined, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Document\>\>\>

## firestore.AuthType

AuthType defines the possible values for the authType field in a Firestore event with auth context. - service_account: a non-user principal used to identify a workload or machine user. - api_key: a non-user client API key. - system: an obscured identity used when Cloud Platform or another system triggered the event. Examples include a database record which was deleted based on a TTL. - unauthenticated: an unauthenticated action. - unknown: a general type to capture all other principals not captured in the other auth types.

**Signature:**  

    export type AuthType = "service_account" | "api_key" | "system" | "unauthenticated" | "unknown";

## firestore.DocumentSnapshot

A Firestore DocumentSnapshot

**Signature:**  

    export type DocumentSnapshot = firestore.DocumentSnapshot;

## firestore.QueryDocumentSnapshot

A Firestore QueryDocumentSnapshot

**Signature:**  

    export type QueryDocumentSnapshot = firestore.QueryDocumentSnapshot;