# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userinfo.md.txt

# UserInfo class

Represents a user's info from a third-party identity provider such as Google or Facebook.

**Signature:**  

    export declare class UserInfo 

## Properties

|                                                         Property                                                         | Modifiers |  Type  |                                 Description                                 |
|--------------------------------------------------------------------------------------------------------------------------|-----------|--------|-----------------------------------------------------------------------------|
| [displayName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userinfo.md#userinfodisplayname) |           | string | The display name for the linked provider.                                   |
| [email](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userinfo.md#userinfoemail)             |           | string | The email for the linked provider.                                          |
| [phoneNumber](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userinfo.md#userinfophonenumber) |           | string | The phone number for the linked provider.                                   |
| [photoURL](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userinfo.md#userinfophotourl)       |           | string | The photo URL for the linked provider.                                      |
| [providerId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userinfo.md#userinfoproviderid)   |           | string | The linked provider ID (for example, "google.com" for the Google provider). |
| [uid](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userinfo.md#userinfouid)                 |           | string | The user identifier for the linked provider.                                |

## Methods

|                                                      Method                                                      | Modifiers |                        Description                         |
|------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------|
| [toJSON()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userinfo.md#userinfotojson) |           | Returns a JSON-serializable representation of this object. |

## UserInfo.displayName

The display name for the linked provider.

**Signature:**  

    readonly displayName: string;

## UserInfo.email

The email for the linked provider.

**Signature:**  

    readonly email: string;

## UserInfo.phoneNumber

The phone number for the linked provider.

**Signature:**  

    readonly phoneNumber: string;

## UserInfo.photoURL

The photo URL for the linked provider.

**Signature:**  

    readonly photoURL: string;

## UserInfo.providerId

The linked provider ID (for example, "google.com" for the Google provider).

**Signature:**  

    readonly providerId: string;

## UserInfo.uid

The user identifier for the linked provider.

**Signature:**  

    readonly uid: string;

## UserInfo.toJSON()

Returns a JSON-serializable representation of this object.

**Signature:**  

    toJSON(): object;

**Returns:**

object

A JSON-serializable representation of this object.