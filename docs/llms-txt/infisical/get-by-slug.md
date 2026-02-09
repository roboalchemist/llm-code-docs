# Source: https://infisical.com/docs/api-reference/endpoints/secret-tags/get-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/project-roles/get-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/organization-roles/get-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/secret-tags/get-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-roles/get-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificate-profiles/get-by-slug.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get by Slug



## OpenAPI

````yaml GET /api/v1/cert-manager/certificate-profiles/slug/{slug}
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
  /api/v1/cert-manager/certificate-profiles/slug/{slug}:
    get:
      tags:
        - PKI Certificate Profiles
      operationId: getCertificateProfileBySlug
      parameters:
        - schema:
            type: string
            minLength: 1
          in: query
          name: projectId
          required: true
        - schema:
            type: string
            minLength: 1
          in: path
          name: slug
          required: true
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  certificateProfile:
                    type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      projectId:
                        type: string
                      caId:
                        type: string
                        format: uuid
                        nullable: true
                      certificatePolicyId:
                        type: string
                        format: uuid
                      slug:
                        type: string
                      description:
                        type: string
                        nullable: true
                      enrollmentType:
                        type: string
                      estConfigId:
                        type: string
                        format: uuid
                        nullable: true
                      apiConfigId:
                        type: string
                        format: uuid
                        nullable: true
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                      acmeConfigId:
                        type: string
                        format: uuid
                        nullable: true
                      issuerType:
                        type: string
                        default: ca
                      externalConfigs:
                        anyOf:
                          - type: object
                            properties:
                              template:
                                type: string
                                minLength: 1
                                description: Certificate template name for Azure AD CS
                            required:
                              - template
                            additionalProperties: false
                          - type: object
                            properties: {}
                            additionalProperties: false
                          - type: object
                            properties: {}
                            additionalProperties: false
                        nullable: true
                      defaultTtlDays:
                        type: number
                        nullable: true
                    required:
                      - id
                      - projectId
                      - certificatePolicyId
                      - slug
                      - enrollmentType
                      - createdAt
                      - updatedAt
                    additionalProperties: false
                required:
                  - certificateProfile
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