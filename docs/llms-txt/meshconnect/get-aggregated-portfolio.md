# Source: https://docs.meshconnect.com/api-reference/portfolio/get-aggregated-portfolio.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.meshconnect.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get aggregated portfolio

> Get the aggregated portfolio of the user containing market values.



## OpenAPI

````yaml get /api/v1/holdings/portfolio
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
  /api/v1/holdings/portfolio:
    get:
      tags:
        - Portfolio
      summary: Get aggregated portfolio
      description: Get the aggregated portfolio of the user containing market values.
      parameters:
        - name: UserId
          in: query
          description: End user ID to get the aggregated portfolio for.
          required: true
          schema:
            type: string
        - name: TimezoneOffset
          in: query
          description: >-
            Offset in second, used to calculate daily return for
            cryptocurrencies.
          schema:
            type: integer
            format: int64
      responses:
        '200':
          description: Portfolio obtained
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/B2BPortfolioModelApiResult'
              examples:
                CEX example:
                  value:
                    content:
                      portfolioCostBasis: 1819.9
                      actualPortfolioPerformance: 6.1
                      equitiesValue: 1934.78
                      cryptocurrenciesValue: 1185.12
                      nftsValue: 0
                      equityPositions:
                        - portfolioPercentage: 0.44
                          totalReturn: -1.3
                          returnPercentage: -8.67
                          companyName: Tesla
                          totalDailyReturn: 0.45
                          dailyReturnPercentage: 3.45
                          marketValue: 13.69
                          lastPrice: 214.44
                          symbol: TSLA
                          amount: 0.063
                          costBasis: 234.8
                        - portfolioPercentage: 38.98
                          totalReturn: 144.97
                          returnPercentage: 13.71
                          companyName: Apple
                          totalDailyReturn: 31.65
                          dailyReturnPercentage: 2.7
                          marketValue: 1201.67
                          lastPrice: 147.27
                          symbol: AAPL
                          amount: 8.15
                          costBasis: 129.5
                      cryptocurrencyPositions:
                        - portfolioPercentage: 11.4018
                          totalReturn: -592.6533
                          returnPercentage: -62.7737
                          companyName: Ethereum
                          totalDailyReturn: -3.6081
                          dailyReturnPercentage: -1.0162
                          marketValue: 351.457
                          lastPrice: 1350.07
                          symbol: ETH
                          amount: 0.260325
                          costBasis: 3626.66
                        - portfolioPercentage: 7.8
                          totalReturn: -85.45
                          returnPercentage: -26.2
                          companyName: Dogecoin
                          totalDailyReturn: -2.45
                          dailyReturnPercentage: -1.0103
                          marketValue: 240.5754
                          lastPrice: 0.05977
                          symbol: DOGE
                          amount: 4025.02
                          costBasis: 0.081
                      nftPositions: []
                    status: ok
                    message: ''
                    errorHash: 7f9b082a
                    errorType: ''
                Self-custody cryptocurrency wallet example:
                  value:
                    content:
                      portfolioCostBasis: 3626.74
                      actualPortfolioPerformance: 5.4
                      equitiesValue: 0
                      cryptocurrenciesValue: 592.03
                      nftsValue: 0
                      equityPositions: []
                      cryptocurrencyPositions:
                        - portfolioPercentage: 11.4018
                          totalReturn: -592.6533
                          returnPercentage: -62.7737
                          companyName: Ethereum
                          totalDailyReturn: -3.6081
                          dailyReturnPercentage: -1.0162
                          marketValue: 351.457
                          lastPrice: 1350.07
                          symbol: ETH
                          amount: 0.260325
                          costBasis: 3626.66
                          distribution:
                            - caipNetworkId: eip155:1
                              address: '0x1111111111111111111111111111111111111111'
                              amount: 0.16
                            - caipNetworkId: eip155:42161
                              address: '0x1111111111111111111111111111111111111111'
                              amount: 0.100325
                        - portfolioPercentage: 7.8
                          totalReturn: -85.45
                          returnPercentage: -26.2
                          companyName: Dogecoin
                          totalDailyReturn: -2.45
                          dailyReturnPercentage: -1.0103
                          marketValue: 240.5754
                          lastPrice: 0.05977
                          symbol: DOGE
                          amount: 4025.02
                          costBasis: 0.081
                          distribution:
                            - caipNetworkId: eip155:1
                              address: '0x1111111111111111111111111111111111111111'
                              amount: 2025.02
                            - caipNetworkId: eip155:42161
                              address: '0x1111111111111111111111111111111111111111'
                              amount: 2000
                      nftPositions: []
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
                status: ok
                message: ''
                errorHash: f6fc87aa
                errorType: ''
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
    B2BPortfolioModelApiResult:
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
            - $ref: '#/components/schemas/B2BPortfolioModel'
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
    B2BPortfolioModel:
      type: object
      properties:
        portfolioCostBasis:
          type: number
          description: Amount of money spent to buy all positions of the portfolio.
          format: double
          nullable: true
        actualPortfolioPerformance:
          type: number
          description: Actual performance based on the cost basis.
          format: double
          nullable: true
        equitiesValue:
          type: number
          description: >-
            Total USD portfolio value of all equities (sum(equity price * equity
            amount)). Does not include cash balance.
          format: double
        cryptocurrenciesValue:
          type: number
          description: Total USD value of all cryptocurrencies in the portfolio.
          format: double
        nftsValue:
          type: number
          description: Total USD value of all NFTs in the portfolio.
          format: double
        equityPositions:
          type: array
          items:
            $ref: '#/components/schemas/PositionWithReturn'
          description: List of equity positions
          nullable: true
        cryptocurrencyPositions:
          type: array
          items:
            $ref: '#/components/schemas/PositionWithReturn'
          description: List of cryptocurrency positions
          nullable: true
        nftPositions:
          type: array
          items:
            $ref: '#/components/schemas/NftPositionWithMarketValues'
          description: List of NFT positions
          nullable: true
      additionalProperties: false
    PositionWithReturn:
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
        portfolioPercentage:
          type: number
          description: What percentage of total portfolio value is taken by this asset.
          format: double
          nullable: true
        totalReturn:
          type: number
          description: "Total return of investment of this asset. Can be negative or null. Based on the cost basis of the asset, cost basis\r\nis not available by some of integrations."
          format: double
          nullable: true
        returnPercentage:
          type: number
          description: >-
            Percent of return of investment for this asset. Can be negative or
            null.
          format: double
          nullable: true
        companyName:
          type: string
          description: Company name of the relative asset.
          nullable: true
        totalDailyReturn:
          type: number
          description: Total daily return of investment for this asset. Can be negative.
          format: double
          nullable: true
        dailyReturnPercentage:
          type: number
          description: >-
            Daily percent of return of investment for this asset. Can be
            negative.
          format: double
          nullable: true
      additionalProperties: false
    NftPositionWithMarketValues:
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
        paymentTokenSymbol:
          type: string
          nullable: true
        name:
          type: string
          nullable: true
        description:
          type: string
          nullable: true
        imageUrl:
          type: string
          nullable: true
        imageOriginalUrl:
          type: string
          nullable: true
        animationUrl:
          type: string
          nullable: true
        backgroundColor:
          type: string
          nullable: true
        marketplaceId:
          type: string
          nullable: true
        tokenId:
          type: string
          nullable: true
        numberOfSales:
          type: integer
          format: int64
          nullable: true
        contractType:
          type: string
          nullable: true
        contractName:
          type: string
          nullable: true
        contractSchemaName:
          type: string
          nullable: true
        contractSymbol:
          type: string
          nullable: true
        contractDescription:
          type: string
          nullable: true
        marketplacePermalink:
          type: string
          nullable: true
        contractExternalLink:
          type: string
          nullable: true
        creatorAddress:
          type: string
          nullable: true
        currentOffer:
          allOf:
            - $ref: '#/components/schemas/NftOrder'
          nullable: true
        lastSale:
          allOf:
            - $ref: '#/components/schemas/NftOrder'
          nullable: true
        blockchain:
          enum:
            - ethereum
            - polygon
            - klaytn
          allOf:
            - $ref: '#/components/schemas/NftBlockchain'
        addressExplorerLink:
          type: string
          nullable: true
        twitterUsername:
          type: string
          nullable: true
        marketValue:
          type: number
          description: Amount of NFTs multiplied by NFT value
          format: double
          nullable: true
        portfolioPercentage:
          type: number
          description: What percentage of total portfolio value is taken by this NFT
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
    NftOrder:
      type: object
      properties:
        orderSide:
          enum:
            - buy
            - sell
          allOf:
            - $ref: '#/components/schemas/NftOrderSide'
        symbol:
          type: string
          nullable: true
        price:
          type: number
          format: double
        priceUsd:
          type: number
          format: double
          nullable: true
        amount:
          type: number
          format: double
        createdTimestamp:
          type: integer
          format: int64
          nullable: true
        updatedTimestamp:
          type: integer
          format: int64
          nullable: true
        symbolLogo:
          type: string
          nullable: true
      additionalProperties: false
    NftBlockchain:
      enum:
        - ethereum
        - polygon
        - klaytn
      type: string
    NftOrderSide:
      enum:
        - buy
        - sell
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