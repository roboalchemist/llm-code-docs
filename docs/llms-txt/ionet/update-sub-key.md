# Source: https://io.net/docs/reference/sub-keys/update-sub-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Sub-API Key

> Updates one or more attributes of an existing sub-API key. Omitted fields are left unchanged.

All body fields are optional — only the fields you include will be updated.

### Unblocking an over-limit key

When a sub-key's `credit_used` exceeds its `credit_limit`, the key is automatically blocked (returns **429 Too Many Requests** on inference calls). To unblock it without waiting for the next cycle reset, raise the `credit_limit` via this endpoint:

```bash  theme={null}
curl -X PATCH "https://api.intelligence.io.solutions/v1/api-keys/sub-keys/{key_id}" \
  -H "x-api-key: $ADMIN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"credit_limit": 50.0}'
```

### Clearing model restrictions

Pass an empty array for `allowed_models` to remove all model restrictions, giving the sub-key access to all models available to the admin:

```json  theme={null}
{ "allowed_models": [] }
```


## OpenAPI

````yaml openapi/sub-keys/update-sub-key.json patch /v1/api-keys/sub-keys/{key_id}
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.io.solutions
security:
  - sec0: []
paths:
  /v1/api-keys/sub-keys/{key_id}:
    patch:
      tags:
        - Sub-API Keys
      summary: Update Sub-API Key
      description: >-
        Updates one or more attributes of an existing sub-API key. Only the
        fields included in the request body are modified — omitted fields retain
        their current values. Pass an empty array for `allowed_models` to remove
        all model restrictions.
      operationId: update_sub_key
      parameters:
        - name: key_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Key ID
          description: UUID of the sub-key to update.
        - name: x-api-key
          in: header
          required: true
          schema:
            type: string
            description: Admin API key (io.net Intelligence)
            title: X-Api-Key
          description: Admin API key that owns the sub-key.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateSubKeyRequest'
      responses:
        '200':
          description: Sub-key updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
              example:
                status: succeeded
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
    UpdateSubKeyRequest:
      type: object
      title: UpdateSubKeyRequest
      description: All fields are optional. Only provided fields are updated.
      properties:
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          default: null
        allowed_models:
          anyOf:
            - type: array
              items:
                type: string
              description: >-
                New model allow-list. Pass an empty array [] to remove all
                restrictions.
            - type: 'null'
          title: Allowed Models
          default: null
        credit_limit:
          anyOf:
            - type: number
              minimum: 0
            - type: 'null'
          title: Credit Limit
          description: >-
            New per-cycle credit cap. Set to a higher value to unblock a key
            that has exceeded its limit.
          default: null
        credit_refresh_cycle:
          anyOf:
            - type: string
              enum:
                - 8h
                - daily
                - weekly
                - monthly
            - type: 'null'
          title: Credit Refresh Cycle
          default: null
        expires_at:
          anyOf:
            - type: string
              format: date-time
            - type: string
              enum:
                - never
            - type: 'null'
          title: Expires At
          default: null
    SuccessResponse:
      type: object
      title: SuccessResponse
      properties:
        status:
          type: string
          example: succeeded
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
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````