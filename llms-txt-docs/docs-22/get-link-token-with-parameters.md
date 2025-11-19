# Source: https://docs.meshconnect.com/api-reference/managed-account-authentication/get-link-token-with-parameters.md

# Get Link token with parameters

> Get a short lived, one-time use token for initializing a Link session using the client-side SDKs

## OpenAPI

````yaml post /api/v1/linktoken
paths:
  path: /api/v1/linktoken
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
              userId:
                allOf:
                  - &ref_0
                    maxLength: 300
                    minLength: 1
                    type: string
                    description: "A unique Id representing the end user. Typically this will be a user Id from the\r\nclient application. Personally identifiable information, such as an email address or phone number,\r\nshould not be used. 300 characters length maximum."
              brokerType:
                allOf:
                  - &ref_1
                    allOf:
                      - $ref: '#/components/schemas/BrokerType'
                    description: "Type of integration to redirect to. Will redirect to catalog if not provided.\r\nNot supported types: DeFiWallet, CryptocurrencyAddress, CryptocurrencyWallet."
                    nullable: true
                    deprecated: true
              restrictMultipleAccounts:
                allOf:
                  - &ref_2
                    type: boolean
                    description: "The final screen of Link allows users to “continue” back to your app or “Link another account.”\r\nIf this param is present then this button will be hidden."
              transferOptions:
                allOf:
                  - &ref_3
                    allOf:
                      - $ref: '#/components/schemas/LinkTokenTransferOptions'
                    description: >-
                      Encapsulates transaction-related parameters, including
                      destination addresses and the amount to transfer in fiat
                      currency.
                    nullable: true
              integrationId:
                allOf:
                  - &ref_4
                    type: string
                    description: >-
                      A unique identifier representing a specific integration
                      obtained from the list of available integrations.
                    format: uuid
                    nullable: true
              disableApiKeyGeneration:
                allOf:
                  - &ref_5
                    type: boolean
                    description: "For direct integrations that also support API keys, Link presents the user with the option to generate an API key for seamless access.\r\nIf this param is true, this feature will be disabled."
              verifyWalletOptions:
                allOf:
                  - &ref_6
                    allOf:
                      - $ref: '#/components/schemas/VerifyWalletOptions'
                    description: Encapsulates verify DeFi wallet parameters.
                    nullable: true
              subClientId:
                allOf:
                  - &ref_7
                    type: string
                    description: >-
                      Sub Client ID, for B2B2B clients to tailor Link experience
                      for their clients.
                    format: uuid
                    nullable: true
            refIdentifier: '#/components/schemas/GetLinkTokenRequest'
            requiredProperties: &ref_8
              - userId
            additionalProperties: false
        examples:
          example:
            value:
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
        description: Create Link token request.
      text/json:
        schemaArray:
          - type: object
            properties:
              userId:
                allOf:
                  - *ref_0
              brokerType:
                allOf:
                  - *ref_1
              restrictMultipleAccounts:
                allOf:
                  - *ref_2
              transferOptions:
                allOf:
                  - *ref_3
              integrationId:
                allOf:
                  - *ref_4
              disableApiKeyGeneration:
                allOf:
                  - *ref_5
              verifyWalletOptions:
                allOf:
                  - *ref_6
              subClientId:
                allOf:
                  - *ref_7
            refIdentifier: '#/components/schemas/GetLinkTokenRequest'
            requiredProperties: *ref_8
            additionalProperties: false
        examples:
          example:
            value:
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
        description: Create Link token request.
      application/*+json:
        schemaArray:
          - type: object
            properties:
              userId:
                allOf:
                  - *ref_0
              brokerType:
                allOf:
                  - *ref_1
              restrictMultipleAccounts:
                allOf:
                  - *ref_2
              transferOptions:
                allOf:
                  - *ref_3
              integrationId:
                allOf:
                  - *ref_4
              disableApiKeyGeneration:
                allOf:
                  - *ref_5
              verifyWalletOptions:
                allOf:
                  - *ref_6
              subClientId:
                allOf:
                  - *ref_7
            refIdentifier: '#/components/schemas/GetLinkTokenRequest'
            requiredProperties: *ref_8
            additionalProperties: false
        examples:
          example:
            value:
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
        description: Create Link token request.
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
                      - $ref: '#/components/schemas/LinkTokenModel'
                    nullable: true
            refIdentifier: '#/components/schemas/LinkTokenModelApiResult'
            additionalProperties: false
        examples:
          example:
            value:
              content:
                linkToken: >-
                  aHR0cHM6Ly93ZWIubWVzaGNvbm5lY3QuY29tL2IyYi1pZnJhbWUve2NsaWVudElkfS9icm9rZXItY29ubmVjdD9hdXRoX2NvZGU9e2F1dGhDb2RlfQ==
              status: ok
              message: ''
              errorHash: 8d443794
              errorType: ''
        description: Link token created.
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - &ref_9
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
                  - &ref_10
                    type: string
                    description: A message generated by the API
                    nullable: true
              displayMessage:
                allOf:
                  - &ref_11
                    type: string
                    description: >-
                      User-friendly display message that can be presented to the
                      end user
                    nullable: true
              errorHash:
                allOf:
                  - &ref_12
                    type: string
                    description: >-
                      An error grouping hash from string components and caller
                      information. Used by bugsnag on FE for correct error
                      grouping
                    nullable: true
                    readOnly: true
              errorType:
                allOf:
                  - &ref_13
                    type: string
                    description: "Strictly-typed error type that is explaining the reason of an unsuccessful status of the operation.\r\nAll possible error types are available in the documentation."
                    nullable: true
              errorData:
                allOf:
                  - &ref_14
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
        description: "BadRequest can happen in following cases:\r\n<list type=\"number\"><item><description>userId parameter not specified</description></item><item><description>Network not supported by the selected DeFi wallet.</description></item></list>"
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
                  - *ref_9
              message:
                allOf:
                  - *ref_10
              displayMessage:
                allOf:
                  - *ref_11
              errorHash:
                allOf:
                  - *ref_12
              errorType:
                allOf:
                  - *ref_13
              errorData:
                allOf:
                  - *ref_14
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
        description: API Client not found.
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
    WalletVerificationMethod:
      enum:
        - signedMessage
      type: string
      description: Verification method.

````