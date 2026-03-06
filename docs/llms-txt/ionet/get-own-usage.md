# Source: https://io.net/docs/reference/sub-keys/get-own-usage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Own Usage (Sub-Key Self-Service)

> Allows a sub-key to check its own credit status without exposing the admin key to the sub-key holder.

This endpoint is authenticated with the **sub-key itself**, not the admin key. It is intended for scenarios where sub-key holders need to monitor their own remaining credits programmatically.

<Note>
  Authenticating with an admin key returns **403 Forbidden**. Use `GET /v1/api-keys/sub-keys/{key_id}/usage` with the admin key to inspect a specific sub-key's status.
</Note>

### Typical use case

A service that holds a sub-key can call this endpoint periodically to determine how much credit remains before being blocked:

```bash  theme={null}
curl "https://api.intelligence.io.solutions/v1/api-keys/sub-keys/me/usage" \
  -H "x-api-key: $SUB_API_KEY"
```

```json  theme={null}
{
  "status": "succeeded",
  "data": {
    "key_id": "71775d2e-fbcc-4ef4-aa30-8aaeb82062c0",
    "credit_used": 7.82,
    "credit_limit": 10.0,
    "remaining_credit": 2.18,
    "credit_refresh_cycle": "monthly"
  }
}
```


## OpenAPI

````yaml openapi/sub-keys/get-own-usage.json get /v1/api-keys/sub-keys/me/usage
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.io.solutions
security:
  - sec0: []
paths:
  /v1/api-keys/sub-keys/me/usage:
    get:
      tags:
        - Sub-API Keys
      summary: Get Own Usage (Sub-Key Self-Service)
      description: >-
        Allows a sub-key to check its own credit status without requiring the
        admin key. This endpoint is intended for sub-key holders who need to
        monitor their own consumption. Admin keys are not accepted here — use
        `GET /v1/api-keys/sub-keys/{key_id}/usage` instead.
      operationId: get_own_usage
      parameters:
        - name: x-api-key
          in: header
          required: true
          schema:
            type: string
            description: Sub-API key
            title: X-Api-Key
          description: The sub-API key itself (not the admin key).
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
        '403':
          description: Forbidden — admin keys must use GET /{key_id}/usage instead
        '404':
          description: Sub-API key not found
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
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````