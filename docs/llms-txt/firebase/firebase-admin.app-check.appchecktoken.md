# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appchecktoken.md.txt

# AppCheckToken interface

Interface representing an App Check token.

**Signature:**  

    export interface AppCheckToken 

## Properties

|                                                              Property                                                               |  Type  |                       Description                       |
|-------------------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------|
| [token](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appchecktoken.md#appchecktokentoken)         | string | The Firebase App Check token.                           |
| [ttlMillis](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appchecktoken.md#appchecktokenttlmillis) | number | The time-to-live duration of the token in milliseconds. |

## AppCheckToken.token

The Firebase App Check token.

**Signature:**  

    token: string;

## AppCheckToken.ttlMillis

The time-to-live duration of the token in milliseconds.

**Signature:**  

    ttlMillis: number;