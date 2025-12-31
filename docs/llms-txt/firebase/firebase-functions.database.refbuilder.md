# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.database.refbuilder.md.txt

# database.RefBuilder class

The Firebase Realtime Database reference builder interface.

Access via \[`functions.database.ref()`\](functions.database#.ref).

**Signature:**  

    export declare class RefBuilder<Ref extends string> 

## Constructors

|                                                                               Constructor                                                                               | Modifiers |                     Description                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------|
| [(constructor)(triggerResource, options)](https://firebase.google.com/docs/reference/functions/firebase-functions.database.refbuilder.md#databaserefbuilderconstructor) |           | Constructs a new instance of the `RefBuilder` class |

## Methods

|                                                                     Method                                                                     | Modifiers |                                                       Description                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------|
| [onCreate(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.database.refbuilder.md#databaserefbuilderoncreate) |           | Event handler that fires every time new data is created in Firebase Realtime Database.                                   |
| [onDelete(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.database.refbuilder.md#databaserefbuilderondelete) |           | Event handler that fires every time data is deleted from Firebase Realtime Database.                                     |
| [onUpdate(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.database.refbuilder.md#databaserefbuilderonupdate) |           | Event handler that fires every time data is updated in Firebase Realtime Database.                                       |
| [onWrite(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.database.refbuilder.md#databaserefbuilderonwrite)   |           | Event handler that fires every time a Firebase Realtime Database write of any kind (creation, update, or delete) occurs. |

## database.RefBuilder.(constructor)

Constructs a new instance of the `RefBuilder` class

**Signature:**  

    constructor(triggerResource: () => string, options: DeploymentOptions);

### Parameters

|    Parameter    |                                                                     Type                                                                      | Description |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| triggerResource | () =\> string                                                                                                                                 |             |
| options         | [DeploymentOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.deploymentoptions.md#deploymentoptions_interface) |             |

## database.RefBuilder.onCreate()

Event handler that fires every time new data is created in Firebase Realtime Database.

**Signature:**  

    onCreate(handler: (snapshot: DataSnapshot, context: EventContext<ParamsOf<Ref>>) => PromiseLike<any> | any): CloudFunction<DataSnapshot>;

### Parameters

| Parameter |                                                                                                                                                                       Type                                                                                                                                                                        |                                      Description                                      |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| handler   | (snapshot: [DataSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class), context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)\<ParamsOf\<Ref\>\>) =\> PromiseLike\<any\> \| any | Event handler that runs every time new data is created in Firebase Realtime Database. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class)\>

A function that you can export and deploy.

## database.RefBuilder.onDelete()

Event handler that fires every time data is deleted from Firebase Realtime Database.

**Signature:**  

    onDelete(handler: (snapshot: DataSnapshot, context: EventContext<ParamsOf<Ref>>) => PromiseLike<any> | any): CloudFunction<DataSnapshot>;

### Parameters

| Parameter |                                                                                                                                                                       Type                                                                                                                                                                        |                                     Description                                     |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| handler   | (snapshot: [DataSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class), context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)\<ParamsOf\<Ref\>\>) =\> PromiseLike\<any\> \| any | Event handler that runs every time data is deleted from Firebase Realtime Database. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class)\>

A function that you can export and deploy.

## database.RefBuilder.onUpdate()

Event handler that fires every time data is updated in Firebase Realtime Database.

**Signature:**  

    onUpdate(handler: (change: Change<DataSnapshot>, context: EventContext<ParamsOf<Ref>>) => PromiseLike<any> | any): CloudFunction<Change<DataSnapshot>>;

### Parameters

| Parameter |                                                                                                                                                                                                                            Type                                                                                                                                                                                                                             |                                   Description                                    |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| handler   | (change: [Change](https://firebase.google.com/docs/reference/functions/firebase-functions.change.md#change_class)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class)\>, context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)\<ParamsOf\<Ref\>\>) =\> PromiseLike\<any\> \| any | Event handler which is run every time a Firebase Realtime Database write occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[Change](https://firebase.google.com/docs/reference/functions/firebase-functions.change.md#change_class)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class)\>\>

A function which you can export and deploy.

## database.RefBuilder.onWrite()

Event handler that fires every time a Firebase Realtime Database write of any kind (creation, update, or delete) occurs.

**Signature:**  

    onWrite(handler: (change: Change<DataSnapshot>, context: EventContext<ParamsOf<Ref>>) => PromiseLike<any> | any): CloudFunction<Change<DataSnapshot>>;

### Parameters

| Parameter |                                                                                                                                                                                                                            Type                                                                                                                                                                                                                             |                                  Description                                  |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| handler   | (change: [Change](https://firebase.google.com/docs/reference/functions/firebase-functions.change.md#change_class)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class)\>, context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)\<ParamsOf\<Ref\>\>) =\> PromiseLike\<any\> \| any | Event handler that runs every time a Firebase Realtime Database write occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[Change](https://firebase.google.com/docs/reference/functions/firebase-functions.change.md#change_class)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class)\>\>

A function that you can export and deploy.