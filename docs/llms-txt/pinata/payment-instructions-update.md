# Source: https://docs.pinata.cloud/api-reference/endpoint/x402/payment-instructions-update.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Payment Instruction

> Updates an existing payment instruction



## OpenAPI

````yaml patch /x402/payment_instructions/{id}
openapi: 3.0.0
info:
  title: Pinata x402 Payment Instructions API
  description: API for managing x402 payment instructions and CID associations
  version: 3.0.0
servers:
  - url: https://api.pinata.cloud/v3
    description: Production server
security: []
paths:
  /x402/payment_instructions/{id}:
    patch:
      summary: Update Payment Instruction
      description: Updates an existing payment instruction
      operationId: updatePaymentInstruction
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
          description: Payment instruction ID
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              minProperties: 1
              properties:
                name:
                  type: string
                  description: Name of the payment instruction
                description:
                  type: string
                  description: Description of the payment instruction
                payment_requirements:
                  type: array
                  minItems: 1
                  items:
                    $ref: '#/components/schemas/PaymentRequirement'
      responses:
        '200':
          description: Successful operation
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    $ref: '#/components/schemas/PaymentInstruction'
        '400':
          description: Bad request
        '401':
          description: Unauthorized
        '403':
          description: Forbidden
        '404':
          description: Not found
      security:
        - bearerAuth: []
components:
  schemas:
    PaymentRequirement:
      type: object
      required:
        - asset
        - pay_to
        - network
        - amount
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
            - eip155:8453
            - eip155:84532
          description: Network for payment (accepts friendly names or EIP-155 chain IDs)
        description:
          type: string
          maxLength: 255
          description: Optional description
        amount:
          type: string
          description: Amount required for payment in smallest token unit
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
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: Pinata API JWT token

````