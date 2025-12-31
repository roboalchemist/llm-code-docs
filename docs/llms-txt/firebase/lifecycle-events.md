# Source: https://firebase.google.com/docs/extensions/publishers/lifecycle-events.md.txt

<br />

Your extension can include[Cloud Tasksfunctions](https://firebase.google.com/docs/functions/task-functions)that trigger when an extension instance goes through any of the following lifecycle events:

- An instance of the extension is installed
- An instance of the extension is updated to a new version
- An extension instance's configuration is changed

One of the most important use cases of this feature is**backfilling data** . For example, suppose you're building an extension that generates thumbnail previews of images uploaded to aCloud Storagebucket. The main work of your extension would be done in a function triggered by the`onFinalize`Cloud Storageevent. However, only images uploaded*after* the extension is installed would be processed. By including in your extension a function triggered by the`onInstall`lifecycle event, you could also generate thumbnail previews of any*existing*images when the extension is installed.

Some other use cases of lifecycle event triggers include:

- Automate post-install setup (creating database records, indexing, etc.)
- If you have to publish backwards-incompatible changes, automatically migrate data on update

## Short-running lifecycle event handlers

If your task can run completely within the[maximumCloud Functionsduration](https://firebase.google.com/docs/functions/quotas#time_limits)(9 minutes using the first-generation API), you can write your lifecycle event handler as a single function that triggers on the task queue`onDispatch`event:  

    export const myTaskFunction = functions.tasks.taskQueue()
      .onDispatch(async () => {
        // Complete your lifecycle event handling task.
        // ...

        // When processing is complete, report status to the user (see below).
      });

Then, in your extension's`extension.yaml`file, do the following:

1. Register your function as an extension resource with the`taskQueueTrigger`property set. If you set`taskQueueTrigger`to the empty map (`{}`), your extension will provision aCloud Tasksqueue using the default settings; you can optionally[tune these settings](https://firebase.google.com/docs/extensions/publishers/lifecycle-events#task-queue-properties).

       resources:
         - name: myTaskFunction
           type: firebaseextensions.v1beta.function
           description: >-
             Describe the task performed when the function is triggered by a lifecycle
             event
           properties:
             location: ${LOCATION}
             taskQueueTrigger: {}

2. Register your function as a handler for one or more lifecycle events:

       resources:
         - ...
       lifecycleEvents:
       onInstall:
       function: myTaskFunction
       processingMessage: Resizing your existing images
       onUpdate:
       function: myOtherTaskFunction
       processingMessage: Setting up your extension
       onConfigure:
       function: myOtherTaskFunction
       processingMessage: Setting up your extension

   You can register functions for any of the following events:`onInstall`,`onUpdate`, and`onConfigure`. All of these events are optional.
   | **Note:** The message you specify here is automatically set as your extension's processing status in theFirebaseconsole when triggering your function. To update or clear the processing status when your function finishes its work, call`setProcessingState()`as described in the[Reporting status](https://firebase.google.com/docs/extensions/publishers/lifecycle-events#reporting-status)section.
3. **Recommended** : If the processing task isn't required for your extension to work, add a[user-configured parameter](https://firebase.google.com/docs/extensions/publishers/parameters#user-configured-parameters)that lets users choose whether to enable it.

   For example, add a parameter like the following:  

       params:
         - param: DO_BACKFILL
           label: Backfill existing images
           description: >
             Should existing, unresized images in the Storage bucket be resized as well?
           type: select
           options:
             - label: Yes
               value: true
             - label: No
               value: false

   And in your function, if the parameter is set to`false`, exit early:  

       export const myTaskFunction = functions.tasks.taskQueue()
         .onDispatch(async () => {
           if (!process.env.DO_BACKFILL) {
       await runtime.setProcessingState(
       "PROCESSING_COMPLETE",
       "Existing images were not resized."
       );
       return;
       }
           // Complete your lifecycle event handling task.
           // ...
         });

## Performing long-running tasks

If your task can't complete within the maximumCloud Functionsduration, break the task into subtasks and perform each subtask in sequence by enqueueing jobs with the Admin SDK's[`TaskQueue.enqueue()`](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.taskqueue#taskqueueenqueue)method.
| **Note:** Do not try to enqueue all of your subtasks at once to process them in parallel. Because authorization happens at enqueue time, tasks towards the end of the queue will fail if authorization has expired by the time they start. Instead, perform your subtasks serially as described in this section.

For example, suppose you want to backfillCloud Firestoredata. You can split the document collection into chunks using[query cursors](https://firebase.google.com/docs/firestore/query-data/query-cursors). After processing a chunk, advance the starting offset and enqueue another function invocation as shown below:  

    import { getFirestore } from "firebase-admin/firestore";
    import { getFunctions } from "firebase-admin/functions";

    exports.backfilldata = functions.tasks.taskQueue().onDispatch(async (data) => {
      // When a lifecycle event triggers this function, it doesn't pass any data,
      // so an undefined offset indicates we're on our first invocation and should
      // start at offset 0. On subsequent invocations, we'll pass an explicit
      // offset.
      const offset = data["offset"] ?? 0;

      // Get a batch of documents, beginning at the offset.
      const snapshot = await getFirestore()
        .collection(process.env.COLLECTION_PATH)
        .startAt(offset)
        .limit(DOCS_PER_BACKFILL)
        .get();
      // Process each document in the batch.
      const processed = await Promise.allSettled(
        snapshot.docs.map(async (documentSnapshot) => {
          // Perform the processing.
        })
      );

      // If we processed a full batch, there are probably more documents to
      // process, so enqueue another invocation of this function, specifying
      // the offset to start with.
      //
      // If we processed less than a full batch, we're done.
      if (processed.length == DOCS_PER_BACKFILL) {
        const queue = getFunctions().taskQueue(
          "backfilldata",
          process.env.EXT_INSTANCE_ID
        );
        await queue.enqueue({
          offset: offset + DOCS_PER_BACKFILL,
        });
      } else {
          // Processing is complete. Report status to the user (see below).
      }
    });

Add the function to your`extension.yaml`as described in the[previous section](https://firebase.google.com/docs/extensions/publishers/lifecycle-events#short-running).

## Reporting status

When all of your processing functions finish, either successfully or with an error, report the status of the task using the Admin SDK's extension runtime methods. Users can see this status on the extension details page in theFirebaseconsole.
| **Note:** Report status only once each time you handle a lifecycle event trigger. In particular, if you break your processing task into multiple function invocations, don't report status every invocation.

### Successful completion and non-fatal errors

To report successful completion and non-fatal errors (errors that don't put the extension into a nonfunctional state), use the Admin SDK's`setProcessingState()`extension runtime method:  

    import { getExtensions } from "firebase-admin/extensions";

    // ...

    getExtensions().runtime().setProcessingState(processingState, message);

You can set the following states:

|                                                                                                                                                                                                                             Non-fatal states                                                                                                                                                                                                                             ||
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PROCESSING_COMPLETE` | Use to report successful task completion. Example: ```genshi getExtensions().runtime().setProcessingState( "PROCESSING_COMPLETE", `Backfill complete. Successfully processed ${numSuccess} documents.` ); ```                                                                                                                                                                                                                                     |
| `PROCESSING_WARNING`  | Use to report partial success. Example: ```genshi getExtensions().runtime().setProcessingState( "PROCESSING_WARNING", `Backfill complete. ${numSuccess} documents processed successfully.` + ` ${numFailed} documents failed to process. ${listOfErrors}.` + ` ${instructionsToFixTheProblem}` ); ```                                                                                                                                             |
| `PROCESSING_FAILED`   | Use to report errors that prevent the task from completing, but don't leave the extension unusable. Example: ```genshi getExtensions().runtime().setProcessingState( "PROCESSING_FAILED", `Backfill failed. ${errorMsg} ${optionalInstructionsToFixTheProblem}.` ); ``` To report errors that*do* leave the extension unusable, call[`setFatalError()`](https://firebase.google.com/docs/extensions/publishers/lifecycle-events#set-fatal-error). |
| `NONE`                | Use to clear the task's status. You can optionally use this to clear the status message from the console (for example, after some amount of time has passed since setting`PROCESSING_COMPLETE`). Example: ```text getExtensions().runtime().setProcessingState("NONE"); ```                                                                                                                                                                       |

### Fatal errors

If an error occurs that prevents the extension from functioning---for example, a required setup task failing---report the fatal error with`setFatalError()`:  

    import { getExtensions } from "firebase-admin/extensions";

    // ...

    getExtensions().runtime().setFatalError(`Post-installation setup failed. ${errorMessage}`);

## Tuning the task queue

If you set the`taskQueueTrigger`property to`{}`, your extension will provision a Cloud Tasks queue with the default settings when an extension instance is installed. Alternatively, you can tune the task queue's concurrency limits and retry behavior by providing specific values:  

    resources:
      - name: myTaskFunction
        type: firebaseextensions.v1beta.function
        description: >-
          Perform a task when triggered by a lifecycle event
        properties:
          location: ${LOCATION}
          taskQueueTrigger:
    rateLimits:
    maxConcurrentDispatches: 1000
    maxDispatchesPerSecond: 500
    retryConfig:
    maxAttempts: 100 # Warning: setting this too low can prevent the function from running
    minBackoffSeconds: 0.1
    maxBackoffSeconds: 3600
    maxDoublings: 16
    lifecycleEvents:
      onInstall: 
        function: myTaskFunction
        processingMessage: Resizing your existing images
      onUpdate:
        function: myTaskFunction
        processingMessage: Setting up your extension
      onConfigure:
        function: myOtherTaskFunction
        processingMessage: Setting up your extension

See[Configure Cloud Tasks queues](https://cloud.google.com/tasks/docs/configuring-queues)in the Google Cloud docs for details on these parameters.

Don't try to specify task queue parameters by passing them to`taskQueue()`. These settings are ignored in favor of the configuration in`extension.yaml`and the configuration defaults.

For example, this won't work:  

    export const myBrokenTaskFunction = functions.tasks
      // DON'T DO THIS IN AN EXTENSION! THESE SETTINGS ARE IGNORED.
      .taskQueue({
        retryConfig: {
          maxAttempts: 5,
          minBackoffSeconds: 60,
        },
        rateLimits: {
          maxConcurrentDispatches: 1000,
          maxDispatchesPerSecond: 10,
        },
      })
      .onDispatch(
        // ...
      );

The`taskQueueTrigger`property in`extension.yaml`is the only way to configure an extension's task queues.

## Examples

The official[`storage-resize-images`](https://github.com/Firebase/extensions/blob/master/storage-resize-images/functions/src/index.ts),[`firestore-bigquery-export`](https://github.com/Firebase/extensions/blob/master/firestore-bigquery-export/functions/src/index.ts), and[`firestore-translate-text`](https://github.com/Firebase/extensions/blob/master/firestore-translate-text/functions/src/index.ts)extensions all use lifecycle event handlers to backfill data.