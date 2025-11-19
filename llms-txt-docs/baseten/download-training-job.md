# Source: https://docs.baseten.co/reference/training-api/download-training-job.md

# Download training job source code

> Get the uploaded training job as a S3 Artifact

## OpenAPI

````yaml get /v1/training_projects/{training_project_id}/jobs/{training_job_id}/download
paths:
  path: /v1/training_projects/{training_project_id}/jobs/{training_job_id}/download
  method: get
  servers:
    - url: https://api.baseten.co
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
              description: >-
                You must specify the scheme 'Api-Key' in the Authorization
                header. For example, `Authorization: Api-Key <Your_Api_Key>`
          cookie: {}
    parameters:
      path:
        training_project_id:
          schema:
            - type: string
              required: true
        training_job_id:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - lang: bash
        source: >
          curl --request GET \

          --url
          https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}/download
          \

          --header "Authorization: Api-Key $BASETEN_API_KEY"
      - lang: python
        source: >-
          import requests

          import os

          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

          url =
          "https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}/download"


          headers = {"Authorization": f"Api-Key {API_KEY}"}


          response = requests.request(
              "GET",
              url,
              headers=headers,
              json={}
          )


          print(response.text)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              artifact_presigned_urls:
                allOf:
                  - description: Presigned URL's for the artifacts
                    items:
                      type: string
                    title: Artifact Presigned Urls
                    type: array
            title: DownloadTrainingJobResponseV1
            description: A response that includes the artifacts for a training job
            refIdentifier: '#/components/schemas/DownloadTrainingJobResponseV1'
            requiredProperties:
              - artifact_presigned_urls
        examples:
          example:
            value:
              artifact_presigned_urls:
                - <string>
        description: A response that includes the artifacts for a training job
  deprecated: false
  type: path
components:
  schemas: {}

````