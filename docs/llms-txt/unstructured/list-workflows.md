# Source: https://docs.unstructured.io/api-reference/workflows/list-workflows.md

# List Workflows

> Retrieve a list of workflows, optionally filtered by source, destination, state, name, date range, and supports pagination and sorting.

## OpenAPI

````yaml https://platform.unstructuredapp.io/openapi.json get /api/v1/workflows/
paths:
  path: /api/v1/workflows/
  method: get
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
      query:
        dag_node_configuration_id:
          schema:
            - type: string
              required: false
              title: Dag Node Configuration Id
            - type: 'null'
              required: false
              title: Dag Node Configuration Id
        source_id:
          schema:
            - type: string
              required: false
              title: Source Id
              format: uuid
            - type: 'null'
              required: false
              title: Source Id
        destination_id:
          schema:
            - type: string
              required: false
              title: Destination Id
              format: uuid
            - type: 'null'
              required: false
              title: Destination Id
        status:
          schema:
            - type: enum<string>
              enum:
                - active
                - inactive
              required: false
              title: WorkflowState
              refIdentifier: '#/components/schemas/WorkflowState'
            - type: 'null'
              required: false
              title: Status
        page:
          schema:
            - type: integer
              required: false
              title: Page
              default: 1
            - type: 'null'
              required: false
              title: Page
              default: 1
        page_size:
          schema:
            - type: integer
              required: false
              title: Page Size
              default: 20
            - type: 'null'
              required: false
              title: Page Size
              default: 20
        created_since:
          schema:
            - type: string
              required: false
              title: Created Since
              format: date-time
            - type: 'null'
              required: false
              title: Created Since
        created_before:
          schema:
            - type: string
              required: false
              title: Created Before
              format: date-time
            - type: 'null'
              required: false
              title: Created Before
        name:
          schema:
            - type: string
              required: false
              title: Name
            - type: 'null'
              required: false
              title: Name
        sort_by:
          schema:
            - type: string
              required: false
              title: Sort By
              default: id
        sort_direction:
          schema:
            - type: enum<string>
              enum:
                - asc
                - desc
              required: false
              title: SortDirection
        show_only_soft_deleted:
          schema:
            - type: boolean
              required: false
              title: Show Only Soft Deleted
              default: false
            - type: 'null'
              required: false
              title: Show Only Soft Deleted
              default: false
        show_recommender_workflows:
          schema:
            - type: boolean
              required: false
              title: Show Recommender Workflows
              default: false
            - type: 'null'
              required: false
              title: Show Recommender Workflows
              default: false
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
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/WorkflowInformation'
            title: Response List Workflows
        examples:
          example:
            value:
              - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
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
    WorkflowInformation:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        name:
          type: string
          title: Name
        sources:
          items:
            type: string
            format: uuid
          type: array
          title: Sources
        destinations:
          items:
            type: string
            format: uuid
          type: array
          title: Destinations
        workflow_type:
          anyOf:
            - $ref: '#/components/schemas/WorkflowType'
            - type: 'null'
        workflow_nodes:
          items:
            $ref: '#/components/schemas/WorkflowNode'
          type: array
          title: Workflow Nodes
        schedule:
          anyOf:
            - $ref: '#/components/schemas/WorkflowSchedule'
            - type: 'null'
        status:
          $ref: '#/components/schemas/WorkflowState'
        created_at:
          type: string
          format: date-time
          title: Created At
        updated_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Updated At
        reprocess_all:
          type: boolean
          title: Reprocess All
          default: false
      type: object
      required:
        - id
        - name
        - sources
        - destinations
        - workflow_nodes
        - status
        - created_at
      title: WorkflowInformation
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