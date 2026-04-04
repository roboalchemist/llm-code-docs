# Source: https://firebase.google.com/docs/functions/pubsub-events.md.txt

<br />

Google Cloud's[Pub/Sub](https://cloud.google.com/pubsub/docs/)is a globally distributed message bus that automatically scales as you need it. You can trigger a function whenever a newPub/Submessage is sent to a specific topic.

## Import the required modules

To get started, import the modules required for handlingPub/Subevents:  

### Node.js

    const {onMessagePublished} = require("firebase-functions/pubsub");
    const logger = require("firebase-functions/logger");  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/pubsub-helloworld/functions/index.js#L19-L20

### Python

    from firebase_functions import pubsub_fn  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/pubsub-helloworld/functions/main.py#L18-L18

## Trigger the function

You must specify thePub/Subtopic name that you want to trigger your function, and set the event within the event handler:  

### Node.js

    exports.hellopubsub = onMessagePublished("topic-name", (event) => {  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/pubsub-helloworld/functions/index.js#L29-L29

### Python

    @pubsub_fn.on_message_published(topic="topic-name")
    def hellopubsub(event: pubsub_fn.CloudEvent[pubsub_fn.MessagePublishedData]) -> None:
        """Log a message using data published to a Pub/Sub topic."""  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/pubsub-helloworld/functions/main.py#L24-L26

## Access the pub/sub message payload

The payload for thePub/Submessage is accessible from the message object returned to your function. For messages with JSON in thePub/Submessage body, theFirebaseSDK forCloud Functionshas a helper property to decode the message. For example, here is a message published with a simple JSON payload:  

    gcloud pubsub topics publish topic-name --message '{"name":"Xenia"}'

You can access a JSON data payload like this via the`json`property:  

### Node.js

```javascript
  // Get the `name` attribute of the PubSub message JSON body.
  let name = null;
  try {
    name = event.data.message.json.name;
  } catch (e) {
    logger.error("PubSub message was not JSON", e);
  }https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/pubsub-helloworld/functions/index.js#L51-L57
```

### Python

    # Get the `name` attribute of the PubSub message JSON body.
    try:
        data = event.data.message.json
    except ValueError:
        print("PubSub message was not JSON")
        return
    if data is None:
        return
    if "name" not in data:
        print("No 'name' key")
        return
    name = data["name"]  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/pubsub-helloworld/functions/main.py#L42-L53

Other, non-JSON payloads are contained in thePub/Submessage as base64 encoded strings in the message object. To read a message like the following, you must decode the base64 encoded string as shown:  

    gcloud pubsub topics publish topic-name --message 'MyMessage'

### Node.js

```javascript
// Decode the PubSub Message body.
const message = event.data.message;
const messageBody = message.data ?
      Buffer.from(message.data, "base64").toString() :
      null;https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/pubsub-helloworld/functions/index.js#L32-L36
```

### Python

    # Decode the PubSub message body.
    message_body = base64.b64decode(event.data.message.data)  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/pubsub-helloworld/functions/main.py#L29-L30

## Access message attributes

Pub/Submessage can be sent with data attributes set in the publish command. For example, you could publish a message with a`name`attribute:  

    gcloud pubsub topics publish topic-name --attribute name=Xenia

You can read such attributes from the corresponding property of the message object:  

### Node.js

```javascript
// Get the `name` attribute of the message.
const name = event.data.message.attributes.name;https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/pubsub-helloworld/functions/index.js#L71-L72
```

### Python

    # Get the `name` attribute of the message.
    if "name" not in event.data.message.attributes:
        print("No 'name' attribute")
        return
    name = event.data.message.attributes["name"]  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/pubsub-helloworld/functions/main.py#L64-L68