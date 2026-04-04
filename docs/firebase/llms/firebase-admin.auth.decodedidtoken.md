# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.decodedidtoken.md.txt

# DecodedIdToken interface

Interface representing a decoded Firebase ID token, returned from the [BaseAuth.verifyIdToken()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthverifyidtoken) method.

Firebase ID tokens are OpenID Connect spec-compliant JSON Web Tokens (JWTs). See the \[ID Token section of the OpenID Connect spec\](http://openid.net/specs/openid-connect-core-1_0.html#IDToken) for more information about the specific properties below.

**Signature:**  

    export interface DecodedIdToken 

## Properties

|                                                                  Property                                                                  |                                                                                      Type                                                                                      |                                                                                                                                                                                                            Description                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [aud](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.decodedidtoken.md#decodedidtokenaud)                       | string                                                                                                                                                                         | The audience for which this token is intended.This value is a string equal to your Firebase project ID, the unique identifier for your Firebase project, which can be found in \[your project's settings\](https://console.firebase.google.com/project/_/settings/general/android:com.random.android).                                                                                                                            |
| [auth_time](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.decodedidtoken.md#decodedidtokenauth_time)           | number                                                                                                                                                                         | Time, in seconds since the Unix epoch, when the end-user authentication occurred.This value is not set when this particular ID token was created, but when the user initially logged in to this session. In a single session, the Firebase SDKs will refresh a user's ID tokens every hour. Each ID token will have a different \[`iat`\](#iat) value, but the same `auth_time` value.                                            |
| [email_verified](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.decodedidtoken.md#decodedidtokenemail_verified) | boolean                                                                                                                                                                        | Whether or not the email of the user to whom the ID token belongs is verified, provided the user has an email.                                                                                                                                                                                                                                                                                                                    |
| [email](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.decodedidtoken.md#decodedidtokenemail)                   | string                                                                                                                                                                         | The email of the user to whom the ID token belongs, if available.                                                                                                                                                                                                                                                                                                                                                                 |
| [exp](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.decodedidtoken.md#decodedidtokenexp)                       | number                                                                                                                                                                         | The ID token's expiration time, in seconds since the Unix epoch. That is, the time at which this ID token expires and should no longer be considered valid.The Firebase SDKs transparently refresh ID tokens every hour, issuing a new ID token with up to a one hour expiration.                                                                                                                                                 |
| [firebase](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.decodedidtoken.md#decodedidtokenfirebase)             | { identities: { \[key: string\]: any; }; sign_in_provider: string; sign_in_second_factor?: string; second_factor_identifier?: string; tenant?: string; \[key: string\]: any; } | Information about the sign in event, including which sign in provider was used and provider-specific identity details.This data is provided by the Firebase Authentication service and is a reserved claim in the ID token.                                                                                                                                                                                                       |
| [iat](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.decodedidtoken.md#decodedidtokeniat)                       | number                                                                                                                                                                         | The ID token's issued-at time, in seconds since the Unix epoch. That is, the time at which this ID token was issued and should start to be considered valid.The Firebase SDKs transparently refresh ID tokens every hour, issuing a new ID token with a new issued-at time. If you want to get the time at which the user session corresponding to the ID token initially occurred, see the \[`auth_time`\](#auth_time) property. |
| [iss](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.decodedidtoken.md#decodedidtokeniss)                       | string                                                                                                                                                                         | The issuer identifier for the issuer of the response.This value is a URL with the format `https://securetoken.google.com/<PROJECT_ID>`, where `<PROJECT_ID>` is the same project ID specified in the \[`aud`\](#aud) property.                                                                                                                                                                                                    |
| [phone_number](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.decodedidtoken.md#decodedidtokenphone_number)     | string                                                                                                                                                                         | The phone number of the user to whom the ID token belongs, if available.                                                                                                                                                                                                                                                                                                                                                          |
| [picture](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.decodedidtoken.md#decodedidtokenpicture)               | string                                                                                                                                                                         | The photo URL for the user to whom the ID token belongs, if available.                                                                                                                                                                                                                                                                                                                                                            |
| [sub](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.decodedidtoken.md#decodedidtokensub)                       | string                                                                                                                                                                         | The `uid` corresponding to the user who the ID token belonged to.As a convenience, this value is copied over to the \[`uid`\](#uid) property.                                                                                                                                                                                                                                                                                     |
| [uid](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.decodedidtoken.md#decodedidtokenuid)                       | string                                                                                                                                                                         | The `uid` corresponding to the user who the ID token belonged to.This value is not actually in the JWT token claims itself. It is added as a convenience, and is set as the value of the \[`sub`\](#sub) property.                                                                                                                                                                                                                |

## DecodedIdToken.aud

The audience for which this token is intended.

This value is a string equal to your Firebase project ID, the unique identifier for your Firebase project, which can be found in \[your project's settings\](https://console.firebase.google.com/project/_/settings/general/android:com.random.android).

**Signature:**  

    aud: string;

## DecodedIdToken.auth_time

Time, in seconds since the Unix epoch, when the end-user authentication occurred.

This value is not set when this particular ID token was created, but when the user initially logged in to this session. In a single session, the Firebase SDKs will refresh a user's ID tokens every hour. Each ID token will have a different \[`iat`\](#iat) value, but the same `auth_time` value.

**Signature:**  

    auth_time: number;

## DecodedIdToken.email_verified

Whether or not the email of the user to whom the ID token belongs is verified, provided the user has an email.

**Signature:**  

    email_verified?: boolean;

## DecodedIdToken.email

The email of the user to whom the ID token belongs, if available.

**Signature:**  

    email?: string;

## DecodedIdToken.exp

The ID token's expiration time, in seconds since the Unix epoch. That is, the time at which this ID token expires and should no longer be considered valid.

The Firebase SDKs transparently refresh ID tokens every hour, issuing a new ID token with up to a one hour expiration.

**Signature:**  

    exp: number;

## DecodedIdToken.firebase

Information about the sign in event, including which sign in provider was used and provider-specific identity details.

This data is provided by the Firebase Authentication service and is a reserved claim in the ID token.

**Signature:**  

    firebase: {
            identities: {
                [key: string]: any;
            };
            sign_in_provider: string;
            sign_in_second_factor?: string;
            second_factor_identifier?: string;
            tenant?: string;
            [key: string]: any;
        };

## DecodedIdToken.iat

The ID token's issued-at time, in seconds since the Unix epoch. That is, the time at which this ID token was issued and should start to be considered valid.

The Firebase SDKs transparently refresh ID tokens every hour, issuing a new ID token with a new issued-at time. If you want to get the time at which the user session corresponding to the ID token initially occurred, see the \[`auth_time`\](#auth_time) property.

**Signature:**  

    iat: number;

## DecodedIdToken.iss

The issuer identifier for the issuer of the response.

This value is a URL with the format `https://securetoken.google.com/<PROJECT_ID>`, where `<PROJECT_ID>` is the same project ID specified in the \[`aud`\](#aud) property.

**Signature:**  

    iss: string;

## DecodedIdToken.phone_number

The phone number of the user to whom the ID token belongs, if available.

**Signature:**  

    phone_number?: string;

## DecodedIdToken.picture

The photo URL for the user to whom the ID token belongs, if available.

**Signature:**  

    picture?: string;

## DecodedIdToken.sub

The `uid` corresponding to the user who the ID token belonged to.

As a convenience, this value is copied over to the \[`uid`\](#uid) property.

**Signature:**  

    sub: string;

## DecodedIdToken.uid

The `uid` corresponding to the user who the ID token belonged to.

This value is not actually in the JWT token claims itself. It is added as a convenience, and is set as the value of the \[`sub`\](#sub) property.

**Signature:**  

    uid: string;