# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/list-gateways.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# List Gateways

> `org:gateways:read`




## OpenAPI

````yaml get /gateways
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /gateways:
    get:
      tags:
        - default
      summary: List Gateways
      description: |
        `org:gateways:read`
      parameters:
        - name: pageSize
          in: query
          schema:
            type: integer
          description: Limits the number of results
          example: '1'
        - name: page
          in: query
          schema:
            type: integer
          description: Paginates through results by offsetting the results
          example: '2'
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Fri, 12 Jul 2024 15:10:48 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '919'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: e321b967c4f4ba6a43947bc195b12bbc
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
                  count: 5
                  rows:
                    - id: 01dae16b-699c-472a-a61e-975a7b9777bd
                      created_at: '2023-01-24T19:51:17.493Z'
                      domain: restricted-example
                      restrict: false
                      custom_domains:
                        - domain: ipfs.pinata.cloud
                          domain_validation_status: pending
                          custom_domain_id: 87980e39-fe71-4dba-9b05-3dfc66593539
                          ssl_validation_status: initializing
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````