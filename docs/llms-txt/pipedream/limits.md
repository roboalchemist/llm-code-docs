# Source: https://pipedream.com/docs/workflows/limits.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Limits

export const MAX_WORKFLOW_EXECUTION_LIMIT = '750';

export const FREE_INSPECTOR_EVENT_LIMIT = '7 days of events';

export const TMP_SIZE_LIMIT = '2GB';

export const FUNCTION_PAYLOAD_LIMIT = '6MB';

export const INSPECTOR_EVENT_EXPIRY_DAYS = '365';

export const DAILY_TESTING_LIMIT = '30 minutes';

export const EMAIL_PAYLOAD_SIZE_LIMIT = '30MB';

export const MEMORY_ABSOLUTE_LIMIT = '10GB';

export const MEMORY_LIMIT = '256MB';

export const PAYLOAD_SIZE_LIMIT = '512KB';

Pipedream imposes limits on source and workflow execution, the events you send to Pipedream, and other properties. You’ll receive an error if you encounter these limits. See our [troubleshooting guide](/troubleshooting/) for more information on these specific errors.

Some of these limits apply only on the free tier. For example, Pipedream limits the number of credits and active workflows you can use on the free tier. **On paid tiers, you can run an unlimited number of credits for any amount of execution time (usage charges apply)**.

Other limits apply across the free and paid tiers. Please see the details on each limit below.

**These limits are subject to change at any time**.

## Number of Workflows

The limit of active workflows depends on your current plan. [See our pricing page](https://pipedream.com/pricing) for more details.

## Number of Event Sources

**You can run an unlimited number of event sources**, as long as each operates under the limits below.

## Execution Credits

Free Pipedream account have a limit on the number of execution credits. Paid plans are not capped but are subject to additional usage charges (you can manually set a usage cap if you want to manage costs).\
\
You can view your credits usage at the bottom-left of [the Pipedream UI](https://pipedream.com).

You can also see more detailed usage in [Billing and Usage Settings](https://pipedream.com/settings/billing). Here you’ll find your usage for the last 30 days, broken out by day, by resource (e.g. your source / workflow).

### Included Credits Usage Notifications

| Tier       | Notifications                                                                                                                                       |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Free tiers | You’ll receive an email when you reach 100% of your usage.                                                                                          |
| Paid tiers | You’ll receive an email at 80% and 100% of your [included credits](/pricing/#included-credits) for your [billing period](/pricing/#billing-period). |

## Daily workflow testing limit

You **do not** use credits testing workflows, but workspaces on the **Free** plan are limited to {MAX_WORKFLOW_EXECUTION_LIMIT} of test runtime per day. If you exceed this limit when testing in the builder, you’ll see a **Runtime Quota Exceeded** error.

## Data stores

Depending on your plan, Pipedream sets limits on:

1. The total number of data stores
2. The total number of keys across all data stores
3. The total storage used across all data stores

You’ll find your workspace’s limits in the **Data Stores** section of usage dashboard in the bottom-left of [the Pipedream UI](https://pipedream.com).

<Frame>
  <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/54ca2228-image_ryjbrh.png?fit=max&auto=format&n=anb6FA0wpd8jtdUB&q=85&s=9ebcd956b1be14fd3c1e503de18618f5" width="410" height="572" data-path="images/54ca2228-image_ryjbrh.png" />
</Frame>

## HTTP Triggers

The following limits apply to [HTTP triggers](/workflows/building-workflows/triggers/#http).

### HTTP Request Body Size

By default, the body of HTTP requests sent to a source or workflow is limited to {PAYLOAD_SIZE_LIMIT}.

Your endpoint will issue a `413 Payload Too Large` status code when the body of your request exceeds {PAYLOAD_SIZE_LIMIT}.

**Pipedream supports two different ways to bypass this limit**. Both of these interfaces support uploading data up to `5TB`, though you may encounter other platform limits.

* You can send large HTTP payloads by passing the `pipedream_upload_body=1` query string or an `x-pd-upload-body: 1` HTTP header in your HTTP request. [Read more here](/workflows/building-workflows/triggers/#sending-large-payloads).
* You can upload multiple large files, like images and videos, using the [large file upload interface](/workflows/building-workflows/triggers/#large-file-support).

### QPS (Queries Per Second)

Generally the rate of HTTP requests sent to an endpoint is quantified by QPS, or *queries per second*. A query refers to an HTTP request.

**You can send an average of 10 requests per second to your HTTP trigger**. Any requests that exceed that threshold may trigger rate limiting. If you’re rate limited, we’ll return a `429 Too Many Requests` response. If you control the application sending requests, you should retry the request with [exponential backoff](https://cloud.google.com/storage/exponential-backoff) or a similar technique.

We’ll also accept short bursts of traffic, as long as you remain close to an average of 10 QPS (e.g. sending a batch of 50 requests every 30 seconds should not trigger rate limiting).

**This limit can be raised for paying customers**. To request an increase, [reach out to our Support team](https://pipedream.com/support/) with the HTTP endpoint whose QPS you’d like to increase, with the new, desired limit.

## Email Triggers

Currently, most of the [limits that apply to HTTP triggers](/workflows/limits/#http-triggers) also apply to [email triggers](/workflows/building-workflows/triggers/#email).

The only limit that differs between email and HTTP triggers is the payload size: the total size of an email sent to a workflow - its body, headers, and attachments - is limited to {EMAIL_PAYLOAD_SIZE_LIMIT}.

## Memory

By default, workflows run with {MEMORY_LIMIT} of memory. You can modify a workflow’s memory [in your workflow’s Settings](/workflows/building-workflows/settings/#memory), up to {MEMORY_ABSOLUTE_LIMIT}.

Increasing your workflow’s memory gives you a proportional increase in CPU. If your workflow is limited by memory or compute, increasing your workflow’s memory can reduce its overall runtime and make it more performant.

**Pipedream charges credits proportional to your memory configuration**. [Read more here](/pricing/faq/#how-does-workflow-memory-affect-credits).

## Disk

Your code, or a third party library, may need access to disk during the execution of your workflow or event source. **You have access to {TMP_SIZE_LIMIT} of disk in the `/tmp` directory**.

This limit cannot be raised.

## Workflows

### Time per execution

Every event sent to a workflow triggers a new execution of that workflow. Workflows have a default execution limit that varies with the trigger type:

* HTTP and Email-triggered workflows default to **30 seconds** per execution.
* Cron-triggered workflows default to **60 seconds** per execution.

If your code exceeds your workflow-level limit, we’ll throw a **Timeout** error and stop your workflow. Any partial logs and observability associated with code cells that ran successfully before the timeout will be attached to the event in the UI, so you can examine the state of your workflow and troubleshoot where it may have failed.

You can increase the timeout limit, up to a max value set by your plan:

| Tier       | Maximum time per execution |
| ---------- | -------------------------- |
| Free tiers | 300 seconds (5 min)        |
| Paid tiers | 750 seconds (12.5 min)     |

Events that trigger a **Timeout** error will appear in red in the [Inspector](/workflows/building-workflows/inspect/). You’ll see the timeout error, also in red, in the cell at which the code timed out.

### Event History

The [Inspector](/workflows/building-workflows/inspect/#the-inspector) shows the execution history for a given workflow. Events have a limited retention period, depending on your plan:

| Tier       | Events retained per workflow                                                     |
| ---------- | -------------------------------------------------------------------------------- |
| Free tiers | {FREE_INSPECTOR_EVENT_LIMIT}                                                     |
| Paid tiers | [View breakdown of events history per paid plan](https://pipedream.com/pricing/) |

The execution details for a specific event also expires after {INSPECTOR_EVENT_EXPIRY_DAYS} days.

### Logs, Step Exports, and other observability

The total size of `console.log()` statements, [step exports](/workflows/#step-exports), and the original event data sent to the workflow cannot exceed a combined size of {FUNCTION_PAYLOAD_LIMIT}. If you produce logs or step exports larger than this - for example, passing around large API responses, CSVs, or other data - you may encounter a **Function Payload Limit Exceeded** in your workflow.

This limit cannot be raised.

## Acceptable Use

We ask that you abide by our [Acceptable Use](https://pipedream.com/terms/#b-acceptable-use) policy. In short this means: don’t use Pipedream to break the law; don’t abuse the platform; and don’t use the platform to harm others.

Built with [Mintlify](https://mintlify.com).
