# Source: https://braintrust.dev/docs/integrations/sdk-integrations/apollo-graphql.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Apollo GraphQL

[Apollo GraphQL](https://www.apollographql.com/) is a platform for building GraphQL APIs. Braintrust traces Apollo GraphQL operations using OpenTelemetry to capture queries, mutations, resolvers, and errors.

## Setup

This integration uses Braintrust's [TypeScript SDK OpenTelemetry configuration](/integrations/sdk-integrations/opentelemetry#typescript-sdk-configuration).

Install the [Braintrust TypeScript SDK](/reference/sdks/typescript) with the following OpenTelemetry dependencies:

<CodeGroup>
  ```bash Typescript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  # pnpm
  pnpm add braintrust @braintrust/otel @opentelemetry/api @opentelemetry/sdk-node @opentelemetry/sdk-trace-base @apollo/server @opentelemetry/api @opentelemetry/sdk-trace-base @opentelemetry/exporter-trace-otlp-http @opentelemetry/resources @opentelemetry/semantic-conventions dotenv
  # npm
  npm install braintrust @braintrust/otel @opentelemetry/api @opentelemetry/sdk-node @opentelemetry/sdk-trace-base @apollo/server @opentelemetry/api @opentelemetry/sdk-trace-base @opentelemetry/exporter-trace-otlp-http @opentelemetry/resources @opentelemetry/semantic-conventions dotenv
  ```
</CodeGroup>

Configure your environment variables:

```bash title=".env" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
# Required
BRAINTRUST_API_KEY=your-api-key

# Parent identifier for organizing traces
# Format: project_name:experiment_name
BRAINTRUST_PARENT=project_name:apollo-graphql

# Optional: Custom OpenTelemetry endpoint (for self-hosted Braintrust)
# BRAINTRUST_OTEL_ENDPOINT=https://api.braintrust.dev/otel/v1/traces
```

## Trace with Apollo GraphQL

Configure OpenTelemetry with Braintrust's span processor and instrument your Apollo Server:

### Basic tracing

```typescript title="apollo-graphql-braintrust.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { trace } from "@opentelemetry/api";
import { SpanStatusCode } from "@opentelemetry/api";
import { BasicTracerProvider } from "@opentelemetry/sdk-trace-base";
import { resourceFromAttributes } from "@opentelemetry/resources";
import { ATTR_SERVICE_NAME } from '@opentelemetry/semantic-conventions';
import { BraintrustSpanProcessor } from "@braintrust/otel";

const provider = new BasicTracerProvider({
  resource: resourceFromAttributes({
    [ATTR_SERVICE_NAME]: "graphql-api",
  }),
  spanProcessors: [new BraintrustSpanProcessor()]
});

provider.register();

// Get a tracer for your GraphQL operations
const tracer = trace.getTracer("apollo-graphql", "1.0.0");

// Import Apollo Server
import { ApolloServer } from "@apollo/server";
import { startStandaloneServer } from "@apollo/server/standalone";

// Define your schema
const typeDefs = `#graphql
  type Query {
    hello(name: String): String!
    books: [Book!]!
    book(id: ID!): Book
  }

  type Book {
    id: ID!
    title: String!
    author: String!
    year: Int
  }

  type Mutation {
    addBook(title: String!, author: String!, year: Int): Book!
  }
`;

// Mock data functions (replace with your actual implementation)
async function fetchBooks() {
  return [
    {
      id: "1",
      title: "The Great Gatsby",
      author: "F. Scott Fitzgerald",
      year: 1925,
    },
    { id: "2", title: "1984", author: "George Orwell", year: 1949 },
  ];
}

async function fetchBookById(id: string) {
  const books = await fetchBooks();
  return books.find((book) => book.id === id);
}

async function createBook({
  title,
  author,
  year,
}: {
  title: string;
  author: string;
  year?: number;
}) {
  return {
    id: String(Date.now()),
    title,
    author,
    year: year || new Date().getFullYear(),
  };
}

// Implement resolvers with tracing
const resolvers = {
  Query: {
    hello: (_: any, { name }: { name?: string }) => {
      // Create a span for this resolver
      const span = tracer.startSpan("query.hello");
      span.setAttributes({
        "graphql.operation": "query",
        "graphql.field": "hello",
        "input.name": name || "undefined",
      });

      try {
        const result = `Hello, ${name || "World"}!`;
        span.setStatus({ code: SpanStatusCode.OK });
        return result;
      } catch (error) {
        span.recordException(error as Error);
        span.setStatus({ code: SpanStatusCode.ERROR });
        throw error;
      } finally {
        span.end();
      }
    },

    books: async () => {
      const span = tracer.startSpan("query.books");
      span.setAttributes({
        "graphql.operation": "query",
        "graphql.field": "books",
      });

      try {
        const books = await fetchBooks();
        span.setAttribute("books.count", books.length);
        span.setStatus({ code: SpanStatusCode.OK });
        return books;
      } catch (error) {
        span.recordException(error as Error);
        span.setStatus({ code: SpanStatusCode.ERROR });
        throw error;
      } finally {
        span.end();
      }
    },

    book: async (_: any, { id }: { id: string }) => {
      const span = tracer.startSpan("query.book");
      span.setAttributes({
        "graphql.operation": "query",
        "graphql.field": "book",
        "book.id": id,
      });

      try {
        const book = await fetchBookById(id);
        span.setAttribute("book.found", book ? "true" : "false");
        span.setStatus({ code: SpanStatusCode.OK });
        return book;
      } catch (error) {
        span.recordException(error as Error);
        span.setStatus({ code: SpanStatusCode.ERROR });
        throw error;
      } finally {
        span.end();
      }
    },
  },

  Mutation: {
    addBook: async (
      _: any,
      { title, author, year }: { title: string; author: string; year?: number },
    ) => {
      const span = tracer.startSpan("mutation.addBook");
      span.setAttributes({
        "graphql.operation": "mutation",
        "graphql.field": "addBook",
        "book.title": title,
        "book.author": author,
      });

      if (year) span.setAttribute("book.year", year);

      try {
        const newBook = await createBook({ title, author, year });
        span.setAttribute("book.id", newBook.id);
        span.setStatus({ code: SpanStatusCode.OK });
        return newBook;
      } catch (error) {
        span.recordException(error as Error);
        span.setStatus({ code: SpanStatusCode.ERROR });
        throw error;
      } finally {
        span.end();
      }
    },
  },
};

// Create and start Apollo Server
const server = new ApolloServer({ typeDefs, resolvers });

async function main() {
  const { url } = await startStandaloneServer(server, {
    listen: { port: 4000 },
    context: async ({ req }) => {
      // Create a root span for each GraphQL request
      const rootSpan = tracer.startSpan("graphql.request");
      rootSpan.setAttribute("http.method", req.method || "POST");
      rootSpan.setAttribute("http.url", req.url || "/graphql");

      // The span will be automatically exported when it ends
      // BraintrustSpanProcessor handles the batching and sending
      setTimeout(() => rootSpan.end(), 100);

      return {};
    },
  });

  console.log(`🚀 Server ready at: ${url}`);
}

main().catch(console.error);
```

### Apollo Router (Federation Gateway)

For Apollo Router, configure OpenTelemetry through the router configuration file:

```yaml title="apollo-router-braintrust.yaml" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
connectors:
  preview_connect_v0_3: true
  sources:
    # OpenAI API configuration
    openai:
      $config:
        apiKey: ${env.OPENAI_API_KEY}

# OpenTelemetry configuration for Braintrust
telemetry:
  exporters:
    tracing:
      # OTLP exporter for Braintrust
      otlp:
        enabled: true
        # Braintrust OTEL endpoint
        endpoint: ${env.BRAINTRUST_OTEL_ENDPOINT:-https://api.braintrust.dev/otel}
        # Use HTTP protocol for Braintrust
        protocol: http
        # HTTP configuration with headers for Braintrust
        http:
          headers:
            # Braintrust API authentication
            Authorization: Bearer ${env.BRAINTRUST_API_KEY}
            # Parent project/experiment for traces
            x-bt-parent: ${env.BRAINTRUST_PARENT:-project_name:apollo-graphql-project}
        # Batch processor configuration for optimal performance
        batch_processor:
          scheduled_delay: 5s
          max_concurrent_exports: 2
          max_export_batch_size: 512
          max_export_timeout: 30s
          max_queue_size: 2048

    metrics:
      # Prometheus endpoint for local debugging
      prometheus:
        enabled: true
        listen: 0.0.0.0:9090
        path: /metrics
      # Optional: OTLP metrics to Braintrust
      otlp:
        enabled: false
        endpoint: ${env.BRAINTRUST_OTEL_ENDPOINT:-https://api.braintrust.dev/otel}
        protocol: http
        http:
          headers:
            Authorization: Bearer ${env.BRAINTRUST_API_KEY}
            x-bt-parent: ${env.BRAINTRUST_PARENT:-project_name:apollo-graphql-project}

# Include subgraph errors in responses for debugging
include_subgraph_errors:
  all: true

# GraphQL query limits
limits:
  max_depth: 20
  max_height: 200
  max_aliases: 30
  max_root_fields: 30
```

## Resources

* [Apollo GraphQL documentation](https://www.apollographql.com/docs/)
* [Apollo Router documentation](https://www.apollographql.com/docs/router/)
* [Braintrust OpenTelemetry guide](/integrations/sdk-integrations/opentelemetry)
