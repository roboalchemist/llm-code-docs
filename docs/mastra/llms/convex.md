# Source: https://mastra.ai/reference/storage/convex

# Convex Storage

The Convex storage implementation provides a serverless storage solution using [Convex](https://convex.dev), a full-stack TypeScript development platform with real-time sync and automatic caching.

> **Observability Not Supported:** Convex storage **doesn't support the observability domain**. Traces from the `DefaultExporter` can't be persisted to Convex, and Mastra Studio's observability features won't work with Convex as your only storage provider. To enable observability, use [composite storage](https://mastra.ai/reference/storage/composite) to route observability data to a supported provider like ClickHouse or PostgreSQL.

> **Record Size Limit:** Convex enforces a **1 MiB maximum record size**. This limit can be exceeded when storing messages with base64-encoded attachments such as images. See [Handling large attachments](https://mastra.ai/docs/memory/storage) for workarounds including uploading attachments to external storage like S3, Cloudflare R2, or [Convex file storage](https://docs.convex.dev/file-storage).

## Installation

**npm**:

```bash
npm install @mastra/convex@latest
```

**pnpm**:

```bash
pnpm add @mastra/convex@latest
```

**Yarn**:

```bash
yarn add @mastra/convex@latest
```

**Bun**:

```bash
bun add @mastra/convex@latest
```

## Convex Setup

Before using `ConvexStore`, you need to set up the Convex schema and storage handler in your Convex project.

### 1. Set up Convex Schema

In `convex/schema.ts`:

```typescript
import { defineSchema } from 'convex/server'
import {
  mastraThreadsTable,
  mastraMessagesTable,
  mastraResourcesTable,
  mastraWorkflowSnapshotsTable,
  mastraScoresTable,
  mastraVectorIndexesTable,
  mastraVectorsTable,
  mastraDocumentsTable,
} from '@mastra/convex/schema'

export default defineSchema({
  mastra_threads: mastraThreadsTable,
  mastra_messages: mastraMessagesTable,
  mastra_resources: mastraResourcesTable,
  mastra_workflow_snapshots: mastraWorkflowSnapshotsTable,
  mastra_scorers: mastraScoresTable,
  mastra_vector_indexes: mastraVectorIndexesTable,
  mastra_vectors: mastraVectorsTable,
  mastra_documents: mastraDocumentsTable,
})
```

### 2. Create the Storage Handler

In `convex/mastra/storage.ts`:

```typescript
import { mastraStorage } from '@mastra/convex/server'

export const handle = mastraStorage
```

### 3. Deploy to Convex

```bash
npx convex dev
# or for production
npx convex deploy
```

## Usage

```typescript
import { ConvexStore } from '@mastra/convex'

const storage = new ConvexStore({
  id: 'convex-storage',
  deploymentUrl: process.env.CONVEX_URL!,
  adminAuthToken: process.env.CONVEX_ADMIN_KEY!,
})
```

## Parameters

**deploymentUrl** (`string`): Convex deployment URL (e.g., https\://your-project.convex.cloud)

**adminAuthToken** (`string`): Convex admin authentication token for backend access

**storageFunction** (`string`): Path to the storage mutation function (default: 'mastra/storage:handle') (Default: `mastra/storage:handle`)

## Constructor Examples

```ts
import { ConvexStore } from '@mastra/convex'

// Basic configuration
const store = new ConvexStore({
  id: 'convex-storage',
  deploymentUrl: 'https://your-project.convex.cloud',
  adminAuthToken: 'your-admin-token',
})

// With custom storage function path
const storeCustom = new ConvexStore({
  id: 'convex-storage',
  deploymentUrl: 'https://your-project.convex.cloud',
  adminAuthToken: 'your-admin-token',
  storageFunction: 'custom/path:handler',
})
```

## Additional Notes

### Schema Management

The storage implementation uses typed Convex tables for each Mastra domain:

| Domain    | Convex Table                | Purpose              |
| --------- | --------------------------- | -------------------- |
| Threads   | `mastra_threads`            | Conversation threads |
| Messages  | `mastra_messages`           | Chat messages        |
| Resources | `mastra_resources`          | User working memory  |
| Workflows | `mastra_workflow_snapshots` | Workflow state       |
| Scorers   | `mastra_scorers`            | Evaluation data      |
| Fallback  | `mastra_documents`          | Unknown tables       |

### Architecture

All typed tables include:

- An `id` field for Mastra's record ID (distinct from Convex's auto-generated `_id`)
- A `by_record_id` index for efficient lookups by Mastra ID

This design ensures compatibility with Mastra's storage contract while leveraging Convex's automatic indexing and real-time capabilities.

### Environment Variables

Set these environment variables for your deployment:

- `CONVEX_URL` – Your Convex deployment URL
- `CONVEX_ADMIN_KEY` – Admin authentication token (get from Convex dashboard)

## Related

- [Convex Vector Store](https://mastra.ai/reference/vectors/convex)
- [Convex Documentation](https://docs.convex.dev/)