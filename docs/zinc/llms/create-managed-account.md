# Source: https://zinc-staging.vercel.app/docs/v2/api-reference/managed-accounts/create-managed-account.md

> ## Documentation Index
> Fetch the complete documentation index at: https://zinc-staging.vercel.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Managed Account

> Create new retailer credentials

Create new retailer credentials for order processing. Credentials are encrypted and stored securely.

## Request Fields

* **email** (required) - The email address for the retailer account
* **password** - The password for the retailer account (encrypted at rest)
* **retailer** - Retailer name (e.g., `amazon`). If omitted, applies as default credentials
* **totp\_secret** - TOTP secret key for two-factor authentication (encrypted at rest)

<Info>
  If your retailer account has 2FA enabled, you must provide the `totp_secret` to avoid verification issues during order processing. See the [Managed Accounts guide](/v2/api-reference/configuration/managed-accounts#two-factor-authentication-totp) for details on finding your TOTP key.
</Info>

## Response

Returns the created credential object with:

* **id** - Unique identifier (UUID)
* **short\_id** - Short identifier used in URLs (e.g., `zn_acct_a1b2c3d4`)
* **email** - Retailer account email
* **retailer** - Retailer name, or null if default credentials
* **has\_totp** - Whether TOTP 2FA is configured
* **has\_forwarding** - Whether email forwarding has been verified
* **created\_at** - Creation timestamp
* **updated\_at** - Last update timestamp

<Warning>
  Passwords and TOTP secrets are never returned in API responses. The `has_totp` field indicates whether 2FA is configured.
</Warning>


## OpenAPI

````yaml versions/latest.json post /managed-accounts
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
    post:
      tags:
        - managed-accounts
      summary: Create Retailer Credentials
      description: Create new retailer credentials for the current user.
      operationId: create_retailer_credentials_managed_accounts_post
      parameters:
        - name: authorization
          in: header
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Authorization
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RetailerCredentialsCreate'
      responses:
        '201':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RetailerCredentialsResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    RetailerCredentialsCreate:
      properties:
        email:
          type: string
          title: Email
        password:
          anyOf:
            - type: string
            - type: 'null'
          title: Password
        retailer:
          anyOf:
            - type: string
            - type: 'null'
          title: Retailer
          description: >-
            Retailer name (e.g., 'amazon'). If null, applies as default
            credentials.
        totp_secret:
          anyOf:
            - type: string
            - type: 'null'
          title: Totp Secret
          description: TOTP secret key for 2FA (will be encrypted at rest).
        retailer_config:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Retailer Config
      type: object
      required:
        - email
      title: RetailerCredentialsCreate
      description: Request model for creating retailer credentials.
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
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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