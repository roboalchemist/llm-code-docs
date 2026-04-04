# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.taskqueueoptions.md.txt

**Signature:**

<br />

    export interface TaskQueueOptions extends options.GlobalOptions 

**Extends:** options.[GlobalOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptions_interface)

## Properties

|                                                                            Property                                                                            |               Type                |                                                                                   Description                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [invoker](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.taskqueueoptions.md#httpstaskqueueoptionsinvoker)         | 'private' \| string \| string\[\] | Who can enqueue tasks for this function. If left unspecified, only service accounts which have roles/cloudtasks.enqueuer and roles/cloudfunctions.invoker will have permissions. |
| [rateLimits](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.taskqueueoptions.md#httpstaskqueueoptionsratelimits)   | TaskRateLimits                    |                                                                                                                                                                                  |
| [retryConfig](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.taskqueueoptions.md#httpstaskqueueoptionsretryconfig) | TaskRetryConfig                   |                                                                                                                                                                                  |

## https.TaskQueueOptions.invoker

Who can enqueue tasks for this function. If left unspecified, only service accounts which have roles/cloudtasks.enqueuer and roles/cloudfunctions.invoker will have permissions.

**Signature:**  

    invoker?: 'private' | string | string[];

## https.TaskQueueOptions.rateLimits

**Signature:**  

    rateLimits?: TaskRateLimits;

## https.TaskQueueOptions.retryConfig

**Signature:**  

    retryConfig?: TaskRetryConfig;