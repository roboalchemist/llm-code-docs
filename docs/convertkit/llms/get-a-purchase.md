# Source: https://developers.kit.com/api-reference/purchases/get-a-purchase.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a purchase



## OpenAPI

````yaml api-reference/v4.json get /v4/purchases/{id}
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/purchases/{id}:
    get:
      tags:
        - Purchases
      summary: Get a purchase
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          example: 15
      responses:
        '200':
          description: Returns the purchase details
          content:
            application/json:
              schema:
                type: object
                properties:
                  purchase:
                    type: object
                    properties:
                      id:
                        type: integer
                      transaction_id:
                        type: string
                      subscriber_id:
                        type: integer
                      status:
                        type: string
                      email_address:
                        type: string
                      currency:
                        type: string
                      transaction_time:
                        type: string
                      subtotal:
                        type: number
                        format: float
                      discount:
                        type: number
                        format: float
                      tax:
                        type: number
                        format: float
                      total:
                        type: number
                        format: float
                      products:
                        type: array
                        items:
                          type: object
                          properties:
                            quantity:
                              type: integer
                              description: Product quantity
                            lid:
                              type: string
                              description: >-
                                Each product should have a unique `lid` (i.e.,
                                line item identifier) for this purchase.
                            unit_price:
                              type: number
                              format: float
                              description: Product price
                            sku:
                              nullable: true
                            name:
                              type: string
                              description: Product name
                            pid:
                              type: string
                              description: >-
                                This is your identifier for a product. Each
                                product provided in the `products` array must
                                have a unique pid. Variants of the same product
                                should have the same pid.
                          required:
                            - quantity
                            - lid
                            - unit_price
                            - sku
                            - name
                            - pid
                    required:
                      - id
                      - transaction_id
                      - subscriber_id
                      - status
                      - email_address
                      - currency
                      - transaction_time
                      - subtotal
                      - discount
                      - tax
                      - total
                      - products
                required:
                  - purchase
              example:
                purchase:
                  id: 14
                  transaction_id: 796-92-4892
                  subscriber_id: 526
                  status: paid
                  email_address: pru.magoo@convertkit.dev
                  currency: USD
                  transaction_time: '2023-02-17T11:43:55Z'
                  subtotal: 78.66
                  discount: 5
                  tax: 7.87
                  total: 81.53
                  products:
                    - quantity: 1
                      lid: 811-75-7900
                      unit_price: 23.22
                      sku: null
                      name: Phantom Hourglass
                      pid: 804-02-4430
                    - quantity: 1
                      lid: 766-49-1241
                      unit_price: 32.22
                      sku: null
                      name: Twilight Princess
                      pid: 833-51-1151
        '401':
          description: Returns a 401 if the token and/or account cannot be authenticated
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                required:
                  - errors
              example:
                errors:
                  - The access token is invalid
        '404':
          description: Returns a 404 when the provided id does not exist
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                required:
                  - errors
              example:
                errors:
                  - Not Found
      security:
        - OAuth2: []
components:
  securitySchemes:
    OAuth2:
      description: Authenticate API requests via an OAuth token
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://api.kit.com/v4/oauth/authorize
          tokenUrl: https://api.kit.com/v4/oauth/token
          refreshUrl: https://api.kit.com/v4/oauth/token
          scopes:
            read: Read access to Kit API v4
            write: Write access to Kit API v4

````

Built with [Mintlify](https://mintlify.com).