# Source: https://braintrust.dev/docs/api-reference/proxy/create-temporary-credential.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create temporary credential

> Create a temporary credential which can access the proxy for a limited time. The temporary credential will be allowed to make requests on behalf of the Braintrust API key (or model provider API key) provided in the `Authorization` header. See [docs](/docs/deploy/ai-proxy#create-temporary-credentials) for code examples.



## OpenAPI

````yaml openapi.yaml post /v1/proxy/credentials
openapi: 3.1.1
info:
  version: 1.0.0
  title: Braintrust API
  description: >-
    API specification for the backend data server. The API is hosted globally at

    https://api.braintrust.dev or in your own environment.


    You can access the OpenAPI spec for this API at
    https://github.com/braintrustdata/braintrust-openapi.
  license:
    name: Apache 2.0
servers:
  - url: https://api.braintrust.dev
security:
  - bearerAuth: []
  - {}
paths:
  /v1/proxy/credentials:
    post:
      tags:
        - Proxy
      summary: Create temporary credential
      description: >-
        Create a temporary credential which can access the proxy for a limited
        time. The temporary credential will be allowed to make requests on
        behalf of the Braintrust API key (or model provider API key) provided in
        the `Authorization` header. See
        [docs](/docs/deploy/ai-proxy#create-temporary-credentials) for code
        examples.
      operationId: proxycredentials
      requestBody:
        description: >-
          The temporary credential will be restricted according to the request
          body.
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                model:
                  type: string
                  nullable: true
                  description: >-
                    Granted model name. Null/undefined to grant usage of all
                    models.
                ttl_seconds:
                  type: number
                  maximum: 86400
                  default: 600
                  description: TTL of the temporary credential. 10 minutes by default.
                logging:
                  type: object
                  nullable: true
                  properties:
                    project_name:
                      type: string
                    compress_audio:
                      type: boolean
                      default: true
                  required:
                    - project_name
                  description: >-
                    If present, proxy will log requests to the given Braintrust
                    project name.
              description: Payload for requesting temporary credentials.
      responses:
        '200':
          description: Successfully created temporary credential
          content:
            application/json:
              schema:
                type: object
                properties:
                  key:
                    type: string
                required:
                  - key
        '400':
          description: >-
            The request was unacceptable, often due to missing a required
            parameter
          content:
            text/plain:
              schema:
                type: string
      security:
        - bearerAuth: []
        - {}
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API key or JWT
      description: >-
        Most Braintrust endpoints are authenticated by providing your API key as
        a header `Authorization: Bearer [api_key]` to your HTTP request. You can
        create an API key in the Braintrust [organization settings
        page](https://www.braintrustdata.com/app/settings?subroute=api-keys).

````