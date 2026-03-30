# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.rawdataconnectevent.md.txt

# dataconnect.RawDataConnectEvent interface

**Signature:**

    export interface RawDataConnectEvent<T> extends CloudEvent<T> 

**Extends:** [CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<T\>

## Properties

| Property | Type | Description |
|---|---|---|
| [authid](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.rawdataconnectevent.md#dataconnectrawdataconnecteventauthid) | string |   |
| [authtype](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.rawdataconnectevent.md#dataconnectrawdataconnecteventauthtype) | AuthType |   |
| [connector](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.rawdataconnectevent.md#dataconnectrawdataconnecteventconnector) | string |   |
| [location](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.rawdataconnectevent.md#dataconnectrawdataconnecteventlocation) | string |   |
| [operation](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.rawdataconnectevent.md#dataconnectrawdataconnecteventoperation) | string |   |
| [project](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.rawdataconnectevent.md#dataconnectrawdataconnecteventproject) | string |   |
| [schema](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.rawdataconnectevent.md#dataconnectrawdataconnecteventschema) | string |   |
| [service](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.rawdataconnectevent.md#dataconnectrawdataconnecteventservice) | string |   |

## dataconnect.RawDataConnectEvent.authid

**Signature:**

    authid?: string;

## dataconnect.RawDataConnectEvent.authtype

**Signature:**

    authtype: AuthType;

## dataconnect.RawDataConnectEvent.connector

**Signature:**

    connector: string;

## dataconnect.RawDataConnectEvent.location

**Signature:**

    location: string;

## dataconnect.RawDataConnectEvent.operation

**Signature:**

    operation: string;

## dataconnect.RawDataConnectEvent.project

**Signature:**

    project: string;

## dataconnect.RawDataConnectEvent.schema

**Signature:**

    schema: string;

## dataconnect.RawDataConnectEvent.service

**Signature:**

    service: string;