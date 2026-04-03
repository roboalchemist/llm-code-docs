# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorupdatesettings.md.txt

# MultiFactorUpdateSettings interface

The multi-factor related user settings for update operations.

**Signature:**  

    export interface MultiFactorUpdateSettings 

## Properties

|                                                                              Property                                                                              |                                                                         Type                                                                          |                                                                                            Description                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [enrolledFactors](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorupdatesettings.md#multifactorupdatesettingsenrolledfactors) | [UpdateMultiFactorInfoRequest](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#updatemultifactorinforequest)\[\] \| null | The updated list of enrolled second factors. The provided list overwrites the user's existing list of second factors. When null is passed, all of the user's existing second factors are removed. |

## MultiFactorUpdateSettings.enrolledFactors

The updated list of enrolled second factors. The provided list overwrites the user's existing list of second factors. When null is passed, all of the user's existing second factors are removed.

**Signature:**  

    enrolledFactors: UpdateMultiFactorInfoRequest[] | null;