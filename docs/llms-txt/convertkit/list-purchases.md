# Source: https://developers.kit.com/api-reference/purchases/list-purchases.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List purchases



## OpenAPI

````yaml api-reference/v4.json get /v4/purchases
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/purchases:
    get:
      tags:
        - Purchases
      summary: List purchases
      parameters:
        - name: after
          description: To fetch next page of results, use `?after=<end_cursor>`
          in: query
          required: false
          schema:
            nullable: true
        - name: before
          description: To fetch previous page of results, use `?before=<start_cursor>`
          in: query
          required: false
          schema:
            nullable: true
        - name: include_total_count
          description: >-
            To include the total count of records in the response, use `true`.
            For large collections, expect a slightly slower response.
          in: query
          required: false
          schema:
            type: boolean
          example: false
        - name: per_page
          description: Number of results per page. Default 500, maximum 1000.
          in: query
          required: false
          schema:
            nullable: true
      responses:
        '200':
          description: Returns a paginated list of all purchases for your account
          content:
            application/json:
              schema:
                type: object
                properties:
                  purchases:
                    type: array
                    items:
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
                          description: Array of purchased products
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
                                description: Product sku
                              name:
                                type: string
                                description: Product name
                              pid:
                                type: string
                                description: >-
                                  This is your identifier for a product. Each
                                  product provided in the `products` array must
                                  have a unique pid. Variants of the same
                                  product should have the same pid.
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
                  pagination:
                    type: object
                    properties:
                      has_previous_page:
                        type: boolean
                      has_next_page:
                        type: boolean
                      start_cursor:
                        type: string
                      end_cursor:
                        type: string
                      per_page:
                        type: integer
                    required:
                      - has_previous_page
                      - has_next_page
                      - start_cursor
                      - end_cursor
                      - per_page
                required:
                  - purchases
                  - pagination
              example:
                purchases:
                  - id: 3
                    transaction_id: 512-41-4101
                    subscriber_id: 526
                    status: paid
                    email_address: pru.magoo@convertkit.dev
                    currency: USD
                    transaction_time: '2023-02-17T11:43:55Z'
                    subtotal: 5
                    discount: 0
                    tax: 0
                    total: 5
                    products:
                      - quantity: 1
                        lid: 000-13-0000
                        unit_price: 0.05
                        sku: null
                        name: Tip
                        pid: 111-75-7524
                  - id: 2
                    transaction_id: 323-79-5320
                    subscriber_id: 526
                    status: paid
                    email_address: pru.magoo@convertkit.dev
                    currency: USD
                    transaction_time: '2023-02-17T11:43:55Z'
                    subtotal: 10
                    discount: 0
                    tax: 1.05
                    total: 11.05
                    products:
                      - quantity: 1
                        lid: 000-12-0000
                        unit_price: 0.1
                        sku: null
                        name: Monthly Game Review
                        pid: 000-11-0000
                  - id: 1
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
                pagination:
                  has_previous_page: false
                  has_next_page: false
                  start_cursor: WzNd
                  end_cursor: WzFd
                  per_page: 500
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