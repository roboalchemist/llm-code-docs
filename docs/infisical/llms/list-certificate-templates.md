# Source: https://infisical.com/docs/api-reference/endpoints/ssh/ca/list-certificate-templates.md

# List templates

> Get list of certificate templates for the SSH CA

## OpenAPI

````yaml GET /api/v1/ssh/ca/{sshCaId}/certificate-templates
paths:
  path: /api/v1/ssh/ca/{sshCaId}/certificate-templates
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
        sshCaId:
          schema:
            - type: string
              required: true
              description: The ID of the SSH CA to get the certificate templates for.
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
              certificateTemplates:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          format: uuid
                        sshCaId:
                          type: string
                          format: uuid
                        status:
                          type: string
                        name:
                          type: string
                        ttl:
                          type: string
                        maxTTL:
                          type: string
                        allowedUsers:
                          type: array
                          items:
                            type: string
                        allowedHosts:
                          type: array
                          items:
                            type: string
                        allowCustomKeyIds:
                          type: boolean
                        allowUserCertificates:
                          type: boolean
                        allowHostCertificates:
                          type: boolean
                      required:
                        - id
                        - sshCaId
                        - status
                        - name
                        - ttl
                        - maxTTL
                        - allowedUsers
                        - allowedHosts
                        - allowCustomKeyIds
                        - allowUserCertificates
                        - allowHostCertificates
                      additionalProperties: false
            requiredProperties:
              - certificateTemplates
            additionalProperties: false
        examples:
          example:
            value:
              certificateTemplates:
                - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  sshCaId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  status: <string>
                  name: <string>
                  ttl: <string>
                  maxTTL: <string>
                  allowedUsers:
                    - <string>
                  allowedHosts:
                    - <string>
                  allowCustomKeyIds: true
                  allowUserCertificates: true
                  allowHostCertificates: true
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