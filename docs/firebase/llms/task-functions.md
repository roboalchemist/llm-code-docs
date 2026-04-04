# Source: https://firebase.google.com/docs/functions/task-functions.md.txt

<br />

Task queue functions take advantage of Google[Cloud Tasks](https://cloud.google.com/tasks/docs/dual-overview)to help your app run time-consuming, resource-intensive, or bandwidth-limited tasks asynchronously, outside your main application flow.

For example, imagine that you want to create backups of a large set of image files that are currently hosted on an API with a rate limit. In order to be a responsible consumer of that API, you need to respect their rate limits. Plus, this kind of long-running job could be vulnerable to failure due to timeouts and memory limits.

To mitigate this complexity, you can write a task queue function that sets basic task options like`scheduleTime`, and`dispatchDeadline`, and then hands the function off to a queue inCloud Tasks. TheCloud Tasksenvironment is designed specifically to ensure effective congestion control and retry policies for these kinds of operations.

The Firebase SDK forCloud Functions for Firebasev3.20.1 and higher interoperates withFirebaseAdmin SDKv10.2.0 and higher to support task queue functions.

Using task queue functions with Firebase can result in charges forCloud Tasksprocessing. See[Cloud Taskspricing](https://cloud.google.com/tasks/pricing)for more information.

## Create task queue functions

To use task queue functions, follow this workflow:

1. Write a task queue function using theFirebaseSDK forCloud Functions.
2. Test your function by triggering it with an HTTP request.
3. Deploy your function with theFirebaseCLI. When deploying your task queue function for the first time, the CLI will create a task queue inCloud Taskswith options (rate limiting and retry) specified in your source code.
4. Add tasks to the newly created task queue, passing along parameters to set up an execution schedule if needed. You can achieve this by writing the code using theAdmin SDKand deploying it toCloud Functions for Firebase.

### Write task queue functions

Code samples in this section are based on an app that sets up a service that backs up all images from NASA's[Astronomy Picture of the Day](https://apod.nasa.gov/apod/astropix.html). To get started, import the required modules:  

### Node.js

    // Dependencies for task queue functions.
    const {onTaskDispatched} = require("firebase-functions/tasks");
    const {onRequest, HttpsError} = require("firebase-functions/https");
    const {getFunctions} = require("firebase-admin/functions");
    const {logger} = require("firebase-functions");

    // Dependencies for image backup.
    const path = require("path");
    const {initializeApp} = require("firebase-admin/app");
    const {getStorage} = require("firebase-admin/storage");
    const {GoogleAuth} = require("google-auth-library");  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/taskqueues-backup-images/functions/index.js#L18-L28

### Python

    # Dependencies for task queue functions.
    from google.cloud import tasks_v2
    import requests
    from firebase_functions.options import RetryConfig, RateLimits, SupportedRegion

    # Dependencies for image backup.
    from datetime import datetime, timedelta
    import json
    import pathlib
    from urllib.parse import urlparse
    from firebase_admin import initialize_app, storage, functions
    from firebase_functions import https_fn, tasks_fn, params
    import google.auth
    from google.auth.transport.requests import AuthorizedSession  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/taskqueues-backup-images/functions/main.py#L16-L29

Use[`onTaskDispatched`](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks#tasksontaskdispatched)or[`on_task_dispatched`](https://firebase.google.com/docs/reference/functions/2nd-gen/python/firebase_functions.tasks_fn)for task queue functions. When writing a task queue function you can set per-queue retry and rate- limiting configuration.

#### Configure task queue functions

Task queue functions come with a powerful set of configuration settings to precisely control rate limits and retry behavior of a task queue:  

### Node.js

    exports.backupapod = onTaskDispatched(
        {
          retryConfig: {
            maxAttempts: 5,
            minBackoffSeconds: 60,
          },
          rateLimits: {
            maxConcurrentDispatches: 6,
          },
        }, async (req) => {  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/taskqueues-backup-images/functions/index.js#L42-L51

### Python

    @tasks_fn.on_task_dispatched(retry_config=RetryConfig(max_attempts=5, min_backoff_seconds=60),
                                 rate_limits=RateLimits(max_concurrent_dispatches=10))
    def backupapod(req: tasks_fn.CallableRequest) -> str:
        """Grabs Astronomy Photo of the Day (APOD) using NASA's API."""  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/taskqueues-backup-images/functions/main.py#L43-L46

- `retryConfig.maxAttempts=5`: Each task in the task queue is automatically retried up to 5 times. This helps mitigate transient errors like network errors or temporary service disruption of a dependent, external service.

- `retryConfig.minBackoffSeconds=60`: Each task is retried at least 60 seconds apart from each attempt. This provides a large buffer between each attempt so we don't rush to exhaust the 5 retry attempts too quickly.

- `rateLimits.maxConcurrentDispatch=6`: At most 6 tasks are dispatched at a given time. This helps ensure a steady stream of requests to the underlying function and helps reduce the number of active instances and cold starts.

### Test task queue functions

For most cases, theCloud Functionsemulator is the best way to test task queue functions. See the Emulator Suite documentation to learn how to[instrument your app for task queue functions emulation](https://firebase.google.com/docs/functions/local-emulator#instrument-tq).

Additionally, task queue functions are exposed as simple HTTP functions in theFirebase Local Emulator Suite. You can test an emulated task function by sending an HTTP POST request with a JSON data payload:  

     # start the Local Emulator Suite
     firebase emulators:start

     # trigger the emulated task queue function
     curl \
      -X POST                                            # An HTTP POST request...
      -H "content-type: application/json" \              # ... with a JSON body
      http://localhost:$PORT/$PROJECT_ID/$REGION/$NAME \ # ... to function url
      -d '{"data": { ... some data .... }}'              # ... with JSON encoded data

### Deploy task queue functions

Deploy task queue function using theFirebaseCLI:  

    $ firebase deploy --only functions:backupapod

When deploying a task queue function for the first time, the CLI creates a task queue inCloud Taskswith options (rate limiting and retry) specified in your source code.

If you encounter permissions errors when deploying functions, make sure that the appropriate[IAM roles](https://firebase.google.com/docs/projects/iam/permissions#functions)are assigned to the user running the deployment commands.

## Enqueue task queue functions

Task queue functions can be enqueued inCloud Tasksfrom a trusted server environment likeCloud Functions for Firebaseusing theFirebaseAdmin SDKfor Node.js or Google Cloud libraries for Python. If you're new to theAdmin SDKs, see[Add Firebase to a server](https://firebase.google.com/docs/admin/setup)to get started.

A typical flow creates a new task, enqueues it inCloud Tasks, and sets the configuration for the task:  

### Node.js

    exports.enqueuebackuptasks = onRequest(
        async (_request, response) => {
          const queue = getFunctions().taskQueue("backupapod");
          const targetUri = await getFunctionUrl("backupapod");

          const enqueues = [];
          for (let i = 0; i <= BACKUP_COUNT; i += 1) {
            const iteration = Math.floor(i / HOURLY_BATCH_SIZE);
            // Delay each batch by N * hour
            const scheduleDelaySeconds = iteration * (60 * 60);

            const backupDate = new Date(BACKUP_START_DATE);
            backupDate.setDate(BACKUP_START_DATE.getDate() + i);
            // Extract just the date portion (YYYY-MM-DD) as string.
            const date = backupDate.toISOString().substring(0, 10);
            enqueues.push(
                queue.enqueue({date}, {
                  scheduleDelaySeconds,
                  dispatchDeadlineSeconds: 60 * 5, // 5 minutes
                  uri: targetUri,
                }),
            );
          }
          await Promise.all(enqueues);
          response.sendStatus(200);
        });  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/taskqueues-backup-images/functions/index.js#L132-L157

### Python

    @https_fn.on_request()
    def enqueuebackuptasks(_: https_fn.Request) -> https_fn.Response:
        """Adds backup tasks to a Cloud Tasks queue."""
        task_queue = functions.task_queue("backupapod")
        target_uri = get_function_url("backupapod")

        for i in range(BACKUP_COUNT):
            batch = i // HOURLY_BATCH_SIZE

            # Delay each batch by N hours
            schedule_delay = timedelta(hours=batch)
            schedule_time = datetime.now() + schedule_delay

            dispatch_deadline_seconds = 60 * 5  # 5 minutes

            backup_date = BACKUP_START_DATE + timedelta(days=i)
            body = {"data": {"date": backup_date.isoformat()[:10]}}
            task_options = functions.TaskOptions(schedule_time=schedule_time,
                                                 dispatch_deadline_seconds=dispatch_deadline_seconds,
                                                 uri=target_uri)
            task_queue.enqueue(body, task_options)
        return https_fn.Response(status=200, response=f"Enqueued {BACKUP_COUNT} tasks")  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/taskqueues-backup-images/functions/main.py#L96-L117

- The sample code tries to spread out execution of tasks by associating a delay of Nth minutes for the Nth task. This translates to triggering \~ 1 task/minute. Note that you can also use`scheduleTime`(Node.js) or`schedule_time`(Python) if you wantCloud Tasksto trigger a task at a specific time.

- The sample code sets the maximum amount of timeCloud Taskswill wait for a task to complete.Cloud Taskswill retry the task following the retry configuration of the queue or until this deadline is reached. In the sample, the queue is configured to retry the task up to 5 times, but the task is automatically cancelled if the whole process (including retry attempts) takes more than 5 minutes.

| **Important:** Note that this configuration set in theAdmin SDKis applied on a per-task basis, unlike retry and rate limit configuration, which are applied per-queue. You can enqueue multiple tasks with theAdmin SDKfor the same function with different configurations (`scheduleTime`) and so on.

## Troubleshooting

### Turn onCloud Taskslogging

Logs fromCloud Taskscontain useful diagnostic information like the status of the request associated with a task. By default, logs fromCloud Tasksare turned off due to the large volume of logs it can potentially generate on your project. We recommend you turn on the debug logs while you are actively developing and debugging your task queue functions. See[Turning on logging](https://cloud.google.com/tasks/docs/logging#turning_on_logging).

### IAM Permissions

You may see`PERMISSION DENIED`errors when enqueueing tasks or whenCloud Taskstries to invoke your task queue functions. Ensure that your project has the following IAM bindings:

- The identity used to enqueue tasks toCloud Tasksneeds`cloudtasks.tasks.create`IAM permission.

  In the sample, this is the[App Enginedefault service account](https://cloud.google.com/functions/docs/securing/function-identity#runtime_service_account)

    gcloud projects add-iam-policy-binding $PROJECT_ID \
      --member=serviceAccount:${PROJECT_ID}@appspot.gserviceaccount.com \
      --role=roles/cloudtasks.enqueuer

- The identity used to enqueue tasks toCloud Tasksneeds permission to use the service account associated with a task inCloud Tasks.

  In the sample, this is the[App Enginedefault service account](https://cloud.google.com/functions/docs/securing/function-identity#runtime_service_account).

See[Google Cloud IAM documentation](https://cloud.google.com/iam/docs/impersonating-service-accounts#impersonate-sa-%0Alevel)for instructions on how to add theApp Enginedefault service account as a user of theApp Enginedefault service account.

- The identity used to trigger the task queue function needs`cloudfunctions.functions.invoke`permission.

  In the sample, this is the[App Enginedefault service account](https://cloud.google.com/functions/docs/securing/function-identity#runtime_service_account)

    gcloud functions add-iam-policy-binding $FUNCTION_NAME \
      --region=us-central1 \
      --member=serviceAccount:${PROJECT_ID}@appspot.gserviceaccount.com \
      --role=roles/cloudfunctions.invoker