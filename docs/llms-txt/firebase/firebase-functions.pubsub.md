# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.md.txt

# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.md.txt

# pubsub namespace

## Functions

|                                                                            Function                                                                             |                     Description                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| [onMessagePublished(topic, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.md#pubsubonmessagepublished)   | Handle a message being published to a Pub/Sub topic. |
| [onMessagePublished(options, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.md#pubsubonmessagepublished) | Handle a message being published to a Pub/Sub topic. |

## Classes

|                                                                 Class                                                                 |                      Description                       |
|---------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| [Message](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.message.md#pubsubmessage_class) | Interface representing a Google Cloud Pub/Sub message. |

## Interfaces

|                                                                                    Interface                                                                                     |                            Description                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [MessagePublishedData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.messagepublisheddata.md#pubsubmessagepublisheddata_interface) | The interface published in a Pub/Sub publish subscription.         |
| [PubSubOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.pubsuboptions.md#pubsubpubsuboptions_interface)                      | PubSubOptions extend EventHandlerOptions but must include a topic. |

## pubsub.onMessagePublished()

Handle a message being published to a Pub/Sub topic.

**Signature:**  

    export declare function onMessagePublished<T = any>(topic: string, handler: (event: CloudEvent<MessagePublishedData<T>>) => any | Promise<any>): CloudFunction<CloudEvent<MessagePublishedData<T>>>;

### Parameters

| Parameter |                                                                                                                                                                               Type                                                                                                                                                                                |                     Description                      |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| topic     | string                                                                                                                                                                                                                                                                                                                                                            | The Pub/Sub topic to watch for message events.       |
| handler   | (event: [CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<[MessagePublishedData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.messagepublisheddata.md#pubsubmessagepublisheddata_interface)\<T\>\>) =\> any \| Promise\<any\> | runs every time a Cloud Pub/Sub message is published |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<[MessagePublishedData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.messagepublisheddata.md#pubsubmessagepublisheddata_interface)\<T\>\>\>

## pubsub.onMessagePublished()

Handle a message being published to a Pub/Sub topic.

**Signature:**  

    export declare function onMessagePublished<T = any>(options: PubSubOptions, handler: (event: CloudEvent<MessagePublishedData<T>>) => any | Promise<any>): CloudFunction<CloudEvent<MessagePublishedData<T>>>;

### Parameters

| Parameter |                                                                                                                                                                               Type                                                                                                                                                                                |                     Description                      |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| options   | [PubSubOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.pubsuboptions.md#pubsubpubsuboptions_interface)                                                                                                                                                                                                       | Option containing information (topic) for event      |
| handler   | (event: [CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<[MessagePublishedData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.messagepublisheddata.md#pubsubmessagepublisheddata_interface)\<T\>\>) =\> any \| Promise\<any\> | runs every time a Cloud Pub/Sub message is published |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<[MessagePublishedData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.messagepublisheddata.md#pubsubmessagepublisheddata_interface)\<T\>\>\>