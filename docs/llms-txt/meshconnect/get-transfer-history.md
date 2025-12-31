# Source: https://docs.meshconnect.com/api-reference/transfers/get-transfer-history.md

# Get transfer history

> Get entire history of cryptocurrency transfers (withdrawals or deposits) executed from an exchange.
Only supports Exchange integrations.

## OpenAPI

````yaml post /api/v1/transfers/list
paths:
  path: /api/v1/transfers/list
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
              count:
                allOf:
                  - type: integer
                    description: "Number of records to include in the response. \n\r\nDefault: `100` \n\r\nMaximum: `250`"
                    format: int32
              cursor:
                allOf:
                  - type: string
                    description: "The cursor to retrieve the next page of transactions.\r\nProviding it will cause the response to only return changes after this update.\r\nIf this field is not provided, the history of transactions will be returned starting with the first-added transaction."
                    nullable: true
              statuses:
                allOf:
                  - type: array
                    items:
                      $ref: >-
                        #/components/schemas/BrokerCryptocurrencyTransactionStatus
                    description: >-
                      If this value is provided, result set is filtered to only
                      include transaction with the provided statuses.
                    nullable: true
              cryptocurrencyAddressType:
                allOf:
                  - allOf:
                      - $ref: '#/components/schemas/CryptocurrencyAddressType'
                    description: >-
                      For cryptocurrency address the type of address is
                      required.
                    nullable: true
              from:
                allOf:
                  - type: integer
                    description: >-
                      If this value is provided, result set is filtered to only
                      include transactions created after this timestamp
                    format: int64
                    nullable: true
            refIdentifier: '#/components/schemas/TransfersBrokerTransactionsListRequest'
            requiredProperties:
              - authToken
              - type
            additionalProperties: false
        examples:
          example:
            value:
              authToken: <string>
              type: robinhood
              count: 123
              cursor: <string>
              statuses:
                - unknown
              cryptocurrencyAddressType: ethAddress
              from: 123
        description: >-
          Authentication token and integration type to obtain the list of
          transfers.
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
                      - $ref: '#/components/schemas/B2BBrokerTransactionsListModel'
                    nullable: true
            refIdentifier: '#/components/schemas/B2BBrokerTransactionsListModelApiResult'
            additionalProperties: false
        examples:
          example:
            value:
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
        description: Transfers obtained.
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