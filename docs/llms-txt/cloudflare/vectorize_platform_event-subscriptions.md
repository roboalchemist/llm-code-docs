# Source: https://developers.cloudflare.com/vectorize/platform/event-subscriptions/index.md

---

title: Event subscriptions · Cloudflare Vectorize docs
description: Event subscriptions allow you to receive messages when events occur
  across your Cloudflare account. Cloudflare products (e.g., KV, Workers AI,
  Workers) can publish structured events to a queue, which you can then consume
  with Workers or HTTP pull consumers to build custom workflows, integrations,
  or logic.
lastUpdated: 2025-11-06T01:33:23.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/vectorize/platform/event-subscriptions/
  md: https://developers.cloudflare.com/vectorize/platform/event-subscriptions/index.md
---

[Event subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/) allow you to receive messages when events occur across your Cloudflare account. Cloudflare products (e.g., [KV](https://developers.cloudflare.com/kv/), [Workers AI](https://developers.cloudflare.com/workers-ai/), [Workers](https://developers.cloudflare.com/workers/)) can publish structured events to a [queue](https://developers.cloudflare.com/queues/), which you can then consume with Workers or [HTTP pull consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers/) to build custom workflows, integrations, or logic.

For more information on [Event Subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/), refer to the [management guide](https://developers.cloudflare.com/queues/event-subscriptions/manage-event-subscriptions/).

## Available Vectorize events

#### `index.created`

Triggered when an index is created.

**Example:**

```json
{
  "type": "cf.vectorize.index.created",
  "source": {
    "type": "vectorize"
  },
  "payload": {
    "name": "my-vector-index",
    "description": "Index for embeddings",
    "createdAt": "2025-05-01T02:48:57.132Z",
    "modifiedAt": "2025-05-01T02:48:57.132Z",
    "dimensions": 1536,
    "metric": "cosine"
  },
  "metadata": {
    "accountId": "f9f79265f388666de8122cfb508d7776",
    "eventSubscriptionId": "1830c4bb612e43c3af7f4cada31fbf3f",
    "eventSchemaVersion": 1,
    "eventTimestamp": "2025-05-01T02:48:57.132Z"
  }
}
```

#### `index.deleted`

Triggered when an index is deleted.

**Example:**

```json
{
  "type": "cf.vectorize.index.deleted",
  "source": {
    "type": "vectorize"
  },
  "payload": {
    "name": "my-vector-index"
  },
  "metadata": {
    "accountId": "f9f79265f388666de8122cfb508d7776",
    "eventSubscriptionId": "1830c4bb612e43c3af7f4cada31fbf3f",
    "eventSchemaVersion": 1,
    "eventTimestamp": "2025-05-01T02:48:57.132Z"
  }
}
```
