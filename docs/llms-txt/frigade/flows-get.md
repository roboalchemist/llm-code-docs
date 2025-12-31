# Source: https://docs.frigade.com/api-reference/flows/flows-get.md

# Get a Flow

> Get a single Flow by its Flow ID/slug.

## OpenAPI

````yaml get /v1/public/flows/{slug}
paths:
  path: /v1/public/flows/{slug}
  method: get
  request:
    security:
      - title: bearer
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Authentication header of the form `Bearer: <token>`, where
                `<token>` is either your public or private API key. [See when to
                use which](/v2/api-reference/authorization)
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: number
                    description: >-
                      The numeric ID of the Flow. This number will be different
                      depending on the version used
              name:
                allOf:
                  - type: string
                    description: The name of the Flow
                    example: New User Announcement
              data:
                allOf:
                  - type: string
                    description: >-
                      JSON encoded raw data of the Flow as defined in the Flow's
                      YAML configuration
                    example: >-
                      {"steps": [{"id": "step_1", "title": "Welcome to my app!",
                      "subtitle": "Let me show you around."}]}
              targetingLogic:
                allOf:
                  - type: string
                    description: The targeting logic for the Flow
                    example: user.property('isAdmin') == true
              type:
                allOf:
                  - type: string
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
                allOf:
                  - type: string
                    description: >-
                      A unique identifier for the Flow such as `flow_abc`. Slugs
                      stay the same between environment and versions.
                    example: flow_abc
              createdAt:
                allOf:
                  - format: date-time
                    type: string
                    description: The data the Flow was created in ISO 8601 format
                    example: '2024-01-01T00:00:00Z'
              modifiedAt:
                allOf:
                  - format: date-time
                    type: string
                    description: The data the Flow was last modified in ISO 8601 format
                    example: '2024-01-01T00:00:00Z'
              version:
                allOf:
                  - type: number
                    description: The version of the Flow
                    example: 1
              status:
                allOf:
                  - type: string
                    description: The status of the Flow
                    example: ACTIVE
                    enum:
                      - ACTIVE
                      - ARCHIVED
                      - DRAFT
              codeSnippet:
                allOf:
                  - type: string
                    description: The original code snippet for the Flow when it was created
                    example: <Frigade.Announcement flowId="my-flow-id" />
            refIdentifier: '#/components/schemas/ExternalizedFlow'
        examples:
          example:
            value:
              id: 123
              name: New User Announcement
              data: >-
                {"steps": [{"id": "step_1", "title": "Welcome to my app!",
                "subtitle": "Let me show you around."}]}
              targetingLogic: user.property('isAdmin') == true
              type: CHECKLIST
              slug: flow_abc
              createdAt: '2024-01-01T00:00:00Z'
              modifiedAt: '2024-01-01T00:00:00Z'
              version: 1
              status: ACTIVE
              codeSnippet: <Frigade.Announcement flowId="my-flow-id" />
        description: The Flow has been successfully returned.
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The Flow was not found.
        examples: {}
        description: The Flow was not found.
  deprecated: false
  type: path
components:
  schemas: {}

````