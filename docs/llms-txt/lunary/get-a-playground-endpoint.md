# Source: https://docs.lunary.ai/docs/api/playground-endpoints/get-a-playground-endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a playground endpoint

> Get a specific playground endpoint by ID



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/playground-endpoints/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/playground-endpoints/{id}:
    get:
      tags:
        - Playground Endpoints
      summary: Get a playground endpoint
      description: Get a specific playground endpoint by ID
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: 4bd06036-0e5a-4d67-ba4b-2f5fbdb818ed
        '404':
          description: Endpoint not found

````