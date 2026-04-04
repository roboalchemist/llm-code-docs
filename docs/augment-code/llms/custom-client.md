# Source: https://docs.augmentcode.com/context-services/context-connectors/advanced/custom-client.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Client

> Build custom search clients for your applications

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

Build custom search clients to load indexes and provide search functionality for web apps, CLIs, or serverless functions.

## Basic Search Client

<Tabs>
  <Tab title="TypeScript">
    ```typescript  theme={null}
    import { SearchClient, FilesystemStore } from "@augmentcode/context-connectors";

    // Create a search client
    const client = new SearchClient({
      store: new FilesystemStore({ basePath: "./indexes" }),
      indexName: "my-docs",
    });

    // Initialize (loads index from store)
    await client.initialize();

    // Search
    const { results } = await client.search("authentication");
    console.log(results);

    // Ask a question about the search results
    const answer = await client.searchAndAsk(
      "authentication",
      "How does auth work?"
    );
    console.log(answer);
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    from auggie_sdk.context import DirectContext
    import os

    class SearchClient:
        def __init__(self, index_name: str, store_path: str = None):
            self.index_name = index_name
            self.store_path = store_path
            self.context = None

        def initialize(self):
            # Load search-optimized state (smaller, no file list)
            search_file = os.path.join(self.store_path, self.index_name, 'search.json')
            self.context = DirectContext.import_from_file(search_file)

        def search(self, query: str):
            return self.context.search(query)

        def ask(self, search_query: str, prompt: str = None):
            return self.context.search_and_ask(search_query, prompt)

    # Usage
    client = SearchClient('my-docs', store_path='./indexes')
    client.initialize()
    results = client.search('authentication')
    answer = client.ask('authentication', 'How does auth work?')
    ```
  </Tab>
</Tabs>

<Note>
  Search clients load `search.json` which is optimized for search operations.
  The full `state.json` file is only needed by indexers for incremental updates.
</Note>

## Web Application

<Tabs>
  <Tab title="TypeScript (Express)">
    ```typescript  theme={null}
    import express from "express";
    import { SearchClient, FilesystemStore } from "@augmentcode/context-connectors";

    const app = express();
    app.use(express.json());

    // Initialize client at startup
    const client = new SearchClient({
      store: new FilesystemStore(),
      indexName: "my-docs",
    });
    await client.initialize();

    app.post("/api/search", async (req, res) => {
      const { query } = req.body;
      const { results } = await client.search(query);
      res.json({ results });
    });

    app.post("/api/ask", async (req, res) => {
      const { query, question } = req.body;
      const answer = await client.searchAndAsk(query, question);
      res.json({ answer });
    });

    app.listen(3000);
    ```
  </Tab>

  <Tab title="Python (Flask)">
    ```python  theme={null}
    from flask import Flask, request, jsonify

    app = Flask(__name__)
    client = SearchClient('my-docs')
    client.initialize()

    @app.post('/api/search')
    def search():
        query = request.json['query']
        results = client.search(query)
        return jsonify({'results': results})

    @app.post('/api/ask')
    def ask():
        query = request.json['query']
        prompt = request.json.get('prompt')
        answer = client.ask(query, prompt)
        return jsonify({'answer': answer})
    ```
  </Tab>
</Tabs>

## CLI Client

<Tabs>
  <Tab title="TypeScript">
    ```typescript  theme={null}
    import { program } from "commander";
    import { SearchClient, FilesystemStore } from "@augmentcode/context-connectors";

    program
      .command("search <query>")
      .option("-i, --index <name>", "Index name", "my-project")
      .action(async (query, options) => {
        const client = new SearchClient({
          store: new FilesystemStore(),
          indexName: options.index,
        });
        await client.initialize();
        const { results } = await client.search(query);
        console.log(results);
      });

    program
      .command("ask <query>")
      .option("-i, --index <name>", "Index name", "my-project")
      .option("-q, --question <question>", "Question to ask")
      .action(async (query, options) => {
        const client = new SearchClient({
          store: new FilesystemStore(),
          indexName: options.index,
        });
        await client.initialize();
        const answer = await client.searchAndAsk(query, options.question);
        console.log(answer);
      });

    program.parse();
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    import click

    @click.group()
    def cli():
        pass

    @cli.command()
    @click.argument('query')
    @click.option('--index', default='my-project')
    def search(query, index):
        client = SearchClient(index)
        client.initialize()
        print(client.search(query))

    @cli.command()
    @click.argument('query')
    @click.option('--index', default='my-project')
    @click.option('--prompt')
    def ask(query, index, prompt):
        client = SearchClient(index)
        client.initialize()
        print(client.ask(query, prompt))

    if __name__ == '__main__':
        cli()
    ```
  </Tab>
</Tabs>

## Serverless Function

<Tabs>
  <Tab title="TypeScript (AWS Lambda)">
    ```typescript  theme={null}
    import { SearchClient, S3Store } from "@augmentcode/context-connectors";

    let client: SearchClient | null = null;

    async function getClient() {
      if (!client) {
        client = new SearchClient({
          store: new S3Store({ bucket: "my-indexes" }),
          indexName: "my-docs",
        });
        await client.initialize();
      }
      return client;
    }

    export async function handler(event: any) {
      const body = JSON.parse(event.body || "{}");
      const { query } = body;

      const client = await getClient();
      const { results } = await client.search(query);

      return {
        statusCode: 200,
        body: JSON.stringify({ results }),
      };
    }
    ```
  </Tab>

  <Tab title="Python (AWS Lambda)">
    ```python  theme={null}
    import json

    client = None

    def get_client():
        global client
        if client is None:
            client = SearchClient('my-docs')
            client.initialize()
        return client

    def lambda_handler(event, context):
        body = json.loads(event.get('body', '{}'))
        query = body.get('query')

        client = get_client()
        results = client.search(query)

        return {
            'statusCode': 200,
            'body': json.dumps({'results': results})
        }
    ```
  </Tab>
</Tabs>

## Next Steps

* [Custom Indexer](/context-services/context-connectors/advanced/custom-indexer) - Build custom indexers
* [Custom Store](/context-services/context-connectors/advanced/custom-store) - Custom storage backends
* [DirectContext API Reference](/context-services/sdk/api-reference) - Complete API docs
