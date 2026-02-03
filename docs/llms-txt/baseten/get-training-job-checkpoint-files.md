# Source: https://docs.baseten.co/reference/training-api/get-training-job-checkpoint-files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get training job checkpoint files

> Get presigned URLs for all checkpoint files for a training job.



## OpenAPI

````yaml get /v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoint_files
openapi: 3.1.0
info:
  description: REST API for management of Baseten resources
  title: Baseten management API
  version: 1.0.0
servers:
  - url: https://api.baseten.co
security:
  - ApiKeyAuth: []
paths:
  /v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoint_files:
    parameters:
      - $ref: '#/components/parameters/training_project_id'
      - $ref: '#/components/parameters/training_job_id'
    get:
      summary: Get training job checkpoint files.
      description: Get presigned URLs for all checkpoint files for a training job.
      responses:
        '200':
          description: >-
            A response to fetch presigned URLs for checkpoint files of a
            training job.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetTrainingJobCheckpointFilesResponseV1'
components:
  parameters:
    training_project_id:
      schema:
        type: string
      name: training_project_id
      in: path
      required: true
    training_job_id:
      schema:
        type: string
      name: training_job_id
      in: path
      required: true
  schemas:
    GetTrainingJobCheckpointFilesResponseV1:
      description: >-
        A response to fetch presigned URLs for checkpoint files of a training
        job.
      properties:
        presigned_urls:
          description: List of presigned URLs for checkpoint files.
          items:
            $ref: '#/components/schemas/CheckpointFile'
          title: Presigned Urls
          type: array
        next_page_token:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: >-
            Token to use for fetching the next page of results. None when there
            are no more results.
          title: Next Page Token
        total_count:
          description: Total number of checkpoint files available.
          title: Total Count
          type: integer
      required:
        - presigned_urls
        - total_count
      title: GetTrainingJobCheckpointFilesResponseV1
      type: object
    CheckpointFile:
      properties:
        url:
          title: Url
          type: string
        relative_file_name:
          title: Relative File Name
          type: string
        node_rank:
          title: Node Rank
          type: integer
        size_bytes:
          title: Size Bytes
          type: integer
        last_modified:
          title: Last Modified
          type: string
      required:
        - url
        - relative_file_name
        - node_rank
        - size_bytes
        - last_modified
      title: CheckpointFile
      type: object
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Authorization
      description: >-
        You must specify the scheme 'Api-Key' in the Authorization header. For
        example, `Authorization: Api-Key <Your_Api_Key>`

````