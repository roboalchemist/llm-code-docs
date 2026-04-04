# Source: https://docs.wandb.ai/weave/reference/service-api/opentelemetry/export-trace.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Export Trace



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /otel/v1/traces
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /otel/v1/traces:
    post:
      tags:
        - OpenTelemetry
      summary: Export Trace
      operationId: export_trace_otel_v1_traces_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}

````