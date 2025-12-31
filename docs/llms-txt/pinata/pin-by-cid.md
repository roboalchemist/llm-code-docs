# Source: https://docs.pinata.cloud/api-reference/endpoint/pin-by-cid.md

# Pin by CID

> `org:files:write`


## OpenAPI

````yaml post /files/public/pin_by_cid
paths:
  path: /files/public/pin_by_cid
  method: post
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              cid:
                allOf:
                  - type: string
                    description: CID of the file you want to pin
              name:
                allOf:
                  - type: string
                    description: Add a custom name for the file
              group_id:
                allOf:
                  - type: string
                    description: ID of the group you would like to upload
              keyvalues:
                allOf:
                  - type: object
                    description: Add additional key value metadata to files upon upload
                    additionalProperties:
                      type: string
              host_nodes:
                allOf:
                  - type: array
                    description: >-
                      An optional array of host node IDs, use `ipfs id` in Kubo
                      to get these
                    items:
                      type: string
            requiredProperties:
              - cid
        examples:
          example:
            value:
              cid: <string>
              name: <string>
              group_id: <string>
              keyvalues: {}
              host_nodes:
                - <string>
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
        examples:
          example:
            value:
              data:
                id: <string>
                name: <string>
                cid: <string>
                keyvalues: {}
                group_id: <string>
                status: <string>
                date_queued: <string>
                hose_nodes:
                  - <string>
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````