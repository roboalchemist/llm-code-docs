# Source: https://firebase.google.com/docs/reference/js/database.datasnapshot.md.txt

# DataSnapshot class

A `DataSnapshot` contains data from a Database location.

Any time you read data from the Database, you receive the data as a `DataSnapshot`. A `DataSnapshot` is passed to the event callbacks you attach with `on()` or `once()`. You can extract the contents of the snapshot as a JavaScript object by calling the `val()` method. Alternatively, you can traverse into the snapshot by calling `child()` to return child snapshots (which you could then call `val()` on).

A `DataSnapshot` is an efficiently generated, immutable copy of the data at a Database location. It cannot be modified and will never change (to modify data, you always call the `set()` method on a `Reference` directly).

**Signature:**  

    export declare class DataSnapshot 

## Properties

|                                                Property                                                 | Modifiers |                                                             Type                                                             |                                                                                                                                                                               Description                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [key](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshotkey)           |           | string \| null                                                                                                               | The key (last part of the path) of the location of this `DataSnapshot`.The last token in a Database location is considered its key. For example, "ada" is the key for the /users/ada/ node. Accessing the key on any `DataSnapshot` will return the key for the location that generated it. However, accessing the key on the root URL of a Database will return `null`. |
| [priority](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshotpriority) |           | string \| number \| null                                                                                                     | Gets the priority value of the data in this `DataSnapshot`.Applications need not use priority but can order collections by ordinary properties (see [Sorting and filtering data](https://firebase.google.com/docs/database/web/lists-of-data#sorting_and_filtering_data) ).                                                                                              |
| [ref](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshotref)           |           | [DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface) | The location of this DataSnapshot.                                                                                                                                                                                                                                                                                                                                       |
| [size](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshotsize)         |           | number                                                                                                                       | Returns the number of child properties of this `DataSnapshot`.                                                                                                                                                                                                                                                                                                           |

## Methods

|                                                     Method                                                      | Modifiers |                                                                                                                                                                                                                                                                                  Description                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [child(path)](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshotchild)         |           | Gets another `DataSnapshot` for the location at the specified relative path.Passing a relative path to the `child()` method of a DataSnapshot returns another `DataSnapshot` for the location at the specified relative path. The relative path can either be a simple child name (for example, "ada") or a deeper, slash-separated path (for example, "ada/name/first"). If the child location has no data, an empty `DataSnapshot` (that is, a `DataSnapshot` whose value is `null`) is returned.                                                                            |
| [exists()](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshotexists)           |           | Returns true if this `DataSnapshot` contains any data. It is slightly more efficient than using `snapshot.val() !== null`.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [exportVal()](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshotexportval)     |           | Exports the entire contents of the DataSnapshot as a JavaScript object.The `exportVal()` method is similar to `val()`, except priority information is included (if available), making it suitable for backing up your data.                                                                                                                                                                                                                                                                                                                                                    |
| [forEach(action)](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshotforeach)   |           | Enumerates the top-level children in the `IteratedDataSnapshot`.Because of the way JavaScript objects work, the ordering of data in the JavaScript object returned by `val()` is not guaranteed to match the ordering on the server nor the ordering of `onChildAdded()` events. That is where `forEach()` comes in handy. It guarantees the children of a `DataSnapshot` will be iterated in their query order.If no explicit `orderBy*()` method is used, results are returned ordered by key (unless priorities are used, in which case, results are returned by priority). |
| [hasChild(path)](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshothaschild)   |           | Returns true if the specified child path has (non-null) data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [hasChildren()](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshothaschildren) |           | Returns whether or not the `DataSnapshot` has any non-`null` child properties.You can use `hasChildren()` to determine if a `DataSnapshot` has any children. If it does, you can enumerate them using `forEach()`. If it doesn't, then either this snapshot contains a primitive value (which can be retrieved with `val()`) or it is empty (in which case, `val()` will return `null`).                                                                                                                                                                                       |
| [toJSON()](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshottojson)           |           | Returns a JSON-serializable representation of this object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [val()](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshotval)                 |           | Extracts a JavaScript value from a `DataSnapshot`.Depending on the data in a `DataSnapshot`, the `val()` method may return a scalar type (string, number, or boolean), an array, or an object. It may also return null, indicating that the `DataSnapshot` is empty (contains no data).                                                                                                                                                                                                                                                                                        |

## DataSnapshot.key

The key (last part of the path) of the location of this `DataSnapshot`.

The last token in a Database location is considered its key. For example, "ada" is the key for the /users/ada/ node. Accessing the key on any `DataSnapshot` will return the key for the location that generated it. However, accessing the key on the root URL of a Database will return `null`.

**Signature:**  

    get key(): string | null;

## DataSnapshot.priority

Gets the priority value of the data in this `DataSnapshot`.

Applications need not use priority but can order collections by ordinary properties (see [Sorting and filtering data](https://firebase.google.com/docs/database/web/lists-of-data#sorting_and_filtering_data) ).

**Signature:**  

    get priority(): string | number | null;

## DataSnapshot.ref

The location of this DataSnapshot.

**Signature:**  

    readonly ref: DatabaseReference;

## DataSnapshot.size

Returns the number of child properties of this `DataSnapshot`.

**Signature:**  

    get size(): number;

## DataSnapshot.child()

Gets another `DataSnapshot` for the location at the specified relative path.

Passing a relative path to the `child()` method of a DataSnapshot returns another `DataSnapshot` for the location at the specified relative path. The relative path can either be a simple child name (for example, "ada") or a deeper, slash-separated path (for example, "ada/name/first"). If the child location has no data, an empty `DataSnapshot` (that is, a `DataSnapshot` whose value is `null`) is returned.

**Signature:**  

    child(path: string): DataSnapshot;

#### Parameters

| Parameter |  Type  |                  Description                   |
|-----------|--------|------------------------------------------------|
| path      | string | A relative path to the location of child data. |

**Returns:**

[DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class)

## DataSnapshot.exists()

Returns true if this `DataSnapshot` contains any data. It is slightly more efficient than using `snapshot.val() !== null`.

**Signature:**  

    exists(): boolean;

**Returns:**

boolean

## DataSnapshot.exportVal()

Exports the entire contents of the DataSnapshot as a JavaScript object.

The `exportVal()` method is similar to `val()`, except priority information is included (if available), making it suitable for backing up your data.

**Signature:**  

    exportVal(): any;

**Returns:**

any

The DataSnapshot's contents as a JavaScript value (Object, Array, string, number, boolean, or `null`).

## DataSnapshot.forEach()

Enumerates the top-level children in the `IteratedDataSnapshot`.

Because of the way JavaScript objects work, the ordering of data in the JavaScript object returned by `val()` is not guaranteed to match the ordering on the server nor the ordering of `onChildAdded()` events. That is where `forEach()` comes in handy. It guarantees the children of a `DataSnapshot` will be iterated in their query order.

If no explicit `orderBy*()` method is used, results are returned ordered by key (unless priorities are used, in which case, results are returned by priority).

**Signature:**  

    forEach(action: (child: IteratedDataSnapshot) => boolean | void): boolean;

#### Parameters

| Parameter |                                                                                Type                                                                                |                                                       Description                                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| action    | (child: [IteratedDataSnapshot](https://firebase.google.com/docs/reference/js/database.iterateddatasnapshot.md#iterateddatasnapshot_interface)) =\> boolean \| void | A function that will be called for each child DataSnapshot. The callback can return true to cancel further enumeration. |

**Returns:**

boolean

true if enumeration was canceled due to your callback returning true.

## DataSnapshot.hasChild()

Returns true if the specified child path has (non-null) data.

**Signature:**  

    hasChild(path: string): boolean;

#### Parameters

| Parameter |  Type  |                      Description                      |
|-----------|--------|-------------------------------------------------------|
| path      | string | A relative path to the location of a potential child. |

**Returns:**

boolean

`true` if data exists at the specified child path; else `false`.

## DataSnapshot.hasChildren()

Returns whether or not the `DataSnapshot` has any non-`null` child properties.

You can use `hasChildren()` to determine if a `DataSnapshot` has any children. If it does, you can enumerate them using `forEach()`. If it doesn't, then either this snapshot contains a primitive value (which can be retrieved with `val()`) or it is empty (in which case, `val()` will return `null`).

**Signature:**  

    hasChildren(): boolean;

**Returns:**

boolean

true if this snapshot has any children; else false.

## DataSnapshot.toJSON()

Returns a JSON-serializable representation of this object.

**Signature:**  

    toJSON(): object | null;

**Returns:**

object \| null

## DataSnapshot.val()

Extracts a JavaScript value from a `DataSnapshot`.

Depending on the data in a `DataSnapshot`, the `val()` method may return a scalar type (string, number, or boolean), an array, or an object. It may also return null, indicating that the `DataSnapshot` is empty (contains no data).

**Signature:**  

    val(): any;

**Returns:**

any

The DataSnapshot's contents as a JavaScript value (Object, Array, string, number, boolean, or `null`).