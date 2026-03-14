# Source: https://tyk.io/docs/planning-for-production/ensure-high-availability/health-check.md

# Source: https://tyk.io/docs/api-reference/health/health-check.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Health Check

> Returns OK if the service is up and running.

## OpenAPI

````yaml swagger/5.8/mdcb-swagger.yml get /health
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
  /health:
    get:
      tags:
        - Health
      summary: Health Check
      description: Returns OK if the service is up and running.
      operationId: healthGet
      responses:
        '200':
          description: Service is up and running.
          content:
            text/plain:
              schema:
                type: string
                example: OK
components:
  securitySchemes:
    api_key:
      in: header
      name: X-Tyk-Authorization
      type: apiKey

````

Built with [Mintlify](https://mintlify.com).
