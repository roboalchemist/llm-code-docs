# Source: https://infisical.com/docs/api-reference/endpoints/certificate-authorities/sign-intermediate.md

# Sign intermediate certificate

> Create intermediate CA certificate from parent CA

## OpenAPI

````yaml POST /api/v1/pki/ca/{caId}/sign-intermediate
paths:
  path: /api/v1/pki/ca/{caId}/sign-intermediate
  method: post
  servers:
    - url: https://us.infisical.com
      description: Production server (US)
    - url: https://eu.infisical.com
      description: Production server (EU)
    - url: http://localhost:8080
      description: Local server
  request:
    security: []
    parameters:
      path:
        caId:
          schema:
            - type: string
              required: true
              description: The ID of the CA to sign the intermediate certificate with.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              csr:
                allOf:
                  - type: string
                    minLength: 1
                    description: The pem-encoded CSR to sign with the CA.
              notBefore:
                allOf:
                  - type: string
                    description: >-
                      The date and time when the intermediate CA becomes valid
                      in YYYY-MM-DDTHH:mm:ss.sssZ format.
              notAfter:
                allOf:
                  - type: string
                    description: >-
                      The date and time when the intermediate CA expires in
                      YYYY-MM-DDTHH:mm:ss.sssZ format.
              maxPathLength:
                allOf:
                  - type: number
                    minimum: -1
                    default: -1
                    description: >-
                      The maximum number of intermediate CAs that may follow
                      this CA in the certificate / CA chain. A maxPathLength of
                      -1 implies no path limit on the chain.
            required: true
            requiredProperties:
              - csr
              - notAfter
            additionalProperties: false
        examples:
          example:
            value:
              csr: <string>
              notBefore: <string>
              notAfter: <string>
              maxPathLength: -1
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              certificate:
                allOf:
                  - type: string
                    description: The signed intermediate certificate.
              certificateChain:
                allOf:
                  - type: string
                    description: The certificate chain of the intermediate certificate.
              issuingCaCertificate:
                allOf:
                  - type: string
                    description: The certificate of the issuing CA.
              serialNumber:
                allOf:
                  - type: string
                    description: The serial number of the intermediate certificate.
            requiredProperties:
              - certificate
              - certificateChain
              - issuingCaCertificate
              - serialNumber
            additionalProperties: false
        examples:
          example:
            value:
              certificate: <string>
              certificateChain: <string>
              issuingCaCertificate: <string>
              serialNumber: <string>
        description: Default Response
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 400
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 400
              message: <string>
              error: <string>
        description: Default Response
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 401
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 401
              message: <string>
              error: <string>
        description: Default Response
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 403
              message:
                allOf:
                  - type: string
              details:
                allOf:
                  - {}
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 403
              message: <string>
              details: <any>
              error: <string>
        description: Default Response
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 404
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 404
              message: <string>
              error: <string>
        description: Default Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 422
              message:
                allOf:
                  - {}
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 422
              message: <any>
              error: <string>
        description: Default Response
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 500
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 500
              message: <string>
              error: <string>
        description: Default Response
  deprecated: false
  type: path
components:
  schemas: {}

````