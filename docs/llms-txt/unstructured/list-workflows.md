# Source: https://docs.unstructured.io/api-reference/workflows/list-workflows.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List Workflows

> Retrieve a list of workflows, optionally filtered by source, destination, state, name, date range, and supports pagination and sorting.



## OpenAPI

````yaml https://platform.unstructuredapp.io/openapi.json get /api/v1/workflows/
openapi: 3.1.0
info:
  title: Platform API
  version: 3.1.0
servers:
  - url: https://platform.unstructuredapp.io/
    description: Unstructured Platform API
    x-speakeasy-server-id: platform-api
security: []
paths:
  /api/v1/workflows/:
    get:
      tags:
        - workflows
      summary: List Workflows
      description: >-
        Retrieve a list of workflows, optionally filtered by source,
        destination, state, name, date range, and supports pagination and
        sorting.
      operationId: list_workflows
      parameters:
        - name: dag_node_configuration_id
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Dag Node Configuration Id
        - name: source_id
          in: query
          required: false
          schema:
            anyOf:
              - type: string
                format: uuid
              - type: 'null'
            title: Source Id
        - name: destination_id
          in: query
          required: false
          schema:
            anyOf:
              - type: string
                format: uuid
              - type: 'null'
            title: Destination Id
        - name: status
          in: query
          required: false
          schema:
            anyOf:
              - $ref: '#/components/schemas/WorkflowState'
              - type: 'null'
            title: Status
        - name: page
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            default: 1
            title: Page
        - name: page_size
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            default: 20
            title: Page Size
        - name: created_since
          in: query
          required: false
          schema:
            anyOf:
              - type: string
                format: date-time
              - type: 'null'
            title: Created Since
        - name: created_before
          in: query
          required: false
          schema:
            anyOf:
              - type: string
                format: date-time
              - type: 'null'
            title: Created Before
        - name: name
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Name
        - name: sort_by
          in: query
          required: false
          schema:
            type: string
            default: id
            title: Sort By
        - name: sort_direction
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/SortDirection'
            default: asc
        - name: show_only_soft_deleted
          in: query
          required: false
          schema:
            anyOf:
              - type: boolean
              - type: 'null'
            default: false
            title: Show Only Soft Deleted
        - name: show_recommender_workflows
          in: query
          required: false
          schema:
            anyOf:
              - type: boolean
              - type: 'null'
            default: false
            title: Show Recommender Workflows
        - name: unstructured-api-key
          in: header
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Unstructured-Api-Key
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/WorkflowInformation'
                title: Response List Workflows
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    WorkflowState:
      type: string
      enum:
        - active
        - inactive
      title: WorkflowState
    SortDirection:
      type: string
      enum:
        - asc
        - desc
      title: SortDirection
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
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    WorkflowType:
      type: string
      enum:
        - basic
        - advanced
        - platinum
        - custom
      title: WorkflowType
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
    CronTabEntry:
      properties:
        cron_expression:
          type: string
          title: Cron Expression
      type: object
      required:
        - cron_expression
      title: CronTabEntry

````