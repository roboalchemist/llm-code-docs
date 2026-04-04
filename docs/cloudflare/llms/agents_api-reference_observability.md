# Source: https://developers.cloudflare.com/agents/api-reference/observability/index.md

---

title: Observability · Cloudflare Agents docs
description: Agent instances use the observability property to emit various
  internal events that can be used for logging and monitoring.
lastUpdated: 2026-02-05T16:44:57.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/agents/api-reference/observability/
  md: https://developers.cloudflare.com/agents/api-reference/observability/index.md
---

`Agent` instances use the `observability` property to emit various internal events that can be used for logging and monitoring.

## Default behavior

The default behavior is to `console.log()` the event value:

```json
{
  "displayMessage": "State updated",
  "id": "EnOzrS_tEo_8dHy5oyl8q",
  "payload": {},
  "timestamp": 1758005142787,
  "type": "state:update"
}
```

## Custom observability

You can configure observability by overriding the property with an implementation of the `Observability` interface. This interface has a single `emit()` method that takes an `ObservabilityEvent`.

* JavaScript

  ```js
  import { Agent } from "agents";
  import {} from "agents/observability";


  const observability = {
    emit(event) {
      if (event.type === "connect") {
        console.log(event.timestamp, event.payload.connectionId);
      }
    },
  };


  class MyAgent extends Agent {
    observability = observability;
  }
  ```

* TypeScript

  ```ts
  import { Agent } from "agents";
  import { type Observability } from "agents/observability";


  const observability: Observability = {
    emit(event) {
      if (event.type === "connect") {
        console.log(event.timestamp, event.payload.connectionId);
      }
    },
  };


  class MyAgent extends Agent {
    override observability = observability;
  }
  ```

## Disabling observability

Alternatively, you can set the property to `undefined` to ignore all events:

* JavaScript

  ```js
  import { Agent } from "agents";


  class MyAgent extends Agent {
    observability = undefined;
  }
  ```

* TypeScript

  ```ts
  import { Agent } from "agents";


  class MyAgent extends Agent {
    override observability = undefined;
  }
  ```

## Event types

The observability system emits events for various agent activities:

| Event Type | Description |
| - | - |
| `connect` | WebSocket connection established |
| `disconnect` | WebSocket connection closed |
| `state:update` | Agent state was updated |
| `message` | Message received from client |
| `error` | Error occurred during processing |
| `schedule:execute` | Scheduled task executed |
| `queue:process` | Queue task processed |

## ObservabilityEvent structure

Each event has the following structure:

```ts
type ObservabilityEvent = {
  id: string; // Unique event identifier
  type: string; // Event type (e.g., "connect", "state:update")
  displayMessage: string; // Human-readable description
  timestamp: number; // Unix timestamp in milliseconds
  payload: Record<string, unknown>; // Event-specific data
};
```

## Integration with external services

You can integrate observability with external logging and monitoring services:

* JavaScript

  ```js
  import { Agent } from "agents";
  import {} from "agents/observability";


  const observability = {
    emit(event) {
      // Send to external logging service
      fetch("https://logging.example.com/ingest", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          service: "my-agent",
          level: event.type === "error" ? "error" : "info",
          message: event.displayMessage,
          metadata: {
            eventId: event.id,
            eventType: event.type,
            timestamp: event.timestamp,
            ...event.payload,
          },
        }),
      }).catch(console.error);
    },
  };


  class MyAgent extends Agent {
    observability = observability;
  }
  ```

* TypeScript

  ```ts
  import { Agent } from "agents";
  import {
    type Observability,
    type ObservabilityEvent,
  } from "agents/observability";


  const observability: Observability = {
    emit(event: ObservabilityEvent) {
      // Send to external logging service
      fetch("https://logging.example.com/ingest", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          service: "my-agent",
          level: event.type === "error" ? "error" : "info",
          message: event.displayMessage,
          metadata: {
            eventId: event.id,
            eventType: event.type,
            timestamp: event.timestamp,
            ...event.payload,
          },
        }),
      }).catch(console.error);
    },
  };


  class MyAgent extends Agent {
    override observability = observability;
  }
  ```

## Filtering events

You can filter which events to process:

* JavaScript

  ```js
  const observability = {
    emit(event) {
      // Only log errors and state updates
      if (event.type === "error" || event.type === "state:update") {
        console.log(JSON.stringify(event));
      }
    },
  };
  ```

* TypeScript

  ```ts
  const observability: Observability = {
    emit(event) {
      // Only log errors and state updates
      if (event.type === "error" || event.type === "state:update") {
        console.log(JSON.stringify(event));
      }
    },
  };
  ```

## Next steps

[Configuration](https://developers.cloudflare.com/agents/api-reference/configuration/)wrangler.jsonc setup and deployment.

[Dashboard setup](https://developers.cloudflare.com/agents/api-reference/configuration/#dashboard-setup)View logs in the Cloudflare dashboard.

[Agents API](https://developers.cloudflare.com/agents/api-reference/agents-api/)Complete API reference for the Agents SDK.
