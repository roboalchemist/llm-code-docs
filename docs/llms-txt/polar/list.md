# Source: https://polar.sh/docs/api-reference/webhooks/endpoints/list.md

# Source: https://polar.sh/docs/api-reference/subscriptions/list.md

# Source: https://polar.sh/docs/api-reference/refunds/list.md

# Source: https://polar.sh/docs/api-reference/products/list.md

# Source: https://polar.sh/docs/api-reference/organizations/list.md

# Source: https://polar.sh/docs/api-reference/orders/list.md

# Source: https://polar.sh/docs/api-reference/meters/list.md

# Source: https://polar.sh/docs/api-reference/license-keys/list.md

# Source: https://polar.sh/docs/api-reference/files/list.md

# Source: https://polar.sh/docs/api-reference/events/list.md

# Source: https://polar.sh/docs/api-reference/discounts/list.md

# Source: https://polar.sh/docs/api-reference/customers/list.md

# Source: https://polar.sh/docs/api-reference/customer-seats/list.md

# Source: https://polar.sh/docs/api-reference/customer-portal/subscriptions/list.md

# Source: https://polar.sh/docs/api-reference/customer-portal/seats/list.md

# Source: https://polar.sh/docs/api-reference/customer-portal/orders/list.md

# Source: https://polar.sh/docs/api-reference/customer-portal/license-keys/list.md

# Source: https://polar.sh/docs/api-reference/customer-portal/downloadables/list.md

# Source: https://polar.sh/docs/api-reference/customer-meters/list.md

# Source: https://polar.sh/docs/api-reference/custom-fields/list.md

# Source: https://polar.sh/docs/api-reference/checkout-links/list.md

# Source: https://polar.sh/docs/api-reference/benefits/list.md

# Source: https://polar.sh/docs/api-reference/checkout-links/list.md

# Source: https://polar.sh/docs/api-reference/benefits/list.md

# Source: https://polar.sh/docs/api-reference/webhooks/endpoints/list.md

# Source: https://polar.sh/docs/api-reference/subscriptions/list.md

# Source: https://polar.sh/docs/api-reference/refunds/list.md

# Source: https://polar.sh/docs/api-reference/products/list.md

# Source: https://polar.sh/docs/api-reference/organizations/list.md

# Source: https://polar.sh/docs/api-reference/orders/list.md

# Source: https://polar.sh/docs/api-reference/meters/list.md

# Source: https://polar.sh/docs/api-reference/license-keys/list.md

# Source: https://polar.sh/docs/api-reference/files/list.md

# Source: https://polar.sh/docs/api-reference/events/list.md

# Source: https://polar.sh/docs/api-reference/discounts/list.md

# Source: https://polar.sh/docs/api-reference/customers/list.md

# Source: https://polar.sh/docs/api-reference/customer-seats/list.md

# Source: https://polar.sh/docs/api-reference/customer-portal/subscriptions/list.md

# Source: https://polar.sh/docs/api-reference/customer-portal/seats/list.md

# Source: https://polar.sh/docs/api-reference/customer-portal/orders/list.md

# Source: https://polar.sh/docs/api-reference/customer-portal/license-keys/list.md

# Source: https://polar.sh/docs/api-reference/customer-portal/downloadables/list.md

# Source: https://polar.sh/docs/api-reference/customer-meters/list.md

# Source: https://polar.sh/docs/api-reference/custom-fields/list.md

# Source: https://polar.sh/docs/api-reference/checkout-links/list.md

# Source: https://polar.sh/docs/api-reference/benefits/list.md

# List Benefits

> List benefits.

**Scopes**: `benefits:read` `benefits:write`

## OpenAPI

````yaml get /v1/benefits/
paths:
  path: /v1/benefits/
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
      path: {}
      query:
        organization_id:
          schema:
            - type: string
              required: false
              title: OrganizationID Filter
              description: |-
                Filter by organization ID.
                The organization ID.
              examples:
                - 1dbfc517-0bbf-4301-9ba8-555ca42b9737
              format: uuid4
              example: 1dbfc517-0bbf-4301-9ba8-555ca42b9737
            - type: array
              items:
                allOf:
                  - type: string
                    format: uuid4
                    examples:
                      - 1dbfc517-0bbf-4301-9ba8-555ca42b9737
                    description: The organization ID.
                    x-polar-selector-widget:
                      resourceRoot: /v1/organizations
                      resourceName: Organization
                      displayProperty: name
              required: false
              title: OrganizationID Filter
              description: Filter by organization ID.
            - type: 'null'
              required: false
              title: OrganizationID Filter
              description: Filter by organization ID.
        type:
          schema:
            - type: enum<string>
              enum:
                - custom
                - discord
                - github_repository
                - downloadables
                - license_keys
                - meter_credit
              required: false
              title: BenefitType
              description: Filter by benefit type.
              refIdentifier: '#/components/schemas/BenefitType'
            - type: array
              items:
                allOf:
                  - $ref: '#/components/schemas/BenefitType'
              required: false
              title: BenefitType Filter
              description: Filter by benefit type.
            - type: 'null'
              required: false
              title: BenefitType Filter
              description: Filter by benefit type.
        query:
          schema:
            - type: string
              required: false
              title: Query
              description: Filter by description.
            - type: 'null'
              required: false
              title: Query
              description: Filter by description.
        page:
          schema:
            - type: integer
              required: false
              title: Page
              description: Page number, defaults to 1.
              minimum: 0
              exclusiveMinimum: true
              default: 1
        limit:
          schema:
            - type: integer
              required: false
              title: Limit
              description: Size of a page, defaults to 10. Maximum is 100.
              minimum: 0
              exclusiveMinimum: true
              default: 10
        sorting:
          schema:
            - type: array
              items:
                allOf:
                  - $ref: '#/components/schemas/BenefitSortProperty'
              required: false
              title: Sorting
              description: >-
                Sorting criterion. Several criteria can be used simultaneously
                and will be applied in order. Add a minus sign `-` before the
                criteria name to sort by descending order.
              default: &ref_0
                - '-created_at'
            - type: 'null'
              required: false
              title: Sorting
              description: >-
                Sorting criterion. Several criteria can be used simultaneously
                and will be applied in order. Add a minus sign `-` before the
                criteria name to sort by descending order.
              default: *ref_0
        metadata:
          schema:
            - type: object
              properties: {}
              required: false
              title: MetadataQuery
              description: >-
                Filter by metadata key-value pairs. It uses the `deepObject`
                style, e.g. `?metadata[key]=value`.
              additionalProperties:
                allOf:
                  - anyOf:
                      - type: string
                      - type: integer
                      - type: boolean
                      - type: array
                        items:
                          type: string
                      - type: array
                        items:
                          type: integer
                      - type: array
                        items:
                          type: boolean
            - type: 'null'
              required: false
              title: MetadataQuery
              description: >-
                Filter by metadata key-value pairs. It uses the `deepObject`
                style, e.g. `?metadata[key]=value`.
          style: deepObject
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\t\"os\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"github.com/polarsource/polar-go/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New(\n        polargo.WithSecurity(os.Getenv(\"POLAR_ACCESS_TOKEN\")),\n    )\n\n    res, err := s.Benefits.List(ctx, operations.BenefitsListRequest{\n        OrganizationID: polargo.Pointer(operations.CreateQueryParamOrganizationIDFilterStr(\n            \"1dbfc517-0bbf-4301-9ba8-555ca42b9737\",\n        )),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.ListResourceBenefit != nil {\n        for {\n            // handle items\n\n            res, err = res.Next()\n\n            if err != nil {\n                // handle error\n            }\n\n            if res == nil {\n                break\n            }\n        }\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          from polar_sdk import Polar


          with Polar(
              access_token="<YOUR_BEARER_TOKEN_HERE>",
          ) as polar:

              res = polar.benefits.list(organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737", page=1, limit=10)

              while res is not None:
                  # Handle items

                  res = res.next()
      - label: Typescript (SDK)
        lang: typescript
        source: |-
          import { Polar } from "@polar-sh/sdk";

          const polar = new Polar({
            accessToken: process.env["POLAR_ACCESS_TOKEN"] ?? "",
          });

          async function run() {
            const result = await polar.benefits.list({
              organizationId: "1dbfc517-0bbf-4301-9ba8-555ca42b9737",
            });

            for await (const page of result) {
              console.log(page);
            }
          }

          run();
      - label: PHP (SDK)
        lang: php
        source: |-
          declare(strict_types=1);

          require 'vendor/autoload.php';

          use Polar;
          use Polar\Models\Operations;

          $sdk = Polar\Polar::builder()
              ->setSecurity(
                  '<YOUR_BEARER_TOKEN_HERE>'
              )
              ->build();

          $request = new Operations\BenefitsListRequest(
              organizationId: '1dbfc517-0bbf-4301-9ba8-555ca42b9737',
          );

          $responses = $sdk->benefits->list(
              request: $request
          );


          foreach ($responses as $response) {
              if ($response->statusCode === 200) {
                  // handle response
              }
          }
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              items:
                allOf:
                  - items:
                      $ref: '#/components/schemas/Benefit'
                      title: Benefit
                    type: array
                    title: Items
              pagination:
                allOf:
                  - $ref: '#/components/schemas/Pagination'
            title: ListResource[Benefit]
            refIdentifier: '#/components/schemas/ListResource_Benefit_'
            requiredProperties:
              - items
              - pagination
        examples:
          example:
            value:
              items:
                - id: <string>
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
              pagination:
                total_count: 123
                max_page: 123
        description: Successful Response
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
    Benefit:
      anyOf:
        - $ref: '#/components/schemas/BenefitCustom'
        - $ref: '#/components/schemas/BenefitDiscord'
        - $ref: '#/components/schemas/BenefitGitHubRepository'
        - $ref: '#/components/schemas/BenefitDownloadables'
        - $ref: '#/components/schemas/BenefitLicenseKeys'
        - $ref: '#/components/schemas/BenefitMeterCredit'
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
          additionalProperties:
            anyOf:
              - type: string
              - type: integer
              - type: number
              - type: boolean
          type: object
          title: Metadata
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
          additionalProperties:
            anyOf:
              - type: string
              - type: integer
              - type: number
              - type: boolean
          type: object
          title: Metadata
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
          additionalProperties:
            anyOf:
              - type: string
              - type: integer
              - type: number
              - type: boolean
          type: object
          title: Metadata
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
          additionalProperties:
            anyOf:
              - type: string
              - type: integer
              - type: number
              - type: boolean
          type: object
          title: Metadata
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
          additionalProperties:
            anyOf:
              - type: string
              - type: integer
              - type: number
              - type: boolean
          type: object
          title: Metadata
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
          additionalProperties:
            anyOf:
              - type: string
              - type: integer
              - type: number
              - type: boolean
          type: object
          title: Metadata
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
    BenefitSortProperty:
      type: string
      enum:
        - created_at
        - '-created_at'
        - description
        - '-description'
        - type
        - '-type'
      title: BenefitSortProperty
    BenefitType:
      type: string
      enum:
        - custom
        - discord
        - github_repository
        - downloadables
        - license_keys
        - meter_credit
      title: BenefitType
    Pagination:
      properties:
        total_count:
          type: integer
          title: Total Count
        max_page:
          type: integer
          title: Max Page
      type: object
      required:
        - total_count
        - max_page
      title: Pagination
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