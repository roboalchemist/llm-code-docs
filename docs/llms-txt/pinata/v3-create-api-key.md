# Source: https://docs.pinata.cloud/api-reference/endpoint/v3-create-api-key.md

# Create API Key

> `org:write`


## OpenAPI

````yaml post /api_keys
paths:
  path: /api_keys
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
              keyName:
                allOf:
                  - type: string
                    description: Name of the API key
              permissions:
                allOf:
                  - type: object
                    properties:
                      admin:
                        type: boolean
                        description: Provides full access to permissions
                      resources:
                        type: array
                        description: >-
                          Provide an array of scopes in the form
                          `org:<RESOURCE>:<PERMISSION>`. Resources include
                          `files`, `groups`, `gateways`, and `analytics`.
                          Permissions are either `read` or `write` (`write`
                          includes `read` permissions)
                        items:
                          type: string
                      endpoints:
                        type: object
                        description: >
                          ### Legacy endpoints

                          These properties are to be used with [legacy
                          endpoints](/api-reference/endpoint/ipfs/pin-file-to-ipfs),
                          any V3 endpoints should use `resources` instead
                        properties:
                          data:
                            type: object
                            properties:
                              pinList:
                                type: boolean
                              userPinnedDataTotal:
                                type: boolean
                          pinning:
                            type: object
                            properties:
                              hashMetadata:
                                type: boolean
                              hashPinPolicy:
                                type: boolean
                              pinByHash:
                                type: boolean
                              pinFileToIPFS:
                                type: boolean
                              pinJSONToIPFS:
                                type: boolean
                              pinJobs:
                                type: boolean
                              unpin:
                                type: boolean
                              userPinPolicy:
                                type: boolean
            requiredProperties:
              - keyName
            example:
              keyname: A test
              permissions:
                admin: true
              maxUses: 2
        examples:
          example:
            value:
              keyname: A test
              permissions:
                admin: true
              maxUses: 2
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties: {}
        examples:
          example:
            value:
              JWT: JWT
              pinata_api_key: key
              pinata_api_secret: secret
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````