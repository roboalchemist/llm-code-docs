# Source: https://io.net/docs/reference/sub-keys/create-sub-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Sub-API Key

> Creates a new sub-API key scoped under an admin key, with optional model restrictions and per-key credit limits.

<Note>
  The full key `value` is returned **only once** at creation time. Store it securely — it cannot be retrieved again. Only the truncated `display` string is stored and returned in subsequent list or usage calls.
</Note>

<Note>
  Only admin API keys can create sub-keys. A sub-key cannot create further sub-keys. If you authenticate with a sub-key, the endpoint returns **403 Forbidden**.
</Note>

### Key fields

* `description` – A human-readable label to identify the key's purpose or owner.

* `allowed_models` – An optional list of model identifiers (e.g. `"meta-llama/Llama-3.3-70B-Instruct"`) that this sub-key is permitted to call. If omitted, all models available to the admin are accessible. Requests to unlisted models are rejected with **403 Forbidden**.

* `credit_limit` – Maximum IO Intelligence credits the sub-key may consume per refresh cycle. Once the limit is reached the key is automatically blocked until the cycle resets or the admin raises the limit via `PATCH`. Set to `null` to impose no per-key cap.

* `credit_refresh_cycle` – How often the usage counter resets: `"8h"`, `"daily"`, `"weekly"`, or `"monthly"` (default).

* `expires_at` – ISO 8601 date-time for key expiry, or the literal string `"never"` for a non-expiring key. Defaults to 180 days from creation when omitted.

* `key_prefix` – An optional lowercase slug (2–8 chars) prepended to the generated key value (e.g. `"acme"` produces `acme-v2-eyJ...`). Defaults to the standard `io-v2` prefix when omitted. Cannot start with `"io"` or contain version markers like `"-v2"`.


## OpenAPI

````yaml openapi/sub-keys/create-sub-key.json post /v1/api-keys/sub-keys
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
    post:
      tags:
        - Sub-API Keys
      summary: Create Sub-API Key
      description: >-
        Creates a new sub-API key scoped under the authenticated admin key. The
        sub-key inherits the admin's credit pool and can be further restricted
        by allowed models and a per-key credit limit.
      operationId: create_sub_key
      parameters:
        - name: x-api-key
          in: header
          required: true
          schema:
            type: string
            description: Admin API key (io.net Intelligence)
            title: X-Api-Key
          description: >-
            Admin API key with full access. Sub-keys created by this key inherit
            its credit pool.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateSubKeyRequest'
      responses:
        '201':
          description: Sub-API key created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateSubKeyResponse'
              example:
                status: succeeded
                data:
                  key_id: 71775d2e-fbcc-4ef4-aa30-8aaeb82062c0
                  value: acme-v2-eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
                  display: acme-v2-eyJh...c0eQ
                  admin_user_id: 95ce9361-447f-4ec0-a698-764c2a2d15b9
                  description: Partner integration key
                  allowed_models:
                    - meta-llama/Llama-3.3-70B-Instruct
                  credit_limit: 10
                  credit_refresh_cycle: monthly
                  expires_at: '2026-08-20T00:00:00'
        '401':
          description: Unauthorized — invalid or missing API key
        '403':
          description: >-
            Forbidden — the provided key is a sub-key and cannot create further
            sub-keys
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    CreateSubKeyRequest:
      type: object
      required:
        - description
      title: CreateSubKeyRequest
      properties:
        description:
          type: string
          title: Description
          description: A human-readable label for the sub-key.
        scopes:
          anyOf:
            - type: array
              items:
                type: string
            - type: 'null'
          title: Scopes
          description: Access scopes. Defaults to ["intelligence"] if omitted.
          default: null
        allowed_models:
          anyOf:
            - type: array
              items:
                type: string
              description: >-
                List of model identifiers this sub-key is permitted to use. If
                omitted, all models available to the admin are allowed.
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
            Maximum credits (in IO Intelligence credits) the sub-key may consume
            per refresh cycle. Null means no per-key limit — the admin's overall
            balance applies.
          default: null
        credit_refresh_cycle:
          type: string
          enum:
            - 8h
            - daily
            - weekly
            - monthly
          title: Credit Refresh Cycle
          description: >-
            How often the sub-key's credit_used counter resets. Defaults to
            "monthly".
          default: monthly
        expires_at:
          anyOf:
            - type: string
              format: date-time
            - type: string
              enum:
                - never
            - type: 'null'
          title: Expires At
          description: >-
            Expiry date-time for the key. Pass "never" for a non-expiring key.
            Defaults to 180 days from creation if omitted.
          default: null
        key_prefix:
          anyOf:
            - type: string
              minLength: 2
              maxLength: 8
              pattern: ^[a-z][a-z0-9-]*[a-z0-9]$
              description: >-
                Custom lowercase slug prepended to the key (e.g. "acme" produces
                "acme-v2-..."). Must be 2–8 lowercase alphanumeric characters
                with optional internal hyphens. Cannot start with "io"
                (reserved) or contain version markers such as "-v2".
            - type: 'null'
          title: Key Prefix
          description: >-
            Optional prefix slug for the generated key. Defaults to the standard
            "io-v2" prefix when omitted.
          default: null
    CreateSubKeyResponse:
      type: object
      title: CreateSubKeyResponse
      properties:
        status:
          type: string
          example: succeeded
        data:
          $ref: '#/components/schemas/SubKeyCreated'
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    SubKeyCreated:
      type: object
      title: SubKeyCreated
      properties:
        key_id:
          type: string
          format: uuid
          title: Key ID
        value:
          type: string
          title: Value
          description: >-
            The full API key string. This is shown only once — store it
            securely.
        display:
          type: string
          title: Display
          description: >-
            A truncated, safe-to-display version of the key (e.g.
            "acme-v2-eyJh...c0eQ").
        admin_user_id:
          type: string
          format: uuid
          title: Admin User ID
        description:
          type: string
          title: Description
        allowed_models:
          anyOf:
            - type: array
              items:
                type: string
            - type: 'null'
          title: Allowed Models
        credit_limit:
          anyOf:
            - type: number
            - type: 'null'
          title: Credit Limit
        credit_refresh_cycle:
          type: string
          title: Credit Refresh Cycle
        expires_at:
          type: string
          title: Expires At
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