# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md.txt

# CloudEvent interface

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

A `CloudEventBase` is the base of a cross-platform format for encoding a serverless event. For more information, see https://github.com/cloudevents/spec.

**Signature:**  

    export interface CloudEvent<T> 

## Properties

|                                                                Property                                                                 |  Type  |                                Description                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------|
| [data](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudeventdata)               | T      | ***(BETA)*** Information about this specific event.                        |
| [id](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudeventid)                   | string | ***(BETA)*** A globally unique ID for this event.                          |
| [source](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudeventsource)           | string | ***(BETA)*** The resource that published this event.                       |
| [specversion](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudeventspecversion) | "1.0"  | ***(BETA)*** Version of the CloudEvents spec for this event.               |
| [subject](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudeventsubject)         | string | ***(BETA)*** The resource, provided by source, that this event relates to. |
| [time](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudeventtime)               | string | ***(BETA)*** When this event occurred.                                     |
| [type](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudeventtype)               | string | ***(BETA)*** The type of event that this represents.                       |

## CloudEvent.data

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Information about this specific event.

**Signature:**  

    data: T;

## CloudEvent.id

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

A globally unique ID for this event.

**Signature:**  

    id: string;

## CloudEvent.source

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The resource that published this event.

**Signature:**  

    source: string;

## CloudEvent.specversion

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Version of the CloudEvents spec for this event.

**Signature:**  

    readonly specversion: "1.0";

## CloudEvent.subject

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The resource, provided by source, that this event relates to.

**Signature:**  

    subject?: string;

## CloudEvent.time

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

When this event occurred.

**Signature:**  

    time: string;

## CloudEvent.type

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The type of event that this represents.

**Signature:**  

    type: string;