# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueueoptions.md.txt

# tasks.TaskQueueOptions interface

Options for configuring the task queue to listen to.

**Signature:**

    export interface TaskQueueOptions 

## Properties

| Property | Type | Description |
|---|---|---|
| [invoker](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionsinvoker) | "private" \| string \| string\[\] | Who can enqueue tasks for this function. If left unspecified, only service accounts which have `roles/cloudtasks.enqueuer` and `roles/cloudfunctions.invoker` will have permissions. |
| [rateLimits](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionsratelimits) | [RateLimits](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.ratelimits.md#tasksratelimits_interface) | How congestion control should be applied to the function. |
| [retryConfig](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionsretryconfig) | [RetryConfig](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.retryconfig.md#tasksretryconfig_interface) | How a task should be retried in the event of a non-2xx return. |

## tasks.TaskQueueOptions.invoker

Who can enqueue tasks for this function. If left unspecified, only service accounts which have `roles/cloudtasks.enqueuer` and `roles/cloudfunctions.invoker` will have permissions.

**Signature:**

    invoker?: "private" | string | string[];

## tasks.TaskQueueOptions.rateLimits

How congestion control should be applied to the function.

**Signature:**

    rateLimits?: RateLimits;

## tasks.TaskQueueOptions.retryConfig

How a task should be retried in the event of a non-2xx return.

**Signature:**

    retryConfig?: RetryConfig;