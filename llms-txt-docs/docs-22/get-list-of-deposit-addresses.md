# Source: https://docs.meshconnect.com/api-reference/managed-transfers/get-list-of-deposit-addresses.md

# Get deposit addresses

> Get or generate a cryptocurrency deposit address that can be used to transfer assets to the financial institution

## OpenAPI

````yaml post /api/v1/transfers/managed/address/list
paths:
  path: /api/v1/transfers/managed/address/list
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
                  - minLength: 1
                    type: string
                    description: Symbol of the required cryptocurrency, e.g. ETH or BTC.
              networks:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/NetworkIdentifier'
                    description: >-
                      Specifies which networks to use to obtain the deposit
                      address of the `Symbol` asset.
                    nullable: true
              mfaCode:
                allOf:
                  - type: string
                    nullable: true
            refIdentifier: >-
              #/components/schemas/ManagedBrokerCryptocurrencyDepositAddressListRequest
            requiredProperties:
              - authToken
              - symbol
              - type
            additionalProperties: false
        examples:
          example:
            value:
              symbol: DOGE
              networks:
                - networkId: 34b66a94-f9f9-49ef-81e8-6ebd5a866f9d
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
                          #/components/schemas/B2BBrokerCryptocurrencyDepositAddressListResponse
                    nullable: true
            refIdentifier: >-
              #/components/schemas/B2BBrokerCryptocurrencyDepositAddressListResponseApiResult
            additionalProperties: false
        examples:
          example:
            value:
              content:
                addresses:
                  - address: D641Fmzx...
                    symbol: DOGE
                    networkName: DOGE
              status: ok
              message: ''
              errorHash: ca2da66f
              errorType: ''
        description: Addresses successfully obtained or generation initiated.
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
    B2BBrokerCryptocurrencyDepositAddressListResponse:
      type: object
      properties:
        addresses:
          type: array
          items:
            $ref: '#/components/schemas/DepositAddressItem'
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
    DepositAddressItem:
      type: object
      properties:
        address:
          type: string
          nullable: true
        symbol:
          type: string
          nullable: true
        networkId:
          type: string
          format: uuid
          nullable: true
        caipId:
          type: string
          nullable: true
        networkName:
          type: string
          nullable: true
        logoUrl:
          type: string
          nullable: true
      additionalProperties: false
    NetworkIdentifier:
      type: object
      properties:
        networkId:
          type: string
          description: Either NetworkId or CaipId should be present, but not both.
          format: uuid
          nullable: true
        caipId:
          type: string
          description: Either NetworkId or CaipId should be present, but not both.
          nullable: true
      additionalProperties: false

````