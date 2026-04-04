# Source: https://firebase.google.com/docs/functions/1st-gen/task-functions-1st.md.txt

> [!NOTE]
> **Note:** The 1st-gen functionality described in this page is also supported in Cloud Functions (2nd gen) with improved features and performance. For more information about 2nd gen, see the [version comparison](https://firebase.google.com/docs/functions/version-comparison). To go directly to the 2nd gen guide for this feature, see [Enqueue functions with Cloud Tasks](https://firebase.google.com/docs/functions/task-functions).

Task queue functions take advantage of Google
[Cloud Tasks](https://cloud.google.com/tasks/docs/dual-overview)
to help your app run time-consuming, resource-intensive, or bandwidth-limited
tasks asynchronously, outside your main application flow.

For example, imagine that you want to create backups of a large set of image
files that are currently hosted on an API with a rate limit. In order to be a
responsible consumer of that API, you need to respect their rate limits. Plus,
this kind of long-running job could be vulnerable to failure due to timeouts and
memory limits.

To mitigate this complexity, you can write a task queue function that sets basic
task options like `scheduleTime`, and `dispatchDeadline`, and then hands the
function off to a queue in Cloud Tasks. The Cloud Tasks
environment is designed specifically to ensure effective congestion control and
retry policies for these kinds of operations.

The Firebase SDK for Cloud Functions for Firebase v3.20.1 and higher interoperates
with Firebase Admin SDK v10.2.0 and higher to support task queue functions.

Using task queue functions with Firebase can result in charges for
Cloud Tasks processing. See
[Cloud Tasks pricing](https://cloud.google.com/tasks/pricing)
for more information.

## Create task queue functions

To use task queue functions, follow this workflow:

1. Write a task queue function using the Firebase SDK for Cloud Functions.
2. Test your function by triggering it with an HTTP request.
3. Deploy your function with the Firebase CLI. When deploying your task queue function for the first time, the CLI will create a task queue in Cloud Tasks with options (rate limiting and retry) specified in your source code.
4. Add tasks to the newly created task queue, passing along parameters to set up an execution schedule if needed. You can achieve this by writing the code using the Admin SDK and deploying it to Cloud Functions for Firebase.

### Write task queue functions

Use [`onDispatch`](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueuebuilder#taskstaskqueuebuilderondispatch)
to get started writing task queue functions. An important
part of writing a task queue function is to set per-queue retry and rate-
limiting configuration. Code samples in this page are based on an app that sets
up a service that backs up all images from NASA's
[Astronomy Picture of the Day](https://apod.nasa.gov/apod/astropix.html):

#### Configure task queue functions

Task queue functions come with a powerful set of configuration settings
to precisely control rate limits and retry behavior of a task queue:

    exports.backupApod = functions
        .runWith( {secrets: ["NASA_API_KEY"]})
        .tasks.taskQueue({
          retryConfig: {
            maxAttempts: 5,
            minBackoffSeconds: 60,
          },
          rateLimits: {
            maxConcurrentDispatches: 6,
          },
        }).onDispatch(async (data) => {https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/taskqueues-backup-images/functions/index.js#L35-L45

- `retryConfig.maxAttempts=5`: Each task in the task queue is automatically retried up to 5 times. This helps mitigate transient errors like network errors or temporary service disruption of a dependent, external service.
- `retryConfig.minBackoffSeconds=60`: Each task is retried at least 60 seconds apart from each attempt. This provides a large buffer between each attempt so we don't rush to exhaust the 5 retry attempts too quickly.
- `rateLimits.maxConcurrentDispatch=6`: At most 6 tasks are dispatched at a given time. This helps ensure a steady stream of requests to the underlying function and helps reduce the number of active instances and cold starts.

### Test task queue functions

For most cases, the Cloud Functions emulator is the best way to test task
queue functions. See the Emulator Suite documentation to learn how to
[instrument your app for task queue functions emulation](https://firebase.google.com/docs/functions/local-emulator#instrument-tq).

Additionally, task queue functions are exposed as simple
HTTP functions in the Firebase Local Emulator Suite. You can test an emulated task function by sending an HTTP POST
request with a json data payload:

     # start the Firebase Emulators
     firebase emulators:start

     # trigger the emulated task queue function
     curl \
      -X POST                                            # An HTTP POST request...
      -H "content-type: application/json" \              # ... with a JSON body
      http://localhost:$PORT/$PROJECT_ID/$REGION/$NAME \ # ... to function url
      -d '{"data": { ... some data .... }}'              # ... with JSON encoded data

### Deploy task queue functions

Deploy task queue function using the Firebase CLI:

    $ firebase deploy --only functions:backupApod

When deploying a task queue function for the first time, the CLI creates a
task queue in Cloud Tasks with options (rate limiting and retry) specified in your source code.

If you encounter permissions errors when deploying functions, make sure that the
appropriate [IAM roles](https://firebase.google.com/docs/projects/iam/permissions#functions)
are assigned to the user running the deployment commands.

## Enqueue task queue functions

Task queue functions can be enqueued in Cloud Tasks from a trusted
server environment like Cloud Functions for Firebase using the Firebase Admin SDK for
Node.js. If you're new to the Admin SDKs, see
[Add Firebase to a server](https://firebase.google.com/docs/admin/setup) to get started.

In a typical flow, the Admin SDK creates a new task, enqueues it in
Cloud Tasks, and sets the configuration for the task:

    exports.enqueueBackupTasks = functions.https.onRequest(
    async (_request, response) => {
      const queue = getFunctions().taskQueue("backupApod");
      const enqueues = [];
      for (let i = 0; i <= 10; i += 1) {
        // Enqueue each task with i*60 seconds delay. Our task queue function
        // should process ~1 task/min.
        const scheduleDelaySeconds = i * 60 
        enqueues.push(
            queue.enqueue(
              { id: `task-${i}` },
              {
                scheduleDelaySeconds,
                dispatchDeadlineSeconds: 60 * 5 // 5 minutes
              },
            ),
        );
      }
      await Promise.all(enqueues);
      response.sendStatus(200);

    });

- `scheduleDelaySeconds`: The sample code tries to spread out execution of tasks by associating a delay of Nth minutes for the Nth task. This translates to triggering \~ 1 task/minute. Note that you can also use `scheduleTime` if you want Cloud Tasks to trigger a task at a specific time.
- `dispatchDeadlineSeconds`: Maximum amount of time Cloud Tasks will wait for a task to complete. Cloud Tasks will retry the task following the retry configuration of the queue or until this deadline is reached. In the sample, the queue is configured to retry the task up to 5 times, but the task is automatically cancelled if the whole process (including retry attempts) takes more than 5 minutes.

> [!IMPORTANT]
> **Important:** Note that this configuration set in the Admin SDK is applied on a per-task basis, unlike retry and rate limit configuration, which are applied per-queue. You can enqueue multiple tasks with the Admin SDK for the same function with different configurations (`scheduleTime`) and so on.

## Troubleshooting

### Turn on Cloud Tasks logging

Logs from Cloud Tasks contain useful diagnostic information like the
status of the request associated with a task. By default, logs from
Cloud Tasks are turned off due to the large volume of logs it can
potentially generate on your project. We recommend you turn on the debug logs
while you are actively developing and debugging your task queue functions. See
[Turning on
logging](https://cloud.google.com/tasks/docs/logging#turning_on_logging).

### IAM Permissions

You may see `PERMISSION DENIED` errors when enqueueing tasks or when
Cloud Tasks tries to invoke your task queue functions. Ensure that your
project has the following IAM bindings:

- The identity used to enqueue tasks to Cloud Tasks needs
  `cloudtasks.tasks.create` IAM permission.

  In the sample, this is the [App Engine default service account](https://cloud.google.com/functions/docs/securing/function-identity#runtime_service_account)

    gcloud projects add-iam-policy-binding $PROJECT_ID \
      --member=serviceAccount:${PROJECT_ID}@appspot.gserviceaccount.com \
      --role=roles/cloudtasks.enqueuer

- The identity used to enqueue tasks to Cloud Tasks needs permission
  to use the service account associated with a task in Cloud Tasks.

  In the sample, this is the [App Engine default service account](https://cloud.google.com/functions/docs/securing/function-identity#runtime_service_account).

See [Google Cloud IAM documentation](https://cloud.google.com/iam/docs/impersonating-service-accounts#impersonate-sa-%0Alevel)
for instructions on how to add the App Engine default service account
as a user of the App Engine default service account.

- The identity used to trigger the task queue function needs
  `cloudfunctions.functions.invoke` permission.

  In the sample, this is the [App Engine default service account](https://cloud.google.com/functions/docs/securing/function-identity#runtime_service_account)

    gcloud functions add-iam-policy-binding $FUNCTION_NAME \
      --region=us-central1 \
      --member=serviceAccount:${PROJECT_ID}@appspot.gserviceaccount.com \
      --role=roles/cloudfunctions.invoker