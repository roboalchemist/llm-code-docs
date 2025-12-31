# Source: https://docs.unstructured.io/api-reference/jobs/get-job-processing-details.md

# Get Job processing details

> Retrieve processing details for a specific job by its ID.

## OpenAPI

````yaml https://platform.unstructuredapp.io/openapi.json get /api/v1/jobs/{job_id}/details
paths:
  path: /api/v1/jobs/{job_id}/details
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
              processing_status:
                allOf:
                  - $ref: '#/components/schemas/JobProcessingStatus'
              node_stats:
                allOf:
                  - items:
                      $ref: '#/components/schemas/JobNodeDetails'
                    type: array
                    title: Node Stats
              message:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Message
            title: JobDetails
            refIdentifier: '#/components/schemas/JobDetails'
            requiredProperties:
              - id
              - processing_status
              - node_stats
        examples:
          example:
            value:
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              processing_status: SCHEDULED
              node_stats:
                - node_name: <string>
                  node_type: <string>
                  node_subtype: <string>
                  ready: 123
                  in_progress: 123
                  success: 123
                  failure: 123
              message: <string>
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