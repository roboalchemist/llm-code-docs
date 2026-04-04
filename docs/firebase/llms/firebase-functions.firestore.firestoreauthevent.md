# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md.txt

# firestore.FirestoreAuthEvent interface

**Signature:**  

    export interface FirestoreAuthEvent<T, Params = Record<string, string>> extends FirestoreEvent<T, Params> 

**Extends:** [FirestoreEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreevent_interface)\<T, Params\>

## Properties

|                                                                               Property                                                                               |                                                              Type                                                               |                  Description                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| [authId](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md#firestorefirestoreautheventauthid)     | string                                                                                                                          | The unique identifier for the principal        |
| [authType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreauthevent.md#firestorefirestoreautheventauthtype) | [AuthType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.md#firestoreauthtype) | The type of principal that triggered the event |

## firestore.FirestoreAuthEvent.authId

The unique identifier for the principal

**Signature:**  

    authId?: string;

## firestore.FirestoreAuthEvent.authType

The type of principal that triggered the event

**Signature:**  

    authType: AuthType;