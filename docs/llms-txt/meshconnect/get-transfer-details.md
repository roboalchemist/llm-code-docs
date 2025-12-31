# Source: https://docs.meshconnect.com/api-reference/transfers/get-transfer-details.md

# Get transfer details

> Get details of a specific transfer (withdrawals or deposits) executed from an exchange.
Only supports Exchange integrations.

## OpenAPI

````yaml post /api/v1/transfers/details
paths:
  path: /api/v1/transfers/details
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
                      ```DeFiWallet```
              addressType:
                allOf:
                  - allOf:
                      - $ref: '#/components/schemas/CryptocurrencyAddressType'
                    description: >-
                      Type of the address of the transferred asset. Can be used
                      instead of the `Symbol` field.
                    nullable: true
              transactionId:
                allOf:
                  - type: string
                    description: Transaction Id by the financial institution
                    nullable: true
              transactionHash:
                allOf:
                  - type: string
                    description: Hash of the transaction on the blockchain
                    nullable: true
              symbol:
                allOf:
                  - type: string
                    description: >-
                      Symbol of the transferred asset. Can be provided instead
                      of the `AddressType` field.
                    nullable: true
            refIdentifier: >-
              #/components/schemas/TransfersBrokerCryptocurrencyTransactionDetailsRequest
            requiredProperties:
              - authToken
              - type
            additionalProperties: false
        examples:
          example:
            value:
              transactionId: 63F1A6B6-BF45-4E51-A624-EC52B5680D48
              authToken: Secret authentication token
              type: robinhood
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
                          #/components/schemas/B2BBrokerCryptocurrencyTransaction
                    nullable: true
            refIdentifier: '#/components/schemas/B2BBrokerCryptocurrencyTransactionApiResult'
            additionalProperties: false
        examples:
          example:
            value:
              content:
                id: 8E25ACB5-A9E2-4D00-8772-A255F010A2A9
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
              status: ok
              message: ''
              errorHash: 803a2abd
              errorType: ''
        description: Transfer details obtained.
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
        description: Transfer details are not correct.
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
        description: Transfer with provided id was not found.
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
    BrokerCryptocurrencyTransactionType:
      enum:
        - unknown
        - deposit
        - withdrawal
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