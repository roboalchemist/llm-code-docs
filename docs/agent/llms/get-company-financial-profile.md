# Source: https://docs.agent.ai/api-reference/get-data/get-company-financial-profile.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Company Financial Profile

> Retrieve detailed financial and company profile information for a given stock symbol, such as market cap and the last known stock price for any company.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/company_financial_profile
openapi: 3.0.0
info:
  version: 1.0.0
  title: AI Actions - Get Data
  description: API specifications for 'Get Data' category AI actions.
  license:
    name: MIT
servers:
  - url: https://api-lr.agent.ai/v1
security:
  - bearerAuth: []
paths:
  /action/company_financial_profile:
    post:
      tags:
        - Get Data
      summary: Get Company Financial Profile
      description: >-
        Retrieve detailed financial and company profile information for a given
        stock symbol, such as market cap and the last known stock price for any
        company.
      operationId: companyFinancialProfile
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                company:
                  type: string
                  description: Stock symbol of the company.
                  example: HUBS, NKE, AAPL
              required:
                - company
      responses:
        '200':
          description: Successful retrieval of company financial profile
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    symbol:
                      type: string
                      description: Company stock symbol
                    price:
                      type: number
                      description: Current stock price
                    beta:
                      type: number
                      description: Beta value indicating stock volatility
                    volAvg:
                      type: integer
                      description: Average trading volume
                    mktCap:
                      type: number
                      description: Market capitalization
                    lastDiv:
                      type: number
                      description: Last dividend payment
                    range:
                      type: string
                      description: 52-week price range
                    changes:
                      type: number
                      description: Price change
                    companyName:
                      type: string
                      description: Full company name
                    currency:
                      type: string
                      description: Trading currency
                    cik:
                      type: string
                      description: SEC Central Index Key
                    isin:
                      type: string
                      description: International Securities Identification Number
                    cusip:
                      type: string
                      description: CUSIP identifier
                    exchange:
                      type: string
                      description: Stock exchange name
                    exchangeShortName:
                      type: string
                      description: Stock exchange abbreviation
                    industry:
                      type: string
                      description: Company industry
                    website:
                      type: string
                      description: Company website URL
                    description:
                      type: string
                      description: Company description
                    ceo:
                      type: string
                      description: Company CEO name
                    sector:
                      type: string
                      description: Company sector
                    country:
                      type: string
                      description: Country of incorporation
                    fullTimeEmployees:
                      type: string
                      description: Number of full-time employees
                    phone:
                      type: string
                      description: Company phone number
                    address:
                      type: string
                      description: Company street address
                    city:
                      type: string
                      description: Company city
                    state:
                      type: string
                      description: Company state
                    zip:
                      type: string
                      description: Company ZIP code
                    dcfDiff:
                      type: number
                      description: Discounted Cash Flow difference
                    dcf:
                      type: number
                      description: Discounted Cash Flow value
                    image:
                      type: string
                      description: Company logo URL
                    ipoDate:
                      type: string
                      description: Initial Public Offering date
                    defaultImage:
                      type: boolean
                      description: Indicates if using default image
                    isEtf:
                      type: boolean
                      description: Indicates if security is an ETF
                    isActivelyTrading:
                      type: boolean
                      description: Indicates if security is actively trading
                    isAdr:
                      type: boolean
                      description: Indicates if security is an ADR
                    isFund:
                      type: boolean
                      description: Indicates if security is a fund
              example:
                status: 200
                response:
                  - symbol: HUBS
                    price: 726.43
                    beta: 1.715
                    volAvg: 473128
                    mktCap: 37885576433
                    lastDiv: 0
                    range: 434.84-881.13
                    changes: -21.57
                    companyName: HubSpot, Inc.
                    currency: USD
                    cik: '0001404655'
                    isin: US4435731009
                    cusip: '443573100'
                    exchange: New York Stock Exchange
                    exchangeShortName: NYSE
                    industry: Software - Application
                    website: https://www.hubspot.com
                    description: >-
                      HubSpot, Inc. provides a cloud-based customer relationship
                      management (CRM) platform for businesses in the Americas,
                      Europe, and the Asia Pacific...
                    ceo: Ms. Yamini Rangan
                    sector: Technology
                    country: US
                    fullTimeEmployees: '8246'
                    phone: 888 482 7768
                    address: 25 First Street
                    city: Cambridge
                    state: MA
                    zip: '02141'
                    dcfDiff: 543.32777
                    dcf: 183.1022333290244
                    image: https://images.financialmodelingprep.com/symbol/HUBS.png
                    ipoDate: '2014-10-09'
                    defaultImage: false
                    isEtf: false
                    isActivelyTrading: true
                    isAdr: false
                    isFund: false
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer token from your account
        ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))

````