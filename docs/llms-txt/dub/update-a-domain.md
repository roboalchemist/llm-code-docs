# Source: https://dub.co/docs/api-reference/endpoint/update-a-domain.md

# Update a domain

> Update a domain for the authenticated workspace.

## OpenAPI

````yaml patch /domains/{slug}
paths:
  path: /domains/{slug}
  method: patch
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
        slug:
          schema:
            - type: string
              required: true
              description: The domain name.
              example: acme.com
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              slug:
                allOf:
                  - type: string
                    minLength: 1
                    maxLength: 190
                    description: Name of the domain.
                    example: acme.com
              expiredUrl:
                allOf:
                  - type: string
                    nullable: true
                    maxLength: 32000
                    description: >-
                      Redirect users to a specific URL when any link under this
                      domain has expired.
                    example: https://acme.com/expired
              notFoundUrl:
                allOf:
                  - type: string
                    nullable: true
                    maxLength: 32000
                    description: >-
                      Redirect users to a specific URL when a link under this
                      domain doesn't exist.
                    example: https://acme.com/not-found
              archived:
                allOf:
                  - type: boolean
                    default: false
                    description: >-
                      Whether to archive this domain. `false` will unarchive a
                      previously archived domain.
                    example: false
              placeholder:
                allOf:
                  - type: string
                    nullable: true
                    maxLength: 100
                    description: >-
                      Provide context to your teammates in the link creation
                      modal by showing them an example of a link to be
                      shortened.
                    example: https://dub.co/help/article/what-is-dub
              logo:
                allOf:
                  - nullable: true
                    anyOf:
                      - type: string
                        pattern: ^data:image\/(png|jpeg|jpg|gif|webp);base64,
                      - type: string
                        format: uri
                      - type: string
                        format: uri
                    description: The logo of the domain.
              assetLinks:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      assetLinks.json configuration file (for deep link support
                      on Android).
              appleAppSiteAssociation:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      apple-app-site-association configuration file (for deep
                      link support on iOS).
        examples:
          example:
            value:
              slug: acme.com
              expiredUrl: https://acme.com/expired
              notFoundUrl: https://acme.com/not-found
              archived: false
              placeholder: https://dub.co/help/article/what-is-dub
              logo: <string>
              assetLinks: <string>
              appleAppSiteAssociation: <string>
    codeSamples:
      - label: updateDomain
        lang: python
        source: |-
          from dub import Dub


          with Dub(
              token="DUB_API_KEY",
          ) as d_client:

              res = d_client.domains.update(slug="acme.com", request_body={
                  "slug": "acme.com",
                  "expired_url": "https://acme.com/expired",
                  "not_found_url": "https://acme.com/not-found",
                  "placeholder": "https://dub.co/help/article/what-is-dub",
              })

              assert res is not None

              # Handle response
              print(res)
      - label: updateDomain
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

          $requestBody = new Operations\UpdateDomainRequestBody(
              slug: 'acme.com',
              expiredUrl: 'https://acme.com/expired',
              notFoundUrl: 'https://acme.com/not-found',
              placeholder: 'https://dub.co/help/article/what-is-dub',
          );

          $response = $sdk->domains->update(
              slug: 'acme.com',
              requestBody: $requestBody

          );

          if ($response->domainSchema !== null) {
              // handle response
          }
      - label: updateDomain
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\tdubgo \"github.com/dubinc/dub-go\"\n\t\"github.com/dubinc/dub-go/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := dubgo.New(\n        dubgo.WithSecurity(\"DUB_API_KEY\"),\n    )\n\n    res, err := s.Domains.Update(ctx, \"acme.com\", &operations.UpdateDomainRequestBody{\n        Slug: dubgo.Pointer(\"acme.com\"),\n        ExpiredURL: dubgo.Pointer(\"https://acme.com/expired\"),\n        NotFoundURL: dubgo.Pointer(\"https://acme.com/not-found\"),\n        Placeholder: dubgo.Pointer(\"https://dub.co/help/article/what-is-dub\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: updateDomain
        lang: ruby
        source: >-
          require 'dub'


          Models = ::OpenApiSDK::Models

          s = ::OpenApiSDK::Dub.new(
                security: Models::Shared::Security.new(
                  token: 'DUB_API_KEY',
                ),
              )

          res = s.domains.update(slug: 'acme.com', request_body:
          Models::Operations::UpdateDomainRequestBody.new(
            slug: 'acme.com',
            expired_url: 'https://acme.com/expired',
            not_found_url: 'https://acme.com/not-found',
            placeholder: 'https://dub.co/help/article/what-is-dub',
          ))


          unless res.nil?
            # handle response
          end
      - label: updateDomain
        lang: typescript
        source: |-
          import { Dub } from "dub";

          const dub = new Dub({
            token: "DUB_API_KEY",
          });

          async function run() {
            const result = await dub.domains.update("acme.com");

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
                    description: The unique identifier of the domain.
              slug:
                allOf:
                  - type: string
                    description: The domain name.
                    example: acme.com
              verified:
                allOf:
                  - type: boolean
                    default: false
                    description: Whether the domain is verified.
              primary:
                allOf:
                  - type: boolean
                    default: false
                    description: >-
                      Whether the domain is the primary domain for the
                      workspace.
              archived:
                allOf:
                  - type: boolean
                    description: Whether the domain is archived.
                    default: false
              placeholder:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      Provide context to your teammates in the link creation
                      modal by showing them an example of a link to be
                      shortened.
                    example: https://dub.co/help/article/what-is-dub
              expiredUrl:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The URL to redirect to when a link under this domain has
                      expired.
                    example: https://acme.com/expired
              notFoundUrl:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The URL to redirect to when a link under this domain
                      doesn't exist.
                    example: https://acme.com/not-found
              logo:
                allOf:
                  - type: string
                    nullable: true
                    description: The logo of the domain.
              assetLinks:
                allOf:
                  - type: string
                    nullable: true
                    default: null
                    description: >-
                      assetLinks.json configuration file (for deep link support
                      on Android).
              appleAppSiteAssociation:
                allOf:
                  - type: string
                    nullable: true
                    default: null
                    description: >-
                      apple-app-site-association configuration file (for deep
                      link support on iOS).
              createdAt:
                allOf:
                  - type: string
                    description: The date the domain was created.
              updatedAt:
                allOf:
                  - type: string
                    description: The date the domain was last updated.
              registeredDomain:
                allOf:
                  - type: object
                    nullable: true
                    properties:
                      id:
                        type: string
                        description: The ID of the registered domain record.
                      autoRenewalDisabledAt:
                        type: string
                        nullable: true
                        description: The date the domain auto-renew is disabled.
                      createdAt:
                        type: string
                        description: The date the domain was created.
                      expiresAt:
                        type: string
                        description: The date the domain expires.
                      renewalFee:
                        type: number
                        description: The fee to renew the domain.
                    required:
                      - id
                      - autoRenewalDisabledAt
                      - createdAt
                      - expiresAt
                      - renewalFee
                    description: The registered domain record.
            refIdentifier: '#/components/schemas/DomainSchema'
            requiredProperties:
              - id
              - slug
              - verified
              - primary
              - archived
              - placeholder
              - expiredUrl
              - notFoundUrl
              - logo
              - assetLinks
              - appleAppSiteAssociation
              - createdAt
              - updatedAt
              - registeredDomain
        examples:
          example:
            value:
              id: <string>
              slug: acme.com
              verified: false
              primary: false
              archived: false
              placeholder: https://dub.co/help/article/what-is-dub
              expiredUrl: https://acme.com/expired
              notFoundUrl: https://acme.com/not-found
              logo: <string>
              assetLinks: null
              appleAppSiteAssociation: null
              createdAt: <string>
              updatedAt: <string>
              registeredDomain:
                id: <string>
                autoRenewalDisabledAt: <string>
                createdAt: <string>
                expiresAt: <string>
                renewalFee: 123
        description: The domain was updated.
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