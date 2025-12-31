# Source: https://infisical.com/docs/api-reference/endpoints/certificates/create-certificate.md

# Issue Certificate



## OpenAPI

````yaml POST /api/v1/cert-manager/certificates
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
  /api/v1/cert-manager/certificates:
    post:
      tags:
        - PKI Certificates
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                profileId:
                  type: string
                  format: uuid
                csr:
                  type: string
                  minLength: 1
                  maxLength: 4096
                attributes:
                  type: object
                  properties:
                    commonName:
                      type: string
                      minLength: 1
                      maxLength: 100
                    keyUsages:
                      type: array
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
                      type: array
                      items:
                        type: string
                        enum:
                          - client_auth
                          - server_auth
                          - code_signing
                          - email_protection
                          - ocsp_signing
                          - time_stamping
                    altNames:
                      type: array
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
                      type: string
                      enum:
                        - RSA-SHA256
                        - RSA-SHA384
                        - RSA-SHA512
                        - ECDSA-SHA256
                        - ECDSA-SHA384
                        - ECDSA-SHA512
                    keyAlgorithm:
                      type: string
                      enum:
                        - RSA_2048
                        - RSA_3072
                        - RSA_4096
                        - EC_prime256v1
                        - EC_secp384r1
                        - EC_secp521r1
                    ttl:
                      type: string
                      minLength: 1
                    notBefore:
                      type: string
                    notAfter:
                      type: string
                  required:
                    - ttl
                  additionalProperties: false
                removeRootsFromChain:
                  anyOf:
                    - type: boolean
                    - type: string
                  default: false
              required:
                - profileId
              additionalProperties: false
        required: true
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  certificate:
                    type: object
                    properties:
                      certificate:
                        type: string
                      issuingCaCertificate:
                        type: string
                      certificateChain:
                        type: string
                      privateKey:
                        type: string
                      serialNumber:
                        type: string
                      certificateId:
                        type: string
                    required:
                      - certificate
                      - issuingCaCertificate
                      - certificateChain
                      - serialNumber
                      - certificateId
                    additionalProperties: false
                    nullable: true
                  certificateRequestId:
                    type: string
                required:
                  - certificate
                  - certificateRequestId
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://infisical.com/docs/llms.txt