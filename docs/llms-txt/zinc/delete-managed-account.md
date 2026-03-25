# Source: https://zinc-staging.vercel.app/docs/v2/api-reference/managed-accounts/delete-managed-account.md

> ## Documentation Index
> Fetch the complete documentation index at: https://zinc-staging.vercel.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Managed Account

> Delete retailer credentials

Permanently delete retailer credentials. This action cannot be undone.

## Path Parameters

* **short\_id** (required) - The short identifier of the credentials to delete (e.g., `zn_acct_a1b2c3d4`)

<Warning>
  Deleting credentials that are actively in use by a processing order may cause the order to fail. Ensure no orders are currently processing with these credentials before deleting.
</Warning>


## OpenAPI

````yaml versions/latest.json delete /managed-accounts/{short_id}
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
    delete:
      tags:
        - managed-accounts
      summary: Delete Retailer Credentials
      description: Delete retailer credentials for the current user.
      operationId: delete_retailer_credentials_managed_accounts__short_id__delete
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
      responses:
        '204':
          description: Successful Response
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
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