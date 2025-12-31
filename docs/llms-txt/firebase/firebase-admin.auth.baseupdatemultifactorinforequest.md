# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseupdatemultifactorinforequest.md.txt

# BaseUpdateMultiFactorInfoRequest interface

Interface representing common properties of a user-enrolled second factor for an `UpdateRequest`.

**Signature:**  

    export interface BaseUpdateMultiFactorInfoRequest 

## Properties

|                                                                                    Property                                                                                    |  Type  |                                                             Description                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------|
| [displayName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseupdatemultifactorinforequest.md#baseupdatemultifactorinforequestdisplayname)       | string | The optional display name for an enrolled second factor.                                                                             |
| [enrollmentTime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseupdatemultifactorinforequest.md#baseupdatemultifactorinforequestenrollmenttime) | string | The optional date the second factor was enrolled, formatted as a UTC string.                                                         |
| [factorId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseupdatemultifactorinforequest.md#baseupdatemultifactorinforequestfactorid)             | string | The type identifier of the second factor. For SMS second factors, this is `phone`.                                                   |
| [uid](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseupdatemultifactorinforequest.md#baseupdatemultifactorinforequestuid)                       | string | The ID of the enrolled second factor. This ID is unique to the user. When not provided, a new one is provisioned by the Auth server. |

## BaseUpdateMultiFactorInfoRequest.displayName

The optional display name for an enrolled second factor.

**Signature:**  

    displayName?: string;

## BaseUpdateMultiFactorInfoRequest.enrollmentTime

The optional date the second factor was enrolled, formatted as a UTC string.

**Signature:**  

    enrollmentTime?: string;

## BaseUpdateMultiFactorInfoRequest.factorId

The type identifier of the second factor. For SMS second factors, this is `phone`.

**Signature:**  

    factorId: string;

## BaseUpdateMultiFactorInfoRequest.uid

The ID of the enrolled second factor. This ID is unique to the user. When not provided, a new one is provisioned by the Auth server.

**Signature:**  

    uid?: string;