# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.httpsfunction.md.txt

# HttpsFunction interface

The function type for HTTPS triggers. This should be exported from your JavaScript file to define a Cloud Function.

This type is a special JavaScript function which takes Express [\`Request\`](https://expressjs.com/en/api.html#req) and [\`Response\`](https://expressjs.com/en/api.html#res) objects as its only arguments.

**Signature:**  

    export interface HttpsFunction 

## Properties

|                                                                Property                                                                |          Type           | Description |
|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-------------|
| [__endpoint](https://firebase.google.com/docs/reference/functions/firebase-functions.httpsfunction.md#httpsfunction__endpoint)         | ManifestEndpoint        |             |
| [__requiredAPIs](https://firebase.google.com/docs/reference/functions/firebase-functions.httpsfunction.md#httpsfunction__requiredapis) | ManifestRequiredAPI\[\] |             |
| [__trigger](https://firebase.google.com/docs/reference/functions/firebase-functions.httpsfunction.md#httpsfunction__trigger)           | TriggerAnnotation       |             |

## HttpsFunction.__endpoint

**Signature:**  

    __endpoint: ManifestEndpoint;

## HttpsFunction.__requiredAPIs

**Signature:**  

    __requiredAPIs?: ManifestRequiredAPI[];

## HttpsFunction.__trigger

**Signature:**  

    __trigger: TriggerAnnotation;