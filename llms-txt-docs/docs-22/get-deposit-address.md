# Source: https://docs.meshconnect.com/api-reference/transfers/get-deposit-address.md

# Source: https://docs.meshconnect.com/api-reference/managed-transfers/get-deposit-address.md

# Get deposit address

> Get or generate a cryptocurrency deposit address that can be used to transfer assets to the financial institution

## OpenAPI

````yaml post /api/v1/transfers/managed/address/get
paths:
  path: /api/v1/transfers/managed/address/get
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
                    description: Type of the institution to connect
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
              networkId:
                allOf:
                  - type: string
                    description: >-
                      Specifies which the network to use to obtain the deposit
                      address of the `Symbol` asset.
                    format: uuid
              mfaCode:
                allOf:
                  - type: string
                    description: >-
                      Some of integrations require MFA code to create a deposit
                      address, e.g. KrakenDirect
                    nullable: true
            refIdentifier: >-
              #/components/schemas/ManagedBrokerCryptocurrencyDepositAddressRequest
            requiredProperties:
              - authToken
              - type
            additionalProperties: false
        examples:
          example:
            value:
              symbol: DOGE
              networkId: 34b66a94-f9f9-49ef-81e8-6ebd5a866f9d
              authToken: Secret authentication token
              type: binanceInternational
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
                          #/components/schemas/B2BBrokerCryptocurrencyDepositAddressResponse
                    nullable: true
            refIdentifier: >-
              #/components/schemas/B2BBrokerCryptocurrencyDepositAddressResponseApiResult
            additionalProperties: false
        examples:
          example:
            value:
              content:
                symbol: DOGE
                address: D641Fmzx...
                chain: DOGE
              status: ok
              message: ''
              errorHash: 010074a1
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
        description: Address for the required symbol is not found.
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
    B2BBrokerCryptocurrencyDepositAddressResponse:
      type: object
      properties:
        symbol:
          type: string
          nullable: true
        address:
          type: string
          nullable: true
        chain:
          type: string
          nullable: true
        memo:
          type: string
          nullable: true
        minimumDepositAmount:
          type: string
          nullable: true
        networkId:
          type: string
          format: uuid
          nullable: true
        brokerResponseStatus:
          allOf:
            - $ref: '#/components/schemas/BrokerResponseStatus'
          nullable: true
        errorMessage:
          type: string
          nullable: true
      additionalProperties: false
    BrokerResponseStatus:
      enum:
        - unknown
        - mfaRequired
        - kycRequired
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