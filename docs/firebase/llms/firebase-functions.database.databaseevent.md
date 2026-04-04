# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md.txt

# database.DatabaseEvent interface

A CloudEvent that contains a DataSnapshot or a Change

**Signature:**  

    export interface DatabaseEvent<T, Params = Record<string, string>> extends CloudEvent<T> 

**Extends:** [CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<T\>

## Properties

|                                                                                     Property                                                                                     |  Type  |                                                           Description                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------|
| [firebaseDatabaseHost](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseeventfirebasedatabasehost) | string | The domain of the database instance                                                                                             |
| [instance](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseeventinstance)                         | string | The instance ID portion of the fully qualified resource name                                                                    |
| [location](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseeventlocation)                         | string | The location of the database                                                                                                    |
| [params](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseeventparams)                             | Params | An object containing the values of the path patterns. Only named capture groups will be populated - {key}, {key=\*}, {key=\*\*} |
| [ref](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.databaseevent.md#databasedatabaseeventref)                                   | string | The database reference path                                                                                                     |

## database.DatabaseEvent.firebaseDatabaseHost

The domain of the database instance

**Signature:**  

    firebaseDatabaseHost: string;

## database.DatabaseEvent.instance

The instance ID portion of the fully qualified resource name

**Signature:**  

    instance: string;

## database.DatabaseEvent.location

The location of the database

**Signature:**  

    location: string;

## database.DatabaseEvent.params

An object containing the values of the path patterns. Only named capture groups will be populated - {key}, {key=\*}, {key=\*\*}

**Signature:**  

    params: Params;

## database.DatabaseEvent.ref

The database reference path

**Signature:**  

    ref: string;