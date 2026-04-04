# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/windows-local-account/reconcile.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/unix-linux-local-account/reconcile.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Reconcile

> Reconcile Unix/Linux Local Account rotation credentials. This operation uses the SSH app connection credentials to reset the password when credentials are out of sync.



## OpenAPI

````yaml POST /api/v2/secret-rotations/unix-linux-local-account/{rotationId}/reconcile
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
  /api/v2/secret-rotations/unix-linux-local-account/{rotationId}/reconcile:
    post:
      tags:
        - Secret Rotations
      description: >-
        Reconcile Unix/Linux Local Account rotation credentials. This operation
        uses the SSH app connection credentials to reset the password when
        credentials are out of sync.
      parameters:
        - schema:
            type: string
            format: uuid
          in: path
          name: rotationId
          required: true
          description: The ID of the SSH Password Rotation to reconcile credentials for.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  reconciled:
                    type: boolean
                  secretRotation:
                    type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      name:
                        type: string
                      description:
                        type: string
                        nullable: true
                      isAutoRotationEnabled:
                        type: boolean
                        default: true
                      activeIndex:
                        type: number
                        default: 0
                      folderId:
                        type: string
                        format: uuid
                      connectionId:
                        type: string
                        format: uuid
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                      rotationInterval:
                        type: number
                      rotationStatus:
                        type: string
                      lastRotationAttemptedAt:
                        type: string
                        format: date-time
                      lastRotatedAt:
                        type: string
                        format: date-time
                      lastRotationJobId:
                        type: string
                        nullable: true
                      nextRotationAt:
                        type: string
                        format: date-time
                        nullable: true
                      isLastRotationManual:
                        type: boolean
                        default: true
                      connection:
                        type: object
                        properties:
                          app:
                            type: string
                            enum:
                              - ssh
                          name:
                            type: string
                          id:
                            type: string
                            format: uuid
                        required:
                          - app
                          - name
                          - id
                        additionalProperties: false
                      environment:
                        type: object
                        properties:
                          slug:
                            type: string
                          name:
                            type: string
                          id:
                            type: string
                            format: uuid
                        required:
                          - slug
                          - name
                          - id
                        additionalProperties: false
                      projectId:
                        type: string
                      folder:
                        type: object
                        properties:
                          id:
                            type: string
                          path:
                            type: string
                        required:
                          - id
                          - path
                        additionalProperties: false
                      rotateAtUtc:
                        type: object
                        properties:
                          hours:
                            type: number
                            minimum: 0
                            maximum: 23
                          minutes:
                            type: number
                            minimum: 0
                            maximum: 59
                        required:
                          - hours
                          - minutes
                        additionalProperties: false
                      lastRotationMessage:
                        type: string
                        nullable: true
                      type:
                        type: string
                        enum:
                          - unix-linux-local-account
                      parameters:
                        type: object
                        properties:
                          username:
                            type: string
                            minLength: 1
                            description: >-
                              The username of the Unix/Linux user account to
                              rotate the password for.
                          passwordRequirements:
                            type: object
                            properties:
                              length:
                                type: number
                                minimum: 1
                                maximum: 250
                                description: The length of the password to generate.
                              required:
                                type: object
                                properties:
                                  digits:
                                    type: number
                                    minimum: 0
                                    description: >-
                                      The amount of digits to require in the
                                      generated password.
                                  lowercase:
                                    type: number
                                    minimum: 0
                                    description: >-
                                      The amount of lowercase characters to
                                      require in the generated password.
                                  uppercase:
                                    type: number
                                    minimum: 0
                                    description: >-
                                      The amount of uppercase characters to
                                      require in the generated password.
                                  symbols:
                                    type: number
                                    minimum: 0
                                    description: >-
                                      The amount of symbols to require in the
                                      generated password.
                                required:
                                  - digits
                                  - lowercase
                                  - uppercase
                                  - symbols
                                additionalProperties: false
                              allowedSymbols:
                                type: string
                                pattern: '[!@#$%^&*()_+\-=\[\]{};'':"\\|,.<>\/?~]'
                                description: >-
                                  The allowed symbols to use in the generated
                                  password (defaults to "-_.~!*").
                            required:
                              - length
                              - required
                            additionalProperties: false
                            description: >-
                              The password requirements to use when generating
                              the new password.
                          rotationMethod:
                            type: string
                            enum:
                              - login-as-target
                              - login-as-root
                            description: >-
                              Whether the rotation should be performed using
                              "login-as-target" (the target user's own
                              credentials) or "login-as-root" (the SSH
                              connection's admin credentials). Defaults to
                              "login-as-target".
                        required:
                          - username
                        additionalProperties: false
                      secretsMapping:
                        type: object
                        properties:
                          username:
                            type: string
                            minLength: 1
                            description: >-
                              The name of the secret that the username will be
                              mapped to.
                          password:
                            type: string
                            minLength: 1
                            description: >-
                              The name of the secret that the rotated password
                              will be mapped to.
                        required:
                          - username
                          - password
                        additionalProperties: false
                    required:
                      - id
                      - name
                      - folderId
                      - connectionId
                      - createdAt
                      - updatedAt
                      - rotationInterval
                      - rotationStatus
                      - lastRotationAttemptedAt
                      - lastRotatedAt
                      - connection
                      - environment
                      - projectId
                      - folder
                      - rotateAtUtc
                      - type
                      - parameters
                      - secretsMapping
                    additionalProperties: false
                required:
                  - message
                  - reconciled
                  - secretRotation
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