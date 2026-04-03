# Source: https://firebase.google.com/docs/functions/custom-events.md.txt

<br />

WithCloud Functions(2nd gen), you can trigger functions in response to*custom events* . These are events provided by special or additional event providers, as opposed to the Firebase events natively supported by theFirebaseSDK forCloud Functions. Via custom event triggers, your app can respond to events provided byFirebase Extensions, or you can publish your own custom events and trigger functions in response to them.
| **Note:**This feature is a public preview. This means that the functionality might change in backward-incompatible ways. A preview release is not subject to any SLA or deprecation policy and may receive limited or no support.

All custom events conform to the[CloudEvents JSON event format](https://cloud.google.com/eventarc/docs/workflows/cloudevents)and are published to[Eventarc](https://cloud.google.com/eventarc/docs/overview).Eventarc[usage fees](https://cloud.google.com/eventarc/pricing)apply.

## Trigger functions with custom events

You can publish custom events (or obtain events from Firebase extensions) and trigger functions in response to those events by implementing this basic flow:

1. Publish the desired events to an Eventarc channel, or identify available events provided by an extension that you have installed.
2. In your function code, subscribe to events on the Eventarc channel with an event handler.
3. In the function, parse the payload returned in the CloudEvent object and perform whatever custom logic your app requires.

For example, a game app might want to send notifications to users as they enter or leave the leaderboard of top ten competitors. This app could publish leaderboard events to the default channel, and then handle the event in a function that sends targeted push notifications to users.

In another example, an extension designed to help apps process large images might emit an event on the completion of image resizing. Apps with this extension installed could handle the completion event by updating links in the app to point to resized versions of the image.

### Publish an event to a channel

Eventarc events are published into[channels](https://cloud.google.com/eventarc/docs/third-parties/create-channels). Channels are a way to group related events and manage access permissions. When you install an extension or deploy a function that consumes custom events, Firebase automatically creates a default channel named`firebase`in the`us-central1`region. TheFirebaseAdmin SDKprovides an`eventarc`subpackage for publishing to channels.

To publish an event from a trusted server (or another function) using the default channel:  

    import {getEventarc} from 'firebase-admin/eventarc';

    getEventarc().channel().publish({
        type: 'achieved-leaderboard',
        subject: 'Welcome to the top 10',
        data: {
          message: 'You have achieved the nth position in our leaderboard!  To see . . .'
        }
    });

In addition to automatically creating the default channel, Firebase sets the environment variable`EVENTARC_CLOUD_EVENT_SOURCE`, which specifies the source of the event. If you are publishing events outside ofCloud Functions for Firebase, you'll need to explicitly add the`source`field in your event payload.

### Handle custom events

You can handle all custom events, including extensions events, with the[`onCustomEventPublished`](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc#eventarconcustomeventpublished)or[`on_custom_event_published`](https://firebase.google.com/docs/reference/functions/2nd-gen/python/firebase_functions.eventarc_fn#on_custom_event_published)handlers. First, import this handler from the Eventarc SDK along with theFirebaseAdmin SDK:  

### Node.js

    const {onCustomEventPublished} = require("firebase-functions/eventarc");
    const logger = require("firebase-functions/logger");
    const {initializeApp} = require("firebase-admin/app");
    const {getFirestore} = require("firebase-admin/firestore");  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/custom-events/functions/index.js#L18-L22

### Python

    from firebase_admin import firestore, initialize_app
    from firebase_functions import eventarc_fn  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/custom-events/functions/main.py#L16-L17

In your function code, pass in the event name as shown for the example function:  

### Node.js

    exports.onimageresized = onCustomEventPublished(
        "firebase.extensions.storage-resize-images.v1.complete",
        (event) => {
          logger.info("Received image resize completed event", event);
          // For example, write resized image details into Firestore.
          return getFirestore()
              .collection("images")
              .doc(event.subject.replace("/", "_")) // original file path
              .set(event.data); // resized images paths and sizes
        });  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/custom-events/functions/index.js#L28-L37

### Python

    @eventarc_fn.on_custom_event_published(
        event_type="firebase.extensions.storage-resize-images.v1.complete")
    def onimageresized(event: eventarc_fn.CloudEvent) -> None:
        print("Received image resize completed event: ", event.type)

        if not isinstance(event.subject, str):
            print("No 'subject' data.")
            return

        # For example, write resized image details into Firestore.
        firestore_client: google.cloud.firestore.Client = firestore.client()
        collection = firestore_client.collection("images")
        doc = collection.document(event.subject.replace("/", "_"))  # original file path
        doc.set(event.data)  # resized images paths and sizes  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/custom-events/functions/main.py#L25-L38

For each particular extension, the payload returned in the event object provides data you can use to perform custom logic for your application flow. In this case, the function uses theAdmin SDKto copy metadata about the resized image to a collection inCloud Firestore, obtaining the filename from the`subject`provided by the event, and saving metadata from the`data`provided by the event.

### Publish and handle events on non-default channels

Custom channels can be useful for cases where you have special permission needs or other requirements, and don't want the same level of visibility and access for all events. You can create your own channels using the[Google Cloud console](https://console.cloud.google.com/eventarc/channels). Publishing and subscribing for events must be done on the same channel.

In cases where a custom event is published on a non-default channel, you'll need to specify the channel in your function code. For example, if you want to handle events that are published in a non-default channel for the`us-west1`location, you need to specify the channel as shown:  

### Node.js

    import { onCustomEventPublished } from "firebase-functions/v2/eventarc";

    export const func = onCustomEventPublished(
        {
          eventType: "firebase.extensions.storage-resize-images.v1.complete",
          channel: "locations/us-west1/channels/firebase",
          region: "us-west1",
        },
        (event) => { ... });

### Python

    @eventarc_fn.on_custom_event_published(
        event_type="firebase.extensions.storage-resize-images.v1.complete",
        channel="locations/us-west1/channels/firebase",
        region="us-west1")
    def onimageresizedwest(event: eventarc_fn.CloudEvent) -> None:
        print("Received image resize completed event: ", event.type)
        # ...  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/custom-events/functions/main.py#L43-L59