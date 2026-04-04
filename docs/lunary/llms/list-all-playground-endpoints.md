# Source: https://docs.lunary.ai/docs/api/playground-endpoints/list-all-playground-endpoints.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List all playground endpoints

> Get all playground endpoints for the current project



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/playground-endpoints
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
    get:
      tags:
        - Playground Endpoints
      summary: List all playground endpoints
      description: Get all playground endpoints for the current project
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: array
                items: 4a64c960-207b-449f-bbf0-b58fc245fd47

````