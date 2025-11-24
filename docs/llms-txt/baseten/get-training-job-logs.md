# Source: https://docs.baseten.co/reference/training-api/get-training-job-logs.md

# Get training job logs

> Get the logs for a training job with the provided filters.

## OpenAPI

````yaml post /v1/training_projects/{training_project_id}/jobs/{training_job_id}/logs
paths:
  path: /v1/training_projects/{training_project_id}/jobs/{training_job_id}/logs
  method: post
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              start_epoch_millis:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    default: null
                    description: Epoch millis timestamp to start fetching logs
                    title: Start Epoch Millis
              end_epoch_millis:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    default: null
                    description: Epoch millis timestamp to end fetching logs
                    title: End Epoch Millis
              direction:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/SortOrderV1'
                      - type: 'null'
                    default: null
                    description: Sort order for logs
              limit:
                allOf:
                  - anyOf:
                      - maximum: 1000
                        minimum: 1
                        type: integer
                      - type: 'null'
                    default: 500
                    description: Limit of logs to fetch in a single request
                    title: Limit
            required: true
            title: GetTrainingJobLogsRequestV1
            description: A request to fetch training logs.
            refIdentifier: '#/components/schemas/GetTrainingJobLogsRequestV1'
        examples:
          example:
            value:
              start_epoch_millis: 123
              end_epoch_millis: 123
              direction: asc
              limit: 500
    codeSamples:
      - lang: bash
        source: >-
          curl --request POST \

          --url
          https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}/logs
          \

          --header "Authorization: Api-Key $BASETEN_API_KEY" \

          --data '{
            "start_epoch_millis": null,
            "end_epoch_millis": null,
            "direction": null,
            "limit": null
          }'
      - lang: python
        source: >-
          import requests

          import os

          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

          url =
          "https://api.baseten.co/v1/training_projects/{training_project_id}/jobs/{training_job_id}/logs"


          headers = {"Authorization": f"Api-Key {API_KEY}"}


          response = requests.request(
              "POST",
              url,
              headers=headers,
              json={'start_epoch_millis': None, 'end_epoch_millis': None, 'direction': None, 'limit': None}
          )


          print(response.text)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              logs:
                allOf:
                  - description: Logs for a specific entity.
                    items:
                      $ref: '#/components/schemas/LogV1'
                    title: Logs
                    type: array
            title: GetLogsResponseV1
            description: A response to querying logs.
            refIdentifier: '#/components/schemas/GetLogsResponseV1'
            requiredProperties:
              - logs
        examples:
          example:
            value:
              logs:
                - timestamp: <string>
                  message: <string>
                  replica: <string>
        description: A response to querying logs.
  deprecated: false
  type: path
components:
  schemas:
    SortOrderV1:
      enum:
        - asc
        - desc
      title: SortOrderV1
      type: string
    LogV1:
      properties:
        timestamp:
          description: Epoch nanosecond timestamp of the log message.
          title: Timestamp
          type: string
        message:
          description: The contents of the log message.
          title: Message
          type: string
        replica:
          anyOf:
            - type: string
            - type: 'null'
          description: The replica the log line was emitted from.
          title: Replica
      required:
        - timestamp
        - message
        - replica
      title: LogV1
      type: object

````