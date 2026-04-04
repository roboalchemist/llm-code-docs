# Source: https://docs.lunary.ai/docs/api/playground-endpoints/create-a-playground-endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a playground endpoint

> Create a new playground endpoint



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/playground-endpoints
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/playground-endpoints:
    post:
      tags:
        - Playground Endpoints
      summary: Create a playground endpoint
      description: Create a new playground endpoint
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: c9f91f28-a872-4e0d-8c0c-0ffccfd5d2b4
      responses:
        '201':
          description: Endpoint created successfully
          content:
            application/json:
              schema:
                $ref: 4bd06036-0e5a-4d67-ba4b-2f5fbdb818ed

````