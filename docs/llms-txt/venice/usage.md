# Source: https://docs.venice.ai/api-reference/endpoint/billing/usage.md

# Billing Usage API (Beta)

> Get paginated billing usage data for the authenticated user. NOTE: This is a beta endpoint and may be subject to change.

## OpenAPI

````yaml GET /billing/usage
paths:
  path: /billing/usage
  method: get
  servers:
    - url: https://api.venice.ai/api/v1
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path: {}
      query:
        currency:
          schema:
            - type: enum<string>
              enum:
                - USD
                - VCU
                - DIEM
              required: false
              description: Filter by currency
              example: USD
        endDate:
          schema:
            - type: string
              required: false
              description: End date for filtering records (ISO 8601)
              format: date-time
              example: '2024-12-31T23:59:59.000Z'
        limit:
          schema:
            - type: integer
              required: false
              description: Number of items per page
              maximum: 500
              minimum: 0
              exclusiveMinimum: true
              default: 200
              example: 200
        page:
          schema:
            - type: integer
              required: false
              description: Page number for pagination
              minimum: 0
              exclusiveMinimum: true
              default: 1
              example: 1
        sortOrder:
          schema:
            - type: enum<string>
              enum:
                - asc
                - desc
              required: false
              description: Sort order for createdAt field
              default: desc
              example: desc
        startDate:
          schema:
            - type: string
              required: false
              description: Start date for filtering records (ISO 8601)
              format: date-time
              example: '2024-01-01T00:00:00.000Z'
      header:
        Accept:
          schema:
            - type: string
              description: Accept header to specify the response format
              example: application/json, text/csv
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              warningMessage:
                allOf:
                  - type: string
                    description: >-
                      A warning message to disambiguate DIEM usage from legacy
                      DIEM (formerly VCU) usage
              data:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        amount:
                          type: number
                          description: The total amount charged for the billing usage entry
                        currency:
                          type: string
                          enum:
                            - USD
                            - VCU
                            - DIEM
                          description: The currency charged for the billing usage entry
                          example: USD
                        inferenceDetails:
                          type: object
                          nullable: true
                          properties:
                            completionTokens:
                              type: number
                              nullable: true
                              description: >-
                                Number of tokens used in the completion. Only
                                present for LLM usage.
                            inferenceExecutionTime:
                              type: number
                              nullable: true
                              description: >-
                                Time taken for inference execution in
                                milliseconds
                            promptTokens:
                              type: number
                              nullable: true
                              description: >-
                                Number of tokens requested in the prompt. Only
                                present for LLM usage.
                            requestId:
                              type: string
                              nullable: true
                              description: Unique identifier for the inference request
                          required:
                            - completionTokens
                            - inferenceExecutionTime
                            - promptTokens
                            - requestId
                          description: >-
                            Details about the related inference request, if
                            applicable
                        notes:
                          type: string
                          description: Notes about the billing usage entry
                        pricePerUnitUsd:
                          type: number
                          description: The price per unit in USD
                        sku:
                          type: string
                          description: The product associated with the billing usage entry
                        timestamp:
                          type: string
                          description: The timestamp the billing usage entry was created
                          example: '2025-01-01T00:00:00.000Z'
                        units:
                          type: number
                          description: The number of units consumed
                      required:
                        - amount
                        - currency
                        - inferenceDetails
                        - notes
                        - pricePerUnitUsd
                        - sku
                        - timestamp
                        - units
              pagination:
                allOf:
                  - type: object
                    properties:
                      limit:
                        type: number
                      page:
                        type: number
                      total:
                        type: number
                      totalPages:
                        type: number
                    required:
                      - limit
                      - page
                      - total
                      - totalPages
            description: The response schema for the billing usage endpoint
            requiredProperties:
              - data
              - pagination
            additionalProperties: false
            example:
              data:
                - amount: -0.1
                  currency: DIEM
                  inferenceDetails: null
                  notes: API Inference
                  pricePerUnitUsd: 0.1
                  sku: venice-sd35-image-unit
                  timestamp: {}
                  units: 1
                - amount: -0.06356
                  currency: DIEM
                  inferenceDetails:
                    completionTokens: 227
                    inferenceExecutionTime: 2964
                    promptTokens: 339
                    requestId: chatcmpl-4007fd29f42b7d3c4107f4345e8d174a
                  notes: API Inference
                  pricePerUnitUsd: 2.8
                  sku: llama-3.3-70b-llm-output-mtoken
                  timestamp: {}
                  units: 0.000227
              pagination:
                limit: 1
                page: 200
                total: 56090
                totalPages: 56090
        examples:
          example:
            value:
              data:
                - amount: -0.1
                  currency: DIEM
                  inferenceDetails: null
                  notes: API Inference
                  pricePerUnitUsd: 0.1
                  sku: venice-sd35-image-unit
                  timestamp: {}
                  units: 1
                - amount: -0.06356
                  currency: DIEM
                  inferenceDetails:
                    completionTokens: 227
                    inferenceExecutionTime: 2964
                    promptTokens: 339
                    requestId: chatcmpl-4007fd29f42b7d3c4107f4345e8d174a
                  notes: API Inference
                  pricePerUnitUsd: 2.8
                  sku: llama-3.3-70b-llm-output-mtoken
                  timestamp: {}
                  units: 0.000227
              pagination:
                limit: 1
                page: 200
                total: 56090
                totalPages: 56090
        description: Successful response
      text/csv:
        schemaArray:
          - type: string
            description: CSV formatted billing usage data
        examples:
          example:
            value: <string>
        description: Successful response
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              details:
                allOf:
                  - type: object
                    properties: {}
                    description: Details about the incorrect input
                    example:
                      _errors: []
                      field:
                        _errors:
                          - Field is required
              error:
                allOf:
                  - type: string
                    description: A description of the error
            refIdentifier: '#/components/schemas/DetailedError'
            requiredProperties:
              - error
        examples:
          example:
            value:
              details:
                _errors: []
                field:
                  _errors:
                    - Field is required
              error: <string>
        description: Invalid request parameters
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: string
                    description: A description of the error
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: &ref_1
              - error
        examples:
          example:
            value:
              error: <string>
        description: Authentication failed
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: Inference processing failed
  deprecated: false
  type: path
components:
  schemas: {}

````