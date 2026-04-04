# Source: https://braintrust.dev/docs/reference/sdks/typescript/migrations/v0-to-v1.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrate from v0.x to v1.x

> Guide for migrating from TypeScript SDK v0.x to v1.x

<Warning>
  **Breaking change**: OpenTelemetry functionality has been moved to the separate `@braintrust/otel` [npm package](https://www.npmjs.com/package/@braintrust/otel). This solves ESM build issues in Next.js (edge), Cloudflare Workers, Bun, and TanStack applications, and adds support for both OpenTelemetry v1 and v2.
</Warning>

If you're not using OpenTelemetry, just upgrade the SDK. If you are using OpenTelemetry features, follow the full migration steps:

<Steps>
  <Step title="Upgrade the SDK">
    <CodeGroup>
      ```bash npm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      npm install braintrust@latest
      ```

      ```bash pnpm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      pnpm add braintrust@latest
      ```
    </CodeGroup>
  </Step>

  <Step title="Install the OpenTelemetry package">
    Add `@braintrust/otel` to your project:

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      npm install @braintrust/otel
      ```

      ```bash pnpm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      pnpm add @braintrust/otel
      ```
    </CodeGroup>
  </Step>

  <Step title="Update imports">
    Replace imports from `braintrust` with imports from `@braintrust/otel` for OpenTelemetry-related functionality.

    * **BraintrustSpanProcessor**

      Before:

      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { BraintrustSpanProcessor } from "braintrust";
      ```

      After:

      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { BraintrustSpanProcessor } from "@braintrust/otel";
      ```

    * **BraintrustExporter**

      Before:

      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { BraintrustExporter } from "braintrust";
      ```

      After:

      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { BraintrustExporter } from "@braintrust/otel";
      ```

    * **Distributed tracing utilities**

      Before:

      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { initLogger, otel } from "braintrust";

      const ctx = otel.contextFromSpanExport(exported);
      const parent = otel.parentFromHeaders(headers);
      const updatedCtx = otel.addSpanParentToBaggage(span);
      ```

      After:

      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { initLogger } from "braintrust";
      import { contextFromSpanExport, parentFromHeaders, addSpanParentToBaggage } from "@braintrust/otel";

      const ctx = contextFromSpanExport(exported);
      const parent = parentFromHeaders(headers);
      const updatedCtx = addSpanParentToBaggage(span);
      ```
  </Step>

  <Step title="Update OTel compatibility">
    If you were previously using the `BRAINTRUST_OTEL_COMPAT=true` environment variable to enable bidirectional interoperability between Braintrust and OpenTelemetry spans, you should now use `setupOtelCompat()` instead.

    Before:

    ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    // Set environment variable before any imports
    process.env.BRAINTRUST_OTEL_COMPAT = "true";

    import { initLogger } from "braintrust";
    import { trace } from "@opentelemetry/api";

    // Create loggers and spans
    const logger = initLogger({ projectName: "my-project" });
    const tracer = trace.getTracer("my-service");

    // Braintrust and OTEL spans work together
    await logger.traced(async (braintrustSpan) => {
      await tracer.startActiveSpan("otel-operation", async (otelSpan) => {
        // Work happens here
        otelSpan.end();
      });
    });
    ```

    After:

    <Note>
      **Important:** Call `setupOtelCompat()` before creating any Braintrust loggers or OpenTelemetry spans.
    </Note>

    ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    import { setupOtelCompat } from "@braintrust/otel";
    import { initLogger } from "braintrust";
    import { trace } from "@opentelemetry/api";

    // Call this first, before any logger or span creation
    setupOtelCompat();

    // Create loggers and spans - they will work together
    const logger = initLogger({ projectName: "my-project" });
    const tracer = trace.getTracer("my-service");

    // Braintrust and OTEL spans work together
    await logger.traced(async (braintrustSpan) => {
      await tracer.startActiveSpan("otel-operation", async (otelSpan) => {
        // Work happens here
        otelSpan.end();
      });
    });
    ```

    If you're writing tests and need to reset the compatibility mode between test cases, use `resetOtelCompat()`:

    ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    import { setupOtelCompat, resetOtelCompat } from "@braintrust/otel";

    describe("my tests", () => {
      beforeEach(() => {
        setupOtelCompat();
      });

      afterEach(() => {
        resetOtelCompat();
      });

      // Your tests here
    });
    ```
  </Step>

  <Step title="Verify your setup">
    After updating imports and, if necessary, OTel compatibility, verify your integration works correctly:

    1. Run your build process to ensure no import errors.
    2. Test that traces appear in Braintrust as expected.
    3. If using distributed tracing, verify parent-child relationships are maintained.

    <Note>
      If you encounter issues during migration, please [open an issue](https://github.com/braintrustdata/braintrust-sdk/issues) with details about your setup and the problem you're experiencing.
    </Note>
  </Step>
</Steps>
