# Source: https://docs.pinata.cloud/api-reference/endpoint/v3-create-api-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Create API Key

> `org:write`




## OpenAPI

````yaml post /api_keys
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /api_keys:
    post:
      tags:
        - default
      summary: Create API Key
      description: |
        `org:write`
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                keyName:
                  type: string
                  description: Name of the API key
                permissions:
                  type: object
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
              required:
                - keyName
              example:
                keyname: A test
                permissions:
                  admin: true
                maxUses: 2
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Tue, 18 Jun 2024 18:52:56 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '818'
            Connection:
              schema:
                type: string
                example: keep-alive
            Strict-Transport-Security:
              schema:
                type: string
                example: max-age=15724800; includeSubDomains
          content:
            application/json:
              schema:
                type: object
              example:
                JWT: JWT
                pinata_api_key: key
                pinata_api_secret: secret
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````