# Source: https://docs.unstructured.io/api-reference/jobs/get-job-processing-details.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Job processing details

> Retrieve processing details for a specific job by its ID.



## OpenAPI

````yaml https://platform.unstructuredapp.io/openapi.json get /api/v1/jobs/{job_id}/details
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
  /api/v1/jobs/{job_id}/details:
    get:
      tags:
        - jobs
      summary: Get Job processing details
      description: Retrieve processing details for a specific job by its ID.
      operationId: get_job_details
      parameters:
        - name: job_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Job Id
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
                $ref: '#/components/schemas/JobDetails'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    JobDetails:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        processing_status:
          $ref: '#/components/schemas/JobProcessingStatus'
        node_stats:
          items:
            $ref: '#/components/schemas/JobNodeDetails'
          type: array
          title: Node Stats
        message:
          anyOf:
            - type: string
            - type: 'null'
          title: Message
      type: object
      required:
        - id
        - processing_status
        - node_stats
      title: JobDetails
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    JobProcessingStatus:
      type: string
      enum:
        - SCHEDULED
        - IN_PROGRESS
        - SUCCESS
        - COMPLETED_WITH_ERRORS
        - STOPPED
        - FAILED
      title: JobProcessingStatus
    JobNodeDetails:
      properties:
        node_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Node Name
        node_type:
          anyOf:
            - type: string
            - type: 'null'
          title: Node Type
        node_subtype:
          anyOf:
            - type: string
            - type: 'null'
          title: Node Subtype
        ready:
          type: integer
          title: Ready
        in_progress:
          type: integer
          title: In Progress
        success:
          type: integer
          title: Success
        failure:
          type: integer
          title: Failure
      type: object
      required:
        - ready
        - in_progress
        - success
        - failure
      title: JobNodeDetails
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