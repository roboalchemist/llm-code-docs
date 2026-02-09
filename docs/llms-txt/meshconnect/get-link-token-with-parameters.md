# Source: https://docs.meshconnect.com/api-reference/managed-account-authentication/get-link-token-with-parameters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.meshconnect.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Link token with parameters

> Get a short lived, one-time use token for initializing a Link session using the client-side SDKs



## OpenAPI

````yaml post /api/v1/linktoken
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
  /api/v1/linktoken:
    post:
      tags:
        - Managed Account Authentication
      summary: Get Link token with parameters
      description: >-
        Get a short lived, one-time use token for initializing a Link session
        using the client-side SDKs
      requestBody:
        description: Create Link token request.
        content:
          application/json:
            schema:
              allOf:
                - $ref: '#/components/schemas/GetLinkTokenRequest'
            example:
              userId: UserId
              configurationId: 18a20b11-e47f-43b9-8546-94284e9ee547
              restrictMultipleAccounts: true
              transferOptions:
                toAddresses:
                  - networkId: e3c7fdd8-b1fc-4e51-85ae-bb276e075611
                    symbol: ETH
                    address: '0x00000000000000000000000'
                  - networkId: e3c7fdd8-b1fc-4e51-85ae-bb276e075611
                    symbol: USDC
                    address: '0x00000000000000000000000'
                  - networkId: 7436e9d0-ba42-4d2b-b4c0-8e4e606b2c12
                    symbol: MATIC
                    address: '0x00000000000000000000000'
                  - networkId: 7436e9d0-ba42-4d2b-b4c0-8e4e606b2c12
                    symbol: USDC
                    address: '0x00000000000000000000000'
                amountInFiat: 10
                isInclusiveFeeEnabled: false
                generatePayLink: false
              disableApiKeyGeneration: false
          text/json:
            schema:
              allOf:
                - $ref: '#/components/schemas/GetLinkTokenRequest'
            example:
              userId: UserId
              configurationId: 18a20b11-e47f-43b9-8546-94284e9ee547
              restrictMultipleAccounts: true
              transferOptions:
                toAddresses:
                  - networkId: e3c7fdd8-b1fc-4e51-85ae-bb276e075611
                    symbol: ETH
                    address: '0x00000000000000000000000'
                  - networkId: e3c7fdd8-b1fc-4e51-85ae-bb276e075611
                    symbol: USDC
                    address: '0x00000000000000000000000'
                  - networkId: 7436e9d0-ba42-4d2b-b4c0-8e4e606b2c12
                    symbol: MATIC
                    address: '0x00000000000000000000000'
                  - networkId: 7436e9d0-ba42-4d2b-b4c0-8e4e606b2c12
                    symbol: USDC
                    address: '0x00000000000000000000000'
                amountInFiat: 10
                isInclusiveFeeEnabled: false
                generatePayLink: false
              disableApiKeyGeneration: false
          application/*+json:
            schema:
              allOf:
                - $ref: '#/components/schemas/GetLinkTokenRequest'
            example:
              userId: UserId
              configurationId: 18a20b11-e47f-43b9-8546-94284e9ee547
              restrictMultipleAccounts: true
              transferOptions:
                toAddresses:
                  - networkId: e3c7fdd8-b1fc-4e51-85ae-bb276e075611
                    symbol: ETH
                    address: '0x00000000000000000000000'
                  - networkId: e3c7fdd8-b1fc-4e51-85ae-bb276e075611
                    symbol: USDC
                    address: '0x00000000000000000000000'
                  - networkId: 7436e9d0-ba42-4d2b-b4c0-8e4e606b2c12
                    symbol: MATIC
                    address: '0x00000000000000000000000'
                  - networkId: 7436e9d0-ba42-4d2b-b4c0-8e4e606b2c12
                    symbol: USDC
                    address: '0x00000000000000000000000'
                amountInFiat: 10
                isInclusiveFeeEnabled: false
                generatePayLink: false
              disableApiKeyGeneration: false
      responses:
        '200':
          description: Link token created.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LinkTokenModelApiResult'
              example:
                content:
                  linkToken: >-
                    aHR0cHM6Ly93ZWIubWVzaGNvbm5lY3QuY29tL2IyYi1pZnJhbWUve2NsaWVudElkfS9icm9rZXItY29ubmVjdD9hdXRoX2NvZGU9e2F1dGhDb2RlfQ==
                status: ok
                message: ''
                errorHash: 8d443794
                errorType: ''
        '400':
          description: "BadRequest can happen in following cases:\r\n<list type=\"number\"><item><description>userId parameter not specified</description></item><item><description>Network not supported by the selected DeFi wallet.</description></item></list>"
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
        '404':
          description: API Client not found.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiResult'
              example:
                status: notFound
                message: Error message
                displayMessage: Optional display message
                errorHash: 7dcbb73d
                errorType: missingField
components:
  schemas:
    GetLinkTokenRequest:
      required:
        - userId
      type: object
      properties:
        userId:
          maxLength: 300
          minLength: 1
          type: string
          description: "A unique Id representing the end user. Typically this will be a user Id from the\r\nclient application. Personally identifiable information, such as an email address or phone number,\r\nshould not be used. 300 characters length maximum."
        brokerType:
          allOf:
            - $ref: '#/components/schemas/BrokerType'
          description: "Type of integration to redirect to. Will redirect to catalog if not provided.\r\nNot supported types: DeFiWallet, CryptocurrencyAddress, CryptocurrencyWallet."
          nullable: true
          deprecated: true
        restrictMultipleAccounts:
          type: boolean
          description: "The final screen of Link allows users to “continue” back to your app or “Link another account.”\r\nIf this param is present then this button will be hidden."
        transferOptions:
          allOf:
            - $ref: '#/components/schemas/LinkTokenTransferOptions'
          description: >-
            Encapsulates transaction-related parameters, including destination
            addresses and the amount to transfer in fiat currency.
          nullable: true
        integrationId:
          type: string
          description: >-
            A unique identifier representing a specific integration obtained
            from the list of available integrations.
          format: uuid
          nullable: true
        disableApiKeyGeneration:
          type: boolean
          description: "For direct integrations that also support API keys, Link presents the user with the option to generate an API key for seamless access.\r\nIf this param is true, this feature will be disabled."
        verifyWalletOptions:
          allOf:
            - $ref: '#/components/schemas/VerifyWalletOptions'
          description: Encapsulates verify DeFi wallet parameters.
          nullable: true
        subClientId:
          type: string
          description: >-
            Sub Client ID, for B2B2B clients to tailor Link experience for their
            clients.
          format: uuid
          nullable: true
      additionalProperties: false
    LinkTokenModelApiResult:
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
            - $ref: '#/components/schemas/LinkTokenModel'
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
    LinkTokenTransferOptions:
      type: object
      properties:
        toAddresses:
          type: array
          items:
            $ref: '#/components/schemas/TransferToAddressWithAmount'
          description: "The list of destination addresses with corresponding networks are asset symbols that\r\ncan be used to initiate incoming transfers. If this parameter is present, the Link\r\nsession will continue to transfer flow after connecting the origin account."
          nullable: true
        amountInFiat:
          type: number
          description: >-
            Amount in USD to transfer. If not provided users can specify amount
            by themselves.
          format: double
          nullable: true
        transactionId:
          maxLength: 128
          minLength: 0
          type: string
          description: >-
            Transaction ID Provided by client to track transaction in future
            calls
          nullable: true
        clientFee:
          maximum: 1
          minimum: 0
          type: number
          description: "A percentage fee (input as a ratio, eg. 0.02500 = 2.500%) added onto your users' gross payments to your company.\r\nThis will override any default fee entered in your Mesh dashboard for an individual transaction.\r\nPlease note: this fee should only be used for Payments (when the transfer destination is an address owned by your company),\r\nand not for Deposits (when the transfer destination is an address owned by the end user).\r\nIf used for Deposits, it will increase the size of the user's Deposit by the fee amount,\r\nbut will incorrectly show to the user as a fee."
          format: double
          nullable: true
        transferType:
          allOf:
            - $ref: '#/components/schemas/TransferTypeEnum'
          description: "Deposit: The user is transferring crypto to a wallet they own on your platform.\r\nPayment: The user is transferring crypto to a wallet your company owns in exchange for receiving a good or service.\r\nOnramp: The user is using balances and linked payment methods in an exchange account to fund the purchase of crypto in their wallet on your platform."
          nullable: true
        isInclusiveFeeEnabled:
          type: boolean
          description: Specifies if all the fees are included in the amount to transfer.
        description:
          maxLength: 256
          minLength: 0
          type: string
          description: Transaction description. (Binance Pay)
          nullable: true
        goodsDetails:
          type: array
          items:
            $ref: '#/components/schemas/GoodsDetails'
          description: Goods details for the transaction. (Binance Pay)
          nullable: true
        generatePayLink:
          type: boolean
          description: "Link presents the user with the option to generate a unique payment link for Mesh pay scenarios.\r\nIf this param is true, a unique payment link will be returned."
      additionalProperties: false
    VerifyWalletOptions:
      type: object
      properties:
        message:
          type: string
          description: "Verification message to sign.\r\nRequired if `signedMessage` is provided in <paramref name=\"VerificationMethods\">VerificationMethods</paramref> list."
          nullable: true
        verificationMethods:
          type: array
          items:
            $ref: '#/components/schemas/WalletVerificationMethod'
          description: >-
            List or required verification methods. By default - sign message
            with wallet key.
          nullable: true
        addresses:
          type: array
          items:
            type: string
          description: >-
            Addresses list to verify. If user verifies another address then
            verification will be failed.
          nullable: true
        networkId:
          type: string
          description: "Network to verify. If user verifies another network address then verification will be failed.\r\nChecked only if Addresses is provided."
          format: uuid
          nullable: true
        networkType:
          allOf:
            - $ref: '#/components/schemas/NetworkType'
          description: "Network type to verify. If user verifies another network address then verification will be failed.\r\nChecked only if Addresses is provided."
          nullable: true
      additionalProperties: false
      description: DeFi wallet verification options.
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
    LinkTokenModel:
      type: object
      properties:
        linkToken:
          type: string
          nullable: true
        paymentLink:
          type: string
          nullable: true
      additionalProperties: false
    TransferToAddressWithAmount:
      type: object
      properties:
        networkId:
          type: string
          description: "The Id of the network in Front system. The list of all available networks can be obtained by\r\nusing `GET /transfers/managed/networks` endpoint."
          format: uuid
        symbol:
          type: string
          description: The symbol of the digital asset.
          nullable: true
        address:
          type: string
          description: The address to send the asset to.
          nullable: true
        addressTag:
          type: string
          description: Secondary address identifier for coins like XRP,XMR etc.
          nullable: true
        amount:
          type: number
          description: Amount of tokens to transfer by specified network.
          format: double
          nullable: true
        displayAmountInFiat:
          type: number
          description: "Transfer amount in fiat which is requested by client to be shown as amount in fiat.\r\nIt will be shown to end-user if and only if it's difference with actual amount in fiat is less that 1%."
          format: double
          nullable: true
        minAmount:
          type: number
          description: >-
            Minimum allowed amount of tokens to transfer by specified
            token/network combination.
          format: double
          nullable: true
        minAmountInFiat:
          type: number
          description: >-
            Minimum allowed amount in fiat to transfer by specified
            token/network combination.
          format: double
          nullable: true
      additionalProperties: false
    TransferTypeEnum:
      enum:
        - deposit
        - payment
        - onramp
      type: string
    GoodsDetails:
      type: object
      properties:
        goodsType:
          type: string
          description: >-
            The type of the goods for the order (01: Tangible Goods, 02: Virtual
            Goods).
          nullable: true
        goodsCategory:
          type: string
          description: The category of goods (e.g., Electronics, Food).
          nullable: true
        referenceGoodsId:
          type: string
          description: A unique reference ID to identify the goods.
          nullable: true
        goodsName:
          type: string
          description: The name of the goods.
          nullable: true
        goodsDetail:
          type: string
          description: Additional details about the goods (optional).
          nullable: true
      additionalProperties: false
    WalletVerificationMethod:
      enum:
        - signedMessage
      type: string
      description: Verification method.
    NetworkType:
      enum:
        - unknown
        - evm
        - solana
        - bitcoin
        - cardano
        - tron
        - avalancheX
        - tezos
        - dogecoin
        - ripple
        - stellar
        - litecoin
        - sui
        - aptos
        - tvm
        - injective
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