# Source: https://docs.meshconnect.com/api-reference/balance/get-account-balance.md

# Get account balance

> Get real-time account fiat balances.

## OpenAPI

````yaml post /api/v1/balance/get
paths:
  path: /api/v1/balance/get
  method: post
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
                  - minLength: 1
                    type: string
                    description: >-
                      Auth token that allows connecting to the target
                      institution
              type:
                allOf:
                  - enum:
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
                    description: |
                      Type of the institution to connect

                      ### Supported integrations:
                      ```Robinhood```
                      ```Coinbase```
                      ```Kraken```
                      ```CryptoCom```
                      ```Binance```
                      ```Gemini```
                      ```OkCoin```
                      ```KuCoin```
                      ```CexIo```
                      ```BinanceInternational```
                      ```Bitstamp```
                      ```GateIo```
                      ```Okx```
                      ```BitFlyer```
                      ```Coinlist```
                      ```Huobi```
                      ```Bitfinex```
                      ```KrakenDirect```
                      ```BinanceInternationalDirect```
                      ```BitfinexDirect```
                      ```Bybit```
                      ```Paxos```
                      ```CoinbasePrime```
                      ```BtcTurkDirect```
                      ```KuCoinDirect```
                      ```OkxOAuth```
                      ```ParibuDirect```
                      ```RobinhoodConnect```
                      ```BlockchainCom```
                      ```BitsoDirect```
                      ```BybitDirect```
                      ```ParibuOAuth```
                      ```BinanceTrDirect```
                      ```BybitDirectMobile```
                      ```Sandbox```
            refIdentifier: '#/components/schemas/BalanceBrokerBaseRequest'
            requiredProperties:
              - authToken
              - type
            additionalProperties: false
        examples:
          example:
            value:
              authToken: Secret authentication token
              type: binanceInternationalDirect
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - enum:
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
                  - type: string
                    description: A message generated by the API
                    nullable: true
              displayMessage:
                allOf:
                  - type: string
                    description: >-
                      User-friendly display message that can be presented to the
                      end user
                    nullable: true
              errorHash:
                allOf:
                  - type: string
                    description: >-
                      An error grouping hash from string components and caller
                      information. Used by bugsnag on FE for correct error
                      grouping
                    nullable: true
                    readOnly: true
              errorType:
                allOf:
                  - type: string
                    description: "Strictly-typed error type that is explaining the reason of an unsuccessful status of the operation.\r\nAll possible error types are available in the documentation."
                    nullable: true
              errorData:
                allOf:
                  - nullable: true
                    readOnly: true
              content:
                allOf:
                  - allOf:
                      - $ref: '#/components/schemas/B2BBrokerAccountBalanceModel'
                    nullable: true
            refIdentifier: '#/components/schemas/B2BBrokerAccountBalanceModelApiResult'
            additionalProperties: false
        examples:
          example:
            value:
              content:
                balances:
                  - cash: 158.5
                    buyingPower: 258.5
                    currencyCode: USD
                  - cash: 10
                    buyingPower: 10
                    currencyCode: EUR
                totalCashUsdValue: 10
                totalBuyingPowerUsdValue: 10
              status: ok
              message: ''
              errorHash: 3ad8c4a4
              errorType: ''
        description: OK
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - enum:
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
                  - type: string
                    description: A message generated by the API
                    nullable: true
              displayMessage:
                allOf:
                  - type: string
                    description: >-
                      User-friendly display message that can be presented to the
                      end user
                    nullable: true
              errorHash:
                allOf:
                  - type: string
                    description: >-
                      An error grouping hash from string components and caller
                      information. Used by bugsnag on FE for correct error
                      grouping
                    nullable: true
                    readOnly: true
              errorType:
                allOf:
                  - type: string
                    description: "Strictly-typed error type that is explaining the reason of an unsuccessful status of the operation.\r\nAll possible error types are available in the documentation."
                    nullable: true
              errorData:
                allOf:
                  - nullable: true
                    readOnly: true
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
    '403':
      application/json:
        schemaArray:
          - type: any
        examples:
          example:
            value: <any>
        description: >-
          The API key used does not have read permission to call this Mesh
          endpoint.
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
    B2BBrokerAccountBalance:
      type: object
      properties:
        cash:
          type: number
          description: Withdrawable cash amount on the account.
          format: double
          nullable: true
        buyingPower:
          type: number
          description: >-
            Buying power indicating the maximum amount the user can spend to buy
            assets. E.g. available margin.
          format: double
          nullable: true
        cryptocurrencyBuyingPower:
          type: number
          description: Buying power available for placing cryptocurrency orders.
          format: double
          nullable: true
        currencyCode:
          type: string
          description: ISO 4217 currency code.
          nullable: true
      additionalProperties: false
    B2BBrokerAccountBalanceModel:
      type: object
      properties:
        balances:
          type: array
          items:
            $ref: '#/components/schemas/B2BBrokerAccountBalance'
          nullable: true
        totalCashUsdValue:
          type: number
          description: Total USD value of all currencies
          format: double
          nullable: true
        totalBuyingPowerUsdValue:
          type: number
          description: Total USD value of all Buying Power
          format: double
          nullable: true
      additionalProperties: false
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