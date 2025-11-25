# Source: https://dub.co/docs/api-reference/endpoint/track-lead.md

# Track a lead

> Track a lead for a short link.

## OpenAPI

````yaml post /track/lead
paths:
  path: /track/lead
  method: post
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              clickId:
                allOf:
                  - type: string
                    description: >-
                      The unique ID of the click that the lead conversion event
                      is attributed to. You can read this value from `dub_id`
                      cookie. [For deferred lead tracking]: If an empty string
                      is provided, Dub will try to find an existing customer
                      with the provided `customerExternalId` and use the
                      `clickId` from the customer if found.
              eventName:
                allOf:
                  - type: string
                    minLength: 1
                    maxLength: 255
                    description: >-
                      The name of the lead event to track. Can also be used as a
                      unique identifier to associate a given lead event for a
                      customer for a subsequent sale event (via the
                      `leadEventName` prop in `/track/sale`).
                    example: Sign up
              customerExternalId:
                allOf:
                  - type: string
                    minLength: 1
                    maxLength: 100
                    description: >-
                      The unique ID of the customer in your system. Will be used
                      to identify and attribute all future events to this
                      customer.
              customerName:
                allOf:
                  - type: string
                    nullable: true
                    maxLength: 100
                    default: null
                    description: >-
                      The name of the customer. If not passed, a random name
                      will be generated (e.g. “Big Red Caribou”).
              customerEmail:
                allOf:
                  - type: string
                    nullable: true
                    format: email
                    maxLength: 100
                    default: null
                    description: The email address of the customer.
              customerAvatar:
                allOf:
                  - type: string
                    nullable: true
                    default: null
                    description: The avatar URL of the customer.
              mode:
                allOf:
                  - type: string
                    enum:
                      - async
                      - wait
                      - deferred
                    default: async
                    description: >-
                      The mode to use for tracking the lead event. `async` will
                      not block the request; `wait` will block the request until
                      the lead event is fully recorded in Dub; `deferred` will
                      defer the lead event creation to a subsequent request.
              eventQuantity:
                allOf:
                  - type: number
                    nullable: true
                    description: >-
                      The numerical value associated with this lead event (e.g.,
                      number of provisioned seats in a free trial). If defined
                      as N, the lead event will be tracked N times.
              metadata:
                allOf:
                  - type: object
                    nullable: true
                    additionalProperties: {}
                    default: null
                    description: >-
                      Additional metadata to be stored with the lead event. Max
                      10,000 characters.
            requiredProperties:
              - clickId
              - eventName
              - customerExternalId
        examples:
          example:
            value:
              clickId: <string>
              eventName: Sign up
              customerExternalId: <string>
              customerName: null
              customerEmail: null
              customerAvatar: null
              mode: async
              eventQuantity: 123
              metadata: null
    codeSamples:
      - label: trackLead
        lang: python
        source: |-
          from dub import Dub


          with Dub(
              token="DUB_API_KEY",
          ) as d_client:

              res = d_client.track.lead(request={
                  "click_id": "<id>",
                  "event_name": "Sign up",
                  "customer_external_id": "<id>",
              })

              assert res is not None

              # Handle response
              print(res)
      - label: trackLead
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

          $request = new Operations\TrackLeadRequestBody(
              clickId: '<id>',
              eventName: 'Sign up',
              customerExternalId: '<id>',
          );

          $response = $sdk->track->lead(
              request: $request
          );

          if ($response->object !== null) {
              // handle response
          }
      - label: trackLead
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\tdubgo \"github.com/dubinc/dub-go\"\n\t\"github.com/dubinc/dub-go/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := dubgo.New(\n        dubgo.WithSecurity(\"DUB_API_KEY\"),\n    )\n\n    res, err := s.Track.Lead(ctx, &operations.TrackLeadRequestBody{\n        ClickID: \"<id>\",\n        EventName: \"Sign up\",\n        CustomerExternalID: \"<id>\",\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: trackLead
        lang: ruby
        source: |-
          require 'dub'

          Models = ::OpenApiSDK::Models
          s = ::OpenApiSDK::Dub.new(
                security: Models::Shared::Security.new(
                  token: 'DUB_API_KEY',
                ),
              )

          req = Models::Operations::TrackLeadRequestBody.new(
            click_id: '<id>',
            event_name: 'Sign up',
            customer_external_id: '<id>',
          )

          res = s.track.lead(request: req)

          unless res.nil?
            # handle response
          end
      - label: trackLead
        lang: typescript
        source: |-
          import { Dub } from "dub";

          const dub = new Dub({
            token: "DUB_API_KEY",
          });

          async function run() {
            const result = await dub.track.lead();

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              click:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                    required:
                      - id
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
                      partnerId:
                        type: string
                        nullable: true
                        description: >-
                          The ID of the partner the short link is associated
                          with.
                      programId:
                        type: string
                        nullable: true
                        description: >-
                          The ID of the program the short link is associated
                          with.
                      tenantId:
                        type: string
                        nullable: true
                        description: >-
                          The ID of the tenant that created the link inside your
                          system. If set, it can be used to fetch all links for
                          a tenant.
                      externalId:
                        type: string
                        nullable: true
                        description: >-
                          The ID of the link in your database. If set, it can be
                          used to identify the link in future API requests (must
                          be prefixed with 'ext_' when passed as a query
                          parameter). This key is unique across your workspace.
                    required:
                      - id
                      - domain
                      - key
                      - shortLink
                      - url
                      - partnerId
                      - programId
                      - tenantId
                      - externalId
                    title: Link
              customer:
                allOf:
                  - type: object
                    properties:
                      name:
                        type: string
                        nullable: true
                      email:
                        type: string
                        nullable: true
                      avatar:
                        type: string
                        nullable: true
                      externalId:
                        type: string
                        nullable: true
                    required:
                      - name
                      - email
                      - avatar
                      - externalId
            requiredProperties:
              - click
              - link
              - customer
        examples:
          example:
            value:
              click:
                id: <string>
              link:
                id: <string>
                domain: <string>
                key: <string>
                shortLink: <string>
                url: <string>
                partnerId: <string>
                programId: <string>
                tenantId: <string>
                externalId: <string>
              customer:
                name: <string>
                email: <string>
                avatar: <string>
                externalId: <string>
        description: A lead was tracked.
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