# Source: https://docs.pinata.cloud/api-reference/endpoint/x402/payment-instructions-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# List Payment Instructions

> Returns a paginated list of payment instructions



## OpenAPI

````yaml get /x402/payment_instructions
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
  /x402/payment_instructions:
    get:
      summary: List Payment Instructions
      description: Returns a paginated list of payment instructions
      operationId: listPaymentInstructions
      parameters:
        - name: limit
          in: query
          schema:
            type: integer
            minimum: 1
            maximum: 1000
            default: 10
          description: Number of items to return
        - name: pageToken
          in: query
          schema:
            type: string
          description: Token for pagination
        - name: cid
          in: query
          schema:
            type: string
          description: Filter by CID mapped (returns max 1 payment instruction)
        - name: name
          in: query
          schema:
            type: string
          description: Filter by name
        - name: id
          in: query
          schema:
            type: string
          description: Filter by ID
      responses:
        '200':
          description: Successful operation
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      payment_instructions:
                        type: array
                        items:
                          $ref: '#/components/schemas/PaymentInstruction'
                      next_page_token:
                        type: string
                        description: Token for next page (omitted on last page)
        '401':
          description: Unauthorized
        '403':
          description: Forbidden
      security:
        - bearerAuth: []
components:
  schemas:
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
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: Pinata API JWT token

````