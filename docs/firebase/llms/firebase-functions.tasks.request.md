# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.request.md.txt

# tasks.Request interface

The request used to call a Task Queue function.

**Signature:**  

    export interface Request<T = any> 

## Properties

|                                                            Property                                                            |   Type   |                         Description                         |
|--------------------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------|
| [auth](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.request.md#tasksrequestauth) | AuthData | The result of decoding and verifying an ODIC token.         |
| [data](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.request.md#tasksrequestdata) | T        | The parameters used by a client when calling this function. |

## tasks.Request.auth

The result of decoding and verifying an ODIC token.

**Signature:**  

    auth?: AuthData;

## tasks.Request.data

The parameters used by a client when calling this function.

**Signature:**  

    data: T;