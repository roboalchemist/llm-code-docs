# Source: https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md.txt

# FirestoreError class

An error returned by a Firestore operation.

**Signature:**  

    export declare class FirestoreError extends FirebaseError 

**Extends:** [FirebaseError](https://firebase.google.com/docs/reference/js/util.firebaseerror.md#firebaseerror_class)

## Properties

|                                                  Property                                                   | Modifiers |                                                 Type                                                 |                    Description                     |
|-------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| [code](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerrorcode)       |           | [FirestoreErrorCode](https://firebase.google.com/docs/reference/js/firestore_.md#firestoreerrorcode) | The backend error code associated with this error. |
| [message](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerrormessage) |           | string                                                                                               | A custom error description.                        |
| [stack](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerrorstack)     |           | string                                                                                               | The stack of the error.                            |

## FirestoreError.code

The backend error code associated with this error.

**Signature:**  

    readonly code: FirestoreErrorCode;

## FirestoreError.message

A custom error description.

**Signature:**  

    readonly message: string;

## FirestoreError.stack

The stack of the error.

**Signature:**  

    readonly stack?: string;