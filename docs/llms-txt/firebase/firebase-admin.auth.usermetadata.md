# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.usermetadata.md.txt

# UserMetadata class

Represents a user's metadata.

**Signature:**  

    export declare class UserMetadata 

## Properties

|                                                                 Property                                                                 | Modifiers |      Type      |                                                                                   Description                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [creationTime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.usermetadata.md#usermetadatacreationtime)       |           | string         | The date the user was created, formatted as a UTC string.                                                                                                                        |
| [lastRefreshTime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.usermetadata.md#usermetadatalastrefreshtime) |           | string \| null | The time at which the user was last active (ID token refreshed), formatted as a UTC Date string (eg 'Sat, 03 Feb 2001 04:05:06 GMT'). Returns null if the user was never active. |
| [lastSignInTime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.usermetadata.md#usermetadatalastsignintime)   |           | string         | The date the user last signed in, formatted as a UTC string.                                                                                                                     |

## Methods

|                                                          Method                                                          | Modifiers |                        Description                         |
|--------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------|
| [toJSON()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.usermetadata.md#usermetadatatojson) |           | Returns a JSON-serializable representation of this object. |

## UserMetadata.creationTime

The date the user was created, formatted as a UTC string.

**Signature:**  

    readonly creationTime: string;

## UserMetadata.lastRefreshTime

The time at which the user was last active (ID token refreshed), formatted as a UTC Date string (eg 'Sat, 03 Feb 2001 04:05:06 GMT'). Returns null if the user was never active.

**Signature:**  

    readonly lastRefreshTime?: string | null;

## UserMetadata.lastSignInTime

The date the user last signed in, formatted as a UTC string.

**Signature:**  

    readonly lastSignInTime: string;

## UserMetadata.toJSON()

Returns a JSON-serializable representation of this object.

**Signature:**  

    toJSON(): object;

**Returns:**

object

A JSON-serializable representation of this object.