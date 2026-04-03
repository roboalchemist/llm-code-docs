# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.eventarc.md.txt

# Eventarc class

Eventarc service bound to the provided app.

**Signature:**  

    export declare class Eventarc 

## Properties

|                                                   Property                                                   | Modifiers | Type |                                                                           Description                                                                           |
|--------------------------------------------------------------------------------------------------------------|-----------|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [app](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.eventarc.md#eventarcapp) |           | App  | The [App](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.app.md#app_interface) associated with the current Eventarc service instance. |

## Methods

|                                                               Method                                                                | Modifiers |                                                                                                                                                                                                                                                                 Description                                                                                                                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [channel(name, options)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.eventarc.md#eventarcchannel) |           | Creates a reference to the Eventarc channel using the provided channel resource name. The channel resource name can be either:- A fully qualified channel resource name: `projects/{project}/locations/{location}/channels/{channel-id}`- A partial resource name with location and channel ID, in which case the runtime project ID of the function is used: `locations/{location}/channels/{channel-id}`- A partial channel ID, in which case the runtime project ID of the function and `us-central1` as location is used: `{channel-id}` |
| [channel(options)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.eventarc.md#eventarcchannel)       |           | Create a reference to the default Firebase channel: `locations/us-central1/channels/firebase`                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## Eventarc.app

The [App](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.app.md#app_interface) associated with the current Eventarc service instance.

**Signature:**  

    get app(): App;

### Example

    var app = eventarc.app;

## Eventarc.channel()

Creates a reference to the Eventarc channel using the provided channel resource name. The channel resource name can be either:

- A fully qualified channel resource name: `projects/{project}/locations/{location}/channels/{channel-id}`

- A partial resource name with location and channel ID, in which case the runtime project ID of the function is used: `locations/{location}/channels/{channel-id}`

- A partial channel ID, in which case the runtime project ID of the function and `us-central1` as location is used: `{channel-id}`

**Signature:**  

    channel(name: string, options?: ChannelOptions): Channel;

### Parameters

| Parameter |                                                                    Type                                                                    |              Description              |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| name      | string                                                                                                                                     | Channel resource name.                |
| options   | [ChannelOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.channeloptions.md#channeloptions_interface) | (optional) additional channel options |

**Returns:**

[Channel](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.channel.md#channel_class)

An Eventarc channel reference for publishing events.

## Eventarc.channel()

Create a reference to the default Firebase channel: `locations/us-central1/channels/firebase`

**Signature:**  

    channel(options?: ChannelOptions): Channel;

### Parameters

| Parameter |                                                                    Type                                                                    |              Description              |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| options   | [ChannelOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.channeloptions.md#channeloptions_interface) | (optional) additional channel options |

**Returns:**

[Channel](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.channel.md#channel_class)

Eventarc channel reference for publishing events.