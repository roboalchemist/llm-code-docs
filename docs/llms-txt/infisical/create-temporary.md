# Source: https://infisical.com/docs/api-reference/endpoints/identity-specific-privilege/v1/create-temporary.md

# Create Temporary

> Create a temporary or a expiring specific privilege for identity.

## OpenAPI

````yaml POST /api/v1/additional-privilege/identity/temporary
paths:
  path: /api/v1/additional-privilege/identity/temporary
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
              identityId:
                allOf:
                  - type: string
                    minLength: 1
                    description: The ID of the machine identity to create.
              projectSlug:
                allOf:
                  - type: string
                    minLength: 1
                    description: The slug of the project of the identity in.
              slug:
                allOf:
                  - type: string
                    minLength: 1
                    maxLength: 60
                    description: The slug of the privilege to create.
              permissions:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        action:
                          type: string
                          enum:
                            - read
                            - create
                            - edit
                            - delete
                          description: >-
                            Describe what action an entity can take. Possible
                            actions: create, edit, delete, and read
                        subject:
                          type: string
                          enum:
                            - role
                            - member
                            - groups
                            - settings
                            - integrations
                            - webhooks
                            - service-tokens
                            - environments
                            - tags
                            - audit-logs
                            - ip-allowlist
                            - workspace
                            - secrets
                            - secret-folders
                            - secret-imports
                            - dynamic-secrets
                            - secret-rollback
                            - secret-approval
                            - secret-rotation
                            - commits
                            - identity
                            - certificate-authorities
                            - certificates
                            - certificate-templates
                            - ssh-certificate-authorities
                            - ssh-certificates
                            - ssh-certificate-templates
                            - ssh-hosts
                            - ssh-host-groups
                            - pki-subscribers
                            - pki-alerts
                            - pki-collections
                            - kms
                            - cmek
                            - secret-syncs
                            - pki-syncs
                            - kmip
                            - secret-scanning-data-sources
                            - secret-scanning-findings
                            - secret-scanning-configs
                            - secret-events
                            - app-connections
                            - pam-folders
                            - pam-resources
                            - pam-accounts
                            - pam-sessions
                            - certificate-profiles
                          description: >-
                            The entity this permission pertains to. Possible
                            options: secrets, environments
                        conditions:
                          type: object
                          properties:
                            environment:
                              type: string
                              description: >-
                                The environment slug this permission should
                                allow.
                            secretPath:
                              type: object
                              properties:
                                $glob:
                                  type: string
                                  minLength: 1
                                  description: >-
                                    The secret path this permission should
                                    allow. Can be a glob pattern such as
                                    /folder-name/*/** 
                              required:
                                - $glob
                              additionalProperties: false
                          additionalProperties: false
                          description: >-
                            When specified, only matching conditions will be
                            allowed to access given resource.
                      required:
                        - action
                        - subject
                      additionalProperties: false
                    description: >
                      @deprecated - use privilegePermission

                      The permission object for the privilege.

                      - Read secrets

                      ```

                      { "permissions": [{"action": "read", "subject":
                      "secrets"]}

                      ```

                      - Read and Write secrets

                      ```

                      { "permissions": [{"action": "read", "subject":
                      "secrets"], {"action": "write", "subject": "secrets"]}

                      ```

                      - Read secrets scoped to an environment and secret path

                      ```

                      - { "permissions": [{"action": "read", "subject":
                      "secrets", "conditions": { "environment": "dev",
                      "secretPath": { "$glob": "/" } }}] }

                      ```
              privilegePermission:
                allOf:
                  - type: object
                    properties:
                      actions:
                        type: array
                        items:
                          type: string
                          enum:
                            - read
                            - create
                            - edit
                            - delete
                          description: >-
                            Describe what action an entity can take. Possible
                            actions: create, edit, delete, and read
                        minItems: 1
                      subject:
                        type: string
                        enum:
                          - secrets
                        description: >-
                          The entity this permission pertains to. Possible
                          options: secrets, environments
                      conditions:
                        type: object
                        properties:
                          environment:
                            type: string
                            description: The environment slug this permission should allow.
                          secretPath:
                            type: object
                            properties:
                              $glob:
                                type: string
                                minLength: 1
                                description: >-
                                  The secret path this permission should allow.
                                  Can be a glob pattern such as
                                  /folder-name/*/** 
                            required:
                              - $glob
                            additionalProperties: false
                        required:
                          - environment
                        additionalProperties: false
                        description: >-
                          When specified, only matching conditions will be
                          allowed to access given resource.
                    required:
                      - actions
                      - subject
                      - conditions
                    additionalProperties: false
                    description: The permission object for the privilege.
              temporaryMode:
                allOf:
                  - type: string
                    enum:
                      - relative
                    description: 'Type of temporary access given. Types: relative.'
              temporaryRange:
                allOf:
                  - type: string
                    description: 'TTL for the temporary time. Eg: 1m, 1h, 1d.'
              temporaryAccessStartTime:
                allOf:
                  - type: string
                    format: date-time
                    description: ISO time for which temporary access should begin.
            required: true
            requiredProperties:
              - identityId
              - projectSlug
              - temporaryMode
              - temporaryRange
              - temporaryAccessStartTime
            additionalProperties: false
        examples:
          example:
            value:
              identityId: <string>
              projectSlug: <string>
              slug: <string>
              permissions:
                - action: read
                  subject: role
                  conditions:
                    environment: <string>
                    secretPath:
                      $glob: <string>
              privilegePermission:
                actions:
                  - read
                subject: secrets
                conditions:
                  environment: <string>
                  secretPath:
                    $glob: <string>
              temporaryMode: relative
              temporaryRange: <string>
              temporaryAccessStartTime: '2023-11-07T05:31:56Z'
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              privilege:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      slug:
                        type: string
                      projectMembershipId:
                        type: string
                        format: uuid
                      isTemporary:
                        type: boolean
                        default: false
                      temporaryMode:
                        type: string
                        nullable: true
                      temporaryRange:
                        type: string
                        nullable: true
                      temporaryAccessStartTime:
                        type: string
                        format: date-time
                        nullable: true
                      temporaryAccessEndTime:
                        type: string
                        format: date-time
                        nullable: true
                      permissions:
                        type: array
                        items:
                          type: object
                          properties:
                            subject:
                              anyOf:
                                - type: string
                                  minLength: 1
                                - type: array
                                  items:
                                    type: string
                            action:
                              anyOf:
                                - type: string
                                  minLength: 1
                                - type: array
                                  items:
                                    type: string
                            conditions: {}
                            inverted:
                              type: boolean
                          required:
                            - action
                          additionalProperties: false
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                    required:
                      - id
                      - slug
                      - projectMembershipId
                      - permissions
                      - createdAt
                      - updatedAt
                    additionalProperties: false
            requiredProperties:
              - privilege
            additionalProperties: false
        examples:
          example:
            value:
              privilege:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                slug: <string>
                projectMembershipId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                isTemporary: false
                temporaryMode: <string>
                temporaryRange: <string>
                temporaryAccessStartTime: '2023-11-07T05:31:56Z'
                temporaryAccessEndTime: '2023-11-07T05:31:56Z'
                permissions:
                  - subject: <string>
                    action: <string>
                    conditions: <any>
                    inverted: true
                createdAt: '2023-11-07T05:31:56Z'
                updatedAt: '2023-11-07T05:31:56Z'
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