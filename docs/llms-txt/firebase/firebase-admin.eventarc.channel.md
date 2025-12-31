# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.channel.md.txt

# Channel class

Eventarc Channel.

**Signature:**  

    export declare class Channel 

## Properties

|                                                                Property                                                                | Modifiers |                                                         Type                                                         |                                                                                   Description                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [allowedEventTypes](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.channel.md#channelallowedeventtypes) |           | string\[\]                                                                                                           | List of event types allowed by this channel for publishing. Other event types are ignored.                                                                                       |
| [eventarc](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.channel.md#channeleventarc)                   |           | [Eventarc](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.eventarc.md#eventarc_class) | The [Eventarc](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.eventarc.md#eventarc_class) service instance associated with the current `Channel`. |
| [name](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.channel.md#channelname)                           |           | string                                                                                                               | The channel name as provided during channel creation. If it was not specifed, the default channel name is returned ('locations/us-central1/channels/firebase').                  |

## Methods

|                                                           Method                                                           | Modifiers |                                                                     Description                                                                      |
|----------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [publish(events)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.channel.md#channelpublish) |           | Publishes provided events to this channel. If channel was created with `allowedEventTypes` and event type is not on that list, the event is ignored. |

## Channel.allowedEventTypes

List of event types allowed by this channel for publishing. Other event types are ignored.

**Signature:**  

    readonly allowedEventTypes?: string[];

## Channel.eventarc

The [Eventarc](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.eventarc.md#eventarc_class) service instance associated with the current `Channel`.

**Signature:**  

    get eventarc(): Eventarc;

### Example

    var app = channel.eventarc;

## Channel.name

The channel name as provided during channel creation. If it was not specifed, the default channel name is returned ('locations/us-central1/channels/firebase').

**Signature:**  

    get name(): string;

## Channel.publish()

Publishes provided events to this channel. If channel was created with `allowedEventTypes` and event type is not on that list, the event is ignored.

**Signature:**  

    publish(events: CloudEvent | CloudEvent[]): Promise<void>;

### Parameters

| Parameter |                                                                                                                                 Type                                                                                                                                 |              Description              |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| events    | [CloudEvent](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.cloudevent.md#cloudevent_interface) \| [CloudEvent](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.cloudevent.md#cloudevent_interface)\[\] | CloudEvent to publish to the channel. |

**Returns:**

Promise\<void\>