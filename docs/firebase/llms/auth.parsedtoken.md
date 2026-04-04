# Source: https://firebase.google.com/docs/reference/js/auth.parsedtoken.md.txt

# ParsedToken interface

Interface representing a parsed ID token.

**Signature:**  

    export interface ParsedToken 

## Properties

|                                              Property                                               |                                                    Type                                                     |                                     Description                                     |
|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [auth_time](https://firebase.google.com/docs/reference/js/auth.parsedtoken.md#parsedtokenauth_time) | string                                                                                                      | Time at which authentication was performed.                                         |
| [exp](https://firebase.google.com/docs/reference/js/auth.parsedtoken.md#parsedtokenexp)             | string                                                                                                      | Expiration time of the token.                                                       |
| [firebase](https://firebase.google.com/docs/reference/js/auth.parsedtoken.md#parsedtokenfirebase)   | { 'sign_in_provider'?: string; 'sign_in_second_factor'?: string; 'identities'?: Record\<string, string\>; } | Firebase specific claims, containing the provider(s) used to authenticate the user. |
| [iat](https://firebase.google.com/docs/reference/js/auth.parsedtoken.md#parsedtokeniat)             | string                                                                                                      | Issuance time of the token.                                                         |
| [sub](https://firebase.google.com/docs/reference/js/auth.parsedtoken.md#parsedtokensub)             | string                                                                                                      | UID of the user.                                                                    |

## ParsedToken.auth_time

Time at which authentication was performed.

**Signature:**  

    'auth_time'?: string;

## ParsedToken.exp

Expiration time of the token.

**Signature:**  

    'exp'?: string;

## ParsedToken.firebase

Firebase specific claims, containing the provider(s) used to authenticate the user.

**Signature:**  

    'firebase'?: {
            'sign_in_provider'?: string;
            'sign_in_second_factor'?: string;
            'identities'?: Record<string, string>;
        };

## ParsedToken.iat

Issuance time of the token.

**Signature:**  

    'iat'?: string;

## ParsedToken.sub

UID of the user.

**Signature:**  

    'sub'?: string;