# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md.txt

# firestore namespace

## Functions

| Function | Description |
|---|---|
| [beforeSnapshotConstructor(event)](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md#firestorebeforesnapshotconstructor) |   |
| [database(database)](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md#firestoredatabase) |   |
| [document(path)](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md#firestoredocument) | Select the Firestore document to listen to for events. |
| [namespace(namespace)](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md#firestorenamespace) |   |
| [snapshotConstructor(event)](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md#firestoresnapshotconstructor) |   |

## Classes

| Class | Description |
|---|---|
| [DatabaseBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.databasebuilder.md#firestoredatabasebuilder_class) |   |
| [DocumentBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.documentbuilder.md#firestoredocumentbuilder_class) |   |
| [NamespaceBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.namespacebuilder.md#firestorenamespacebuilder_class) |   |

## Type Aliases

| Type Alias | Description |
|---|---|
| [DocumentSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md#firestoredocumentsnapshot) |   |
| [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md#firestorequerydocumentsnapshot) |   |

## firestore.beforeSnapshotConstructor()

**Signature:**

    export declare function beforeSnapshotConstructor(event: LegacyEvent): DocumentSnapshot;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| event | [LegacyEvent](https://firebase.google.com/docs/reference/functions/firebase-functions.legacyevent.md#legacyevent_interface) |   |

**Returns:**

[DocumentSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md#firestoredocumentsnapshot)

## firestore.database()

**Signature:**

    export declare function database(database: string): DatabaseBuilder;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| database | string |   |

**Returns:**

[DatabaseBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.databasebuilder.md#firestoredatabasebuilder_class)

## firestore.document()

Select the Firestore document to listen to for events.

**Signature:**

    export declare function document<Path extends string>(path: Path): DocumentBuilder<Path>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| path | Path | Full database path to listen to. This includes the name of the collection that the document is a part of. For example, if the collection is named "users" and the document is named "Ada", then the path is "/users/Ada". |

**Returns:**

[DocumentBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.documentbuilder.md#firestoredocumentbuilder_class)\<Path\>

## firestore.namespace()

**Signature:**

    export declare function namespace(namespace: string): NamespaceBuilder;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| namespace | string |   |

**Returns:**

[NamespaceBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.namespacebuilder.md#firestorenamespacebuilder_class)

## firestore.snapshotConstructor()

**Signature:**

    export declare function snapshotConstructor(event: LegacyEvent): DocumentSnapshot;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| event | [LegacyEvent](https://firebase.google.com/docs/reference/functions/firebase-functions.legacyevent.md#legacyevent_interface) |   |

**Returns:**

[DocumentSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md#firestoredocumentsnapshot)

## firestore.DocumentSnapshot

**Signature:**

    export type DocumentSnapshot = firestore.DocumentSnapshot;

## firestore.QueryDocumentSnapshot

**Signature:**

    export type QueryDocumentSnapshot = firestore.QueryDocumentSnapshot;