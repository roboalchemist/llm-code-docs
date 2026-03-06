# Source: https://io.net/docs/reference/sub-keys/get-key-usage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Sub-Key Usage

> Returns credit status for a specific sub-key: credits used in the current billing period, the configured limit, and remaining allowance.

Use this endpoint to monitor whether a specific sub-key is approaching or has exceeded its credit limit.

The `remaining_credit` field is `null` when no `credit_limit` has been configured for the key — in that case, the key is only bounded by the admin's overall account balance.

<Note>
  Credit usage reflects **settled** payments processed by the billing pipeline. There may be a short lag (typically under a minute) between a completed inference call and the usage appearing here.
</Note>


## OpenAPI

````yaml openapi/sub-keys/get-key-usage.json get /v1/api-keys/sub-keys/{key_id}/usage
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.io.solutions
security:
  - sec0: []
paths:
  /v1/api-keys/sub-keys/{key_id}/usage:
    get:
      tags:
        - Sub-API Keys
      summary: Get Sub-Key Usage
      description: >-
        Returns the credit status for a specific sub-key: how much has been
        consumed in the current billing period, the configured limit, and the
        remaining allowance.
      operationId: get_key_usage
      parameters:
        - name: key_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Key ID
          description: UUID of the sub-key to inspect.
        - name: x-api-key
          in: header
          required: true
          schema:
            type: string
            description: Admin API key (io.net Intelligence)
            title: X-Api-Key
          description: Admin API key that owns the sub-key.
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/KeyUsageResponse'
              example:
                status: succeeded
                data:
                  key_id: 71775d2e-fbcc-4ef4-aa30-8aaeb82062c0
                  credit_used: 1.234
                  credit_limit: 10
                  remaining_credit: 8.766
                  credit_refresh_cycle: monthly
        '401':
          description: Unauthorized — invalid or missing API key
        '404':
          description: Sub-API key not found or not owned by this admin
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    KeyUsageResponse:
      type: object
      title: KeyUsageResponse
      properties:
        status:
          type: string
          example: succeeded
        data:
          $ref: '#/components/schemas/KeyUsageData'
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    KeyUsageData:
      type: object
      title: KeyUsageData
      properties:
        key_id:
          type: string
          format: uuid
          title: Key ID
        credit_used:
          type: number
          title: Credit Used
          description: Credits consumed in the current billing period.
        credit_limit:
          anyOf:
            - type: number
            - type: 'null'
          title: Credit Limit
          description: Maximum credits allowed per cycle. Null if no per-key limit is set.
        remaining_credit:
          anyOf:
            - type: number
            - type: 'null'
          title: Remaining Credit
          description: >-
            Credits remaining before the key is blocked. Null if no limit is
            configured.
        credit_refresh_cycle:
          type: string
          enum:
            - 8h
            - daily
            - weekly
            - monthly
          title: Credit Refresh Cycle
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
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````