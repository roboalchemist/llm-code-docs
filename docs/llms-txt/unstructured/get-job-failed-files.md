# Source: https://docs.unstructured.io/api-reference/jobs/get-job-failed-files.md

# Get Job Failed Files

> Retrieve failed files for a specific job by its ID.

## OpenAPI

````yaml https://platform.unstructuredapp.io/openapi.json get /api/v1/jobs/{job_id}/failed-files
paths:
  path: /api/v1/jobs/{job_id}/failed-files
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
              failed_files:
                allOf:
                  - items:
                      $ref: '#/components/schemas/FailedFile'
                    type: array
                    title: Failed Files
            title: JobFailedFiles
            refIdentifier: '#/components/schemas/JobFailedFiles'
            requiredProperties:
              - failed_files
        examples:
          example:
            value:
              failed_files:
                - document: <string>
                  error: <string>
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
    FailedFile:
      properties:
        document:
          type: string
          title: Document
        error:
          type: string
          title: Error
      type: object
      required:
        - document
        - error
      title: FailedFile
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