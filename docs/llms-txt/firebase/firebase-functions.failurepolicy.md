# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.failurepolicy.md.txt

# FailurePolicy interface

Configuration option for failure policy on background functions.

**Signature:**  

    export interface FailurePolicy 

## Properties

|                                                       Property                                                       |          Type           |                  Description                  |
|----------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------|
| [retry](https://firebase.google.com/docs/reference/functions/firebase-functions.failurepolicy.md#failurepolicyretry) | Record\<string, never\> | Retry configuration. Must be an empty object. |

## FailurePolicy.retry

Retry configuration. Must be an empty object.

**Signature:**  

    retry: Record<string, never>;