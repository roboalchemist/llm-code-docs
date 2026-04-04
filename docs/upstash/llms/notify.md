# Source: https://upstash.com/docs/workflow/rest/runs/notify.md

# Source: https://upstash.com/docs/workflow/features/notify.md

# Source: https://upstash.com/docs/workflow/basics/context/notify.md

# Source: https://upstash.com/docs/workflow/basics/client/notify.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# client.notify

The `notify` method notifies workflows that are waiting for a specific event.

Workflows paused at a [`context.waitForEvent`](/workflow/basics/context/waitForEvent) step with the matching `eventId` will be resumed, and the provided `eventData` will be passed back to them.

## Arguments

<ParamField body="eventId" type="string" required>
  The identifier of the event to notify.
</ParamField>

<ParamField body="eventData" type="any" optional>
  Data to deliver to the waiting workflow(s).
  This value will be returned in the `eventData` field of `context.waitForEvent`.
</ParamField>

## Response

Returns a list of `Waiter` objects representing the workflows that were notified:

<Snippet file="qstash/waiter.mdx" />

## Usage

```javascript  theme={"system"}
import { Client } from "@upstash/workflow";

const client = new Client({ token: "<QSTASH_TOKEN>" });

await client.notify({
  eventId: "my-event-id",
  eventData: "my-data", // data passed to the workflow run
});
```
