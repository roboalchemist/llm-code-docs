# Source: https://developers.kit.com/api-reference/purchases/create-a-purchase.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a purchase



## OpenAPI

````yaml api-reference/v4.json post /v4/purchases
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/purchases:
    post:
      tags:
        - Purchases
      summary: Create a purchase
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                purchase:
                  type: object
                  properties:
                    email_address:
                      type: string
                      description: The subscriber that the purchase belongs to
                    transaction_id:
                      type: string
                    status:
                      type: string
                    subtotal:
                      type: number
                      format: float
                    tax:
                      type: number
                      format: float
                    shipping:
                      type: integer
                    discount:
                      type: number
                      format: float
                    total:
                      type: number
                      format: float
                    currency:
                      type: string
                      description: 3 letter currency code (e.g. `USD`)
                    transaction_time:
                      type: string
                    products:
                      type: array
                      description: Array of purchased products
                      items:
                        type: object
                        properties:
                          name:
                            type: string
                            description: Product name
                          pid:
                            type: string
                            description: >-
                              This is your identifier for a product. Each
                              product provided in the `products` array must have
                              a unique pid. Variants of the same product should
                              have the same pid.
                          lid:
                            type: string
                            description: >-
                              Each product should have a unique `lid` (i.e.,
                              line item identifier) for this purchase.
                          quantity:
                            type: integer
                            description: Product quantity
                          unit_price:
                            type: number
                            format: float
                            description: Product price
                          sku:
                            type: string
                            description: Product sku
                        required:
                          - name
                          - pid
                          - lid
                          - quantity
                          - unit_price
                          - sku
                  required:
                    - email_address
                    - transaction_id
                    - status
                    - subtotal
                    - tax
                    - shipping
                    - discount
                    - total
                    - currency
                    - transaction_time
                    - products
              required:
                - purchase
            example:
              purchase:
                email_address: pru.magoo@convertkit.dev
                transaction_id: 796-92-4892
                status: paid
                subtotal: 78.66
                tax: 7.87
                shipping: 0
                discount: 5
                total: 81.53
                currency: USD
                transaction_time: '2023-02-17T11:43:55Z'
                products:
                  - name: Phantom Hourglass
                    pid: 804-02-4430
                    lid: 811-75-7900
                    quantity: 1
                    unit_price: 23.22
                    sku: SM21-SH-M02-RD-S-001
                  - name: Twilight Princess
                    pid: 833-51-1151
                    lid: 766-49-1241
                    quantity: 1
                    unit_price: 32.22
                    sku: WT21-JK-M03-BK-L-012
                  - name: Four Swords
                    pid: 217-99-4325
                    lid: 563-95-8878
                    quantity: 1
                    unit_price: 23.22
                    sku: FL21-TS-M01-BL-M-020
      responses:
        '201':
          description: >-
            Creates a purchase for the provided subscriber and returns its
            details. It also creates products if they don't exist.
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
                        description: The subscriber that the purchase belongs to
                      currency:
                        type: string
                        description: 3 letter currency code (e.g. `USD`)
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
                              type: string
                              description: Product sku
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
                  id: 20
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
                      sku: SM21-SH-M02-RD-S-001
                      name: Phantom Hourglass
                      pid: 804-02-4430
                    - quantity: 1
                      lid: 766-49-1241
                      unit_price: 32.22
                      sku: WT21-JK-M03-BK-L-012
                      name: Twilight Princess
                      pid: 833-51-1151
                    - quantity: 1
                      lid: 563-95-8878
                      unit_price: 23.22
                      sku: FL21-TS-M01-BL-M-020
                      name: Four Swords
                      pid: 217-99-4325
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
        '422':
          description: Returns a 422 when one or more of the parameters are invalid
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
                  - Transaction cannot be blank
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