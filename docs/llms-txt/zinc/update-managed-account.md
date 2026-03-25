# Source: https://zinc-staging.vercel.app/docs/v2/api-reference/managed-accounts/update-managed-account.md

> ## Documentation Index
> Fetch the complete documentation index at: https://zinc-staging.vercel.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Managed Account

> Update existing retailer credentials

Update an existing managed account's retailer credentials. Only provided fields are updated.

## Path Parameters

* **short\_id** (required) - The short identifier of the credentials to update (e.g., `zn_acct_a1b2c3d4`)

## Request Fields

All fields are optional. Only provided fields are updated.

* **email** - New email address
* **password** - New password (encrypted at rest)
* **retailer** - New retailer association
* **totp\_secret** - Update the 2FA secret key (encrypted at rest)

## Response

Returns the updated credential object.


## OpenAPI

````yaml versions/latest.json put /managed-accounts/{short_id}
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
  /managed-accounts/{short_id}:
    put:
      tags:
        - managed-accounts
      summary: Update Retailer Credentials
      description: Update retailer credentials for the current user.
      operationId: update_retailer_credentials_managed_accounts__short_id__put
      parameters:
        - name: short_id
          in: path
          required: true
          schema:
            type: string
            title: Short Id
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
              $ref: '#/components/schemas/RetailerCredentialsUpdate'
      responses:
        '200':
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
    RetailerCredentialsUpdate:
      properties:
        email:
          anyOf:
            - type: string
            - type: 'null'
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
        totp_secret:
          anyOf:
            - type: string
            - type: 'null'
          title: Totp Secret
        retailer_config:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Retailer Config
      type: object
      title: RetailerCredentialsUpdate
      description: Request model for updating retailer credentials.
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