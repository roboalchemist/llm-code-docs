# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/submit-prepayment-balances.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Submit Prepayment Balances

> Sends the prepayment balances. The partner should do this at least once a day and ideally once per hour. <br/> Use the `credentials.access_token` we provided in the [Upsert Installation](#upsert-installation) body to authorize this request.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/billing/balance
openapi: 3.0.3
info:
  title: Vercel REST API & SDK
  description: >-
    The [`@vercel/sdk`](https://www.npmjs.com/package/@vercel/sdk) is a
    type-safe Typescript SDK that allows you to access the resources and methods
    of the Vercel REST API. Learn how to [install
    it](https://vercel.com/docs/rest-api/sdk#installing-vercel-sdk) and
    [authenticate](https://vercel.com/docs/rest-api/sdk#authentication) with a
    Vercel access token.
  contact:
    email: support@vercel.com
    name: Vercel Support
    url: https://vercel.com/support
  version: 0.0.1
servers:
  - url: https://api.vercel.com
    description: Production API
security: []
paths:
  /v1/installations/{integrationConfigurationId}/billing/balance:
    post:
      tags:
        - marketplace
      summary: Submit Prepayment Balances
      description: >-
        Sends the prepayment balances. The partner should do this at least once
        a day and ideally once per hour. <br/> Use the
        `credentials.access_token` we provided in the [Upsert
        Installation](#upsert-installation) body to authorize this request.
      operationId: submit-prepayment-balances
      parameters:
        - name: integrationConfigurationId
          in: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                timestamp:
                  description: >-
                    Server time of your integration, used to determine the most
                    recent data for race conditions & updates. Only the latest
                    usage data for a given day, week, and month will be kept.
                  type: string
                  format: date-time
                balances:
                  type: array
                  items:
                    type: object
                    description: A credit balance for a particular token type
                    properties:
                      resourceId:
                        type: string
                        description: >-
                          Partner's resource ID, exclude if credits are tied to
                          the installation and not an individual resource.
                      credit:
                        type: string
                        description: >-
                          A human-readable description of the credits the user
                          currently has, e.g. \"2,000 Tokens\"
                      nameLabel:
                        type: string
                        description: >-
                          The name of the credits, for display purposes, e.g.
                          \"Tokens\"
                      currencyValueInCents:
                        type: number
                        description: >-
                          The dollar value of the credit balance, in USD and
                          provided in cents, which is used to trigger automatic
                          purchase thresholds.
                    required:
                      - currencyValueInCents
                    additionalProperties: false
              required:
                - timestamp
                - balances
              additionalProperties: false
      responses:
        '201':
          description: ''
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````