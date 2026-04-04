# Source: https://docs.meshconnect.com/api-reference/managed-account-authentication/retrieve-the-list-of-all-available-integrations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.meshconnect.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve the list of all available integrations.

> Returns a list of integrations with details including the integration ID, name, type,
DeFi wallet provider ID, and categories.



## OpenAPI

````yaml get /api/v1/integrations
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
  /api/v1/integrations:
    get:
      tags:
        - Managed Account Authentication
      summary: Retrieve the list of all available integrations.
      description: "Returns a list of integrations with details including the integration ID, name, type,\r\nDeFi wallet provider ID, and categories."
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/IntegrationsResponseApiResult'
              example:
                content:
                  items:
                    - id: 47624467-e52e-4938-a41a-7926b6c27acf
                      name: Coinbase
                      type: coinbase
                      style:
                        fieldActiveLight: 0052FF
                        buttonPrimaryLight: 0052FF
                        buttonHoverLight: 014CEC
                        buttonTextLight: FFFFFF
                        buttonTextHoverLight: FFFFFF
                        fieldActiveDark: 578BFA
                        buttonPrimaryDark: 578BFA
                        buttonHoverDark: 507FE5
                        buttonTextDark: 0A0B0D
                        buttonTextHoverDark: 0A0B0D
                      logo:
                        logoLightUrl: >-
                          https://file-cdn.meshconnect.com/public/logos/Coinbase_Logo_Light.svg
                        logoDarkUrl: >-
                          https://file-cdn.meshconnect.com/public/logos/Coinbase_Logo_Dark.svg
                        logoWhiteUrl: >-
                          https://file-cdn.meshconnect.com/public/logos/Coinbase_Logo_White.svg
                        logoBlackUrl: >-
                          https://file-cdn.meshconnect.com/public/logos/Coinbase_Logo_Black.svg
                        logoColorUrl: >-
                          https://file-cdn.meshconnect.com/public/logos/Coinbase_Logo_Color.svg
                        iconLightUrl: >-
                          https://file-cdn.meshconnect.com/public/logos/Coinbase_Icon_Light.svg
                        iconDarkUrl: >-
                          https://file-cdn.meshconnect.com/public/logos/Coinbase_Icon_Dark.svg
                        iconWhiteUrl: >-
                          https://file-cdn.meshconnect.com/public/logos/Coinbase_Icon_White.svg
                        iconBlackUrl: >-
                          https://file-cdn.meshconnect.com/public/logos/Coinbase_Icon_Black.svg
                        iconColorUrl: >-
                          https://file-cdn.meshconnect.com/public/logos/Coinbase_Icon_Color.svg
                        base64Logo: >-
                          iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAMAAADXqc3KAAAA1VBMVEUAAAAAgP8AVf8AM/8AVdUAROgAQ+kAROkAROkAQ+oAQuoAROoAQ+gAROkAQ+kAQ+kAROkAQ+kAQ+kAROkAQugAQ+kAQ+kAROkAQ+kAQ+kAQ+kAQ+kAQ+kXVesOTuoAQ+kBROkERukFR+kNTeoOTeoUUusZVeshW+wpYe0qYu0uZe0yaO00ae05be5fifFgivGMqvWSr/amvfeqwPi7zfnE0/rO2/vU3/vY4vzc5fze5/zh6fzi6vzl7P3m7f3p7/3u8v7x9f73+f75+/76+//+/v////94Z10/AAAAH3RSTlMAAgMFBk9QUlNUVVZXiImKi4ykptfY2dvc3fHz9Pr8ZrpFhQAAAAFiS0dERhe6+e0AAADPSURBVBgZncHXVsJAFAXQExM6UhJCwEGPYsfesKCiAvf/P8m5swIhPLI3thbUo3gwiKNagJxyn6leCZmdNte0PCy1mdNAqswNRThBn+r0/n3+/XRAKwmg6lTnnyI/s2c6VaiI6kVerzg8phNCdWmNZHHBlRjK0LqVCTMGytC6kwkze1BdWteyGHElhopoHY7l7YZHJ3RCqBrV5VTk9288pKpABT2qs4eP2dfjPq3Eh1PihgJSLebsYslrck3DQ6aYMJUUkONXw44xnbDiY1v/vNIqVzlyMewAAAAASUVORK5CYII=
                      cryptoTransfersSupported: true
                    - id: 3d8f5c31-9fc0-4b61-bdfb-00fb18cbb9ad
                      name: CoinCircle
                      type: deFiWallet
                      deFiWalletProviderId: 36d8d9c0c7fe2957149ce8e878f3a01...
                      categories:
                        - deFiWallet
                      style:
                        fieldActiveLight: 0052FF
                        buttonPrimaryLight: 0052FF
                        buttonHoverLight: 014CEC
                        buttonTextLight: FFFFFF
                        buttonTextHoverLight: FFFFFF
                        fieldActiveDark: 578BFA
                        buttonPrimaryDark: 578BFA
                        buttonHoverDark: 507FE5
                        buttonTextDark: 0A0B0D
                        buttonTextHoverDark: 0A0B0D
                      logo:
                        logoColorUrl: >-
                          https://file-cdn.meshconnect.com/public/logos/CoinCircle_Logo_Color.svg
                        iconColorUrl: >-
                          https://file-cdn.meshconnect.com/public/logos/CoinCircle_Icon_Color.svg
                      cryptoTransfersSupported: true
                status: ok
                message: ''
                errorHash: d48f676e
                errorType: ''
components:
  schemas:
    IntegrationsResponseApiResult:
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
            - $ref: '#/components/schemas/IntegrationsResponse'
          description: Integration response.
          nullable: true
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
    IntegrationsResponse:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/IntegrationModel'
          description: Integrations list.
          nullable: true
      additionalProperties: false
      description: Integration response.
    IntegrationModel:
      type: object
      properties:
        id:
          type: string
          description: Integration unique identifier.
          format: uuid
        name:
          type: string
          description: Integration name.
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
          description: Integration type.
        deFiWalletProviderId:
          type: string
          description: DeFi wallet provider identifier.
          nullable: true
        categories:
          type: array
          items:
            $ref: '#/components/schemas/FinancialInstitutionIntegrationType'
          description: Integration categories.
          nullable: true
        style:
          allOf:
            - $ref: '#/components/schemas/IntegrationStyle'
          description: Style object.
          nullable: true
        logo:
          allOf:
            - $ref: '#/components/schemas/IntegrationLogo'
          description: Logo object.
          nullable: true
        forgotPasswordLink:
          type: string
          description: Forgot Password Link.
          nullable: true
        cryptoTransfersSupported:
          type: boolean
          description: Indicates if crypto transfers supported by integration.
      additionalProperties: false
      description: Integration model.
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
    FinancialInstitutionIntegrationType:
      enum:
        - brokerage
        - bank
        - exchange
        - wallet
        - address
        - nftMarketplace
        - deFiWallet
      type: string
    IntegrationStyle:
      type: object
      properties:
        fieldActiveLight:
          type: string
          description: Field Active Light Hex Color
          nullable: true
        buttonPrimaryLight:
          type: string
          description: Button Primary Light Hex Color
          nullable: true
        buttonHoverLight:
          type: string
          description: Button Hover Light Hex Color
          nullable: true
        buttonTextLight:
          type: string
          description: Button Text Light Hex Color
          nullable: true
        buttonTextHoverLight:
          type: string
          description: Button Text Hover Light Hex Color
          nullable: true
        fieldActiveDark:
          type: string
          description: Field Active Dark Hex Color
          nullable: true
        buttonPrimaryDark:
          type: string
          description: Button Primary Dark Hex Color
          nullable: true
        buttonHoverDark:
          type: string
          description: Button Hover Dark Hex Color
          nullable: true
        buttonTextDark:
          type: string
          description: Button Text Dark Hex Color
          nullable: true
        buttonTextHoverDark:
          type: string
          description: Button Text Hover Dark Hex Color
          nullable: true
      additionalProperties: false
      description: Integration style
    IntegrationLogo:
      type: object
      properties:
        logoLightUrl:
          type: string
          description: Light logo url.
          nullable: true
        logoDarkUrl:
          type: string
          description: Dark logo url.
          nullable: true
        logoWhiteUrl:
          type: string
          description: White logo url.
          nullable: true
        logoBlackUrl:
          type: string
          description: Black logo url.
          nullable: true
        logoColorUrl:
          type: string
          description: Colored logo url.
          nullable: true
        iconLightUrl:
          type: string
          description: White icon url.
          nullable: true
        iconDarkUrl:
          type: string
          description: Light icon url.
          nullable: true
        iconWhiteUrl:
          type: string
          description: Dark icon url.
          nullable: true
        iconBlackUrl:
          type: string
          description: Balck icon url.
          nullable: true
        iconColorUrl:
          type: string
          description: Colored logo url.
          nullable: true
        base64Logo:
          type: string
          description: Base64 PNG logo.
          nullable: true
      additionalProperties: false
      description: Integreation logos.
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