# Source: https://docs.lunary.ai/docs/api/test/test-endpoint-with-authentication-check.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Test endpoint with authentication check

> A test endpoint that validates authentication headers



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/test-endpoint/auth
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/test-endpoint/auth:
    post:
      tags:
        - Test
      summary: Test endpoint with authentication check
      description: A test endpoint that validates authentication headers
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
      responses:
        '200':
          description: Successful response with authentication info
        '401':
          description: Unauthorized - missing or invalid authentication
      security:
        - BearerAuth: []
        - ApiKeyAuth: []
        - BasicAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````