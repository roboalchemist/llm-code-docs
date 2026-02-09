# Source: https://upstash.com/docs/workflow/features/failureFunction/reliability.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Reliability of Failure Function

The failure function is executed whenever a workflow run fails.

In some cases, the failure function itself may throw an error.
When this happens, it will be retried according to the workflow run's retry configuration.
If all retry attempts also fail, the failure function execution is marked as failed.

You can view and filter workflow runs with failed failure function executions in the DLQ dashboard.

<Frame caption="You can filter DLQ entries by failure function state">
  <img src="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/failure_callback_state_filter.png?fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=bb2e7876881dd34056eec3c76de7f4fe" data-og-width="2562" width="2562" data-og-height="1976" height="1976" data-path="img/workflow/failure_callback_state_filter.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/failure_callback_state_filter.png?w=280&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=da2326f2f6a4e9150fc03f9ad10338ee 280w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/failure_callback_state_filter.png?w=560&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=72659c9797764dd292603c98be068ca7 560w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/failure_callback_state_filter.png?w=840&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=a603d1168489ffdc38b86a90f1ce1afd 840w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/failure_callback_state_filter.png?w=1100&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=596753274e040acadea3f40bad09176f 1100w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/failure_callback_state_filter.png?w=1650&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=940a2b4ba4cd0a8ada87650bcffb0638 1650w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/failure_callback_state_filter.png?w=2500&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=90b1dd00d63775ea95ef4ab80977de4a 2500w" />
</Frame>

From the DLQ dashboard, you can retry the failure function.

<Frame caption="You can filter DLQ entries by failure function state">
  <img src="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/retry_failure_callback.png?fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=b821a3bd718fe7f8dfbb9f3600659b99" data-og-width="2568" width="2568" data-og-height="1988" height="1988" data-path="img/workflow/retry_failure_callback.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/retry_failure_callback.png?w=280&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=77fecfb6cf4a3dfe916f447adac2b6d4 280w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/retry_failure_callback.png?w=560&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=119ab6e368e3c9268da35c3c3d367b21 560w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/retry_failure_callback.png?w=840&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=6bf3f9e9604924594b21166bfa297318 840w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/retry_failure_callback.png?w=1100&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=c059230b1c21e93466ecb4380ddc95f2 1100w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/retry_failure_callback.png?w=1650&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=50ba5df4a42e7dcba612a7a3d29e9365 1650w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/retry_failure_callback.png?w=2500&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=feb1c2edd18cf8f8095f58d6d0a6ae4f 2500w" />
</Frame>

You can perform this action programmatically as well:

```ts  theme={"system"}
import { Client } from "@upstash/workflow";

const client = new Client({ token: "<QSTASH_TOKEN>" });

const response = await client.dlq.retryFailureFunction({
  dlqId: "dlq-12345" // The ID of the DLQ message to retry
});
```
