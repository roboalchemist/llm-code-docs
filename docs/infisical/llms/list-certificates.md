# Source: https://infisical.com/docs/api-reference/endpoints/pki/syncs/list-certificates.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificate-profiles/list-certificates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Certificates



## OpenAPI

````yaml GET /api/v1/cert-manager/certificate-profiles/{id}/certificates
openapi: 3.0.3
info:
  title: Infisical API
  description: List of all available APIs that can be consumed
  version: 0.0.1
servers:
  - url: https://us.infisical.com
    description: Production server (US)
  - url: https://eu.infisical.com
    description: Production server (EU)
  - url: http://localhost:8080
    description: Local server
security: []
paths:
  /api/v1/cert-manager/certificate-profiles/{id}/certificates:
    get:
      tags:
        - PKI Certificate Profiles
      operationId: listCertificateProfileCertificates
      parameters:
        - schema:
            type: number
            minimum: 0
            default: 0
          in: query
          name: offset
          required: false
        - schema:
            type: number
            minimum: 1
            maximum: 100
            default: 20
          in: query
          name: limit
          required: false
        - schema:
            type: string
            enum:
              - active
              - expired
              - revoked
          in: query
          name: status
          required: false
        - schema:
            type: string
          in: query
          name: search
          required: false
        - schema:
            type: string
            format: uuid
          in: path
          name: id
          required: true
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  certificates:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                        serialNumber:
                          type: string
                        cn:
                          type: string
                        status:
                          type: string
                        notBefore:
                          type: string
                          format: date-time
                        notAfter:
                          type: string
                          format: date-time
                        revokedAt:
                          type: string
                          format: date-time
                          nullable: true
                        createdAt:
                          type: string
                          format: date-time
                      required:
                        - id
                        - serialNumber
                        - cn
                        - status
                        - notBefore
                        - notAfter
                        - createdAt
                      additionalProperties: false
                required:
                  - certificates
                additionalProperties: false
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 400
                  message:
                    type: string
                  error:
                    type: string
                  details: {}
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '401':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 401
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '403':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 403
                  message:
                    type: string
                  details: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '404':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 404
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '422':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 422
                  message: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - error
                additionalProperties: false
        '500':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 500
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false

````