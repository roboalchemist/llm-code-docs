# Source: https://docs.augmentcode.com/context-services/context-connectors/advanced/custom-store.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Store

> Create custom storage backends for your indexes

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

Create custom storage backends to save and load DirectContext state from local filesystem, S3, or any storage system.

## Local Filesystem Store

<Tabs>
  <Tab title="TypeScript">
    ```typescript  theme={null}
    import { promises as fs } from "node:fs";
    import { join } from "node:path";
    import type { IndexStore, IndexState, IndexStateSearchOnly } from "@augmentcode/context-connectors";

    class LocalStore implements IndexStore {
      constructor(private basePath: string = "./indexes") {}

      async save(key: string, fullState: IndexState, searchState: IndexStateSearchOnly): Promise<void> {
        const indexDir = join(this.basePath, key);
        await fs.mkdir(indexDir, { recursive: true });

        // Full state for incremental indexing
        await fs.writeFile(join(indexDir, "state.json"), JSON.stringify(fullState, null, 2));
        // Search-optimized state (smaller)
        await fs.writeFile(join(indexDir, "search.json"), JSON.stringify(searchState, null, 2));
      }

      async loadState(key: string): Promise<IndexState | null> {
        try {
          const data = await fs.readFile(join(this.basePath, key, "state.json"), "utf-8");
          return JSON.parse(data);
        } catch {
          return null;
        }
      }

      async loadSearch(key: string): Promise<IndexState | null> {
        try {
          const data = await fs.readFile(join(this.basePath, key, "search.json"), "utf-8");
          return JSON.parse(data);
        } catch {
          return null;
        }
      }

      async delete(key: string): Promise<void> {
        await fs.rm(join(this.basePath, key), { recursive: true, force: true });
      }

      async list(): Promise<string[]> {
        const entries = await fs.readdir(this.basePath, { withFileTypes: true });
        return entries.filter(e => e.isDirectory()).map(e => e.name);
      }
    }
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    import json
    import os
    from pathlib import Path

    class LocalStore:
        def __init__(self, base_path: str = None):
            self.base_path = base_path

        def save(self, index_name: str, full_state, search_state):
            """Save both full state and search-optimized state."""
            index_dir = os.path.join(self.base_path, index_name)
            Path(index_dir).mkdir(parents=True, exist_ok=True)

            # Full state for incremental indexing
            with open(os.path.join(index_dir, 'state.json'), 'w') as f:
                json.dump(full_state, f, indent=2)

            # Search-optimized state (smaller)
            with open(os.path.join(index_dir, 'search.json'), 'w') as f:
                json.dump(search_state, f, indent=2)

        def load_state(self, index_name: str):
            """Load full state for incremental indexing."""
            state_path = os.path.join(self.base_path, index_name, 'state.json')
            if not os.path.exists(state_path):
                return None
            with open(state_path, 'r') as f:
                return json.load(f)

        def load_search(self, index_name: str):
            """Load search-optimized state for search operations."""
            search_path = os.path.join(self.base_path, index_name, 'search.json')
            if not os.path.exists(search_path):
                return None
            with open(search_path, 'r') as f:
                return json.load(f)

    # Usage
    store = LocalStore(base_path='./indexes')
    context = DirectContext.create()
    context.add_to_index([File(path='file.py', contents='...')])

    # Export both states
    full_state = context.export(mode='full')
    search_state = context.export(mode='search-only')

    store.save('my-project', full_state, search_state)
    ```
  </Tab>
</Tabs>

## S3 Store

<Tabs>
  <Tab title="TypeScript">
    ```typescript  theme={null}
    import { S3Client, GetObjectCommand, PutObjectCommand } from "@aws-sdk/client-s3";
    import type { IndexStore, IndexState, IndexStateSearchOnly } from "@augmentcode/context-connectors";

    class S3Store implements IndexStore {
      private client: S3Client;

      constructor(
        private bucket: string,
        private prefix = "context-connectors/"
      ) {
        this.client = new S3Client({});
      }

      async save(key: string, fullState: IndexState, searchState: IndexStateSearchOnly): Promise<void> {
        await Promise.all([
          this.client.send(new PutObjectCommand({
            Bucket: this.bucket,
            Key: `${this.prefix}${key}/state.json`,
            Body: JSON.stringify(fullState, null, 2),
            ContentType: "application/json",
          })),
          this.client.send(new PutObjectCommand({
            Bucket: this.bucket,
            Key: `${this.prefix}${key}/search.json`,
            Body: JSON.stringify(searchState, null, 2),
            ContentType: "application/json",
          })),
        ]);
      }

      async loadState(key: string): Promise<IndexState | null> {
        try {
          const response = await this.client.send(new GetObjectCommand({
            Bucket: this.bucket,
            Key: `${this.prefix}${key}/state.json`,
          }));
          const body = await response.Body?.transformToString();
          return body ? JSON.parse(body) : null;
        } catch {
          return null;
        }
      }

      async loadSearch(key: string): Promise<IndexState | null> {
        try {
          const response = await this.client.send(new GetObjectCommand({
            Bucket: this.bucket,
            Key: `${this.prefix}${key}/search.json`,
          }));
          const body = await response.Body?.transformToString();
          return body ? JSON.parse(body) : null;
        } catch {
          return null;
        }
      }

      // ... delete() and list() implementations
    }

    // Usage
    const store = new S3Store("my-bucket");
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    import boto3
    import json

    class S3Store:
        def __init__(self, bucket: str, prefix: str = 'context-connectors/'):
            self.s3 = boto3.client('s3')
            self.bucket = bucket
            self.prefix = prefix

        def save(self, index_name: str, full_state, search_state):
            """Save both full state and search-optimized state."""
            state_key = f'{self.prefix}{index_name}/state.json'
            search_key = f'{self.prefix}{index_name}/search.json'

            self.s3.put_object(
                Bucket=self.bucket,
                Key=state_key,
                Body=json.dumps(full_state, indent=2)
            )
            self.s3.put_object(
                Bucket=self.bucket,
                Key=search_key,
                Body=json.dumps(search_state, indent=2)
            )

        def load_state(self, index_name: str):
            """Load full state for incremental indexing."""
            key = f'{self.prefix}{index_name}/state.json'
            try:
                response = self.s3.get_object(Bucket=self.bucket, Key=key)
                return json.loads(response['Body'].read())
            except self.s3.exceptions.NoSuchKey:
                return None

        def load_search(self, index_name: str):
            """Load search-optimized state for search operations."""
            key = f'{self.prefix}{index_name}/search.json'
            try:
                response = self.s3.get_object(Bucket=self.bucket, Key=key)
                return json.loads(response['Body'].read())
            except self.s3.exceptions.NoSuchKey:
                return None

    # Usage
    store = S3Store('my-bucket')
    store.save('my-project', full_state, search_state)
    ```
  </Tab>
</Tabs>

<Note>
  **Built-in S3 Store:** The `@augmentcode/context-connectors` package includes a built-in `S3Store` class. Use it directly:

  ```typescript  theme={null}
  import { S3Store } from "@augmentcode/context-connectors";
  const store = new S3Store({ bucket: "my-bucket" });
  ```
</Note>

## Other Storage Examples

<Tabs>
  <Tab title="TypeScript">
    **Redis:**

    ```typescript  theme={null}
    import { createClient } from "redis";
    import type { IndexStore, IndexState, IndexStateSearchOnly } from "@augmentcode/context-connectors";

    class RedisStore implements IndexStore {
      constructor(private redis: ReturnType<typeof createClient>) {}

      async save(key: string, fullState: IndexState, searchState: IndexStateSearchOnly): Promise<void> {
        await Promise.all([
          this.redis.set(`context:${key}:state`, JSON.stringify(fullState)),
          this.redis.set(`context:${key}:search`, JSON.stringify(searchState)),
        ]);
      }

      async loadState(key: string): Promise<IndexState | null> {
        const data = await this.redis.get(`context:${key}:state`);
        return data ? JSON.parse(data) : null;
      }

      async loadSearch(key: string): Promise<IndexState | null> {
        const data = await this.redis.get(`context:${key}:search`);
        return data ? JSON.parse(data) : null;
      }
      // ... delete() and list() implementations
    }
    ```
  </Tab>

  <Tab title="Python">
    **Redis:**

    ```python  theme={null}
    class RedisStore:
        def save(self, index_name: str, full_state, search_state):
            self.redis.set(f'context:{index_name}:state', json.dumps(full_state))
            self.redis.set(f'context:{index_name}:search', json.dumps(search_state))

        def load_state(self, index_name: str):
            data = self.redis.get(f'context:{index_name}:state')
            return json.loads(data) if data else None

        def load_search(self, index_name: str):
            data = self.redis.get(f'context:{index_name}:search')
            return json.loads(data) if data else None
    ```

    **Database:**

    ```python  theme={null}
    class DatabaseStore:
        def save(self, index_name: str, full_state, search_state):
            self.db.execute('''
                INSERT INTO indexes (name, full_state, search_state)
                VALUES (%s, %s, %s)
                ON CONFLICT (name) DO UPDATE
                SET full_state = %s, search_state = %s
            ''', [index_name, json.dumps(full_state), json.dumps(search_state),
                  json.dumps(full_state), json.dumps(search_state)])

        def load_state(self, index_name: str):
            row = self.db.query_one('SELECT full_state FROM indexes WHERE name = %s', [index_name])
            return json.loads(row['full_state']) if row else None

        def load_search(self, index_name: str):
            row = self.db.query_one('SELECT search_state FROM indexes WHERE name = %s', [index_name])
            return json.loads(row['search_state']) if row else None
    ```
  </Tab>
</Tabs>

## Index File Layout

Each index consists of two files:

| File          | Purpose                    | Size    | Used By                            |
| ------------- | -------------------------- | ------- | ---------------------------------- |
| `state.json`  | Full state with file paths | Larger  | Indexers (for incremental updates) |
| `search.json` | Search-optimized state     | Smaller | Search clients                     |

The `search.json` file excludes the blobs array (list of indexed file paths), making it much smaller for search-only use cases. Indexers need the full `state.json` to determine which files have changed for incremental updates.

## Next Steps

* [Custom Indexer](/context-services/context-connectors/advanced/custom-indexer) - Build custom indexers
* [Custom Client](/context-services/context-connectors/advanced/custom-client) - Build search clients
* [Store Indexes in S3](/context-services/context-connectors/quickstart/share-with-s3) - S3 storage guide
