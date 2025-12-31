# Source: https://docs.pinata.cloud/sdk/files/public/add-swap.md

# Source: https://docs.pinata.cloud/sdk/files/private/add-swap.md

# Source: https://docs.pinata.cloud/api-reference/endpoint/add-swap.md

# Source: https://docs.pinata.cloud/sdk/files/public/add-swap.md

# Source: https://docs.pinata.cloud/sdk/files/private/add-swap.md

# Source: https://docs.pinata.cloud/api-reference/endpoint/add-swap.md

# Source: https://docs.pinata.cloud/sdk/files/public/add-swap.md

# Source: https://docs.pinata.cloud/sdk/files/private/add-swap.md

# Source: https://docs.pinata.cloud/api-reference/endpoint/add-swap.md

# Add Swap

> `org:files:write`


## OpenAPI

````yaml put /files/{network}/swap/{cid}
paths:
  path: /files/{network}/swap/{cid}
  method: put
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
      path:
        network:
          schema:
            - type: enum<string>
              enum:
                - public
                - private
              required: true
              description: Target either the public or private IPFS network
        cid:
          schema:
            - type: string
              required: true
              description: The target original CID
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              swapCid:
                allOf:
                  - type: string
                    description: The CID you want to redirect to
            requiredProperties:
              - swapCid
            example:
              swapCid: bafkreig4zcnmqa23zff3ye7tuef6wrlq3aimffzm22axfeh3ddmawzlzz4
        examples:
          example:
            value:
              swapCid: bafkreig4zcnmqa23zff3ye7tuef6wrlq3aimffzm22axfeh3ddmawzlzz4
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
                      mapped_cid:
                        type: string
                        description: >-
                          The current CID that is being pointed to from the
                          original
                      created_at:
                        type: string
                        description: The date this CID was updated
        examples:
          example:
            value:
              data:
                mapped_cid: bafkreig4zcnmqa23zff3ye7tuef6wrlq3aimffzm22axfeh3ddmawzlzz4
                created_at: '2024-09-20T17:09:39.490275Z'
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````