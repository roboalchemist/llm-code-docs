# Source: https://firebase.google.com/docs/extensions/publishers/user-hooks.md.txt

<br />

You can provide users who install your extension the ability to insert their own custom logic into the execution of your extension. There are two ways to accomplish this:

- **Eventarc events**: to give users a way to asynchronously react to events, you can publish to Eventarc. Users can deploy event handler functions that, for example, send notifications after long-running tasks complete, or they can define their own post-processing functions.

- **Synchronous hooks**: to give users a way to add blocking logic to your extension, you can add synchronous hooks at predefined points in the extension's operation. At these points, you run a user-provider function and proceed only after it completes. Pre-processing tasks often fall under this category.

An extension can use either or both methods.

## Eventarc events

To publish events from an extension:

1. Declare the event types you will publish in the`extension.yaml`file:

       events:
         - type: publisher-id.extension-name.version.event-name
           description: event-description
         - type: publisher-id.extension-name.version.another-event-name
           description: another-event-description

   The`type`identifier is made of several dot-delimited fields. The[publisher ID](https://firebase.google.com/docs/extensions/publishers/register), extension name, and event name fields are required. The version field is recommended. Choose a unique and descriptive event name for each event type you publish.

   For example, the[`storage-resize-images`extension](https://github.com/firebase/extensions/blob/next/storage-resize-images/extension.yaml)declares a single event type:  

       events:
         - type: firebase.extensions.storage-resize-images.v1.complete
           description: |
             Occurs when image resizing completes. The event will contain further
             details about specific formats and sizes.

   Users will be able to choose which events to subscribe to when they install the extension.
2. In your extension functions, import the Eventarc API from theAdmin SDKand initialize an event channel using the user's installation settings. These settings are exposed using the following environment variables:

   - `EVENTARC_CHANNEL`: the fully-qualified name of the Eventarc channel to which the user chose to publish events.
   - `EXT_SELECTED_EVENTS`: a comma-separated list of event types the user chose to publish. When you initialize a channel with this value, the Admin SDK automatically filters out events user did not select.
   - `EVENTARC_CLOUD_EVENT_SOURCE`: the Cloud Event source identifier. The Admin SDK automatically passes this value in the`source`field of published events. You typically don't need to explicitly use this variable.

   If events weren't enabled at installation, these variables will be undefined. You can use this fact to initialize an event channel only when events are enabled:  

       import * as admin from "firebase-admin";
       import {getEventarc} from 'firebase-admin/eventarc';

       admin.initializeApp();

       // Set eventChannel to a newly-initialized channel, or `undefined` if events
       // aren't enabled.
       const eventChannel =
         process.env.EVENTARC_CHANNEL &&
         getEventarc().channel(process.env.EVENTARC_CHANNEL, {
           allowedEventTypes: process.env.EXT_SELECTED_EVENTS,
         });

3. Publish events to the channel at the points in your extension you want to expose to users. For example:

       // If events are enabled, publish a `complete` event to the configured
       // channel.
       eventChannel && eventChannel.publish({
           type: 'firebase.extensions.storage-resize-images.v1.complete',
           subject: filename,  // the name of the original file
           data: {
             // ...
           }
       });

4. Document the events you publish, in either the PREINSTALL or POSTINSTALL file.

   For each event, document the following:
   - Its intended purpose
   - The point in your extension's logic it runs
   - The output data it includes
   - The conditions for its execution

   Additionally, warn users not to perform any actions in their event handlers that might trigger the same extension, resulting in an infinite loop.

When you publish events from an extension, users can deploy event handlers to respond with custom logic.

For example, the following example deletes the original image after it has been resized. Note that this example handler makes use of the`subject`property of the event, which in this case is the image's original filename.  

    exports.onimageresized = onCustomEventPublished(
        "firebase.extensions.storage-resize-images.v1.complete",
        (event) => {
          logger.info("Received image resize completed event", event);
          // For example, delete the original.
          return admin.storage()
              .bucket("my-project.firebasestorage.app")
              .file(event.subject)
              .delete();
        });

See[Custom event triggers](https://firebase.google.com/docs/functions/custom-events#handle-events)for more information.

### Example

The official[Resize Images extension](https://github.com/firebase/extensions/tree/next/storage-resize-images)provides an asynchronous hook by[publishing to Eventarc](https://github.com/firebase/extensions/blob/c29781c7e67c004e2491e4ce3c43b25b05bd3de6/storage-resize-images/functions/src/index.ts#L109-L117)after resizing an image.

## Synchronous hooks

When you want to provide users with a hook that must complete successfully for one of your extension functions to operate, use*synchronous hooks*.

A synchronous hook calls a user-defined[HTTPS callable Cloud Function](https://firebase.google.com/docs/functions/http-events)and awaits completion (possibly with a returned value) before continuing. An error in the user-provided function results in an error in the extension function.

To expose a synchronous hook:

1. Add a parameter to your extension that allows users to configure the extension with the URL to their custom Cloud Function. For example:

       - param: PREPROCESSING_FUNCTION
         label: Pre-processing function URL
         description: >
           An HTTPS callable function that will be called to transform the input data
           before it is processed by this function.
         type: string
         example: https://us-west1-my-project-id.cloudfunctions.net/preprocessData
         required: false

2. At the point in your extension where you want to expose the hook, call the function using its URL. For example:

       const functions = require('firebase-functions/v1');
       const fetch = require('node-fetch');

       const preprocessFunctionURL = process.env.PREPROCESSING_FUNCTION;

       exports.yourFunctionName = functions.firestore.document("collection/{doc_id}")
           .onWrite((change, context) => {
             // PREPROCESSING_FUNCTION hook begins here.
             // If a preprocessing function is defined, call it before continuing.
             if (preprocessFunctionURL) {
               try {
                 await fetch(preprocessFunctionURL); // Could also be a POST request if you want to send data.
               } catch (e) {
                 // Preprocessing failure causes the function to fail.
                 functions.logger.error("Preprocessor error:", e);
                 return;
               }
             }
             // End of PREPROCESSING_FUNCTION hook.

             // Main function logic follows.
             // ...
           });

3. Document any hooks you make available in either the PREINSTALL or POSTINSTALL file.

   For each hook, document the following:
   - Its intended purpose
   - The point in your extension's logic it runs
   - Its expected inputs and outputs
   - The conditions (or options) for its execution

   Additionally, warn users not to perform any actions in the hook function that might trigger the same extension, resulting in an infinite loop.

### Example

The[Algolia Search extension](https://github.com/algolia/firestore-algolia-search/)provides a synchronous hook to[call a user-supplied transform function](https://github.com/algolia/firestore-algolia-search/blob/34592d513eac22691d76917874a6466032976f67/functions/src/transform.ts)prior to writing to Algolia.