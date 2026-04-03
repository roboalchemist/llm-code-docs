# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.change.md.txt

# firestore.Change class

The Cloud Functions interface for events that change state, such as Realtime Database or Cloud Firestore `onWrite` and `onUpdate` events.

For more information about the format used to construct `Change` objects, see below.

**Signature:**  

    export declare class Change<T> 

## Constructors

|                                                                             Constructor                                                                             | Modifiers |                   Description                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------|
| [(constructor)(before, after)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.change.md#firestorechangeconstructor) |           | Constructs a new instance of the `Change` class |

## Properties

|                                                                 Property                                                                 | Modifiers | Type | Description |
|------------------------------------------------------------------------------------------------------------------------------------------|-----------|------|-------------|
| [after](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.change.md#firestorechangeafter)   |           | T    |             |
| [before](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.change.md#firestorechangebefore) |           | T    |             |

## Methods

|                                                                              Method                                                                               | Modifiers |                                                                   Description                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [fromJSON(json, customizer)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.change.md#firestorechangefromjson)    | `static`  | Factory method for creating a `Change` from JSON and an optional customizer function to be applied to both the `before` and the `after` fields. |
| [fromObjects(before, after)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.change.md#firestorechangefromobjects) | `static`  | Factory method for creating a `Change` from a `before` object and an `after` object.                                                            |

## firestore.Change.(constructor)

Constructs a new instance of the `Change` class

**Signature:**  

    constructor(before: T, after: T);

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| before    | T    |             |
| after     | T    |             |

## firestore.Change.after

**Signature:**  

    after: T;

## firestore.Change.before

**Signature:**  

    before: T;

## firestore.Change.fromJSON()

Factory method for creating a `Change` from JSON and an optional customizer function to be applied to both the `before` and the `after` fields.

**Signature:**  

    static fromJSON<T>(json: ChangeJson, customizer?: (x: any) => T): Change<T>;

### Parameters

| Parameter  |      Type      | Description |
|------------|----------------|-------------|
| json       | ChangeJson     |             |
| customizer | (x: any) =\> T |             |

**Returns:**

[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<T\>

## firestore.Change.fromObjects()

Factory method for creating a `Change` from a `before` object and an `after` object.

**Signature:**  

    static fromObjects<T>(before: T, after: T): Change<T>;

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| before    | T    |             |
| after     | T    |             |

**Returns:**

[Change](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.change.md#change_class)\<T\>