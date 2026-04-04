# Source: https://uptrace.dev/raw/guides/opentelemetry-node-lambda.md

# OpenTelemetry Node.js AWS Lambda

> Learn how to instrument Node.js AWS Lambda functions with OpenTelemetry to gain visibility into serverless applications, track cold starts, and trace downstream dependencies.

AWS Lambda simplifies serverless application development by abstracting away infrastructure management, but this abstraction makes it harder to understand what happens inside your functions. By instrumenting Node.js Lambda functions with OpenTelemetry, you gain visibility into execution times, cold starts, and downstream service calls.

## How Lambda Execution Works

Lambda runs your code in isolated containers that scale automatically. When there are no incoming requests, Lambda freezes idle containers. This freeze/thaw behavior has important implications for telemetry:

- **Frozen state**: All processes pause, including background flush timers
- **Unpredictable timing**: Containers can remain frozen from seconds to hours
- **Data loss risk**: Buffered telemetry may never be sent if not flushed before freeze

The solution is to flush telemetry data synchronously before each Lambda invocation completes.

## Prerequisites

Before you begin, make sure you have:

- Node.js 18+ runtime (Lambda supports Node.js 18.x, 20.x, and 22.x)
- An [Uptrace DSN](/get#dsn) (cloud or self-hosted)
- AWS CLI or Serverless Framework for deployment

Install the required packages:

```shell
npm install @uptrace/node @opentelemetry/api \
  @opentelemetry/auto-instrumentations-node \
  @opentelemetry/instrumentation-aws-lambda
```

## Instrumentation Setup

Create a separate file called `otel.js` that initializes OpenTelemetry before your application code runs:

```js
const uptrace = require('@uptrace/node')
const otel = require('@opentelemetry/api')
const {
  getNodeAutoInstrumentations,
} = require('@opentelemetry/auto-instrumentations-node')
const {
  AwsLambdaInstrumentation,
} = require('@opentelemetry/instrumentation-aws-lambda')

uptrace.configureOpentelemetry({
  // Set via UPTRACE_DSN env var or uncomment below:
  // dsn: '<FIXME>',
  serviceName: 'myservice',
  serviceVersion: '1.0.0',
  deploymentEnvironment: 'production',
  instrumentations: [
    getNodeAutoInstrumentations(),
    new AwsLambdaInstrumentation({
      disableAwsContextPropagation: true,
    }),
  ],
})
```

If you use ESM (ES modules), create `otel.mjs` instead:

```js
import { configureOpentelemetry } from '@uptrace/node'
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node'
import { AwsLambdaInstrumentation } from '@opentelemetry/instrumentation-aws-lambda'

configureOpentelemetry({
  serviceName: 'myservice',
  serviceVersion: '1.0.0',
  deploymentEnvironment: 'production',
  instrumentations: [
    getNodeAutoInstrumentations(),
    new AwsLambdaInstrumentation({
      disableAwsContextPropagation: true,
    }),
  ],
})
```

## Configuring Lambda to Load OpenTelemetry

Lambda must load the OpenTelemetry initialization code before your application code using the `--require` flag (or `--import` for ESM).

### Serverless Framework

Add the `NODE_OPTIONS` environment variable to your `serverless.yml`:

```yaml
service: lambda-otel-example
frameworkVersion: '3'
provider:
  name: aws
  runtime: nodejs20.x
  environment:
    NODE_OPTIONS: --require otel
    UPTRACE_DSN: ${env:UPTRACE_DSN}
  region: eu-west-2
functions:
  otel-lambda-example:
    handler: handler.hello
```

For ESM, use `--import` instead:

```yaml
environment:
  NODE_OPTIONS: --import ./otel.mjs
```

### AWS CLI

Set the environment variable using the AWS CLI:

```shell
aws lambda update-function-configuration \
  --function-name otel-lambda-example \
  --environment "Variables={NODE_OPTIONS=--require otel,UPTRACE_DSN=<your-dsn>}"
```

### AWS Console

Navigate to your function's **Configuration** > **Environment variables** and add:

<table>
<thead>
  <tr>
    <th>
      Key
    </th>
    
    <th>
      Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        NODE_OPTIONS
      </code>
    </td>
    
    <td>
      <code>
        --require otel
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        UPTRACE_DSN
      </code>
    </td>
    
    <td>
      Your DSN from Uptrace
    </td>
  </tr>
</tbody>
</table>

## Cold Start Monitoring

Cold starts occur when Lambda creates a new container to handle a request. The OpenTelemetry Lambda instrumentation automatically captures cold start information as span attributes:

- `faas.coldstart` â boolean indicating whether this was a cold start
- `faas.invocation_id` â the unique invocation ID
- `cloud.resource_id` â the function ARN

You can filter spans in Uptrace by `faas.coldstart = true` to analyze cold start latency separately from warm invocations. Common strategies to reduce cold starts include:

- **Provisioned concurrency** â keeps containers warm at a fixed cost
- **Smaller bundles** â reduce initialization time by minimizing dependencies
- **Lazy initialization** â defer heavy SDK initialization to first use

## OpenTelemetry Lambda Layer

Alternatively, you can add the [opentelemetry-lambda](https://github.com/open-telemetry/opentelemetry-lambda) layer to your function, which bundles the OpenTelemetry SDK and auto-instrumentation. This approach avoids adding OpenTelemetry packages to your deployment bundle but gives you less control over configuration. See the [Node.js example](https://github.com/open-telemetry/opentelemetry-lambda/tree/main/nodejs) for details.

## What is Uptrace?

Uptrace is an [OpenTelemetry APM](/opentelemetry/apm) that supports distributed tracing, metrics, and logs. You can use it to monitor applications and troubleshoot issues.

![Uptrace Overview](/home/screenshots/apm.png)

Uptrace comes with an intuitive query builder, rich dashboards, alerting rules with notifications, and integrations for most languages and frameworks.

Uptrace can process billions of spans and metrics on a single server and allows you to monitor your applications at 10x lower cost.

In just a few minutes, you can try Uptrace by visiting the [cloud demo](https://play.uptrace.dev/) (no login required) or running it locally with [Docker](/get/hosted/docker). The source code is available on [GitHub](https://github.com/uptrace/uptrace).

## What's next?

Node.js Lambda functions now have full OpenTelemetry tracing for serverless monitoring. Track invocations, cold starts, and downstream dependencies. For traditional Node.js applications, see [Express instrumentation](/guides/opentelemetry-express) or [Next.js instrumentation](/guides/opentelemetry-nextjs), or compare with [Go Lambda](/guides/opentelemetry-go-lambda) for alternative runtime options.
