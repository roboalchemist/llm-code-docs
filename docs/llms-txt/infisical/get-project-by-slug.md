# Source: https://infisical.com/docs/api-reference/endpoints/projects/get-project-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/projects/get-project-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/projects/get-project-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/projects/get-project-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/projects/get-project-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/projects/get-project-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/projects/get-project-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/projects/get-project-by-slug.md

# Get Project By Slug

> Get project details by slug

## OpenAPI

````yaml GET /api/v2/workspace/{slug}
paths:
  path: /api/v2/workspace/{slug}
  method: get
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
        slug:
          schema:
            - type: string
              required: true
              description: The slug of the project to get.
              maxLength: 64
              minLength: 1
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
              id:
                allOf:
                  - type: string
              name:
                allOf:
                  - type: string
              description:
                allOf:
                  - type: string
                    nullable: true
              type:
                allOf:
                  - type: string
              defaultProduct:
                allOf:
                  - type: string
                    nullable: true
              slug:
                allOf:
                  - type: string
              autoCapitalization:
                allOf:
                  - type: boolean
                    default: false
                    nullable: true
              orgId:
                allOf:
                  - type: string
                    format: uuid
              createdAt:
                allOf:
                  - type: string
                    format: date-time
              updatedAt:
                allOf:
                  - type: string
                    format: date-time
              version:
                allOf:
                  - type: number
                    default: 1
              upgradeStatus:
                allOf:
                  - type: string
                    nullable: true
              pitVersionLimit:
                allOf:
                  - type: number
                    default: 10
              kmsCertificateKeyId:
                allOf:
                  - type: string
                    format: uuid
                    nullable: true
              auditLogsRetentionDays:
                allOf:
                  - type: number
                    nullable: true
              hasDeleteProtection:
                allOf:
                  - type: boolean
                    default: false
                    nullable: true
              secretSharing:
                allOf:
                  - type: boolean
                    default: true
              showSnapshotsLegacy:
                allOf:
                  - type: boolean
                    default: false
              secretDetectionIgnoreValues:
                allOf:
                  - type: array
                    items:
                      type: string
                    nullable: true
              _id:
                allOf:
                  - type: string
              environments:
                allOf:
                  - type: array
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
                allOf:
                  - type: string
                    nullable: true
            requiredProperties:
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
        examples:
          example:
            value:
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