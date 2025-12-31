# Source: https://firebase.google.com/docs/reference/js/auth.userinfo.md.txt

# UserInfo interface

User profile information, visible only to the Firebase project's apps.

**Signature:**  

    export interface UserInfo 

## Properties

|                                             Property                                              |      Type      |                                        Description                                        |
|---------------------------------------------------------------------------------------------------|----------------|-------------------------------------------------------------------------------------------|
| [displayName](https://firebase.google.com/docs/reference/js/auth.userinfo.md#userinfodisplayname) | string \| null | The display name of the user.                                                             |
| [email](https://firebase.google.com/docs/reference/js/auth.userinfo.md#userinfoemail)             | string \| null | The email of the user.                                                                    |
| [phoneNumber](https://firebase.google.com/docs/reference/js/auth.userinfo.md#userinfophonenumber) | string \| null | The phone number normalized based on the E.164 standard (e.g. +16505550101) for the user. |
| [photoURL](https://firebase.google.com/docs/reference/js/auth.userinfo.md#userinfophotourl)       | string \| null | The profile photo URL of the user.                                                        |
| [providerId](https://firebase.google.com/docs/reference/js/auth.userinfo.md#userinfoproviderid)   | string         | The provider used to authenticate the user.                                               |
| [uid](https://firebase.google.com/docs/reference/js/auth.userinfo.md#userinfouid)                 | string         | The user's unique ID, scoped to the project.                                              |

## UserInfo.displayName

The display name of the user.

**Signature:**  

    readonly displayName: string | null;

## UserInfo.email

The email of the user.

**Signature:**  

    readonly email: string | null;

## UserInfo.phoneNumber

The phone number normalized based on the E.164 standard (e.g. +16505550101) for the user.

This is null if the user has no phone credential linked to the account.

**Signature:**  

    readonly phoneNumber: string | null;

## UserInfo.photoURL

The profile photo URL of the user.

**Signature:**  

    readonly photoURL: string | null;

## UserInfo.providerId

The provider used to authenticate the user.

**Signature:**  

    readonly providerId: string;

## UserInfo.uid

The user's unique ID, scoped to the project.

**Signature:**  

    readonly uid: string;