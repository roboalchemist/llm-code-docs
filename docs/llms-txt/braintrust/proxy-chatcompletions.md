# Source: https://braintrust.dev/docs/api-reference/proxy/proxy-chatcompletions.md

# Proxy chat/completions

> Proxy a chat/completions request to the specified model, converting its format as needed. Will cache if temperature=0 or seed is set.



## OpenAPI

````yaml openapi.yaml post /v1/proxy/chat/completions
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
  /v1/proxy/chat/completions:
    post:
      tags:
        - Proxy
      summary: Proxy chat/completions
      description: >-
        Proxy a chat/completions request to the specified model, converting its
        format as needed. Will cache if temperature=0 or seed is set.
      operationId: proxychatCompletions
      requestBody:
        description: >-
          See the [OpenAI
          docs](https://platform.openai.com/docs/api-reference/chat/create) for
          details.
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt