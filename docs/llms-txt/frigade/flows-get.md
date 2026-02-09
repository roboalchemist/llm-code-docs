# Source: https://docs.frigade.com/api-reference/flows/flows-get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a Flow

> Get a single Flow by its Flow ID/slug.



## OpenAPI

````yaml get /v1/public/flows/{slug}
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
  /v1/public/flows/{slug}:
    get:
      tags:
        - flows
      description: Get a single Flow by its Flow ID/slug.
      operationId: FlowsController_getBySlug
      parameters: []
      responses:
        '200':
          description: The Flow has been successfully returned.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ExternalizedFlow'
        '404':
          description: The Flow was not found.
      security:
        - bearer: []
components:
  schemas:
    ExternalizedFlow:
      type: object
      properties:
        id:
          type: number
          description: >-
            The numeric ID of the Flow. This number will be different depending
            on the version used
        name:
          type: string
          description: The name of the Flow
          example: New User Announcement
        data:
          type: string
          description: >-
            JSON encoded raw data of the Flow as defined in the Flow's YAML
            configuration
          example: >-
            {"steps": [{"id": "step_1", "title": "Welcome to my app!",
            "subtitle": "Let me show you around."}]}
        targetingLogic:
          type: string
          description: The targeting logic for the Flow
          example: user.property('isAdmin') == true
        type:
          type: string
          description: The type of Flow
          example: CHECKLIST
          enum:
            - ANNOUNCEMENT
            - BANNER
            - CARD
            - CHECKLIST
            - CUSTOM
            - FORM
            - SURVEY
            - TOUR
        slug:
          type: string
          description: >-
            A unique identifier for the Flow such as `flow_abc`. Slugs stay the
            same between environment and versions.
          example: flow_abc
        createdAt:
          format: date-time
          type: string
          description: The data the Flow was created in ISO 8601 format
          example: '2024-01-01T00:00:00Z'
        modifiedAt:
          format: date-time
          type: string
          description: The data the Flow was last modified in ISO 8601 format
          example: '2024-01-01T00:00:00Z'
        version:
          type: number
          description: The version of the Flow
          example: 1
        status:
          type: string
          description: The status of the Flow
          example: ACTIVE
          enum:
            - ACTIVE
            - ARCHIVED
            - DRAFT
        codeSnippet:
          type: string
          description: The original code snippet for the Flow when it was created
          example: <Frigade.Announcement flowId="my-flow-id" />
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