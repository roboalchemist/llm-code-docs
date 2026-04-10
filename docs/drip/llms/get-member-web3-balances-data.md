# Source: https://docs.drip.re/api-reference/web3-activations-members/get-member-web3-balances-data.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Get member web3 balances data

> Get member web3 balances data by a specific member of a specific activation

## OpenAPI

````yaml https://api.drip.re/docs/json get /api/v1/realms/{realmId}/web3/members/{dripId}/balances
openapi: 3.1.0
info:
  title: Drip Rewards API
  description: The official API documentation for the Drip Rewards Ecosystem
  version: 1.0.0
servers:
  - url: https://api.drip.re/
    description: DRIP API
security:
  - BearerAuth: []
tags: []
externalDocs:
  url: https://swagger.io
  description: Find more info here
paths:
  /api/v1/realms/{realmId}/web3/members/{dripId}/balances:
    get:
      tags:
        - Web3-Activations-Members
      summary: Get member web3 balances data
      description: >-
        Get member web3 balances data by a specific member of a specific
        activation
      parameters:
        - schema:
            type: string
          in: path
          name: realmId
          required: true
        - schema:
            type: string
          in: path
          name: dripId
          required: true
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    $ref: '#/components/schemas/MemberBalancesData'
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MessageResponse'
        '403':
          description: Default Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ForbiddenResponse'
        '404':
          description: Default Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotFoundResponse'
        '500':
          description: Default Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    MemberBalancesData:
      $ref: '#/components/schemas/MemberBalancesData'
      type: object
      properties:
        claimableBalances:
          $ref: '#/components/schemas/ClaimableBalancesData'
        claimableBalancesByActivation:
          $ref: '#/components/schemas/ClaimableBalancesByActivationData'
        tokenBalances:
          $ref: '#/components/schemas/TokenBalancesData'
    MessageResponse:
      $ref: '#/components/schemas/MessageResponse'
      type: object
      properties:
        message:
          type: string
    ForbiddenResponse:
      $ref: '#/components/schemas/ForbiddenResponse'
      description: Forbidden response, user is not authorized to access the resource
      type: object
      required:
        - error
        - message
      properties:
        error:
          type: string
          enum:
            - Forbidden
          description: Error type
        message:
          type: string
          description: Error message
    NotFoundResponse:
      $ref: '#/components/schemas/NotFoundResponse'
      type: object
      description: Not found response, resource not found
      required:
        - error
        - message
      properties:
        error:
          type: string
          enum:
            - Not Found
          description: Error type
        message:
          type: string
          description: Error message
    ErrorResponse:
      $ref: '#/components/schemas/ErrorResponse'
      type: object
      required:
        - error
      properties:
        error:
          type: string
          description: Error message
        message:
          type: string
          description: Error message
          nullable: true
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API Key
      description: API Key

````

Built with [Mintlify](https://mintlify.com).
