# Source: https://firebase.google.com/docs/functions/1st-gen/pubsub-events-1st.md.txt

<br />

| **Note:** The 1st-gen functionality described in this page is also supported inCloud Functions(2nd gen) with improved features and performance. For more information about 2nd gen, see the[version comparison](https://firebase.google.com/docs/functions/version-comparison). To go directly to the 2nd gen guide for this feature, see[Pub/Sub triggers](https://firebase.google.com/docs/functions/pubsub-events).

Google Cloud's[Pub/Sub](https://cloud.google.com/pubsub/docs/)is a globally distributed message bus that automatically scales as you need it. You can create a function that handlesPub/Subevents by using[`functions.pubsub`](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub).

## Trigger a pub/sub function

You can trigger a function whenever a newPub/Submessage is sent to a specific topic. You must specify thePub/Subtopic name that you want to trigger your function, and set the event within the[`onPublish()`](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.topicbuilder#pubsubtopicbuilderonpublish)event handler:

<br />

```gdscript
exports.helloPubSub = functions.pubsub.topic('topic-name').onPublish((message) => {
  // ...
});
```

<br />

## Access the pub/sub message payload

The payload for thePub/Submessage is accessible from the[`Message`](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.message)object returned to your function. For messages with JSON in thePub/Submessage body, theFirebaseSDK forCloud Functionshas a helper property to decode the message. For example, here is a message published with a simple JSON payload:  

    gcloud pubsub topics publish topic-name --message '{"name":"Xenia"}'

You can access a JSON data payload like this via the[`json`](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.message#pubsubmessagejson)property:  

```mysql
  // Get the `name` attribute of the PubSub message JSON body.
  let name = null;
  try {
    name = message.json.name;
  } catch (e) {
    functions.logger.error('PubSub message was not JSON', e);
  }https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/pubsub-helloworld/functions/index.js#L46-L52
```

Other, non-JSON payloads are contained in thePub/Submessage as base64 encoded strings in the message object. To read a message like the following, you must decode the base64 encoded string as shown:  

    gcloud pubsub topics publish topic-name --message 'MyMessage'

<br />

```gdscript
// Decode the PubSub Message body.
const messageBody = message.data ? Buffer.from(message.data, 'base64').toString() : null;https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/pubsub-helloworld/functions/index.js#L31-L32
```

<br />

## Access message attributes

Pub/Submessage can be sent with data attributes set in the publish command. For example, you could publish a message with a`name`attribute:  

    gcloud pubsub topics publish topic-name --attribute name=Xenia

You can read such attributes from[`Message.attributes`](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub#pubsubmessageattributes):

<br />

```mysql
// Get the `name` attribute of the message.
const name = message.attributes.name;https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/pubsub-helloworld/functions/index.js#L65-L66
```

<br />

You might notice that some basic data such as the message ID or the message publish time are not available in`Message.attributes`. To work around this, you can access these details in the triggering event's[`EventContext`](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext). For example:  

    exports.myFunction = functions.pubsub.topic('topic1').onPublish((message, context) => {
        console.log('The function was triggered at ', context.timestamp);
        console.log('The unique ID for the event is', context.eventId);
    });