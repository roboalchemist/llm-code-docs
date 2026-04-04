# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.phonemultifactorinfo.md.txt

# PhoneMultiFactorInfo class

Interface representing a phone specific user-enrolled second factor.

**Signature:**  

    export declare class PhoneMultiFactorInfo extends MultiFactorInfo 

**Extends:** [MultiFactorInfo](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorinfo.md#multifactorinfo_class)

## Properties

|                                                                     Property                                                                     | Modifiers |  Type  |                       Description                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------|---------------------------------------------------------|
| [phoneNumber](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.phonemultifactorinfo.md#phonemultifactorinfophonenumber) |           | string | The phone number associated with a phone second factor. |

## Methods

|                                                                  Method                                                                  | Modifiers |                        Description                         |
|------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------|
| [toJSON()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.phonemultifactorinfo.md#phonemultifactorinfotojson) |           | Returns a JSON-serializable representation of this object. |

## PhoneMultiFactorInfo.phoneNumber

The phone number associated with a phone second factor.

**Signature:**  

    readonly phoneNumber: string;

## PhoneMultiFactorInfo.toJSON()

Returns a JSON-serializable representation of this object.

**Signature:**  

    toJSON(): object;

**Returns:**

object

A JSON-serializable representation of this object.