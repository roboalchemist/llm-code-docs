# Source: https://dub.co/docs/api-reference/endpoint/retrieve-a-customer.md

# Retrieve a customer

> Retrieve a customer by ID for the authenticated workspace.

## OpenAPI

````yaml get /customers/{id}
paths:
  path: /customers/{id}
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
      path:
        id:
          schema:
            - type: string
              required: true
              description: >-
                The unique ID of the customer. You may use either the customer's
                `id` on Dub (obtained via `/customers` endpoint) or their
                `externalId` (unique ID within your system, prefixed with
                `ext_`, e.g. `ext_123`).
      query:
        includeExpandedFields:
          schema:
            - type: boolean
              description: >-
                Whether to include expanded fields on the customer (`link`,
                `partner`, `discount`).
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getCustomer
        lang: python
        source: |-
          from dub import Dub


          with Dub(
              token="DUB_API_KEY",
          ) as d_client:

              res = d_client.customers.get(request={
                  "id": "<id>",
              })

              assert res is not None

              # Handle response
              print(res)
      - label: getCustomer
        lang: php
        source: |-
          declare(strict_types=1);

          require 'vendor/autoload.php';

          use Dub;

          $sdk = Dub\Dub::builder()
              ->setSecurity(
                  'DUB_API_KEY'
              )
              ->build();



          $response = $sdk->customers->get(
              id: '<id>'
          );

          if ($response->object !== null) {
              // handle response
          }
      - label: getCustomer
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\tdubgo \"github.com/dubinc/dub-go\"\n\t\"github.com/dubinc/dub-go/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := dubgo.New(\n        dubgo.WithSecurity(\"DUB_API_KEY\"),\n    )\n\n    res, err := s.Customers.Get(ctx, operations.GetCustomerRequest{\n        ID: \"<id>\",\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: getCustomer
        lang: ruby
        source: |-
          require 'dub'

          Models = ::OpenApiSDK::Models
          s = ::OpenApiSDK::Dub.new(
                security: Models::Shared::Security.new(
                  token: 'DUB_API_KEY',
                ),
              )

          req = Models::Operations::GetCustomerRequest.new(
            id: '<id>',
          )

          res = s.customers.get(request: req)

          unless res.nil?
            # handle response
          end
      - label: getCustomer
        lang: typescript
        source: |-
          import { Dub } from "dub";

          const dub = new Dub({
            token: "DUB_API_KEY",
          });

          async function run() {
            const result = await dub.customers.get({
              id: "<id>",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: >-
                      The unique ID of the customer. You may use either the
                      customer's `id` on Dub (obtained via `/customers`
                      endpoint) or their `externalId` (unique ID within your
                      system, prefixed with `ext_`, e.g. `ext_123`).
              externalId:
                allOf:
                  - type: string
                    description: Unique identifier for the customer in the client's app.
              name:
                allOf:
                  - type: string
                    description: Name of the customer.
              email:
                allOf:
                  - type: string
                    nullable: true
                    description: Email of the customer.
              avatar:
                allOf:
                  - type: string
                    nullable: true
                    description: Avatar URL of the customer.
              country:
                allOf:
                  - type: string
                    nullable: true
                    description: Country of the customer.
              sales:
                allOf:
                  - type: number
                    nullable: true
                    description: Total number of sales for the customer.
              saleAmount:
                allOf:
                  - type: number
                    nullable: true
                    description: Total amount of sales for the customer.
              createdAt:
                allOf:
                  - type: string
                    description: The date the customer was created.
              link:
                allOf:
                  - type: object
                    nullable: true
                    properties:
                      id:
                        type: string
                        description: The unique ID of the short link.
                      domain:
                        type: string
                        description: >-
                          The domain of the short link. If not provided, the
                          primary domain for the workspace will be used (or
                          `dub.sh` if the workspace has no domains).
                      key:
                        type: string
                        description: >-
                          The short link slug. If not provided, a random
                          7-character slug will be generated.
                      shortLink:
                        type: string
                        format: uri
                        description: >-
                          The full URL of the short link, including the https
                          protocol (e.g. `https://dub.sh/try`).
                      url:
                        type: string
                        format: uri
                        description: The destination URL of the short link.
                      programId:
                        type: string
                        nullable: true
                        description: >-
                          The ID of the program the short link is associated
                          with.
                    required:
                      - id
                      - domain
                      - key
                      - shortLink
                      - url
                      - programId
                    title: Link
              programId:
                allOf:
                  - type: string
                    nullable: true
              partner:
                allOf:
                  - type: object
                    nullable: true
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
                          The partner's email address. Should be a unique value
                          across Dub.
                      image:
                        type: string
                        nullable: true
                        description: The partner's avatar image.
                    required:
                      - id
                      - name
                      - email
                      - image
              discount:
                allOf:
                  - type: object
                    nullable: true
                    properties:
                      id:
                        type: string
                      amount:
                        type: number
                      type:
                        type: string
                        enum:
                          - percentage
                          - flat
                      maxDuration:
                        type: number
                        nullable: true
                      couponId:
                        type: string
                        nullable: true
                      couponTestId:
                        type: string
                        nullable: true
                      description:
                        type: string
                        nullable: true
                      partnersCount:
                        type: number
                        nullable: true
                    required:
                      - id
                      - amount
                      - type
                      - maxDuration
                      - couponId
                      - couponTestId
            requiredProperties:
              - id
              - externalId
              - name
              - createdAt
        examples:
          example:
            value:
              id: <string>
              externalId: <string>
              name: <string>
              email: <string>
              avatar: <string>
              country: <string>
              sales: 123
              saleAmount: 123
              createdAt: <string>
              link:
                id: <string>
                domain: <string>
                key: <string>
                shortLink: <string>
                url: <string>
                programId: <string>
              programId: <string>
              partner:
                id: <string>
                name: <string>
                email: <string>
                image: <string>
              discount:
                id: <string>
                amount: 123
                type: percentage
                maxDuration: 123
                couponId: <string>
                couponTestId: <string>
                description: <string>
                partnersCount: 123
        description: The customer object.
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