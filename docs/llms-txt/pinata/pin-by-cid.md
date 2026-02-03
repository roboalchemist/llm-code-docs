# Source: https://docs.pinata.cloud/api-reference/endpoint/pin-by-cid.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Pin by CID

> `org:files:write`




## OpenAPI

````yaml post /files/public/pin_by_cid
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
    post:
      summary: Pin by CID
      description: |
        `org:files:write`
      operationId: pinByCid
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - cid
              properties:
                cid:
                  type: string
                  description: CID of the file you want to pin
                name:
                  type: string
                  description: Add a custom name for the file
                group_id:
                  type: string
                  description: ID of the group you would like to upload
                keyvalues:
                  type: object
                  description: Add additional key value metadata to files upon upload
                  additionalProperties:
                    type: string
                host_nodes:
                  type: array
                  description: >-
                    An optional array of host node IDs, use `ipfs id` in Kubo to
                    get these
                  items:
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
                      id:
                        type: string
                      name:
                        type: string
                      cid:
                        type: string
                      keyvalues:
                        type: object
                      group_id:
                        type: string
                      status:
                        type: string
                      date_queued:
                        type: string
                      hose_nodes:
                        type: array
                        items:
                          type: string
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````