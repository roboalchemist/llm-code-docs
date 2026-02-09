# Source: https://infisical.com/docs/api-reference/endpoints/projects/create-project.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/projects/create-project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Project

> Create a new project



## OpenAPI

````yaml POST /api/v2/workspace
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
  /api/v2/workspace:
    post:
      tags:
        - Projects
      description: Create a new project
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                projectName:
                  type: string
                  description: The name of the project to create.
                projectDescription:
                  type: string
                  description: An optional description label for the project.
                slug:
                  type: string
                  minLength: 5
                  maxLength: 36
                  description: An optional slug for the project.
                kmsKeyId:
                  type: string
                template:
                  type: string
                  minLength: 1
                  maxLength: 64
                  default: default
                  description: >-
                    The name of the project template, if specified, to apply to
                    this project.
                type:
                  type: string
                  enum:
                    - secret-manager
                    - cert-manager
                    - kms
                    - ssh
                    - secret-scanning
                    - pam
                    - ai
                  default: secret-manager
                shouldCreateDefaultEnvs:
                  type: boolean
                  default: true
                hasDeleteProtection:
                  type: boolean
                  default: false
              required:
                - projectName
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
                  project:
                    type: object
                    properties:
                      id:
                        type: string
                      name:
                        type: string
                      description:
                        type: string
                        nullable: true
                      type:
                        type: string
                      defaultProduct:
                        type: string
                        nullable: true
                      slug:
                        type: string
                      autoCapitalization:
                        type: boolean
                        default: false
                        nullable: true
                      orgId:
                        type: string
                        format: uuid
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                      version:
                        type: number
                        default: 1
                      upgradeStatus:
                        type: string
                        nullable: true
                      pitVersionLimit:
                        type: number
                        default: 10
                      kmsCertificateKeyId:
                        type: string
                        format: uuid
                        nullable: true
                      auditLogsRetentionDays:
                        type: number
                        nullable: true
                      hasDeleteProtection:
                        type: boolean
                        default: false
                        nullable: true
                      secretSharing:
                        type: boolean
                        default: true
                      showSnapshotsLegacy:
                        type: boolean
                        default: false
                      secretDetectionIgnoreValues:
                        type: array
                        items:
                          type: string
                        nullable: true
                      enforceEncryptedSecretManagerSecretMetadata:
                        type: boolean
                        nullable: true
                      _id:
                        type: string
                      environments:
                        type: array
                        items:
                          type: object
                          properties:
                            name:
                              type: string
                            slug:
                              type: string
                            id:
                              type: string
                          required:
                            - name
                            - slug
                            - id
                          additionalProperties: false
                      kmsSecretManagerKeyId:
                        type: string
                        nullable: true
                    required:
                      - id
                      - name
                      - type
                      - slug
                      - orgId
                      - createdAt
                      - updatedAt
                      - _id
                      - environments
                    additionalProperties: false
                required:
                  - project
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
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: An access token in Infisical

````