# Source: https://firebase.google.com/docs/functions/1st-gen/pubsub-events-1st.md.txt

> [!NOTE]
> **Note:** The 1st-gen functionality described in this page is also supported in Cloud Functions (2nd gen) with improved features and performance. For more information about 2nd gen, see the [version comparison](https://firebase.google.com/docs/functions/version-comparison). To go directly to the 2nd gen guide for this feature, see [Pub/Sub triggers](https://firebase.google.com/docs/functions/pubsub-events).

Google Cloud's [Pub/Sub](https://cloud.google.com/pubsub/docs/) is a
globally distributed message bus that automatically scales as you need it. You
can create a function that handles Pub/Sub events by using
[`functions.pubsub`](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub).

## Trigger a pub/sub function

You can trigger a function whenever a new Pub/Sub message is sent
to a specific topic. You must specify the Pub/Sub topic name that
you want to trigger your function, and set the event within the
[`onPublish()`](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.topicbuilder#pubsubtopicbuilderonpublish)
event handler:

<br />

```
exports.helloPubSub = functions.pubsub.topic('topic-name').onPublish((message) => {
  // ...
});
```

<br />

## Access the pub/sub message payload

The payload for the Pub/Sub message is accessible from the
[`Message`](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.message) object returned
to your function. For messages with JSON in the Pub/Sub message
body, the Firebase SDK for Cloud Functions has a helper property to decode the message. For
example, here is a message published with a simple JSON payload:

    gcloud pubsub topics publish topic-name --message '{"name":"Xenia"}'

You can access a JSON data payload like this via the
[`json`](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.message#pubsubmessagejson) property:

```
  // Get the `name` attribute of the PubSub message JSON body.
  let name = null;
  try {
    name = message.json.name;
  } catch (e) {
    functions.logger.error('PubSub message was not JSON', e);
  }
```

Other, non-JSON payloads are contained in the Pub/Sub message as
base64 encoded strings in the message object. To read a message like the
following, you must decode the base64 encoded string as shown:

    gcloud pubsub topics publish topic-name --message 'MyMessage'

<br />

```
// Decode the PubSub Message body.
const messageBody = message.data ? Buffer.from(message.data, 'base64').toString() : null;
```

<br />

## Access message attributes

Pub/Sub message can be sent with data attributes set in the
publish command. For example, you could publish a message with a `name`
attribute:

    gcloud pubsub topics publish topic-name --attribute name=Xenia

You can read such attributes from
[`Message.attributes`](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub#pubsubmessageattributes):

<br />

```
// Get the `name` attribute of the message.
const name = message.attributes.name;
```

<br />

You might notice that some basic data such as the message ID or the
message publish time are not available in `Message.attributes`. To work around
this, you can access these details in the triggering event's
[`EventContext`](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext).
For example:

    exports.myFunction = functions.pubsub.topic('topic1').onPublish((message, context) => {
        console.log('The function was triggered at ', context.timestamp);
        console.log('The unique ID for the event is', context.eventId);
    });