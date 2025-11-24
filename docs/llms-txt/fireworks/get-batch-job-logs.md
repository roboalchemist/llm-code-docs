# Source: https://docs.fireworks.ai/api-reference-dlde/get-batch-job-logs.md

# Get Batch Job Logs

## OpenAPI

````yaml get /v1/accounts/{account_id}/batchJobs/{batch_job_id}:getLogs
paths:
  path: /v1/accounts/{account_id}/batchJobs/{batch_job_id}:getLogs
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
        batch_job_id:
          schema:
            - type: string
              required: true
              description: The Batch Job Id
      query:
        ranks:
          schema:
            - type: array
              items:
                allOf:
                  - type: integer
                    format: int32
              required: false
              description: Ranks, for which to fetch logs.
          explode: true
        pageSize:
          schema:
            - type: integer
              required: false
              description: >-
                The maximum number of log entries to return. The maximum
                page_size is 10,000,

                values above 10,000 will be coerced to 10,000.

                If unspecified, the default is 100.
        pageToken:
          schema:
            - type: string
              required: false
              description: >-
                A page token, received from a previous GetBatchJobLogsRequest
                call. Provide this

                to retrieve the subsequent page. When paginating, all other
                parameters

                provided to GetBatchJobLogsRequest must match the call that
                provided the page

                token.
        startTime:
          schema:
            - type: string
              required: false
              description: |-
                Entries before this timestamp won't be returned.
                If not specified, up to page_size last records will be returned.
              format: date-time
        filter:
          schema:
            - type: string
              required: false
              description: |-
                Only entries matching this filter will be returned.
                Currently only basic substring match is performed.
        startFromHead:
          schema:
            - type: boolean
              required: false
              description: >-
                Pagination direction, time-wise reverse direction by default
                (false).
        readMask:
          schema:
            - type: string
              required: false
              description: >-
                The fields to be returned in the response. If empty or "*", all
                fields will be returned.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              entries:
                allOf:
                  - type: array
                    items:
                      type: object
                      $ref: '#/components/schemas/gatewayLogEntry'
              nextPageToken:
                allOf:
                  - type: string
                    description: >-
                      A token, which can be sent as `page_token` to retrieve the
                      next page.

                      If this field is omitted, there are no subsequent pages.
            refIdentifier: '#/components/schemas/gatewayGetBatchJobLogsResponse'
        examples:
          example:
            value:
              entries:
                - logTime: '2023-11-07T05:31:56Z'
                  rank: 123
                  message: <string>
              nextPageToken: <string>
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas:
    gatewayLogEntry:
      type: object
      properties:
        logTime:
          type: string
          format: date-time
          description: The timestamp of the log entry.
        rank:
          type: integer
          format: int32
          description: The rank which produced the log entry.
        message:
          type: string
          description: The log messsage.

````