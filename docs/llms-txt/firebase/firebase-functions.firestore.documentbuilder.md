# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.documentbuilder.md.txt

# firestore.DocumentBuilder class

**Signature:**  

    export declare class DocumentBuilder<Path extends string> 

## Constructors

|                                                                                     Constructor                                                                                     | Modifiers |                       Description                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------|
| [(constructor)(triggerResource, options)](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.documentbuilder.md#firestoredocumentbuilderconstructor) |           | Constructs a new instance of the `DocumentBuilder` class |

## Methods

|                                                                           Method                                                                           | Modifiers |                          Description                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------|
| [onCreate(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.documentbuilder.md#firestoredocumentbuilderoncreate) |           | Respond only to document creations.                            |
| [onDelete(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.documentbuilder.md#firestoredocumentbuilderondelete) |           | Respond only to document deletions.                            |
| [onUpdate(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.documentbuilder.md#firestoredocumentbuilderonupdate) |           | Respond only to document updates.                              |
| [onWrite(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.documentbuilder.md#firestoredocumentbuilderonwrite)   |           | Respond to all document writes (creates, updates, or deletes). |

## firestore.DocumentBuilder.(constructor)

Constructs a new instance of the `DocumentBuilder` class

**Signature:**  

    constructor(triggerResource: () => string, options: DeploymentOptions);

### Parameters

|    Parameter    |                                                                     Type                                                                      | Description |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| triggerResource | () =\> string                                                                                                                                 |             |
| options         | [DeploymentOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.deploymentoptions.md#deploymentoptions_interface) |             |

## firestore.DocumentBuilder.onCreate()

Respond only to document creations.

**Signature:**  

    onCreate(handler: (snapshot: QueryDocumentSnapshot, context: EventContext<ParamsOf<Path>>) => PromiseLike<any> | any): CloudFunction<QueryDocumentSnapshot>;

### Parameters

| Parameter |                                                                                                                                                                        Type                                                                                                                                                                         | Description |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| handler   | (snapshot: [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md#firestorequerydocumentsnapshot), context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)\<ParamsOf\<Path\>\>) =\> PromiseLike\<any\> \| any |             |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md#firestorequerydocumentsnapshot)\>

## firestore.DocumentBuilder.onDelete()

Respond only to document deletions.

**Signature:**  

    onDelete(handler: (snapshot: QueryDocumentSnapshot, context: EventContext<ParamsOf<Path>>) => PromiseLike<any> | any): CloudFunction<QueryDocumentSnapshot>;

### Parameters

| Parameter |                                                                                                                                                                        Type                                                                                                                                                                         | Description |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| handler   | (snapshot: [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md#firestorequerydocumentsnapshot), context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)\<ParamsOf\<Path\>\>) =\> PromiseLike\<any\> \| any |             |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md#firestorequerydocumentsnapshot)\>

## firestore.DocumentBuilder.onUpdate()

Respond only to document updates.

**Signature:**  

    onUpdate(handler: (change: Change<QueryDocumentSnapshot>, context: EventContext<ParamsOf<Path>>) => PromiseLike<any> | any): CloudFunction<Change<QueryDocumentSnapshot>>;

### Parameters

| Parameter |                                                                                                                                                                                                                             Type                                                                                                                                                                                                                              | Description |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| handler   | (change: [Change](https://firebase.google.com/docs/reference/functions/firebase-functions.change.md#change_class)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md#firestorequerydocumentsnapshot)\>, context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)\<ParamsOf\<Path\>\>) =\> PromiseLike\<any\> \| any |             |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[Change](https://firebase.google.com/docs/reference/functions/firebase-functions.change.md#change_class)\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md#firestorequerydocumentsnapshot)\>\>

## firestore.DocumentBuilder.onWrite()

Respond to all document writes (creates, updates, or deletes).

**Signature:**  

    onWrite(handler: (change: Change<DocumentSnapshot>, context: EventContext<ParamsOf<Path>>) => PromiseLike<any> | any): CloudFunction<Change<DocumentSnapshot>>;

### Parameters

| Parameter |                                                                                                                                                                                                                        Type                                                                                                                                                                                                                         | Description |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| handler   | (change: [Change](https://firebase.google.com/docs/reference/functions/firebase-functions.change.md#change_class)\<[DocumentSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md#firestoredocumentsnapshot)\>, context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)\<ParamsOf\<Path\>\>) =\> PromiseLike\<any\> \| any |             |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[Change](https://firebase.google.com/docs/reference/functions/firebase-functions.change.md#change_class)\<[DocumentSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.md#firestoredocumentsnapshot)\>\>