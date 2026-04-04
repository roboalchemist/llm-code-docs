# Source: https://docs.frigade.com/api-reference/flows/flows-put.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Flow

> Update a Flow's configuration and metadata

As this endpoint modifies data, you will need to use the [private API key](/api-reference/authorization).

<Warning>Only call this endpoint from your backend code.</Warning>

### Obtaining the numeric ID of a Flow

To obtain the numeric ID of a Flow, you should make a [GET request](/api-reference/flows/flows-get) to get the Flow you are looking to change. The numeric ID is a number and is different from the slug (e.g. `flow_GzXC2fHz`). The reason for this is that different [versions](/platform/versioning) of the Flow share the same slug but have different numeric IDs to differentiate them.


## OpenAPI

````yaml put /v1/flows/{numericFlowId}
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
  /v1/flows/{numericFlowId}:
    put:
      tags:
        - flows
      description: Update a Flow's configuration and metadata
      operationId: FlowsController_update
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateFlowDto'
      responses:
        '200':
          description: The flow has been successfully updated.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ExternalizedFlow'
      security:
        - bearer: []
components:
  schemas:
    UpdateFlowDto:
      type: object
      properties:
        name:
          type: string
          description: The name of the Flow
          example: New User Announcement
        data:
          type: string
          description: >-
            JSON or YAML encoded raw data of thew Flow. If provided in JSON
            format it will be converted to YAML automatically
          example: >-
            {"steps": [{"id": "step_1", "title": "Welcome to my app!",
            "subtitle": "Let me show you around."}]}
        description:
          type: string
          description: The description of the Flow
          example: This is a Flow that welcomes new users to the app
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
        active:
          type: boolean
          description: >-
            Whether the Flow is active or not. If set to `false`, the Flow will
            not be shown to users
          example: true
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