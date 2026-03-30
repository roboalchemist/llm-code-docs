# Source: https://tyk.io/docs/api-reference/debug/cpu-profiling-data.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# CPU Profiling data

> Returns CPU profiling data. Available only when HTTPProfile is enabled in sink.conf.

## OpenAPI

````yaml swagger/5.8/mdcb-swagger.yml get /debug/pprof/profile
openapi: 3.0.0
info:
  contact:
    email: support@tyk.io
    name: Tyk Technologies
    url: https://tyk.io/contact
  version: 1.0.0
  title: MDCB Data Planes and Diagnostics API
  description: >
    This API provides operations for monitoring Data Planes connected to MDCB
    and accessing diagnostic data.  It includes endpoints for retrieving
    connected data plane details, performing health checks,  and accessing Go's
    built-in pprof diagnostics for advanced performance profiling.
servers:
  - url: https://{tenant}
    variables:
      tenant:
        default: localhost:8181
        description: Your MDCB host
security:
  - api_key: []
tags:
  - name: Data Planes
    description: Operations related to data plane management and information
  - name: Health
    description: Endpoints for checking system health and status
  - name: Debug
    description: Diagnostic and profiling endpoints
  - name: Configuration
    description: Configuration and environment variable management
paths:
  /debug/pprof/profile:
    get:
      tags:
        - Debug
      summary: CPU Profiling data
      description: >-
        Returns CPU profiling data. Available only when HTTPProfile is enabled
        in sink.conf.
      operationId: debugPprofProfileGet
      responses:
        '200':
          description: CPU profiling data.
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary
components:
  securitySchemes:
    api_key:
      in: header
      name: X-Tyk-Authorization
      type: apiKey

````

Built with [Mintlify](https://mintlify.com).
