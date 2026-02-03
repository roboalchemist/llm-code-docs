# Source: https://braintrust.dev/docs/api-reference/cors/enable-cors-`v1project`.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Enable CORS (`/v1/project`)

> Enable CORS



## OpenAPI

````yaml openapi.yaml options /v1/project
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
  /v1/project:
    options:
      tags:
        - CORS
      summary: Enable CORS (`/v1/project`)
      description: Enable CORS
      operationId: optionsProject
      responses:
        '200':
          description: Response for CORS method
          headers:
            Access-Control-Allow-Credentials:
              schema:
                type: string
            Access-Control-Allow-Headers:
              schema:
                type: string
            Access-Control-Allow-Methods:
              schema:
                type: string
            Access-Control-Allow-Origin:
              schema:
                type: string
            Access-Control-Max-Age:
              schema:
                type: string
          content: {}
        '400':
          description: >-
            The request was unacceptable, often due to missing a required
            parameter
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
      security: []
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