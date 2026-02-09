# Source: https://braintrust.dev/docs/api-reference/proxy/proxy-a-model-to-chatcompletions-or-completions-automatically.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Proxy a model to chat/completions or completions automatically

> Proxy a request to either chat/completions or completions automatically based on the model. Will cache if temperature=0 or seed is set.



## OpenAPI

````yaml openapi.yaml post /v1/proxy/auto
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
  /v1/proxy/auto:
    post:
      tags:
        - Proxy
      summary: Proxy a model to chat/completions or completions automatically
      description: >-
        Proxy a request to either chat/completions or completions automatically
        based on the model. Will cache if temperature=0 or seed is set.
      operationId: proxyauto
      requestBody:
        description: The chat/completions or completions payload (depending on the model)
        required: true
        content:
          application/json:
            schema:
              nullable: true
      responses:
        '200':
          description: Proxy response (supports both streaming and non-streaming formats)
          content:
            application/json:
              schema:
                nullable: true
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