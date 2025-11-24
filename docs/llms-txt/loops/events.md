# Source: https://loops.so/docs/events.md

# Source: https://loops.so/docs/api-reference/examples/events.md

# Events API examples

> Code examples for sending events with the Loops API and SDKs.

## Send an event

[API reference](/api-reference/send-event)

<CodeGroup>
  ```js JavaScript theme={"dark"}
  await fetch("https://app.loops.so/api/v1/events/send", {
    method: "POST",
    headers: {
      "Authorization": "Bearer <your-api-key>",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      email: "test@example.com",
      eventName: "testEvent",
    }),
  });
  ```

  ```js JavaScript SDK theme={"dark"}
  import { LoopsClient } from "loops";

  const loops = new LoopsClient("<your-api-key>");

  const response = await loops.sendEvent({
    email: "test@example.com",
    eventName: "testEvent",
  });
  ```

  ```php PHP SDK theme={"dark"}
  use Loops\LoopsClient;

  $loops = new LoopsClient("<your-api-key>");

  $result = $loops->events->send(
    email: 'test@example.com',
    event_name: 'testEvent',
  );
  ```

  ```ruby Ruby SDK theme={"dark"}
  response = LoopsSdk::Events.send(
    email: "test@example.com",
    event_name: "testEvent",
  )
  ```

  ```python Python theme={"dark"}
  import requests

  response = requests.post(
      "https://app.loops.so/api/v1/events/send",
      headers={
          "Authorization": "Bearer <your-api-key>",
          "Content-Type": "application/json"
      },
      json={
          "email": "test@example.com",
          "eventName": "testEvent",
      }
  )
  ```
</CodeGroup>

## Send an event with event properties

Include data that can be used in your loop emails triggered by the event.

[API reference](/api-reference/send-event)

<CodeGroup>
  ```js JavaScript {10-12} theme={"dark"}
  await fetch("https://app.loops.so/api/v1/events/send", {
    method: "POST",
    headers: {
      "Authorization": "Bearer <your-api-key>",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      email: "test@example.com",
      eventName: "testEvent",
      eventProperties: {
        "testProperty": "testValue",
      },
    }),
  });
  ```

  ```js JavaScript SDK {8-10} theme={"dark"}
  import { LoopsClient } from "loops";

  const loops = new LoopsClient("<your-api-key>");

  const response = await loops.sendEvent({
    email: "test@example.com",
    eventName: "testEvent",
    eventProperties: {
      "testProperty": "testValue",
    },
  });
  ```

  ```php PHP SDK {8-10} theme={"dark"}
  use Loops\LoopsClient;

  $loops = new LoopsClient("<your-api-key>");

  $result = $loops->events->send(
    email: 'test@example.com',
    event_name: 'testEvent',
    event_properties: [
      'testProperty' => 'testValue',
    ],
  );
  ```

  ```ruby Ruby SDK {4-6} theme={"dark"}
  response = LoopsSdk::Events.send(
    email: "test@example.com",
    event_name: "testEvent",
    event_properties: {
      testProperty: "testValue",
    },
  )
  ```

  ```python Python {12-14} theme={"dark"}
  import requests

  response = requests.post(
      "https://app.loops.so/api/v1/events/send",
      headers={
          "Authorization": "Bearer <your-api-key>",
          "Content-Type": "application/json"
      },
      json={
          "email": "test@example.com",
          "eventName": "testEvent",
          "eventProperties": {
              "testProperty": "testValue",
          },
      }
  )
  ```
</CodeGroup>

## Send an event and update the contact

Include contact properties to update the contact as the event is sent.

[API reference](/api-reference/send-event)

<CodeGroup>
  ```js JavaScript {10} theme={"dark"}
  await fetch("https://app.loops.so/api/v1/events/send", {
    method: "POST",
    headers: {
      "Authorization": "Bearer <your-api-key>",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      email: "test@example.com",
      eventName: "testEvent",
      planName: "Pro", // Contact property
    }),
  });
  ```

  ```js JavaScript SDK {8-10} theme={"dark"}
  import { LoopsClient } from "loops";

  const loops = new LoopsClient("<your-api-key>");

  const response = await loops.sendEvent({
    email: "test@example.com",
    eventName: "testEvent",
    contactProperties: {
      planName: "Pro",
    },
  });
  ```

  ```php PHP SDK {8-10} theme={"dark"}
  use Loops\LoopsClient;

  $loops = new LoopsClient("<your-api-key>");

  $result = $loops->events->send(
    email: 'test@example.com',
    event_name: 'testEvent',
    contact_properties: [
      'planName' => 'Pro',
    ],
  );
  ```

  ```ruby Ruby SDK {4-6} theme={"dark"}
  response = LoopsSdk::Events.send(
    email: "test@example.com",
    event_name: "testEvent",
    contact_properties: {
      planName: "Pro",
    },
  )
  ```

  ```python Python {12-14} theme={"dark"}
  import requests

  response = requests.post(
      "https://app.loops.so/api/v1/events/send",
      headers={
          "Authorization": "Bearer <your-api-key>",
          "Content-Type": "application/json"
      },
      json={
          "email": "test@example.com",
          "eventName": "testEvent",
          "contactProperties": {
              "planName": "Pro",
          },
      }
  )
  ```
</CodeGroup>

## Send an event with an idempotency key

Add an `Idempotency-Key` header to the request to prevent duplicate requests.

[API reference](/api-reference/send-event#param-idempotency-key)

<CodeGroup>
  ```js JavaScript {6} theme={"dark"}
  await fetch("https://app.loops.so/api/v1/events/send", {
    method: "POST",
    headers: {
      "Authorization": "Bearer <your-api-key>",
      "Content-Type": "application/json"
      "Idempotency-Key": "550e8400-e29b-41d4-a716-446655440000",
    },
    body: JSON.stringify({
      email: "test@example.com",
      eventName: "testEvent",
    }),
  });
  ```

  ```js JavaScript SDK {8-10} theme={"dark"}
  import { LoopsClient } from "loops";

  const loops = new LoopsClient("<your-api-key>");

  const response = await loops.sendEvent({
    email: "test@example.com",
    eventName: "testEvent",
    headers: {
      "Idempotency-Key": "550e8400-e29b-41d4-a716-446655440000",
    },
  });
  ```

  ```php PHP SDK {8-10} theme={"dark"}
  use Loops\LoopsClient;

  $loops = new LoopsClient("<your-api-key>");

  $result = $loops->events->send(
    email: 'test@example.com',
    event_name: 'testEvent',
    headers: [
      'Idempotency-Key' => '550e8400-e29b-41d4-a716-446655440000',
    ],
  );
  ```

  ```ruby Ruby SDK {4-6} theme={"dark"}
  response = LoopsSdk::Events.send(
    email: "test@example.com",
    event_name: "testEvent",
    headers: {
      "Idempotency-Key" => "550e8400-e29b-41d4-a716-446655440000",
    },
  )
  ```

  ```python Python {8} theme={"dark"}
  import requests

  response = requests.post(
      "https://app.loops.so/api/v1/events/send",
      headers={
          "Authorization": "Bearer <your-api-key>",
          "Content-Type": "application/json"
          "Idempotency-Key": "550e8400-e29b-41d4-a716-446655440000",
      },
      json={
          "email": "test@example.com",
          "eventName": "testEvent",
      }
  )
  ```
</CodeGroup>
