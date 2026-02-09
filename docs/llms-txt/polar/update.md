# Source: https://polar.sh/docs/api-reference/webhooks/endpoints/update.md

# Source: https://polar.sh/docs/api-reference/subscriptions/update.md

# Source: https://polar.sh/docs/api-reference/products/update.md

# Source: https://polar.sh/docs/api-reference/organizations/update.md

# Source: https://polar.sh/docs/api-reference/meters/update.md

# Source: https://polar.sh/docs/api-reference/license-keys/update.md

# Source: https://polar.sh/docs/api-reference/files/update.md

# Source: https://polar.sh/docs/api-reference/discounts/update.md

# Source: https://polar.sh/docs/api-reference/customers/update.md

# Source: https://polar.sh/docs/api-reference/customer-portal/subscriptions/update.md

# Source: https://polar.sh/docs/api-reference/custom-fields/update.md

# Source: https://polar.sh/docs/api-reference/checkout-links/update.md

# Source: https://polar.sh/docs/api-reference/benefits/update.md

> ## Documentation Index
> Fetch the complete documentation index at: https://polar.sh/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Benefit

> Update a benefit.

**Scopes**: `benefits:write`



## OpenAPI

````yaml patch /v1/benefits/{id}
openapi: 3.1.0
info:
  title: Polar API
  summary: Polar HTTP and Webhooks API
  description: Read the docs at https://polar.sh/docs/api-reference
  version: 0.1.0
servers:
  - url: https://api.polar.sh
    description: Production environment
    x-speakeasy-server-id: production
  - url: https://sandbox-api.polar.sh
    description: Sandbox environment
    x-speakeasy-server-id: sandbox
security:
  - access_token: []
tags:
  - name: public
    description: >-
      Endpoints shown and documented in the Polar API documentation and
      available in our SDKs.
  - name: private
    description: >-
      Endpoints that should appear in the schema only in development to generate
      our internal JS SDK.
  - name: mcp
    description: Endpoints enabled in the MCP server.
paths:
  /v1/benefits/{id}:
    patch:
      tags:
        - benefits
        - public
      summary: Update Benefit
      description: |-
        Update a benefit.

        **Scopes**: `benefits:write`
      operationId: benefits:update
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid4
            description: The benefit ID.
            x-polar-selector-widget:
              resourceRoot: /v1/benefits
              resourceName: Benefit
              displayProperty: description
            title: Id
      requestBody:
        required: true
        content:
          application/json:
            schema:
              anyOf:
                - $ref: '#/components/schemas/BenefitCustomUpdate'
                - $ref: '#/components/schemas/BenefitDiscordUpdate'
                - $ref: '#/components/schemas/BenefitGitHubRepositoryUpdate'
                - $ref: '#/components/schemas/BenefitDownloadablesUpdate'
                - $ref: '#/components/schemas/BenefitLicenseKeysUpdate'
                - $ref: '#/components/schemas/BenefitMeterCreditUpdate'
              title: Benefit Update
      responses:
        '200':
          description: Benefit updated.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Benefit'
                title: Benefit
        '404':
          description: Benefit not found.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceNotFound'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    BenefitCustomUpdate:
      properties:
        metadata:
          additionalProperties:
            anyOf:
              - type: string
                maxLength: 500
                minLength: 1
              - type: integer
              - type: number
              - type: boolean
          propertyNames:
            maxLength: 40
            minLength: 1
          type: object
          maxProperties: 50
          title: Metadata
          description: |-
            Key-value object allowing you to store additional information.

            The key must be a string with a maximum length of **40 characters**.
            The value must be either:

            * A string with a maximum length of **500 characters**
            * An integer
            * A floating-point number
            * A boolean

            You can store up to **50 key-value pairs**.
        description:
          anyOf:
            - type: string
              maxLength: 42
              minLength: 3
            - type: 'null'
          title: Description
          description: >-
            The description of the benefit. Will be displayed on products having
            this benefit.
        type:
          type: string
          const: custom
          title: Type
        properties:
          anyOf:
            - $ref: '#/components/schemas/BenefitCustomProperties'
            - type: 'null'
      type: object
      required:
        - type
      title: BenefitCustomUpdate
    BenefitDiscordUpdate:
      properties:
        metadata:
          additionalProperties:
            anyOf:
              - type: string
                maxLength: 500
                minLength: 1
              - type: integer
              - type: number
              - type: boolean
          propertyNames:
            maxLength: 40
            minLength: 1
          type: object
          maxProperties: 50
          title: Metadata
          description: |-
            Key-value object allowing you to store additional information.

            The key must be a string with a maximum length of **40 characters**.
            The value must be either:

            * A string with a maximum length of **500 characters**
            * An integer
            * A floating-point number
            * A boolean

            You can store up to **50 key-value pairs**.
        description:
          anyOf:
            - type: string
              maxLength: 42
              minLength: 3
            - type: 'null'
          title: Description
          description: >-
            The description of the benefit. Will be displayed on products having
            this benefit.
        type:
          type: string
          const: discord
          title: Type
        properties:
          anyOf:
            - $ref: '#/components/schemas/BenefitDiscordCreateProperties'
            - type: 'null'
      type: object
      required:
        - type
      title: BenefitDiscordUpdate
    BenefitGitHubRepositoryUpdate:
      properties:
        metadata:
          additionalProperties:
            anyOf:
              - type: string
                maxLength: 500
                minLength: 1
              - type: integer
              - type: number
              - type: boolean
          propertyNames:
            maxLength: 40
            minLength: 1
          type: object
          maxProperties: 50
          title: Metadata
          description: |-
            Key-value object allowing you to store additional information.

            The key must be a string with a maximum length of **40 characters**.
            The value must be either:

            * A string with a maximum length of **500 characters**
            * An integer
            * A floating-point number
            * A boolean

            You can store up to **50 key-value pairs**.
        description:
          anyOf:
            - type: string
              maxLength: 42
              minLength: 3
            - type: 'null'
          title: Description
          description: >-
            The description of the benefit. Will be displayed on products having
            this benefit.
        type:
          type: string
          const: github_repository
          title: Type
        properties:
          anyOf:
            - $ref: '#/components/schemas/BenefitGitHubRepositoryCreateProperties'
            - type: 'null'
      type: object
      required:
        - type
      title: BenefitGitHubRepositoryUpdate
    BenefitDownloadablesUpdate:
      properties:
        metadata:
          additionalProperties:
            anyOf:
              - type: string
                maxLength: 500
                minLength: 1
              - type: integer
              - type: number
              - type: boolean
          propertyNames:
            maxLength: 40
            minLength: 1
          type: object
          maxProperties: 50
          title: Metadata
          description: |-
            Key-value object allowing you to store additional information.

            The key must be a string with a maximum length of **40 characters**.
            The value must be either:

            * A string with a maximum length of **500 characters**
            * An integer
            * A floating-point number
            * A boolean

            You can store up to **50 key-value pairs**.
        description:
          anyOf:
            - type: string
              maxLength: 42
              minLength: 3
            - type: 'null'
          title: Description
          description: >-
            The description of the benefit. Will be displayed on products having
            this benefit.
        type:
          type: string
          const: downloadables
          title: Type
        properties:
          anyOf:
            - $ref: '#/components/schemas/BenefitDownloadablesCreateProperties'
            - type: 'null'
      type: object
      required:
        - type
      title: BenefitDownloadablesUpdate
    BenefitLicenseKeysUpdate:
      properties:
        metadata:
          additionalProperties:
            anyOf:
              - type: string
                maxLength: 500
                minLength: 1
              - type: integer
              - type: number
              - type: boolean
          propertyNames:
            maxLength: 40
            minLength: 1
          type: object
          maxProperties: 50
          title: Metadata
          description: |-
            Key-value object allowing you to store additional information.

            The key must be a string with a maximum length of **40 characters**.
            The value must be either:

            * A string with a maximum length of **500 characters**
            * An integer
            * A floating-point number
            * A boolean

            You can store up to **50 key-value pairs**.
        description:
          anyOf:
            - type: string
              maxLength: 42
              minLength: 3
            - type: 'null'
          title: Description
          description: >-
            The description of the benefit. Will be displayed on products having
            this benefit.
        type:
          type: string
          const: license_keys
          title: Type
        properties:
          anyOf:
            - $ref: '#/components/schemas/BenefitLicenseKeysCreateProperties'
            - type: 'null'
      type: object
      required:
        - type
      title: BenefitLicenseKeysUpdate
    BenefitMeterCreditUpdate:
      properties:
        metadata:
          additionalProperties:
            anyOf:
              - type: string
                maxLength: 500
                minLength: 1
              - type: integer
              - type: number
              - type: boolean
          propertyNames:
            maxLength: 40
            minLength: 1
          type: object
          maxProperties: 50
          title: Metadata
          description: |-
            Key-value object allowing you to store additional information.

            The key must be a string with a maximum length of **40 characters**.
            The value must be either:

            * A string with a maximum length of **500 characters**
            * An integer
            * A floating-point number
            * A boolean

            You can store up to **50 key-value pairs**.
        description:
          anyOf:
            - type: string
              maxLength: 42
              minLength: 3
            - type: 'null'
          title: Description
          description: >-
            The description of the benefit. Will be displayed on products having
            this benefit.
        type:
          type: string
          const: meter_credit
          title: Type
        properties:
          anyOf:
            - $ref: '#/components/schemas/BenefitMeterCreditCreateProperties'
            - type: 'null'
      type: object
      required:
        - type
      title: BenefitMeterCreditUpdate
    Benefit:
      anyOf:
        - $ref: '#/components/schemas/BenefitCustom'
        - $ref: '#/components/schemas/BenefitDiscord'
        - $ref: '#/components/schemas/BenefitGitHubRepository'
        - $ref: '#/components/schemas/BenefitDownloadables'
        - $ref: '#/components/schemas/BenefitLicenseKeys'
        - $ref: '#/components/schemas/BenefitMeterCredit'
    ResourceNotFound:
      properties:
        error:
          type: string
          const: ResourceNotFound
          title: Error
          examples:
            - ResourceNotFound
        detail:
          type: string
          title: Detail
      type: object
      required:
        - error
        - detail
      title: ResourceNotFound
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    BenefitCustomProperties:
      properties:
        note:
          anyOf:
            - anyOf:
                - type: string
                - type: 'null'
              description: >-
                Private note to be shared with customers who have this benefit
                granted.
            - type: 'null'
          title: Note
      type: object
      required:
        - note
      title: BenefitCustomProperties
      description: Properties for a benefit of type `custom`.
    BenefitDiscordCreateProperties:
      properties:
        guild_token:
          type: string
          title: Guild Token
        role_id:
          type: string
          title: Role Id
          description: The ID of the Discord role to grant.
        kick_member:
          type: boolean
          title: Kick Member
          description: Whether to kick the member from the Discord server on revocation.
      type: object
      required:
        - guild_token
        - role_id
        - kick_member
      title: BenefitDiscordCreateProperties
      description: Properties to create a benefit of type `discord`.
    BenefitGitHubRepositoryCreateProperties:
      properties:
        repository_owner:
          type: string
          title: Repository Owner
          description: The owner of the repository.
          examples:
            - polarsource
        repository_name:
          type: string
          title: Repository Name
          description: The name of the repository.
          examples:
            - private_repo
        permission:
          type: string
          enum:
            - pull
            - triage
            - push
            - maintain
            - admin
          title: Permission
          description: >-
            The permission level to grant. Read more about roles and their
            permissions on [GitHub
            documentation](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization#permissions-for-each-role).
      type: object
      required:
        - repository_owner
        - repository_name
        - permission
      title: BenefitGitHubRepositoryCreateProperties
      description: Properties to create a benefit of type `github_repository`.
    BenefitDownloadablesCreateProperties:
      properties:
        archived:
          additionalProperties:
            type: boolean
          propertyNames:
            format: uuid4
          type: object
          title: Archived
          default: {}
        files:
          items:
            type: string
            format: uuid4
          type: array
          minItems: 1
          title: Files
      type: object
      required:
        - files
      title: BenefitDownloadablesCreateProperties
    BenefitLicenseKeysCreateProperties:
      properties:
        prefix:
          anyOf:
            - type: string
            - type: 'null'
          title: Prefix
        expires:
          anyOf:
            - $ref: '#/components/schemas/BenefitLicenseKeyExpirationProperties'
            - type: 'null'
        activations:
          anyOf:
            - $ref: '#/components/schemas/BenefitLicenseKeyActivationCreateProperties'
            - type: 'null'
        limit_usage:
          anyOf:
            - type: integer
              exclusiveMinimum: 0
            - type: 'null'
          title: Limit Usage
      type: object
      title: BenefitLicenseKeysCreateProperties
    BenefitMeterCreditCreateProperties:
      properties:
        units:
          type: integer
          maximum: 2147483647
          exclusiveMinimum: 0
          title: Units
        rollover:
          type: boolean
          title: Rollover
        meter_id:
          type: string
          format: uuid4
          title: Meter Id
      type: object
      required:
        - units
        - rollover
        - meter_id
      title: BenefitMeterCreditCreateProperties
      description: Properties for creating a benefit of type `meter_unit`.
    BenefitCustom:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the benefit.
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        type:
          type: string
          const: custom
          title: Type
        description:
          type: string
          title: Description
          description: The description of the benefit.
        selectable:
          type: boolean
          title: Selectable
          description: Whether the benefit is selectable when creating a product.
        deletable:
          type: boolean
          title: Deletable
          description: Whether the benefit is deletable.
        organization_id:
          type: string
          format: uuid4
          title: Organization Id
          description: The ID of the organization owning the benefit.
        metadata:
          $ref: '#/components/schemas/MetadataOutputType'
        properties:
          $ref: '#/components/schemas/BenefitCustomProperties'
      type: object
      required:
        - id
        - created_at
        - modified_at
        - type
        - description
        - selectable
        - deletable
        - organization_id
        - metadata
        - properties
      title: BenefitCustom
      description: |-
        A benefit of type `custom`.

        Use it to grant any kind of benefit that doesn't fit in the other types.
    BenefitDiscord:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the benefit.
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        type:
          type: string
          const: discord
          title: Type
        description:
          type: string
          title: Description
          description: The description of the benefit.
        selectable:
          type: boolean
          title: Selectable
          description: Whether the benefit is selectable when creating a product.
        deletable:
          type: boolean
          title: Deletable
          description: Whether the benefit is deletable.
        organization_id:
          type: string
          format: uuid4
          title: Organization Id
          description: The ID of the organization owning the benefit.
        metadata:
          $ref: '#/components/schemas/MetadataOutputType'
        properties:
          $ref: '#/components/schemas/BenefitDiscordProperties'
      type: object
      required:
        - id
        - created_at
        - modified_at
        - type
        - description
        - selectable
        - deletable
        - organization_id
        - metadata
        - properties
      title: BenefitDiscord
      description: |-
        A benefit of type `discord`.

        Use it to automatically invite your backers to a Discord server.
    BenefitGitHubRepository:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the benefit.
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        type:
          type: string
          const: github_repository
          title: Type
        description:
          type: string
          title: Description
          description: The description of the benefit.
        selectable:
          type: boolean
          title: Selectable
          description: Whether the benefit is selectable when creating a product.
        deletable:
          type: boolean
          title: Deletable
          description: Whether the benefit is deletable.
        organization_id:
          type: string
          format: uuid4
          title: Organization Id
          description: The ID of the organization owning the benefit.
        metadata:
          $ref: '#/components/schemas/MetadataOutputType'
        properties:
          $ref: '#/components/schemas/BenefitGitHubRepositoryProperties'
      type: object
      required:
        - id
        - created_at
        - modified_at
        - type
        - description
        - selectable
        - deletable
        - organization_id
        - metadata
        - properties
      title: BenefitGitHubRepository
      description: >-
        A benefit of type `github_repository`.


        Use it to automatically invite your backers to a private GitHub
        repository.
    BenefitDownloadables:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the benefit.
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        type:
          type: string
          const: downloadables
          title: Type
        description:
          type: string
          title: Description
          description: The description of the benefit.
        selectable:
          type: boolean
          title: Selectable
          description: Whether the benefit is selectable when creating a product.
        deletable:
          type: boolean
          title: Deletable
          description: Whether the benefit is deletable.
        organization_id:
          type: string
          format: uuid4
          title: Organization Id
          description: The ID of the organization owning the benefit.
        metadata:
          $ref: '#/components/schemas/MetadataOutputType'
        properties:
          $ref: '#/components/schemas/BenefitDownloadablesProperties'
      type: object
      required:
        - id
        - created_at
        - modified_at
        - type
        - description
        - selectable
        - deletable
        - organization_id
        - metadata
        - properties
      title: BenefitDownloadables
    BenefitLicenseKeys:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the benefit.
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        type:
          type: string
          const: license_keys
          title: Type
        description:
          type: string
          title: Description
          description: The description of the benefit.
        selectable:
          type: boolean
          title: Selectable
          description: Whether the benefit is selectable when creating a product.
        deletable:
          type: boolean
          title: Deletable
          description: Whether the benefit is deletable.
        organization_id:
          type: string
          format: uuid4
          title: Organization Id
          description: The ID of the organization owning the benefit.
        metadata:
          $ref: '#/components/schemas/MetadataOutputType'
        properties:
          $ref: '#/components/schemas/BenefitLicenseKeysProperties'
      type: object
      required:
        - id
        - created_at
        - modified_at
        - type
        - description
        - selectable
        - deletable
        - organization_id
        - metadata
        - properties
      title: BenefitLicenseKeys
    BenefitMeterCredit:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the benefit.
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        type:
          type: string
          const: meter_credit
          title: Type
        description:
          type: string
          title: Description
          description: The description of the benefit.
        selectable:
          type: boolean
          title: Selectable
          description: Whether the benefit is selectable when creating a product.
        deletable:
          type: boolean
          title: Deletable
          description: Whether the benefit is deletable.
        organization_id:
          type: string
          format: uuid4
          title: Organization Id
          description: The ID of the organization owning the benefit.
        metadata:
          $ref: '#/components/schemas/MetadataOutputType'
        properties:
          $ref: '#/components/schemas/BenefitMeterCreditProperties'
      type: object
      required:
        - id
        - created_at
        - modified_at
        - type
        - description
        - selectable
        - deletable
        - organization_id
        - metadata
        - properties
      title: BenefitMeterCredit
      description: |-
        A benefit of type `meter_unit`.

        Use it to grant a number of units on a specific meter.
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
    BenefitLicenseKeyExpirationProperties:
      properties:
        ttl:
          type: integer
          exclusiveMinimum: 0
          title: Ttl
        timeframe:
          type: string
          enum:
            - year
            - month
            - day
          title: Timeframe
      type: object
      required:
        - ttl
        - timeframe
      title: BenefitLicenseKeyExpirationProperties
    BenefitLicenseKeyActivationCreateProperties:
      properties:
        limit:
          type: integer
          maximum: 50
          exclusiveMinimum: 0
          title: Limit
        enable_customer_admin:
          type: boolean
          title: Enable Customer Admin
      type: object
      required:
        - limit
        - enable_customer_admin
      title: BenefitLicenseKeyActivationCreateProperties
    MetadataOutputType:
      additionalProperties:
        anyOf:
          - type: string
          - type: integer
          - type: number
          - type: boolean
      type: object
    BenefitDiscordProperties:
      properties:
        guild_id:
          type: string
          title: Guild Id
          description: The ID of the Discord server.
        role_id:
          type: string
          title: Role Id
          description: The ID of the Discord role to grant.
        kick_member:
          type: boolean
          title: Kick Member
          description: Whether to kick the member from the Discord server on revocation.
        guild_token:
          type: string
          title: Guild Token
      type: object
      required:
        - guild_id
        - role_id
        - kick_member
        - guild_token
      title: BenefitDiscordProperties
      description: Properties for a benefit of type `discord`.
    BenefitGitHubRepositoryProperties:
      properties:
        repository_owner:
          type: string
          title: Repository Owner
          description: The owner of the repository.
          examples:
            - polarsource
        repository_name:
          type: string
          title: Repository Name
          description: The name of the repository.
          examples:
            - private_repo
        permission:
          type: string
          enum:
            - pull
            - triage
            - push
            - maintain
            - admin
          title: Permission
          description: >-
            The permission level to grant. Read more about roles and their
            permissions on [GitHub
            documentation](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization#permissions-for-each-role).
      type: object
      required:
        - repository_owner
        - repository_name
        - permission
      title: BenefitGitHubRepositoryProperties
      description: Properties for a benefit of type `github_repository`.
    BenefitDownloadablesProperties:
      properties:
        archived:
          additionalProperties:
            type: boolean
          propertyNames:
            format: uuid4
          type: object
          title: Archived
        files:
          items:
            type: string
            format: uuid4
          type: array
          title: Files
      type: object
      required:
        - archived
        - files
      title: BenefitDownloadablesProperties
    BenefitLicenseKeysProperties:
      properties:
        prefix:
          anyOf:
            - type: string
            - type: 'null'
          title: Prefix
        expires:
          anyOf:
            - $ref: '#/components/schemas/BenefitLicenseKeyExpirationProperties'
            - type: 'null'
        activations:
          anyOf:
            - $ref: '#/components/schemas/BenefitLicenseKeyActivationProperties'
            - type: 'null'
        limit_usage:
          anyOf:
            - type: integer
            - type: 'null'
          title: Limit Usage
      type: object
      required:
        - prefix
        - expires
        - activations
        - limit_usage
      title: BenefitLicenseKeysProperties
    BenefitMeterCreditProperties:
      properties:
        units:
          type: integer
          title: Units
        rollover:
          type: boolean
          title: Rollover
        meter_id:
          type: string
          format: uuid4
          title: Meter Id
      type: object
      required:
        - units
        - rollover
        - meter_id
      title: BenefitMeterCreditProperties
      description: Properties for a benefit of type `meter_unit`.
    BenefitLicenseKeyActivationProperties:
      properties:
        limit:
          type: integer
          title: Limit
        enable_customer_admin:
          type: boolean
          title: Enable Customer Admin
      type: object
      required:
        - limit
        - enable_customer_admin
      title: BenefitLicenseKeyActivationProperties
  securitySchemes:
    access_token:
      type: http
      scheme: bearer
      description: >-
        You can generate an **Organization Access Token** from your
        organization's settings.

````