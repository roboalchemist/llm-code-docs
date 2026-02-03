# Source: https://docs.infera.org/api-reference/endpoint/get-available-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.infera.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Available Models



## OpenAPI

````yaml get /available_models
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.infera.org/
    description: Infera production servers
security: []
paths:
  /available_models:
    get:
      summary: Get Available Models
      operationId: get_available_models_available_models_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
      security:
        - APIKeyHeader: []
components:
  securitySchemes:
    APIKeyHeader:
      type: apiKey
      in: header
      name: api_key

````