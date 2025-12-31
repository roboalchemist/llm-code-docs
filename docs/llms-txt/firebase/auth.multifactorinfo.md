# Source: https://firebase.google.com/docs/reference/js/auth.multifactorinfo.md.txt

# MultiFactorInfo interface

A structure containing the information of a second factor entity.

**Signature:**  

    export interface MultiFactorInfo 

## Properties

|                                                       Property                                                        |                                                                                         Type                                                                                         |                             Description                             |
|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| [displayName](https://firebase.google.com/docs/reference/js/auth.multifactorinfo.md#multifactorinfodisplayname)       | string \| null                                                                                                                                                                       | The user friendly name of the current second factor.                |
| [enrollmentTime](https://firebase.google.com/docs/reference/js/auth.multifactorinfo.md#multifactorinfoenrollmenttime) | string                                                                                                                                                                               | The enrollment date of the second factor formatted as a UTC string. |
| [factorId](https://firebase.google.com/docs/reference/js/auth.multifactorinfo.md#multifactorinfofactorid)             | (typeof [FactorIdMap](https://firebase.google.com/docs/reference/js/auth.md#factorid))\[keyof typeof [FactorIdMap](https://firebase.google.com/docs/reference/js/auth.md#factorid)\] | The identifier of the second factor.                                |
| [uid](https://firebase.google.com/docs/reference/js/auth.multifactorinfo.md#multifactorinfouid)                       | string                                                                                                                                                                               | The multi-factor enrollment ID.                                     |

## MultiFactorInfo.displayName

The user friendly name of the current second factor.

**Signature:**  

    readonly displayName?: string | null;

## MultiFactorInfo.enrollmentTime

The enrollment date of the second factor formatted as a UTC string.

**Signature:**  

    readonly enrollmentTime: string;

## MultiFactorInfo.factorId

The identifier of the second factor.

**Signature:**  

    readonly factorId: (typeof FactorIdMap)[keyof typeof FactorIdMap];

## MultiFactorInfo.uid

The multi-factor enrollment ID.

**Signature:**  

    readonly uid: string;