# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.sessioncookieoptions.md.txt

# SessionCookieOptions interface

Interface representing the session cookie options needed for the [BaseAuth.createSessionCookie()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthcreatesessioncookie) method.

**Signature:**  

    export interface SessionCookieOptions 

## Properties

|                                                                   Property                                                                   |  Type  |                                                        Description                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------|
| [expiresIn](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.sessioncookieoptions.md#sessioncookieoptionsexpiresin) | number | The session cookie custom expiration in milliseconds. The minimum allowed is 5 minutes and the maxium allowed is 2 weeks. |

## SessionCookieOptions.expiresIn

The session cookie custom expiration in milliseconds. The minimum allowed is 5 minutes and the maxium allowed is 2 weeks.

**Signature:**  

    expiresIn: number;