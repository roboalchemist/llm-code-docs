# Source: https://trigger.dev/docs/runs.md

# Runs

> Understanding the lifecycle of task run execution in Trigger.dev

In Trigger.dev, the concepts of runs and attempts are fundamental to understanding how tasks are executed and managed. This article explains these concepts in detail and provides insights into the various states a run can go through during its lifecycle.

## What are runs?

A run is created when you trigger a task (e.g. calling `yourTask.trigger({ foo: "bar" })`). It represents a single instance of a task being executed and contains the following key information:

* A unique run ID
* The current status of the run
* The payload (input data) for the task
* Lots of other metadata

## The run lifecycle

A run can go through **various** states during its lifecycle. The following diagram illustrates a typical state transition where a single run is triggered and completes successfully:

<img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-lifecycle.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=a8936884740688be9f52dd5d7356fb44" alt="Run Lifecycle" data-og-width="1430" width="1430" data-og-height="549" height="549" data-path="images/run-lifecycle.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-lifecycle.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=3af5089f036381cbacc1749c212eb0f4 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-lifecycle.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=cace40b5bbab66d38031fed3e28a9182 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-lifecycle.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=f177c420bee7020b3a0e0e4ff73a1ee0 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-lifecycle.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=cba5c92e5b76a9651c89376826b1b34c 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-lifecycle.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=74a0627ced1962111e7b78debaa3bcb8 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-lifecycle.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=7850d8f28313b615293b27dc6d4bf428 2500w" />

Runs can also find themselves in lots of other states depending on what's happening at any given time. The following sections describe all the possible states in more detail.

### Initial states

<Icon icon="rectangle-history" iconType="solid" color="#FBBF24" size={17} /> **Pending version**:
The task is waiting for a version update because it cannot execute without additional information (task, queue, etc.).

<Icon icon="clock" iconType="solid" color="#878C99" size={17} /> **Delayed**: When a run is triggered
with a delay, it enters this state until the specified delay period has passed.

<Icon icon="rectangle-history" iconType="solid" color="#878C99" size={17} /> **Queued**: The run is ready
to be executed and is waiting in the queue.

<Icon icon="rectangle-history" iconType="solid" color="#878C99" size={17} /> **Dequeued**: The task has been dequeued and is being sent to a worker to start executing.

### Execution states

<Icon icon="spinner-third" iconType="duotone" color="#3B82F6" size={17} /> **Executing**: The task is
currently being executed by a worker.

<Icon icon="hourglass" iconType="solid" color="#878C99" size={17} /> **Waiting**: You have used a
[triggerAndWait()](/triggering#yourtask-triggerandwait), [batchTriggerAndWait()](/triggering#yourtask-batchtriggerandwait) or a [wait function](/wait). When the wait is complete, the task will resume execution.

### Final states

<Icon icon="circle-check" iconType="solid" color="#28BF5C" size={17} /> **Completed**: The task has successfully
finished execution.

<Icon icon="ban" iconType="solid" color="#878C99" size={17} /> **Canceled**: The run was manually canceled
by the user.

<Icon icon="circle-xmark" iconType="solid" color="#E11D48" size={17} /> **Failed**: The task has failed
to complete successfully due to an error in the task code.

<Icon icon="alarm-exclamation" iconType="solid" color="#E11D48" size={17} /> **Timed out**: Task has
failed because it exceeded its `maxDuration`.

<Icon icon="fire" iconType="solid" color="#E11D48" size={17} /> **Crashed**: The worker process crashed
during execution (likely due to an Out of Memory error) and won’t be retried.

<Icon icon="bug" iconType="solid" color="#E11D48" size={17} /> **System failure**: An unrecoverable system
error has occurred.

<Icon icon="trash-can" iconType="solid" color="#878C99" size={17} /> **Expired**: The run's [Time-to-Live](#time-to-live-ttl)
(TTL) has passed before it could start executing.

## Attempts

An attempt represents a single execution of a task within a run. A run can have one or more attempts, depending on the task's retry settings and whether it fails. Each attempt has:

* A unique attempt ID
* A status
* An output (if successful) or an error (if failed)

When a task fails, it will be retried according to its retry settings, creating new attempts until it either succeeds or reaches the retry limit.

<img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-retries.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=520a05470d031b8117b2780405964153" alt="Run with retries" data-og-width="1430" width="1430" data-og-height="585" height="585" data-path="images/run-with-retries.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-retries.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=f9d43bd7b37a9fffaa342cc4d05bb89a 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-retries.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=ace34edfe0154bcff7c2555e6ae3bf83 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-retries.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=a3a7478cfd71ede3194dd2ae2226ac12 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-retries.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=2dd91c524cf54fe9c6b3960afb7e3ad6 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-retries.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=8a2680c03a1515e3f25ac1f36bc25377 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-retries.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=6c0a8c1b610d5befaf82b583e2adcedf 2500w" />

## Run completion

A run is considered finished when:

1. The last attempt succeeds, or
2. The task has reached its retry limit and all attempts have failed

At this point, the run will have either an output (if successful) or an error (if failed).

## Boolean helpers

Run objects returned from the API and Realtime include convenient boolean helper methods to check the run's status:

```ts  theme={null}
import { runs } from "@trigger.dev/sdk";

const run = await runs.retrieve("run_1234");

if (run.isCompleted) {
  console.log("Run completed successfully");
}
```

* **`isQueued`**: Returns `true` when the status is `QUEUED`, `PENDING_VERSION`, or `DELAYED`
* **`isExecuting`**: Returns `true` when the status is `EXECUTING` or `DEQUEUED`. These count against your concurrency limits.
* **`isWaiting`**: Returns `true` when the status is `WAITING`. These do not count against your concurrency limits.
* **`isCompleted`**: Returns `true` when the status is any of the completed statuses
* **`isCanceled`**: Returns `true` when the status is `CANCELED`
* **`isFailed`**: Returns `true` when the status is any of the failed statuses
* **`isSuccess`**: Returns `true` when the status is `COMPLETED`

These helpers are also available when subscribing to Realtime run updates:

```ts  theme={null}
import { runs } from "@trigger.dev/sdk";

for await (const run of runs.subscribeToRun("run_1234")) {
  if (run.isCompleted) {
    console.log("Run completed successfully!");
    break;
  }
}
```

## Advanced run features

### Idempotency Keys

When triggering a task, you can provide an idempotency key to ensure the task is executed only once, even if triggered multiple times. This is useful for preventing duplicate executions in distributed systems.

```ts  theme={null}
await yourTask.trigger({ foo: "bar" }, { idempotencyKey: "unique-key" });
```

* If a run with the same idempotency key is already in progress, the new trigger will be ignored.
* If the run has already finished, the previous output or error will be returned.

See our [Idempotency docs](/idempotency) for more information.

### Canceling runs

You can cancel an in-progress run using the API or the dashboard:

```ts  theme={null}
await runs.cancel(runId);
```

When a run is canceled:

– The task execution is stopped

– The run is marked as canceled

– The task will not be retried

– Any in-progress child runs are also canceled

### Time-to-live (TTL)

TTL is a time-to-live setting that defines the maximum duration a run can remain in a queued state before being automatically expired. You can set a TTL when triggering a run:

```ts  theme={null}
await yourTask.trigger({ foo: "bar" }, { ttl: "10m" });
```

If the run hasn't started within the specified TTL, it will automatically expire, returning the status `Expired`. This is useful for time-sensitive tasks where immediate execution is important. For example, when you queue many runs simultaneously and exceed your concurrency limits, some runs might be delayed - using TTL ensures they only execute if they can start within your specified timeframe.

Note that dev runs automatically have a 10-minute TTL. In Staging and Production environments, no TTL is set by default.

<img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-ttl.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=2a3663f4cf4d7c4249c5c82f54859a76" alt="Run with TTL" data-og-width="1406" width="1406" data-og-height="453" height="453" data-path="images/run-with-ttl.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-ttl.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=c596effb593c6533723019ba62d72cf9 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-ttl.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=fd441b76d258f5d8ad83b17a42dfeb1c 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-ttl.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=a1ba26b44a1b1fb0822eb7142aaf69ef 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-ttl.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=477990ac794bc64d536becff619cdd81 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-ttl.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=56720e4a594907f52dabc475dd663b03 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-ttl.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=f3c577f8ef1ee2bcb22bf66259d88869 2500w" />

### Delayed runs

You can schedule a run to start after a specified delay:

```ts  theme={null}
await yourTask.trigger({ foo: "bar" }, { delay: "1h" });
```

This is useful for tasks that need to be executed at a specific time in the future.

<img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-delay.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=fe68bf64bab17c12f0c1c532bdb48ab4" alt="Run with delay" data-og-width="1430" width="1430" data-og-height="581" height="581" data-path="images/run-with-delay.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-delay.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=e185434d9cd2a26155dee5ac5e94f370 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-delay.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=829277bb21bc824019d68fc8f755ce2c 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-delay.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=7e88e6325a8559caca3c76a573f5523c 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-delay.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=ce7e12e3199088a1c7316918bb6fb3a7 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-delay.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=0cf1c7ecc525f8f8f5c4550cdd463df3 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-delay.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=03fc83ca451c8b58faf1c79c34bdface 2500w" />

### Replaying runs

You can create a new run with the same payload as a previous run:

```ts  theme={null}
await runs.replay(runId);
```

This is useful for re-running a task with the same input, especially for debugging or recovering from failures. The new run will use the latest version of the task.

You can also replay runs from the dashboard using the same or different payload. Learn how to do this [here](/replaying).

### Waiting for runs

#### triggerAndWait()

The `triggerAndWait()` function triggers a task and then lets you wait for the result before continuing. [Learn more about triggerAndWait()](/triggering#yourtask-triggerandwait).

<img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-triggerAndWait().png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=b7175cd727983b76dc998fa76cdc7279" alt="Run with triggerAndWait" data-og-width="1617" width="1617" data-og-height="735" height="735" data-path="images/run-with-triggerAndWait().png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-triggerAndWait().png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=b6c6add3e9f09f52eb4b63e1e723175a 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-triggerAndWait().png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=6d78b248fdc52ef7833f4ba71713b3f0 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-triggerAndWait().png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=0f69ee104ab1e7afb9fde3d69b9b6d7a 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-triggerAndWait().png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=292ec187be08fefd76f30c3a768b7449 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-triggerAndWait().png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=c3cedaa32be6515ab9738df67c87276a 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-triggerAndWait().png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=c8e309d749162c08006a9baca616ef74 2500w" />

#### batchTriggerAndWait()

Similar to `triggerAndWait()`, the `batchTriggerAndWait()` function lets you batch trigger a task and wait for all the results [Learn more about batchTriggerAndWait()](/triggering#yourtask-batchtriggerandwait).

<img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-batchTriggerAndWait().png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=26974085e23f5dd55ea301234b477655" alt="Run with batchTriggerAndWait" data-og-width="1617" width="1617" data-og-height="940" height="940" data-path="images/run-with-batchTriggerAndWait().png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-batchTriggerAndWait().png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=96d696e99dec5085efd8327dce107618 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-batchTriggerAndWait().png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=8c926544b58cd261021928eeda461bf4 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-batchTriggerAndWait().png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=8f412df861d962ccaba445a95971daca 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-batchTriggerAndWait().png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=e590ab7550353f53a6e3b62972c38771 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-batchTriggerAndWait().png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=cc03c2493a62ae36b30ecad5ce3889ab 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-with-batchTriggerAndWait().png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=7863f7505ba010ae2b1f0f998f57cf35 2500w" />

### Runs API

#### runs.list()

List runs in a specific environment. You can filter the runs by status, created at, task identifier, version, and more:

```ts  theme={null}
import { runs } from "@trigger.dev/sdk";

// Get the first page of runs, returning up to 20 runs
let page = await runs.list({ limit: 20 });

for (const run of page.data) {
  console.log(run);
}

// Keep getting the next page until there are no more runs
while (page.hasNextPage()) {
  page = await page.getNextPage();
  // Do something with the next page of runs
}
```

You can also use an Async Iterator to get all runs:

```ts  theme={null}
import { runs } from "@trigger.dev/sdk";

for await (const run of runs.list({ limit: 20 })) {
  console.log(run);
}
```

You can provide multiple filters to the `list()` function to narrow down the results:

```ts  theme={null}
import { runs } from "@trigger.dev/sdk";

const response = await runs.list({
  status: ["QUEUED", "EXECUTING"], // Filter by status
  taskIdentifier: ["my-task", "my-other-task"], // Filter by task identifier
  from: new Date("2024-04-01T00:00:00Z"), // Filter by created at
  to: new Date(),
  version: "20241127.2", // Filter by deployment version,
  tag: ["tag1", "tag2"], // Filter by tags
  batch: "batch_1234", // Filter by batch ID
  schedule: "sched_1234", // Filter by schedule ID
});
```

#### runs.retrieve()

Fetch a single run by it's ID:

```ts  theme={null}
import { runs } from "@trigger.dev/sdk";

const run = await runs.retrieve(runId);
```

You can provide the type of the task to correctly type the `run.payload` and `run.output`:

```ts  theme={null}
import { runs } from "@trigger.dev/sdk";
import type { myTask } from "./trigger/myTask";

const run = await runs.retrieve<typeof myTask>(runId);

console.log(run.payload.foo); // string
console.log(run.output.bar); // string
```

If you have just triggered a run, you can pass the entire response object to `retrieve()` and the response will already be typed:

```ts  theme={null}
import { runs, tasks } from "@trigger.dev/sdk";
import type { myTask } from "./trigger/myTask";

const response = await tasks.trigger<typeof myTask>({ foo: "bar" });
const run = await runs.retrieve(response);

console.log(run.payload.foo); // string
console.log(run.output.bar); // string
```

#### runs.cancel()

Cancel a run:

```ts  theme={null}
import { runs } from "@trigger.dev/sdk";

await runs.cancel(runId);
```

#### runs.replay()

Replay a run:

```ts  theme={null}
import { runs } from "@trigger.dev/sdk";

await runs.replay(runId);
```

#### runs.reschedule()

Updates a delayed run with a new delay. Only valid when the run is in the DELAYED state.

```ts  theme={null}
import { runs } from "@trigger.dev/sdk";

await runs.reschedule(runId, { delay: "1h" });
```

### Real-time updates

Subscribe to changes to a specific run in real-time:

```ts  theme={null}
import { runs } from "@trigger.dev/sdk";

for await (const run of runs.subscribeToRun(runId)) {
  console.log(run);
}
```

Similar to `runs.retrieve()`, you can provide the type of the task to correctly type the `run.payload` and `run.output`:

```ts  theme={null}
import { runs } from "@trigger.dev/sdk";
import type { myTask } from "./trigger/myTask";

for await (const run of runs.subscribeToRun<typeof myTask>(runId)) {
  console.log(run.payload.foo); // string
  console.log(run.output?.bar); // string | undefined
}
```

For more on real-time updates, see the [Realtime](/realtime) documentation.

### Triggering runs for undeployed tasks

It's possible to trigger a run for a task that hasn't been deployed yet. The run will enter the "Waiting for deploy" state until the task is deployed. Once deployed, the run will be queued and executed normally.
This feature is particularly useful in CI/CD pipelines where you want to trigger tasks before the deployment is complete.
