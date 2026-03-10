# Source: https://www.inngest.com/docs-markdown/reference/typescript/v4/functions/step-wait-for-event

# Wait for event

Use `step.waitForEvent()` to pause your function's execution until a matching event is received or a timeout is reached. This is useful for building human-in-the-loop workflows, waiting for approvals, or coordinating between separate functions.

## `step.waitForEvent(id, options): Promise<null | EventPayload>`

- `id` (string): The ID of the step. This will be what appears in your function's logs and is used to memoize step state across function versions.

* `options` (object): Options for configuring how to wait for the event.The name of a given event to wait for, or an eventType() result for typed return values.The amount of time to wait to receive the event. A time string compatible with the ms package, e.g. "30m", "3 hours", or "2.5d"The property to match the event trigger and the wait event, using dot-notation, e.g. data.userId. Cannot be combined with if.An expression on which to conditionally match the original event trigger (event) and the wait event (async). Cannot be combined with match.Expressions are defined using the Common Expression Language (CEL) with the events accessible using dot-notation. Read our guide to writing expressions for more info. Examples:event.data.userId == async.data.userId && async.data.billing\_plan == 'pro'

```ts
// Wait 7 days for an approval and match invoice IDs
const approval = await step.waitForEvent("wait-for-approval", {
  event: "app/invoice.approved",
  timeout: "7d",
  match: "data.invoiceId",
});

// Wait 30 days for a user to start a subscription
// on the pro plan
const subscription = await step.waitForEvent("wait-for-subscription", {
  event: "app/subscription.created",
  timeout: "30d",
  if: "event.data.userId == async.data.userId && async.data.billing_plan == 'pro'",
});

// Use eventType() for typed return values
const approvalType = eventType("app/approval.received", {
  schema: z.object({ approved: z.boolean() }),
});

const approval = await step.waitForEvent("wait-for-approval", {
  event: approvalType,
  timeout: "7d",
});
// approval?.data is typed as { approved: boolean }
```

> **Callout:** step.waitForEvent() must be called using await or some other Promise handler to ensure your function sleeps correctly.