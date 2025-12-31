# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appchecktokenoptions.md.txt

# AppCheckTokenOptions interface

Interface representing App Check token options.

**Signature:**  

    export interface AppCheckTokenOptions 

## Properties

|                                                                     Property                                                                      |  Type  |                                                                  Description                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [ttlMillis](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appchecktokenoptions.md#appchecktokenoptionsttlmillis) | number | The length of time, in milliseconds, for which the App Check token will be valid. This value must be between 30 minutes and 7 days, inclusive. |

## AppCheckTokenOptions.ttlMillis

The length of time, in milliseconds, for which the App Check token will be valid. This value must be between 30 minutes and 7 days, inclusive.

**Signature:**  

    ttlMillis?: number;