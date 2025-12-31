# Source: https://upstash.com/docs/workflow/features/dlq.md

# Source: https://upstash.com/docs/qstash/sdks/ts/examples/dlq.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/dlq.md

# Source: https://upstash.com/docs/qstash/features/dlq.md

# Source: https://upstash.com/docs/workflow/features/dlq.md

# Source: https://upstash.com/docs/qstash/sdks/ts/examples/dlq.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/dlq.md

# Source: https://upstash.com/docs/qstash/features/dlq.md

# Source: https://upstash.com/docs/workflow/features/dlq.md

# Source: https://upstash.com/docs/qstash/sdks/ts/examples/dlq.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/dlq.md

# Source: https://upstash.com/docs/qstash/features/dlq.md

# Source: https://upstash.com/docs/workflow/features/dlq.md

# Source: https://upstash.com/docs/qstash/sdks/ts/examples/dlq.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/dlq.md

# Source: https://upstash.com/docs/qstash/features/dlq.md

# Source: https://upstash.com/docs/workflow/features/dlq.md

# Source: https://upstash.com/docs/qstash/sdks/ts/examples/dlq.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/dlq.md

# Source: https://upstash.com/docs/qstash/features/dlq.md

# Source: https://upstash.com/docs/workflow/features/dlq.md

# Overview

The Dead Letter Queue (DLQ) automatically captures failed workflow runs that have exhausted all retry attempts.

This ensures that no workflow execution is lost and provides multiple options for recovering from failures gracefully.

## How it works?

When a workflow step fails and exhausts all configured retries, Upstash Workflow automatically moves the failed run to the DLQ.
This happens automatically without any additional configuration required.

<Frame caption="Failed workflow runs are automatically moved to the Dead Letter Queue">
  <img src="https://mintcdn.com/upstash/GtBGrkScIq73E0LP/img/workflow/dlq.png?fit=max&auto=format&n=GtBGrkScIq73E0LP&q=85&s=55c87055536c48c56216202e3a640ac5" data-og-width="2726" width="2726" data-og-height="1652" height="1652" data-path="img/workflow/dlq.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/GtBGrkScIq73E0LP/img/workflow/dlq.png?w=280&fit=max&auto=format&n=GtBGrkScIq73E0LP&q=85&s=6f0358afca9d674e292c64ea81d61da8 280w, https://mintcdn.com/upstash/GtBGrkScIq73E0LP/img/workflow/dlq.png?w=560&fit=max&auto=format&n=GtBGrkScIq73E0LP&q=85&s=b45ac5fa1f9cdecb83d23f4ad6d5a51d 560w, https://mintcdn.com/upstash/GtBGrkScIq73E0LP/img/workflow/dlq.png?w=840&fit=max&auto=format&n=GtBGrkScIq73E0LP&q=85&s=3e7254872b08ae214cd99eab4c40efdd 840w, https://mintcdn.com/upstash/GtBGrkScIq73E0LP/img/workflow/dlq.png?w=1100&fit=max&auto=format&n=GtBGrkScIq73E0LP&q=85&s=713068e3a84d90bac77caa55c9cd7341 1100w, https://mintcdn.com/upstash/GtBGrkScIq73E0LP/img/workflow/dlq.png?w=1650&fit=max&auto=format&n=GtBGrkScIq73E0LP&q=85&s=59c549301e52181ebd7169597d6dc108 1650w, https://mintcdn.com/upstash/GtBGrkScIq73E0LP/img/workflow/dlq.png?w=2500&fit=max&auto=format&n=GtBGrkScIq73E0LP&q=85&s=d85e89f2716701a583c4e9236ba2906c 2500w" />
</Frame>

The DLQ serves as a safety net, preserving failed workflow runs with their complete execution context.

<Note>
  Dead Letter Queue entries have retention period based on your pricing plan:

  * **Free**: 3 days
  * **Pay-as-you-go**: 1 week
  * **Fixed pricing**: Up to 3 months

  After the retention duration expires, DLQ items are automatically removed and cannot be recovered.
</Note>

## Recovery Actions

Once a workflow run is in the DLQ, you can take the following actions:

* **[Restart](/workflow/features/dlq/restart)** – trigger the workflow from the beginning.
* **[Resume](/workflow/features/dlq/resume)** – continue the workflow from the point of failure.
* **[Re-run Failure Function](/workflow/features/dlq/callback)** – execute the workflow's failure handling logic again.
* or delete the DLQ entry if no action is required.

You can apply these actions in bulk to multiple DLQ entries. Check the individual action pages for more details.
