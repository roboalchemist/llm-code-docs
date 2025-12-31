# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.cloudevent.md.txt

# CloudEvent interface

A CloudEvent describes event data.

**Signature:**  

    export interface CloudEvent 

## Properties

|                                                                 Property                                                                 |                                                          Type                                                           |                                                                                                      Description                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [data](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.cloudevent.md#cloudeventdata)                       | object \| string                                                                                                        | Data payload of the event. Objects are stringified with JSON and strings are be passed along as-is.                                                                                                                   |
| [datacontenttype](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.cloudevent.md#cloudeventdatacontenttype) | string                                                                                                                  | MIME type of the data being sent with the event in the `data` field. Only `application/json` and `text/plain` are currently supported. If not specified, it is automatically inferred from the type of provided data. |
| [id](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.cloudevent.md#cloudeventid)                           | string                                                                                                                  | Identifier for the event. If not provided, it is auto-populated with a UUID.                                                                                                                                          |
| [source](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.cloudevent.md#cloudeventsource)                   | string                                                                                                                  | Identifies the context in which an event happened. If not provided, the value of `EVENTARC_CLOUD_EVENT_SOURCE` environment variable is used and if that is not set, a validation error is thrown.                     |
| [specversion](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.cloudevent.md#cloudeventspecversion)         | [CloudEventVersion](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.md#cloudeventversion) | The version of the CloudEvents specification which the event uses. If not provided, is set to `1.0` -- the only supported value.                                                                                      |
| [subject](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.cloudevent.md#cloudeventsubject)                 | string                                                                                                                  | Subject (context) of the event in the context of the event producer.                                                                                                                                                  |
| [time](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.cloudevent.md#cloudeventtime)                       | string                                                                                                                  | Timestamp of the event. Must be in ISO time format. If not specified, current time (at the moment of publishing) is used.                                                                                             |
| [type](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.cloudevent.md#cloudeventtype)                       | string                                                                                                                  | Type of the event. Should be prefixed with a reverse-DNS name (`com.my-org.v1.something.happended`).                                                                                                                  |

## CloudEvent.data

Data payload of the event. Objects are stringified with JSON and strings are be passed along as-is.

**Signature:**  

    data?: object | string;

## CloudEvent.datacontenttype

MIME type of the data being sent with the event in the `data` field. Only `application/json` and `text/plain` are currently supported. If not specified, it is automatically inferred from the type of provided data.

**Signature:**  

    datacontenttype?: string;

## CloudEvent.id

Identifier for the event. If not provided, it is auto-populated with a UUID.

**Signature:**  

    id?: string;

## CloudEvent.source

Identifies the context in which an event happened. If not provided, the value of `EVENTARC_CLOUD_EVENT_SOURCE` environment variable is used and if that is not set, a validation error is thrown.

**Signature:**  

    source?: string;

## CloudEvent.specversion

The version of the CloudEvents specification which the event uses. If not provided, is set to `1.0` -- the only supported value.

**Signature:**  

    specversion?: CloudEventVersion;

## CloudEvent.subject

Subject (context) of the event in the context of the event producer.

**Signature:**  

    subject?: string;

## CloudEvent.time

Timestamp of the event. Must be in ISO time format. If not specified, current time (at the moment of publishing) is used.

**Signature:**  

    time?: string;

## CloudEvent.type

Type of the event. Should be prefixed with a reverse-DNS name (`com.my-org.v1.something.happended`).

**Signature:**  

    type: string;