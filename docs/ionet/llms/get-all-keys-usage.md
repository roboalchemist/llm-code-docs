# Source: https://io.net/docs/reference/sub-keys/get-all-keys-usage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get All Sub-Keys Usage

> Returns aggregated token usage and credit cost for every sub-key owned by the admin, broken down by model for today and all time.

This endpoint is designed for admin-level billing dashboards. It returns a breakdown per sub-key, with each entry showing:

* **`today`** — token consumption and credit cost since midnight UTC.
* **`all_time`** — cumulative consumption since the sub-key was created.
* **`totals`** — aggregate `today_credit_cost` and `all_time_credit_cost` across all sub-keys.

Each entry's `models` array shows which models were used and their individual costs, allowing you to see exactly where credits are being spent.

<Note>
  This endpoint requires the Intelligence database to be reachable. It returns **503 Service Unavailable** if the intelligence database is temporarily unavailable.
</Note>


## OpenAPI

````yaml openapi/sub-keys/get-all-keys-usage.json get /v1/api-keys/sub-keys/usage
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.io.solutions
security:
  - sec0: []
paths:
  /v1/api-keys/sub-keys/usage:
    get:
      tags:
        - Sub-API Keys
      summary: Get All Sub-Keys Usage
      description: >-
        Returns token consumption and credit cost for every sub-key owned by the
        authenticated admin, broken down by model for both today and all time.
      operationId: get_all_keys_usage
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
                $ref: '#/components/schemas/AllKeysUsageResponse'
              example:
                status: succeeded
                data:
                  keys:
                    - api_key_id: 71775d2e-fbcc-4ef4-aa30-8aaeb82062c0
                      description: Partner integration key
                      display: acme-v2-eyJh...c0eQ
                      today:
                        models:
                          - model_name: meta-llama/Llama-3.3-70B-Instruct
                            input_tokens: 1500
                            output_tokens: 320
                            credit_cost: 0.000024
                        total_input_tokens: 1500
                        total_output_tokens: 320
                        total_credit_cost: 0.000024
                      all_time:
                        models:
                          - model_name: meta-llama/Llama-3.3-70B-Instruct
                            input_tokens: 48000
                            output_tokens: 12000
                            credit_cost: 0.000834
                        total_input_tokens: 48000
                        total_output_tokens: 12000
                        total_credit_cost: 0.000834
                  totals:
                    today_credit_cost: 0.000024
                    all_time_credit_cost: 0.000834
        '401':
          description: Unauthorized — invalid or missing API key
        '503':
          description: Intelligence database unavailable
components:
  schemas:
    AllKeysUsageResponse:
      type: object
      title: AllKeysUsageResponse
      properties:
        status:
          type: string
          example: succeeded
        data:
          $ref: '#/components/schemas/AllKeysUsageData'
    AllKeysUsageData:
      type: object
      title: AllKeysUsageData
      properties:
        keys:
          type: array
          items:
            $ref: '#/components/schemas/KeyUsageEntry'
          title: Keys
        totals:
          $ref: '#/components/schemas/UsageTotals'
    KeyUsageEntry:
      type: object
      title: KeyUsageEntry
      properties:
        api_key_id:
          type: string
          format: uuid
          title: API Key ID
        description:
          type: string
          title: Description
        display:
          type: string
          title: Display
        today:
          $ref: '#/components/schemas/UsagePeriod'
          title: Today
        all_time:
          $ref: '#/components/schemas/UsagePeriod'
          title: All Time
    UsageTotals:
      type: object
      title: UsageTotals
      properties:
        today_credit_cost:
          type: number
          title: Today Credit Cost
        all_time_credit_cost:
          type: number
          title: All Time Credit Cost
    UsagePeriod:
      type: object
      title: UsagePeriod
      properties:
        models:
          type: array
          items:
            $ref: '#/components/schemas/ModelUsageBreakdown'
          title: Models
        total_input_tokens:
          type: integer
          title: Total Input Tokens
        total_output_tokens:
          type: integer
          title: Total Output Tokens
        total_credit_cost:
          type: number
          title: Total Credit Cost
    ModelUsageBreakdown:
      type: object
      title: ModelUsageBreakdown
      properties:
        model_name:
          type: string
          title: Model Name
        input_tokens:
          type: integer
          title: Input Tokens
        output_tokens:
          type: integer
          title: Output Tokens
        credit_cost:
          type: number
          title: Credit Cost
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````