# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.database.md.txt

# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.md.txt

# database namespace

## Functions

|                                                                         Function                                                                         |                                         Description                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [onValueCreated(ref, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.md#databaseonvaluecreated)  | Event handler which triggers when data is created in Realtime Database.                      |
| [onValueCreated(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.md#databaseonvaluecreated) | Event handler which triggers when data is created in Realtime Database.                      |
| [onValueDeleted(ref, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.md#databaseonvaluedeleted)  | Event handler which triggers when data is deleted in Realtime Database.                      |
| [onValueDeleted(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.md#databaseonvaluedeleted) | Event handler which triggers when data is deleted in Realtime Database.                      |
| [onValueUpdated(ref, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.md#databaseonvalueupdated)  | Event handler which triggers when data is updated in Realtime Database.                      |
| [onValueUpdated(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.md#databaseonvalueupdated) | Event handler which triggers when data is updated in Realtime Database.                      |
| [onValueWritten(ref, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.md#databaseonvaluewritten)  | Event handler which triggers when data is created, updated, or deleted in Realtime Database. |
| [onValueWritten(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.md#databaseonvaluewritten) | Event handler which triggers when data is created, updated, or deleted in Realtime Database. |

## Classes

|                                                                          Class                                                                           |                            Description                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [DataSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class) | Interface representing a Firebase Realtime database data snapshot. |

## Interfaces

|                                                                                        Interface                                                                                        |                                     Description                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [DatabaseEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseevent_interface)                         | A CloudEvent that contains a DataSnapshot or a Change                               |
| [RawRTDBCloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.rawrtdbcloudevent.md#databaserawrtdbcloudevent_interface)             |                                                                                     |
| [RawRTDBCloudEventData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.rawrtdbcloudeventdata.md#databaserawrtdbcloudeventdata_interface) |                                                                                     |
| [ReferenceOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptions_interface)                | ReferenceOptions extend EventHandlerOptions with provided ref and optional instance |

## database.onValueCreated()

Event handler which triggers when data is created in Realtime Database.

**Signature:**  

    export declare function onValueCreated<Ref extends string>(ref: Ref, handler: (event: DatabaseEvent<DataSnapshot, ParamsOf<Ref>>) => any | Promise<any>): CloudFunction<DatabaseEvent<DataSnapshot, ParamsOf<Ref>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                        Type                                                                                                                                                                                                                                         |                               Description                                |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| ref       | Ref                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                          |
| handler   | (event: [DatabaseEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseevent_interface)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class), [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Ref\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Realtime Database create occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[DatabaseEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseevent_interface)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class), [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Ref\>\>\>

## database.onValueCreated()

Event handler which triggers when data is created in Realtime Database.

**Signature:**  

    export declare function onValueCreated<Ref extends string>(opts: ReferenceOptions<Ref>, handler: (event: DatabaseEvent<DataSnapshot, ParamsOf<Ref>>) => any | Promise<any>): CloudFunction<DatabaseEvent<DataSnapshot, ParamsOf<Ref>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                        Type                                                                                                                                                                                                                                         |                               Description                                |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| opts      | [ReferenceOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptions_interface)\<Ref\>                                                                                                                                                                                                                                                                                                     | Options that can be set on an individual event-handling function.        |
| handler   | (event: [DatabaseEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseevent_interface)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class), [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Ref\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Realtime Database create occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[DatabaseEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseevent_interface)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class), [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Ref\>\>\>

## database.onValueDeleted()

Event handler which triggers when data is deleted in Realtime Database.

**Signature:**  

    export declare function onValueDeleted<Ref extends string>(ref: Ref, handler: (event: DatabaseEvent<DataSnapshot, ParamsOf<Ref>>) => any | Promise<any>): CloudFunction<DatabaseEvent<DataSnapshot, ParamsOf<Ref>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                        Type                                                                                                                                                                                                                                         |                                Description                                 |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| ref       | Ref                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                            |
| handler   | (event: [DatabaseEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseevent_interface)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class), [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Ref\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Realtime Database deletion occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[DatabaseEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseevent_interface)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class), [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Ref\>\>\>

## database.onValueDeleted()

Event handler which triggers when data is deleted in Realtime Database.

**Signature:**  

    export declare function onValueDeleted<Ref extends string>(opts: ReferenceOptions<Ref>, handler: (event: DatabaseEvent<DataSnapshot, ParamsOf<Ref>>) => any | Promise<any>): CloudFunction<DatabaseEvent<DataSnapshot, ParamsOf<Ref>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                        Type                                                                                                                                                                                                                                         |                                Description                                 |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| opts      | [ReferenceOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptions_interface)\<Ref\>                                                                                                                                                                                                                                                                                                     | Options that can be set on an individual event-handling function.          |
| handler   | (event: [DatabaseEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseevent_interface)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class), [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Ref\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Realtime Database deletion occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[DatabaseEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseevent_interface)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class), [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Ref\>\>\>

## database.onValueUpdated()

Event handler which triggers when data is updated in Realtime Database.

**Signature:**  

    export declare function onValueUpdated<Ref extends string>(ref: Ref, handler: (event: DatabaseEvent<Change<DataSnapshot>, ParamsOf<Ref>>) => any | Promise<any>): CloudFunction<DatabaseEvent<Change<DataSnapshot>, ParamsOf<Ref>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                                                                     Type                                                                                                                                                                                                                                                                                                     |                               Description                                |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| ref       | Ref                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                          |
| handler   | (event: [DatabaseEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class)\>, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Ref\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Realtime Database update occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[DatabaseEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class)\>, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Ref\>\>\>

## database.onValueUpdated()

Event handler which triggers when data is updated in Realtime Database.

**Signature:**  

    export declare function onValueUpdated<Ref extends string>(opts: ReferenceOptions<Ref>, handler: (event: DatabaseEvent<Change<DataSnapshot>, ParamsOf<Ref>>) => any | Promise<any>): CloudFunction<DatabaseEvent<Change<DataSnapshot>, ParamsOf<Ref>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                                                                     Type                                                                                                                                                                                                                                                                                                     |                               Description                                |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| opts      | [ReferenceOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptions_interface)\<Ref\>                                                                                                                                                                                                                                                                                                                                                                                                                              | Options that can be set on an individual event-handling function.        |
| handler   | (event: [DatabaseEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class)\>, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Ref\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Realtime Database update occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[DatabaseEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class)\>, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Ref\>\>\>

## database.onValueWritten()

Event handler which triggers when data is created, updated, or deleted in Realtime Database.

**Signature:**  

    export declare function onValueWritten<Ref extends string>(ref: Ref, handler: (event: DatabaseEvent<Change<DataSnapshot>, ParamsOf<Ref>>) => any | Promise<any>): CloudFunction<DatabaseEvent<Change<DataSnapshot>, ParamsOf<Ref>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                                                                     Type                                                                                                                                                                                                                                                                                                     |                                         Description                                         |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| ref       | Ref                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                             |
| handler   | (event: [DatabaseEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class)\>, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Ref\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Realtime Database create, update, or delete occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[DatabaseEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class)\>, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Ref\>\>\>

## database.onValueWritten()

Event handler which triggers when data is created, updated, or deleted in Realtime Database.

**Signature:**  

    export declare function onValueWritten<Ref extends string>(opts: ReferenceOptions<Ref>, handler: (event: DatabaseEvent<Change<DataSnapshot>, ParamsOf<Ref>>) => any | Promise<any>): CloudFunction<DatabaseEvent<Change<DataSnapshot>, ParamsOf<Ref>>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                                                                                     Type                                                                                                                                                                                                                                                                                                     |                                         Description                                         |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| opts      | [ReferenceOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptions_interface)\<Ref\>                                                                                                                                                                                                                                                                                                                                                                                                                              | Options that can be set on an individual event-handling function.                           |
| handler   | (event: [DatabaseEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class)\>, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Ref\>\>) =\> any \| Promise\<any\> | Event handler which is run every time a Realtime Database create, update, or delete occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[DatabaseEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseevent_interface)\<[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<[DataSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class)\>, [ParamsOf](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#paramsof)\<Ref\>\>\>