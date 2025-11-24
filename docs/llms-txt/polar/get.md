# Source: https://polar.sh/docs/api-reference/webhooks/endpoints/get.md

# Source: https://polar.sh/docs/api-reference/subscriptions/get.md

# Source: https://polar.sh/docs/api-reference/products/get.md

# Source: https://polar.sh/docs/api-reference/organizations/get.md

# Source: https://polar.sh/docs/api-reference/orders/get.md

# Source: https://polar.sh/docs/api-reference/metrics/get.md

# Source: https://polar.sh/docs/api-reference/meters/get.md

# Source: https://polar.sh/docs/api-reference/license-keys/get.md

# Source: https://polar.sh/docs/api-reference/events/get.md

# Source: https://polar.sh/docs/api-reference/discounts/get.md

# Source: https://polar.sh/docs/api-reference/customers/get.md

# Source: https://polar.sh/docs/api-reference/customer-portal/subscriptions/get.md

# Source: https://polar.sh/docs/api-reference/customer-portal/orders/get.md

# Source: https://polar.sh/docs/api-reference/customer-portal/license-keys/get.md

# Source: https://polar.sh/docs/api-reference/customer-portal/downloadables/get.md

# Source: https://polar.sh/docs/api-reference/customer-meters/get.md

# Source: https://polar.sh/docs/api-reference/custom-fields/get.md

# Source: https://polar.sh/docs/api-reference/checkout-links/get.md

# Source: https://polar.sh/docs/api-reference/benefits/get.md

# Get Benefit

> Get a benefit by ID.

**Scopes**: `benefits:read` `benefits:write`

## OpenAPI

````yaml get /v1/benefits/{id}
paths:
  path: /v1/benefits/{id}
  method: get
  servers:
    - url: https://api.polar.sh
      description: Production environment
    - url: https://sandbox-api.polar.sh
      description: Sandbox environment
  request:
    security:
      - title: access token
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                You can generate an **Organization Access Token** from your
                organization's settings.
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              title: Id
              description: The benefit ID.
              format: uuid4
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\t\"os\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New(\n        polargo.WithSecurity(os.Getenv(\"POLAR_ACCESS_TOKEN\")),\n    )\n\n    res, err := s.Benefits.Get(ctx, \"<value>\")\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Benefit != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          from polar_sdk import Polar


          with Polar(
              access_token="<YOUR_BEARER_TOKEN_HERE>",
          ) as polar:

              res = polar.benefits.get(id="<value>")

              # Handle response
              print(res)
      - label: Typescript (SDK)
        lang: typescript
        source: |-
          import { Polar } from "@polar-sh/sdk";

          const polar = new Polar({
            accessToken: process.env["POLAR_ACCESS_TOKEN"] ?? "",
          });

          async function run() {
            const result = await polar.benefits.get({
              id: "<value>",
            });

            console.log(result);
          }

          run();
      - label: PHP (SDK)
        lang: php
        source: |-
          declare(strict_types=1);

          require 'vendor/autoload.php';

          use Polar;

          $sdk = Polar\Polar::builder()
              ->setSecurity(
                  '<YOUR_BEARER_TOKEN_HERE>'
              )
              ->build();



          $response = $sdk->benefits->get(
              id: '<value>'
          );

          if ($response->benefit !== null) {
              // handle response
          }
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Id
                    description: The ID of the benefit.
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    title: Created At
                    description: Creation timestamp of the object.
              modified_at:
                allOf:
                  - anyOf:
                      - type: string
                        format: date-time
                      - type: 'null'
                    title: Modified At
                    description: Last modification timestamp of the object.
              type:
                allOf:
                  - type: string
                    const: custom
                    title: Type
              description:
                allOf:
                  - type: string
                    title: Description
                    description: The description of the benefit.
              selectable:
                allOf:
                  - type: boolean
                    title: Selectable
                    description: Whether the benefit is selectable when creating a product.
              deletable:
                allOf:
                  - type: boolean
                    title: Deletable
                    description: Whether the benefit is deletable.
              organization_id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Organization Id
                    description: The ID of the organization owning the benefit.
              metadata:
                allOf:
                  - additionalProperties:
                      anyOf:
                        - type: string
                        - type: integer
                        - type: number
                        - type: boolean
                    type: object
                    title: Metadata
              properties:
                allOf:
                  - $ref: '#/components/schemas/BenefitCustomProperties'
            title: BenefitCustom
            description: >-
              A benefit of type `custom`.


              Use it to grant any kind of benefit that doesn't fit in the other
              types.
            refIdentifier: '#/components/schemas/BenefitCustom'
            requiredProperties:
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
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Id
                    description: The ID of the benefit.
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    title: Created At
                    description: Creation timestamp of the object.
              modified_at:
                allOf:
                  - anyOf:
                      - type: string
                        format: date-time
                      - type: 'null'
                    title: Modified At
                    description: Last modification timestamp of the object.
              type:
                allOf:
                  - type: string
                    const: discord
                    title: Type
              description:
                allOf:
                  - type: string
                    title: Description
                    description: The description of the benefit.
              selectable:
                allOf:
                  - type: boolean
                    title: Selectable
                    description: Whether the benefit is selectable when creating a product.
              deletable:
                allOf:
                  - type: boolean
                    title: Deletable
                    description: Whether the benefit is deletable.
              organization_id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Organization Id
                    description: The ID of the organization owning the benefit.
              metadata:
                allOf:
                  - additionalProperties:
                      anyOf:
                        - type: string
                        - type: integer
                        - type: number
                        - type: boolean
                    type: object
                    title: Metadata
              properties:
                allOf:
                  - $ref: '#/components/schemas/BenefitDiscordProperties'
            title: BenefitDiscord
            description: |-
              A benefit of type `discord`.

              Use it to automatically invite your backers to a Discord server.
            refIdentifier: '#/components/schemas/BenefitDiscord'
            requiredProperties:
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
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Id
                    description: The ID of the benefit.
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    title: Created At
                    description: Creation timestamp of the object.
              modified_at:
                allOf:
                  - anyOf:
                      - type: string
                        format: date-time
                      - type: 'null'
                    title: Modified At
                    description: Last modification timestamp of the object.
              type:
                allOf:
                  - type: string
                    const: github_repository
                    title: Type
              description:
                allOf:
                  - type: string
                    title: Description
                    description: The description of the benefit.
              selectable:
                allOf:
                  - type: boolean
                    title: Selectable
                    description: Whether the benefit is selectable when creating a product.
              deletable:
                allOf:
                  - type: boolean
                    title: Deletable
                    description: Whether the benefit is deletable.
              organization_id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Organization Id
                    description: The ID of the organization owning the benefit.
              metadata:
                allOf:
                  - additionalProperties:
                      anyOf:
                        - type: string
                        - type: integer
                        - type: number
                        - type: boolean
                    type: object
                    title: Metadata
              properties:
                allOf:
                  - $ref: '#/components/schemas/BenefitGitHubRepositoryProperties'
            title: BenefitGitHubRepository
            description: >-
              A benefit of type `github_repository`.


              Use it to automatically invite your backers to a private GitHub
              repository.
            refIdentifier: '#/components/schemas/BenefitGitHubRepository'
            requiredProperties:
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
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Id
                    description: The ID of the benefit.
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    title: Created At
                    description: Creation timestamp of the object.
              modified_at:
                allOf:
                  - anyOf:
                      - type: string
                        format: date-time
                      - type: 'null'
                    title: Modified At
                    description: Last modification timestamp of the object.
              type:
                allOf:
                  - type: string
                    const: downloadables
                    title: Type
              description:
                allOf:
                  - type: string
                    title: Description
                    description: The description of the benefit.
              selectable:
                allOf:
                  - type: boolean
                    title: Selectable
                    description: Whether the benefit is selectable when creating a product.
              deletable:
                allOf:
                  - type: boolean
                    title: Deletable
                    description: Whether the benefit is deletable.
              organization_id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Organization Id
                    description: The ID of the organization owning the benefit.
              metadata:
                allOf:
                  - additionalProperties:
                      anyOf:
                        - type: string
                        - type: integer
                        - type: number
                        - type: boolean
                    type: object
                    title: Metadata
              properties:
                allOf:
                  - $ref: '#/components/schemas/BenefitDownloadablesProperties'
            title: BenefitDownloadables
            refIdentifier: '#/components/schemas/BenefitDownloadables'
            requiredProperties:
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
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Id
                    description: The ID of the benefit.
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    title: Created At
                    description: Creation timestamp of the object.
              modified_at:
                allOf:
                  - anyOf:
                      - type: string
                        format: date-time
                      - type: 'null'
                    title: Modified At
                    description: Last modification timestamp of the object.
              type:
                allOf:
                  - type: string
                    const: license_keys
                    title: Type
              description:
                allOf:
                  - type: string
                    title: Description
                    description: The description of the benefit.
              selectable:
                allOf:
                  - type: boolean
                    title: Selectable
                    description: Whether the benefit is selectable when creating a product.
              deletable:
                allOf:
                  - type: boolean
                    title: Deletable
                    description: Whether the benefit is deletable.
              organization_id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Organization Id
                    description: The ID of the organization owning the benefit.
              metadata:
                allOf:
                  - additionalProperties:
                      anyOf:
                        - type: string
                        - type: integer
                        - type: number
                        - type: boolean
                    type: object
                    title: Metadata
              properties:
                allOf:
                  - $ref: '#/components/schemas/BenefitLicenseKeysProperties'
            title: BenefitLicenseKeys
            refIdentifier: '#/components/schemas/BenefitLicenseKeys'
            requiredProperties:
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
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Id
                    description: The ID of the benefit.
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    title: Created At
                    description: Creation timestamp of the object.
              modified_at:
                allOf:
                  - anyOf:
                      - type: string
                        format: date-time
                      - type: 'null'
                    title: Modified At
                    description: Last modification timestamp of the object.
              type:
                allOf:
                  - type: string
                    const: meter_credit
                    title: Type
              description:
                allOf:
                  - type: string
                    title: Description
                    description: The description of the benefit.
              selectable:
                allOf:
                  - type: boolean
                    title: Selectable
                    description: Whether the benefit is selectable when creating a product.
              deletable:
                allOf:
                  - type: boolean
                    title: Deletable
                    description: Whether the benefit is deletable.
              organization_id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Organization Id
                    description: The ID of the organization owning the benefit.
              metadata:
                allOf:
                  - additionalProperties:
                      anyOf:
                        - type: string
                        - type: integer
                        - type: number
                        - type: boolean
                    type: object
                    title: Metadata
              properties:
                allOf:
                  - $ref: '#/components/schemas/BenefitMeterCreditProperties'
            title: BenefitMeterCredit
            description: |-
              A benefit of type `meter_unit`.

              Use it to grant a number of units on a specific meter.
            refIdentifier: '#/components/schemas/BenefitMeterCredit'
            requiredProperties:
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
        examples:
          example:
            value:
              id: <string>
              created_at: '2023-11-07T05:31:56Z'
              modified_at: '2023-11-07T05:31:56Z'
              type: <string>
              description: <string>
              selectable: true
              deletable: true
              organization_id: <string>
              metadata: {}
              properties:
                note: <string>
        description: Successful Response
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    const: ResourceNotFound
                    title: Error
                    examples:
                      - ResourceNotFound
              detail:
                allOf:
                  - type: string
                    title: Detail
            title: ResourceNotFound
            refIdentifier: '#/components/schemas/ResourceNotFound'
            requiredProperties:
              - error
              - detail
        examples:
          example:
            value:
              error: ResourceNotFound
              detail: <string>
        description: Benefit not found.
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    type: array
                    title: Detail
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
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

````