# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updatemultifactorinforequest.md.txt

Interface representing common properties of a user enrolled second factor for an`UpdateRequest`.

<br />

**Signature:**  

    export interface UpdateMultiFactorInfoRequest 

## Properties

|                                                                                Property                                                                                |  Type  |                                                             Description                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------|
| [displayName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updatemultifactorinforequest.md#updatemultifactorinforequestdisplayname)       | string | The optional display name for an enrolled second factor.                                                                             |
| [enrollmentTime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updatemultifactorinforequest.md#updatemultifactorinforequestenrollmenttime) | string | The optional date the second factor was enrolled, formatted as a UTC string.                                                         |
| [factorId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updatemultifactorinforequest.md#updatemultifactorinforequestfactorid)             | string | The type identifier of the second factor. For SMS second factors, this is`phone`.                                                    |
| [uid](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updatemultifactorinforequest.md#updatemultifactorinforequestuid)                       | string | The ID of the enrolled second factor. This ID is unique to the user. When not provided, a new one is provisioned by the Auth server. |

## UpdateMultiFactorInfoRequest.displayName

The optional display name for an enrolled second factor.

**Signature:**  

    displayName?: string;

## UpdateMultiFactorInfoRequest.enrollmentTime

The optional date the second factor was enrolled, formatted as a UTC string.

**Signature:**  

    enrollmentTime?: string;

## UpdateMultiFactorInfoRequest.factorId

The type identifier of the second factor. For SMS second factors, this is`phone`.

**Signature:**  

    factorId: string;

## UpdateMultiFactorInfoRequest.uid

The ID of the enrolled second factor. This ID is unique to the user. When not provided, a new one is provisioned by the Auth server.

**Signature:**  

    uid?: string;