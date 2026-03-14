# Source: https://docs.linkup.so/pages/documentation/api-reference/endpoint/get-balance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# /credits/balance

> The `/credits/balance` endpoint allows you to retrieve your current credits balance.

The **`/credits/balance`** endpoint allows you to check your current credit balance.

<Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
  Create a Linkup account for free to get your API key.
</Card>


## OpenAPI

````yaml https://api.linkup.so/v1/openapi.json get /v1/credits/balance
openapi: 3.0.0
info:
  title: Linkup API
  description: >-
    Search the web in real time to get trustworthy, source-backed answers. Find
    the latest news and comprehensive results from the most relevant sources.
    Use natural language queries to quickly gather facts, citations, and
    context.
  version: '1.0'
  contact: {}
servers:
  - url: https://api.linkup.so
security: []
tags: []
paths:
  /v1/credits/balance:
    get:
      tags:
        - Credits
      summary: /credits/balance
      description: >-
        The `/credits/balance` endpoint allows you to retrieve your current
        credits balance.
      operationId: balance
      parameters: []
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreditDto'
        '401':
          description: Unauthorized - Invalid or missing API key
      security:
        - bearer: []
components:
  schemas:
    CreditDto:
      type: object
      properties:
        balance:
          type: number
          description: The number of credits remaining in your account.
          example: 123.456
      required:
        - balance
  securitySchemes:
    bearer:
      scheme: bearer
      bearerFormat: JWT
      type: http

````

Built with [Mintlify](https://mintlify.com).