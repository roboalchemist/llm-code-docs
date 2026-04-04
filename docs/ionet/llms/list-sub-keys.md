# Source: https://io.net/docs/reference/sub-keys/list-sub-keys.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Sub-API Keys

> Returns all active sub-API keys owned by the authenticated admin key, including current-period credit usage for each key.

The response includes one entry per active sub-key with the following credit fields:

* `credit_limit` — the per-cycle cap configured for the key (`null` means no per-key cap).
* `credit_used` — credits consumed so far in the **current** billing period (resets according to `credit_refresh_cycle`).

<Note>
  Expired or revoked keys are not included in this list.
</Note>


## OpenAPI

````yaml openapi/sub-keys/list-sub-keys.json get /v1/api-keys/sub-keys
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.io.solutions
security:
  - sec0: []
paths:
  /v1/api-keys/sub-keys:
    get:
      tags:
        - Sub-API Keys
      summary: List Sub-API Keys
      description: >-
        Returns all active sub-API keys created by the authenticated admin key,
        along with each key's current credit usage for the active billing
        period.
      operationId: list_sub_keys
      parameters:
        - name: x-api-key
          in: header
          required: true
          schema:
            type: string
            description: Admin API key (io.net Intelligence)
            title: X-Api-Key
          description: Admin API key.
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListSubKeysResponse'
              example:
                status: succeeded
                data:
                  - id: 71775d2e-fbcc-4ef4-aa30-8aaeb82062c0
                    description: Partner integration key
                    display: acme-v2-eyJh...c0eQ
                    created_at: '2026-02-20T10:00:00'
                    expires_at: '2026-08-20T00:00:00'
                    expired: false
                    allowed_models:
                      - meta-llama/Llama-3.3-70B-Instruct
                    credit_limit: 10
                    credit_used: 1.234
                    credit_refresh_cycle: monthly
        '401':
          description: Unauthorized — invalid or missing API key
components:
  schemas:
    ListSubKeysResponse:
      type: object
      title: ListSubKeysResponse
      properties:
        status:
          type: string
          example: succeeded
        data:
          type: array
          items:
            $ref: '#/components/schemas/SubKeyItem'
          title: Data
    SubKeyItem:
      type: object
      title: SubKeyItem
      properties:
        id:
          type: string
          format: uuid
          title: ID
          description: Unique identifier of the sub-key.
        description:
          type: string
          title: Description
        display:
          type: string
          title: Display
          description: Truncated key value safe to display in UIs.
        created_at:
          type: string
          format: date-time
          title: Created At
        expires_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Expires At
        expired:
          type: boolean
          title: Expired
        allowed_models:
          anyOf:
            - type: array
              items:
                type: string
            - type: 'null'
          title: Allowed Models
          description: Model allow-list. Null means all models are permitted.
        credit_limit:
          anyOf:
            - type: number
            - type: 'null'
          title: Credit Limit
          description: Per-cycle credit cap. Null means no per-key limit.
        credit_used:
          type: number
          title: Credit Used
          description: Credits consumed in the current refresh period.
        credit_refresh_cycle:
          type: string
          enum:
            - 8h
            - daily
            - weekly
            - monthly
          title: Credit Refresh Cycle
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````