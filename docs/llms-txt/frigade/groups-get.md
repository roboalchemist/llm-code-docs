# Source: https://docs.frigade.com/api-reference/groups/groups-get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Find a Group

> Find a group by ID



## OpenAPI

````yaml get /v1/groups
openapi: 3.0.0
info:
  title: Frigade API
  description: Official Frigade API documentation
  version: '1.0'
  contact: {}
servers: []
security: []
tags: []
paths:
  /v1/groups:
    get:
      tags:
        - groups
      description: Find a group by ID
      operationId: UserGroupsController_get
      parameters:
        - name: groupId
          required: true
          in: query
          description: The ID of the group
          schema:
            type: string
      responses:
        '200':
          description: The group was successfully found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ExternalizedUserGroup'
        '404':
          description: The group was not found
      security:
        - bearer: []
components:
  schemas:
    ExternalizedUserGroup:
      type: object
      properties:
        name:
          type: string
          description: The name of the group
          example: Acme Inc.
        groupId:
          type: string
          description: The ID of the group as defined in your own application
          example: x34daa11-3745-4ac0-880e-d4b4d51fe13f
        createdAt:
          format: date-time
          type: string
          description: The date the group was created
          example: '2021-01-01T00:00:00.000Z'
        modifiedAt:
          format: date-time
          type: string
          description: The date the group was last modified
          example: '2021-01-01T00:00:00.000Z'
        properties:
          type: string
          description: The properties of the group
          example:
            name: Acme Inc.
            companyUrl: https://example.com
            logoUrl: https://example.com/logo.jpg
        membersCount:
          type: number
          description: The number of members in the group
          example: 42
        trackingEvents:
          description: The tracking events associated with the group
          example:
            - event: SignedUp
              properties:
                source: landing-page
                campaign: summer-sale
              createdAt: '2024-01-01T00:00:00Z'
          type: array
          items:
            type: string
  securitySchemes:
    bearer:
      scheme: bearer
      bearerFormat: JWT
      type: http
      description: >-
        Authentication header of the form `Bearer: <token>`, where `<token>` is
        either your public or private API key. [See when to use
        which](/v2/api-reference/authorization)

````