# Source: https://firebase.google.com/docs/reference/js/auth.oauthcredentialoptions.md.txt

# OAuthCredentialOptions interface

Defines the options for initializing an [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class).

For ID tokens with nonce claim, the raw nonce has to also be provided.

**Signature:**  

    export interface OAuthCredentialOptions 

## Properties

|                                                           Property                                                            |  Type  |                                                                          Description                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [accessToken](https://firebase.google.com/docs/reference/js/auth.oauthcredentialoptions.md#oauthcredentialoptionsaccesstoken) | string | The OAuth access token used to initialize the [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class). |
| [idToken](https://firebase.google.com/docs/reference/js/auth.oauthcredentialoptions.md#oauthcredentialoptionsidtoken)         | string | The OAuth ID token used to initialize the [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class).     |
| [rawNonce](https://firebase.google.com/docs/reference/js/auth.oauthcredentialoptions.md#oauthcredentialoptionsrawnonce)       | string | The raw nonce associated with the ID token.                                                                                                                   |

## OAuthCredentialOptions.accessToken

The OAuth access token used to initialize the [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class).

**Signature:**  

    accessToken?: string;

## OAuthCredentialOptions.idToken

The OAuth ID token used to initialize the [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class).

**Signature:**  

    idToken?: string;

## OAuthCredentialOptions.rawNonce

The raw nonce associated with the ID token.

It is required when an ID token with a nonce field is provided. The SHA-256 hash of the raw nonce must match the nonce field in the ID token.

**Signature:**  

    rawNonce?: string;