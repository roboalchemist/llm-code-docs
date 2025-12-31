# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updatephonemultifactorinforequest.md.txt

# UpdatePhoneMultiFactorInfoRequest interface

Interface representing a phone specific user-enrolled second factor for an `UpdateRequest`.

**Signature:**  

    export interface UpdatePhoneMultiFactorInfoRequest extends BaseUpdateMultiFactorInfoRequest 

**Extends:** [BaseUpdateMultiFactorInfoRequest](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseupdatemultifactorinforequest.md#baseupdatemultifactorinforequest_interface)

## Properties

|                                                                                  Property                                                                                  |  Type  |                       Description                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------|
| [phoneNumber](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updatephonemultifactorinforequest.md#updatephonemultifactorinforequestphonenumber) | string | The phone number associated with a phone second factor. |

## UpdatePhoneMultiFactorInfoRequest.phoneNumber

The phone number associated with a phone second factor.

**Signature:**  

    phoneNumber: string;