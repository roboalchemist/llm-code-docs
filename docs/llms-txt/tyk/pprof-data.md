# Source: https://tyk.io/docs/api-reference/debug/pprof-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# pprof data

> Serves various pprof data like heap, goroutine, threadcreate, block, and so on. The `{profileType}` path parameter can accept various profiling types as well as more complex patterns. Available only when HTTPProfile is enabled in sink.conf.




## OpenAPI

````yaml swagger/5.8/mdcb-swagger.yml get /debug/pprof/{profileType}
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
  /debug/pprof/{profileType}:
    get:
      tags:
        - Debug
      summary: pprof data
      description: >
        Serves various pprof data like heap, goroutine, threadcreate, block, and
        so on. The `{profileType}` path parameter can accept various profiling
        types as well as more complex patterns. Available only when HTTPProfile
        is enabled in sink.conf.
      operationId: debugPprofProfileTypeGet
      parameters:
        - in: path
          name: profileType
          required: true
          description: >-
            The specific pprof data to retrieve (heap, goroutine, threadcreate,
            block, etc.), or a pattern matching multiple types.
          schema:
            type: string
            example: heap
      responses:
        '200':
          description: pprof data.
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