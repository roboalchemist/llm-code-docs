# Source: https://docs.meshconnect.com/api-reference/transfers/get-details-of-asset.md

# Get details of asset

> Get details of the asset for deposit or withdrawal. For example, several exchanges support same tokens over multiple
blockchains, and thus require the name of chain to be supplied for transfers. This endpoint allows getting such details.

## OpenAPI

````yaml post /api/v1/transfers/symbol/details
paths:
  path: /api/v1/transfers/symbol/details
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
                      ```BinanceInternational```
                      ```Bitstamp```
                      ```GateIo```
                      ```Okx```
                      ```Huobi```
                      ```Bitfinex```
                      ```KrakenDirect```
                      ```BinanceInternationalDirect```
                      ```BitfinexDirect```
                      ```Bybit```
                      ```Paxos```
                      ```CoinbasePrime```
                      ```BtcTurkDirect```
                      ```ParibuDirect```
                      ```RobinhoodConnect```
                      ```BlockchainCom```
                      ```BinanceConnect```
                      ```RevolutConnect```
                      ```BinancePay```
                      ```BybitDirect```
                      ```ParibuOAuth```
                      ```PayPalConnect```
                      ```CoinbaseRamp```
                      ```BybitDirectMobile```
                      ```Sandbox```
                      ```CryptoComPay```
                      ```DeFiWallet```
              symbol:
                allOf:
                  - type: string
                    description: "Symbol of the required cryptocurrency, e.g. ETH or BTC.\r\nCan be used instead of the `AddressType` field."
                    nullable: true
              addressType:
                allOf:
                  - allOf:
                      - $ref: '#/components/schemas/CryptocurrencyAddressType'
                    description: "Type of the address of symbol to be transferred. Providing `EthAddress` will assume a transfer of ETH over Ethereum blockchain.\r\nCan be used instead of `Symbol` field."
                    nullable: true
              chain:
                allOf:
                  - type: string
                    description: >-
                      Chain of the required cryptocurrency, e.g. USDT has
                      USDT-ERC20, USDT-TRC20, and USDT-Omni
                    nullable: true
              mfaCode:
                allOf:
                  - type: string
                    description: >-
                      Some of integrations require MFA code to create a deposit
                      address, e.g. KrakenDirect
                    nullable: true
            refIdentifier: >-
              #/components/schemas/TransfersBrokerCryptocurrencyDepositAddressRequest
            requiredProperties:
              - authToken
              - type
            additionalProperties: false
        examples:
          example:
            value:
              symbol: DOGE
              chain: DOGE
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
                      - $ref: >-
                          #/components/schemas/B2BBrokerCryptocurrencySymbolDetailsResponse
                    nullable: true
            refIdentifier: >-
              #/components/schemas/B2BBrokerCryptocurrencySymbolDetailsResponseApiResult
            additionalProperties: false
        examples:
          example:
            value:
              content:
                symbol: ETH
                addressTypes:
                  - ethAddress
                chains:
                  - chain: Ethereum
                    fee: 0.00001
              status: ok
              message: ''
              errorHash: 2028c79c
              errorType: ''
        description: Address successfully obtained or generation initiated.
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - &ref_0
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
                  - &ref_1
                    type: string
                    description: A message generated by the API
                    nullable: true
              displayMessage:
                allOf:
                  - &ref_2
                    type: string
                    description: >-
                      User-friendly display message that can be presented to the
                      end user
                    nullable: true
              errorHash:
                allOf:
                  - &ref_3
                    type: string
                    description: >-
                      An error grouping hash from string components and caller
                      information. Used by bugsnag on FE for correct error
                      grouping
                    nullable: true
                    readOnly: true
              errorType:
                allOf:
                  - &ref_4
                    type: string
                    description: "Strictly-typed error type that is explaining the reason of an unsuccessful status of the operation.\r\nAll possible error types are available in the documentation."
                    nullable: true
              errorData:
                allOf:
                  - &ref_5
                    nullable: true
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
        description: Request details are not correct.
    '401':
      application/json:
        schemaArray:
          - type: any
        examples:
          example:
            value: <any>
        description: 'Unauthorized: Client Id or Client Secret are not correct or missing.'
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
              displayMessage:
                allOf:
                  - *ref_2
              errorHash:
                allOf:
                  - *ref_3
              errorType:
                allOf:
                  - *ref_4
              errorData:
                allOf:
                  - *ref_5
            refIdentifier: '#/components/schemas/ApiResult'
            additionalProperties: false
        examples:
          example:
            value:
              status: notFound
              message: Error message
              displayMessage: Optional display message
              errorHash: 7dcbb73d
              errorType: missingField
        description: Asset details for provided symbol are not found.
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
    B2BBrokerCryptocurrencySymbolDetailsResponse:
      type: object
      properties:
        symbol:
          type: string
          description: Requested symbol
          nullable: true
        addressTypes:
          type: array
          items:
            $ref: '#/components/schemas/CryptocurrencyAddressType'
          description: Supported address types
          nullable: true
        chains:
          type: array
          items:
            $ref: '#/components/schemas/BrokerCryptocurrencyChain'
          description: >-
            Supported chains. One of the values should be provided to execute
            transfers
          nullable: true
      additionalProperties: false
    BrokerCryptocurrencyChain:
      type: object
      properties:
        chain:
          type: string
          description: Name of the chain, should be provided when initiating a transfer
          nullable: true
        feeDescription:
          type: string
          nullable: true
        notes:
          type: string
          description: Notes or tips provided by the integration
          nullable: true
        fee:
          type: number
          format: double
          nullable: true
        minWithdrawAmount:
          type: number
          format: double
          nullable: true
        maxWithdrawAmount:
          type: number
          format: double
          nullable: true
        networkId:
          type: string
          format: uuid
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
    CryptocurrencyAddressType:
      enum:
        - ethAddress
        - btcAddress
        - ltcAddress
        - solAddress
        - algoAddress
        - celoAddress
        - cardanoAddress
        - polygonAddress
        - bnbAddress
        - elrondAddress
        - neoAddress
        - xrpAddress
        - flowAddress
        - harmonyOneAddress
        - tronAddress
        - dogeAddress
        - opAddress
      type: string

````