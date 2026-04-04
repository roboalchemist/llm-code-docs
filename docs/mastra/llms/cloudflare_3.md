# Source: https://mastra.ai/reference/storage/cloudflare

# Cloudflare Storage

The Cloudflare KV storage implementation provides a globally distributed, serverless key-value store solution using Cloudflare Workers KV.

> **Observability Not Supported:** Cloudflare KV storage **doesn't support the observability domain**. Traces from the `DefaultExporter` can't be persisted to KV, and Mastra Studio's observability features won't work with Cloudflare KV as your only storage provider. To enable observability, use [composite storage](https://mastra.ai/reference/storage/composite) to route observability data to a supported provider like ClickHouse or PostgreSQL.

## Installation

**npm**:

```bash
npm install @mastra/cloudflare@latest
```

**pnpm**:

```bash
pnpm add @mastra/cloudflare@latest
```

**Yarn**:

```bash
yarn add @mastra/cloudflare@latest
```

**Bun**:

```bash
bun add @mastra/cloudflare@latest
```

## Usage

```typescript
import { CloudflareStore } from '@mastra/cloudflare'

// --- Example 1: Using Workers Binding ---
const storageWorkers = new CloudflareStore({
  id: 'cloudflare-workers-storage',
  bindings: {
    threads: THREADS_KV, // KVNamespace binding for threads table
    messages: MESSAGES_KV, // KVNamespace binding for messages table
    // Add other tables as needed
  },
  keyPrefix: 'dev_', // Optional: isolate keys per environment
})

// --- Example 2: Using REST API ---
const storageRest = new CloudflareStore({
  id: 'cloudflare-rest-storage',
  accountId: process.env.CLOUDFLARE_ACCOUNT_ID!, // Cloudflare Account ID
  apiToken: process.env.CLOUDFLARE_API_TOKEN!, // Cloudflare API Token
  namespacePrefix: 'dev_', // Optional: isolate namespaces per environment
})
```

## Parameters

**id** (`string`): Unique identifier for this storage instance.

**bindings** (`Record<string, KVNamespace>`): Cloudflare Workers KV bindings (for Workers runtime)

**accountId** (`string`): Cloudflare Account ID (for REST API)

**apiToken** (`string`): Cloudflare API Token (for REST API)

**namespacePrefix** (`string`): Optional prefix for all namespace names (useful for environment isolation)

**keyPrefix** (`string`): Optional prefix for all keys (useful for environment isolation)

### Additional Notes

### Schema Management

The storage implementation handles schema creation and updates automatically. It creates the following tables:

- `threads`: Stores conversation threads
- `messages`: Stores individual messages
- `metadata`: Stores additional metadata for threads and messages

### Consistency & Propagation

Cloudflare KV is an eventually consistent store, meaning that data may not be immediately available across all regions after a write.

### Key Structure & Namespacing

Keys in Cloudflare KV are structured as a combination of a configurable prefix and a table-specific format (e.g., `threads:threadId`). For Workers deployments, `keyPrefix` is used to isolate data within a namespace; for REST API deployments, `namespacePrefix` is used to isolate entire namespaces between environments or applications.