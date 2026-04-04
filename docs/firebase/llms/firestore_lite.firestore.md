# Source: https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md.txt

# Firestore class

The Cloud Firestore service interface.

Do not call this constructor directly. Instead, use [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore).

**Signature:**  

    export declare class Firestore 

## Properties

|                                            Property                                             | Modifiers |                                                 Type                                                  |                                                                         Description                                                                          |
|-------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [app](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestoreapp)   |           | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) associated with this `Firestore` service instance. |
| [type](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestoretype) |           | 'firestore-lite' \| 'firestore'                                                                       | Whether it's a Firestore or Firestore Lite instance.                                                                                                         |

## Methods

|                                                Method                                                 | Modifiers |                               Description                                |
|-------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------|
| [toJSON()](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestoretojson) |           | Returns a JSON-serializable representation of this `Firestore` instance. |

## Firestore.app

The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) associated with this `Firestore` service instance.

**Signature:**  

    get app(): FirebaseApp;

## Firestore.type

Whether it's a Firestore or Firestore Lite instance.

**Signature:**  

    type: 'firestore-lite' | 'firestore';

## Firestore.toJSON()

Returns a JSON-serializable representation of this `Firestore` instance.

**Signature:**  

    toJSON(): object;

**Returns:**

object