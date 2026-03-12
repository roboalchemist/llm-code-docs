# Source: https://pipedream.com/docs/workflows/building-workflows/settings/concurrency-and-throttling.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Concurrency and Throttling

export const MAX_WORKFLOW_QUEUE_SIZE = '10,000';

export const DEFAULT_WORKFLOW_QUEUE_SIZE = '100';

Pipedream makes it easy to manage the concurrency and rate at which events trigger your workflow code using execution controls.

## Overview

Workflows listen for events and execute as soon as they are triggered. While this behavior is expected for many use cases, there can be unintended consequences.

### Concurrency

Without restricting concurrency, events can be processed in parallel and there is no guarantee that they will execute in the order in which they were received. This can cause race conditions.

For example, if two workflow events try to add data to Google Sheets simultaneously, they may both attempt to write data to the same row. As a result, one event can overwrite data from another event. The diagram below illustrates this example — both `Event 1` and `Event 2` attempt to write data to Google Sheets concurrently — as a result, they will both write to the same row and the data for one event will be overwritten and lost (and no error will be thrown).

<Frame>
  <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/b210c2af-image.png?fit=max&auto=format&n=Acz4Z1ch6TM7-aI8&q=85&s=9afb42755a538295b36d98fdd9a2884d" width="1712" height="542" data-path="images/b210c2af-image.png" />
</Frame>

You can avoid race conditions like this by limiting workflow concurrency to a single “worker”. What this means is that only one event will be processed at a time, and the next event will not start processing until the first is complete (unprocessed events will be maintained in a queue and processed by the workflow in order). The following diagram illustrates how the events in the last diagram would executed if concurrency was limited to a single worker.

<Frame>
  <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/8c2db97e-image.png?fit=max&auto=format&n=grEzwYhEB2vZSwGw&q=85&s=4f7491aed260ab8e5127de3b2aa0af97" width="1752" height="536" data-path="images/8c2db97e-image.png" />
</Frame>

While the first example resulted in only two rows of data in Google Sheets, this time data for all three events are recorded to three separate rows.

### Throttling

If your workflow integrates with any APIs, then you may need to limit the rate at which your workflow executes to avoid hitting rate limits from your API provider. Since event-driven workflows are stateless, you can’t manage the rate of execution from within your workflow code. Pipedream’s execution controls solve this problem by allowing you to control the maximum number of times a workflow may be invoked over a specific period of time (e.g., up to 1 event every second).

<Note>
  Pipedream controls the frequency of workflow invocations over a specified time interval using fixed window throttling. For example, if the execution rate limit is set at 1 execution every 5 seconds, this means that your workflow will be invoked no more than once within a fixed 5-second time box. This doesn’t mean that executions will occur 5 seconds apart.
</Note>

## Usage

Events emitted from a source to a workflow are placed in a queue, and Pipedream triggers your workflow with events from the queue based on your concurrency and throttling settings. These settings may be customized per workflow (so the same events may be processed at different rates by different workflows).

<Frame>
  <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/a27eb1fb-image.png?fit=max&auto=format&n=Acz4Z1ch6TM7-aI8&q=85&s=340d660293342541eeb328b13f49e374" width="1670" height="750" data-path="images/a27eb1fb-image.png" />
</Frame>

The maximum number of events Pipedream will queue per workflow depends on your account type.

* Up to 100 events will be queued per workflow for the workspaces on the free tier.
* Workflows owned by paid plans may have custom limits. If you need a larger queue size, [see here](/workflows/building-workflows/settings/concurrency-and-throttling/#increasing-the-queue-size-for-a-workflow).

**IMPORTANT:** If the number of events emitted to a workflow exceeds the queue size, events will be lost. If that happens, you’ll see an error in your workflow, and you’ll receive an error email.

To learn more about how the feature works and technical details, check out our [engineering blog post](https://blog.pipedream.com/concurrency-controls-design/).

### Where Do I Manage Concurrency and Throttling?

Concurrency and throttling can be managed in the **Execution Controls** section of your **Workflow Settings**. Event queues are currently supported for any workflow that is triggered by an event source. Event queues are not currently supported for native workflow triggers (native HTTP, cron, SDK and email).

<Frame>
  <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/79d58ce6-image.png?fit=max&auto=format&n=grEzwYhEB2vZSwGw&q=85&s=d332c127a1edb8ba56622fdebc7b7583" width="398" height="399" data-path="images/79d58ce6-image.png" />
</Frame>

### Managing Event Concurrency

Concurrency controls define how many events can be executed in parallel. To enforce serialized, in-order execution, limit concurrency to `1` worker. This guarantees that each event will only be processed once the execution for the previous event is complete.

To execute events in parallel, increase the number of workers (the number of workers defines the maximum number of concurrent events that may be processed), or disable concurrency controls for unlimited parallelization.

### Throttling Workflow Execution

To throttle workflow execution, enable it in your workflow settings and configure the **limit** and **interval**.

The limit defines how many events (from `0-10000`) to process in a given time period.

The interval defines the time period over which the limit will be enforced. You may specify the time period as a number of seconds, minutes or hours (ranging from `1-10000`)

### Applying Concurrency and Throttling Together

The conditions for both concurrency and throttling must be met in order for a new event to trigger a workflow execution. Here are some examples:

| Concurrency | Throttling           | Result                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Off         | Off                  | Events will trigger your workflow **as soon as they are received**. Events may execute in parallel.                                                                                                                                                                                                                                                                                                                       |
| 1 Worker    | Off                  | Events will trigger your workflow in a **serialized pattern** (a maximum of 1 event will be processed at a time). As soon as one event finishes processing, the next event in the queue will be processed.                                                                                                                                                                                                                |
| 1 Worker    | 1 Event per Second   | Events will trigger your workflow in a **serialized pattern** at a **maximum rate** of 1 event per second. If an event takes *less* than one second to finish processing, the next event in the queue will not being processing until 1 second from the start of the most recently processed event. If an event takes *longer* than one second to process, the next event in the queue will begin processing immediately. |
| 1 Worker    | 10 Events per Minute | Events will trigger your workflow in a **serialized pattern** at a **maximum rate** of 10 events per minute. If an event takes *less* than one minute to finish processing, the next event in the queue immediately begin processing. If 10 events been processed in less than one minute, the remaining events will be queued until 1 minute from the start of the initial event.                                        |
| 5 Workers   | Off                  | Up to 5 events will trigger your workflow in parallel as soon as they are received. If more events arrive while 5 events are being processed, they will be queued and executed in order as soon as an event completes processing.                                                                                                                                                                                         |

### Pausing Workflow Execution

To stop the queue from invoking your workflow, throttle workflow execution and set the limit to `0`.

### Increasing the queue size for a workflow

By default, your workflow can hold up to {DEFAULT_WORKFLOW_QUEUE_SIZE} events in its queue at once. Any events that arrive once the queue is full will be dropped, and you’ll see an [Event Queue Full](/troubleshooting/#event-queue-full) error.

For example, if you serialize the execution of your workflow by setting a concurrency of `1`, but receive 200 events from your workflow’s event source at once, the workflow’s queue can only hold the first 100 events. The last 100 events will be dropped.

Users on [paid tiers](https://pipedream.com/pricing) can increase their queue size up to {MAX_WORKFLOW_QUEUE_SIZE} events for a given workflow, just below the **Concurrency** section of your **Execution Controls** settings:

<Frame>
  <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/427b69e5-image.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=6297eb084edeaba940ac41087cb2b176" width="710" height="258" data-path="images/427b69e5-image.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).
