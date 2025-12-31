# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.usermetadatarequest.md.txt

# UserMetadataRequest interface

User metadata to include when importing a user.

**Signature:**  

    export interface UserMetadataRequest 

## Properties

|                                                                       Property                                                                       |  Type  |                         Description                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------|
| [creationTime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.usermetadatarequest.md#usermetadatarequestcreationtime)     | string | The date the user was created, formatted as a UTC string.    |
| [lastSignInTime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.usermetadatarequest.md#usermetadatarequestlastsignintime) | string | The date the user last signed in, formatted as a UTC string. |

## UserMetadataRequest.creationTime

The date the user was created, formatted as a UTC string.

**Signature:**  

    creationTime?: string;

## UserMetadataRequest.lastSignInTime

The date the user last signed in, formatted as a UTC string.

**Signature:**  

    lastSignInTime?: string;