# Source: https://firebase.google.com/docs/reference/js/auth.phonemultifactorinfo.md.txt

# PhoneMultiFactorInfo interface

The subclass of the [MultiFactorInfo](https://firebase.google.com/docs/reference/js/auth.multifactorinfo.md#multifactorinfo_interface) interface for phone number second factors. The `factorId` of this second factor is [FactorId](https://firebase.google.com/docs/reference/js/auth.md#factorid).PHONE.

**Signature:**  

    export interface PhoneMultiFactorInfo extends MultiFactorInfo 

**Extends:** [MultiFactorInfo](https://firebase.google.com/docs/reference/js/auth.multifactorinfo.md#multifactorinfo_interface)

## Properties

|                                                         Property                                                          |  Type  |                         Description                         |
|---------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------|
| [phoneNumber](https://firebase.google.com/docs/reference/js/auth.phonemultifactorinfo.md#phonemultifactorinfophonenumber) | string | The phone number associated with the current second factor. |

## PhoneMultiFactorInfo.phoneNumber

The phone number associated with the current second factor.

**Signature:**  

    readonly phoneNumber: string;