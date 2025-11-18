# Source: https://upstash.com/docs/workflow/features/retries.md

# Source: https://upstash.com/docs/redis/sdks/ts/retries.md

# Source: https://upstash.com/docs/workflow/features/retries.md

# Overview

Upstash Workflow provides an automatic retry mechanism to improve reliability and make workflows resilient against temporary failures.
Workflow automatically handles transient errors such as network issues or service unavailability.

## How Retries Work

When a step fails, Upstash Workflow automatically retries the failed step with configurable retry attempts and delay strategy.
This allows temporary issues to resolve without manual intervention.

<Frame caption="A failing step is automatically retried three times by default">
  <img src="https://mintcdn.com/upstash/GtBGrkScIq73E0LP/img/workflow/automatic_retry.png?fit=max&auto=format&n=GtBGrkScIq73E0LP&q=85&s=b082701763068698f0c9cf799c0b103f" data-og-width="2712" width="2712" data-og-height="2062" height="2062" data-path="img/workflow/automatic_retry.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/GtBGrkScIq73E0LP/img/workflow/automatic_retry.png?w=280&fit=max&auto=format&n=GtBGrkScIq73E0LP&q=85&s=812f44fe1af682d6f76d24fd2c6a596f 280w, https://mintcdn.com/upstash/GtBGrkScIq73E0LP/img/workflow/automatic_retry.png?w=560&fit=max&auto=format&n=GtBGrkScIq73E0LP&q=85&s=6ba50e0cf5663866adc1f7188c9ca005 560w, https://mintcdn.com/upstash/GtBGrkScIq73E0LP/img/workflow/automatic_retry.png?w=840&fit=max&auto=format&n=GtBGrkScIq73E0LP&q=85&s=140d6b7de2f3b1fec736f3da37eb72a4 840w, https://mintcdn.com/upstash/GtBGrkScIq73E0LP/img/workflow/automatic_retry.png?w=1100&fit=max&auto=format&n=GtBGrkScIq73E0LP&q=85&s=1dd701aab5c1bafa5bba097f62e5f070 1100w, https://mintcdn.com/upstash/GtBGrkScIq73E0LP/img/workflow/automatic_retry.png?w=1650&fit=max&auto=format&n=GtBGrkScIq73E0LP&q=85&s=98521bb337818bd4e4b353829858973a 1650w, https://mintcdn.com/upstash/GtBGrkScIq73E0LP/img/workflow/automatic_retry.png?w=2500&fit=max&auto=format&n=GtBGrkScIq73E0LP&q=85&s=92fccb600a8c71c94434416677aaa59d 2500w" />
</Frame>

By default, the retry count is set to **3**, and an **exponential backoff** delay strategy is used.

```javascript Default Backoff Algorithm theme={"system"}
// n = how many times this request has been retried
delay = min(86400, e ** (2.5*n)) // in seconds
```

| Retry Attempt | Algorithm | Delay |
| ------------- | --------- | ----- |
| 1             | $e^{2.5}$ | 12s   |
| 2             | $e^5$     | 2m28s |
| 3             | $e^{7.5}$ | 30m8s |
| 4+            | $86400$   | 24h   |

## Configuration

You can configure retry behavior when starting a new workflow run.

### Configure Retry Attempt Count

You can specify how many times a step should be retried upon failure.

```typescript Configure Retry Attempt Count theme={"system"}
import { Client } from "@upstash/workflow";

const client = new Client({ token: "<QSTASH_TOKEN>" })

const { workflowRunId } = await client.trigger({
  url: "https://<YOUR_WORKFLOW_ENDPOINT>/<YOUR-WORKFLOW-ROUTE>",
  retries: 3,
  keepTriggerConfig: true,
})
```

### Configure Retry Delay Strategy

Retry delay is the time to wait before trying again after a failure. You can define a custom retry delay strategy.

The delay is defined as a math expression that is calculated on every retry.
The expression can use the `retried` variable, which represents how many times the step has already retried (starting from 0).

To apply a constant delay, you can simply provide a fixed value.

The expression must return the delay in **milliseconds**.

```typescript Configure Retry Delay Strategy theme={"system"}
import { Client } from "@upstash/workflow";

const client = new Client({ token: "<QSTASH_TOKEN>" })

const { workflowRunId } = await client.trigger({
  url: "https://<YOUR_WORKFLOW_ENDPOINT>/<YOUR-WORKFLOW-ROUTE>",
  retries: 3,
  retryDelay: "(1 + retried) * 1000",
  keepTriggerConfig: true,
})
```
