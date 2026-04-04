# Source: https://www.activepieces.com/docs/endpoints/user-invitations/upsert.md

# Source: https://www.activepieces.com/docs/endpoints/global-connections/upsert.md

# Source: https://www.activepieces.com/docs/endpoints/connections/upsert.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Upsert Connection

> Upsert an app connection based on the app name



## OpenAPI

````yaml POST /v1/app-connections
openapi: 3.0.3
info:
  title: Activepieces Documentation
  version: 0.0.0
servers:
  - url: https://cloud.activepieces.com/api
    description: Production Server
security: []
externalDocs:
  url: https://www.activepieces.com/docs
  description: Find more info here
paths:
  /v1/app-connections:
    post:
      tags:
        - app-connections
      description: Upsert an app connection based on the app name
      requestBody:
        content:
          application/json:
            schema:
              anyOf:
                - title: Secret Text
                  description: Secret Text
                  type: object
                  properties:
                    externalId:
                      type: string
                    displayName:
                      type: string
                    pieceName:
                      type: string
                    projectId:
                      type: string
                    metadata:
                      type: object
                      additionalProperties: {}
                    pieceVersion:
                      type: string
                    type:
                      type: string
                      enum:
                        - SECRET_TEXT
                    value:
                      type: object
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
                  required:
                    - externalId
                    - displayName
                    - pieceName
                    - projectId
                    - type
                    - value
                - title: OAuth2
                  description: OAuth2
                  type: object
                  properties:
                    externalId:
                      type: string
                    displayName:
                      type: string
                    pieceName:
                      type: string
                    projectId:
                      type: string
                    metadata:
                      type: object
                      additionalProperties: {}
                    pieceVersion:
                      type: string
                    type:
                      type: string
                      enum:
                        - OAUTH2
                    value:
                      type: object
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
                  required:
                    - externalId
                    - displayName
                    - pieceName
                    - projectId
                    - type
                    - value
                - title: Cloud OAuth2
                  description: Cloud OAuth2
                  type: object
                  properties:
                    externalId:
                      type: string
                    displayName:
                      type: string
                    pieceName:
                      type: string
                    projectId:
                      type: string
                    metadata:
                      type: object
                      additionalProperties: {}
                    pieceVersion:
                      type: string
                    type:
                      type: string
                      enum:
                        - CLOUD_OAUTH2
                    value:
                      type: object
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
                          additionalProperties: {}
                        type:
                          type: string
                          enum:
                            - CLOUD_OAUTH2
                      required:
                        - client_id
                        - code
                        - scope
                        - type
                  required:
                    - externalId
                    - displayName
                    - pieceName
                    - projectId
                    - type
                    - value
                - title: Platform OAuth2
                  description: Platform OAuth2
                  type: object
                  properties:
                    externalId:
                      type: string
                    displayName:
                      type: string
                    pieceName:
                      type: string
                    projectId:
                      type: string
                    metadata:
                      type: object
                      additionalProperties: {}
                    pieceVersion:
                      type: string
                    type:
                      type: string
                      enum:
                        - PLATFORM_OAUTH2
                    value:
                      type: object
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
                          additionalProperties: {}
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
                  required:
                    - externalId
                    - displayName
                    - pieceName
                    - projectId
                    - type
                    - value
                - title: Basic Auth
                  description: Basic Auth
                  type: object
                  properties:
                    externalId:
                      type: string
                    displayName:
                      type: string
                    pieceName:
                      type: string
                    projectId:
                      type: string
                    metadata:
                      type: object
                      additionalProperties: {}
                    pieceVersion:
                      type: string
                    type:
                      type: string
                      enum:
                        - BASIC_AUTH
                    value:
                      type: object
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
                  required:
                    - externalId
                    - displayName
                    - pieceName
                    - projectId
                    - type
                    - value
                - title: Custom Auth
                  description: Custom Auth
                  type: object
                  properties:
                    externalId:
                      type: string
                    displayName:
                      type: string
                    pieceName:
                      type: string
                    projectId:
                      type: string
                    metadata:
                      type: object
                      additionalProperties: {}
                    pieceVersion:
                      type: string
                    type:
                      type: string
                      enum:
                        - CUSTOM_AUTH
                    value:
                      type: object
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
                  required:
                    - externalId
                    - displayName
                    - pieceName
                    - projectId
                    - type
                    - value
                - title: No Auth
                  description: No Auth
                  type: object
                  properties:
                    externalId:
                      type: string
                    displayName:
                      type: string
                    pieceName:
                      type: string
                    projectId:
                      type: string
                    metadata:
                      type: object
                      additionalProperties: {}
                    pieceVersion:
                      type: string
                    type:
                      type: string
                      enum:
                        - NO_AUTH
                    value:
                      type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - NO_AUTH
                      required:
                        - type
                  required:
                    - externalId
                    - displayName
                    - pieceName
                    - projectId
                    - type
                    - value
      responses:
        '200':
          description: Default Response
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: http
      description: Use your api key generated from the admin console
      scheme: bearer

````