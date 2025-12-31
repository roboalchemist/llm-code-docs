# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userproviderrequest.md.txt

# UserProviderRequest interface

User provider data to include when importing a user.

**Signature:**  

    export interface UserProviderRequest 

## Properties

|                                                                    Property                                                                    |  Type  |                                 Description                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------|
| [displayName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userproviderrequest.md#userproviderrequestdisplayname) | string | The display name for the linked provider.                                   |
| [email](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userproviderrequest.md#userproviderrequestemail)             | string | The email for the linked provider.                                          |
| [phoneNumber](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userproviderrequest.md#userproviderrequestphonenumber) | string | The phone number for the linked provider.                                   |
| [photoURL](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userproviderrequest.md#userproviderrequestphotourl)       | string | The photo URL for the linked provider.                                      |
| [providerId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userproviderrequest.md#userproviderrequestproviderid)   | string | The linked provider ID (for example, "google.com" for the Google provider). |
| [uid](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userproviderrequest.md#userproviderrequestuid)                 | string | The user identifier for the linked provider.                                |

## UserProviderRequest.displayName

The display name for the linked provider.

**Signature:**  

    displayName?: string;

## UserProviderRequest.email

The email for the linked provider.

**Signature:**  

    email?: string;

## UserProviderRequest.phoneNumber

The phone number for the linked provider.

**Signature:**  

    phoneNumber?: string;

## UserProviderRequest.photoURL

The photo URL for the linked provider.

**Signature:**  

    photoURL?: string;

## UserProviderRequest.providerId

The linked provider ID (for example, "google.com" for the Google provider).

**Signature:**  

    providerId: string;

## UserProviderRequest.uid

The user identifier for the linked provider.

**Signature:**  

    uid: string;