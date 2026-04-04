# Source: https://firebase.google.com/docs/functions/quotas.md.txt

This page details the scalable, usage-based limits for Cloud Functions
according to the Blaze pay-as-you-go pricing plan. These limits apply to
Firebase projects that deploy functions to the Node.js 10 runtime environment.

The Blaze plan provides generous amounts of invocations, compute time, and
internet traffic free of charge. However, function deployments incur
small-scale charges for the storage space used for the function's container.
See the Firebase [FAQ](https://firebase.google.com/docs/functions/faq-and-troubleshooting#storage-charge) for more information.

> [!NOTE]
> To increase quotas above the defaults listed here, go to the [Firebase Quotas Page](https://console.cloud.google.com/iam-admin/quotas?service=cloudfunctions.googleapis.com&usage=ALL&project=_), select the quotas you want to modify, click **Edit quotas**, supply your user information if prompted, and enter the new quota limit for each quota you selected.

Quotas for Firebase encompass 4 areas:

- Resource Limits

  These affect the total amount of resources your functions can consume.
- Time Limits

  These affect how long things can run.
- Rate Limits

  These affect the rate at which you can call the Firebase API
  to manage your functions.
- Networking Limits

  These affect outbound connection and instance limits.

The different types of limits are described in more detail below.
Differences between limits for Firebase (1st gen) and
Firebase (2nd gen) are noted where applicable.

## Resource Limits

Resource limits affect the total amount of resources your functions can consume.
The regional scope is per project, and each project maintains its own limits.

| Quota | Description | Limit (1st gen) | Limit (2nd gen) | Can be increased | Scope |
|---|---|---|---|---|---|
| Number of functions | The total number of functions that can be deployed per region | 1,000 | 1,000 minus the number of Cloud Run services deployed | No | per region |
| Max deployment size | The maximum size of a single function deployment | 100MB (compressed) for sources. 500MB (uncompressed) for sources plus modules. | N/A | No | per function |
| Max uncompressed HTTP request size | Data sent to HTTP Functions in an HTTP request | 10MB | 32MB | No | per invocation |
| Max uncompressed HTTP response size | Data sent from HTTP functions in an HTTP response | 10MB | 10MB for streaming responses. 32MB for non-streaming responses. | No | per invocation |
| Max event size for event-driven functions | Data sent in events to background functions | 10MB | 512KB for Eventarc events. 10MB for legacy events. | No | per event |
| Max function memory | Amount of memory each function instance can use | 8GiB | 32GiB | No | per function |
| Max project memory | Amount of memory, in By, that a project can use. It is measured by the total sum of user-requested memory across function instances over a 1 minute period. | Depends on selected region. This limit might be greater in high-capacity regions or lower in recently opened regions. | N/A | Yes | per project and region |
| Max project CPU | Amount of CPU, in milli vCPU, that a project can use. It is measured by the total sum of user-requested CPU across function instances over a 1 minute period. | Depends on selected region. This limit might be greater in high-capacity regions or lower in recently opened regions. | N/A | Yes | per project and region |

> [!NOTE]
> **Note:** If you are triggering a function using Pub/Sub, either via [event-driven functions](https://firebase.google.com/docs/functions/pubsub-events) or as the [HTTP target](https://firebase.google.com/docs/functions/http-events) of a push subscription, be aware that Pub/Sub messages are base64-encoded. A 10 MB Pub/Sub message - the [maximum size](https://cloud.google.com/pubsub/quotas#resource_limits) supported - is larger than 10 MB once it is encoded, and can thus exceed the Cloud Functions max size limit.

## Time Limits

| Quota | Description | Limit (1st gen) | Limit (2nd gen) | Can be increased | Scope |
|---|---|---|---|---|---|
| Max function duration | The maximum amount of time a function can run before being forcibly terminated | 540 seconds | - 60 minutes for HTTP functions. - 1800 seconds for scheduled/Task queue functions. - 540 seconds for event-driven functions. | No | per invocation |

## Rate Limits

| Quota | Description | Limit (1st gen) | Limit (2nd gen) | Can be increased | Scope |
|---|---|---|---|---|---|
| API calls (READ) | Calls to describe or list functions via the Firebase API | 5000 per 100 seconds | 1200 per 60 seconds | Only for 1st gen | per project (1st gen) per region (2nd gen) |
| API calls (WRITE) | Calls to deploy or delete functions via the Firebase API | 80 per 100 seconds | 60 per 60 seconds | No [^1^](https://firebase.google.com/docs/functions/quotas#footnote) | per project (1st gen) per region (2nd gen) |
| API calls (CALL) | Calls to the "call" API | 16 per 100 seconds | N/A | No [^2^](https://firebase.google.com/docs/functions/quotas#footnote) | per project |

> [!NOTE]
> ^1^ You cannot increase the WRITE quota. Insufficient quota generally occurs due to one of the following:
>
> - Use of a CI/CD system that deploys many functions concurrently or sequentially at a high rate.
> - Use of the Firebase CLI to deploy multiple functions simultaneously.
>
> In each case, you can avoid hitting this quota by changing the rate of
> deployments. For example, if you are deploying using the Firebase CLI,
> [use
> the `--only` flag to deploy individual functions](https://firebase.google.com/docs/cli/#deploy_specific_functions).

> [!NOTE]
> ^2^ The CALL API only applies to Firebase (1st gen). You cannot increase the CALL quota. Insufficient quota generally occurs if you mistakenly use this API to invoke your functions in production. Please keep in mind that this API is meant for testing with the Google Cloud console or [`gcloud functions call`](https://cloud.google.com/sdk/gcloud/reference/functions/call) CLI, and it cannot handle heavy traffic.

## Networking limits

For information about Firebase (2nd gen) networking request and
bandwidth limits, see [Networking limits](https://cloud.google.com/run/quotas#networking_limits).

The following networking limits apply to Firebase (1st gen):

- Outbound connections per second per instance: 500 (cannot be increased)
- Outbound DNS resolutions per second per instance: 100 (cannot be increased)
- Maximum packets per second per instance: 80,000
- Maximum bits per second per instance: 100,000,000

## Scalability

Firebase invoked by HTTP scale up quickly to handle incoming traffic,
while background functions scale more gradually. A function's ability to scale
up is dictated by a few factors, including:

- The amount of time it takes for a function's execution to complete (short-running functions can generally scale up to handle more concurrent requests).
- The amount of time it takes for a function to initialize on [cold start](https://firebase.google.com/docs/functions/tips#use_dependencies_wisely).
- Your function's error rate.
- Transient factors, such as regional load and data center capacity.

Background functions have additional limits, as explained below. These limits do not apply to 1st gen [HTTP functions](https://firebase.google.com/docs/functions/http-events).

<br />

### Additional quotas for background functions

| Quota | Description | Limit | Can be increased | Scope | Product version |
|---|---|---|---|---|---|
| Max concurrent invocations | The maximum concurrent invocations of a single function **Example:** if handling each event takes 100 seconds, the invocation rate will be limited to 30 per second on average | 3,000 | Yes | per function | 1st gen only |
| Max invocation rate | The maximum rate of events being handled by a single function **Example:** if handling an event takes 100ms, the invocation rate will be limited to 1000 per second even if only 100 requests, on average, are handled in parallel | 1000 per second | No | per function | 1st gen only |
| Max concurrent event data size | The maximum total size of incoming events to concurrent invocations of a single function **Example:** if events are of size 1MB and processing them takes 10 seconds, the average rate will be 1 event per second, because the 11th event will not be processed until processing one of the first 10 events finishes | 10MB | No | per function | 1st gen and 2nd gen |
| Max throughput of incoming events | The maximum throughput of incoming events to a single function **Example:** if events are of size 1MB, then the invocation rate can be maximum 10 per second, even if functions finish within 100ms | 10MB per second | No | per function | 1st gen and 2nd gen |

## When you reach a quota limit

When a function consumes all of an allocated resource, the resource becomes
unavailable until the quota is refreshed or increased. This may mean that your
function and all other functions in the same project will not work until then.
A function returns an HTTP 500 error code when one of the resources is
over quota and the function cannot execute.

To increase quotas above the defaults listed here, go to the
[Firebase Quotas page](https://console.cloud.google.com/iam-admin/quotas?service=cloudfunctions.googleapis.com&usage=ALL&project=_), select the quotas you want to modify, click
**Edit quotas**, supply your user information if prompted, and enter the new
quota limit for each quota you selected.

## Quota limits for Firebase CLI deployment

For each function that the Firebase CLI deploys, these types of
rate and time limits are affected:

- API calls (READ) - 1 call per deployment, no matter how many functions
  - Limit: 5000 per 100 seconds
- API calls (WRITE) - 1 call per function
  - Limit: 80 per 100 seconds

See also the [Firebase CLI reference](https://firebase.google.com/docs/cli#deployment).