# Source: https://firebase.google.com/docs/reference/js/auth.config.md.txt

# Config interface

Interface representing the `Auth` config.

**Signature:**  

    export interface Config 

## Properties

|                                                Property                                                 |  Type  |                                  Description                                   |
|---------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------|
| [apiHost](https://firebase.google.com/docs/reference/js/auth.config.md#configapihost)                   | string | The host at which the Firebase Auth backend is running.                        |
| [apiKey](https://firebase.google.com/docs/reference/js/auth.config.md#configapikey)                     | string | The API Key used to communicate with the Firebase Auth backend.                |
| [apiScheme](https://firebase.google.com/docs/reference/js/auth.config.md#configapischeme)               | string | The scheme used to communicate with the Firebase Auth backend.                 |
| [authDomain](https://firebase.google.com/docs/reference/js/auth.config.md#configauthdomain)             | string | The domain at which the web widgets are hosted (provided via Firebase Config). |
| [sdkClientVersion](https://firebase.google.com/docs/reference/js/auth.config.md#configsdkclientversion) | string | The SDK Client Version.                                                        |
| [tokenApiHost](https://firebase.google.com/docs/reference/js/auth.config.md#configtokenapihost)         | string | The host at which the Secure Token API is running.                             |

## Config.apiHost

The host at which the Firebase Auth backend is running.

**Signature:**  

    apiHost: string;

## Config.apiKey

The API Key used to communicate with the Firebase Auth backend.

**Signature:**  

    apiKey: string;

## Config.apiScheme

The scheme used to communicate with the Firebase Auth backend.

**Signature:**  

    apiScheme: string;

## Config.authDomain

The domain at which the web widgets are hosted (provided via Firebase Config).

**Signature:**  

    authDomain?: string;

## Config.sdkClientVersion

The SDK Client Version.

**Signature:**  

    sdkClientVersion: string;

## Config.tokenApiHost

The host at which the Secure Token API is running.

**Signature:**  

    tokenApiHost: string;