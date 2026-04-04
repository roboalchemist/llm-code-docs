# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.createmultifactorinforequest.md.txt

Interface representing base properties of a user enrolled second factor for a`CreateRequest`.

<br />

**Signature:**  

    export interface CreateMultiFactorInfoRequest 

## Properties

|                                                                             Property                                                                             |  Type  |                                    Description                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------|
| [displayName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.createmultifactorinforequest.md#createmultifactorinforequestdisplayname) | string | The optional display name for an enrolled second factor.                          |
| [factorId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.createmultifactorinforequest.md#createmultifactorinforequestfactorid)       | string | The type identifier of the second factor. For SMS second factors, this is`phone`. |

## CreateMultiFactorInfoRequest.displayName

The optional display name for an enrolled second factor.

**Signature:**  

    displayName?: string;

## CreateMultiFactorInfoRequest.factorId

The type identifier of the second factor. For SMS second factors, this is`phone`.

**Signature:**  

    factorId: string;