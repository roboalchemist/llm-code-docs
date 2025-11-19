# Source: https://docs.meshconnect.com/api-reference/managed-account-authentication/refresh-auth-token.md

# Refresh auth token

> Refresh auth token of the connected institution.
Some institutions do not require tokens to be refreshed.
            
The following institutions require custom flows:
            
WeBull: AuthToken should be provided along with the RefreshToken
            
Vanguard: security settings may activate MFA, requiring user action.
If MFA is triggered, a second refresh request should be sent.
Second request should contain MFA code and access token obtained from initial response

## OpenAPI

````yaml post /api/v1/token/refresh
paths:
  path: /api/v1/token/refresh
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
              refreshToken:
                allOf:
                  - minLength: 1
                    type: string
              createNewRefreshToken:
                allOf:
                  - type: boolean
                    description: "Optional, used when we the refresh token should be refreshed.\r\nCurrently this flow is supported by TD Ameritrade"
                    nullable: true
              accessToken:
                allOf:
                  - type: string
                    description: "Some institutions may require accessToken to be provided as well.\r\nIt's currently required by WeBull and Vanguard"
                    nullable: true
              tradeToken:
                allOf:
                  - type: string
                    description: Currently used to update WeBull trade token.
                    nullable: true
              mfaCode:
                allOf:
                  - type: string
                    description: >-
                      Optional, currently used by Vanguard if account has
                      enforced MFA enabled.
                    nullable: true
              metadata:
                allOf:
                  - type: object
                    additionalProperties:
                      type: string
                      nullable: true
                    description: Additional metadata
                    nullable: true
            refIdentifier: '#/components/schemas/BrokerRefreshTokenRequest'
            requiredProperties:
              - refreshToken
              - type
            additionalProperties: false
        examples:
          example:
            value:
              refreshToken: Secret refresh token
              type: coinbase
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
                      - $ref: '#/components/schemas/B2BBrokerRefreshTokenResponse'
                    nullable: true
            refIdentifier: '#/components/schemas/B2BBrokerRefreshTokenResponseApiResult'
            additionalProperties: false
        examples:
          example:
            value:
              content:
                status: succeeded
                expiresInSeconds: 86400
                brokerAccountTokens:
                  - accessToken: New secret token
                    refreshToken: New secret refresh token
              status: ok
              message: ''
              errorHash: 9d3039e8
              errorType: ''
        description: OK
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
              message: Unauthorized token
              displayMessage: >-
                Could not refresh the authentication token. The provided data is
                not correct
              errorHash: 1bc4f94f
              errorType: badRequest
        description: Bad Request
    '401':
      application/json:
        schemaArray:
          - type: any
        examples:
          example:
            value: <any>
        description: Unauthorized
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
    B2BBrokerAuthStatus:
      enum:
        - failed
        - succeeded
        - mfaRequired
      type: string
    B2BBrokerRefreshTokenResponse:
      type: object
      properties:
        status:
          enum:
            - failed
            - succeeded
            - mfaRequired
          allOf:
            - $ref: '#/components/schemas/B2BBrokerAuthStatus'
        errorMessage:
          type: string
          nullable: true
        account:
          allOf:
            - $ref: '#/components/schemas/BrokerAccount'
          nullable: true
          deprecated: true
        accessToken:
          type: string
          nullable: true
          deprecated: true
        refreshToken:
          type: string
          nullable: true
          deprecated: true
        expiresInSeconds:
          type: integer
          format: int32
          nullable: true
        refreshTokenExpiresInSeconds:
          type: integer
          format: int32
          nullable: true
        brokerAccountTokens:
          type: array
          items:
            $ref: '#/components/schemas/BrokerAccountTokens'
          nullable: true
      additionalProperties: false
    BrokerAccount:
      type: object
      properties:
        meshAccountId:
          type: string
          format: uuid
        frontAccountId:
          type: string
          format: uuid
          readOnly: true
          deprecated: true
        accountId:
          type: string
          nullable: true
        accountName:
          type: string
          nullable: true
        fund:
          type: number
          description: "Buying power of the account. Typically consists of cash plus available margin.\r\nFor non-margin accounts fund contains cash only"
          format: double
          nullable: true
        cash:
          type: number
          description: Cash balance in USD
          format: double
          nullable: true
        isReconnected:
          type: boolean
          description: "Indicates if this account was already connected by the current user and device.\r\nCan be null."
          nullable: true
        balances:
          type: array
          items:
            $ref: '#/components/schemas/BrokerFiatBalance'
          description: The list of all asset balances of account
          nullable: true
      additionalProperties: false
    BrokerAccountTokens:
      type: object
      properties:
        account:
          allOf:
            - $ref: '#/components/schemas/BrokerAccount'
          nullable: true
        accessToken:
          type: string
          nullable: true
        refreshToken:
          type: string
          nullable: true
        tokenId:
          type: string
          description: >-
            Token identifier provided by Mesh when the actual integration's
            token is managed by Mesh's Token Management System.
          nullable: true
      additionalProperties: false
    BrokerFiatBalance:
      type: object
      properties:
        symbol:
          type: string
          description: Account balance currency
          nullable: true
        buyingPower:
          type: number
          description: "BuyingPower indicates total amount of money the user can spend for buying stock. Always includes cash and\r\ncan also include margin"
          format: double
          nullable: true
        cryptoBuyingPower:
          type: number
          description: >-
            BuyingPower indicates total amount of money the user can spend for
            buying crypto.
          format: double
          nullable: true
        cash:
          type: number
          description: Account cash indicates total amount of money
          format: double
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
      type: string

````