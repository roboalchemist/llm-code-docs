# Source: https://docs.aws.amazon.com/powertools/python/latest/build_recipes/troubleshooting/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cicd-integration/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/build_recipes/performance-optimization/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/build_recipes/build-tools/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/build_recipes/getting-started/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/build_recipes/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/tutorial/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/utilities/jmespath_functions/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/utilities/middleware_factory/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/utilities/feature_flags/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/utilities/idempotency/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/utilities/data_classes/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/utilities/validation/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/utilities/typing/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/utilities/batch/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/utilities/parameters/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/appsync_events/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/appsync/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/api_gateway/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/core/metrics/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/core/logger/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/core/tracer/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/roadmap/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/upgrade/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/changelog/index.md

# Source: https://docs.aws.amazon.com/powertools/python/latest/index.md

Powertools for AWS Lambda (Python) is a developer toolkit to implement Serverless best practices and increase developer velocity.

Ready to use Powertools for AWS Lambda? Jump to [Installation](https://docs.aws.amazon.com/powertools/python/latest/getting-started/install/index.md).

- **Features**

  ______________________________________________________________________

  Adopt one, a few, or all industry practices. **Progressively**.

  [All features](#features)

- **Installation**

  ______________________________________________________________________

  Install via pip, Lambda Layers, or SAR.

  [Get started](https://docs.aws.amazon.com/powertools/python/latest/getting-started/install/index.md)

- **Support this project**

  ______________________________________________________________________

  Become a public reference, share your work, join the community.

  [Support](#support-powertools-for-aws-lambda-python)

- **Other languages**

  ______________________________________________________________________

  Powertools is also available in other languages.

  [Java](https://docs.aws.amazon.com/powertools/java/), [TypeScript](https://docs.aws.amazon.com/powertools/typescript/latest/), [.NET](https://docs.aws.amazon.com/powertools/dotnet/)

## Features

| Utility                                                                                                           | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| [Tracer](https://docs.aws.amazon.com/powertools/python/latest/core/tracer/index.md)                               | Decorators and utilities to trace Lambda function handlers, and both synchronous and asynchronous functions |
| [Logger](https://docs.aws.amazon.com/powertools/python/latest/core/logger/index.md)                               | Structured logging made easier, and target to enrich structured logging with key Lambda context details     |
| [Metrics](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/index.md)                             | Custom Metrics created asynchronously via CloudWatch Embedded Metric Format (EMF)                           |
| [Event Handler](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/api_gateway/index.md)     | Event handler for API Gateway, ALB, Lambda Function URL, VPC Lattice, AppSync, and Bedrock Agents           |
| [Parameters](https://docs.aws.amazon.com/powertools/python/latest/utilities/parameters/index.md)                  | Retrieve and cache parameter values from Parameter Store, Secrets Manager, AppConfig, or DynamoDB           |
| [Parser](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/index.md)                          | Data parsing and deep validation using Pydantic                                                             |
| [Batch Processing](https://docs.aws.amazon.com/powertools/python/latest/utilities/batch/index.md)                 | Handle partial failures for SQS, Kinesis Data Streams, and DynamoDB Streams                                 |
| [Idempotency](https://docs.aws.amazon.com/powertools/python/latest/utilities/idempotency/index.md)                | Make your Lambda functions idempotent and prevent duplicate execution                                       |
| [Feature Flags](https://docs.aws.amazon.com/powertools/python/latest/utilities/feature_flags/index.md)            | A simple rule engine to evaluate when features should be enabled                                            |
| [Validation](https://docs.aws.amazon.com/powertools/python/latest/utilities/validation/index.md)                  | JSON Schema validator for inbound events and responses                                                      |
| [Data Masking](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/index.md)              | Protect confidential data with easy removal or encryption                                                   |
| [Streaming](https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming/index.md)                    | Stream datasets larger than available memory                                                                |
| [Middleware Factory](https://docs.aws.amazon.com/powertools/python/latest/utilities/middleware_factory/index.md)  | Create your own middleware to run logic before and after each Lambda invocation                             |
| [Typing](https://docs.aws.amazon.com/powertools/python/latest/utilities/typing/index.md)                          | Static typing classes to speedup development in your IDE                                                    |
| [Event Source Data Classes](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_classes/index.md) | Data classes describing the schema of common Lambda event triggers                                          |
| [JMESPath Functions](https://docs.aws.amazon.com/powertools/python/latest/utilities/jmespath_functions/index.md)  | Built-in JMESPath functions to deserialize common encoded JSON payloads                                     |
| [Kafka](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/index.md)                            | Deserialize and validate Kafka events with support for Avro, Protocol Buffers, and JSON Schema              |

## Examples

You can find examples in the [examples directory](https://github.com/aws-powertools/powertools-lambda-python/tree/develop/examples) and a quick start using SAM CLI:

```
sam init --app-template hello-world-powertools-python --name sam-app --package-type Zip --runtime python3.13 --no-tracing

```

For a more complete example, check the [Powertools for AWS workshop](https://catalog.workshops.aws/serverless-powertools).

## Environment variables

Info

Explicit parameters take precedence over environment variables.

| Environment variable                 | Description                                    | Utility                                                                                          | Default             |
| ------------------------------------ | ---------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------- |
| `POWERTOOLS_SERVICE_NAME`            | Service name for tracing, metrics, and logging | All                                                                                              | `service_undefined` |
| `POWERTOOLS_LOG_LEVEL`               | Sets logging level                             | [Logger](https://docs.aws.amazon.com/powertools/python/latest/core/logger/index.md)              | `INFO`              |
| `POWERTOOLS_LOGGER_LOG_EVENT`        | Logs incoming event                            | [Logger](https://docs.aws.amazon.com/powertools/python/latest/core/logger/index.md)              | `false`             |
| `POWERTOOLS_LOGGER_SAMPLE_RATE`      | Debug log sampling                             | [Logger](https://docs.aws.amazon.com/powertools/python/latest/core/logger/index.md)              | `0`                 |
| `POWERTOOLS_METRICS_NAMESPACE`       | Namespace for metrics                          | [Metrics](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/index.md)            | `None`              |
| `POWERTOOLS_METRICS_DISABLED`        | Disables metrics emission                      | [Metrics](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/index.md)            | `false`             |
| `POWERTOOLS_TRACE_DISABLED`          | Disables tracing                               | [Tracer](https://docs.aws.amazon.com/powertools/python/latest/core/tracer/index.md)              | `false`             |
| `POWERTOOLS_TRACER_CAPTURE_RESPONSE` | Captures return as metadata                    | [Tracer](https://docs.aws.amazon.com/powertools/python/latest/core/tracer/index.md)              | `true`              |
| `POWERTOOLS_TRACER_CAPTURE_ERROR`    | Captures exception as metadata                 | [Tracer](https://docs.aws.amazon.com/powertools/python/latest/core/tracer/index.md)              | `true`              |
| `POWERTOOLS_PARAMETERS_MAX_AGE`      | Cache TTL in seconds                           | [Parameters](https://docs.aws.amazon.com/powertools/python/latest/utilities/parameters/index.md) | `5`                 |
| `POWERTOOLS_PARAMETERS_SSM_DECRYPT`  | Decrypt SSM parameters                         | [Parameters](https://docs.aws.amazon.com/powertools/python/latest/utilities/parameters/index.md) | `false`             |
| `POWERTOOLS_DEV`                     | Increases verbosity for development            | Multiple                                                                                         | `false`             |
| `POWERTOOLS_DEBUG`                   | Enables debug logging for Powertools           | All                                                                                              | `false`             |

### Development mode

When `POWERTOOLS_DEV` is set to `true`, it enables development-friendly settings:

| Utility       | Effect                                             |
| ------------- | -------------------------------------------------- |
| Logger        | Increases JSON indentation to 4 for readability    |
| Event Handler | Enables full traceback errors and CORS in dev mode |
| Tracer        | Disables tracing in non-Lambda environments        |
| Metrics       | Disables metrics emission (can be overridden)      |

## Support Powertools for AWS Lambda (Python)

- **Become a public reference**

  ______________________________________________________________________

  Add your company name and logo on our [landing page](https://powertools.aws.dev).

  [GitHub Issue template](https://github.com/aws-powertools/powertools-lambda-python/issues/new?assignees=&labels=customer-reference&template=support_powertools.yml&title=%5BSupport+Lambda+Powertools%5D%3A+%3Cyour+organization+name%3E)

- **Share your work**

  ______________________________________________________________________

  Blog posts, videos, and sample projects about Powertools.

  [GitHub Issue template](https://github.com/aws-powertools/powertools-lambda-python/issues/new?assignees=&labels=community-content&template=share_your_work.yml&title=%5BI+Made+This%5D%3A+%3CTITLE%3E)

- **Join the community**

  ______________________________________________________________________

  Connect, ask questions, and share what features you use.

  [Discord invite](https://discord.gg/B8zZKbbyET)

## Tenets

These are our core principles to guide our decision making.

- **AWS Lambda only**. We optimize for AWS Lambda function environments and supported runtimes only. Utilities might work with web frameworks and non-Lambda environments, though they are not officially supported.
- **Eases the adoption of best practices**. The main priority of the utilities is to facilitate best practices adoption, as defined in the AWS Well-Architected Serverless Lens; all other functionality is optional.
- **Keep it lean**. Additional dependencies are carefully considered for security and ease of maintenance, and prevent negatively impacting startup time.
- **We strive for backwards compatibility**. New features and changes should keep backwards compatibility. If a breaking change cannot be avoided, the deprecation and migration process should be clearly defined.
- **We work backwards from the community**. We aim to strike a balance of what would work best for 80% of customers. Emerging practices are considered and discussed via Requests for Comment (RFCs).
- **Progressive**. Utilities are designed to be incrementally adoptable for customers at any stage of their Serverless journey. They follow language idioms and their community's common practices.
