# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md.txt

# firestore.FirestoreEvent interface

A CloudEvent that contains a DocumentSnapshot or a Change

**Signature:**  

    export interface FirestoreEvent<T, Params = Record<string, string>> extends CloudEvent<T> 

**Extends:** [CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<T\>

## Properties

|                                                                            Property                                                                            |  Type  |                                                           Description                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------|
| [database](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreeventdatabase)   | string | The Firestore database                                                                                                          |
| [document](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreeventdocument)   | string | The document path                                                                                                               |
| [location](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreeventlocation)   | string | The location of the Firestore instance                                                                                          |
| [namespace](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreeventnamespace) | string | The Firestore namespace                                                                                                         |
| [params](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreeventparams)       | Params | An object containing the values of the path patterns. Only named capture groups will be populated - {key}, {key=\*}, {key=\*\*} |
| [project](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.firestoreevent.md#firestorefirestoreeventproject)     | string | The project identifier                                                                                                          |

## firestore.FirestoreEvent.database

The Firestore database

**Signature:**  

    database: string;

## firestore.FirestoreEvent.document

The document path

**Signature:**  

    document: string;

## firestore.FirestoreEvent.location

The location of the Firestore instance

**Signature:**  

    location: string;

## firestore.FirestoreEvent.namespace

The Firestore namespace

**Signature:**  

    namespace: string;

## firestore.FirestoreEvent.params

An object containing the values of the path patterns. Only named capture groups will be populated - {key}, {key=\*}, {key=\*\*}

**Signature:**  

    params: Params;

## firestore.FirestoreEvent.project

The project identifier

**Signature:**  

    project: string;