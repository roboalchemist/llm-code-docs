# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.blockingfunction.md.txt

# BlockingFunction interface

The function type for Auth Blocking triggers.

This type is a special JavaScript function for Auth Blocking triggers which takes Express [\`Request\`](https://expressjs.com/en/api.html#req) and [\`Response\`](https://expressjs.com/en/api.html#res) objects as its only arguments.

**Signature:**  

    export interface BlockingFunction 

## Properties

|                                                                   Property                                                                   |          Type           | Description |
|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-------------|
| [__endpoint](https://firebase.google.com/docs/reference/functions/firebase-functions.blockingfunction.md#blockingfunction__endpoint)         | ManifestEndpoint        |             |
| [__requiredAPIs](https://firebase.google.com/docs/reference/functions/firebase-functions.blockingfunction.md#blockingfunction__requiredapis) | ManifestRequiredAPI\[\] |             |
| [__trigger](https://firebase.google.com/docs/reference/functions/firebase-functions.blockingfunction.md#blockingfunction__trigger)           | TriggerAnnotation       |             |

## BlockingFunction.__endpoint

**Signature:**  

    __endpoint: ManifestEndpoint;

## BlockingFunction.__requiredAPIs

**Signature:**  

    __requiredAPIs?: ManifestRequiredAPI[];

## BlockingFunction.__trigger

**Signature:**  

    __trigger: TriggerAnnotation;