# Source: https://developers.cloudflare.com/agents/getting-started/add-to-existing-project/index.md

---

title: Add to existing project · Cloudflare Agents docs
description: This guide shows how to add agents to an existing Cloudflare
  Workers project. If you are starting fresh, refer to Building a chat agent
  instead.
lastUpdated: 2026-02-08T17:40:34.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/agents/getting-started/add-to-existing-project/
  md: https://developers.cloudflare.com/agents/getting-started/add-to-existing-project/index.md
---

This guide shows how to add agents to an existing Cloudflare Workers project. If you are starting fresh, refer to [Building a chat agent](https://developers.cloudflare.com/agents/getting-started/build-a-chat-agent/) instead.

## Prerequisites

* An existing Cloudflare Workers project with a Wrangler configuration file
* Node.js 18 or newer

## 1. Install the package

* npm

  ```sh
  npm i agents
  ```

* yarn

  ```sh
  yarn add agents
  ```

* pnpm

  ```sh
  pnpm add agents
  ```

For React applications, no additional packages are needed — React bindings are included.

For Hono applications:

* npm

  ```sh
  npm i agents hono-agents
  ```

* yarn

  ```sh
  yarn add agents hono-agents
  ```

* pnpm

  ```sh
  pnpm add agents hono-agents
  ```

## 2. Create an Agent

Create a new file for your agent (for example, `src/agents/counter.ts`):

* JavaScript

  ```js
  import { Agent } from "agents";


  export class CounterAgent extends Agent {
    initialState = { count: 0 };


    increment() {
      this.setState({ count: this.state.count + 1 });
      return this.state.count;
    }


    decrement() {
      this.setState({ count: this.state.count - 1 });
      return this.state.count;
    }
  }
  ```

* TypeScript

  ```ts
  import { Agent } from "agents";


  export type CounterState = {
    count: number;
  };


  export class CounterAgent extends Agent<Env, CounterState> {
    initialState: CounterState = { count: 0 };


    increment() {
      this.setState({ count: this.state.count + 1 });
      return this.state.count;
    }


    decrement() {
      this.setState({ count: this.state.count - 1 });
      return this.state.count;
    }
  }
  ```

## 3. Update Wrangler configuration

Add the Durable Object binding and migration:

* wrangler.jsonc

  ```jsonc
  {
    "name": "my-existing-project",
    "main": "src/index.ts",
    "compatibility_date": "2025-01-01",
    "compatibility_flags": ["nodejs_compat"],


    "durable_objects": {
      "bindings": [
        {
          "name": "CounterAgent",
          "class_name": "CounterAgent",
        },
      ],
    },


    "migrations": [
      {
        "tag": "v1",
        "new_sqlite_classes": ["CounterAgent"],
      },
    ],
  }
  ```

* wrangler.toml

  ```toml
  name = "my-existing-project"
  main = "src/index.ts"
  compatibility_date = "2025-01-01"
  compatibility_flags = [ "nodejs_compat" ]


  [[durable_objects.bindings]]
  name = "CounterAgent"
  class_name = "CounterAgent"


  [[migrations]]
  tag = "v1"
  new_sqlite_classes = [ "CounterAgent" ]
  ```

**Key points:**

* `name` in bindings becomes the property on `env` (for example, `env.CounterAgent`)
* `class_name` must exactly match your exported class name
* `new_sqlite_classes` enables SQLite storage for state persistence
* `nodejs_compat` flag is required for the agents package

## 4. Export the Agent class

Your agent class must be exported from your main entry point. Update your `src/index.ts`:

* JavaScript

  ```js
  // Export the agent class (required for Durable Objects)
  export { CounterAgent } from "./agents/counter";


  // Your existing exports...
  export default {
    // ...
  };
  ```

* TypeScript

  ```ts
  // Export the agent class (required for Durable Objects)
  export { CounterAgent } from "./agents/counter";


  // Your existing exports...
  export default {
    // ...
  };
  ```

## 5. Wire up routing

Choose the approach that matches your project structure:

### Plain Workers (fetch handler)

* JavaScript

  ```js
  import { routeAgentRequest } from "agents";
  export { CounterAgent } from "./agents/counter";


  export default {
    async fetch(request, env, ctx) {
      // Try agent routing first
      const agentResponse = await routeAgentRequest(request, env);
      if (agentResponse) return agentResponse;


      // Your existing routing logic
      const url = new URL(request.url);
      if (url.pathname === "/api/hello") {
        return Response.json({ message: "Hello!" });
      }


      return new Response("Not found", { status: 404 });
    },
  };
  ```

* TypeScript

  ```ts
  import { routeAgentRequest } from "agents";
  export { CounterAgent } from "./agents/counter";


  export default {
    async fetch(request: Request, env: Env, ctx: ExecutionContext) {
      // Try agent routing first
      const agentResponse = await routeAgentRequest(request, env);
      if (agentResponse) return agentResponse;


      // Your existing routing logic
      const url = new URL(request.url);
      if (url.pathname === "/api/hello") {
        return Response.json({ message: "Hello!" });
      }


      return new Response("Not found", { status: 404 });
    },
  };
  ```

### Hono

* JavaScript

  ```js
  import { Hono } from "hono";
  import { agentsMiddleware } from "hono-agents";
  export { CounterAgent } from "./agents/counter";


  const app = new Hono();


  // Add agents middleware - handles WebSocket upgrades and agent HTTP requests
  app.use("*", agentsMiddleware());


  // Your existing routes continue to work
  app.get("/api/hello", (c) => c.json({ message: "Hello!" }));


  export default app;
  ```

* TypeScript

  ```ts
  import { Hono } from "hono";
  import { agentsMiddleware } from "hono-agents";
  export { CounterAgent } from "./agents/counter";


  const app = new Hono<{ Bindings: Env }>();


  // Add agents middleware - handles WebSocket upgrades and agent HTTP requests
  app.use("*", agentsMiddleware());


  // Your existing routes continue to work
  app.get("/api/hello", (c) => c.json({ message: "Hello!" }));


  export default app;
  ```

### With static assets

If you are serving static assets alongside agents, static assets are served first by default. Your Worker code only runs for paths that do not match a static asset:

* JavaScript

  ```js
  import { routeAgentRequest } from "agents";
  export { CounterAgent } from "./agents/counter";


  export default {
    async fetch(request, env, ctx) {
      // Static assets are served automatically before this runs
      // This only handles non-asset requests


      // Route to agents
      const agentResponse = await routeAgentRequest(request, env);
      if (agentResponse) return agentResponse;


      return new Response("Not found", { status: 404 });
    },
  };
  ```

* TypeScript

  ```ts
  import { routeAgentRequest } from "agents";
  export { CounterAgent } from "./agents/counter";


  export default {
    async fetch(request: Request, env: Env, ctx: ExecutionContext) {
      // Static assets are served automatically before this runs
      // This only handles non-asset requests


      // Route to agents
      const agentResponse = await routeAgentRequest(request, env);
      if (agentResponse) return agentResponse;


      return new Response("Not found", { status: 404 });
    },
  };
  ```

Configure assets in the Wrangler configuration file:

* wrangler.jsonc

  ```jsonc
  {
    "assets": {
      "directory": "./public",
    },
  }
  ```

* wrangler.toml

  ```toml
  [assets]
  directory = "./public"
  ```

## 6. Add TypeScript types

You can generate types automatically from your Wrangler configuration file:

```sh
npx wrangler types env.d.ts
```

This creates an `env.d.ts` file with all your bindings typed. Alternatively, you can manually update your `Env` type to include the agent namespace:

```ts
import type { CounterAgent } from "./agents/counter";


interface Env {
  // Your existing bindings
  MY_KV: KVNamespace;
  MY_DB: D1Database;


  // Add agent bindings
  CounterAgent: DurableObjectNamespace<CounterAgent>;
}
```

Refer to [Configuration](https://developers.cloudflare.com/agents/api-reference/configuration/#generating-types) for more details on type generation.

## 7. Connect from the frontend

### React

* JavaScript

  ```js
  import { useState } from "react";
  import { useAgent } from "agents/react";
  function CounterWidget() {
    const [count, setCount] = useState(0);


    const agent = useAgent({
      agent: "CounterAgent",
      onStateUpdate: (state) => setCount(state.count),
    });


    return (
      <>
        {count}
        <button onClick={() => agent.stub.increment()}>+</button>
        <button onClick={() => agent.stub.decrement()}>-</button>
      </>
    );
  }
  ```

* TypeScript

  ```ts
  import { useState } from "react";
  import { useAgent } from "agents/react";
  import type { CounterAgent, CounterState } from "./agents/counter";


  function CounterWidget() {
    const [count, setCount] = useState(0);


    const agent = useAgent<CounterAgent, CounterState>({
      agent: "CounterAgent",
      onStateUpdate: (state) => setCount(state.count),
    });


    return (
      <>
        {count}
        <button onClick={() => agent.stub.increment()}>+</button>
        <button onClick={() => agent.stub.decrement()}>-</button>
      </>
    );
  }
  ```

### Vanilla JavaScript

* JavaScript

  ```js
  import { AgentClient } from "agents/client";


  const agent = new AgentClient({
    agent: "CounterAgent",
    name: "user-123", // Optional: unique instance name
    onStateUpdate: (state) => {
      document.getElementById("count").textContent = state.count;
    },
  });


  // Call methods
  document.getElementById("increment").onclick = () => agent.call("increment");
  ```

* TypeScript

  ```ts
  import { AgentClient } from "agents/client";


  const agent = new AgentClient({
    agent: "CounterAgent",
    name: "user-123", // Optional: unique instance name
    onStateUpdate: (state) => {
      document.getElementById("count").textContent = state.count;
    },
  });


  // Call methods
  document.getElementById("increment").onclick = () => agent.call("increment");
  ```

## Adding multiple agents

Add more agents by extending the configuration:

* JavaScript

  ```js
  // src/agents/chat.ts
  export class Chat extends Agent {
    // ...
  }


  // src/agents/scheduler.ts
  export class Scheduler extends Agent {
    // ...
  }
  ```

* TypeScript

  ```ts
  // src/agents/chat.ts
  export class Chat extends Agent {
    // ...
  }


  // src/agents/scheduler.ts
  export class Scheduler extends Agent {
    // ...
  }
  ```

Update the Wrangler configuration file:

* wrangler.jsonc

  ```jsonc
  {
    "durable_objects": {
      "bindings": [
        { "name": "CounterAgent", "class_name": "CounterAgent" },
        { "name": "Chat", "class_name": "Chat" },
        { "name": "Scheduler", "class_name": "Scheduler" },
      ],
    },
    "migrations": [
      {
        "tag": "v1",
        "new_sqlite_classes": ["CounterAgent", "Chat", "Scheduler"],
      },
    ],
  }
  ```

* wrangler.toml

  ```toml
  [[durable_objects.bindings]]
  name = "CounterAgent"
  class_name = "CounterAgent"


  [[durable_objects.bindings]]
  name = "Chat"
  class_name = "Chat"


  [[durable_objects.bindings]]
  name = "Scheduler"
  class_name = "Scheduler"


  [[migrations]]
  tag = "v1"
  new_sqlite_classes = [ "CounterAgent", "Chat", "Scheduler" ]
  ```

Export all agents from your entry point:

* JavaScript

  ```js
  export { CounterAgent } from "./agents/counter";
  export { Chat } from "./agents/chat";
  export { Scheduler } from "./agents/scheduler";
  ```

* TypeScript

  ```ts
  export { CounterAgent } from "./agents/counter";
  export { Chat } from "./agents/chat";
  export { Scheduler } from "./agents/scheduler";
  ```

## Common integration patterns

### Agents behind authentication

Check auth before routing to agents:

* JavaScript

  ```js
  export default {
    async fetch(request, env) {
      // Check auth for agent routes
      if (request.url.includes("/agents/")) {
        const authResult = await checkAuth(request, env);
        if (!authResult.valid) {
          return new Response("Unauthorized", { status: 401 });
        }
      }


      const agentResponse = await routeAgentRequest(request, env);
      if (agentResponse) return agentResponse;


      // ... rest of routing
    },
  };
  ```

* TypeScript

  ```ts
  export default {
    async fetch(request: Request, env: Env) {
      // Check auth for agent routes
      if (request.url.includes("/agents/")) {
        const authResult = await checkAuth(request, env);
        if (!authResult.valid) {
          return new Response("Unauthorized", { status: 401 });
        }
      }


      const agentResponse = await routeAgentRequest(request, env);
      if (agentResponse) return agentResponse;


      // ... rest of routing
    },
  };
  ```

### Custom agent path prefix

By default, agents are routed at `/agents/{agent-name}/{instance-name}`. You can customize this:

* JavaScript

  ```js
  import { routeAgentRequest } from "agents";


  const agentResponse = await routeAgentRequest(request, env, {
    prefix: "/api/agents", // Now routes at /api/agents/{agent-name}/{instance-name}
  });
  ```

* TypeScript

  ```ts
  import { routeAgentRequest } from "agents";


  const agentResponse = await routeAgentRequest(request, env, {
    prefix: "/api/agents", // Now routes at /api/agents/{agent-name}/{instance-name}
  });
  ```

Refer to [Routing](https://developers.cloudflare.com/agents/api-reference/routing/) for more options including CORS, custom instance naming, and location hints.

### Accessing agents from server code

You can interact with agents directly from your Worker code:

* JavaScript

  ```js
  import { getAgentByName } from "agents";


  export default {
    async fetch(request, env) {
      if (request.url.endsWith("/api/increment")) {
        // Get a specific agent instance
        const counter = await getAgentByName(env.CounterAgent, "shared-counter");
        const newCount = await counter.increment();
        return Response.json({ count: newCount });
      }
      // ...
    },
  };
  ```

* TypeScript

  ```ts
  import { getAgentByName } from "agents";


  export default {
    async fetch(request: Request, env: Env) {
      if (request.url.endsWith("/api/increment")) {
        // Get a specific agent instance
        const counter = await getAgentByName(env.CounterAgent, "shared-counter");
        const newCount = await counter.increment();
        return Response.json({ count: newCount });
      }
      // ...
    },
  };
  ```

## Troubleshooting

### Agent not found, or 404 errors

1. **Check the export** - Agent class must be exported from your main entry point.
2. **Check the binding** - `class_name` in the Wrangler configuration file must exactly match the exported class name.
3. **Check the route** - Default route is `/agents/{agent-name}/{instance-name}`.

### No such Durable Object class error

Add the migration to the Wrangler configuration file:

* wrangler.jsonc

  ```jsonc
  {
    "migrations": [
      {
        "tag": "v1",
        "new_sqlite_classes": ["YourAgentClass"],
      },
    ],
  }
  ```

* wrangler.toml

  ```toml
  [[migrations]]
  tag = "v1"
  new_sqlite_classes = [ "YourAgentClass" ]
  ```

### WebSocket connection fails

Ensure your routing passes the response unchanged:

* JavaScript

  ```js
  // Correct - return the response directly
  const agentResponse = await routeAgentRequest(request, env);
  if (agentResponse) return agentResponse;


  // Wrong - this breaks WebSocket connections
  if (agentResponse) return new Response(agentResponse.body);
  ```

* TypeScript

  ```ts
  // Correct - return the response directly
  const agentResponse = await routeAgentRequest(request, env);
  if (agentResponse) return agentResponse;


  // Wrong - this breaks WebSocket connections
  if (agentResponse) return new Response(agentResponse.body);
  ```

### State not persisting

Check that:

1. You are using `this.setState()`, not mutating `this.state` directly.
2. The agent class is in `new_sqlite_classes` in migrations.
3. You are connecting to the same agent instance name.

## Next steps

[State management](https://developers.cloudflare.com/agents/api-reference/store-and-sync-state/)Manage and synchronize agent state.

[Schedule tasks](https://developers.cloudflare.com/agents/api-reference/schedule-tasks/)Background tasks and cron jobs.

[Agent class internals](https://developers.cloudflare.com/agents/concepts/agent-class/)Full lifecycle and methods reference.

[Agents API](https://developers.cloudflare.com/agents/api-reference/agents-api/)Complete API reference for the Agents SDK.
