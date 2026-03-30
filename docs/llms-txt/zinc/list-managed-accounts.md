# Source: https://zinc-staging.vercel.app/docs/v2/api-reference/managed-accounts/list-managed-accounts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://zinc-staging.vercel.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Managed Accounts

> List all retailer credentials for your account

Retrieve a list of all retailer credentials associated with your account.

## Response

Returns an object containing:

* **credentials** - Array of retailer credential objects
* **total** - Total number of credentials

Each credential includes:

* **id** - Unique identifier (UUID)
* **short\_id** - Short identifier used in URLs (e.g., `zn_acct_a1b2c3d4`)
* **email** - Retailer account email
* **retailer** - Retailer name, or null if default credentials
* **has\_totp** - Whether TOTP 2FA is configured
* **has\_forwarding** - Whether email forwarding has been verified
* **created\_at** - When the credentials were created
* **updated\_at** - When the credentials were last updated


## OpenAPI

````yaml versions/latest.json get /managed-accounts
openapi: 3.1.0
info:
  title: 'Zinc '
  summary: >-
    Zinc lets you search, buy, and return items from top online retailers with a
    single API.
  version: '2026-02-19'
  x-logo:
    url: https://mintlify.s3.us-west-1.amazonaws.com/zinc/logo/light.png
servers:
  - url: https://api.zinc.com
    description: Production
security: []
paths:
  /managed-accounts:
    get:
      tags:
        - managed-accounts
      summary: List Retailer Credentials
      description: List all retailer credentials for the current user.
      operationId: list_retailer_credentials_managed_accounts_get
      parameters:
        - name: authorization
          in: header
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Authorization
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RetailerCredentialsListResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    RetailerCredentialsListResponse:
      properties:
        credentials:
          items:
            $ref: '#/components/schemas/RetailerCredentialsResponse'
          type: array
          title: Credentials
        total:
          type: integer
          title: Total
      type: object
      required:
        - credentials
        - total
      title: RetailerCredentialsListResponse
      description: Response model for list of retailer credentials.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    RetailerCredentialsResponse:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        short_id:
          type: string
          title: Short Id
        email:
          type: string
          title: Email
        retailer:
          anyOf:
            - type: string
            - type: 'null'
          title: Retailer
        has_totp:
          type: boolean
          title: Has Totp
          description: Whether TOTP 2FA is configured for this account.
          default: false
        has_forwarding:
          type: boolean
          title: Has Forwarding
          description: Whether email forwarding has been verified for this account.
          default: false
        retailer_config:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Retailer Config
        forwarding_email:
          type: string
          title: Forwarding Email
          description: >-
            Email address to forward retailer emails to for verification and 2FA
            code extraction.
        created_at:
          type: string
          format: date-time
          title: Created At
        updated_at:
          type: string
          format: date-time
          title: Updated At
      type: object
      required:
        - id
        - short_id
        - email
        - retailer
        - forwarding_email
        - created_at
        - updated_at
      title: RetailerCredentialsResponse
      description: Response model for retailer credentials.
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

Built with [Mintlify](https://mintlify.com).