# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.request.md.txt

# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.https.request.md.txt

# https.Request interface

An express request with the wire format representation of the request body.

**Signature:**  

    export interface Request extends express.Request 

**Extends:** express.Request

## Properties

|                                                        Property                                                         |  Type  |                     Description                     |
|-------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------|
| [rawBody](https://firebase.google.com/docs/reference/functions/firebase-functions.https.request.md#httpsrequestrawbody) | Buffer | The wire format representation of the request body. |

## https.Request.rawBody

The wire format representation of the request body.

**Signature:**  

    rawBody: Buffer;