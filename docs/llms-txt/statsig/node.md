# Source: https://docs.statsig.com/ai-evals/node.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Node AI SDK

> Statsig's Node SDK for AI Application Configuration & Telemetry

<Callout icon="github">
  <a href="https://github.com/statsig-io/statsig-ai-node" target="_blank" rel="noreferrer">Node AI SDK on Github</a>,
  <a href="https://www.npmjs.com/package/@statsig/statsig-ai" target="_blank" rel="noreferrer">NPM Package</a>
</Callout>

<Warning>
  This SDK is available in an open beta, and its methods may change. We encourage you to reach out on [Slack](https://statsig.com/slack) for help getting setup, and so we can communicate changes.
</Warning>

## Overview

The Statsig Node AI SDK lets you manage your prompts, online and offline evals, and debug your LLM applications in production. It depends upon the [Statsig Node Server SDK](/server-core/node-core), but provides convenient hooks for AI-specific functionality.

<Steps>
  <Step title="Install the SDK">
    <CodeGroup>
      ```js npm theme={null}
      npm install @statsig/statsig-ai
      ```

      ```js pnpm theme={null}
      pnpm add @statsig/statsig-ai
      ```

      ```js yarn theme={null}
      yarn add @statsig/statsig-ai
      ```
    </CodeGroup>

    If you have unique setup needs like a frozen lockfile, take a look at the [Node Server SDK docs](/server-core/node-core#installation) - the AI SDK will install Node Server if you don't already have it.
  </Step>

  <Step title="Initialize the SDK">
    If you already have a Statsig instance, you can pass it into the SDK. Otherwise, we'll create an instance for you internally.

    <Tabs>
      <Tab title="Don't use Statsig">
        Initialize the AI SDK with a Server Secret Key from the Statsig console.

        <Warning>
          Server Secret Keys should always be kept private. If you expose one, you can
          disable and recreate it in the Statsig console.
        </Warning>

        ```js  theme={null}
        import { StatsigAI } from '@statsig/statsig-ai';

        const statsigAI = new StatsigAI({'YOUR_SERVER_SECRET_KEY'});
        await statsigAI.initialize();
        ```

        <Accordion title="Initializing With Options">
          Optionally, you can configure [StatsigOptions](/server-core/node-core#statsig-options) for your Statsig instance:

          ```js  theme={null}
          import { StatsigAI, StatsigAIOptions } from '@statsig/statsig-ai';
          import { StatsigOptions } from '@statsig/statsig-server-core-node';

          // if you want to configure any statsig options, this is optional:
          const statsigOptions: StatsigOptions = {
            environment: 'production',
          };

          const statsigAI = new StatsigAI({'YOUR_SERVER_SECRET_KEY', statsigOptions});
          await statsigAI.initialize();

          // if you would like to use any statsig methods, you can access the statsig instance from the statsigAI instance:
          const gate = statsigAI.getStatsig().checkGate(statsigUser, 'my_gate');
          ```
        </Accordion>
      </Tab>

      <Tab title="Already have Statsig instance">
        After installation, initialize the SDK with a [Server Secret Key from the Statsig console](https://console.statsig.com/api_keys).

        <Warning>
          Server Secret Keys should always be kept private. If you expose one, you can
          disable and recreate it in the Statsig console.
        </Warning>

        If you initialize this way, the AI SDK won’t handle initialization, flushing, or shutdown.

        ```js  theme={null}
        import { Statsig } from '@statsig/statsig-server-core-node';
        import { StatsigAI } from '@statsig/statsig-ai';

        const statsig = new Statsig('YOUR_SERVER_SECRET_KEY');
        await statsig.initialize();

        const statsigAI = new StatsigAI({statsig});
        await statsigAI.initialize();
        ```

        <Accordion title="Initializing With Options">
          Optionally, you can configure [StatsigOptions](/server-core/node-core#statsig-options):

          ```js  theme={null}
          import { Statsig } from '@statsig/statsig-server-core-node';
          import { StatsigAI, StatsigAIOptions } from '@statsig/statsig-ai';

          const statsig = new Statsig('YOUR_SERVER_SECRET_KEY', {
            environment: 'production',
          });
          await statsig.initialize();
          await statsigAI.initialize();
          ```
        </Accordion>
      </Tab>
    </Tabs>
  </Step>
</Steps>

## Using the SDK

### Getting a Prompt

Statsig can act as the control plane for your LLM prompts, allowing you to version and change them without deploying code. For more information, see the [Prompts](/ai-evals/prompts) documentation.

```js  theme={null}
import { StatsigUser } from '@statsig/statsig-ai';
// Create a user object
const user = new StatsigUser({ userID: 'a-user' });

// Get the prompt
const myPrompt = statsigAI.getPrompt(user, 'my_prompt');

// Use the live version of the prompt
const liveVersion = myPrompt.getLive();

// Get the candidate versions of the prompt
const candidateVersions = myPrompt.getCandidates();

// Use the live version of the prompt in a completion
const response = await openai.chat.completions.create({
  model: liveVersion.getModel({ fallback: 'gpt-4' }), // optional fallback
  temperature: liveVersion.getTemperature(),
  max_tokens: liveVersion.getMaxTokens(),
  messages: [{ role: 'user', content: 'Your prompt here' }],
});
```

### Logging Eval Results

When running an [online eval](/ai-evals/online-evals), you can log results back to Statsig for analysis.
Provide a score between 0 and 1, along with the grader name and any useful metadata (e.g., session IDs).
Currently, you must provide the grader manually — future releases will support automated grading options.

```js  theme={null}
import { StatsigUser } from '@statsig/statsig-ai';

const livePromptVersion = statsigAI.getPrompt(user, 'my_prompt').getLive();
// Create a user object
const user = new StatsigUser({ userID: 'a-user' });

// Log the results of the eval
statsigAI.logEvalGrade(user, livePromptVersion, 0.5, 'my_grader', {
  session_id: '1234567890',
});

// flush eval grade events to statsig
await statsigAI.flush();
```

### Programmatic Evaluation

Programmatic evaluation allows you to run evaluations on datasets programmatically, automatically scoring outputs and sending results to Statsig for analysis.

With programmatic evaluation, you can:

* **Run evaluations on datasets**: Process arrays, iterators, or async generators of input/expected pairs
* **Define custom tasks**: Create functions that generate outputs from inputs (supports both sync and async)
* **Score outputs**: Use single or multiple named scorer functions to evaluate outputs (supports boolean, numeric, or metadata-rich scores)
* **Use parameters**: Pass dynamic parameters to tasks using Zod schemas (Node) or dictionaries (Python)
* **Categorize data**: Group evaluation records by categories for better analysis
* **Compute summary scores**: Aggregate results across all records with custom summary functions
* **Handle errors gracefully**: Task and scorer errors are caught and reported without stopping the evaluation

The evaluation automatically sends results to Statsig, where you can view them in the console alongside your other eval data.

<Note>
  Tasks and scorers can be async functions. Data can also be provided as async
  functions, promises, or async iterators. The `expected` field in data records
  is optional; scorers can evaluate outputs without expected values. Task and
  scorer errors are automatically caught and reported in the results.
</Note>

```js  theme={null}
import { Eval } from '@statsig/statsig-ai';
import { z } from 'zod';

// Basic evaluation with a single scorer
const result = await Eval('greeting_task', {
  data: [
    { input: 'world', expected: 'Hello world' },
    { input: 'test', expected: 'Hello test' },
  ],
  task: (input: string) => `Hello ${input}`,
  scorer: ({ output, expected }) => output === expected,
  evalRunName: 'run-123',
});

// Multiple named scorers
const result2 = await Eval('multi_scorer_task', {
  data: [
    { input: 'world', expected: 'Hello world' },
    { input: 'test', expected: 'Hello test' },
  ],
  task: (input: string) => `Hello ${input}`,
  scorer: {
    correctness: ({ output, expected }) => output === expected,
    startsWithHello: ({ output }) => output.startsWith('Hello'),
    lengthCheck: ({ output }) => output.length > 5,
  },
});

// Using parameters with Zod schemas
const result3 = await Eval('parameterized_task', {
  data: [
    { input: 'world', expected: 'Hi world' },
  ],
  task: (input: string, hooks) => {
    const prefix = hooks.parameters.name || 'Hello';
    return `${prefix} ${input}`;
  },
  scorer: ({ output, expected }) => output === expected,
  parameters: {
    name: z.string().default('Hi'),
  },
});

// Extras: Categories and summary scores
const result4 = await Eval('categorized_with_summary', {
  data: [
    { input: 'world', expected: 'Hello world', category: 'greeting' },
    { input: 'test', expected: 'Hello test', category: ['greeting', 'test'] },
    { input: 'foo', expected: 'Goodbye foo', category: 'farewell' },
  ],
  task: (input: string) => `Hello ${input}`,
  scorer: {
    correctness: ({ output, expected }) => output === expected,
  },
  summaryScoresFn: (results) => {
    const correct = results.filter(r => r.scores.correctness === 1).length;
    return {
      accuracy: correct / results.length,
      total: results.length,
    };
  },
});
```

### OpenTelemetry (OTEL)

The AI SDK works with OpenTelemetry for sending telemetry to Statsig.
You can enable OTel tracing by calling the `initializeTracing` function.
You can also provide a custom `TracerProvider` to the `initializeTracing` function if you want to customize the tracing behavior.
More advanced OTel configuration and exporter support are on the way.

The simplest way to start tracing with Statsig and OTel is to call `initializeTracing()` at the root of your application.

```js  theme={null}
// instrumentation.{js,ts}
import { initializeTracing } from '@statsig/statsig-ai/otel';

initializeTracing({
  // optional: enables the global trace provider registration
  // so that you can create spans without having to create a new trace provider
  enableGlobalTraceProviderRegistration: true,
});
```

If you already have your own OTel setup with `NodeSDK`, you only need to initialize Statsig's OTel tracing and use the processor created by `initializeTracing()`.

```js  theme={null}
// instrumentation.{js,ts}

import { NodeSDK } from '@opentelemetry/sdk-node';

import {
  PeriodicExportingMetricReader,
  ConsoleMetricExporter,
} from '@opentelemetry/sdk-metrics';

import { initializeTracing } from '@statsig/statsig-ai/otel';

// when you have your own otel setup and don't want to use the global trace provider
// you can disable it with the options below
const { processor } = initializeTracing({
  // prevents creating a global context manager
  skipGlobalContextManagerSetup: true,
  exporterOptions: {
    sdkKey: process.env.STATSIG_SDK_KEY!,
  },
});


const sdk = new NodeSDK({
  // IMPORTANT: use the processor created by initializeTracing
  // to make sure that spans are exported to Statsig
  spanProcessors: [processor],
  metricReader: new PeriodicExportingMetricReader({
    exporter: new ConsoleMetricExporter(),
  }),
  // ... other node sdk options like autoInstrumentations
});


sdk.start();
export { sdk };
```

The `initializeOTel` function accepts the below options for setting up tracing with OTel.

```ts  theme={null}
type InitializeOptions = {
  /** An optional global context manager to use. If not provided, one will be created and set as the global context manager unless `skipGlobalContextManagerSetup` is true. */
  globalContextManager?: ContextManager;
  /** If true, will not attempt to set up a global context manager automatically. */
  skipGlobalContextManagerSetup?: boolean;

  /** If true, will register the trace provider globally. */
  enableGlobalTraceProviderRegistration?: boolean;
  /** An optional global trace provider to use. If not provided, a new BasicTracerProvider will be created and optionally registered globally */
  globalTraceProvider?: TracerProvider;

  /** Options to pass to the StatsigOTLPTraceExporter */
  exporterOptions?: StatsigOTLPTraceExporterOptions;

  // resource options
  serviceName?: string;
  version?: string;
  environment?: string;
};
```

For more examples see the [Statsig AI Node SDK](https://github.com/statsig-io/statsig-ai-node/tree/main/examples/otel).

### Wrapping OpenAI

The Statsig OpenAI Wrapper automatically adds tracing and log events to your OpenAI SDK usage, giving you in-console visibility with minimal setup.

```js  theme={null}
import { wrapOpenAI, StatsigAI } from '@statsig/statsig-ai';
import { OpenAI } from 'openai';

// if you have your own otel, you do not need an statsigAI instance here.
// But if you want to use the default Otel on statsigAI, you need to initialize the SDK.
statsigAI = new StatsigAI({"YOUR_SERVER_SECRET_KEY"});
await statsigAI.initialize();

const client = wrapOpenAI(
  new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
  })
);

const response = await client.chat.completions.create({
  model: "gpt-4",
  messages: [{ role: "user", content: "Hello, world!" }],
});
```

<AiOptionsPreamble />

<AiOptions />

## Using other SDK methods

Whether you passed in a Statsig instance or not, you can access the Statsig instance from the statsigAI instance, and use its many methods:

```javascript  theme={null}
// Check a gate value
const gate = statsigAI.getStatsig().checkGate(statsigUser, 'my_gate');

// Log an event
statsigAI.getStatsig().logEvent(statsigUser, 'my_event', { value: 1 });
```

Refer to the [Statsig Node SDK](/server-core/node-core) docs for more information on how to use the Core Statsig SDK methods, plus information on advanced setup + singleton usage.


Built with [Mintlify](https://mintlify.com).