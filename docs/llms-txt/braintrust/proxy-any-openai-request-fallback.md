# Source: https://braintrust.dev/docs/api-reference/proxy/proxy-any-openai-request-fallback.md

# Proxy any OpenAI request (fallback)

> Any requests which do not match the above paths will be proxied directly to the OpenAI API.



## OpenAPI

````yaml openapi.yaml post /v1/proxy/{path+}
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
  /v1/proxy/{path+}:
    post:
      tags:
        - Proxy
      summary: Proxy any OpenAI request (fallback)
      description: >-
        Any requests which do not match the above paths will be proxied directly
        to the OpenAI API.
      operationId: proxy{path+}
      parameters:
        - name: path+
          in: path
          required: true
          schema:
            type: array
            items:
              type: string
          description: The path to proxy
      requestBody:
        description: The request body
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