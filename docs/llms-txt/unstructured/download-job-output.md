# Source: https://docs.unstructured.io/api-reference/jobs/download-job-output.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Download Job output

> Download the output of a job from a workflow where the input file was provided at runtime.



## OpenAPI

````yaml https://platform.unstructuredapp.io/openapi.json get /api/v1/jobs/{job_id}/download
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
  /api/v1/jobs/{job_id}/download:
    get:
      tags:
        - jobs
      summary: Download Job output
      description: >-
        Download the output of a job from a workflow where the input file was
        provided at runtime.
      operationId: download_job_output
      parameters:
        - name: job_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Job Id
        - name: file_id
          in: query
          required: true
          schema:
            type: string
            description: ID of the file to download
            title: File Id
          description: ID of the file to download
        - name: node_id
          in: query
          required: false
          schema:
            anyOf:
              - type: string
                format: uuid
              - type: 'null'
            description: >-
              Node ID to retrieve the corresponding output file.If not provided,
              uses the last node in the workflow.
            title: Node Id
          description: >-
            Node ID to retrieve the corresponding output file.If not provided,
            uses the last node in the workflow.
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
              schema: {}
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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