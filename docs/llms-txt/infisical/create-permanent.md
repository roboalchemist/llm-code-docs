# Source: https://infisical.com/docs/api-reference/endpoints/identity-specific-privilege/v1/create-permanent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Permanent

> Create a permanent or a non expiry specific privilege for identity.



## OpenAPI

````yaml POST /api/v1/additional-privilege/identity/permanent
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
  /api/v1/additional-privilege/identity/permanent:
    post:
      tags:
        - Identity Specific Privileges
      description: Create a permanent or a non expiry specific privilege for identity.
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                identityId:
                  type: string
                  minLength: 1
                  description: The ID of the machine identity to create.
                projectSlug:
                  type: string
                  minLength: 1
                  description: The slug of the project of the identity in.
                slug:
                  type: string
                  minLength: 1
                  maxLength: 60
                  description: The slug of the privilege to create.
                permissions:
                  type: array
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
                          - secret-event-subscriptions
                          - app-connections
                          - pam-folders
                          - pam-resources
                          - pam-accounts
                          - pam-sessions
                          - certificate-profiles
                          - certificate-policies
                          - approval-requests
                          - approval-request-grants
                          - mcp-endpoints
                          - mcp-servers
                          - mcp-activity-logs
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

                    { "permissions": [{"action": "read", "subject": "secrets"]}

                    ```

                    - Read and Write secrets

                    ```

                    { "permissions": [{"action": "read", "subject": "secrets"],
                    {"action": "write", "subject": "secrets"]}

                    ```

                    - Read secrets scoped to an environment and secret path

                    ```

                    - { "permissions": [{"action": "read", "subject": "secrets",
                    "conditions": { "environment": "dev", "secretPath": {
                    "$glob": "/" } }}] }

                    ```
                privilegePermission:
                  type: object
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
                                Can be a glob pattern such as /folder-name/*/** 
                          required:
                            - $glob
                          additionalProperties: false
                      required:
                        - environment
                      additionalProperties: false
                      description: >-
                        When specified, only matching conditions will be allowed
                        to access given resource.
                  required:
                    - actions
                    - subject
                    - conditions
                  additionalProperties: false
                  description: The permission object for the privilege.
              required:
                - identityId
                - projectSlug
              additionalProperties: false
        required: true
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  privilege:
                    type: object
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
                required:
                  - privilege
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