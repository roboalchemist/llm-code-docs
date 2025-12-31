# Source: https://www.activepieces.com/docs/endpoints/user-invitations/upsert.md

# Source: https://www.activepieces.com/docs/endpoints/global-connections/upsert.md

# Source: https://www.activepieces.com/docs/endpoints/connections/upsert.md

# Source: https://www.activepieces.com/docs/endpoints/user-invitations/upsert.md

# Source: https://www.activepieces.com/docs/endpoints/global-connections/upsert.md

# Source: https://www.activepieces.com/docs/endpoints/connections/upsert.md

# Source: https://www.activepieces.com/docs/endpoints/user-invitations/upsert.md

# Source: https://www.activepieces.com/docs/endpoints/global-connections/upsert.md

# Source: https://www.activepieces.com/docs/endpoints/connections/upsert.md

# Upsert Connection

> Upsert an app connection based on the app name

## OpenAPI

````yaml POST /v1/app-connections
paths:
  path: /v1/app-connections
  method: post
  servers:
    - url: https://cloud.activepieces.com/api
      description: Production Server
  request:
    security:
      - title: apiKey
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Use your api key generated from the admin console
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
              externalId:
                allOf:
                  - type: string
              displayName:
                allOf:
                  - type: string
              pieceName:
                allOf:
                  - type: string
              projectId:
                allOf:
                  - type: string
              metadata:
                allOf:
                  - type: object
                    additionalProperties: {}
              type:
                allOf:
                  - type: string
                    enum:
                      - SECRET_TEXT
              value:
                allOf:
                  - type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - SECRET_TEXT
                      secret_text:
                        minLength: 1
                        type: string
                    required:
                      - type
                      - secret_text
            title: Secret Text
            description: Secret Text
            requiredProperties:
              - externalId
              - displayName
              - pieceName
              - projectId
              - type
              - value
          - type: object
            properties:
              externalId:
                allOf:
                  - type: string
              displayName:
                allOf:
                  - type: string
              pieceName:
                allOf:
                  - type: string
              projectId:
                allOf:
                  - type: string
              metadata:
                allOf:
                  - type: object
                    additionalProperties: {}
              type:
                allOf:
                  - type: string
                    enum:
                      - OAUTH2
              value:
                allOf:
                  - type: object
                    properties:
                      client_id:
                        minLength: 1
                        type: string
                      code:
                        minLength: 1
                        type: string
                      code_challenge:
                        type: string
                      scope:
                        type: string
                      authorization_method:
                        anyOf:
                          - type: string
                            enum:
                              - HEADER
                          - type: string
                            enum:
                              - BODY
                      client_secret:
                        minLength: 1
                        type: string
                      grant_type:
                        anyOf:
                          - type: string
                            enum:
                              - authorization_code
                          - type: string
                            enum:
                              - client_credentials
                      props:
                        type: object
                        additionalProperties: {}
                      redirect_url:
                        minLength: 1
                        type: string
                      type:
                        type: string
                        enum:
                          - OAUTH2
                    required:
                      - client_id
                      - code
                      - scope
                      - client_secret
                      - redirect_url
                      - type
            title: OAuth2
            description: OAuth2
            requiredProperties:
              - externalId
              - displayName
              - pieceName
              - projectId
              - type
              - value
          - type: object
            properties:
              externalId:
                allOf:
                  - type: string
              displayName:
                allOf:
                  - type: string
              pieceName:
                allOf:
                  - type: string
              projectId:
                allOf:
                  - type: string
              metadata:
                allOf:
                  - type: object
                    additionalProperties: {}
              type:
                allOf:
                  - type: string
                    enum:
                      - CLOUD_OAUTH2
              value:
                allOf:
                  - type: object
                    properties:
                      client_id:
                        minLength: 1
                        type: string
                      code:
                        minLength: 1
                        type: string
                      code_challenge:
                        type: string
                      scope:
                        type: string
                      authorization_method:
                        anyOf:
                          - type: string
                            enum:
                              - HEADER
                          - type: string
                            enum:
                              - BODY
                      props:
                        type: object
                        additionalProperties:
                          type: string
                      type:
                        type: string
                        enum:
                          - CLOUD_OAUTH2
                    required:
                      - client_id
                      - code
                      - scope
                      - type
            title: Cloud OAuth2
            description: Cloud OAuth2
            requiredProperties:
              - externalId
              - displayName
              - pieceName
              - projectId
              - type
              - value
          - type: object
            properties:
              externalId:
                allOf:
                  - type: string
              displayName:
                allOf:
                  - type: string
              pieceName:
                allOf:
                  - type: string
              projectId:
                allOf:
                  - type: string
              metadata:
                allOf:
                  - type: object
                    additionalProperties: {}
              type:
                allOf:
                  - type: string
                    enum:
                      - PLATFORM_OAUTH2
              value:
                allOf:
                  - type: object
                    properties:
                      client_id:
                        minLength: 1
                        type: string
                      code:
                        minLength: 1
                        type: string
                      code_challenge:
                        type: string
                      scope:
                        type: string
                      authorization_method:
                        anyOf:
                          - type: string
                            enum:
                              - HEADER
                          - type: string
                            enum:
                              - BODY
                      props:
                        type: object
                        additionalProperties:
                          type: string
                      type:
                        type: string
                        enum:
                          - PLATFORM_OAUTH2
                      redirect_url:
                        minLength: 1
                        type: string
                    required:
                      - client_id
                      - code
                      - scope
                      - type
                      - redirect_url
            title: Platform OAuth2
            description: Platform OAuth2
            requiredProperties:
              - externalId
              - displayName
              - pieceName
              - projectId
              - type
              - value
          - type: object
            properties:
              externalId:
                allOf:
                  - type: string
              displayName:
                allOf:
                  - type: string
              pieceName:
                allOf:
                  - type: string
              projectId:
                allOf:
                  - type: string
              metadata:
                allOf:
                  - type: object
                    additionalProperties: {}
              type:
                allOf:
                  - type: string
                    enum:
                      - BASIC_AUTH
              value:
                allOf:
                  - type: object
                    properties:
                      username:
                        minLength: 1
                        type: string
                      password:
                        minLength: 1
                        type: string
                      type:
                        type: string
                        enum:
                          - BASIC_AUTH
                    required:
                      - username
                      - password
                      - type
            title: Basic Auth
            description: Basic Auth
            requiredProperties:
              - externalId
              - displayName
              - pieceName
              - projectId
              - type
              - value
          - type: object
            properties:
              externalId:
                allOf:
                  - type: string
              displayName:
                allOf:
                  - type: string
              pieceName:
                allOf:
                  - type: string
              projectId:
                allOf:
                  - type: string
              metadata:
                allOf:
                  - type: object
                    additionalProperties: {}
              type:
                allOf:
                  - type: string
                    enum:
                      - CUSTOM_AUTH
              value:
                allOf:
                  - type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - CUSTOM_AUTH
                      props:
                        type: object
                        additionalProperties: {}
                    required:
                      - type
                      - props
            title: Custom Auth
            description: Custom Auth
            requiredProperties:
              - externalId
              - displayName
              - pieceName
              - projectId
              - type
              - value
          - type: object
            properties:
              externalId:
                allOf:
                  - type: string
              displayName:
                allOf:
                  - type: string
              pieceName:
                allOf:
                  - type: string
              projectId:
                allOf:
                  - type: string
              metadata:
                allOf:
                  - type: object
                    additionalProperties: {}
              type:
                allOf:
                  - type: string
                    enum:
                      - NO_AUTH
              value:
                allOf:
                  - type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - NO_AUTH
                    required:
                      - type
            title: No Auth
            description: No Auth
            requiredProperties:
              - externalId
              - displayName
              - pieceName
              - projectId
              - type
              - value
        examples:
          example:
            value:
              externalId: <string>
              displayName: <string>
              pieceName: <string>
              projectId: <string>
              metadata: {}
              type: SECRET_TEXT
              value:
                type: SECRET_TEXT
                secret_text: <string>
  response:
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Default Response
        examples: {}
        description: Default Response
  deprecated: false
  type: path
components:
  schemas: {}

````