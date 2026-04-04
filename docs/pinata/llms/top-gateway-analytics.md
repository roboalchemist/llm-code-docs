# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/top-gateway-analytics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Top Gateway Analytics

> `org:analytics:read`




## OpenAPI

````yaml get /analytics/gateways/top
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /analytics/gateways/top:
    get:
      tags:
        - Gateway Analytics
      summary: Top Gateway Analytics
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
          example: '2024-07-01'
        - name: end_date
          in: query
          schema:
            type: string
          description: End date of aggregation in the format `YYYY-MM-DD`
          required: true
          example: '2024-08-15'
        - name: by
          in: query
          schema:
            type: string
            enum:
              - cid
              - country
              - region
              - user_agent
              - referrer
              - file_name
          description: >-
            Attribute to aggregaate results by, must be `cid`, `country`,
            `region`, `user_agent`, `referer`, or `file_name`.
          required: true
          example: cid
        - name: sort_by
          in: query
          schema:
            type: string
            enum:
              - requests
              - bandwidth
          description: Sort data by either `requests` or `bandwidth`
          required: true
          example: requests
        - name: cid
          in: query
          schema:
            type: string
          description: Filter by CID
          example: bafybeiegx7bgm5gpiutivw6e234gflheqjmp7hxlxfkihd3zdfx6omocia
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
            enum:
              - asc
              - desc
          description: Sort results by either `asc` or `desc`
          example: desc
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Thu, 15 Aug 2024 19:37:33 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '121'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: 90aee3f47b78a6ce735c304de3d691f5
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
                  - value: >-
                      bafybeiegx7bgm5gpiutivw6e234gflheqjmp7hxlxfkihd3zdfx6omocia
                    requests: 1341
                    bandwidth: 287310699
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````