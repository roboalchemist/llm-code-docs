# Source: https://braintrust.dev/docs/instrument/custom-tracing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add custom tracing

> Manually instrument application logic beyond LLM calls

While [AI provider wrappers](/instrument/wrap-providers) automatically log LLM calls, you often need to trace additional application logic like data retrieval, preprocessing, business logic, or tool invocations. Custom tracing lets you capture these operations.

## Trace function calls

Braintrust SDKs provide tools to trace function execution and capture inputs, outputs, and errors:

* **Python SDK** uses the `@traced` decorator to automatically wrap functions
* **TypeScript SDK** uses `wrapTraced()` to create traced function wrappers
* **Go SDK** uses OpenTelemetry's manual span management with `tracer.Start()` and `span.End()`

All approaches achieve the same result—capturing function-level observability—but with different ergonomics suited to each language's idioms.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { initLogger, wrapTraced } from "braintrust";

  const logger = initLogger({ projectName: "My Project" });

  // Wrap a function to trace it automatically
  const fetchUserData = wrapTraced(async function fetchUserData(userId: string) {
    // This function's input (userId) and output (return value) are logged
    const response = await fetch(`/api/users/${userId}`);
    return response.json();
  });

  // Use the function normally
  const userData = await fetchUserData("user-123");
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import init_logger, traced

  logger = init_logger(project="My Project")

  # Decorate a function to trace it automatically
  @traced
  def fetch_user_data(user_id: str):
      # This function's input (user_id) and output (return value) are logged
      response = requests.get(f"/api/users/{user_id}")
      return response.json()

  # Use the function normally
  user_data = fetch_user_data("user-123")
  ```

  ```go  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  package main

  import (
  	"context"
  	"fmt"
  	"go.opentelemetry.io/otel"
  	"go.opentelemetry.io/otel/attribute"
  )

  func fetchUserData(ctx context.Context, userID string) (map[string]interface{}, error) {
  	tracer := otel.Tracer("my-service")
  	ctx, span := tracer.Start(ctx, "fetchUserData")
  	defer span.End()

  	// Log input
  	span.SetAttributes(attribute.String("input.user_id", userID))

  	// Your application logic
  	userData := map[string]interface{}{"id": userID, "name": "John"}

  	// Log output
  	span.SetAttributes(attribute.String("output", fmt.Sprintf("%v", userData)))

  	return userData, nil
  }

  func main() {
  	// Use the function normally
  	userData, _ := fetchUserData(context.Background(), "user-123")
  	fmt.Println(userData)
  }
  ```
</CodeGroup>

The traced function automatically creates a span with:

* Function name as the span name
* Function arguments as input
* Return value as output
* Any errors that occur

## Add metadata and tags

Enrich spans with custom metadata and tags to make them easier to filter and analyze. Tags can be applied to any span in a trace, including nested spans, and are automatically aggregated at the trace level:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { initLogger, wrapTraced } from "braintrust";

  const logger = initLogger({ projectName: "My Project" });

  const processDocument = wrapTraced(async function processDocument(
    docId: string,
    span,
  ) {
    // Add custom metadata and tags
    span.log({
      metadata: {
        documentId: docId,
        processingType: "summarization",
        userId: "user-123",
      },
      tags: ["document-processing", "summarization"],
    });

    const doc = await loadDocument(docId);
    const summary = await summarize(doc);

    return summary;
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import init_logger, traced, current_span

  logger = init_logger(project="My Project")

  @traced
  def process_document(doc_id: str):
      # Get the current span
      span = current_span()

      # Add custom metadata and tags
      span.log(
          metadata={
              "document_id": doc_id,
              "processing_type": "summarization",
              "user_id": "user-123",
          },
          tags=["document-processing", "summarization"],
      )

      doc = load_document(doc_id)
      summary = summarize(doc)

      return summary
  ```

  ```go  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  package main

  import (
  	"context"
  	"go.opentelemetry.io/otel"
  	"go.opentelemetry.io/otel/attribute"
  )

  func processDocument(ctx context.Context, docID string) (string, error) {
  	tracer := otel.Tracer("my-service")
  	ctx, span := tracer.Start(ctx, "processDocument")
  	defer span.End()

  	// Add custom metadata
  	span.SetAttributes(
  		attribute.String("metadata.document_id", docID),
  		attribute.String("metadata.processing_type", "summarization"),
  		attribute.String("metadata.user_id", "user-123"),
  	)

  	// Add tags (using braintrust namespace for OTel)
  	span.SetAttributes(
  		attribute.StringSlice("braintrust.tags", []string{"document-processing", "summarization"}),
  	)

  	// Your logic here
  	summary := "Document summary"

  	return summary, nil
  }

  func main() {
  	summary, _ := processDocument(context.Background(), "doc-123")
  	_ = summary
  }
  ```

  ```csharp  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  using System;
  using System.Threading.Tasks;
  using Braintrust.Sdk;

  class Program
  {
      static async Task<string> LoadDocument(string docId)
      {
          // Your document loading logic here
          return "document content";
      }

      static async Task<string> Summarize(string doc)
      {
          // Your summarization logic here
          return "summary";
      }

      static async Task<string> ProcessDocument(string docId)
      {
          var activitySource = Braintrust.Sdk.Braintrust.Get().GetActivitySource();

          using var activity = activitySource.StartActivity("processDocument");

          // Add custom metadata
          activity?.SetTag("metadata.document_id", docId);
          activity?.SetTag("metadata.processing_type", "summarization");
          activity?.SetTag("metadata.user_id", "user-123");

          // Add tags
          activity?.SetTag("braintrust.tags", new[] { "document-processing", "summarization" });

          // Your logic here
          var doc = await LoadDocument(docId);
          var summary = await Summarize(doc);

          return summary;
      }

      static async Task Main(string[] args)
      {
          var summary = await ProcessDocument("doc-123");
          Console.WriteLine(summary);
      }
  }
  ```
</CodeGroup>

<Note>
  Tags from all spans in a trace are aggregated together at the trace level. When you log additional tags to the same span, they are automatically merged (union) rather than replaced, allowing you to add contextual tags throughout your application logic.
</Note>

## Manual spans

For more control, create spans manually using `logger.traced()` or `startSpan()`:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { initLogger } from "braintrust";

  const logger = initLogger({ projectName: "My Project" });

  async function complexWorkflow(input: string) {
    // Create a manual span
    await logger.traced(
      async (span) => {
        span.log({ input });

        // Step 1
        const data = await fetchData(input);
        span.log({ metadata: { step: "fetch", recordCount: data.length } });

        // Step 2
        const processed = await processData(data);
        span.log({ metadata: { step: "process" } });

        // Log final output
        span.log({ output: processed });
      },
      { name: "complexWorkflow", type: "task" },
    );
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import init_logger

  logger = init_logger(project="My Project")

  def complex_workflow(input_text: str):
      # Create a manual span
      with logger.start_span(name="complexWorkflow", span_attributes={"type": "task"}) as span:
          span.log(input=input_text)

          # Step 1
          data = fetch_data(input_text)
          span.log(metadata={"step": "fetch", "record_count": len(data)})

          # Step 2
          processed = process_data(data)
          span.log(metadata={"step": "process"})

          # Log final output
          span.log(output=processed)
  ```

  ```go  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  package main

  import (
  	"context"
  	"go.opentelemetry.io/otel"
  	"go.opentelemetry.io/otel/attribute"
  )

  func complexWorkflow(ctx context.Context, input string) error {
  	tracer := otel.Tracer("my-service")
  	ctx, span := tracer.Start(ctx, "complexWorkflow")
  	defer span.End()

  	span.SetAttributes(attribute.String("type", "task"))
  	span.SetAttributes(attribute.String("input", input))

  	// Step 1
  	data := []string{"item1", "item2"} // Placeholder for fetchData
  	span.SetAttributes(
  		attribute.String("metadata.step", "fetch"),
  		attribute.Int("metadata.record_count", len(data)),
  	)

  	// Step 2
  	processed := "processed data" // Placeholder for processData
  	span.SetAttributes(attribute.String("metadata.step", "process"))

  	// Log final output
  	span.SetAttributes(attribute.String("output", processed))

  	return nil
  }

  func main() {
  	_ = complexWorkflow(context.Background(), "user input")
  }
  ```
</CodeGroup>

## Nest spans

Spans automatically nest when called within other spans, creating a hierarchy that represents your application's execution flow:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { initLogger, wrapTraced } from "braintrust";

  const logger = initLogger({ projectName: "My Project" });

  const fetchData = wrapTraced(async function fetchData(query: string) {
    // Database query logic
    return await db.query(query);
  });

  const transformData = wrapTraced(async function transformData(data: any[]) {
    // Data transformation logic
    return data.map((item) => transform(item));
  });

  // Parent span containing child spans
  const pipeline = wrapTraced(async function pipeline(input: string) {
    const data = await fetchData(input); // Child span 1
    const transformed = await transformData(data); // Child span 2
    return transformed;
  });

  // Creates a trace with nested spans:
  // pipeline
  //   └─ fetchData
  //   └─ transformData
  await pipeline("user query");
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import init_logger, traced

  logger = init_logger(project="My Project")

  @traced
  def fetch_data(query: str):
      # Database query logic
      return db.query(query)

  @traced
  def transform_data(data: list):
      # Data transformation logic
      return [transform(item) for item in data]

  # Parent span containing child spans
  @traced
  def pipeline(input_text: str):
      data = fetch_data(input_text)  # Child span 1
      transformed = transform_data(data)  # Child span 2
      return transformed

  # Creates a trace with nested spans:
  # pipeline
  #   └─ fetch_data
  #   └─ transform_data
  pipeline("user query")
  ```
</CodeGroup>

This nesting makes it easy to see which operations happened as part of a larger workflow.

## Next steps

* [Advanced tracing](/instrument/advanced-tracing) patterns and techniques
* [Capture user feedback](/instrument/user-feedback) like thumbs up/down
* [View your logs](/observe/view-logs) in the Braintrust dashboard
