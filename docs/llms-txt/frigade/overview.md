# Source: https://docs.frigade.com/sdk/overview.md

# Source: https://docs.frigade.com/platform/overview.md

# Source: https://docs.frigade.com/overview.md

# Source: https://docs.frigade.com/integrations/overview.md

# Source: https://docs.frigade.com/component/overview.md

# Source: https://docs.frigade.com/api-reference/users/overview.md

# Source: https://docs.frigade.com/api-reference/groups/overview.md

# Source: https://docs.frigade.com/api-reference/flows/overview.md

# Source: https://docs.frigade.com/sdk/overview.md

# Source: https://docs.frigade.com/platform/overview.md

# Source: https://docs.frigade.com/overview.md

# Source: https://docs.frigade.com/integrations/overview.md

# Source: https://docs.frigade.com/component/overview.md

# Source: https://docs.frigade.com/api-reference/users/overview.md

# Source: https://docs.frigade.com/api-reference/groups/overview.md

# Source: https://docs.frigade.com/api-reference/flows/overview.md

# Source: https://docs.frigade.com/sdk/overview.md

# Source: https://docs.frigade.com/platform/overview.md

# Source: https://docs.frigade.com/overview.md

# Source: https://docs.frigade.com/integrations/overview.md

# Source: https://docs.frigade.com/component/overview.md

# Source: https://docs.frigade.com/api-reference/users/overview.md

# Source: https://docs.frigade.com/api-reference/groups/overview.md

# Source: https://docs.frigade.com/api-reference/flows/overview.md

# Source: https://docs.frigade.com/sdk/overview.md

# Source: https://docs.frigade.com/platform/overview.md

# Source: https://docs.frigade.com/overview.md

# Source: https://docs.frigade.com/integrations/overview.md

# Source: https://docs.frigade.com/component/overview.md

# Source: https://docs.frigade.com/api-reference/users/overview.md

# Source: https://docs.frigade.com/api-reference/groups/overview.md

# Source: https://docs.frigade.com/api-reference/flows/overview.md

# Source: https://docs.frigade.com/sdk/overview.md

# Source: https://docs.frigade.com/platform/overview.md

# Source: https://docs.frigade.com/overview.md

# Source: https://docs.frigade.com/integrations/overview.md

# Source: https://docs.frigade.com/component/overview.md

# Source: https://docs.frigade.com/api-reference/users/overview.md

# Source: https://docs.frigade.com/api-reference/groups/overview.md

# Source: https://docs.frigade.com/api-reference/flows/overview.md

# Get all Flows

> Get all Flows for your organization.

## OpenAPI

````yaml get /v1/public/flows
paths:
  path: /v1/public/flows
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
              data:
                allOf:
                  - description: The data returned by the query
                    type: array
                    items:
                      $ref: '#/components/schemas/ExternalizedFlow'
              offset:
                allOf:
                  - type: number
                    description: The current pagination offset (if any)
                    default: 0
                    example: 0
              limit:
                allOf:
                  - type: number
                    description: The total number of records returned in this response
                    default: 100
                    example: 100
            refIdentifier: '#/components/schemas/PaginatedResult'
        examples:
          example:
            value:
              data:
                - id: 123
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
              offset: 0
              limit: 100
        description: Return all flows.
  deprecated: false
  type: path
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

````