# Source: https://docs.augmentcode.com/context-services/context-connectors/advanced/custom-indexer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Indexer

> Build a custom indexer for any data source using DirectContext

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

Build a custom indexer to fetch content from any source (API, database, CMS) and index it with DirectContext.

## Basic Example

<Tabs>
  <Tab title="TypeScript">
    ```typescript  theme={null}
    import { Indexer, FilesystemStore } from "@augmentcode/context-connectors";
    import type { Source, FileEntry, FileChanges, SourceMetadata, FileInfo } from "@augmentcode/context-connectors";

    // Implement the Source interface for your data source
    class ApiSource implements Source {
      readonly type = "custom" as const;

      async fetchAll(): Promise<FileEntry[]> {
        // Replace with your actual data source (API, database, CMS, etc.)
        const response = await fetch("https://api.example.com/docs");
        const docs = await response.json();
        return docs.map((doc: any) => ({
          path: doc.path,
          contents: doc.content,
        }));
      }

      async fetchChanges(previous: SourceMetadata): Promise<FileChanges | null> {
        // Return null to always do full re-index
        // Or implement incremental updates based on your data source
        return null;
      }

      async getMetadata(): Promise<SourceMetadata> {
        return {
          type: "custom",
          identifier: "api-docs",
          ref: new Date().toISOString(),
          syncedAt: new Date().toISOString(),
        };
      }

      async listFiles(directory?: string): Promise<FileInfo[]> {
        const files = await this.fetchAll();
        return files.map(f => ({ path: f.path, type: "file" as const }));
      }

      async readFile(path: string): Promise<string | null> {
        const files = await this.fetchAll();
        return files.find(f => f.path === path)?.contents ?? null;
      }
    }

    // Usage
    const source = new ApiSource();
    const store = new FilesystemStore({ basePath: "./indexes" });
    const indexer = new Indexer();

    const result = await indexer.index(source, store, "my-docs");
    console.log(`Indexed ${result.filesIndexed} files (${result.type})`);
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    from auggie_sdk.context import DirectContext, File
    import json
    import os
    from pathlib import Path

    class CustomIndexer:
        def __init__(self, store_path: str = None):
            self.store_path = store_path

        def fetch_files(self):
            """Fetch from your data source (API, database, CMS, etc.)"""
            # Replace with your actual data source
            return [
                File(path='docs/intro.md', contents='# Introduction\n...'),
                File(path='docs/api.md', contents='# API Reference\n...'),
            ]

        def index(self, index_name: str):
            index_dir = os.path.join(self.store_path, index_name)
            state_file = os.path.join(index_dir, 'state.json')

            # Load existing or create new context
            if os.path.exists(state_file):
                context = DirectContext.import_from_file(state_file)
            else:
                context = DirectContext.create()

            # Fetch and index files
            files = self.fetch_files()

            # Handle incremental updates
            indexed_paths = set(context.get_indexed_paths())
            current_paths = {f.path for f in files}
            paths_to_remove = [p for p in indexed_paths if p not in current_paths]

            if paths_to_remove:
                context.remove_from_index(paths_to_remove)

            context.add_to_index(files)

            # Export both full and search-only states
            full_state = context.export(mode='full')
            search_state = context.export(mode='search-only')

            # Save both files
            Path(index_dir).mkdir(parents=True, exist_ok=True)

            with open(os.path.join(index_dir, 'state.json'), 'w') as f:
                json.dump(full_state, f, indent=2)

            with open(os.path.join(index_dir, 'search.json'), 'w') as f:
                json.dump(search_state, f, indent=2)

    # Usage
    indexer = CustomIndexer(store_path='./indexes')
    indexer.index('my-docs')
    ```
  </Tab>
</Tabs>

<Note>
  **Index Layout:** The indexer saves two files:

  * `state.json` - Full state including file path list (for incremental indexing)
  * `search.json` - Optimized state without file list (smaller, for search clients)

  Search clients should load `search.json`. Indexers need `state.json` for incremental updates.
</Note>

## Data Source Examples

<Tabs>
  <Tab title="TypeScript">
    **REST API:**

    ```typescript  theme={null}
    async fetchAll(): Promise<FileEntry[]> {
      const response = await fetch("https://api.example.com/docs");
      const docs = await response.json();
      return docs.map((doc: any) => ({ path: doc.path, contents: doc.content }));
    }
    ```

    **Database:**

    ```typescript  theme={null}
    async fetchAll(): Promise<FileEntry[]> {
      const docs = await db.query("SELECT path, content FROM documents");
      return docs.map(doc => ({ path: doc.path, contents: doc.content }));
    }
    ```
  </Tab>

  <Tab title="Python">
    **REST API:**

    ```python  theme={null}
    def fetch_files(self):
        response = requests.get('https://api.example.com/docs')
        return [File(path=doc['path'], contents=doc['content']) for doc in response.json()]
    ```

    **Database:**

    ```python  theme={null}
    def fetch_files(self):
        docs = db.query('SELECT path, content FROM documents')
        return [File(path=doc.path, contents=doc.content) for doc in docs]
    ```
  </Tab>
</Tabs>

## Automation

**Cron (Node.js):**

```bash  theme={null}
0 * * * * cd /path/to/project && npx tsx indexer.ts
```

**Cron (Python):**

```bash  theme={null}
0 * * * * cd /path/to/project && python indexer.py
```

**GitHub Actions:** See [GitHub Actions Auto-Indexing](/context-services/context-connectors/quickstart/github-actions-indexing)

## Next Steps

* [Custom Store](/context-services/context-connectors/advanced/custom-store) - Custom storage backends
* [Custom Client](/context-services/context-connectors/advanced/custom-client) - Build search clients
* [DirectContext API Reference](/context-services/sdk/api-reference) - Complete API docs
