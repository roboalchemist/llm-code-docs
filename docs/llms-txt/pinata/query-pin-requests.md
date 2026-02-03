# Source: https://docs.pinata.cloud/api-reference/endpoint/query-pin-requests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Query Pin Requests

> `org:files:read`




## OpenAPI

````yaml get /files/public/pin_by_cid
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /files/public/pin_by_cid:
    get:
      summary: Query Pin Requests
      description: |
        `org:files:read`
      operationId: queryPinRequests
      parameters:
        - name: order
          description: Change the order of the results by date_queued
          in: query
          schema:
            type: string
            enum:
              - ASC
              - DESC
          example: ASC
        - name: status
          description: Filter pin by CID status
          in: query
          schema:
            type: string
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
        - name: cid
          description: Filter queue by CID
          in: query
          schema:
            type: string
          example: QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng
        - name: limit
          description: Limit the number of results returned when querying the queue
          in: query
          schema:
            type: string
          example: 10
        - name: pageToken
          description: Paginate through pin by cid request results
          in: query
          schema:
            type: string
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Tue, 27 Aug 2024 15:04:00 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '303'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: 5cda7fd04bb31bc8c6bd461089fcfa1c
            Strict-Transport-Security:
              schema:
                type: string
                example: max-age=15724800; includeSubDomains
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
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
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````