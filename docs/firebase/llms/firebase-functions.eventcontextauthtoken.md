# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontextauthtoken.md.txt

# EventContextAuthToken interface

https://firebase.google.com/docs/reference/security/database#authtoken

**Signature:**  

    export interface EventContextAuthToken 

## Properties

|                                                                        Property                                                                        |                                              Type                                              | Description |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|-------------|
| [aud](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontextauthtoken.md#eventcontextauthtokenaud)                       | string                                                                                         |             |
| [auth_time](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontextauthtoken.md#eventcontextauthtokenauth_time)           | number                                                                                         |             |
| [email_verified](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontextauthtoken.md#eventcontextauthtokenemail_verified) | boolean                                                                                        |             |
| [email](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontextauthtoken.md#eventcontextauthtokenemail)                   | string                                                                                         |             |
| [exp](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontextauthtoken.md#eventcontextauthtokenexp)                       | number                                                                                         |             |
| [firebase](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontextauthtoken.md#eventcontextauthtokenfirebase)             | { identities?: { \[key: string\]: string\[\]; }; sign_in_provider?: string; tenant?: string; } |             |
| [iat](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontextauthtoken.md#eventcontextauthtokeniat)                       | number                                                                                         |             |
| [iss](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontextauthtoken.md#eventcontextauthtokeniss)                       | string                                                                                         |             |
| [name](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontextauthtoken.md#eventcontextauthtokenname)                     | string                                                                                         |             |
| [phone_number](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontextauthtoken.md#eventcontextauthtokenphone_number)     | string                                                                                         |             |
| [sub](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontextauthtoken.md#eventcontextauthtokensub)                       | string                                                                                         |             |

## EventContextAuthToken.aud

**Signature:**  

    aud: string;

## EventContextAuthToken.auth_time

**Signature:**  

    auth_time: number;

## EventContextAuthToken.email_verified

**Signature:**  

    email_verified?: boolean;

## EventContextAuthToken.email

**Signature:**  

    email?: string;

## EventContextAuthToken.exp

**Signature:**  

    exp: number;

## EventContextAuthToken.firebase

**Signature:**  

    firebase?: {
            identities?: {
                [key: string]: string[];
            };
            sign_in_provider?: string;
            tenant?: string;
        };

## EventContextAuthToken.iat

**Signature:**  

    iat: number;

## EventContextAuthToken.iss

**Signature:**  

    iss: string;

## EventContextAuthToken.name

**Signature:**  

    name?: string;

## EventContextAuthToken.phone_number

**Signature:**  

    phone_number?: string;

## EventContextAuthToken.sub

**Signature:**  

    sub: string;