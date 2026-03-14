# Source: https://tyk.io/docs/api-reference/health/check-system-readiness-status.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Check system readiness status

> Assesses the readiness of the system and its critical components. This endpoint determines if the system is prepared to handle requests by evaluating the status of essential services and dependencies.

## OpenAPI

````yaml swagger/5.8/mdcb-swagger.yml get /readiness
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
  /readiness:
    get:
      tags:
        - Health
      summary: Check system readiness status
      description: >
        Assesses the readiness of the system and its critical components. This
        endpoint determines if the system is prepared to handle requests by
        evaluating the status of essential services and dependencies.
      operationId: readinessGet
      responses:
        '200':
          description: >
            System is ready. All critical components are operational and  the
            system is capable of handling requests.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ReadinessStatus'
        '503':
          description: >
            System is not ready. One or more critical components are 
            non-operational, preventing the system from handling requests
            properly.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ReadinessFailure'
components:
  schemas:
    ReadinessStatus:
      type: object
      properties:
        status:
          type: string
          example: pass
        status_code:
          type: integer
          example: 200
        components:
          type: array
          items:
            $ref: '#/components/schemas/ComponentReadiness'
    ReadinessFailure:
      type: object
      properties:
        status:
          type: string
          example: fail
        status_code:
          type: integer
          example: 503
        components:
          type: array
          items:
            $ref: '#/components/schemas/ComponentReadinessFailure'
    ComponentReadiness:
      type: object
      properties:
        name:
          type: string
          example: postgres
        status:
          type: string
          example: pass
        observation_ts:
          type: string
          format: date-time
          example: '2024-07-29T13:58:56.699052-04:00'
    ComponentReadinessFailure:
      type: object
      properties:
        name:
          type: string
          example: postgres
        status:
          type: string
          example: fail
        observation_ts:
          type: string
          format: date-time
          example: '2024-07-29T13:58:56.699052-04:00'
  securitySchemes:
    api_key:
      in: header
      name: X-Tyk-Authorization
      type: apiKey

````

Built with [Mintlify](https://mintlify.com).
