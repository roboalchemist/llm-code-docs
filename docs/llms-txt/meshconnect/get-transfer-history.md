# Source: https://docs.meshconnect.com/api-reference/transfers/get-transfer-history.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.meshconnect.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get transfer history

> Get entire history of cryptocurrency transfers (withdrawals or deposits) executed from an exchange.
Only supports Exchange integrations.



## OpenAPI

````yaml post /api/v1/transfers/list
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
  /api/v1/transfers/list:
    post:
      tags:
        - Transfers
      summary: Get transfer history
      description: "Get entire history of cryptocurrency transfers (withdrawals or deposits) executed from an exchange.\r\nOnly supports Exchange integrations."
      requestBody:
        description: >-
          Authentication token and integration type to obtain the list of
          transfers.
        content:
          application/json:
            schema:
              allOf:
                - $ref: '#/components/schemas/TransfersBrokerTransactionsListRequest'
      responses:
        '200':
          description: Transfers obtained.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/B2BBrokerTransactionsListModelApiResult'
              example:
                content:
                  transfers:
                    - id: 8E25ACB5-A9E2-4D00-8772-A255F010A2A9
                      status: succeeded
                      type: deposit
                      fromAddress: D5PumQwt...
                      targetAddress: D641Fmzx...
                      symbol: DOGE
                      hash: 3310c6202aaeb44754a118ce11f255382d012060ade0d6d9f...
                      amount: 15
                      transactionAmount: 10
                      createdTimestamp: 1653215600
                      updatedTimestamp: 1653215600
                      networkTransactionFee:
                        amount: 5
                        symbol: DOGE
                      confirmations: 17
                      blockchainMethod: transfer
                    - id: 70E6E3CF-5ACF-49C5-A4E1-5FB85A567F26
                      status: succeeded
                      type: withdrawal
                      fromAddress: 0x7BDE8361Fe587daD0e35448E754...
                      targetAddress: 0x83C8F28c26bF6aaca652Df1DbBE...
                      symbol: ETH
                      hash: 0x77f3a280aa5cfe956a5759c24cf774325504070b32b4159...
                      amount: 0.1
                      transactionAmount: 0.099
                      createdTimestamp: 1653211113
                      updatedTimestamp: 1653211113
                      networkTransactionFee:
                        amount: 0.001
                        symbol: ETH
                      confirmations: 18
                      blockchainMethod: transfer
                  total: 2
                  cursor: N2VkZDI0MDMtNmRhYy01NThhLTk5NDUDYzI12M3GQ3ZmQ2
                  earliestTimestamp: 1653211113
                status: ok
                message: ''
                errorHash: 37c012c2
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
    TransfersBrokerTransactionsListRequest:
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
        count:
          type: integer
          description: "Number of records to include in the response. \n\r\nDefault: `100` \n\r\nMaximum: `250`"
          format: int32
        cursor:
          type: string
          description: "The cursor to retrieve the next page of transactions.\r\nProviding it will cause the response to only return changes after this update.\r\nIf this field is not provided, the history of transactions will be returned starting with the first-added transaction."
          nullable: true
        statuses:
          type: array
          items:
            $ref: '#/components/schemas/BrokerCryptocurrencyTransactionStatus'
          description: >-
            If this value is provided, result set is filtered to only include
            transaction with the provided statuses.
          nullable: true
        cryptocurrencyAddressType:
          allOf:
            - $ref: '#/components/schemas/CryptocurrencyAddressType'
          description: For cryptocurrency address the type of address is required.
          nullable: true
        from:
          type: integer
          description: >-
            If this value is provided, result set is filtered to only include
            transactions created after this timestamp
          format: int64
          nullable: true
      additionalProperties: false
    B2BBrokerTransactionsListModelApiResult:
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
            - $ref: '#/components/schemas/B2BBrokerTransactionsListModel'
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
    BrokerCryptocurrencyTransactionStatus:
      enum:
        - unknown
        - failed
        - frozen
        - succeeded
        - mfaRequired
        - pending
        - expired
        - canceled
        - waitingForSignature
        - waitingForClearing
        - awaitingApproval
        - awaitingConfirmation
        - awaitingVerification
        - rejected
        - pendingCancel
        - emailVerification
        - deviceConfirmationRequired
        - mfaFailed
        - addressWhitelistRequired
        - secondMfaRequired
        - emailConfirmationApprovalRequired
        - travelRuleRequired
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
    B2BBrokerTransactionsListModel:
      type: object
      properties:
        transfers:
          type: array
          items:
            $ref: '#/components/schemas/B2BBrokerCryptocurrencyTransaction'
          description: List of obtained transfers.
          nullable: true
        total:
          type: integer
          description: Total amount of records.
          format: int64
        cursor:
          type: string
          description: The cursor to retrieve the next page of transfers.
          nullable: true
        earliestTimestamp:
          type: integer
          description: Earliest transfer timestamp.
          format: int64
      additionalProperties: false
    B2BBrokerCryptocurrencyTransaction:
      type: object
      properties:
        id:
          type: string
          description: Identifier of the transfer, if provided by the financial institution
          nullable: true
        status:
          enum:
            - unknown
            - failed
            - frozen
            - succeeded
            - mfaRequired
            - pending
            - expired
            - canceled
            - waitingForSignature
            - waitingForClearing
            - awaitingApproval
            - awaitingConfirmation
            - awaitingVerification
            - rejected
            - pendingCancel
            - emailVerification
            - deviceConfirmationRequired
            - mfaFailed
            - addressWhitelistRequired
            - secondMfaRequired
            - emailConfirmationApprovalRequired
            - travelRuleRequired
          allOf:
            - $ref: '#/components/schemas/BrokerCryptocurrencyTransactionStatus'
          description: Current status of the transaction
        statusDetails:
          type: string
          description: >-
            Details of the current status of the transfer, as provided by the
            financial institution
          nullable: true
        type:
          enum:
            - unknown
            - deposit
            - withdrawal
          allOf:
            - $ref: '#/components/schemas/BrokerCryptocurrencyTransactionType'
          description: The direction of the transaction
        fromAddress:
          type: string
          description: Address where the transaction was sent from
          nullable: true
        targetAddress:
          type: string
          description: Address where the transaction was sent to
          nullable: true
        symbol:
          type: string
          description: Ticker of the transaction
          nullable: true
        chain:
          type: string
          description: Crypto Chain the transaction belongs to
          nullable: true
        memo:
          type: string
          description: Memo of the transaction (also called "Tag")
          nullable: true
        hash:
          type: string
          description: Hash of the transaction
          nullable: true
        amount:
          type: number
          description: >-
            Full amount affected the balance, typically transaction amount plus
            fee
          format: double
        transactionAmount:
          type: number
          description: Transaction amount
          format: double
          nullable: true
        createdTimestamp:
          type: integer
          description: >-
            Unix timestamp in seconds indicating when the transaction was
            created
          format: int64
        updatedTimestamp:
          type: integer
          description: >-
            Unix timestamp in seconds indicating when the transaction was last
            updated
          format: int64
        networkTransactionFee:
          allOf:
            - $ref: '#/components/schemas/BrokerCryptocurrencyTransactionNetworkFee'
          description: Fee taken by the network
          nullable: true
        transferFee:
          type: number
          description: Fee taken by the financial institution
          format: double
          nullable: true
        confirmations:
          type: integer
          description: Number of confirmations on the blockchain
          format: int64
          nullable: true
        blockchainMethodName:
          type: string
          description: Name of the executed blockchain function based on decoded input data
          nullable: true
        blockchainMethod:
          enum:
            - transfer
            - swap
            - mint
            - withdraw
            - claimRewards
            - deposit
            - approve
            - forgeToken
            - multicall
            - migrateToken
            - claim
            - openSeaTransfer
            - cancel
            - commit
            - run
            - repay
            - execute
            - stake
            - merge
          allOf:
            - $ref: >-
                #/components/schemas/BrokerCryptocurrencyTransactionBlockchainMethod
          description: >-
            Executed blockchain function based on decoded input data. Not
            guaranteed to be identified
      additionalProperties: false
    BrokerCryptocurrencyTransactionType:
      enum:
        - unknown
        - deposit
        - withdrawal
      type: string
    BrokerCryptocurrencyTransactionNetworkFee:
      type: object
      properties:
        gasPrice:
          type: number
          format: double
          nullable: true
        gasUsed:
          type: number
          format: double
          nullable: true
        amount:
          type: number
          format: double
          nullable: true
        symbol:
          type: string
          nullable: true
      additionalProperties: false
    BrokerCryptocurrencyTransactionBlockchainMethod:
      enum:
        - transfer
        - swap
        - mint
        - withdraw
        - claimRewards
        - deposit
        - approve
        - forgeToken
        - multicall
        - migrateToken
        - claim
        - openSeaTransfer
        - cancel
        - commit
        - run
        - repay
        - execute
        - stake
        - merge
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