# Source: https://docs.lunary.ai/docs/api/playground-endpoints/update-a-playground-endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a playground endpoint

> Update an existing playground endpoint



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi put /v1/playground-endpoints/{id}
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
    put:
      tags:
        - Playground Endpoints
      summary: Update a playground endpoint
      description: Update an existing playground endpoint
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: 31a68629-cdb7-4daf-9513-a3ecd607266c
      responses:
        '200':
          description: Endpoint updated successfully
          content:
            application/json:
              schema:
                $ref: 4bd06036-0e5a-4d67-ba4b-2f5fbdb818ed
        '404':
          description: Endpoint not found

````