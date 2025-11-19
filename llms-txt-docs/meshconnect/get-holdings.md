# Source: https://docs.meshconnect.com/api-reference/portfolio/get-holdings.md

# Get holdings.

> Obtain assets from the connected investment account. Performs realtime API call to the underlying integration.

## OpenAPI

````yaml post /api/v1/holdings/get
paths:
  path: /api/v1/holdings/get
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
                      ```OpenSea```
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
                      ```BinanceOAuth```
                      ```BybitDirect```
                      ```ParibuOAuth```
                      ```BinanceTrDirect```
                      ```BybitDirectMobile```
                      ```Sandbox```
                      ```DeFiWallet```
              includeMarketValue:
                allOf:
                  - type: boolean
            refIdentifier: '#/components/schemas/PortfolioHoldingsRequest'
            requiredProperties:
              - authToken
              - type
            additionalProperties: false
        examples:
          example:
            value:
              authToken: <string>
              type: robinhood
              includeMarketValue: true
        description: Request containing authentication token
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
                      - $ref: '#/components/schemas/HoldingsModel'
                    nullable: true
            refIdentifier: '#/components/schemas/HoldingsModelApiResult'
            additionalProperties: false
        examples:
          Trading platform example:
            value:
              content:
                equityPositions:
                  - symbol: AAPL
                    amount: 3
                    costBasis: 109
                  - symbol: F
                    amount: 27
                    costBasis: 7.05791
                cryptocurrencyPositions:
                  - marketValue: 75.15
                    lastPrice: 0.05
                    symbol: DOGE
                    amount: 1503
                    costBasis: 0.033
                  - symbol: BTC
                    amount: 3.0001672
                    costBasis: 18000
                status: succeeded
                errorMessage: ''
                displayMessage: ''
                notSupportedEquityPositions:
                  - symbol: CUSIP38259P508
                    amount: 1
                notSupportedCryptocurrencyPositions: []
                nftPositions: []
                optionPositions: []
                type: robinhood
                accountId: 5FUVPB0
                institutionName: Robinhood
                accountName: Margin account
              status: ok
              message: ''
              errorHash: 7f9b082a
              errorType: ''
          Self-custody cryptocurrency wallet example:
            value:
              content:
                equityPositions: []
                cryptocurrencyPositions:
                  - marketValue: 75.15
                    lastPrice: 0.05
                    symbol: DOGE
                    amount: 1503
                    costBasis: 0.033
                    distribution:
                      - caipNetworkId: eip155:1
                        address: '0x1111111111111111111111111111111111111111'
                        amount: 1500
                      - caipNetworkId: eip155:42161
                        address: '0x1111111111111111111111111111111111111111'
                        amount: 3
                  - symbol: BTC
                    amount: 3.0001672
                    costBasis: 18000
                    distribution:
                      - caipNetworkId: bip122:000000000019d6689c085ae165831e93
                        address: bc1q5cyxnuxmeuwuvkwfem96lxyepd5t0gd5nqf6h4
                        amount: 1
                      - caipNetworkId: bip122:000000000019d6689c085ae165831e93
                        address: bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf7du0
                        amount: 1
                      - caipNetworkId: bip122:000000000019d6689c085ae165831e93
                        address: bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh
                        amount: 1.0001672
                status: succeeded
                errorMessage: ''
                displayMessage: ''
                notSupportedEquityPositions: []
                notSupportedCryptocurrencyPositions: []
                nftPositions: []
                optionPositions: []
                type: deFiWallet
                accountId: 8c02d545753b596075ecbc20e2b7d3fb5b380c52
                institutionName: DeFiWallet
                accountName: MetaMask wallet
              status: ok
              message: ''
              errorHash: 7f9b082a
              errorType: ''
        description: Holdings obtained
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
        description: 'Unauthorized: Client Id or Client Secret are not correct or missing.'
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
    B2BNftPosition:
      type: object
      properties:
        amount:
          type: number
          format: double
        costBasis:
          type: number
          format: double
          nullable: true
        contractAddress:
          type: string
          nullable: true
        name:
          type: string
          nullable: true
        description:
          type: string
          nullable: true
        marketplaceId:
          type: string
          nullable: true
        tokenId:
          type: string
          nullable: true
        marketplacePermalink:
          type: string
          nullable: true
        addressType:
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
          allOf:
            - $ref: '#/components/schemas/CryptocurrencyAddressType'
      additionalProperties: false
    B2BOptionPosition:
      type: object
      properties:
        symbol:
          type: string
          description: Symbol of the underlying stock
          nullable: true
        amount:
          type: number
          description: Amount of options
          format: double
        averageOpenPrice:
          type: number
          description: Total average paid price
          format: double
        direction:
          enum:
            - unknown
            - buyToOpen
            - buyToClose
            - sellToOpen
            - sellToClose
            - buyToCover
            - sellShort
          allOf:
            - $ref: '#/components/schemas/BrokerOptionDirection'
          description: Side of the option, buy or sell
        createdTimestamp:
          type: integer
          format: int64
        updatedTimestamp:
          type: integer
          format: int64
        numberOfSharesInContract:
          type: number
          description: Number of shares of the underlying stock
          format: double
        optionType:
          enum:
            - unknown
            - call
            - put
          allOf:
            - $ref: '#/components/schemas/BrokerOptionType'
          description: Type of the option, put or call
        expirationTimestamp:
          type: integer
          description: The last day that the option contract is valid
          format: int64
        strikePrice:
          type: number
          description: The price at which a put or call option can be exercised
          format: double
      additionalProperties: false
    BrokerOptionDirection:
      enum:
        - unknown
        - buyToOpen
        - buyToClose
        - sellToOpen
        - sellToClose
        - buyToCover
        - sellShort
      type: string
    BrokerOptionType:
      enum:
        - unknown
        - call
        - put
      type: string
    BrokerRequestStatus:
      enum:
        - succeeded
        - failed
        - notAuthorized
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
    DeFiPositionDistribution:
      required:
        - address
        - amount
        - caipNetworkId
      type: object
      properties:
        caipNetworkId:
          type: string
          description: Cryptocurrency CAIP-2 network ID associated with this distribution.
          nullable: true
        address:
          type: string
          description: The wallet address on the specific network.
          nullable: true
        amount:
          type: number
          description: Amount of cryptocurrency allocated to this network and address.
          format: double
      additionalProperties: false
      description: "Represents the distribution of a DeFi position across different networks and addresses.\r\nThis class holds the network-specific information, wallet address, and the amount of cryptocurrency\r\nallocated to each network and address for self-custody (DeFi) wallets."
    HoldingsModel:
      type: object
      properties:
        status:
          enum:
            - succeeded
            - failed
            - notAuthorized
          allOf:
            - $ref: '#/components/schemas/BrokerRequestStatus'
          description: Status of the request to the institution's API
        errorMessage:
          type: string
          description: Error message specifying the problem
          nullable: true
        displayMessage:
          type: string
          description: User-friendly error message, optimized to be shown to the end user
          nullable: true
        notSupportedEquityPositions:
          type: array
          items:
            $ref: '#/components/schemas/Position'
          description: The equity positions Front could not recognize
          nullable: true
        notSupportedCryptocurrencyPositions:
          type: array
          items:
            $ref: '#/components/schemas/Position'
          description: The cryptocurrency positions Front could not recognize
          nullable: true
        nftPositions:
          type: array
          items:
            $ref: '#/components/schemas/B2BNftPosition'
          description: NFT holdings on the account
          nullable: true
        optionPositions:
          type: array
          items:
            $ref: '#/components/schemas/B2BOptionPosition'
          description: Option holdings on the account
          nullable: true
        type:
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
          description: Type of the institution
        accountId:
          type: string
          description: External institution's account id (returned by the institution)
          nullable: true
        institutionName:
          type: string
          description: Friendly name of the connected institution
          nullable: true
        accountName:
          type: string
          description: Name of the account as returned from the institution
          nullable: true
        equityPositions:
          type: array
          items:
            $ref: '#/components/schemas/PositionWithMarketValue'
          description: Equity holdings, such as stocks and ETFs
          nullable: true
        cryptocurrencyPositions:
          type: array
          items:
            $ref: '#/components/schemas/PositionWithMarketValue'
          description: Cryptocurrency holdings on the account
          nullable: true
      additionalProperties: false
    Position:
      type: object
      properties:
        name:
          type: string
          description: Name of the asset
          nullable: true
        symbol:
          type: string
          description: Symbol of the asset
          nullable: true
        amount:
          type: number
          description: Amount of the asset
          format: double
        costBasis:
          type: number
          description: The total original value (or purchase price) of the asset
          format: double
          nullable: true
        distribution:
          type: array
          items:
            $ref: '#/components/schemas/DeFiPositionDistribution'
          description: "Breakdown of crypto distribution across different networks and addresses.\r\nThis data is populated only for self-custody (DeFi) wallets."
          nullable: true
      additionalProperties: false
    PositionWithMarketValue:
      type: object
      properties:
        name:
          type: string
          description: Name of the asset
          nullable: true
        symbol:
          type: string
          description: Symbol of the asset
          nullable: true
        amount:
          type: number
          description: Amount of the asset
          format: double
        costBasis:
          type: number
          description: The total original value (or purchase price) of the asset
          format: double
          nullable: true
        distribution:
          type: array
          items:
            $ref: '#/components/schemas/DeFiPositionDistribution'
          description: "Breakdown of crypto distribution across different networks and addresses.\r\nThis data is populated only for self-custody (DeFi) wallets."
          nullable: true
        marketValue:
          type: number
          description: >-
            Market value of the asset: amount of asset multiplied by last asset
            value.
          format: double
          nullable: true
        lastPrice:
          type: number
          description: Current last price of the asset.
          format: double
          nullable: true
      additionalProperties: false

````