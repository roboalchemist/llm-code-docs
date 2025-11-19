# Source: https://infisical.com/docs/api-reference/endpoints/certificates/issue-certificate.md

# Issue Certificate

## OpenAPI

````yaml POST /api/v3/pki/certificates/issue-certificate
paths:
  path: /api/v3/pki/certificates/issue-certificate
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              profileId:
                allOf:
                  - type: string
                    format: uuid
              commonName:
                allOf:
                  - type: string
                    minLength: 1
                    maxLength: 100
              ttl:
                allOf:
                  - type: string
                    minLength: 1
              keyUsages:
                allOf:
                  - type: array
                    items:
                      type: string
                      enum:
                        - digital_signature
                        - key_encipherment
                        - non_repudiation
                        - data_encipherment
                        - key_agreement
                        - key_cert_sign
                        - crl_sign
                        - encipher_only
                        - decipher_only
              extendedKeyUsages:
                allOf:
                  - type: array
                    items:
                      type: string
                      enum:
                        - client_auth
                        - server_auth
                        - code_signing
                        - email_protection
                        - ocsp_signing
                        - time_stamping
              notBefore:
                allOf:
                  - type: string
              notAfter:
                allOf:
                  - type: string
              altNames:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - dns_name
                            - ip_address
                            - email
                            - uri
                        value:
                          type: string
                          minLength: 1
                      required:
                        - type
                        - value
                      additionalProperties: false
              signatureAlgorithm:
                allOf:
                  - type: string
                    enum:
                      - RSA-SHA256
                      - RSA-SHA384
                      - RSA-SHA512
                      - ECDSA-SHA256
                      - ECDSA-SHA384
                      - ECDSA-SHA512
              keyAlgorithm:
                allOf:
                  - type: string
                    enum:
                      - RSA_2048
                      - RSA_3072
                      - RSA_4096
                      - EC_prime256v1
                      - EC_secp384r1
                      - EC_secp521r1
            required: true
            requiredProperties:
              - profileId
              - ttl
              - signatureAlgorithm
              - keyAlgorithm
            additionalProperties: false
        examples:
          example:
            value:
              profileId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              commonName: <string>
              ttl: <string>
              keyUsages:
                - digital_signature
              extendedKeyUsages:
                - client_auth
              notBefore: <string>
              notAfter: <string>
              altNames:
                - type: dns_name
                  value: <string>
              signatureAlgorithm: RSA-SHA256
              keyAlgorithm: RSA_2048
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              certificate:
                allOf:
                  - type: string
              issuingCaCertificate:
                allOf:
                  - type: string
              certificateChain:
                allOf:
                  - type: string
              privateKey:
                allOf:
                  - type: string
              serialNumber:
                allOf:
                  - type: string
              certificateId:
                allOf:
                  - type: string
            requiredProperties:
              - certificate
              - issuingCaCertificate
              - certificateChain
              - serialNumber
              - certificateId
            additionalProperties: false
        examples:
          example:
            value:
              certificate: <string>
              issuingCaCertificate: <string>
              certificateChain: <string>
              privateKey: <string>
              serialNumber: <string>
              certificateId: <string>
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