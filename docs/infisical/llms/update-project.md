# Source: https://infisical.com/docs/api-reference/endpoints/projects/update-project.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/projects/update-project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Project

> Update project



## OpenAPI

````yaml PATCH /api/v1/workspace/{workspaceId}
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
  /api/v1/workspace/{workspaceId}:
    patch:
      tags:
        - Projects
      description: Update project
      parameters:
        - schema:
            type: string
          in: path
          name: workspaceId
          required: true
          description: The ID of the project to update.
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  maxLength: 64
                  description: The new name of the project.
                description:
                  type: string
                  maxLength: 256
                  description: An optional description label for the project.
                autoCapitalization:
                  type: boolean
                  description: Disable or enable auto-capitalization for the project.
                hasDeleteProtection:
                  type: boolean
                  description: Enable or disable delete protection for the project.
                slug:
                  type: string
                  maxLength: 64
                  description: >-
                    An optional slug for the project. (must be unique within the
                    organization)
                secretSharing:
                  type: boolean
                  description: Enable or disable secret sharing for the project.
                showSnapshotsLegacy:
                  type: boolean
                  description: Enable or disable legacy snapshots for the project.
                defaultProduct:
                  type: string
                  enum:
                    - secret-manager
                    - cert-manager
                    - kms
                    - ssh
                    - secret-scanning
                    - pam
                    - ai
                  description: The default product in which the project will open
                secretDetectionIgnoreValues:
                  type: array
                  items:
                    type: string
                  description: The list of secret values to ignore for secret detection.
              additionalProperties: false
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  workspace:
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
                    required:
                      - id
                      - name
                      - type
                      - slug
                      - orgId
                      - createdAt
                      - updatedAt
                    additionalProperties: false
                required:
                  - workspace
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