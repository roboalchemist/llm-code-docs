# Source: https://firebase.google.com/docs/reference/js/auth.multifactorassertion.md.txt

# MultiFactorAssertion interface

The base class for asserting ownership of a second factor.

This is used to facilitate enrollment of a second factor on an existing user or sign-in of a user who already verified the first factor.

**Signature:**  

    export interface MultiFactorAssertion 

## Properties

|                                                      Property                                                       |                                                                                         Type                                                                                         |             Description              |
|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| [factorId](https://firebase.google.com/docs/reference/js/auth.multifactorassertion.md#multifactorassertionfactorid) | (typeof [FactorIdMap](https://firebase.google.com/docs/reference/js/auth.md#factorid))\[keyof typeof [FactorIdMap](https://firebase.google.com/docs/reference/js/auth.md#factorid)\] | The identifier of the second factor. |

## MultiFactorAssertion.factorId

The identifier of the second factor.

**Signature:**  

    readonly factorId: (typeof FactorIdMap)[keyof typeof FactorIdMap];