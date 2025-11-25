# Source: https://upstash.com/docs/workflow/examples/waitForEvent.md

# Source: https://upstash.com/docs/workflow/basics/context/waitForEvent.md

# Source: https://upstash.com/docs/workflow/examples/waitForEvent.md

# Source: https://upstash.com/docs/workflow/basics/context/waitForEvent.md

# Source: https://upstash.com/docs/workflow/examples/waitForEvent.md

# Source: https://upstash.com/docs/workflow/basics/context/waitForEvent.md

# Source: https://upstash.com/docs/workflow/examples/waitForEvent.md

# Waiting for Events

<Note>
  This feature is not yet available in
  [workflow-py](https://github.com/upstash/workflow-py). See our
  [Roadmap](/workflow/roadmap) for feature parity plans and
  [Changelog](/workflow/changelog) for updates.
</Note>

## Introduction

This example demonstrates how to handle order processing using Upstash Workflow. The workflow will wait for an external system to process an order and resume once it is 'notified'. See our documentation [for more details about events](/workflow/howto/events).

## Use Case

Our workflow will be:

1. Receive an order request.
2. Send an email to request order processing.
3. Wait for an external event that indicates the order has been processed.
4. Handle timeout scenarios if the event is not received in time.
5. Save the results

## Code Example

```typescript  theme={"system"}
import { serve } from "@upstash/workflow/nextjs";

export const { POST } = serve(async (context) => {
  const { orderId, userEmail } = context.requestPayload;

  // Step 1: request order processing
  await context.run("request order processing", async () => {
    await requestProcessing(orderId)
  })

  // Step 2: Wait for the order to be processed
  const { eventData, timeout } = await context.waitForEvent(
    "wait for order processing",
    `order-${orderId}`,
    {
      timeout: "10m" // 10 minutes timeout
    }
  );

  if (timeout) {
    // end workflow in case of timeout
    return;
  }

  const processedData = eventData;

  // Step 3: Log the processed order
  await context.run("process-order", async () => {
    console.log(`Order ${orderId} processed:`, processedData);
  });

  // Step 4: Send a confirmation email
  await context.run("send-confirmation-email", async () => {
    await sendEmail(
      userEmail,
      "Your order has been processed!",
      processedData
    );
  });
});
```

Code for notifying the worklfow:

```typescript  theme={"system"}
import { Client } from "@upstash/workflow";

const client = new Client({ token: "<QSTASH_TOKEN>" })
const orderId = "1324"

await client.notify({
  eventId: `order-${orderId}`,
  eventData: { deliveryTime: "2 days" }
});
```

## Code Breakdown

### 1. Requesting Order Processing

In its first step, we call a method to request processing of the order in the request payload:

```typescript  theme={"system"}
await context.run("request order processing", async () => {
  await requestProcessing(orderId)
})
```

You can imagine that this step sends an email to the company responsible for the delivery.

### 2. Waiting for the Event

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/events/wait.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=b3df80343dc367c8fd09ad6481c499ef" data-og-width="1722" width="1722" data-og-height="968" height="968" data-path="img/qstash-workflow/events/wait.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/events/wait.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=eaad3c3925ec650f24de49ab927eee9f 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/events/wait.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=69e1e0c8056d8f595ad1e9c15f297bc7 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/events/wait.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=6b0af5a4244d8988889dd01e7b83fd41 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/events/wait.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=a7d9eabbaddef6bbbabb6e6530c49950 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/events/wait.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=968e19f9a4e634b25ae6cdea637e2cba 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/events/wait.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=0ba58ebcf66045fa7d2ff148295adab4 2500w" />
</Frame>

Next, the workflow waits for the order to be processed. It uses [the `waitForEvent` method](/workflow/basics/context#context-waitforevent) to pause execution and listen for the event. A timeout of 10 minutes (600 seconds) is applied to avoid indefinite waiting.

```typescript  theme={"system"}
const { eventData, timeout } = await context.waitForEvent(
  "wait for order processing",
  `order-${orderId}`,
  {
    timeout: "10m" // 10 minutes timeout
  }
);

if (timeout) {
  // end workflow in case of timeout
  return;
}
```

The workflow listens for the event with the ID `order-${orderId}`. When the external service notifies the workflow with this ID, the workflow resumes. If no event is received in time, the timeout ensures the workflow doesn't hang.

### 3. Processing the Order

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/events/resume.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=f9bd8c9beaa9cd1a245d9ad05e9368a3" data-og-width="1818" width="1818" data-og-height="1134" height="1134" data-path="img/qstash-workflow/events/resume.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/events/resume.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=e8f187626788599658c3d01e90ba8a83 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/events/resume.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=b28dbb06f5b7d8d0056d15bdd56c9626 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/events/resume.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=5512887f292138f88b0e267f7913a0f4 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/events/resume.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=e8044982eb0a63e10b817b8f5bba4096 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/events/resume.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=abf44426dba2d1381ab3266ef8df8dec 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/events/resume.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=3523c231515576213c67bd0b0819b4e8 2500w" />
</Frame>

Once the workflow resumes, the order data (`eventData`) is logged. This step could include updates to the database, inventory adjustments, or other backend operations specific to order processing.

```typescript  theme={"system"}
await context.run("process-order", async () => {
  console.log(`Order ${orderId} processed:`, processedData);
});
```

### 4. Sending a Confirmation Email

Once the order is processed, the workflow sends a confirmation email to the user.

```typescript  theme={"system"}
await context.run("send-confirmation-email", async () => {
  await sendEmail(
    userEmail,
    "Your order has been processed!",
    processedData
  );
});
```

## External Event Notification

To notify the workflow that the order has been processed, the external system sends a notification to the workflow with relevant data using the [`notify` method from the `Client`](/workflow/basics/client#notify-waiting-workflow). Alternatively, you can use [`context.notify` method](/workflow/basics/context#context-notify).

```typescript  theme={"system"}
import { Client } from "@upstash/workflow";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const orderId = "1324";

await client.notify({
  eventId: `order-${orderId}`,
  eventData: { deliveryTime: "2 days" }
});
```

## Key Features

1. **Asynchronous Event Handling**: The workflow waits for an external event (order processing) to occur and only resumes once the event is received.
2. **Timeout Control**: A timeout mechanism ensures that the workflow doesn't hang if the event isn't received within the expected time.
3. **Order Processing**: Once notified, the workflow handles order processing and sends a confirmation email to the customer.
4. **External Event Notifications**: The external system can notify the workflow, providing the necessary data to resume execution and complete the process.
