# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updaterequest.md.txt

# UpdateRequest interface

Interface representing the properties to update on the provided user.

**Signature:**  

    export interface UpdateRequest 

## Properties

|                                                                    Property                                                                    |                                                                                  Type                                                                                   |                                                                                                                                                                                                                                                                                      Description                                                                                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [disabled](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updaterequest.md#updaterequestdisabled)                   | boolean                                                                                                                                                                 | Whether or not the user is disabled: `true` for disabled; `false` for enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [displayName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updaterequest.md#updaterequestdisplayname)             | string \| null                                                                                                                                                          | The user's display name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [email](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updaterequest.md#updaterequestemail)                         | string                                                                                                                                                                  | The user's primary email.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [emailVerified](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updaterequest.md#updaterequestemailverified)         | boolean                                                                                                                                                                 | Whether or not the user's primary email is verified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [multiFactor](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updaterequest.md#updaterequestmultifactor)             | [MultiFactorUpdateSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorupdatesettings.md#multifactorupdatesettings_interface) | The user's updated multi-factor related properties.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [password](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updaterequest.md#updaterequestpassword)                   | string                                                                                                                                                                  | The user's unhashed password.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [phoneNumber](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updaterequest.md#updaterequestphonenumber)             | string \| null                                                                                                                                                          | The user's primary phone number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [photoURL](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updaterequest.md#updaterequestphotourl)                   | string \| null                                                                                                                                                          | The user's photo URL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [providersToUnlink](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updaterequest.md#updaterequestproviderstounlink) | string\[\]                                                                                                                                                              | Unlinks this user from the specified providers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [providerToLink](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updaterequest.md#updaterequestprovidertolink)       | [UserProvider](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userprovider.md#userprovider_interface)                                        | Links this user to the specified provider.Linking a provider to an existing user account does not invalidate the refresh token of that account. In other words, the existing account would continue to be able to access resources, despite not having used the newly linked provider to log in. If you wish to force the user to authenticate with this new provider, you need to (a) revoke their refresh token (see https://firebase.google.com/docs/auth/admin/manage-sessions#revoke_refresh_tokens), and (b) ensure no other authentication methods are present on this account. |

## UpdateRequest.disabled

Whether or not the user is disabled: `true` for disabled; `false` for enabled.

**Signature:**  

    disabled?: boolean;

## UpdateRequest.displayName

The user's display name.

**Signature:**  

    displayName?: string | null;

## UpdateRequest.email

The user's primary email.

**Signature:**  

    email?: string;

## UpdateRequest.emailVerified

Whether or not the user's primary email is verified.

**Signature:**  

    emailVerified?: boolean;

## UpdateRequest.multiFactor

The user's updated multi-factor related properties.

**Signature:**  

    multiFactor?: MultiFactorUpdateSettings;

## UpdateRequest.password

The user's unhashed password.

**Signature:**  

    password?: string;

## UpdateRequest.phoneNumber

The user's primary phone number.

**Signature:**  

    phoneNumber?: string | null;

## UpdateRequest.photoURL

The user's photo URL.

**Signature:**  

    photoURL?: string | null;

## UpdateRequest.providersToUnlink

Unlinks this user from the specified providers.

**Signature:**  

    providersToUnlink?: string[];

## UpdateRequest.providerToLink

Links this user to the specified provider.

Linking a provider to an existing user account does not invalidate the refresh token of that account. In other words, the existing account would continue to be able to access resources, despite not having used the newly linked provider to log in. If you wish to force the user to authenticate with this new provider, you need to (a) revoke their refresh token (see https://firebase.google.com/docs/auth/admin/manage-sessions#revoke_refresh_tokens), and (b) ensure no other authentication methods are present on this account.

**Signature:**  

    providerToLink?: UserProvider;