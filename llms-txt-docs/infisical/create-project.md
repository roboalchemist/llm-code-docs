# Source: https://infisical.com/docs/api-reference/endpoints/projects/create-project.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/projects/create-project.md

# Create Project

> Create a new project

## OpenAPI

````yaml POST /api/v2/workspace
paths:
  path: /api/v2/workspace
  method: post
  servers:
    - url: https://us.infisical.com
      description: Production server (US)
    - url: https://eu.infisical.com
      description: Production server (EU)
    - url: http://localhost:8080
      description: Local server
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: An access token in Infisical
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
              projectName:
                allOf:
                  - type: string
                    description: The name of the project to create.
              projectDescription:
                allOf:
                  - type: string
                    description: An optional description label for the project.
              slug:
                allOf:
                  - type: string
                    minLength: 5
                    maxLength: 36
                    description: An optional slug for the project.
              kmsKeyId:
                allOf:
                  - type: string
              template:
                allOf:
                  - type: string
                    minLength: 1
                    maxLength: 64
                    default: default
                    description: >-
                      The name of the project template, if specified, to apply
                      to this project.
              type:
                allOf:
                  - type: string
                    enum:
                      - secret-manager
                      - cert-manager
                      - kms
                      - ssh
                      - secret-scanning
                      - pam
                    default: secret-manager
              shouldCreateDefaultEnvs:
                allOf:
                  - type: boolean
                    default: true
              hasDeleteProtection:
                allOf:
                  - type: boolean
                    default: false
            required: true
            requiredProperties:
              - projectName
            additionalProperties: false
        examples:
          example:
            value:
              projectName: <string>
              projectDescription: <string>
              slug: <string>
              kmsKeyId: <string>
              template: default
              type: secret-manager
              shouldCreateDefaultEnvs: true
              hasDeleteProtection: false
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              project:
                allOf:
                  - type: object
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
            requiredProperties:
              - project
            additionalProperties: false
        examples:
          example:
            value:
              project:
                id: <string>
                name: <string>
                description: <string>
                type: <string>
                defaultProduct: <string>
                slug: <string>
                autoCapitalization: false
                orgId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                createdAt: '2023-11-07T05:31:56Z'
                updatedAt: '2023-11-07T05:31:56Z'
                version: 1
                upgradeStatus: <string>
                pitVersionLimit: 10
                kmsCertificateKeyId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                auditLogsRetentionDays: 123
                hasDeleteProtection: false
                secretSharing: true
                showSnapshotsLegacy: false
                secretDetectionIgnoreValues:
                  - <string>
                _id: <string>
                environments:
                  - name: <string>
                    slug: <string>
                    id: <string>
                kmsSecretManagerKeyId: <string>
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