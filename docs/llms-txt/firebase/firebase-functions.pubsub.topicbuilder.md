# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.topicbuilder.md.txt

# pubsub.TopicBuilder class

The Google Cloud Pub/Sub topic builder.

Access via `functions.pubsub.topic()`.

**Signature:**  

    export declare class TopicBuilder 

## Constructors

|                                                                               Constructor                                                                               | Modifiers |                      Description                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------|
| [(constructor)(triggerResource, options)](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.topicbuilder.md#pubsubtopicbuilderconstructor) |           | Constructs a new instance of the `TopicBuilder` class |

## Methods

|                                                                      Method                                                                      | Modifiers |                                Description                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------|
| [onPublish(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.topicbuilder.md#pubsubtopicbuilderonpublish) |           | Event handler that fires every time a Cloud Pub/Sub message is published. |

## pubsub.TopicBuilder.(constructor)

Constructs a new instance of the `TopicBuilder` class

**Signature:**  

    constructor(triggerResource: () => string, options: DeploymentOptions);

### Parameters

|    Parameter    |                                                                     Type                                                                      | Description |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| triggerResource | () =\> string                                                                                                                                 |             |
| options         | [DeploymentOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.deploymentoptions.md#deploymentoptions_interface) |             |

## pubsub.TopicBuilder.onPublish()

Event handler that fires every time a Cloud Pub/Sub message is published.

**Signature:**  

    onPublish(handler: (message: Message, context: EventContext) => PromiseLike<any> | any): CloudFunction<Message>;

### Parameters

| Parameter |                                                                                                                                                    Type                                                                                                                                                    |                               Description                                |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| handler   | (message: [Message](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.message.md#pubsubmessage_class), context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)) =\> PromiseLike\<any\> \| any | Event handler that runs every time a Cloud Pub/Sub message is published. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[Message](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.message.md#pubsubmessage_class)\>

A function that you can export and deploy.