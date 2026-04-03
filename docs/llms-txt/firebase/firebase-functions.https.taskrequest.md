# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.taskrequest.md.txt

The request used to call a Task Queue function.

<br />

**Signature:**  

    export interface TaskRequest<T = any> 

## Properties

|                                                                Property                                                                |   Type   |                         Description                         |
|----------------------------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------|
| [auth](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.taskrequest.md#httpstaskrequestauth) | AuthData | The result of decoding and verifying an ODIC token.         |
| [data](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.taskrequest.md#httpstaskrequestdata) | T        | The parameters used by a client when calling this function. |

## https.TaskRequest.auth

The result of decoding and verifying an ODIC token.

**Signature:**  

    auth?: AuthData;

## https.TaskRequest.data

The parameters used by a client when calling this function.

**Signature:**  

    data: T;