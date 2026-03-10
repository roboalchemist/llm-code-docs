# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.dataconnectevent.md.txt

# dataconnect.DataConnectEvent interface

**Signature:**

    export interface DataConnectEvent<T, Params extends Record<never, string>> extends CloudEvent<T> 

**Extends:** [CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<T\>

## Properties

| Property | Type | Description |
|---|---|---|
| [authId](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.dataconnectevent.md#dataconnectdataconnecteventauthid) | string | The unique identifier for the principal |
| [authType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.dataconnectevent.md#dataconnectdataconnecteventauthtype) | AuthType | The type of principal that triggered the event |
| [location](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.dataconnectevent.md#dataconnectdataconnecteventlocation) | string | The location of the Firebase Data Connect instance |
| [params](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.dataconnectevent.md#dataconnectdataconnecteventparams) | Params | An object containing the values of the path patterns. Only named capture groups will be populated - {key}, {key=\*}, {key=\*\*}. |
| [project](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.dataconnectevent.md#dataconnectdataconnecteventproject) | string | The project identifier |

## dataconnect.DataConnectEvent.authId

The unique identifier for the principal

**Signature:**

    authId?: string;

## dataconnect.DataConnectEvent.authType

The type of principal that triggered the event

**Signature:**

    authType: AuthType;

## dataconnect.DataConnectEvent.location

The location of the Firebase Data Connect instance

**Signature:**

    location: string;

## dataconnect.DataConnectEvent.params

An object containing the values of the path patterns. Only named capture groups will be populated - {key}, {key=\*}, {key=\*\*}.

**Signature:**

    params: Params;

## dataconnect.DataConnectEvent.project

The project identifier

**Signature:**

    project: string;