# Source: https://dub.co/docs/api-reference/endpoint/retrieve-a-list-of-commissions.md

# List all commissions

> Retrieve a list of commissions for a program.

## OpenAPI

````yaml get /commissions
paths:
  path: /commissions
  method: get
  servers:
    - url: https://api.dub.co
      description: Production API
  request:
    security:
      - title: token
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path: {}
      query:
        type:
          schema:
            - type: enum<string>
              enum:
                - click
                - lead
                - sale
                - custom
        customerId:
          schema:
            - type: string
              description: Filter the list of commissions by the associated customer.
        payoutId:
          schema:
            - type: string
              description: Filter the list of commissions by the associated payout.
        partnerId:
          schema:
            - type: string
              description: >-
                Filter the list of commissions by the associated partner. When
                specified, takes precedence over `tenantId`.
        tenantId:
          schema:
            - type: string
              description: >-
                Filter the list of commissions by the associated partner's
                `tenantId` (their unique ID within your database).
        groupId:
          schema:
            - type: string
              description: Filter the list of commissions by the associated partner group.
        invoiceId:
          schema:
            - type: string
              description: >-
                Filter the list of commissions by the associated invoice. Since
                invoiceId is unique on a per-program basis, this will only
                return one commission per invoice.
        status:
          schema:
            - type: enum<string>
              enum:
                - pending
                - processed
                - paid
                - refunded
                - duplicate
                - fraud
                - canceled
              description: Filter the list of commissions by their corresponding status.
        sortBy:
          schema:
            - type: enum<string>
              enum:
                - createdAt
                - amount
              description: The field to sort the list of commissions by.
              default: createdAt
        sortOrder:
          schema:
            - type: enum<string>
              enum:
                - asc
                - desc
              description: The sort order for the list of commissions.
              default: desc
        interval:
          schema:
            - type: enum<string>
              enum:
                - 24h
                - 7d
                - 30d
                - 90d
                - 1y
                - mtd
                - qtd
                - ytd
                - all
              description: The interval to retrieve commissions for.
              default: all
        start:
          schema:
            - type: string
              description: The start date of the date range to filter the commissions by.
        end:
          schema:
            - type: string
              description: The end date of the date range to filter the commissions by.
        page:
          schema:
            - type: number
              description: The page number for pagination.
              minimum: 0
              exclusiveMinimum: true
              default: 1
              example: 1
        pageSize:
          schema:
            - type: number
              description: The number of items per page.
              maximum: 100
              minimum: 0
              exclusiveMinimum: true
              default: 100
              example: 50
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: listCommissions
        lang: python
        source: |-
          from dub import Dub


          with Dub(
              token="DUB_API_KEY",
          ) as d_client:

              res = d_client.commissions.list(request={
                  "page_size": 50,
              })

              assert res is not None

              # Handle response
              print(res)
      - label: listCommissions
        lang: php
        source: |-
          declare(strict_types=1);

          require 'vendor/autoload.php';

          use Dub;
          use Dub\Models\Operations;

          $sdk = Dub\Dub::builder()
              ->setSecurity(
                  'DUB_API_KEY'
              )
              ->build();

          $request = new Operations\ListCommissionsRequest(
              pageSize: 50,
          );

          $response = $sdk->commissions->list(
              request: $request
          );

          if ($response->responseBodies !== null) {
              // handle response
          }
      - label: listCommissions
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\tdubgo \"github.com/dubinc/dub-go\"\n\t\"github.com/dubinc/dub-go/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := dubgo.New(\n        dubgo.WithSecurity(\"DUB_API_KEY\"),\n    )\n\n    res, err := s.Commissions.List(ctx, operations.ListCommissionsRequest{\n        PageSize: dubgo.Pointer[float64](50),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: listCommissions
        lang: ruby
        source: |-
          require 'dub'

          Models = ::OpenApiSDK::Models
          s = ::OpenApiSDK::Dub.new(
                security: Models::Shared::Security.new(
                  token: 'DUB_API_KEY',
                ),
              )

          req = Models::Operations::ListCommissionsRequest.new(
            page_size: 50.0,
          )

          res = s.commissions.list(request: req)

          unless res.nil?
            # handle response
          end
      - label: listCommissions
        lang: typescript
        source: |-
          import { Dub } from "dub";

          const dub = new Dub({
            token: "DUB_API_KEY",
          });

          async function run() {
            const result = await dub.commissions.list();

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - type: object
                  properties:
                    id:
                      type: string
                      description: The commission's unique ID on Dub.
                      example: cm_1JVR7XRCSR0EDBAF39FZ4PMYE
                    type:
                      type: string
                      enum:
                        - click
                        - lead
                        - sale
                        - custom
                    amount:
                      type: number
                    earnings:
                      type: number
                    currency:
                      type: string
                    status:
                      type: string
                      enum:
                        - pending
                        - processed
                        - paid
                        - refunded
                        - duplicate
                        - fraud
                        - canceled
                    invoiceId:
                      type: string
                      nullable: true
                    description:
                      type: string
                      nullable: true
                    quantity:
                      type: number
                    userId:
                      type: string
                      nullable: true
                      description: The user who created the manual commission.
                    createdAt:
                      type: string
                    updatedAt:
                      type: string
                    partner:
                      type: object
                      properties:
                        id:
                          type: string
                          description: The partner's unique ID on Dub.
                        name:
                          type: string
                          maxLength: 190
                          description: The partner's full legal name.
                        email:
                          type: string
                          nullable: true
                          maxLength: 190
                          description: >-
                            The partner's email address. Should be a unique
                            value across Dub.
                        image:
                          type: string
                          nullable: true
                          description: The partner's avatar image.
                        payoutsEnabledAt:
                          type: string
                          nullable: true
                          description: The date when the partner enabled payouts.
                        country:
                          type: string
                          nullable: true
                          description: The partner's country (required for tax purposes).
                      required:
                        - id
                        - name
                        - email
                        - image
                        - payoutsEnabledAt
                        - country
                    customer:
                      type: object
                      nullable: true
                      properties:
                        id:
                          type: string
                          description: >-
                            The unique ID of the customer. You may use either
                            the customer's `id` on Dub (obtained via
                            `/customers` endpoint) or their `externalId` (unique
                            ID within your system, prefixed with `ext_`, e.g.
                            `ext_123`).
                        externalId:
                          type: string
                          description: >-
                            Unique identifier for the customer in the client's
                            app.
                        name:
                          type: string
                          description: Name of the customer.
                        email:
                          type: string
                          nullable: true
                          description: Email of the customer.
                        avatar:
                          type: string
                          nullable: true
                          description: Avatar URL of the customer.
                        country:
                          type: string
                          nullable: true
                          description: Country of the customer.
                        sales:
                          type: number
                          nullable: true
                          description: Total number of sales for the customer.
                        saleAmount:
                          type: number
                          nullable: true
                          description: Total amount of sales for the customer.
                        createdAt:
                          type: string
                          description: The date the customer was created.
                      required:
                        - id
                        - externalId
                        - name
                        - createdAt
                  required:
                    - id
                    - amount
                    - earnings
                    - currency
                    - status
                    - invoiceId
                    - description
                    - quantity
                    - createdAt
                    - updatedAt
                    - partner
        examples:
          example:
            value:
              - id: cm_1JVR7XRCSR0EDBAF39FZ4PMYE
                type: click
                amount: 123
                earnings: 123
                currency: <string>
                status: pending
                invoiceId: <string>
                description: <string>
                quantity: 123
                userId: <string>
                createdAt: <string>
                updatedAt: <string>
                partner:
                  id: <string>
                  name: <string>
                  email: <string>
                  image: <string>
                  payoutsEnabledAt: <string>
                  country: <string>
                customer:
                  id: <string>
                  externalId: <string>
                  name: <string>
                  email: <string>
                  avatar: <string>
                  country: <string>
                  sales: 123
                  saleAmount: 123
                  createdAt: <string>
        description: The list of commissions.
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - bad_request
                        description: A short code indicating the error code returned.
                        example: bad_request
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: https://dub.co/docs/api-reference/errors#bad-request
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: bad_request
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#bad-request
        description: >-
          The server cannot or will not process the request due to something
          that is perceived to be a client error (e.g., malformed request
          syntax, invalid request message framing, or deceptive request
          routing).
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - unauthorized
                        description: A short code indicating the error code returned.
                        example: unauthorized
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: https://dub.co/docs/api-reference/errors#unauthorized
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: unauthorized
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#unauthorized
        description: >-
          Although the HTTP standard specifies "unauthorized", semantically this
          response means "unauthenticated". That is, the client must
          authenticate itself to get the requested response.
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - forbidden
                        description: A short code indicating the error code returned.
                        example: forbidden
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: https://dub.co/docs/api-reference/errors#forbidden
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: forbidden
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#forbidden
        description: >-
          The client does not have access rights to the content; that is, it is
          unauthorized, so the server is refusing to give the requested
          resource. Unlike 401 Unauthorized, the client's identity is known to
          the server.
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - not_found
                        description: A short code indicating the error code returned.
                        example: not_found
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: https://dub.co/docs/api-reference/errors#not-found
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: not_found
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#not-found
        description: The server cannot find the requested resource.
    '409':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - conflict
                        description: A short code indicating the error code returned.
                        example: conflict
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: https://dub.co/docs/api-reference/errors#conflict
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: conflict
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#conflict
        description: >-
          This response is sent when a request conflicts with the current state
          of the server.
    '410':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - invite_expired
                        description: A short code indicating the error code returned.
                        example: invite_expired
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: >-
                          https://dub.co/docs/api-reference/errors#invite-expired
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: invite_expired
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#invite-expired
        description: >-
          This response is sent when the requested content has been permanently
          deleted from server, with no forwarding address.
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - unprocessable_entity
                        description: A short code indicating the error code returned.
                        example: unprocessable_entity
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: >-
                          https://dub.co/docs/api-reference/errors#unprocessable-entity
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: unprocessable_entity
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#unprocessable-entity
        description: >-
          The request was well-formed but was unable to be followed due to
          semantic errors.
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - rate_limit_exceeded
                        description: A short code indicating the error code returned.
                        example: rate_limit_exceeded
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: >-
                          https://dub.co/docs/api-reference/errors#rate-limit_exceeded
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: rate_limit_exceeded
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#rate-limit_exceeded
        description: >-
          The user has sent too many requests in a given amount of time ("rate
          limiting")
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - internal_server_error
                        description: A short code indicating the error code returned.
                        example: internal_server_error
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: >-
                          https://dub.co/docs/api-reference/errors#internal-server_error
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: internal_server_error
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#internal-server_error
        description: The server has encountered a situation it does not know how to handle.
  deprecated: false
  type: path
components:
  schemas: {}

````