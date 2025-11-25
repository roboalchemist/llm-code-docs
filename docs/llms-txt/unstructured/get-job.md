# Source: https://docs.unstructured.io/api-reference/jobs/get-job.md

# Get Job

> Retrieve detailed information for a specific job by its ID.

## OpenAPI

````yaml https://platform.unstructuredapp.io/openapi.json get /api/v1/jobs/{job_id}
paths:
  path: /api/v1/jobs/{job_id}
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
      path:
        job_id:
          schema:
            - type: string
              required: true
              title: Job Id
              format: uuid
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
    body: {}
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
              workflow_id:
                allOf:
                  - type: string
                    format: uuid
                    title: Workflow Id
              workflow_name:
                allOf:
                  - type: string
                    title: Workflow Name
              status:
                allOf:
                  - $ref: '#/components/schemas/JobStatus'
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    title: Created At
              runtime:
                allOf:
                  - anyOf:
                      - type: string
                        format: duration
                      - type: 'null'
                    title: Runtime
              input_file_ids:
                allOf:
                  - anyOf:
                      - items:
                          type: string
                        type: array
                      - type: 'null'
                    title: Input File Ids
              output_node_files:
                allOf:
                  - anyOf:
                      - items:
                          $ref: '#/components/schemas/NodeFileMetadata'
                        type: array
                      - type: 'null'
                    title: Output Node Files
              job_type:
                allOf:
                  - $ref: '#/components/schemas/WorkflowJobType'
                    default: ephemeral
            title: JobInformation
            refIdentifier: '#/components/schemas/JobInformation'
            requiredProperties:
              - id
              - workflow_id
              - workflow_name
              - status
              - created_at
        examples:
          example:
            value:
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              workflow_id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              workflow_name: <string>
              status: SCHEDULED
              created_at: '2023-11-07T05:31:56Z'
              runtime: <string>
              input_file_ids:
                - <string>
              output_node_files:
                - node_id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  file_id: <string>
              job_type: ephemeral
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
      type: object
      required:
        - node_id
        - file_id
      title: NodeFileMetadata
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
    WorkflowJobType:
      type: string
      enum:
        - ephemeral
        - persistent
        - scheduled
        - template
      title: WorkflowJobType

````