# Source: https://docs.pinata.cloud/api-reference/endpoint/query-pin-requests.md

# Query Pin Requests

> `org:files:read`


## OpenAPI

````yaml get /files/public/pin_by_cid
paths:
  path: /files/public/pin_by_cid
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
        order:
          schema:
            - type: enum<string>
              enum:
                - ASC
                - DESC
              description: Change the order of the results by date_queued
        status:
          schema:
            - type: enum<string>
              enum:
                - prechecking
                - backfilled
                - retreiving
                - expired
                - searching
                - over_free_limit
                - over_max_size
                - invalid_object
                - bad_host_node
              description: Filter pin by CID status
        cid:
          schema:
            - type: string
              description: Filter queue by CID
        limit:
          schema:
            - type: string
              description: Limit the number of results returned when querying the queue
        pageToken:
          schema:
            - type: string
              description: Paginate through pin by cid request results
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
                    properties:
                      jobs:
                        type: array
                        items:
                          type: object
                          properties:
                            id:
                              type: string
                            cid:
                              type: string
                            name:
                              type: string
                            status:
                              type: string
                            keyvalues:
                              type: object
                            host_nodes:
                              type: array
                              items:
                                type: string
                            group_id:
                              type: string
                            date_queued:
                              type: string
                      next_page_token:
                        type: string
        examples:
          example:
            value:
              data:
                jobs:
                  - id: <string>
                    cid: <string>
                    name: <string>
                    status: <string>
                    keyvalues: {}
                    host_nodes:
                      - <string>
                    group_id: <string>
                    date_queued: <string>
                next_page_token: <string>
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````