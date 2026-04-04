# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.basecreatemultifactorinforequest.md.txt

# BaseCreateMultiFactorInfoRequest interface

Interface representing base properties of a user-enrolled second factor for a `CreateRequest`.

**Signature:**  

    export interface BaseCreateMultiFactorInfoRequest 

## Properties

|                                                                                 Property                                                                                 |  Type  |                                    Description                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------|
| [displayName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.basecreatemultifactorinforequest.md#basecreatemultifactorinforequestdisplayname) | string | The optional display name for an enrolled second factor.                           |
| [factorId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.basecreatemultifactorinforequest.md#basecreatemultifactorinforequestfactorid)       | string | The type identifier of the second factor. For SMS second factors, this is `phone`. |

## BaseCreateMultiFactorInfoRequest.displayName

The optional display name for an enrolled second factor.

**Signature:**  

    displayName?: string;

## BaseCreateMultiFactorInfoRequest.factorId

The type identifier of the second factor. For SMS second factors, this is `phone`.

**Signature:**  

    factorId: string;