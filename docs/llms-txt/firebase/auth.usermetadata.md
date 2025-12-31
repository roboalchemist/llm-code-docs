# Source: https://firebase.google.com/docs/reference/js/auth.usermetadata.md.txt

# UserMetadata interface

Interface representing a user's metadata.

**Signature:**  

    export interface UserMetadata 

## Properties

|                                                    Property                                                     |  Type  |          Description          |
|-----------------------------------------------------------------------------------------------------------------|--------|-------------------------------|
| [creationTime](https://firebase.google.com/docs/reference/js/auth.usermetadata.md#usermetadatacreationtime)     | string | Time the user was created.    |
| [lastSignInTime](https://firebase.google.com/docs/reference/js/auth.usermetadata.md#usermetadatalastsignintime) | string | Time the user last signed in. |

## UserMetadata.creationTime

Time the user was created.

**Signature:**  

    readonly creationTime?: string;

## UserMetadata.lastSignInTime

Time the user last signed in.

**Signature:**  

    readonly lastSignInTime?: string;