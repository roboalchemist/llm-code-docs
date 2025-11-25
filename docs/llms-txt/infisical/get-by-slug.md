# Source: https://infisical.com/docs/api-reference/endpoints/secret-tags/get-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/project-roles/get-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/secret-tags/get-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-roles/get-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificate-profiles/get-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-tags/get-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/project-roles/get-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/secret-tags/get-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-roles/get-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/certificate-profiles/get-by-slug.md

# Get by Slug

## OpenAPI

````yaml GET /api/v1/pki/certificate-profiles/slug/{slug}
paths:
  path: /api/v1/pki/certificate-profiles/slug/{slug}
  method: get
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
        slug:
          schema:
            - type: string
              required: true
              minLength: 1
      query:
        projectId:
          schema:
            - type: string
              required: true
              minLength: 1
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              certificateProfile:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      projectId:
                        type: string
                      caId:
                        type: string
                        format: uuid
                      certificateTemplateId:
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
                    required:
                      - id
                      - projectId
                      - caId
                      - certificateTemplateId
                      - slug
                      - enrollmentType
                      - createdAt
                      - updatedAt
                    additionalProperties: false
            requiredProperties:
              - certificateProfile
            additionalProperties: false
        examples:
          example:
            value:
              certificateProfile:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                projectId: <string>
                caId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                certificateTemplateId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                slug: <string>
                description: <string>
                enrollmentType: <string>
                estConfigId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                apiConfigId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                createdAt: '2023-11-07T05:31:56Z'
                updatedAt: '2023-11-07T05:31:56Z'
                acmeConfigId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
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