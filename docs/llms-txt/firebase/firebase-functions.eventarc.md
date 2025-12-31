# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.md.txt

# eventarc namespace

## Functions

|                                                                                   Function                                                                                    |                         Description                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| [onCustomEventPublished(eventType, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.md#eventarconcustomeventpublished) | Handles an Eventarc event published on the default channel. |
| [onCustomEventPublished(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.md#eventarconcustomeventpublished)      | Handles an Eventarc event.                                  |

## Interfaces

|                                                                                         Interface                                                                                          |                   Description                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| [EventarcTriggerOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptions_interface) | Options that can be set on an Eventarc trigger. |

## eventarc.onCustomEventPublished()

Handles an Eventarc event published on the default channel.

**Signature:**  

    export declare function onCustomEventPublished<T = any>(eventType: string, handler: (event: CloudEvent<T>) => any | Promise<any>): CloudFunction<CloudEvent<T>>;

### Parameters

| Parameter |                                                                                     Type                                                                                      |              Description              |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| eventType | string                                                                                                                                                                        | Type of the event to trigger on.      |
| handler   | (event: [CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<T\>) =\> any \| Promise\<any\> | A function to execute when triggered. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<T\>\>

A function that you can export and deploy.

## eventarc.onCustomEventPublished()

Handles an Eventarc event.

**Signature:**  

    export declare function onCustomEventPublished<T = any>(opts: EventarcTriggerOptions, handler: (event: CloudEvent<T>) => any | Promise<any>): CloudFunction<CloudEvent<T>>;

### Parameters

| Parameter |                                                                                            Type                                                                                            |              Description              |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| opts      | [EventarcTriggerOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptions_interface) | Options to set on this function       |
| handler   | (event: [CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<T\>) =\> any \| Promise\<any\>              | A function to execute when triggered. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<T\>\>

A function that you can export and deploy.