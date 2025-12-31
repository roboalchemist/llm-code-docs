# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userprovider.md.txt

# UserProvider interface

Represents a user identity provider that can be associated with a Firebase user.

**Signature:**  

    export interface UserProvider 

## Properties

|                                                             Property                                                             |  Type  |                                 Description                                 |
|----------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------|
| [displayName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userprovider.md#userproviderdisplayname) | string | The display name for the linked provider.                                   |
| [email](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userprovider.md#userprovideremail)             | string | The email for the linked provider.                                          |
| [phoneNumber](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userprovider.md#userproviderphonenumber) | string | The phone number for the linked provider.                                   |
| [photoURL](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userprovider.md#userproviderphotourl)       | string | The photo URL for the linked provider.                                      |
| [providerId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userprovider.md#userproviderproviderid)   | string | The linked provider ID (for example, "google.com" for the Google provider). |
| [uid](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userprovider.md#userprovideruid)                 | string | The user identifier for the linked provider.                                |

## UserProvider.displayName

The display name for the linked provider.

**Signature:**  

    displayName?: string;

## UserProvider.email

The email for the linked provider.

**Signature:**  

    email?: string;

## UserProvider.phoneNumber

The phone number for the linked provider.

**Signature:**  

    phoneNumber?: string;

## UserProvider.photoURL

The photo URL for the linked provider.

**Signature:**  

    photoURL?: string;

## UserProvider.providerId

The linked provider ID (for example, "google.com" for the Google provider).

**Signature:**  

    providerId?: string;

## UserProvider.uid

The user identifier for the linked provider.

**Signature:**  

    uid?: string;