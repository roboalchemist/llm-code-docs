# Source: https://infisical.com/docs/api-reference/endpoints/projects/delete-project.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/projects/delete-project.md

# Delete Project

> Delete project

## OpenAPI

````yaml DELETE /api/v1/workspace/{workspaceId}
paths:
  path: /api/v1/workspace/{workspaceId}
  method: delete
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
      path:
        workspaceId:
          schema:
            - type: string
              required: true
              description: The ID of the project to delete.
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              workspace:
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
                    required:
                      - id
                      - name
                      - type
                      - slug
                      - orgId
                      - createdAt
                      - updatedAt
                    additionalProperties: false
            additionalProperties: false
        examples:
          example:
            value:
              workspace:
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