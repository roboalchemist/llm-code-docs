# Source: https://infisical.com/docs/api-reference/endpoints/certificates/certificate-request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Certificate Request



## OpenAPI

````yaml GET /api/v1/cert-manager/certificates/certificate-requests/{requestId}
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
  /api/v1/cert-manager/certificates/certificate-requests/{requestId}:
    get:
      tags:
        - PKI Certificates
      operationId: getCertificateRequest
      parameters:
        - schema:
            type: string
            format: uuid
          in: path
          name: requestId
          required: true
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    enum:
                      - pending_approval
                      - pending
                      - issued
                      - failed
                      - rejected
                  certificate:
                    type: string
                    nullable: true
                  certificateId:
                    type: string
                    nullable: true
                  privateKey:
                    type: string
                    nullable: true
                  serialNumber:
                    type: string
                    nullable: true
                  errorMessage:
                    type: string
                    nullable: true
                  commonName:
                    type: string
                    nullable: true
                  organization:
                    type: string
                    nullable: true
                  organizationalUnit:
                    type: string
                    nullable: true
                  country:
                    type: string
                    nullable: true
                  state:
                    type: string
                    nullable: true
                  locality:
                    type: string
                    nullable: true
                  basicConstraints:
                    type: object
                    properties:
                      isCA:
                        type: boolean
                      pathLength:
                        type: number
                    required:
                      - isCA
                    additionalProperties: false
                    nullable: true
                  createdAt:
                    type: string
                    format: date-time
                  updatedAt:
                    type: string
                    format: date-time
                required:
                  - status
                  - certificate
                  - certificateId
                  - privateKey
                  - serialNumber
                  - errorMessage
                  - createdAt
                  - updatedAt
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