# Source: https://docs.pinata.cloud/api-reference/endpoint/x402/payment-instructions-get.md

# Get Payment Instruction

> Retrieves a specific payment instruction by ID

## OpenAPI

````yaml get /x402/payment_instructions/{id}
paths:
  path: /x402/payment_instructions/{id}
  method: get
  servers:
    - url: https://api.pinata.cloud/v3
      description: Production server
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Pinata API JWT token
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              description: Payment instruction ID
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - $ref: '#/components/schemas/PaymentInstruction'
        examples:
          example:
            value:
              data:
                id: <string>
                version: 123
                payment_requirements:
                  - asset: <string>
                    pay_to: <string>
                    network: base
                    description: <string>
                    max_amount_required: <string>
                name: <string>
                description: <string>
                created_at: '2023-11-07T05:31:56Z'
        description: Successful operation
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Unauthorized
        examples: {}
        description: Unauthorized
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Forbidden
        examples: {}
        description: Forbidden
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Not found
        examples: {}
        description: Not found
  deprecated: false
  type: path
components:
  schemas:
    PaymentRequirement:
      type: object
      required:
        - asset
        - pay_to
        - network
        - max_amount_required
      properties:
        asset:
          type: string
          pattern: ^0x[a-fA-F0-9]+$
          description: Token contract address (must start with 0x)
        pay_to:
          type: string
          pattern: ^0x[a-fA-F0-9]+$
          description: Ethereum address to receive payment (must start with 0x)
        network:
          type: string
          enum:
            - base
            - base-sepolia
          description: Network for payment
        description:
          type: string
          maxLength: 255
          description: Optional description
        max_amount_required:
          type: string
          description: Maximum amount required for payment
    PaymentInstruction:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier
        version:
          type: integer
          description: Version number
        payment_requirements:
          type: array
          items:
            $ref: '#/components/schemas/PaymentRequirement'
        name:
          type: string
          description: Name of the payment instruction
        description:
          type: string
          description: Description of the payment instruction
        created_at:
          type: string
          format: date-time
          description: Creation timestamp

````