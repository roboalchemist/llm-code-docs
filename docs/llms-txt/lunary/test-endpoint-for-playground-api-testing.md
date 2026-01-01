# Source: https://docs.lunary.ai/docs/api/test/test-endpoint-for-playground-api-testing.md

# Test endpoint for playground API testing

> A public endpoint that echoes back the request data for testing the playground custom API feature



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/test-endpoint
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/test-endpoint:
    post:
      tags:
        - Test
      summary: Test endpoint for playground API testing
      description: >-
        A public endpoint that echoes back the request data for testing the
        playground custom API feature
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
      responses:
        '200':
          description: Successful response with echoed data
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    description: Success message
                  receivedAt:
                    type: string
                    format: date-time
                    description: When the request was received
                  echo:
                    type: object
                    description: The request data echoed back
                  headers:
                    type: object
                    description: Request headers received
                  method:
                    type: string
                    description: HTTP method used

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt