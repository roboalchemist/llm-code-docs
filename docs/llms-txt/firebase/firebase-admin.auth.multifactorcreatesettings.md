# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorcreatesettings.md.txt

# MultiFactorCreateSettings interface

The multi-factor related user settings for create operations.

**Signature:**  

    export interface MultiFactorCreateSettings 

## Properties

|                                                                              Property                                                                              |                                                                     Type                                                                      |                     Description                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| [enrolledFactors](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorcreatesettings.md#multifactorcreatesettingsenrolledfactors) | [CreateMultiFactorInfoRequest](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#createmultifactorinforequest)\[\] | The created user's list of enrolled second factors. |

## MultiFactorCreateSettings.enrolledFactors

The created user's list of enrolled second factors.

**Signature:**  

    enrolledFactors: CreateMultiFactorInfoRequest[];