# Source: https://docs.pinata.cloud/api-reference/endpoint/remove-signature-from-cid.md

# Remove Signature from CID

> `org:files:write`


## OpenAPI

````yaml delete /files/{network}/signature/{cid}
paths:
  path: /files/{network}/signature/{cid}
  method: delete
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
              description: Target CID
      query: {}
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
              data: null
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````