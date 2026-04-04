# Source: https://tyk.io/docs/api-reference/configuration/retrieve-environment-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve environment variables

> Returns environment variables of the system. You can optionally filter for a specific configuration field.

**Example curl commands:**

Get all environment variables:
```bash
curl -X GET \ 
http://localhost:8181/env \
-H 'X-Tyk-Authorization: your-secret-key'
```

Get specific environment variable:
```bash
curl -X GET \
'http://localhost:8181/env?env=TYK_MDCB_SYNCWORKERCONFIG_WARMUPTIME' \
-H 'X-Tyk-Authorization: your-secret-key'
```




## OpenAPI

````yaml swagger/5.8/mdcb-swagger.yml get /env
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
  /env:
    get:
      tags:
        - Configuration
      summary: Retrieve environment variables
      description: >
        Returns environment variables of the system. You can optionally filter
        for a specific configuration field.


        **Example curl commands:**


        Get all environment variables:

        ```bash

        curl -X GET \ 

        http://localhost:8181/env \

        -H 'X-Tyk-Authorization: your-secret-key'

        ```


        Get specific environment variable:

        ```bash

        curl -X GET \

        'http://localhost:8181/env?env=TYK_MDCB_SYNCWORKERCONFIG_WARMUPTIME' \

        -H 'X-Tyk-Authorization: your-secret-key'

        ```
      operationId: envGet
      parameters:
        - in: header
          name: X-Tyk-Authorization
          description: Secret value set in sink.conf
          required: true
          schema:
            type: string
          example: your-secret-key
        - in: query
          name: env
          description: Optional environment variable name to filter by
          required: false
          schema:
            type: string
          example: TYK_MDCB_SYNCWORKERCONFIG_WARMUPTIME
      responses:
        '200':
          description: Successful retrieval of environment variables.
          content:
            application/json:
              schema:
                oneOf:
                  - type: array
                    items:
                      type: string
                  - $ref: '#/components/schemas/EnvVariable'
              examples:
                array_response:
                  summary: All environment variables
                  value:
                    - TYK_MDCB_ANALYTICSSTORAGE_SSLINSECURESKIPVERIFY=false
                    - TYK_MDCB_STORAGE_HOST=localhost
                    - TYK_MDCB_LISTENPORT=9090
                single_variable:
                  summary: Single environment variable (filtered by query parameter)
                  value:
                    config_field: sync_worker_config.warmup_time
                    env: TYK_MDCB_SYNCWORKERCONFIG_WARMUPTIME
                    value: '0'
                    obfuscated: false
        '400':
          description: Environment variable not found.
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: environment variable not found
        '401':
          description: Forbidden access due to invalid or missing administrative key.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    EnvVariable:
      type: object
      properties:
        config_field:
          type: string
          example: sync_worker_config.warmup_time
        env:
          type: string
          example: TYK_MDCB_SYNCWORKERCONFIG_WARMUPTIME
        value:
          type: string
          example: '0'
        obfuscated:
          type: boolean
          example: false
    Error:
      type: object
      properties:
        error:
          type: string
          example: Attempted administrative access with invalid or missing key!
  securitySchemes:
    api_key:
      in: header
      name: X-Tyk-Authorization
      type: apiKey

````

Built with [Mintlify](https://mintlify.com).