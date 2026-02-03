# Source: https://docs.unstructured.io/api-reference/workflows/run-workflow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Run Workflow

> Run a workflow by triggering a new job if none is currently active.



## OpenAPI

````yaml https://platform.unstructuredapp.io/openapi.json post /api/v1/workflows/{workflow_id}/run
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
  /api/v1/workflows/{workflow_id}/run:
    post:
      tags:
        - workflows
      summary: Run Workflow
      description: Run a workflow by triggering a new job if none is currently active.
      operationId: run_workflow
      parameters:
        - name: workflow_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Workflow Id
        - name: unstructured-api-key
          in: header
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Unstructured-Api-Key
      requestBody:
        content:
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Body_run_workflow'
      responses:
        '202':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JobInformation'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_run_workflow:
      properties:
        input_files:
          anyOf:
            - items:
                type: string
                format: binary
              type: array
            - type: 'null'
          title: Input Files
      type: object
      title: Body_run_workflow
    JobInformation:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        workflow_id:
          type: string
          format: uuid
          title: Workflow Id
        workflow_name:
          type: string
          title: Workflow Name
        status:
          $ref: '#/components/schemas/JobStatus'
        created_at:
          type: string
          format: date-time
          title: Created At
        runtime:
          anyOf:
            - type: string
              format: duration
            - type: 'null'
          title: Runtime
        input_file_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Input File Ids
        output_node_files:
          anyOf:
            - items:
                $ref: '#/components/schemas/NodeFileMetadata'
              type: array
            - type: 'null'
          title: Output Node Files
        job_type:
          $ref: '#/components/schemas/WorkflowJobType'
          default: ephemeral
      type: object
      required:
        - id
        - workflow_id
        - workflow_name
        - status
        - created_at
      title: JobInformation
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    JobStatus:
      type: string
      enum:
        - SCHEDULED
        - IN_PROGRESS
        - COMPLETED
        - STOPPED
        - FAILED
      title: JobStatus
    NodeFileMetadata:
      properties:
        node_id:
          type: string
          format: uuid
          title: Node Id
        file_id:
          type: string
          title: File Id
        node_type:
          type: string
          title: Node Type
        node_subtype:
          type: string
          title: Node Subtype
      type: object
      required:
        - node_id
        - file_id
        - node_type
        - node_subtype
      title: NodeFileMetadata
    WorkflowJobType:
      type: string
      enum:
        - ephemeral
        - persistent
        - scheduled
        - template
      title: WorkflowJobType
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

````