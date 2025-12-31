# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.database.datasnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md.txt

# database.DataSnapshot class

Interface representing a Firebase Realtime database data snapshot.

**Signature:**  

    export declare class DataSnapshot implements database.DataSnapshot 

**Implements:** database.DataSnapshot

## Constructors

|                                                                                        Constructor                                                                                        | Modifiers |                      Description                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------|
| [(constructor)(data, path, app, instance)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshotconstructor) |           | Constructs a new instance of the `DataSnapshot` class |

## Properties

|                                                                        Property                                                                        | Modifiers |        Type        |                                                                                                                                                                            Description                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [instance](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshotinstance) |           | string             |                                                                                                                                                                                                                                                                                                                                                                    |
| [key](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshotkey)           |           | string \| null     | The key (last part of the path) of the location of this `DataSnapshot`.The last token in a database location is considered its key. For example, "ada" is the key for the `/users/ada/` node. Accessing the key on any `DataSnapshot` returns the key for the location that generated it. However, accessing the key on the root URL of a database returns `null`. |
| [ref](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshotref)           |           | database.Reference | Returns a \[`Reference`\](/docs/reference/admin/node/admin.database.Reference) to the database location where the triggering write occurred. Has full read and write access.                                                                                                                                                                                       |

## Methods

|                                                                              Method                                                                               | Modifiers |                                                                                                                                                                                                                                                                           Description                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [child(childPath)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshotchild)       |           | Gets a `DataSnapshot` for the location at the specified relative path.The relative path can either be a simple child name (for example, "ada") or a deeper slash-separated path (for example, "ada/name/first").                                                                                                                                                                                                                                                                                                                                                |
| [exists()](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshotexists)              |           | Returns `true` if this `DataSnapshot` contains any data. It is slightly more efficient than using `snapshot.val() !== null`. `true` if this `DataSnapshot` contains any data; otherwise, `false`.                                                                                                                                                                                                                                                                                                                                                               |
| [exportVal()](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshotexportval)        |           | Exports the entire contents of the `DataSnapshot` as a JavaScript object. The contents of the `DataSnapshot` as a JavaScript value (Object, Array, string, number, boolean, or `null`).                                                                                                                                                                                                                                                                                                                                                                         |
| [forEach(action)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshotforeach)      |           | Enumerates the `DataSnapshot`s of the children items.Because of the way JavaScript objects work, the ordering of data in the JavaScript object returned by `val()` is not guaranteed to match the ordering on the server nor the ordering of `child_added` events. That is where `forEach()` comes in handy. It guarantees the children of a `DataSnapshot` can be iterated in their query order.If no explicit `orderBy*()` method is used, results are returned ordered by key (unless priorities are used, in which case, results are returned by priority). |
| [getPriority()](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshotgetpriority)    |           | Gets the priority value of the data in this `DataSnapshot`.As an alternative to using priority, applications can order collections by ordinary properties. See \[Sorting and filtering data\](/docs/database/web/lists-of-data#sorting_and_filtering_data). The priority value of the data.                                                                                                                                                                                                                                                                     |
| [hasChild(childPath)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshothaschild) |           | Returns `true` if the specified child path has (non-`null`) data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [hasChildren()](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshothaschildren)    |           | Returns whether or not the `DataSnapshot` has any non-`null` child properties.You can use `hasChildren()` to determine if a `DataSnapshot` has any children. If it does, you can enumerate them using `forEach()`. If it doesn't, then either this snapshot contains a primitive value (which can be retrieved with `val()`) or it is empty (in which case, `val()` returns `null`). `true` if this snapshot has any children; else `false`.                                                                                                                    |
| [numChildren()](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshotnumchildren)    |           | Returns the number of child properties of this `DataSnapshot`. Number of child properties of this `DataSnapshot`.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [toJSON()](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshottojson)              |           | Returns a JSON-serializable representation of this object. A JSON-serializable representation of this object.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [val()](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshotval)                    |           | Extracts a JavaScript value from a `DataSnapshot`.Depending on the data in a `DataSnapshot`, the `val()` method may return a scalar type (string, number, or boolean), an array, or an object. It may also return `null`, indicating that the `DataSnapshot` is empty (contains no data). The snapshot's contents as a JavaScript value (Object, Array, string, number, boolean, or `null`).                                                                                                                                                                    |

## database.DataSnapshot.(constructor)

Constructs a new instance of the `DataSnapshot` class

**Signature:**  

    constructor(data: any, path?: string, // path is undefined for the database root
        app?: App, instance?: string);

### Parameters

| Parameter |  Type  | Description |
|-----------|--------|-------------|
| data      | any    |             |
| path      | string |             |
| app       | App    |             |
| instance  | string |             |

## database.DataSnapshot.instance

**Signature:**  

    instance: string;

## database.DataSnapshot.key

The key (last part of the path) of the location of this `DataSnapshot`.

The last token in a database location is considered its key. For example, "ada" is the key for the `/users/ada/` node. Accessing the key on any `DataSnapshot` returns the key for the location that generated it. However, accessing the key on the root URL of a database returns `null`.

**Signature:**  

    get key(): string | null;

## database.DataSnapshot.ref

Returns a \[`Reference`\](/docs/reference/admin/node/admin.database.Reference) to the database location where the triggering write occurred. Has full read and write access.

**Signature:**  

    get ref(): database.Reference;

## database.DataSnapshot.child()

Gets a `DataSnapshot` for the location at the specified relative path.

The relative path can either be a simple child name (for example, "ada") or a deeper slash-separated path (for example, "ada/name/first").

**Signature:**  

    child(childPath: string): DataSnapshot;

### Parameters

| Parameter |  Type  | Description |
|-----------|--------|-------------|
| childPath | string |             |

**Returns:**

[DataSnapshot](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.datasnapshot.md#databasedatasnapshot_class)

## database.DataSnapshot.exists()

Returns `true` if this `DataSnapshot` contains any data. It is slightly more efficient than using `snapshot.val() !== null`.

`true` if this `DataSnapshot` contains any data; otherwise, `false`.

**Signature:**  

    exists(): boolean;

**Returns:**

boolean

## database.DataSnapshot.exportVal()

Exports the entire contents of the `DataSnapshot` as a JavaScript object.

The contents of the `DataSnapshot` as a JavaScript value (Object, Array, string, number, boolean, or `null`).

**Signature:**  

    exportVal(): any;

**Returns:**

any

## database.DataSnapshot.forEach()

Enumerates the `DataSnapshot`s of the children items.

Because of the way JavaScript objects work, the ordering of data in the JavaScript object returned by `val()` is not guaranteed to match the ordering on the server nor the ordering of `child_added` events. That is where `forEach()` comes in handy. It guarantees the children of a `DataSnapshot` can be iterated in their query order.

If no explicit `orderBy*()` method is used, results are returned ordered by key (unless priorities are used, in which case, results are returned by priority).

**Signature:**  

    forEach(action: (a: IteratedDataSnapshot) => boolean | void): boolean;

### Parameters

| Parameter |                     Type                      |                                                                                           Description                                                                                            |
|-----------|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| action    | (a: IteratedDataSnapshot) =\> boolean \| void | A function that is called for each child `DataSnapshot`. The callback can return `true` to cancel further enumeration. `true` if enumeration was canceled due to your callback returning `true`. |

**Returns:**

boolean

## database.DataSnapshot.getPriority()

Gets the priority value of the data in this `DataSnapshot`.

As an alternative to using priority, applications can order collections by ordinary properties. See \[Sorting and filtering data\](/docs/database/web/lists-of-data#sorting_and_filtering_data).

The priority value of the data.

**Signature:**  

    getPriority(): string | number | null;

**Returns:**

string \| number \| null

## database.DataSnapshot.hasChild()

Returns `true` if the specified child path has (non-`null`) data.

**Signature:**  

    hasChild(childPath: string): boolean;

### Parameters

| Parameter |  Type  | Description |
|-----------|--------|-------------|
| childPath | string |             |

**Returns:**

boolean

## database.DataSnapshot.hasChildren()

Returns whether or not the `DataSnapshot` has any non-`null` child properties.

You can use `hasChildren()` to determine if a `DataSnapshot` has any children. If it does, you can enumerate them using `forEach()`. If it doesn't, then either this snapshot contains a primitive value (which can be retrieved with `val()`) or it is empty (in which case, `val()` returns `null`).

`true` if this snapshot has any children; else `false`.

**Signature:**  

    hasChildren(): boolean;

**Returns:**

boolean

## database.DataSnapshot.numChildren()

Returns the number of child properties of this `DataSnapshot`.

Number of child properties of this `DataSnapshot`.

**Signature:**  

    numChildren(): number;

**Returns:**

number

## database.DataSnapshot.toJSON()

Returns a JSON-serializable representation of this object.

A JSON-serializable representation of this object.

**Signature:**  

    toJSON(): Record<string, unknown>;

**Returns:**

Record\<string, unknown\>

## database.DataSnapshot.val()

Extracts a JavaScript value from a `DataSnapshot`.

Depending on the data in a `DataSnapshot`, the `val()` method may return a scalar type (string, number, or boolean), an array, or an object. It may also return `null`, indicating that the `DataSnapshot` is empty (contains no data).

The snapshot's contents as a JavaScript value (Object, Array, string, number, boolean, or `null`).

**Signature:**  

    val(): any;

**Returns:**

any