# Source: https://docs.baseten.co/reference/training-api/download-training-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Download training job source code

> Get the uploaded training job as a S3 Artifact



## OpenAPI

````yaml get /v1/training_projects/{training_project_id}/jobs/{training_job_id}/download
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
  /v1/training_projects/{training_project_id}/jobs/{training_job_id}/download:
    parameters:
      - $ref: '#/components/parameters/training_project_id'
      - $ref: '#/components/parameters/training_job_id'
    get:
      summary: Get the uploaded training job as a S3 Artifact
      description: Get the uploaded training job as a S3 Artifact
      responses:
        '200':
          description: A response that includes the artifacts for a training job
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DownloadTrainingJobResponseV1'
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
    DownloadTrainingJobResponseV1:
      description: A response that includes the artifacts for a training job
      properties:
        artifact_presigned_urls:
          description: Presigned URL's for the artifacts
          items:
            type: string
          title: Artifact Presigned Urls
          type: array
      required:
        - artifact_presigned_urls
      title: DownloadTrainingJobResponseV1
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