# Source: https://docs.lunary.ai/docs/api/users/list-project-users.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List project users

> This endpoint retrieves a list of users tracked within the project.
It supports pagination, filtering, and sorting options.




## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/external-users
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/external-users:
    get:
      tags:
        - Users
      summary: List project users
      description: |
        This endpoint retrieves a list of users tracked within the project.
        It supports pagination, filtering, and sorting options.
      parameters:
        - in: query
          name: limit
          schema:
            type: integer
            default: 100
        - in: query
          name: page
          schema:
            type: integer
            default: 0
        - in: query
          name: search
          schema:
            type: string
        - in: query
          name: startDate
          schema:
            type: string
            format: date-time
        - in: query
          name: endDate
          schema:
            type: string
            format: date-time
        - in: query
          name: timeZone
          schema:
            type: string
        - in: query
          name: sortField
          schema:
            type: string
            default: createdAt
        - in: query
          name: sortDirection
          schema:
            type: string
            enum:
              - asc
              - desc
            default: desc
        - in: query
          name: checks
          schema:
            type: string
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                  page:
                    type: integer
                  limit:
                    type: integer
                  data:
                    type: array
                    items:
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