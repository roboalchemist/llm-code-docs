# Source: https://docs.pinata.cloud/api-reference/endpoint/x402/cids-add.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Add CID to Payment Instruction

> Associates a CID with a payment instruction



## OpenAPI

````yaml put /x402/payment_instructions/{id}/cids/{cid}
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
  /x402/payment_instructions/{id}/cids/{cid}:
    put:
      summary: Add CID to Payment Instruction
      description: Associates a CID with a payment instruction
      operationId: addCID
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
          description: Payment instruction ID
        - name: cid
          in: path
          required: true
          schema:
            type: string
          description: Content Identifier (CID)
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
                      payment_instruction_id:
                        type: string
                      cid:
                        type: string
                      created_at:
                        type: string
                        format: date-time
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
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: Pinata API JWT token

````