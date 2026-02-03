# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/time-interval-gateway-analytics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Time Interval Gateway Analytics

> `org:analytics:read`




## OpenAPI

````yaml get /analytics/gateways/time_series
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /analytics/gateways/time_series:
    get:
      tags:
        - Gateway Analytics
      summary: Time Interval Gateway Analytics
      description: |
        `org:analytics:read`
      parameters:
        - name: gateway_domain
          in: query
          schema:
            type: string
          description: Gateway domain to filter by
          required: true
          example: dweb.mypinata.cloud
        - name: start_date
          in: query
          schema:
            type: string
          description: Start date of aggregation in the format `YYYY-MM-DD`
          required: true
          example: '2024-08-01'
        - name: end_date
          in: query
          schema:
            type: string
          description: End date of aggregation in the format `YYYY-MM-DD`
          required: true
          example: '2024-08-15'
        - name: date_interval
          in: query
          schema:
            type: string
            enum:
              - day
              - week
          description: >-
            Date interval to view gateway usage by. Must be either `day` or
            `week.`
          required: true
          example: day
        - name: sort_by
          in: query
          schema:
            type: string
            enum:
              - requests
              - bandwidth
          description: Sort data by either `requests` or `bandwidth`
          example: requests
        - name: cid
          in: query
          schema:
            type: string
          description: Filter by CID
          example: QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng
        - name: file_name
          in: query
          schema:
            type: string
          description: Filter by file name
          example: 8.png
        - name: user_agent
          in: query
          schema:
            type: string
          description: Filter by user agent
          example: Go-http-client/2.0
        - name: country
          in: query
          schema:
            type: string
          description: Filter by country
          example: us
        - name: region
          in: query
          schema:
            type: string
          description: Filter by region
          example: us - TN
        - name: referer
          in: query
          schema:
            type: string
          description: Filter by referer
          example: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
        - name: http_status_code
          in: query
          schema:
            type: string
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
          example: '200'
        - name: limit
          in: query
          schema:
            type: integer
          description: Limit the number of results returned, default is 100
          example: '100'
        - name: sort_order
          in: query
          schema:
            type: string
          description: Sort results by either `asc` or `desc`
          example: desc
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Thu, 15 Aug 2024 22:56:37 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '1139'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: a789a76d7449671ba0393d54ba883855
            Strict-Transport-Security:
              schema:
                type: string
                example: max-age=15724800; includeSubDomains
          content:
            application/json:
              schema:
                type: object
              example:
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
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````