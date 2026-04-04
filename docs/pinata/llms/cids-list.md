# Source: https://docs.pinata.cloud/api-reference/endpoint/x402/cids-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# List CIDs for Payment Instruction

> Returns a paginated list of CIDs associated with a payment instruction



## OpenAPI

````yaml get /x402/payment_instructions/{id}/cids
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
  /x402/payment_instructions/{id}/cids:
    get:
      summary: List CIDs for Payment Instruction
      description: Returns a paginated list of CIDs associated with a payment instruction
      operationId: listCIDs
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
          description: Payment instruction ID
        - name: limit
          in: query
          schema:
            type: integer
            minimum: 1
            maximum: 1000
            default: 20
          description: Number of items to return
        - name: pageToken
          in: query
          schema:
            type: string
          description: Token for pagination
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
                      cids:
                        type: array
                        items:
                          type: string
                      next_page_token:
                        type: string
                        description: Token for next page (omitted on last page)
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