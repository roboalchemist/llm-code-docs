# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md.txt

# UserRecord class

Represents a user.

**Signature:**  

    export declare class UserRecord 

## Properties

|                                                                    Property                                                                    | Modifiers |                                                                       Type                                                                        |                                                                                                                                                                                                                                           Description                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [customClaims](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecordcustomclaims)                 |           | { \[key: string\]: any; }                                                                                                                         | The user's custom claims object if available, typically used to define user roles and propagated to an authenticated user's ID token. This is set via [BaseAuth.setCustomUserClaims()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthsetcustomuserclaims)                                                                                                                                                                                        |
| [disabled](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecorddisabled)                         |           | boolean                                                                                                                                           | Whether or not the user is disabled: `true` for disabled; `false` for enabled.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [displayName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecorddisplayname)                   |           | string                                                                                                                                            | The user's display name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [email](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecordemail)                               |           | string                                                                                                                                            | The user's primary email, if set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [emailVerified](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecordemailverified)               |           | boolean                                                                                                                                           | Whether or not the user's primary email is verified.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [metadata](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecordmetadata)                         |           | [UserMetadata](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.usermetadata.md#usermetadata_class)                      | Additional metadata about the user.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [multiFactor](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecordmultifactor)                   |           | [MultiFactorSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorsettings.md#multifactorsettings_class) | The multi-factor related properties for the current user, if available.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [passwordHash](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecordpasswordhash)                 |           | string                                                                                                                                            | The user's hashed password (base64-encoded), only if Firebase Auth hashing algorithm (SCRYPT) is used. If a different hashing algorithm had been used when uploading this user, as is typical when migrating from another Auth system, this will be an empty string. If no password is set, this is null. This is only available when the user is obtained from [BaseAuth.listUsers()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthlistusers). |
| [passwordSalt](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecordpasswordsalt)                 |           | string                                                                                                                                            | The user's password salt (base64-encoded), only if Firebase Auth hashing algorithm (SCRYPT) is used. If a different hashing algorithm had been used to upload this user, typical when migrating from another Auth system, this will be an empty string. If no password is set, this is null. This is only available when the user is obtained from [BaseAuth.listUsers()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthlistusers).              |
| [phoneNumber](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecordphonenumber)                   |           | string                                                                                                                                            | The user's primary phone number, if set.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [photoURL](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecordphotourl)                         |           | string                                                                                                                                            | The user's photo URL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [providerData](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecordproviderdata)                 |           | [UserInfo](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userinfo.md#userinfo_class)\[\]                              | An array of providers (for example, Google, Facebook) linked to the user.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [tenantId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecordtenantid)                         |           | string \| null                                                                                                                                    | The ID of the tenant the user belongs to, if available.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [tokensValidAfterTime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecordtokensvalidaftertime) |           | string                                                                                                                                            | The date the user's tokens are valid after, formatted as a UTC string. This is updated every time the user's refresh token are revoked either from the [BaseAuth.revokeRefreshTokens()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthrevokerefreshtokens) API or from the Firebase Auth backend on big account changes (password resets, password or email updates, etc).                                                                       |
| [uid](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecorduid)                                   |           | string                                                                                                                                            | The user's `uid`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## Methods

|                                                        Method                                                        | Modifiers |                        Description                         |
|----------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------|
| [toJSON()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord.md#userrecordtojson) |           | Returns a JSON-serializable representation of this object. |

## UserRecord.customClaims

The user's custom claims object if available, typically used to define user roles and propagated to an authenticated user's ID token. This is set via [BaseAuth.setCustomUserClaims()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthsetcustomuserclaims)

**Signature:**  

    readonly customClaims?: {
            [key: string]: any;
        };

## UserRecord.disabled

Whether or not the user is disabled: `true` for disabled; `false` for enabled.

**Signature:**  

    readonly disabled: boolean;

## UserRecord.displayName

The user's display name.

**Signature:**  

    readonly displayName?: string;

## UserRecord.email

The user's primary email, if set.

**Signature:**  

    readonly email?: string;

## UserRecord.emailVerified

Whether or not the user's primary email is verified.

**Signature:**  

    readonly emailVerified: boolean;

## UserRecord.metadata

Additional metadata about the user.

**Signature:**  

    readonly metadata: UserMetadata;

## UserRecord.multiFactor

The multi-factor related properties for the current user, if available.

**Signature:**  

    readonly multiFactor?: MultiFactorSettings;

## UserRecord.passwordHash

The user's hashed password (base64-encoded), only if Firebase Auth hashing algorithm (SCRYPT) is used. If a different hashing algorithm had been used when uploading this user, as is typical when migrating from another Auth system, this will be an empty string. If no password is set, this is null. This is only available when the user is obtained from [BaseAuth.listUsers()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthlistusers).

**Signature:**  

    readonly passwordHash?: string;

## UserRecord.passwordSalt

The user's password salt (base64-encoded), only if Firebase Auth hashing algorithm (SCRYPT) is used. If a different hashing algorithm had been used to upload this user, typical when migrating from another Auth system, this will be an empty string. If no password is set, this is null. This is only available when the user is obtained from [BaseAuth.listUsers()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthlistusers).

**Signature:**  

    readonly passwordSalt?: string;

## UserRecord.phoneNumber

The user's primary phone number, if set.

**Signature:**  

    readonly phoneNumber?: string;

## UserRecord.photoURL

The user's photo URL.

**Signature:**  

    readonly photoURL?: string;

## UserRecord.providerData

An array of providers (for example, Google, Facebook) linked to the user.

**Signature:**  

    readonly providerData: UserInfo[];

## UserRecord.tenantId

The ID of the tenant the user belongs to, if available.

**Signature:**  

    readonly tenantId?: string | null;

## UserRecord.tokensValidAfterTime

The date the user's tokens are valid after, formatted as a UTC string. This is updated every time the user's refresh token are revoked either from the [BaseAuth.revokeRefreshTokens()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthrevokerefreshtokens) API or from the Firebase Auth backend on big account changes (password resets, password or email updates, etc).

**Signature:**  

    readonly tokensValidAfterTime?: string;

## UserRecord.uid

The user's `uid`.

**Signature:**  

    readonly uid: string;

## UserRecord.toJSON()

Returns a JSON-serializable representation of this object.

**Signature:**  

    toJSON(): object;

**Returns:**

object

A JSON-serializable representation of this object.