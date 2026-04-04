# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.auth.md.txt

# auth namespace

## Functions

|                                                                   Function                                                                   |                                   Description                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [user(userOptions)](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.md#authuser)                                | Handles events related to Firebase Auth users events.                           |
| [userRecordConstructor(wireData)](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.md#authuserrecordconstructor) | Helper function that creates a `UserRecord` class from data sent over the wire. |

## Classes

|                                                                         Class                                                                         |                                                 Description                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [HttpsError](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.httpserror.md#authhttpserror_class)                         | An explicit error that can be thrown from a handler to send an error to the client that called the function. |
| [UserBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.userbuilder.md#authuserbuilder_class)                      | Builder used to create functions for Firebase Auth user lifecycle events.                                    |
| [UserRecordMetadata](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.userrecordmetadata.md#authuserrecordmetadata_class) | Helper class to create the user metadata in a `UserRecord` object.                                           |

## Interfaces

|                                                              Interface                                                               |             Description             |
|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| [UserOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.useroptions.md#authuseroptions_interface) | Options for Auth blocking function. |

## Type Aliases

|                                                  Type Alias                                                  |                                                                                              Description                                                                                              |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [UserInfo](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.md#authuserinfo)     | `UserInfo` that is part of the `UserRecord`.                                                                                                                                                          |
| [UserRecord](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.md#authuserrecord) | The `UserRecord` passed to Cloud Functions is the same [UserRecord](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord) that is returned by the Firebase Admin SDK. |

## auth.user()

Handles events related to Firebase Auth users events.

**Signature:**  

    export declare function user(userOptions?: UserOptions): UserBuilder;

### Parameters

|  Parameter  |                                                                 Type                                                                 |      Description       |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| userOptions | [UserOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.useroptions.md#authuseroptions_interface) | Resource level options |

**Returns:**

[UserBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.userbuilder.md#authuserbuilder_class)

UserBuilder - Builder used to create functions for Firebase Auth user lifecycle events

## auth.userRecordConstructor()

Helper function that creates a `UserRecord` class from data sent over the wire.

**Signature:**  

    export declare function userRecordConstructor(wireData: Record<string, unknown>): UserRecord;

### Parameters

| Parameter |           Type            |       Description       |
|-----------|---------------------------|-------------------------|
| wireData  | Record\<string, unknown\> | data sent over the wire |

**Returns:**

[UserRecord](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.md#authuserrecord)

an instance of `UserRecord` with correct toJSON functions

## auth.UserInfo

`UserInfo` that is part of the `UserRecord`.

**Signature:**  

    export type UserInfo = auth.UserInfo;

## auth.UserRecord

The `UserRecord` passed to Cloud Functions is the same [UserRecord](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord) that is returned by the Firebase Admin SDK.

**Signature:**  

    export type UserRecord = auth.UserRecord;