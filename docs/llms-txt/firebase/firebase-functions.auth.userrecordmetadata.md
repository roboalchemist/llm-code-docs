# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.auth.userrecordmetadata.md.txt

# auth.UserRecordMetadata class

Helper class to create the user metadata in a `UserRecord` object.

**Signature:**  

    export declare class UserRecordMetadata implements auth.UserMetadata 

**Implements:** auth.UserMetadata

## Constructors

|                                                                                     Constructor                                                                                     | Modifiers |                         Description                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------|
| [(constructor)(creationTime, lastSignInTime)](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.userrecordmetadata.md#authuserrecordmetadataconstructor) |           | Constructs a new instance of the `UserRecordMetadata` class |

## Properties

|                                                                         Property                                                                          | Modifiers |  Type  | Description |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------|-------------|
| [creationTime](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.userrecordmetadata.md#authuserrecordmetadatacreationtime)     |           | string |             |
| [lastSignInTime](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.userrecordmetadata.md#authuserrecordmetadatalastsignintime) |           | string |             |

## Methods

|                                                                   Method                                                                    | Modifiers |                                 Description                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------|
| [toJSON()](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.userrecordmetadata.md#authuserrecordmetadatatojson) |           | Returns a plain JavaScript object with the properties of UserRecordMetadata. |

## auth.UserRecordMetadata.(constructor)

Constructs a new instance of the `UserRecordMetadata` class

**Signature:**  

    constructor(creationTime: string, lastSignInTime: string);

### Parameters

|   Parameter    |  Type  | Description |
|----------------|--------|-------------|
| creationTime   | string |             |
| lastSignInTime | string |             |

## auth.UserRecordMetadata.creationTime

**Signature:**  

    creationTime: string;

## auth.UserRecordMetadata.lastSignInTime

**Signature:**  

    lastSignInTime: string;

## auth.UserRecordMetadata.toJSON()

Returns a plain JavaScript object with the properties of UserRecordMetadata.

**Signature:**  

    toJSON(): AuthUserMetadata;

**Returns:**

AuthUserMetadata