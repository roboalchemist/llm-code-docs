# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.messagepublisheddata.md.txt

# pubsub.MessagePublishedData interface

The interface published in a Pub/Sub publish subscription.

**Signature:**  

    export interface MessagePublishedData<T = any> 

## Properties

|                                                                                  Property                                                                                  |                                                                    Type                                                                    |          Description          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| [message](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.messagepublisheddata.md#pubsubmessagepublisheddatamessage)           | [Message](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.message.md#pubsubmessage_class)\<T\> | Google Cloud Pub/Sub message. |
| [subscription](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.messagepublisheddata.md#pubsubmessagepublisheddatasubscription) | string                                                                                                                                     | A subscription resource.      |

## pubsub.MessagePublishedData.message

Google Cloud Pub/Sub message.

**Signature:**  

    readonly message: Message<T>;

## pubsub.MessagePublishedData.subscription

A subscription resource.

**Signature:**  

    readonly subscription: string;