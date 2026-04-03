# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authuserrecord.md.txt

# identity.AuthUserRecord interface

The `UserRecord` passed to auth blocking functions from the identity platform.

**Signature:**  

    export interface AuthUserRecord 

## Properties

|                                                                                      Property                                                                                      |          Type           |                                                              Description                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [customClaims](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authuserrecord.md#identityauthuserrecordcustomclaims)                 | Record\<string, any\>   | The user's custom claims object if available, typically used to define user roles and propagated to an authenticated user's ID token. |
| [disabled](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authuserrecord.md#identityauthuserrecorddisabled)                         | boolean                 | Whether or not the user is disabled: `true` for disabled; `false` for enabled.                                                        |
| [displayName](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authuserrecord.md#identityauthuserrecorddisplayname)                   | string                  | The user's display name.                                                                                                              |
| [email](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authuserrecord.md#identityauthuserrecordemail)                               | string                  | The user's primary email, if set.                                                                                                     |
| [emailVerified](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authuserrecord.md#identityauthuserrecordemailverified)               | boolean                 | Whether or not the user's primary email is verified.                                                                                  |
| [metadata](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authuserrecord.md#identityauthuserrecordmetadata)                         | AuthUserMetadata        | Additional metadata about the user.                                                                                                   |
| [multiFactor](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authuserrecord.md#identityauthuserrecordmultifactor)                   | AuthMultiFactorSettings | The multi-factor related properties for the current user, if available.                                                               |
| [passwordHash](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authuserrecord.md#identityauthuserrecordpasswordhash)                 | string                  | The user's hashed password (base64-encoded).                                                                                          |
| [passwordSalt](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authuserrecord.md#identityauthuserrecordpasswordsalt)                 | string                  | The user's password salt (base64-encoded).                                                                                            |
| [phoneNumber](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authuserrecord.md#identityauthuserrecordphonenumber)                   | string                  | The user's primary phone number, if set.                                                                                              |
| [photoURL](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authuserrecord.md#identityauthuserrecordphotourl)                         | string                  | The user's photo URL.                                                                                                                 |
| [providerData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authuserrecord.md#identityauthuserrecordproviderdata)                 | AuthUserInfo\[\]        | An array of providers (for example, Google, Facebook) linked to the user.                                                             |
| [tenantId](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authuserrecord.md#identityauthuserrecordtenantid)                         | string \| null          | The ID of the tenant the user belongs to, if available.                                                                               |
| [tokensValidAfterTime](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authuserrecord.md#identityauthuserrecordtokensvalidaftertime) | string                  | The date the user's tokens are valid after, formatted as a UTC string.                                                                |
| [uid](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authuserrecord.md#identityauthuserrecorduid)                                   | string                  | The user's `uid`.                                                                                                                     |

## identity.AuthUserRecord.customClaims

The user's custom claims object if available, typically used to define user roles and propagated to an authenticated user's ID token.

**Signature:**  

    customClaims?: Record<string, any>;

## identity.AuthUserRecord.disabled

Whether or not the user is disabled: `true` for disabled; `false` for enabled.

**Signature:**  

    disabled: boolean;

## identity.AuthUserRecord.displayName

The user's display name.

**Signature:**  

    displayName?: string;

## identity.AuthUserRecord.email

The user's primary email, if set.

**Signature:**  

    email?: string;

## identity.AuthUserRecord.emailVerified

Whether or not the user's primary email is verified.

**Signature:**  

    emailVerified: boolean;

## identity.AuthUserRecord.metadata

Additional metadata about the user.

**Signature:**  

    metadata: AuthUserMetadata;

## identity.AuthUserRecord.multiFactor

The multi-factor related properties for the current user, if available.

**Signature:**  

    multiFactor?: AuthMultiFactorSettings;

## identity.AuthUserRecord.passwordHash

The user's hashed password (base64-encoded).

**Signature:**  

    passwordHash?: string;

## identity.AuthUserRecord.passwordSalt

The user's password salt (base64-encoded).

**Signature:**  

    passwordSalt?: string;

## identity.AuthUserRecord.phoneNumber

The user's primary phone number, if set.

**Signature:**  

    phoneNumber?: string;

## identity.AuthUserRecord.photoURL

The user's photo URL.

**Signature:**  

    photoURL?: string;

## identity.AuthUserRecord.providerData

An array of providers (for example, Google, Facebook) linked to the user.

**Signature:**  

    providerData: AuthUserInfo[];

## identity.AuthUserRecord.tenantId

The ID of the tenant the user belongs to, if available.

**Signature:**  

    tenantId?: string | null;

## identity.AuthUserRecord.tokensValidAfterTime

The date the user's tokens are valid after, formatted as a UTC string.

**Signature:**  

    tokensValidAfterTime?: string;

## identity.AuthUserRecord.uid

The user's `uid`.

**Signature:**  

    uid: string;