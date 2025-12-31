# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.authdata.md.txt

Metadata about the authorization used to invoke a function.

**Signature:**  

    export interface AuthData 

## Properties

|                                                                 Property                                                                 |      Type      | Description |
|------------------------------------------------------------------------------------------------------------------------------------------|----------------|-------------|
| [rawToken](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.authdata.md#tasksauthdatarawtoken) | string         |             |
| [token](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.authdata.md#tasksauthdatatoken)       | DecodedIdToken |             |
| [uid](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.authdata.md#tasksauthdatauid)           | string         |             |

## tasks.AuthData.rawToken

**Signature:**  

    rawToken: string;

## tasks.AuthData.token

**Signature:**  

    token: DecodedIdToken;

## tasks.AuthData.uid

**Signature:**  

    uid: string;