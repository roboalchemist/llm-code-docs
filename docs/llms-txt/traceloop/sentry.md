# Source: https://www.traceloop.com/docs/openllmetry/integrations/sentry.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM Observability with Sentry and OpenLLMetry

Install Sentry SDK with OpenTelemetry support:

<CodeGroup>
  ```bash Python theme={null}
  pip install --upgrade 'sentry-sdk[opentelemetry]'
  ```

  ```bash Typescript (Node.js) theme={null}
  npm install @sentry/node @sentry/opentelemetry-node
  ```
</CodeGroup>

Initialize Sentry and enable OpenTelemetry instrumentation:

<CodeGroup>
  ```python Python theme={null}
  import sentry_sdk

  sentry_sdk.init(
  dsn=<Your DSN>,
  enable_tracing=True,

      # set the instrumenter to use OpenTelemetry instead of Sentry
      instrumenter="otel",

  )

  ```

  ```javascript Typescript (Node.js) theme={null}
  Sentry.init({
    dsn: <Your DSN>,
    tracesSampleRate: 1.0,
    skipOpenTelemetrySetup: true,
  });
  ```
</CodeGroup>

Then, when initializing the Traceloop SDK, make sure to override the processor and propagator:

<CodeGroup>
  ```python Python theme={null}
  from traceloop.sdk import Traceloop
  from sentry_sdk.integrations.opentelemetry import SentrySpanProcessor, SentryPropagator

  Traceloop.init(processor=SentrySpanProcessor(), propagator=SentryPropagator())

  ```

  ```javascript Typescript (Node.js) theme={null}
  import * as traceloop from "@traceloop/node-server-sdk";
  import { SentrySpanProcessor, SentryPropagator, SentrySampler } from "@sentry/opentelemetry";

  traceloop.initialize({
    contextManager: new Sentry.SentryContextManager(),
    processor: new SentrySpanProcessor(),
    propagator: new SentryPropagator()
  })
  ```
</CodeGroup>
