# Source: https://mastra.ai/reference/vectors/convex

# Convex Vector Store

The ConvexVector class provides vector storage and similarity search using [Convex](https://convex.dev). It stores embeddings inside Convex and performs cosine similarity search.

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

Before using `ConvexVector`, you need to set up the Convex schema and storage handler. See [Convex Storage Setup](https://mastra.ai/reference/storage/convex) for setup instructions.

## Constructor Options

**deploymentUrl** (`string`): Convex deployment URL (e.g., https\://your-project.convex.cloud)

**adminAuthToken** (`string`): Convex admin authentication token

**storageFunction** (`string`): Path to the storage mutation function (Default: `mastra/storage:handle`)

## Constructor Examples

### Basic Configuration

```ts
import { ConvexVector } from '@mastra/convex'

const vectorStore = new ConvexVector({
  id: 'convex-vectors',
  deploymentUrl: 'https://your-project.convex.cloud',
  adminAuthToken: 'your-admin-token',
})
```

### Custom Storage Function

```ts
const vectorStore = new ConvexVector({
  id: 'convex-vectors',
  deploymentUrl: 'https://your-project.convex.cloud',
  adminAuthToken: 'your-admin-token',
  storageFunction: 'custom/path:handler',
})
```

## Methods

### createIndex()

**indexName** (`string`): Name of the index to create

**dimension** (`number`): Vector dimension (must match your embedding model)

**metric** (`'cosine' | 'euclidean' | 'dotproduct'`): Distance metric for similarity search (only cosine is currently supported) (Default: `cosine`)

```typescript
await vectorStore.createIndex({
  indexName: 'my_vectors',
  dimension: 1536,
})
```

### upsert()

**indexName** (`string`): Name of the index to upsert vectors into

**vectors** (`number[][]`): Array of embedding vectors

**metadata** (`Record<string, any>[]`): Metadata for each vector

**ids** (`string[]`): Optional vector IDs (auto-generated if not provided)

```typescript
await vectorStore.upsert({
  indexName: "my_vectors",
  vectors: [[0.1, 0.2, 0.3, ...]],
  metadata: [{ label: "example" }],
  ids: ["vec-1"],
});
```

### query()

**indexName** (`string`): Name of the index to query

**queryVector** (`number[]`): Query vector

**topK** (`number`): Number of results to return (Default: `10`)

**filter** (`Record<string, any>`): Metadata filters

**includeVector** (`boolean`): Whether to include the vector in the result (Default: `false`)

```typescript
const results = await vectorStore.query({
  indexName: "my_vectors",
  queryVector: [0.1, 0.2, 0.3, ...],
  topK: 5,
  filter: { category: "documents" },
});
```

### listIndexes()

Returns an array of index names as strings.

```typescript
const indexes = await vectorStore.listIndexes()
// ["my_vectors", "embeddings", ...]
```

### describeIndex()

**indexName** (`string`): Name of the index to describe

Returns:

```typescript
interface IndexStats {
  dimension: number
  count: number
  metric: 'cosine' | 'euclidean' | 'dotproduct'
}
```

### deleteIndex()

**indexName** (`string`): Name of the index to delete

Deletes the index and all its vectors.

```typescript
await vectorStore.deleteIndex({ indexName: 'my_vectors' })
```

### updateVector()

Update a single vector by ID or by metadata filter. Either `id` or `filter` must be provided, but not both.

**indexName** (`string`): Name of the index containing the vector

**id** (`string`): ID of the vector to update (mutually exclusive with filter)

**filter** (`Record<string, any>`): Metadata filter to identify vector(s) to update (mutually exclusive with id)

**update** (`{ vector?: number[]; metadata?: Record<string, any>; }`): Object containing the vector and/or metadata to update

```typescript
// Update by ID
await vectorStore.updateVector({
  indexName: 'my_vectors',
  id: 'vector123',
  update: {
    vector: [0.1, 0.2, 0.3],
    metadata: { label: 'updated' },
  },
})

// Update by filter
await vectorStore.updateVector({
  indexName: 'my_vectors',
  filter: { category: 'product' },
  update: {
    metadata: { status: 'reviewed' },
  },
})
```

### deleteVector()

**indexName** (`string`): Name of the index containing the vector

**id** (`string`): ID of the vector to delete

```typescript
await vectorStore.deleteVector({ indexName: 'my_vectors', id: 'vector123' })
```

### deleteVectors()

Delete multiple vectors by IDs or by metadata filter. Either `ids` or `filter` must be provided, but not both.

**indexName** (`string`): Name of the index containing the vectors to delete

**ids** (`string[]`): Array of vector IDs to delete (mutually exclusive with filter)

**filter** (`Record<string, any>`): Metadata filter to identify vectors to delete (mutually exclusive with ids)

```typescript
// Delete by IDs
await vectorStore.deleteVectors({
  indexName: 'my_vectors',
  ids: ['vec1', 'vec2', 'vec3'],
})

// Delete by filter
await vectorStore.deleteVectors({
  indexName: 'my_vectors',
  filter: { status: 'archived' },
})
```

## Response Types

Query results are returned in this format:

```typescript
interface QueryResult {
  id: string
  score: number
  metadata: Record<string, any>
  vector?: number[] // Only included if includeVector is true
}
```

## Metadata Filtering

ConvexVector supports metadata filtering with various operators:

```typescript
// Simple equality
const results = await vectorStore.query({
  indexName: 'my_vectors',
  queryVector: embedding,
  filter: { category: 'documents' },
})

// Comparison operators
const results = await vectorStore.query({
  indexName: 'my_vectors',
  queryVector: embedding,
  filter: {
    price: { $gt: 100 },
    status: { $in: ['active', 'pending'] },
  },
})

// Logical operators
const results = await vectorStore.query({
  indexName: 'my_vectors',
  queryVector: embedding,
  filter: {
    $and: [{ category: 'electronics' }, { price: { $lte: 500 } }],
  },
})
```

### Supported Filter Operators

| Operator | Description           |
| -------- | --------------------- |
| `$eq`    | Equal to              |
| `$ne`    | Not equal to          |
| `$gt`    | Greater than          |
| `$gte`   | Greater than or equal |
| `$lt`    | Less than             |
| `$lte`   | Less than or equal    |
| `$in`    | In array              |
| `$nin`   | Not in array          |
| `$and`   | Logical AND           |
| `$or`    | Logical OR            |

## Architecture

ConvexVector stores vectors in the `mastra_vectors` table with the following structure:

- `id`: Unique vector identifier
- `indexName`: Name of the index
- `embedding`: The vector data (array of floats)
- `metadata`: Optional JSON metadata

Vector similarity search is performed using cosine similarity, computed in the Convex function.

## Related

- [Convex Storage](https://mastra.ai/reference/storage/convex)
- [Metadata Filters](https://mastra.ai/reference/rag/metadata-filters)
- [Convex Documentation](https://docs.convex.dev/)