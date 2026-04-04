# Source: https://upstash.com/docs/workflow/rest/dlq/callback.md

# Source: https://upstash.com/docs/workflow/features/dlq/callback.md

# Source: https://upstash.com/docs/workflow/basics/client/dlq/callback.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# client.dlq.retryFailureFunction

If a workflow's `failureFunction` or `failureUrl` request has failed, you can retry it using the `retryFailureFunction` method:

## Arguments

## Response

## Usage

```ts  theme={"system"}
import { Client } from "@upstash/workflow";

const client = new Client({ token: "<QSTASH_TOKEN>" });

// Retry the failure callback for a specific DLQ message
const response = await client.dlq.retryFailureFunction({
  dlqId: "dlq-12345" // The ID of the DLQ message to retry
});
```
