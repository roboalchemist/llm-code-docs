# Source: https://docs.unstructured.io/api-reference/jobs/get-job-failed-files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Job Failed Files

> Retrieve failed files for a specific job by its ID.



## OpenAPI

````yaml https://platform.unstructuredapp.io/openapi.json get /api/v1/jobs/{job_id}/failed-files
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
  /api/v1/jobs/{job_id}/failed-files:
    get:
      tags:
        - jobs
      summary: Get Job Failed Files
      description: Retrieve failed files for a specific job by its ID.
      operationId: get_job_failed_files
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
                $ref: '#/components/schemas/JobFailedFiles'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    JobFailedFiles:
      properties:
        failed_files:
          items:
            $ref: '#/components/schemas/FailedFile'
          type: array
          title: Failed Files
      type: object
      required:
        - failed_files
      title: JobFailedFiles
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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