# Source: https://firebase.google.com/docs/reference/js/auth.additionaluserinfo.md.txt

# AdditionalUserInfo interface

A structure containing additional user information from a federated identity provider.

**Signature:**  

    export interface AdditionalUserInfo 

## Properties

|                                                      Property                                                       |               Type                |                                       Description                                        |
|---------------------------------------------------------------------------------------------------------------------|-----------------------------------|------------------------------------------------------------------------------------------|
| [isNewUser](https://firebase.google.com/docs/reference/js/auth.additionaluserinfo.md#additionaluserinfoisnewuser)   | boolean                           | Whether the user is new (created via sign-up) or existing (authenticated using sign-in). |
| [profile](https://firebase.google.com/docs/reference/js/auth.additionaluserinfo.md#additionaluserinfoprofile)       | Record\<string, unknown\> \| null | Map containing IDP-specific user data.                                                   |
| [providerId](https://firebase.google.com/docs/reference/js/auth.additionaluserinfo.md#additionaluserinfoproviderid) | string \| null                    | Identifier for the provider used to authenticate this user.                              |
| [username](https://firebase.google.com/docs/reference/js/auth.additionaluserinfo.md#additionaluserinfousername)     | string \| null                    | The username if the provider is GitHub or Twitter.                                       |

## AdditionalUserInfo.isNewUser

Whether the user is new (created via sign-up) or existing (authenticated using sign-in).

**Signature:**  

    readonly isNewUser: boolean;

## AdditionalUserInfo.profile

Map containing IDP-specific user data.

**Signature:**  

    readonly profile: Record<string, unknown> | null;

## AdditionalUserInfo.providerId

Identifier for the provider used to authenticate this user.

**Signature:**  

    readonly providerId: string | null;

## AdditionalUserInfo.username

The username if the provider is GitHub or Twitter.

**Signature:**  

    readonly username?: string | null;