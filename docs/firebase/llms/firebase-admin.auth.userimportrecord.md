# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportrecord.md.txt

# UserImportRecord interface

Interface representing a user to import to Firebase Auth via the [BaseAuth.importUsers()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthimportusers) method.

**Signature:**  

    export interface UserImportRecord 

## Properties

|                                                                   Property                                                                   |                                                                                  Type                                                                                   |                                                                                                                                                                         Description                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [customClaims](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportrecord.md#userimportrecordcustomclaims)   | { \[key: string\]: any; }                                                                                                                                               | The user's custom claims object if available, typically used to define user roles and propagated to an authenticated user's ID token.                                                                                                                                                                                                                       |
| [disabled](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportrecord.md#userimportrecorddisabled)           | boolean                                                                                                                                                                 | Whether or not the user is disabled: `true` for disabled; `false` for enabled.                                                                                                                                                                                                                                                                              |
| [displayName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportrecord.md#userimportrecorddisplayname)     | string                                                                                                                                                                  | The user's display name.                                                                                                                                                                                                                                                                                                                                    |
| [email](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportrecord.md#userimportrecordemail)                 | string                                                                                                                                                                  | The user's primary email, if set.                                                                                                                                                                                                                                                                                                                           |
| [emailVerified](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportrecord.md#userimportrecordemailverified) | boolean                                                                                                                                                                 | Whether or not the user's primary email is verified.                                                                                                                                                                                                                                                                                                        |
| [metadata](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportrecord.md#userimportrecordmetadata)           | [UserMetadataRequest](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.usermetadatarequest.md#usermetadatarequest_interface)                   | Additional metadata about the user.                                                                                                                                                                                                                                                                                                                         |
| [multiFactor](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportrecord.md#userimportrecordmultifactor)     | [MultiFactorUpdateSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorupdatesettings.md#multifactorupdatesettings_interface) | The user's multi-factor related properties.                                                                                                                                                                                                                                                                                                                 |
| [passwordHash](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportrecord.md#userimportrecordpasswordhash)   | Buffer                                                                                                                                                                  | The buffer of bytes representing the user's hashed password. When a user is to be imported with a password hash, [UserImportOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportoptions.md#userimportoptions_interface) are required to be specified to identify the hashing algorithm used to generate this hash. |
| [passwordSalt](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportrecord.md#userimportrecordpasswordsalt)   | Buffer                                                                                                                                                                  | The buffer of bytes representing the user's password salt.                                                                                                                                                                                                                                                                                                  |
| [phoneNumber](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportrecord.md#userimportrecordphonenumber)     | string                                                                                                                                                                  | The user's primary phone number, if set.                                                                                                                                                                                                                                                                                                                    |
| [photoURL](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportrecord.md#userimportrecordphotourl)           | string                                                                                                                                                                  | The user's photo URL.                                                                                                                                                                                                                                                                                                                                       |
| [providerData](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportrecord.md#userimportrecordproviderdata)   | [UserProviderRequest](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userproviderrequest.md#userproviderrequest_interface)\[\]               | An array of providers (for example, Google, Facebook) linked to the user.                                                                                                                                                                                                                                                                                   |
| [tenantId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportrecord.md#userimportrecordtenantid)           | string                                                                                                                                                                  | The identifier of the tenant where user is to be imported to. When not provided in an `admin.auth.Auth` context, the user is uploaded to the default parent project. When not provided in an `admin.auth.TenantAwareAuth` context, the user is uploaded to the tenant corresponding to that `TenantAwareAuth` instance's tenant ID.                         |
| [uid](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportrecord.md#userimportrecorduid)                     | string                                                                                                                                                                  | The user's `uid`.                                                                                                                                                                                                                                                                                                                                           |

## UserImportRecord.customClaims

The user's custom claims object if available, typically used to define user roles and propagated to an authenticated user's ID token.

**Signature:**  

    customClaims?: {
            [key: string]: any;
        };

## UserImportRecord.disabled

Whether or not the user is disabled: `true` for disabled; `false` for enabled.

**Signature:**  

    disabled?: boolean;

## UserImportRecord.displayName

The user's display name.

**Signature:**  

    displayName?: string;

## UserImportRecord.email

The user's primary email, if set.

**Signature:**  

    email?: string;

## UserImportRecord.emailVerified

Whether or not the user's primary email is verified.

**Signature:**  

    emailVerified?: boolean;

## UserImportRecord.metadata

Additional metadata about the user.

**Signature:**  

    metadata?: UserMetadataRequest;

## UserImportRecord.multiFactor

The user's multi-factor related properties.

**Signature:**  

    multiFactor?: MultiFactorUpdateSettings;

## UserImportRecord.passwordHash

The buffer of bytes representing the user's hashed password. When a user is to be imported with a password hash, [UserImportOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userimportoptions.md#userimportoptions_interface) are required to be specified to identify the hashing algorithm used to generate this hash.

**Signature:**  

    passwordHash?: Buffer;

## UserImportRecord.passwordSalt

The buffer of bytes representing the user's password salt.

**Signature:**  

    passwordSalt?: Buffer;

## UserImportRecord.phoneNumber

The user's primary phone number, if set.

**Signature:**  

    phoneNumber?: string;

## UserImportRecord.photoURL

The user's photo URL.

**Signature:**  

    photoURL?: string;

## UserImportRecord.providerData

An array of providers (for example, Google, Facebook) linked to the user.

**Signature:**  

    providerData?: UserProviderRequest[];

## UserImportRecord.tenantId

The identifier of the tenant where user is to be imported to. When not provided in an `admin.auth.Auth` context, the user is uploaded to the default parent project. When not provided in an `admin.auth.TenantAwareAuth` context, the user is uploaded to the tenant corresponding to that `TenantAwareAuth` instance's tenant ID.

**Signature:**  

    tenantId?: string;

## UserImportRecord.uid

The user's `uid`.

**Signature:**  

    uid: string;