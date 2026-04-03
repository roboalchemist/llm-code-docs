# Source: https://firebase.google.com/docs/reference/js/auth.usercredential.md.txt

# UserCredential interface

A structure containing a [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface), the [OperationType](https://firebase.google.com/docs/reference/js/auth.md#operationtype), and the provider ID.

`operationType` could be [OperationType](https://firebase.google.com/docs/reference/js/auth.md#operationtype).SIGN_IN for a sign-in operation, [OperationType](https://firebase.google.com/docs/reference/js/auth.md#operationtype).LINK for a linking operation and [OperationType](https://firebase.google.com/docs/reference/js/auth.md#operationtype).REAUTHENTICATE for a reauthentication operation.

**Signature:**  

    export interface UserCredential 

## Properties

|                                                     Property                                                      |                                                                                                   Type                                                                                                   |                                       Description                                        |
|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [operationType](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredentialoperationtype) | (typeof [OperationTypeMap](https://firebase.google.com/docs/reference/js/auth.md#operationtype))\[keyof typeof [OperationTypeMap](https://firebase.google.com/docs/reference/js/auth.md#operationtype)\] | The type of operation which was used to authenticate the user (such as sign-in or link). |
| [providerId](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredentialproviderid)       | string \| null                                                                                                                                                                                           | The provider which was used to authenticate the user.                                    |
| [user](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredentialuser)                   | [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface)                                                                                                                        | The user authenticated by this credential.                                               |

## UserCredential.operationType

The type of operation which was used to authenticate the user (such as sign-in or link).

**Signature:**  

    operationType: (typeof OperationTypeMap)[keyof typeof OperationTypeMap];

## UserCredential.providerId

The provider which was used to authenticate the user.

**Signature:**  

    providerId: string | null;

## UserCredential.user

The user authenticated by this credential.

**Signature:**  

    user: User;