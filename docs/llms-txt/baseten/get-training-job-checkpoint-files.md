# Source: https://docs.baseten.co/reference/training-api/get-training-job-checkpoint-files.md

# Get training job checkpoint files

> Get presigned URLs for all checkpoint files for a training job.

## OpenAPI

````yaml get /v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoint_files
paths:
  path: >-
    /v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoint_files
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
          https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoint_files
          \

          --header "Authorization: Api-Key $BASETEN_API_KEY"
      - lang: python
        source: >-
          import requests

          import os

          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

          url =
          "https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoint_files"


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
              presigned_urls:
                allOf:
                  - description: List of presigned URLs for checkpoint files.
                    items:
                      $ref: '#/components/schemas/CheckpointFile'
                    title: Presigned Urls
                    type: array
              next_page_token:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    default: null
                    description: >-
                      Token to use for fetching the next page of results. None
                      when there are no more results.
                    title: Next Page Token
              total_count:
                allOf:
                  - description: Total number of checkpoint files available.
                    title: Total Count
                    type: integer
            title: GetTrainingJobCheckpointFilesResponseV1
            description: >-
              A response to fetch presigned URLs for checkpoint files of a
              training job.
            refIdentifier: '#/components/schemas/GetTrainingJobCheckpointFilesResponseV1'
            requiredProperties:
              - presigned_urls
              - total_count
        examples:
          example:
            value:
              presigned_urls:
                - url: <string>
                  relative_file_name: <string>
                  node_rank: 123
                  size_bytes: 123
                  last_modified: <string>
              next_page_token: 123
              total_count: 123
        description: >-
          A response to fetch presigned URLs for checkpoint files of a training
          job.
  deprecated: false
  type: path
components:
  schemas:
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

````