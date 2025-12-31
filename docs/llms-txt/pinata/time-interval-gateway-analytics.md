# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/time-interval-gateway-analytics.md

# Time Interval Gateway Analytics

> `org:analytics:read`


## OpenAPI

````yaml get /analytics/gateways/time_series
paths:
  path: /analytics/gateways/time_series
  method: get
  servers:
    - url: https://api.pinata.cloud/v3
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path: {}
      query:
        gateway_domain:
          schema:
            - type: string
              required: true
              description: Gateway domain to filter by
        start_date:
          schema:
            - type: string
              required: true
              description: Start date of aggregation in the format `YYYY-MM-DD`
        end_date:
          schema:
            - type: string
              required: true
              description: End date of aggregation in the format `YYYY-MM-DD`
        date_interval:
          schema:
            - type: enum<string>
              enum:
                - day
                - week
              required: true
              description: >-
                Date interval to view gateway usage by. Must be either `day` or
                `week.`
        sort_by:
          schema:
            - type: enum<string>
              enum:
                - requests
                - bandwidth
              description: Sort data by either `requests` or `bandwidth`
        cid:
          schema:
            - type: string
              description: Filter by CID
        file_name:
          schema:
            - type: string
              description: Filter by file name
        user_agent:
          schema:
            - type: string
              description: Filter by user agent
        country:
          schema:
            - type: string
              description: Filter by country
        region:
          schema:
            - type: string
              description: Filter by region
        referer:
          schema:
            - type: string
              description: Filter by referer
        http_status_code:
          schema:
            - type: enum<string>
              enum:
                - '200'
                - '206'
                - '301'
                - '302'
                - '304'
                - '307'
                - '308'
                - '404'
                - '499'
              description: Filter results by HTTP status code
        limit:
          schema:
            - type: integer
              description: Limit the number of results returned, default is 100
        sort_order:
          schema:
            - type: string
              description: Sort results by either `asc` or `desc`
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties: {}
        examples:
          example:
            value:
              data:
                total_requests: 1756
                total_bandwidth: 1034631262
                time_periods:
                  - period_start_time: '2024-08-15'
                    requests: 100
                    bandwidth: 75721161
                  - period_start_time: '2024-08-14'
                    requests: 109
                    bandwidth: 55430651
                  - period_start_time: '2024-08-13'
                    requests: 70
                    bandwidth: 32806252
                  - period_start_time: '2024-08-12'
                    requests: 71
                    bandwidth: 90781331
                  - period_start_time: '2024-08-11'
                    requests: 121
                    bandwidth: 60168755
                  - period_start_time: '2024-08-10'
                    requests: 187
                    bandwidth: 86036341
                  - period_start_time: '2024-08-09'
                    requests: 360
                    bandwidth: 262348634
                  - period_start_time: '2024-08-08'
                    requests: 86
                    bandwidth: 45399695
                  - period_start_time: '2024-08-07'
                    requests: 114
                    bandwidth: 27869980
                  - period_start_time: '2024-08-06'
                    requests: 146
                    bandwidth: 65227201
                  - period_start_time: '2024-08-05'
                    requests: 93
                    bandwidth: 101281128
                  - period_start_time: '2024-08-04'
                    requests: 62
                    bandwidth: 18297460
                  - period_start_time: '2024-08-03'
                    requests: 65
                    bandwidth: 21646988
                  - period_start_time: '2024-08-02'
                    requests: 64
                    bandwidth: 49484961
                  - period_start_time: '2024-08-01'
                    requests: 108
                    bandwidth: 42130724
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````