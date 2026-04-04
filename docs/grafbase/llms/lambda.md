# Source: https://grafbase.com/docs/gateway/deployment/lambda.md

# Deploy to Lambda

Deploy the Grafbase Gateway to the AWS Lambda platform as a serverless function. We provide a separate build targeting the Lambda platform for each gateway release. This has differences from running the gateway binary in a normal server environment. Select the correct builds for Lambda - normal builds won't work in AWS Lambda.

## Lambda Size Selection

The Grafbase Lambda Gateway uses minimal memory: common usage stays below hundred megabytes. The Lambda memory setting affects how much CPU AWS allocates for the function, so choosing a higher base memory amount can improve cold start times and general performance, even when the Gateway doesn't need the memory.

## Lambda Binary Selection

The [gateway release](https://github.com/grafbase/grafbase/releases) includes two Lambda-targeted binaries:

- `grafbase-gateway-lambda-aarch64-unknown-linux-musl` for Amazon Graviton platform, targeting 64-bit ARM architecture.
- `grafbase-gateway-lambda-x86_64-unknown-linux-musl` for 64-bit x86 platform.

The binaries won't work if you deploy them to the wrong CPU architecture. The aarch64 version is smaller, so using Graviton (when available in your region) can speed up cold starts due to the smaller size.

Lambda binaries work only in AWS Lambda or a Lambda-emulating docker image. These binaries optimize for size over runtime speed to minimize cold start time.

## Set up Lambda for the Grafbase Lambda Gateway

Configure the Lambda function as needed. Control Gateway execution settings through these environment variables:

- `GRAFBASE_CONFIG_PATH` sets the Grafbase configuration file path. Default: `./grafbase.toml`, looking for configuration in the Lambda root directory.
- `GRAFBASE_SCHEMA_PATH` sets the federated schema path. Default: `./federated.graphql`, looking in the Lambda root directory.
- `GRAFBASE_LOG` sets log level. Values: `error`, `warn`, `info`, `debug`, `trace` or `off`. Default: `info`.
- `GRAFBASE_LOG_STYLE` sets log message style. Values: `text` or `json`. Default: `text`.

## Deployment

Package the Grafbase Lambda Gateway with the gateway configuration and federated graph. Unlike a full server, Lambda functions freeze without traffic, preventing background graph updates. After publishing a new subgraph:

1. [Download](https://github.com/grafbase/grafbase/releases) your preferred Grafbase Lambda Gateway version
2. Rename the binary to `bootstrap`
3. Copy the configuration file to the same directory
4. Get the latest federated graph from the Grafbase API

Include these files in your deployment:

```bash
.
├── bootstrap
├── grafbase.toml
└── federated.graphql
```

Deploy following the [AWS documentation](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html).

## Configuration differences

Configure the Grafbase Lambda Gateway with the same configuration file as the binary, with these changes:

- AWS defines listen address and port - network settings don't apply
- AWS handles transport layer security - TLS settings in Grafbase configuration don't apply
- OpenTelemetry settings work similarly, but batching doesn't affect Lambda
- Set CORS from Gateway configuration or Lambda settings

## OpenTelemetry

We recommend using [AWS X-Ray](https://aws.amazon.com/xray/) for OpenTelemetry tracing in Lambda. The Grafbase Lambda Gateway propagates span IDs in X-Ray format and connects Lambda traces to Gateway traces.

Because functions sleep without traffic, you must flush traces before request responses. This increases response times. Run an OLPC collector in the same datacenter as your Lambda function. Install the [AWS distro for OpenTelemetry Collector](https://aws-otel.github.io/docs/setup/ec2) in Amazon Elastic Computer Cloud. Place the EC2 instance in the same region and virtual private network for best performance.

Configure the Grafbase Lambda Gateway to send traces to your functional OpenTelemetry collector:

```toml
[telemetry]
service_name = "my-federated-graph"

[telemetry.tracing]
enabled = true
sampling = 1

[telemetry.tracing.propagation]
aws_xray = true

[telemetry.tracing.exporters.otlp]
enabled = true
endpoint = "http://<IP>:4317"
protocol = "grpc"
timeout = 5
```