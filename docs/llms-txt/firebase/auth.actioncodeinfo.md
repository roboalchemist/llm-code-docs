# Source: https://firebase.google.com/docs/reference/js/auth.actioncodeinfo.md.txt

# ActionCodeInfo interface

A response from [checkActionCode()](https://firebase.google.com/docs/reference/js/auth.md#checkactioncode_d2ae15a).

**Signature:**  

    export interface ActionCodeInfo 

## Properties

|                                                 Property                                                  |                                                                                                               Type                                                                                                               |                      Description                      |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| [data](https://firebase.google.com/docs/reference/js/auth.actioncodeinfo.md#actioncodeinfodata)           | { email?: string \| null; multiFactorInfo?: [MultiFactorInfo](https://firebase.google.com/docs/reference/js/auth.multifactorinfo.md#multifactorinfo_interface) \| null; previousEmail?: string \| null; }                        | The data associated with the action code.             |
| [operation](https://firebase.google.com/docs/reference/js/auth.actioncodeinfo.md#actioncodeinfooperation) | (typeof [ActionCodeOperationMap](https://firebase.google.com/docs/reference/js/auth.md#actioncodeoperation))\[keyof typeof [ActionCodeOperationMap](https://firebase.google.com/docs/reference/js/auth.md#actioncodeoperation)\] | The type of operation that generated the action code. |

## ActionCodeInfo.data

The data associated with the action code.

For the [ActionCodeOperation](https://firebase.google.com/docs/reference/js/auth.md#actioncodeoperation).PASSWORD_RESET, [ActionCodeOperation](https://firebase.google.com/docs/reference/js/auth.md#actioncodeoperation).VERIFY_EMAIL, and [ActionCodeOperation](https://firebase.google.com/docs/reference/js/auth.md#actioncodeoperation).RECOVER_EMAIL actions, this object contains an email field with the address the email was sent to.

For the [ActionCodeOperation](https://firebase.google.com/docs/reference/js/auth.md#actioncodeoperation).RECOVER_EMAIL action, which allows a user to undo an email address change, this object also contains a `previousEmail` field with the user account's current email address. After the action completes, the user's email address will revert to the value in the `email` field from the value in `previousEmail` field.

For the [ActionCodeOperation](https://firebase.google.com/docs/reference/js/auth.md#actioncodeoperation).VERIFY_AND_CHANGE_EMAIL action, which allows a user to verify the email before updating it, this object contains a `previousEmail` field with the user account's email address before updating. After the action completes, the user's email address will be updated to the value in the `email` field from the value in `previousEmail` field.

For the [ActionCodeOperation](https://firebase.google.com/docs/reference/js/auth.md#actioncodeoperation).REVERT_SECOND_FACTOR_ADDITION action, which allows a user to unenroll a newly added second factor, this object contains a `multiFactorInfo` field with the information about the second factor. For phone second factor, the `multiFactorInfo` is a [MultiFactorInfo](https://firebase.google.com/docs/reference/js/auth.multifactorinfo.md#multifactorinfo_interface) object, which contains the phone number.

**Signature:**  

    data: {
            email?: string | null;
            multiFactorInfo?: MultiFactorInfo | null;
            previousEmail?: string | null;
        };

## ActionCodeInfo.operation

The type of operation that generated the action code.

**Signature:**  

    operation: (typeof ActionCodeOperationMap)[keyof typeof ActionCodeOperationMap];