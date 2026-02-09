# Source: https://docs.lunary.ai/docs/api/users/get-a-specific-user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a specific user



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/external-users/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/external-users/{id}:
    get:
      tags:
        - Users
      summary: Get a specific user
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: string
        createdAt:
          type: string
          format: date-time
        externalId:
          type: string
        lastSeen:
          type: string
          format: date-time
        props:
          type: object
        cost:
          type: number

````