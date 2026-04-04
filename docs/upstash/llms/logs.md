# Source: https://upstash.com/docs/workflow/rest/runs/logs.md

# Source: https://upstash.com/docs/workflow/basics/client/logs.md

# Source: https://upstash.com/docs/qstash/sdks/ts/examples/logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Logs

#### Get all logs with pagination using cursor

Since there can be a large number of logs, they are paginated.
You can go through the results using the `cursor`.

```typescript  theme={"system"}
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const logs = [];
let cursor = null;
while (true) {
  const res = await client.logs({ cursor });
  logs.push(...res.logs);
  cursor = res.cursor;
  if (!cursor) {
    break;
  }
}
```

#### Filter logs by state and only return the first 50.

<Info>
  More filters can be found in the [API Reference](/qstash/api/events/list).
</Info>

```typescript  theme={"system"}
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const res = await client.logs({ 
  filter: {
    state: "DELIVERED",
    count: 50
  }
});
```
