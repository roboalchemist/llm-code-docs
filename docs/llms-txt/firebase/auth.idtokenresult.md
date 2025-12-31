# Source: https://firebase.google.com/docs/reference/js/auth.idtokenresult.md.txt

# IdTokenResult interface

Interface representing ID token result obtained from [User.getIdTokenResult()](https://firebase.google.com/docs/reference/js/auth.user.md#usergetidtokenresult).

`IdTokenResult` contains the ID token JWT string and other helper properties for getting different data associated with the token as well as all the decoded payload claims.

Note that these claims are not to be trusted as they are parsed client side. Only server side verification can guarantee the integrity of the token claims.

**Signature:**  

    export interface IdTokenResult 

## Properties

|                                                         Property                                                          |                                                  Type                                                  |                                                        Description                                                         |
|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [authTime](https://firebase.google.com/docs/reference/js/auth.idtokenresult.md#idtokenresultauthtime)                     | string                                                                                                 | The authentication time formatted as a UTC string.                                                                         |
| [claims](https://firebase.google.com/docs/reference/js/auth.idtokenresult.md#idtokenresultclaims)                         | [ParsedToken](https://firebase.google.com/docs/reference/js/auth.parsedtoken.md#parsedtoken_interface) | The entire payload claims of the ID token including the standard reserved claims as well as the custom claims.             |
| [expirationTime](https://firebase.google.com/docs/reference/js/auth.idtokenresult.md#idtokenresultexpirationtime)         | string                                                                                                 | The ID token expiration time formatted as a UTC string.                                                                    |
| [issuedAtTime](https://firebase.google.com/docs/reference/js/auth.idtokenresult.md#idtokenresultissuedattime)             | string                                                                                                 | The ID token issuance time formatted as a UTC string.                                                                      |
| [signInProvider](https://firebase.google.com/docs/reference/js/auth.idtokenresult.md#idtokenresultsigninprovider)         | string \| null                                                                                         | The sign-in provider through which the ID token was obtained (anonymous, custom, phone, password, etc).                    |
| [signInSecondFactor](https://firebase.google.com/docs/reference/js/auth.idtokenresult.md#idtokenresultsigninsecondfactor) | string \| null                                                                                         | The type of second factor associated with this session, provided the user was multi-factor authenticated (eg. phone, etc). |
| [token](https://firebase.google.com/docs/reference/js/auth.idtokenresult.md#idtokenresulttoken)                           | string                                                                                                 | The Firebase Auth ID token JWT string.                                                                                     |

## IdTokenResult.authTime

The authentication time formatted as a UTC string.

This is the time the user authenticated (signed in) and not the time the token was refreshed.

**Signature:**  

    authTime: string;

## IdTokenResult.claims

The entire payload claims of the ID token including the standard reserved claims as well as the custom claims.

**Signature:**  

    claims: ParsedToken;

## IdTokenResult.expirationTime

The ID token expiration time formatted as a UTC string.

**Signature:**  

    expirationTime: string;

## IdTokenResult.issuedAtTime

The ID token issuance time formatted as a UTC string.

**Signature:**  

    issuedAtTime: string;

## IdTokenResult.signInProvider

The sign-in provider through which the ID token was obtained (anonymous, custom, phone, password, etc).

Note, this does not map to provider IDs.

**Signature:**  

    signInProvider: string | null;

## IdTokenResult.signInSecondFactor

The type of second factor associated with this session, provided the user was multi-factor authenticated (eg. phone, etc).

**Signature:**  

    signInSecondFactor: string | null;

## IdTokenResult.token

The Firebase Auth ID token JWT string.

**Signature:**  

    token: string;