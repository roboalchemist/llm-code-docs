# Source: https://firebase.google.com/docs/reference/js/app-check.appchecktoken.md.txt

# AppCheckToken interface

The token returned from an App Check provider.

**Signature:**  

    export interface AppCheckToken 

## Properties

|                                                          Property                                                          |  Type  |                      Description                       |
|----------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------|
| [expireTimeMillis](https://firebase.google.com/docs/reference/js/app-check.appchecktoken.md#appchecktokenexpiretimemillis) | number | The local timestamp after which the token will expire. |
| [token](https://firebase.google.com/docs/reference/js/app-check.appchecktoken.md#appchecktokentoken)                       | string |                                                        |

## AppCheckToken.expireTimeMillis

The local timestamp after which the token will expire.

**Signature:**  

    readonly expireTimeMillis: number;

## AppCheckToken.token

**Signature:**  

    readonly token: string;