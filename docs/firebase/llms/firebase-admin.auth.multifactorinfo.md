# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorinfo.md.txt

# MultiFactorInfo class

Interface representing the common properties of a user-enrolled second factor.

**Signature:**  

    export declare abstract class MultiFactorInfo 

## Properties

|                                                                   Property                                                                   | Modifiers |  Type  |                                                         Description                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------|-----------------------------------------------------------------------------------------------------------------------------|
| [displayName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorinfo.md#multifactorinfodisplayname)       |           | string | The optional display name of the enrolled second factor.                                                                    |
| [enrollmentTime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorinfo.md#multifactorinfoenrollmenttime) |           | string | The optional date the second factor was enrolled, formatted as a UTC string.                                                |
| [factorId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorinfo.md#multifactorinfofactorid)             |           | string | The type identifier of the second factor. For SMS second factors, this is `phone`. For TOTP second factors, this is `totp`. |
| [uid](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorinfo.md#multifactorinfouid)                       |           | string | The ID of the enrolled second factor. This ID is unique to the user.                                                        |

## Methods

|                                                             Method                                                             | Modifiers |                        Description                         |
|--------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------|
| [toJSON()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorinfo.md#multifactorinfotojson) |           | Returns a JSON-serializable representation of this object. |

## MultiFactorInfo.displayName

The optional display name of the enrolled second factor.

**Signature:**  

    readonly displayName?: string;

## MultiFactorInfo.enrollmentTime

The optional date the second factor was enrolled, formatted as a UTC string.

**Signature:**  

    readonly enrollmentTime?: string;

## MultiFactorInfo.factorId

The type identifier of the second factor. For SMS second factors, this is `phone`. For TOTP second factors, this is `totp`.

**Signature:**  

    readonly factorId: string;

## MultiFactorInfo.uid

The ID of the enrolled second factor. This ID is unique to the user.

**Signature:**  

    readonly uid: string;

## MultiFactorInfo.toJSON()

Returns a JSON-serializable representation of this object.

**Signature:**  

    toJSON(): object;

**Returns:**

object

A JSON-serializable representation of this object.