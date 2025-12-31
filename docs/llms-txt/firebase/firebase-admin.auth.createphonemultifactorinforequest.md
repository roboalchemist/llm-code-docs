# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.createphonemultifactorinforequest.md.txt

# CreatePhoneMultiFactorInfoRequest interface

Interface representing a phone specific user-enrolled second factor for a `CreateRequest`.

**Signature:**  

    export interface CreatePhoneMultiFactorInfoRequest extends BaseCreateMultiFactorInfoRequest 

**Extends:** [BaseCreateMultiFactorInfoRequest](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.basecreatemultifactorinforequest.md#basecreatemultifactorinforequest_interface)

## Properties

|                                                                                  Property                                                                                  |  Type  |                       Description                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------|
| [phoneNumber](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.createphonemultifactorinforequest.md#createphonemultifactorinforequestphonenumber) | string | The phone number associated with a phone second factor. |

## CreatePhoneMultiFactorInfoRequest.phoneNumber

The phone number associated with a phone second factor.

**Signature:**  

    phoneNumber: string;