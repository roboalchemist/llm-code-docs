# Source: https://docs.fireworks.ai/api-reference/get-dpo-job-metrics-file-endpoint.md

# null

## OpenAPI

````yaml get /v1/accounts/{account_id}/dpoJobs/{dpo_job_id}:getMetricsFileEndpoint
paths:
  path: /v1/accounts/{account_id}/dpoJobs/{dpo_job_id}:getMetricsFileEndpoint
  method: get
  servers:
    - url: https://api.fireworks.ai
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer authentication using your Fireworks API key. Format:
                Bearer <API_KEY>
          cookie: {}
    parameters:
      path:
        account_id:
          schema:
            - type: string
              required: true
              description: The Account Id
        dpo_job_id:
          schema:
            - type: string
              required: true
              description: The Dpo Job Id
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              signedUrl:
                allOf:
                  - type: string
                    title: The signed URL for the metrics file
            title: |-
              when the JobMetrics file has been created for the DPO job
              and the file exists, we will populate this field
              empty otherwise
            refIdentifier: '#/components/schemas/gatewayGetDpoJobMetricsFileResponse'
        examples:
          example:
            value:
              signedUrl: <string>
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas: {}

````