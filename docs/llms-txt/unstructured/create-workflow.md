# Source: https://docs.unstructured.io/api-reference/workflows/create-workflow.md

# Create Workflow

> Create a new workflow, either custom or auto, and configure its settings.

## OpenAPI

````yaml https://platform.unstructuredapp.io/openapi.json post /api/v1/workflows/
paths:
  path: /api/v1/workflows/
  method: post
  servers:
    - url: https://platform.unstructuredapp.io/
      description: Unstructured Platform API
  request:
    security:
      - title: HTTPBearer
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path: {}
      query: {}
      header:
        unstructured-api-key:
          schema:
            - type: string
              required: false
              title: Unstructured-Api-Key
            - type: 'null'
              required: false
              title: Unstructured-Api-Key
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    title: Name
              source_id:
                allOf:
                  - anyOf:
                      - type: string
                        format: uuid
                      - type: 'null'
                    title: Source Id
              destination_id:
                allOf:
                  - anyOf:
                      - type: string
                        format: uuid
                      - type: 'null'
                    title: Destination Id
              workflow_type:
                allOf:
                  - $ref: '#/components/schemas/WorkflowType'
              workflow_nodes:
                allOf:
                  - anyOf:
                      - items:
                          $ref: '#/components/schemas/WorkflowNode'
                        type: array
                      - type: 'null'
                    title: Workflow Nodes
              template_id:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Template Id
              schedule:
                allOf:
                  - anyOf:
                      - type: string
                        enum:
                          - every 15 minutes
                          - every hour
                          - every 2 hours
                          - every 4 hours
                          - every 6 hours
                          - every 8 hours
                          - every 10 hours
                          - every 12 hours
                          - daily
                          - weekly
                          - monthly
                      - type: 'null'
                    title: Schedule
              reprocess_all:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Reprocess All
                    default: false
            required: true
            title: CreateWorkflow
            refIdentifier: '#/components/schemas/CreateWorkflow'
            requiredProperties:
              - name
              - workflow_type
        examples:
          example:
            value:
              name: <string>
              source_id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              destination_id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              workflow_type: basic
              workflow_nodes:
                - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  name: <string>
                  type: <string>
                  subtype: <string>
                  settings: {}
              template_id: <string>
              schedule: every 15 minutes
              reprocess_all: true
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid
                    title: Id
              name:
                allOf:
                  - type: string
                    title: Name
              sources:
                allOf:
                  - items:
                      type: string
                      format: uuid
                    type: array
                    title: Sources
              destinations:
                allOf:
                  - items:
                      type: string
                      format: uuid
                    type: array
                    title: Destinations
              workflow_type:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/WorkflowType'
                      - type: 'null'
              workflow_nodes:
                allOf:
                  - items:
                      $ref: '#/components/schemas/WorkflowNode'
                    type: array
                    title: Workflow Nodes
              schedule:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/WorkflowSchedule'
                      - type: 'null'
              status:
                allOf:
                  - $ref: '#/components/schemas/WorkflowState'
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    title: Created At
              updated_at:
                allOf:
                  - anyOf:
                      - type: string
                        format: date-time
                      - type: 'null'
                    title: Updated At
              reprocess_all:
                allOf:
                  - type: boolean
                    title: Reprocess All
                    default: false
            title: WorkflowInformation
            refIdentifier: '#/components/schemas/WorkflowInformation'
            requiredProperties:
              - id
              - name
              - sources
              - destinations
              - workflow_nodes
              - status
              - created_at
        examples:
          example:
            value:
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              name: <string>
              sources:
                - 3c90c3cc-0d44-4b50-8888-8dd25736052a
              destinations:
                - 3c90c3cc-0d44-4b50-8888-8dd25736052a
              workflow_type: basic
              workflow_nodes:
                - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  name: <string>
                  type: <string>
                  subtype: <string>
                  settings: {}
              schedule:
                crontab_entries:
                  - cron_expression: 0 0 * * *
              status: active
              created_at: '2023-11-07T05:31:56Z'
              updated_at: '2023-11-07T05:31:56Z'
              reprocess_all: false
        description: Successful Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    type: array
                    title: Detail
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
    CronTabEntry:
      properties:
        cron_expression:
          type: string
          title: Cron Expression
      type: object
      required:
        - cron_expression
      title: CronTabEntry
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
    WorkflowNode:
      properties:
        id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Id
        name:
          type: string
          title: Name
        type:
          type: string
          title: Type
        subtype:
          type: string
          title: Subtype
        settings:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Settings
      type: object
      required:
        - name
        - type
        - subtype
      title: WorkflowNode
    WorkflowSchedule:
      properties:
        crontab_entries:
          items:
            $ref: '#/components/schemas/CronTabEntry'
          type: array
          title: Crontab Entries
      type: object
      required:
        - crontab_entries
      title: WorkflowSchedule
      examples:
        - crontab_entries:
            - cron_expression: 0 0 * * *
    WorkflowState:
      type: string
      enum:
        - active
        - inactive
      title: WorkflowState
    WorkflowType:
      type: string
      enum:
        - basic
        - advanced
        - platinum
        - custom
        - template
      title: WorkflowType

````