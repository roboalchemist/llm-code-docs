# Source: https://docs.meshconnect.com/api-reference/managed-account-authentication/remove-connection.md

# Remove connection

> Remove connection to the financial institution and erase all related data completely.

## OpenAPI

````yaml delete /api/v1/account
paths:
  path: /api/v1/account
  method: delete
  servers:
    - url: https://integration-api.meshconnect.com
    - url: https://sandbox-integration-api.meshconnect.com
  request:
    security:
      - title: Client Secret & Client Id
        parameters:
          query: {}
          header:
            X-Client-Secret:
              type: apiKey
              description: Contact Mesh to get client Secret
            X-Client-Id:
              type: apiKey
              description: Contact Mesh to get client Id
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              authToken:
                allOf:
                  - &ref_0
                    minLength: 1
                    type: string
                    description: >-
                      Auth token that allows connecting to the target
                      institution
              type:
                allOf:
                  - &ref_1
                    enum:
                      - robinhood
                      - eTrade
                      - alpaca
                      - tdAmeritrade
                      - weBull
                      - stash
                      - interactiveBrokers
                      - public
                      - coinbase
                      - kraken
                      - coinbasePro
                      - cryptoCom
                      - openSea
                      - binanceUs
                      - gemini
                      - cryptocurrencyAddress
                      - cryptocurrencyWallet
                      - okCoin
                      - bittrex
                      - kuCoin
                      - etoro
                      - cexIo
                      - binanceInternational
                      - bitstamp
                      - gateIo
                      - acorns
                      - okx
                      - bitFlyer
                      - coinlist
                      - huobi
                      - bitfinex
                      - deFiWallet
                      - krakenDirect
                      - vanguard
                      - binanceInternationalDirect
                      - bitfinexDirect
                      - bybit
                      - paxos
                      - coinbasePrime
                      - btcTurkDirect
                      - kuCoinDirect
                      - okxOAuth
                      - paribuDirect
                      - robinhoodConnect
                      - blockchainCom
                      - bitsoDirect
                      - binanceConnect
                      - binanceOAuth
                      - revolutConnect
                      - binancePay
                      - bybitDirect
                      - paribuOAuth
                      - payPalConnect
                      - binanceTrDirect
                      - coinbaseRamp
                      - bybitDirectMobile
                      - sandbox
                      - cryptoComPay
                      - bybitEuDirect
                    allOf:
                      - $ref: '#/components/schemas/BrokerType'
                    description: Type of the institution to connect
            refIdentifier: '#/components/schemas/BrokerBaseRequest'
            requiredProperties: &ref_2
              - authToken
              - type
            additionalProperties: false
        examples:
          example:
            value:
              authToken: Secret authentication token
              type: robinhood
      text/json:
        schemaArray:
          - type: object
            properties:
              authToken:
                allOf:
                  - *ref_0
              type:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/BrokerBaseRequest'
            requiredProperties: *ref_2
            additionalProperties: false
        examples:
          example:
            value:
              authToken: Secret authentication token
              type: robinhood
      application/*+json:
        schemaArray:
          - type: object
            properties:
              authToken:
                allOf:
                  - *ref_0
              type:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/BrokerBaseRequest'
            requiredProperties: *ref_2
            additionalProperties: false
        examples:
          example:
            value:
              authToken: Secret authentication token
              type: robinhood
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - &ref_3
                    enum:
                      - ok
                      - serverFailure
                      - permissionDenied
                      - badRequest
                      - notFound
                      - conflict
                      - tooManyRequest
                      - locked
                      - unavailableForLegalReasons
                    allOf:
                      - $ref: '#/components/schemas/ApiResultStatus'
                    readOnly: true
              message:
                allOf:
                  - &ref_4
                    type: string
                    description: A message generated by the API
                    nullable: true
              displayMessage:
                allOf:
                  - &ref_5
                    type: string
                    description: >-
                      User-friendly display message that can be presented to the
                      end user
                    nullable: true
              errorHash:
                allOf:
                  - &ref_6
                    type: string
                    description: >-
                      An error grouping hash from string components and caller
                      information. Used by bugsnag on FE for correct error
                      grouping
                    nullable: true
                    readOnly: true
              errorType:
                allOf:
                  - &ref_7
                    type: string
                    description: "Strictly-typed error type that is explaining the reason of an unsuccessful status of the operation.\r\nAll possible error types are available in the documentation."
                    nullable: true
              errorData:
                allOf:
                  - &ref_8
                    nullable: true
                    readOnly: true
            refIdentifier: '#/components/schemas/ApiResult'
            additionalProperties: false
        examples:
          example:
            value:
              status: ok
              message: ''
              errorHash: f6fc87aa
              errorType: ''
        description: OK
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - *ref_3
              message:
                allOf:
                  - *ref_4
              displayMessage:
                allOf:
                  - *ref_5
              errorHash:
                allOf:
                  - *ref_6
              errorType:
                allOf:
                  - *ref_7
              errorData:
                allOf:
                  - *ref_8
            refIdentifier: '#/components/schemas/ApiResult'
            additionalProperties: false
        examples:
          example:
            value:
              status: badRequest
              message: Error message
              displayMessage: Optional display message
              errorHash: 7dcbb73d
              errorType: missingField
        description: Bad Request
    '401':
      application/json:
        schemaArray:
          - type: any
        examples:
          example:
            value: <any>
        description: Unauthorized
  deprecated: false
  type: path
components:
  schemas:
    ApiResultStatus:
      enum:
        - ok
        - serverFailure
        - permissionDenied
        - badRequest
        - notFound
        - conflict
        - tooManyRequest
        - locked
        - unavailableForLegalReasons
      type: string
    BrokerType:
      enum:
        - robinhood
        - eTrade
        - alpaca
        - tdAmeritrade
        - weBull
        - stash
        - interactiveBrokers
        - public
        - coinbase
        - kraken
        - coinbasePro
        - cryptoCom
        - openSea
        - binanceUs
        - gemini
        - cryptocurrencyAddress
        - cryptocurrencyWallet
        - okCoin
        - bittrex
        - kuCoin
        - etoro
        - cexIo
        - binanceInternational
        - bitstamp
        - gateIo
        - acorns
        - okx
        - bitFlyer
        - coinlist
        - huobi
        - bitfinex
        - deFiWallet
        - krakenDirect
        - vanguard
        - binanceInternationalDirect
        - bitfinexDirect
        - bybit
        - paxos
        - coinbasePrime
        - btcTurkDirect
        - kuCoinDirect
        - okxOAuth
        - paribuDirect
        - robinhoodConnect
        - blockchainCom
        - bitsoDirect
        - binanceConnect
        - binanceOAuth
        - revolutConnect
        - binancePay
        - bybitDirect
        - paribuOAuth
        - payPalConnect
        - binanceTrDirect
        - coinbaseRamp
        - bybitDirectMobile
        - sandbox
        - cryptoComPay
        - bybitEuDirect
      type: string

````