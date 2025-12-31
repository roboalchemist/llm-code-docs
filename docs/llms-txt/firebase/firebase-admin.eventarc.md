# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.md.txt

# firebase-admin.eventarc package

Firebase Eventarc.

## Functions

|                                                         Function                                                         |                                                                                                                                                                           Description                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [getEventarc(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.md#geteventarc_8a40afc) | Gets the [Eventarc](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.eventarc.md#eventarc_class) service for the default app or a given app.`getEventarc()` can be called with no arguments to access the default app's `Eventarc` service or as `getEventarc(app)` to access the `Eventarc` service associated with specific app. |

## Classes

|                                                        Class                                                         |                 Description                 |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| [Channel](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.channel.md#channel_class)    | Eventarc Channel.                           |
| [Eventarc](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.eventarc.md#eventarc_class) | Eventarc service bound to the provided app. |

## Interfaces

|                                                                 Interface                                                                  |            Description             |
|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| [ChannelOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.channeloptions.md#channeloptions_interface) | Channel options interface.         |
| [CloudEvent](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.cloudevent.md#cloudevent_interface)             | A CloudEvent describes event data. |

## Type Aliases

|                                                       Type Alias                                                        |      Description      |
|-------------------------------------------------------------------------------------------------------------------------|-----------------------|
| [CloudEventVersion](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.md#cloudeventversion) | A CloudEvent version. |

## getEventarc(app)

Gets the [Eventarc](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.eventarc.md#eventarc_class) service for the default app or a given app.

`getEventarc()` can be called with no arguments to access the default app's `Eventarc` service or as `getEventarc(app)` to access the `Eventarc` service associated with specific app.

**Signature:**  

    export declare function getEventarc(app?: App): Eventarc;

### Parameters

| Parameter | Type |                                                        Description                                                        |
|-----------|------|---------------------------------------------------------------------------------------------------------------------------|
| app       | App  | Optional app whose `Eventarc` service will be returned. If not provided, the default `Eventarc` service will be returned. |

**Returns:**

[Eventarc](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.eventarc.md#eventarc_class)

The default `Eventarc` service if no app is provided or the `Eventarc` service associated with the provided app.

### Example 1

    // Get the Eventarc service for the default app
    const defaultEventarc = getEventarc();

### Example 2

    // Get the Eventarc service for a given app
    const otherEventarc = getEventarc(otherApp);

## CloudEventVersion

A CloudEvent version.

**Signature:**  

    export type CloudEventVersion = '1.0';