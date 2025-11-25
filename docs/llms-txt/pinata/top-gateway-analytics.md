# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/top-gateway-analytics.md

# Top Gateway Analytics

> `org:analytics:read`


## OpenAPI

````yaml get /analytics/gateways/top
paths:
  path: /analytics/gateways/top
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
        by:
          schema:
            - type: enum<string>
              enum:
                - cid
                - country
                - region
                - user_agent
                - referrer
                - file_name
              required: true
              description: >-
                Attribute to aggregaate results by, must be `cid`, `country`,
                `region`, `user_agent`, `referer`, or `file_name`.
        sort_by:
          schema:
            - type: enum<string>
              enum:
                - requests
                - bandwidth
              required: true
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
            - type: enum<string>
              enum:
                - asc
                - desc
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
                - value: bafybeiegx7bgm5gpiutivw6e234gflheqjmp7hxlxfkihd3zdfx6omocia
                  requests: 1341
                  bandwidth: 287310699
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````