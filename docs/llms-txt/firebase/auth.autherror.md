# Source: https://firebase.google.com/docs/reference/js/auth.autherror.md.txt

# AuthError interface

Interface for an `Auth` error.

**Signature:**  

    export interface AuthError extends FirebaseError 

**Extends:** [FirebaseError](https://firebase.google.com/docs/reference/js/util.firebaseerror.md#firebaseerror_class)

## Properties

|                                             Property                                              |                                                       Type                                                        |              Description               |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| [customData](https://firebase.google.com/docs/reference/js/auth.autherror.md#autherrorcustomdata) | { readonly appName: string; readonly email?: string; readonly phoneNumber?: string; readonly tenantId?: string; } | Details about the Firebase Auth error. |

## AuthError.customData

Details about the Firebase Auth error.

**Signature:**  

    readonly customData: {
            readonly appName: string;
            readonly email?: string;
            readonly phoneNumber?: string;
            readonly tenantId?: string;
        };