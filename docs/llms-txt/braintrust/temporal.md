# Source: https://braintrust.dev/docs/integrations/sdk-integrations/temporal.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Temporal

> Trace Temporal workflows and activities with Braintrust

[Temporal](https://temporal.io/) is a durable execution platform for building reliable distributed applications. Braintrust integrates with Temporal to automatically trace workflows and activities, providing full observability across your workflow executions.

The integration captures:

* Workflow execution spans
* Activity execution spans with metadata
* Distributed traces across workers
* Parent-child relationships between workflows and activities

## Setup

Install the required packages:

<CodeGroup>
  ```bash TypeScript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  # pnpm
  pnpm add @braintrust/temporal braintrust @temporalio/client @temporalio/worker @temporalio/workflow @temporalio/activity @temporalio/common
  # npm
  npm install @braintrust/temporal braintrust @temporalio/client @temporalio/worker @temporalio/workflow @temporalio/activity @temporalio/common
  ```

  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pip install "braintrust[temporal]"
  ```

  ```bash Go theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  go get github.com/braintrustdata/braintrust-sdk-go
  go get go.temporal.io/sdk
  go get go.temporal.io/contrib/opentelemetry
  ```
</CodeGroup>

<Note>
  Temporal integration requires TypeScript SDK v2.1.0+.
</Note>

## Trace with Temporal

Braintrust provides automatic tracing for Temporal workflows and activities. The integration uses a plugin pattern for TypeScript and Python, and OpenTelemetry interceptors for Go.

### TypeScript

Use the `BraintrustTemporalPlugin` with both your Temporal Client and Worker. The plugin automatically instruments your workflows and activities, creating spans that capture execution details and propagate trace context across process boundaries.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { Client, Connection } from "@temporalio/client";
import { Worker } from "@temporalio/worker";
import * as braintrust from "braintrust";
import { BraintrustTemporalPlugin } from "@braintrust/temporal";

// Initialize Braintrust
braintrust.initLogger({ projectName: "my-project" });

// Create a single plugin instance
const plugin = new BraintrustTemporalPlugin();

// Use the plugin with your Client
const client = new Client({
  connection: await Connection.connect(),
  plugins: [plugin],
});

// Use the same plugin with your Worker
const worker = await Worker.create({
  taskQueue: "my-task-queue",
  workflowsPath: require.resolve("./workflows"),
  activities,
  plugins: [plugin],
});
```

The plugin automatically:

* Creates parent spans for workflow executions
* Creates child spans for activity executions
* Propagates trace context across workers via headers
* Handles concurrent workflow execution safely

### Python

Use `BraintrustPlugin` from `braintrust.contrib.temporal` with both your Temporal Client and Worker. The plugin intercepts workflow and activity executions to create spans with full context, including workflow IDs, activity types, and execution metadata.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from braintrust.contrib.temporal import BraintrustPlugin
from temporalio.client import Client
from temporalio.worker import Worker

# Create a single plugin instance
plugin = BraintrustPlugin()

# Use the plugin with your Client
client = await Client.connect(
    "localhost:7233",
    plugins=[plugin],
)

# Use the same plugin with your Worker
worker = Worker(
    client,
    task_queue="my-task-queue",
    workflows=[MyWorkflow],
    activities=[my_activity],
    plugins=[plugin],
)

await worker.run()
```

The plugin handles:

* Workflow execution spans via `BraintrustWorkflowInboundInterceptor`
* Activity execution spans with workflow metadata
* Span context serialization/deserialization via Temporal headers
* Temporal sandbox compatibility for braintrust imports

### Go

Go uses OpenTelemetry interceptors to integrate Braintrust with Temporal. This approach leverages Temporal's native OpenTelemetry support, routing spans through the Braintrust SDK's trace provider for unified observability.

```go  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
package main

import (
	"context"
	"log"

	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/propagation"
	"go.opentelemetry.io/otel/sdk/trace"
	"go.temporal.io/sdk/activity"
	"go.temporal.io/sdk/client"
	"go.temporal.io/sdk/contrib/opentelemetry"
	"go.temporal.io/sdk/interceptor"
	"go.temporal.io/sdk/worker"
	"go.temporal.io/sdk/workflow"

	"github.com/braintrustdata/braintrust-sdk-go"
)

// MyWorkflow is a minimal workflow that executes an activity
func MyWorkflow(ctx workflow.Context, input string) (string, error) {
	var result string
	err := workflow.ExecuteActivity(ctx, MyActivity, input).Get(ctx, &result)
	return result, err
}

// MyActivity is a minimal activity
func MyActivity(ctx context.Context, input string) (string, error) {
	logger := activity.GetLogger(ctx)
	logger.Info("Processing input", "input", input)
	return "processed: " + input, nil
}

func main() {
	ctx := context.Background()

	// Set up OpenTelemetry TracerProvider
	tp := trace.NewTracerProvider()
	defer tp.Shutdown(ctx)
	otel.SetTracerProvider(tp)

	// Configure propagators for distributed tracing
	otel.SetTextMapPropagator(propagation.NewCompositeTextMapPropagator(
		propagation.TraceContext{},
		propagation.Baggage{},
	))

	// Initialize Braintrust
	_, err := braintrust.New(tp,
		braintrust.WithProject("My Project"),
	)
	if err != nil {
		log.Fatal(err)
	}

	// Create OpenTelemetry interceptor for Temporal
	tracer := otel.Tracer("temporal-example")
	tracingInterceptor, err := opentelemetry.NewTracingInterceptor(
		opentelemetry.TracerOptions{Tracer: tracer},
	)
	if err != nil {
		log.Fatal(err)
	}

	// Create Temporal client with tracing
	c, err := client.Dial(client.Options{
		Interceptors: []interceptor.ClientInterceptor{tracingInterceptor},
	})
	if err != nil {
		log.Fatal(err)
	}
	defer c.Close()

	// Create worker with the same client
	w := worker.New(c, "my-task-queue", worker.Options{})
	w.RegisterWorkflow(MyWorkflow)
	w.RegisterActivity(MyActivity)

	if err := w.Run(worker.InterruptCh()); err != nil {
		log.Fatal(err)
	}
}
```

## Resources

* [Temporal documentation](https://docs.temporal.io/)
* [Temporal Python SDK](https://github.com/temporalio/sdk-python)
* [Temporal TypeScript SDK](https://github.com/temporalio/sdk-typescript)
* [Temporal Go SDK](https://github.com/temporalio/sdk-go)
* [OpenTelemetry integration guide](/integrations/sdk-integrations/opentelemetry)
