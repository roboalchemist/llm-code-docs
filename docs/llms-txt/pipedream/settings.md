# Source: https://pipedream.com/docs/workflows/building-workflows/settings.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Settings

export const WARM_WORKERS_CREDITS_PER_INTERVAL = '5';

export const WARM_WORKERS_INTERVAL = '10 minutes';

export const MEMORY_ABSOLUTE_LIMIT = '10GB';

export const MEMORY_LIMIT = '256MB';

You can control workflow-specific settings in your workflow’s **Settings**:

1. Visit your workflow
2. Click on Workflow Settings on the top left:

<Frame>
  <img src="https://res.cloudinary.com/pipedreamin/image/upload/v1710510858/docs/workflows/building-workflows/settings/CleanShot_2024-03-15_at_09.53.34_sqkcse.gif" />
</Frame>

<Note>
  You can also open the workflow settings using `CMD` + `,` on Mac, or `Ctrl` + `,` on Windows.
</Note>

## Enable Workflow

If you’d like to pause your workflow from executing completely, you can disable it or re-enable it here.

## Error Handling

By default, you’ll receive notifications when your workflow throws an unhandled error. See the [error docs](/workflows/building-workflows/errors/) for more detail on these notifications.

You can disable these notifications for your workflow by disabling the **Notify me on errors** toggle:

<Frame>
  <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/40fa3a1f-Screen_Shot_2022-06-30_at_4.30.44_PM_oauty4.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=4f18d96290e23ac19d8bda915d9ad4a8" width="370" height="166" data-path="images/40fa3a1f-Screen_Shot_2022-06-30_at_4.30.44_PM_oauty4.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/40fa3a1f-Screen_Shot_2022-06-30_at_4.30.44_PM_oauty4.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=4f18d96290e23ac19d8bda915d9ad4a8" width="370" height="166" data-path="images/40fa3a1f-Screen_Shot_2022-06-30_at_4.30.44_PM_oauty4.png" />
</Frame>

## Auto-retry Errors

<Note>
  **Out of Memory and Timeout Errors**

  Pipedream will not automatically retry if an execution fails due to an Out of Memory (OOM) error or a timeout. If you encounter these errors frequently, consider increasing the configuration settings for your workflow.
</Note>

Customers on the [Advanced Plan](https://pipedream.com/pricing) can automatically retry workflows on errors. If any step in your workflow throws an error, Pipedream will retry the workflow from that failed step, re-rerunning the step up to 8 times over a 10 hour span with an [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff) strategy.

On error, the step will export a `$summary` property that tells you how many times the step has been retried, and an `$attempt` object with the following properties:

1. `error` — All the details of the error the step threw — the error, the stack, etc.
2. `cancel_url` — You can call this URL to cancel the retry
3. `rerun_url` — You can call this URL to proceed with the execution immediately
4. `resume_ts` — An ISO 8601 timestamp that tells you the timestamp of the next retry

<Frame>
  <img src="https://mintcdn.com/pipedream/nKh6d_6A4aXFb6xD/images/f074d2e5-Screen_Shot_2023-02-22_at_6.29.08_PM_ssnzsi.png?fit=max&auto=format&n=nKh6d_6A4aXFb6xD&q=85&s=698e20c9842cdd1a852044d5ab90d700" width="1788" height="754" data-path="images/f074d2e5-Screen_Shot_2023-02-22_at_6.29.08_PM_ssnzsi.png" />
</Frame>

If the step execution succeeds during any retry, the execution will proceed to the next step of the workflow.

If the step fails on all 8 retries and throws a final error, you’ll receive [an error notification](/workflows/building-workflows/errors/) through your standard notification channel.

### Send error notifications on the first error

By default, if a step fails on all 8 retries, and throws a final error, you’ll receive [an error notification](/workflows/building-workflows/errors/) through your standard notification channel. But sometimes you need to investigate errors as soon as they happen. If you’re connecting to your database, and receive an error that the DB is down, you may want to investigate that immediately.

On any workflow with auto-retry enabled, you can optionally choose to **Send notification on first error**. This is disabled by default so you don’t get emails for transient errors, but you can enable for critical workflows where you want visibility into all errors.

For custom control over error handling, you can implement error logic in code steps (e.g. `try` / `catch` statements in Node.js code), or [create your own custom error workflow](/workflows/building-workflows/errors/#handle-errors-with-custom-logic).

## Data Retention Controls

By default, Pipedream stores exports, logs, and other data tied to workflow executions. You can view these logs in two places:

1. [The workflow inspector](/workflows/building-workflows/inspect/#the-inspector)
2. [Event History](/workflows/event-history/)

But if you’re processing sensitive data, you may not want to store those logs. You can **Disable data retention** in your workflow settings to disable **all** logging. Since Pipedream stores no workflow logs with this setting enabled, you’ll see no logs in the inspector or event history UI.

<Frame>
  <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/a6ee1e54-image.png?fit=max&auto=format&n=Acz4Z1ch6TM7-aI8&q=85&s=4736195aa2e48782f65b047feb8efee6" width="1184" height="650" data-path="images/a6ee1e54-image.png" />
</Frame>

Refer to our [pricing page](https://pipedream.com/pricing) to understand the latest limits based on your plan.

### Constraints

* **Data Retention Controls do not apply to sources**: Even with data retention disabled on your workflow, Pipedream will still log inbound events for the source.
* **No events will be shown in the UI**: When data retention is disabled for your workflow, the Pipedream UI will not show any new events in the inspector or Event History for that workflow.

<Note>
  **Avoid surfacing events in the builder**

  Even with data retention disabled on your workflow, the builder will still surface inbound events when in build mode. To avoid surfacing potentially sensitive data here as well, refer to [these docs](/workflows/building-workflows/triggers/#pipedream-specific-request-parameters).
</Note>

## Execution Controls

### Execution Timeout Limit

Workflows have a default [execution limit](/workflows/limits/#time-per-execution), which defines the time the workflow can run for a single execution until it’s timed out.

If your workflow times out, and needs to run for longer than the [default limit](/workflows/limits/#time-per-execution), you can change that limit here.

### Memory

By default, workflows run with {MEMORY_LIMIT} of memory. If you’re processing a lot of data in memory, you might need to raise that limit. Here, you can increase the memory of your workflow up to {MEMORY_ABSOLUTE_LIMIT}.

Increasing your workflow’s memory gives you a proportional increase in CPU, so increasing your workflow’s memory can reduce its overall runtime and make it more performant.

<Note>
  **How can my workflow run faster?**

  See [our guide on running workflows faster](/troubleshooting/#how-can-my-workflow-run-faster).
</Note>

**Pipedream charges credits proportional to your memory configuration**. When you modify your memory settings, Pipedream will show you the number of credits you’ll be charged per execution. [Read more here](/pricing/faq/#how-does-workflow-memory-affect-credits).

### Concurrency and Throttling

[Manage the concurrency and rate](/workflows/building-workflows/settings/concurrency-and-throttling/) at which events from a source trigger your workflow code.

## Eliminate cold starts

A **cold start** refers to the delay between the invocation of workflow and the execution of the workflow code. Cold starts happen when Pipedream spins up a new [execution environment](/privacy-and-security/#execution-environment) to handle incoming events.

Specifically, cold starts occur on the first request to your workflow after a period of inactivity (roughly 5 minutes), or if your initial worker is already busy and a new worker needs to be initialized. In these cases, Pipedream creates a new execution environment to process your event. **Initializing this environment takes a few seconds, which delays the execution of this first event**.

You can reduce cold starts by configuring a number of dedicated **workers**:

1. Visit your workflow’s **Settings**
2. Under **Execution Controls**, select the toggle to **Eliminate cold starts**
3. Configure [the appropriate number of workers](/workflows/building-workflows/settings/#how-many-workers-should-i-configure) for your use case

<Frame>
  <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/33d59c4a-Screenshot_2023-06-06_at_12.24.03_PM_zctp50.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=9e81283c1a3bed6ee6e0cf78292baa20" width="1204" height="264" data-path="images/33d59c4a-Screenshot_2023-06-06_at_12.24.03_PM_zctp50.png" />
</Frame>

When you configure workers for a specific workflow, Pipedream initializes dedicated workers — virtual machines that run Pipedream’s [execution environment](/privacy-and-security/#execution-environment). [It can take a few minutes](/workflows/building-workflows/settings/#how-long-does-it-take-to-spin-up-a-dedicated-worker) for new dedicated workers to deploy. Once deployed, these workers are available at all times to respond to workflow executions, with no cold starts.

<Warning>
  You may need to configure [multiple dedicated workers](/workflows/building-workflows/settings/#how-many-workers-should-i-configure) to handle multiple, concurrent requests.

  Pipedream also performs some initialization operations on new workflow runs, so you may still observe a small startup time (typically around 50ms per workflow step) on dedicated workers.
</Warning>

### When should I configure dedicated workers?

You should configure dedicated workers when you need to process requests as soon as possible, with no latency.

For example, you may build an HTTP-triggered workflow that returns a synchronous HTTP response to a user, without delay. Or you may be building a Slack bot and need to respond to Slack’s webhook within a few seconds. Since these workflows need to respond quickly, they’re good cases to use dedicated workers.

### How many workers should I configure?

Incoming requests are handled by a single worker, one at a time. If you only receive one request a minute, and the workflow finishes execution in a few seconds, you may only need one worker.

But you might have a higher-volume app that receives two concurrent requests. In that case, Pipedream spins up **two** workers to handle each request.

For many user-facing (even internal) applications, the number of requests over time can be modeled with a [Poisson distrubution](https://en.wikipedia.org/wiki/Poisson_distribution). You can use that distribution to estimate the number of workers you need at an average time, or set it higher if you want to ensure a specific percentage of requests hit a dedicated worker. You can also save a record of all workflow runs to your own database, with the timestamp they ran ([see `steps.trigger.context.ts`](/workflows/building-workflows/triggers/#stepstriggercontext)), and look at your own pattern of requests, to compute the optimal number of workers.

### Do compute budgets apply to dedicated workers?

No, compute budgets do not apply to dedicated workers, they only apply to credits incurred by compute from running workflows, sources, etc.

### How long does it take to spin up a dedicated worker?

It can take 5-10 minutes for Pipedream to fully configure a new dedicated worker. Before that time, you may still observe cold starts with new incoming requests.

### Pricing for dedicated workers

You’re charged {WARM_WORKERS_CREDITS_PER_INTERVAL} credits for every {WARM_WORKERS_INTERVAL} a dedicated worker is live, per worker, per {MEMORY_LIMIT} memory. You can view the credits used by dedicated workers [in your billing settings](https://pipedream.com/settings/billing):

<Frame>
  <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/91aa1910-Screenshot_2023-06-05_at_6.26.53_PM_stlljl.png?fit=max&auto=format&n=grEzwYhEB2vZSwGw&q=85&s=4ca2a2ebe134ea77f4f8caa4ffa58b96" width="1044" height="400" data-path="images/91aa1910-Screenshot_2023-06-05_at_6.26.53_PM_stlljl.png" />
</Frame>

For example, if you run a single dedicated worker for 24 hours, that would cost 720 credits:

```python  theme={null}
5 credits per 10 min
* 6 10-min periods per hour
* 24 hours
= 720 credits
```

{WARM_WORKERS_INTERVAL} is the *minimum* interval that Pipedream charges for usage. If you have a dedicated worker live for 1 minute, Pipedream will still charge {WARM_WORKERS_CREDITS_PER_INTERVAL} credits.

Additionally, any change to dedicated worker configuration, (including worklow deploys) will result in an extra {WARM_WORKERS_CREDITS_PER_INTERVAL} credits of usage.

<Frame>
  <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/18b7c0f7-Screenshot_2023-06-06_at_12.23.03_PM_mpsqek.png?fit=max&auto=format&n=NF77kliJSewMqg65&q=85&s=c0cde9793b606c38b6710ef6c339ad9b" width="3016" height="1476" data-path="images/18b7c0f7-Screenshot_2023-06-06_at_12.23.03_PM_mpsqek.png" />
</Frame>

### Limits

Each attachment is limited to `25MB` in size. The total size of all attachments within a single workflow cannot exceed `200MB`.

Built with [Mintlify](https://mintlify.com).
