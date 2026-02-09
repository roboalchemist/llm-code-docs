# Source: https://docs.meshconnect.com/api-reference/portfolio/get-holdings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.meshconnect.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get holdings.

> Obtain assets from the connected investment account. Performs realtime API call to the underlying integration.



## OpenAPI

````yaml post /api/v1/holdings/get
openapi: 3.0.1
info:
  title: Mesh Connect Integration API
  description: >-

    Mesh allows users to connect accounts of financial institutions,

    crypto exchanges, and self-custody wallets. Mesh handles credential

    validation, MFA, and error handling for each integration. After

    an account is connected, Mesh allows client applications to read holdings,

    transaction history and balances and execute crypto transfers (with user
    approval).
  version: '1.0'
servers:
  - url: https://integration-api.meshconnect.com
  - url: https://sandbox-integration-api.meshconnect.com
security:
  - Client-Secret: []
    Client-Id: []
tags:
  - name: QuickNode
  - name: Integrations account information
  - name: Managed Account Authentication
    description: >-
      The recommended approach for account authentication. Front manages
      multiple authentication flows and handles all authentication steps such as
      MFA codes and OAuth redirect through our web and mobile SDKs.
  - name: Self Managed Account Authentication
    description: >-
      Not recommended approach. Using this approach, the API client is
      responsible for handling multiple authentication flows and supporting
      future updates and changes.
  - name: Portfolio
    description: |


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
      ```Uphold```
      ```SandboxCoinbase```
      ```DeFiWallet```
  - name: Balance
    description: |


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
      ```Uphold```
      ```SandboxCoinbase```
  - name: Transactions
    description: >


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

      ```Bybit```

      ```CoinbasePrime```

      ```RobinhoodConnect```

      ```Sandbox```

      ```Uphold```

      ```SandboxCoinbase```



      ### Integration-specific notes:



      #### Binance:



      Because of limitations of Binance API, initial loading of transaction
      history in Binance can take long time


      depending on the size of the portfolio.



      #### OkCoin:



      Getting transactions history from OkCoin is not currently supported.
  - name: Transfers
    description: >


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

      ```Uphold```

      ```BinancePayOnchain```

      ```SandboxCoinbase```

      ```BybitPay```

      ```DeFiWallet```



      ### Integration-specific notes:



      #### Robinhood:



      Cryptocurrency transfers should be enabled in Robinhood settings.
      Transfers are disabled by default, enabling them for end users requires a
      review from Robinhood.


      Please note:
       * `MfaCode` parameter is required to initiate a transaction in Robinhood.
       * The user's security settings should be configured to use an authenticator application.
       * Robinhood doesn't allow initiation of transactions if the authenticator application is not configured.


      #### Coinbase:



      `MfaCode` parameter should be used to initiate transactions in Coinbase.
       * If the end user's Coinbase account is configured to use text messages (SMS) for two factor authentication, the API will return `MfaRequired` status, and a text code will then be sent by Coinbase. The code is expected to be provided in the subsequent call using the `MfaCode` request field
       * If the account is configured to use an authenticator application, the API is expecting to get the code in the `MfaCode` request field.


      #### Kraken:



      Kraken requires the explicit chain name to be provided (e.g. `Dogecoin` or
      `Ethereum (ERC20)`). The list of possible chains can be obtained by
      calling `symbol/details` endpoint.


      To initiate a transaction, a Kraken Address Key name should be provided in
      `TargetAddress` field. Target address should be added using Kraken UI,
      then its name should be used.



      #### Binance:



      `Enable Withdrawals` permission should be given to the user's API key to
      initiate transfers with Binance Us.


      Binance requires adding the IP address to the list of trusted IPs to be
      able to create API keys with transfer permission.
       * Please reach out to Front to get the static IP address. This address should be provided to the end user, and the user should be instructed to add it to the list of trusted IP addresses.
       * By default, the permission to enable withdrawals is turned off. If the end user's API key does not have the permission, asset transfers will not be available.


      #### KuCoin:



      KuCoin requires adding the IP address to the list of trusted IPs to be
      able to create API keys with transfer permission.


      `Fee` parameter should be used to initiate a transaction in KuCoin.


      Please note:
       * Please reach out to Front to get the static IP address. This address should be provided to the end user, and the user should be instructed to add it to the list of trusted IP addresses.
       * All currencies have their minimum `fee` and `amount` requirements. Please use `symbol/details` endpoint to get this data for a particular symbol.
       * KuCoin requires chain name to be provided for getting deposit address or initiating a cryptocurrency transfer. Some cryptocurrencies are supported over multiple chains. It's recommended to use `symbol/details` endpoint to get the list of supported chains and show it to the end user to select a target one.


      #### BinanceInternational:



      `Enable Withdrawals` permission should be given to the user's API key to
      initiate transfers with Binance International.


      Binance requires adding the IP address to the list of trusted IPs to be
      able to create API keys with transfer permission.
       * Please reach out to Front to get the static IP address. This address should be provided to the end user, and the user should be instructed to add it to the list of trusted IP addresses.
       * By default, the permission to enable withdrawals is turned off. If the end user's API key does not have the permission, asset transfers will not be available.


      #### GateIo:



      Gate.io requires adding IP address to the list of trusted IP addresses to
      be able to initiate a cryptocurrency transfers.


      Withdrawal address should be already verified or added on the Gate.io UI
      (in mobile application or on the web site).
       * Please reach out to Front to get the static IP address for withdrawals. This address should be provided to the end user, and the user should be instructed to add it to the list of trusted IP addresses.
       * Only verified withdrawal blockchain addresses are allowed for withdrawal with Gate.io API.
       * Gate.io requires chain name to be provided for getting deposit address or initiating a cryptocurrency transfer. Some cryptocurrencies are supported over multiple chains. It's recommended to use `symbol/details` endpoint to get the list of supported chains and show it to the end user to select a target one.


      #### Huobi:



      Warning: Huobi does not refund executed deposits that are below the
      `Minimum Deposit Amount`
       * Please check the MinimumDepositAmount in Get Deposit Address response in order to avoid making a deposit below the minimum amount
       * Huobi does not allow withdrawals to addresses that are not white-listed, please add the address that you would like to withdraw to the white list of addresses through the UI so that a withrawal can be processed


      #### Bitfinex:
       * The hash of transfer is not available when making a transfer in Bitfinex. To get the hash please re-query the transfer using the transaction id.
       * Bitfinex does not separate sub-accounts when returning the list of transfers.Therefore the same list of transfers is returned for all Bitfinex sub-accounts.


      #### KrakenDirect:



      Kraken requires the explicit chain name to be provided (e.g. `Dogecoin` or
      `Ethereum (ERC20)`). The list of possible chains can be obtained by
      calling `symbol/details` endpoint.


      To initiate a transaction, a Kraken Address Key name should be provided in
      `TargetAddress` field. Target address should be added using Kraken UI,
      then its name should be used.



      #### BitfinexDirect:
       * The hash of transfer is not available when making a transfer in Bitfinex. To get the hash please re-query the transfer using the transaction id.
       * Bitfinex does not separate sub-accounts when returning the list of transfers.Therefore the same list of transfers is returned for all Bitfinex sub-accounts.
  - name: Assets
  - name: Managed Transfers
  - name: Wallets
paths:
  /api/v1/holdings/get:
    post:
      tags:
        - Portfolio
      summary: Get holdings.
      description: >-
        Obtain assets from the connected investment account. Performs realtime
        API call to the underlying integration.
      requestBody:
        description: Request containing authentication token
        content:
          application/json:
            schema:
              allOf:
                - $ref: '#/components/schemas/PortfolioHoldingsRequest'
      responses:
        '200':
          description: Holdings obtained
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HoldingsModelApiResult'
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
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiResult'
              example:
                status: badRequest
                message: Error message
                displayMessage: Optional display message
                errorHash: 7dcbb73d
                errorType: missingField
        '401':
          description: 'Unauthorized: Client Id or Client Secret are not correct or missing.'
          content:
            application/json:
              schema: {}
        '403':
          description: >-
            The API key used does not have read permission to call this Mesh
            endpoint.
          content:
            application/json:
              schema: {}
components:
  schemas:
    PortfolioHoldingsRequest:
      required:
        - authToken
        - type
      type: object
      properties:
        authToken:
          minLength: 1
          type: string
          description: Auth token that allows connecting to the target institution
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
            - uphold
            - binancePayOnchain
            - sandboxCoinbase
            - bybitPay
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
            ```Uphold```
            ```SandboxCoinbase```
            ```DeFiWallet```
        includeMarketValue:
          type: boolean
      additionalProperties: false
    HoldingsModelApiResult:
      type: object
      properties:
        status:
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
          type: string
          description: A message generated by the API
          nullable: true
        displayMessage:
          type: string
          description: User-friendly display message that can be presented to the end user
          nullable: true
        errorHash:
          type: string
          description: >-
            An error grouping hash from string components and caller
            information. Used by bugsnag on FE for correct error grouping
          nullable: true
          readOnly: true
        errorType:
          type: string
          description: "Strictly-typed error type that is explaining the reason of an unsuccessful status of the operation.\r\nAll possible error types are available in the documentation."
          nullable: true
        errorData:
          nullable: true
          readOnly: true
        content:
          allOf:
            - $ref: '#/components/schemas/HoldingsModel'
          nullable: true
      additionalProperties: false
    ApiResult:
      type: object
      properties:
        status:
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
          type: string
          description: A message generated by the API
          nullable: true
        displayMessage:
          type: string
          description: User-friendly display message that can be presented to the end user
          nullable: true
        errorHash:
          type: string
          description: >-
            An error grouping hash from string components and caller
            information. Used by bugsnag on FE for correct error grouping
          nullable: true
          readOnly: true
        errorType:
          type: string
          description: "Strictly-typed error type that is explaining the reason of an unsuccessful status of the operation.\r\nAll possible error types are available in the documentation."
          nullable: true
        errorData:
          nullable: true
          readOnly: true
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
        - uphold
        - binancePayOnchain
        - sandboxCoinbase
        - bybitPay
      type: string
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
            - uphold
            - binancePayOnchain
            - sandboxCoinbase
            - bybitPay
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
    BrokerRequestStatus:
      enum:
        - succeeded
        - failed
        - notAuthorized
      type: string
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
  securitySchemes:
    Client-Secret:
      type: apiKey
      description: Contact Mesh to get client Secret
      name: X-Client-Secret
      in: header
    Client-Id:
      type: apiKey
      description: Contact Mesh to get client Id
      name: X-Client-Id
      in: header

````