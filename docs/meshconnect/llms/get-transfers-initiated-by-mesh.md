# Source: https://docs.meshconnect.com/api-reference/managed-transfers/get-transfers-initiated-by-mesh.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.meshconnect.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get transfers initiated by Mesh

> Get cryptocurrency transfers initiated by Mesh on exchanges or self-custody wallets.



## OpenAPI

````yaml get /api/v1/transfers/managed/mesh
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
  /api/v1/transfers/managed/mesh:
    get:
      tags:
        - Managed Transfers
      summary: Get transfers initiated by Mesh
      description: >-
        Get cryptocurrency transfers initiated by Mesh on exchanges or
        self-custody wallets.
      parameters:
        - name: Count
          in: query
          description: Number of items to return. Default 10, maximum - 100.
          schema:
            type: integer
            format: int32
        - name: Offset
          in: query
          description: Number of items to skip.
          schema:
            type: integer
            format: int32
        - name: Id
          in: query
          description: Mesh transfer identifier.
          schema:
            type: string
            format: uuid
        - name: ClientTransactionId
          in: query
          description: Client transaction identifier.
          schema:
            maxLength: 128
            minLength: 0
            type: string
        - name: UserId
          in: query
          description: Client's user identifier.
          schema:
            maxLength: 50
            minLength: 0
            type: string
        - name: IntegrationIds
          in: query
          description: Transfered integration.
          schema:
            maxItems: 100
            type: array
            items:
              type: string
              format: uuid
        - name: Statuses
          in: query
          description: Transfer statuses.
          schema:
            maxItems: 5
            type: array
            items:
              $ref: '#/components/schemas/TransferStatus'
        - name: FromTimestamp
          in: query
          description: Transfer created minimum timestamp.
          schema:
            type: integer
            format: int64
        - name: ToTimestamp
          in: query
          description: Transfer created maximum timestamp.
          schema:
            type: integer
            format: int64
        - name: MinAmountInFiat
          in: query
          description: Minimum amount in fiat.
          schema:
            type: number
            format: double
        - name: MaxAmountInFiat
          in: query
          description: Maximum amount in fiat.
          schema:
            type: number
            format: double
        - name: OrderBy
          in: query
          description: Order by column.
          schema:
            allOf:
              - $ref: '#/components/schemas/TransferOrderByFields'
        - name: Hash
          in: query
          description: Transfer hash.
          schema:
            type: string
        - name: SubClientId
          in: query
          description: Sub-client identifier.
          schema:
            type: string
            format: uuid
        - name: DescendingOrder
          in: query
          description: Value indicating if ordering is descending.
          schema:
            type: boolean
        - name: IsSandBox
          in: query
          description: Value indicating if Env is Sandbox.
          schema:
            type: boolean
        - name: IncludeRefundInformation
          in: query
          description: "When true, includes refund information (summary and details) in the response.\r\nThis includes partial refund data with transaction hashes, statuses, and amounts.\r\nDefault is false for backward compatibility."
          schema:
            type: boolean
      responses:
        '200':
          description: Transfers obtained.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TransferModelPaginationResponseApiResult'
              example:
                content:
                  items:
                    - userId: '123456798'
                      amountToReceive: 0
                      networkId: 00000000-0000-0000-0000-000000000000
                      networkLogoUrl: >-
                        https://file-cdn.meshconnect.com/public/logos/networks/Polygon.svg
                      infoUrl: >-
                        https://polygonscan.com/tx/0x5b0ac59e43b63f2985d78994b6270d747f1019777201ca18ebb36ad1e1a8693e
                      from:
                        logoUrl: https://logo.com/logo.jpg
                        id: 8e25acb5-a9e2-4d00-8772-a255f010a2a9
                        type: robinhood
                        name: Robinhood
                      sourceAmount: 10.122
                      destinationAmount: 10
                      totalFeesAmountInFiat: 0.5
                      totalTransactionAmountInFiat: 1000.5
                      fundingMethods:
                        - type: cryptocurrencyConversion
                          amount: 2
                          amountInFiat: 20
                          toSymbol: WETH
                          fromAmount: 1
                          fromSymbol: BTC
                          fee:
                            fee: 0.0001
                            feeCurrency: ETH
                            feeInFiat: 0.1
                            feeInTransferCurrency: 0
                        - type: paymentMethodDepositUsage
                          amount: 3
                          amountInFiat: 30
                          toSymbol: WETH
                          fromAmount: 1
                          fromSymbol: USD
                          paymentMethodType: bankAccount
                          fee:
                            fee: 0.0001
                            feeCurrency: USD
                            feeInFiat: 0.1
                            feeInTransferCurrency: 0
                        - type: existingCryptocurrencyBalance
                          amount: 5
                          amountInFiat: 50
                          toSymbol: WETH
                          fromAmount: 5
                          fromSymbol: ETH
                      id: 8e25acb5-a9e2-4d00-8772-a255f010a2a9
                      clientTransactionId: '123456'
                      institutionTransactionId: '456789'
                      status: succeeded
                      amountInFiat: 1000.3
                      amountToReceiveInFiat: 0
                      amountInFiatCurrencyCode: USD
                      amount: 10.123
                      symbol: WETH
                      tokenAddress: '0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619'
                      networkName: Polygon
                      createdTimestamp: 1653211113
                      hash: 0x77f3a280aa5cfe956a5759c24cf774325504070b32b4159...
                      gasFee:
                        fee: 0.0001
                        feeCurrency: MATIC
                        feeInFiat: 0.1
                        feeInTransferCurrency: 0
                      withdrawalFee:
                        fee: 0.0001
                        feeCurrency: WETH
                        feeInFiat: 0.1
                        feeInTransferCurrency: 0
                      processingFee:
                        fee: 0.0001
                        feeCurrency: WETH
                        feeInFiat: 0.1
                        feeInTransferCurrency: 0
                      executedTimestamp: 1707462614
                      transferType: payment
                      isFeeIncluded: false
                      isSmartFundingTransfer: false
                      unitPrice: 0
                      requestedTransferAmount: 0
                      isBridgingTransfer: false
                    - userId: '123456798'
                      amountToReceive: 0
                      networkId: 00000000-0000-0000-0000-000000000000
                      from:
                        logoUrl: https://logo.com/logo.jpg
                        id: 8e25acb5-a9e2-4d00-8772-a255f010a2a9
                        type: deFiWallet
                        name: MetaMask
                      totalFeesAmountInFiat: 0
                      totalTransactionAmountInFiat: 10.3
                      fundingMethods: []
                      id: 12345678-a9e2-4d00-8772-a255f010a2a9
                      clientTransactionId: '123456'
                      institutionTransactionId: '456789'
                      status: failed
                      amountInFiat: 10.3
                      amountToReceiveInFiat: 0
                      amountInFiatCurrencyCode: USD
                      amount: 0.123
                      symbol: WETH
                      tokenAddress: '0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619'
                      networkName: Polygon
                      createdTimestamp: 1653211113
                      hash: 0x77f3a280aa5cfe956a5759c24cf774325504070b32b4159...
                      isFeeIncluded: false
                      isSmartFundingTransfer: false
                      unitPrice: 0
                      requestedTransferAmount: 0
                      isBridgingTransfer: false
                  total: 10
                  range:
                    start: 0
                    end: -1
                    isValid: false
                    count: 0
                  hasMorePages: true
                status: ok
                message: ''
                errorHash: bf6d53f3
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
components:
  schemas:
    TransferStatus:
      enum:
        - pending
        - succeeded
        - failed
      type: string
    TransferOrderByFields:
      enum:
        - id
        - clientTransferId
        - userId
        - fromType
        - amountInFiat
        - status
        - createdTimestamp
        - symbol
        - networkName
      type: string
    TransferModelPaginationResponseApiResult:
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
            - $ref: '#/components/schemas/TransferModelPaginationResponse'
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
    TransferModelPaginationResponse:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/TransferModel'
          description: list of items
          nullable: true
        total:
          type: integer
          description: Total number of items
          format: int64
        range:
          allOf:
            - $ref: '#/components/schemas/IndexRange'
          description: >-
            A zero indexed based range that indicates the current start item
            index and end item index set
          nullable: true
        hasMorePages:
          type: boolean
          readOnly: true
      additionalProperties: false
    TransferModel:
      required:
        - id
      type: object
      properties:
        id:
          type: string
          description: Mesh transfer identifier.
          format: uuid
        clientTransactionId:
          type: string
          description: Client transaction identifier.
          nullable: true
        institutionTransactionId:
          type: string
          description: Integration transaction identifier.
          nullable: true
        status:
          enum:
            - pending
            - succeeded
            - failed
          allOf:
            - $ref: '#/components/schemas/TransferStatus'
          description: Transfer status.
        amountInFiat:
          type: number
          description: Transfer amount in fiat.
          format: double
        amountToReceiveInFiat:
          type: number
          description: Actual transfer amount without fees in fiat.
          format: double
        amountInFiatCurrencyCode:
          type: string
          description: Transfer amount in fiat currency code.
          nullable: true
        amount:
          type: number
          description: Transfer amount.
          format: double
        symbol:
          type: string
          description: Transfer cryptocurrency symbol.
          nullable: true
        tokenAddress:
          type: string
          description: Transfer cryptocurrency token contract address (e.g., for ERC20s).
          nullable: true
        networkName:
          type: string
          description: Transfer network name.
          nullable: true
        createdTimestamp:
          type: integer
          description: Created timestamp.
          format: int64
        hash:
          type: string
          description: Transfer hash.
          nullable: true
        subClientId:
          type: string
          description: Sub-client identifier.
          format: uuid
          nullable: true
        clientId:
          type: string
          description: Client identifier.
          format: uuid
          nullable: true
        companyName:
          type: string
          description: Company name
          nullable: true
        gasFee:
          allOf:
            - $ref: '#/components/schemas/TransferFee'
          description: Transfer network gas fee.
          nullable: true
        withdrawalFee:
          allOf:
            - $ref: '#/components/schemas/TransferFee'
          description: Financial institution withdrawal fee.
          nullable: true
        processingFee:
          allOf:
            - $ref: '#/components/schemas/TransferFee'
          description: Transfer processing fee.
          nullable: true
        executedTimestamp:
          type: integer
          description: Transfer executed Unix timestamp.
          format: int64
          nullable: true
        transferType:
          allOf:
            - $ref: '#/components/schemas/TransferTypeEnum'
          description: Type of a transfer.
          nullable: true
        isFeeIncluded:
          type: boolean
          description: Is fee included.
        destinationAddress:
          type: string
          description: Transfer Destination Address.
          nullable: true
        addressTag:
          type: string
          description: Transfer Destination Address Tag.
          nullable: true
        isSmartFundingTransfer:
          type: boolean
          description: >-
            Indicates whether this transfer is part of a smart funding
            operation.
        unitPrice:
          type: number
          description: Unit price of the cryptocurrency in fiat at the time of transfer.
          format: double
        requestedTransferAmount:
          type: number
          description: The exact amount requested for transfer before any fees are applied.
          format: double
        refundAddress:
          type: string
          description: Transfer Refund Address.
          nullable: true
        isBridgingTransfer:
          type: boolean
          description: >-
            Indicates whether this transfer involves bridging between different
            blockchain networks.
        userId:
          type: string
          description: Client's user identifier.
          nullable: true
        amountToReceive:
          type: number
          description: Actual transfer amount without fees.
          format: double
        networkId:
          type: string
          description: Id of the transfer network.
          format: uuid
        networkLogoUrl:
          type: string
          description: Network logo URL.
          nullable: true
        infoUrl:
          type: string
          description: Transfer info url on blockchain explorer.
          format: uri
          nullable: true
        from:
          allOf:
            - $ref: '#/components/schemas/TransferIntegrationWithLogoModel'
          nullable: true
        sourceAmount:
          type: number
          description: Amount what was actually transferred from source account.
          format: double
          nullable: true
        destinationAmount:
          type: number
          description: Amount what destination actually received.
          format: double
          nullable: true
        destinationAmountInFiat:
          type: number
          description: Amount in fiat what destination actually received.
          format: double
          nullable: true
        totalFeesAmountInFiat:
          type: number
          description: Total fees paid by user to execute this transaction.
          format: double
          readOnly: true
        totalTransactionAmountInFiat:
          type: number
          description: Total fiat transaction amount in origin integration.
          format: double
          readOnly: true
        fundingMethods:
          type: array
          items:
            $ref: '#/components/schemas/TransferFundingModel'
          description: The funding methods that were used to fund the transaction.
          nullable: true
        bridgingDetails:
          allOf:
            - $ref: '#/components/schemas/BridgingTransferDetailsModel'
          description: Bridging operation details.
          nullable: true
      additionalProperties: false
    IndexRange:
      type: object
      properties:
        start:
          type: integer
          description: The zero-based start index (inclusive)
          format: int64
        end:
          type: integer
          description: The zero-based end index (inclusive)
          format: int64
        isValid:
          type: boolean
          readOnly: true
        count:
          type: integer
          format: int64
          readOnly: true
      additionalProperties: false
      description: Represents a zero-based index range
    TransferFee:
      type: object
      properties:
        fee:
          type: number
          description: The amount of the fee.
          format: double
        feeCurrency:
          type: string
          description: >-
            The currency of the fee. Does not match the currency of the transfer
            in some cases.
          nullable: true
        feeInFiat:
          type: number
          description: The value of the fee converted to the fiat currency.
          format: double
        feeInTransferCurrency:
          type: number
          description: The value of the fee converted to the transfer currency.
          format: double
      additionalProperties: false
    TransferTypeEnum:
      enum:
        - deposit
        - payment
        - onramp
      type: string
    TransferIntegrationWithLogoModel:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier of integration.
          format: uuid
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
          description: Type of integration.
        name:
          type: string
          description: Name of integration.
          nullable: true
        logoUrl:
          type: string
          description: Integration logo URL.
          nullable: true
      additionalProperties: false
    TransferFundingModel:
      type: object
      properties:
        type:
          enum:
            - existingCryptocurrencyBalance
            - buyingPowerPurchase
            - paymentMethodDepositUsage
            - cryptocurrencyConversion
            - stableCoinNoFeeConversion
            - cryptocurrencyBuyingPowerConversion
            - cryptocurrencyMultiStepConversion
          allOf:
            - $ref: '#/components/schemas/CryptocurrencyFundingOptionType'
          description: Type of the funding method.
        amount:
          type: number
          description: Amount funded.
          format: double
        amountInFiat:
          type: number
          description: Amount in fiat.
          format: double
        toSymbol:
          type: string
          description: Symbol purchased.
          nullable: true
        fromAmount:
          type: number
          description: Amount used.
          format: double
        fromSymbol:
          type: string
          description: Symbol used.
          nullable: true
        paymentMethodType:
          allOf:
            - $ref: '#/components/schemas/BrokerPaymentMethodType'
          description: Payment method type
          nullable: true
        fee:
          allOf:
            - $ref: '#/components/schemas/TransferFee'
          description: Fee of funding.
          nullable: true
      additionalProperties: false
      description: Funding method model.
    BridgingTransferDetailsModel:
      type: object
      properties:
        status:
          enum:
            - recordCreated
            - registeredInProvider
            - sourceTransferStarted
            - inReview
            - providerAwaitingSourceTransfer
            - providerFundsReceived
            - providerProcessingPayment
            - providerProcessedPayment
            - providerSetUndeliverable
            - returned
            - refundRegisteredInProvider
            - providerAwaitingSourceRefundTransfer
            - providerRefundFundsReceived
            - providerProcessingRefundPayment
            - providerProcessedRefundPayment
            - refunded
            - canceled
            - failed
          allOf:
            - $ref: '#/components/schemas/BridgingOperationStatus'
        statusDescription:
          type: string
          nullable: true
        targetSide:
          allOf:
            - $ref: '#/components/schemas/BridgingTransferSide'
          nullable: true
        sourceSide:
          allOf:
            - $ref: '#/components/schemas/BridgingTransferSide'
          nullable: true
        timeline:
          type: array
          items:
            $ref: '#/components/schemas/BridgingTimelineEvent'
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
        - uphold
        - binancePayOnchain
        - sandboxCoinbase
        - bybitPay
      type: string
    CryptocurrencyFundingOptionType:
      enum:
        - existingCryptocurrencyBalance
        - buyingPowerPurchase
        - paymentMethodDepositUsage
        - cryptocurrencyConversion
        - stableCoinNoFeeConversion
        - cryptocurrencyBuyingPowerConversion
        - cryptocurrencyMultiStepConversion
      type: string
    BrokerPaymentMethodType:
      enum:
        - card
        - bankAccount
        - digitalWallet
        - unknown
      type: string
    BridgingOperationStatus:
      enum:
        - recordCreated
        - registeredInProvider
        - sourceTransferStarted
        - inReview
        - providerAwaitingSourceTransfer
        - providerFundsReceived
        - providerProcessingPayment
        - providerProcessedPayment
        - providerSetUndeliverable
        - returned
        - refundRegisteredInProvider
        - providerAwaitingSourceRefundTransfer
        - providerRefundFundsReceived
        - providerProcessingRefundPayment
        - providerProcessedRefundPayment
        - refunded
        - canceled
        - failed
      type: string
    BridgingTransferSide:
      type: object
      properties:
        networkName:
          type: string
          nullable: true
        symbol:
          type: string
          nullable: true
        amount:
          type: number
          format: double
        transactionHash:
          type: string
          nullable: true
        infoUrl:
          type: string
          format: uri
          nullable: true
      additionalProperties: false
    BridgingTimelineEvent:
      type: object
      properties:
        eventType:
          type: string
          nullable: true
        description:
          type: string
          nullable: true
        timestamp:
          type: integer
          format: int64
      additionalProperties: false
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