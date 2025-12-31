# Source: https://dub.co/docs/api-reference/endpoint/update-a-link.md

# Update a link

> Update a link for the authenticated workspace. If there's no change, returns it as it is.

## OpenAPI

````yaml patch /links/{linkId}
paths:
  path: /links/{linkId}
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
        linkId:
          schema:
            - type: string
              required: true
              description: >-
                The id of the link to update. You may use either `linkId`
                (obtained via `/links/info` endpoint) or `externalId` prefixed
                with `ext_`.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              url:
                allOf:
                  - type: string
                    maxLength: 32000
                    description: The destination URL of the short link.
                    example: https://google.com
              domain:
                allOf:
                  - type: string
                    maxLength: 190
                    description: >-
                      The domain of the short link (without protocol). If not
                      provided, the primary domain for the workspace will be
                      used (or `dub.sh` if the workspace has no domains).
              key:
                allOf:
                  - type: string
                    maxLength: 190
                    description: >-
                      The short link slug. If not provided, a random 7-character
                      slug will be generated.
              externalId:
                allOf:
                  - type: string
                    nullable: true
                    minLength: 1
                    maxLength: 255
                    description: >-
                      The ID of the link in your database. If set, it can be
                      used to identify the link in future API requests (must be
                      prefixed with 'ext_' when passed as a query parameter).
                      This key is unique across your workspace.
                    example: '123456'
              tenantId:
                allOf:
                  - type: string
                    nullable: true
                    maxLength: 255
                    description: >-
                      The ID of the tenant that created the link inside your
                      system. If set, it can be used to fetch all links for a
                      tenant.
              programId:
                allOf:
                  - type: string
                    nullable: true
                    description: The ID of the program the short link is associated with.
              partnerId:
                allOf:
                  - type: string
                    nullable: true
                    description: The ID of the partner the short link is associated with.
              trackConversion:
                allOf:
                  - type: boolean
                    description: >-
                      Whether to track conversions for the short link. Defaults
                      to `false` if not provided.
              archived:
                allOf:
                  - type: boolean
                    description: >-
                      Whether the short link is archived. Defaults to `false` if
                      not provided.
              tagIds:
                allOf:
                  - anyOf:
                      - type: string
                      - type: array
                        items:
                          type: string
                    description: The unique IDs of the tags assigned to the short link.
                    example:
                      - clux0rgak00011...
              tagNames:
                allOf:
                  - anyOf:
                      - type: string
                      - type: array
                        items:
                          type: string
                    description: >-
                      The unique name of the tags assigned to the short link
                      (case insensitive).
              folderId:
                allOf:
                  - type: string
                    nullable: true
                    description: The unique ID existing folder to assign the short link to.
              comments:
                allOf:
                  - type: string
                    nullable: true
                    description: The comments for the short link.
              expiresAt:
                allOf:
                  - type: string
                    nullable: true
                    description: The date and time when the short link will expire at.
              expiredUrl:
                allOf:
                  - type: string
                    nullable: true
                    maxLength: 32000
                    description: The URL to redirect to when the short link has expired.
              password:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The password required to access the destination URL of the
                      short link.
              proxy:
                allOf:
                  - type: boolean
                    description: >-
                      Whether the short link uses Custom Link Previews feature.
                      Defaults to `false` if not provided.
              title:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The custom link preview title (og:title). Will be used for
                      Custom Link Previews if `proxy` is true. Learn more:
                      https://d.to/og
              description:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The custom link preview description (og:description). Will
                      be used for Custom Link Previews if `proxy` is true. Learn
                      more: https://d.to/og
              image:
                allOf:
                  - nullable: true
                    anyOf:
                      - type: string
                        pattern: ^data:image\/(png|jpeg|jpg|gif|webp);base64,
                      - type: string
                        format: uri
              video:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The custom link preview video (og:video). Will be used for
                      Custom Link Previews if `proxy` is true. Learn more:
                      https://d.to/og
              rewrite:
                allOf:
                  - type: boolean
                    description: >-
                      Whether the short link uses link cloaking. Defaults to
                      `false` if not provided.
              ios:
                allOf:
                  - type: string
                    nullable: true
                    maxLength: 32000
                    description: >-
                      The iOS destination URL for the short link for iOS device
                      targeting.
              android:
                allOf:
                  - type: string
                    nullable: true
                    maxLength: 32000
                    description: >-
                      The Android destination URL for the short link for Android
                      device targeting.
              geo:
                allOf:
                  - $ref: '#/components/schemas/linkGeoTargeting'
              doIndex:
                allOf:
                  - type: boolean
                    description: >-
                      Allow search engines to index your short link. Defaults to
                      `false` if not provided. Learn more: https://d.to/noindex
              utm_source:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The UTM source of the short link. If set, this will
                      populate or override the UTM source in the destination
                      URL.
              utm_medium:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The UTM medium of the short link. If set, this will
                      populate or override the UTM medium in the destination
                      URL.
              utm_campaign:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The UTM campaign of the short link. If set, this will
                      populate or override the UTM campaign in the destination
                      URL.
              utm_term:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The UTM term of the short link. If set, this will populate
                      or override the UTM term in the destination URL.
              utm_content:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The UTM content of the short link. If set, this will
                      populate or override the UTM content in the destination
                      URL.
              ref:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The referral tag of the short link. If set, this will
                      populate or override the `ref` query parameter in the
                      destination URL.
              webhookIds:
                allOf:
                  - type: array
                    nullable: true
                    items:
                      type: string
                    description: >-
                      An array of webhook IDs to trigger when the link is
                      clicked. These webhooks will receive click event data.
              testVariants:
                allOf:
                  - type: array
                    nullable: true
                    items:
                      type: object
                      properties:
                        url:
                          type: string
                        percentage:
                          type: number
                          minimum: 10
                          maximum: 90
                      required:
                        - url
                        - percentage
                    minItems: 2
                    maxItems: 4
                    description: >-
                      An array of A/B test URLs and the percentage of traffic to
                      send to each URL.
                    example:
                      - url: https://example.com/variant-1
                        percentage: 50
                      - url: https://example.com/variant-2
                        percentage: 50
              testStartedAt:
                allOf:
                  - type: string
                    nullable: true
                    description: The date and time when the tests started.
              testCompletedAt:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The date and time when the tests were or will be
                      completed.
              publicStats:
                allOf:
                  - type: boolean
                    description: >-
                      Deprecated: Use `dashboard` instead. Whether the short
                      link's stats are publicly accessible. Defaults to `false`
                      if not provided.
                    deprecated: true
              tagId:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      Deprecated: Use `tagIds` instead. The unique ID of the tag
                      assigned to the short link.
                    deprecated: true
        examples:
          example:
            value:
              url: https://google.com
              domain: <string>
              key: <string>
              externalId: '123456'
              tenantId: <string>
              programId: <string>
              partnerId: <string>
              trackConversion: true
              archived: true
              tagIds:
                - clux0rgak00011...
              tagNames: <string>
              folderId: <string>
              comments: <string>
              expiresAt: <string>
              expiredUrl: <string>
              password: <string>
              proxy: true
              title: <string>
              description: <string>
              image: <string>
              video: <string>
              rewrite: true
              ios: <string>
              android: <string>
              geo: {}
              doIndex: true
              utm_source: <string>
              utm_medium: <string>
              utm_campaign: <string>
              utm_term: <string>
              utm_content: <string>
              ref: <string>
              webhookIds:
                - <string>
              testVariants:
                - url: https://example.com/variant-1
                  percentage: 50
                - url: https://example.com/variant-2
                  percentage: 50
              testStartedAt: <string>
              testCompletedAt: <string>
              publicStats: true
              tagId: <string>
    codeSamples:
      - label: updateLink
        lang: python
        source: |-
          from dub import Dub


          with Dub(
              token="DUB_API_KEY",
          ) as d_client:

              res = d_client.links.update(link_id="<id>", request_body={
                  "url": "https://google.com",
                  "external_id": "123456",
                  "tag_ids": [
                      "clux0rgak00011...",
                  ],
                  "test_variants": [
                      {
                          "url": "https://example.com/variant-1",
                          "percentage": 50,
                      },
                      {
                          "url": "https://example.com/variant-2",
                          "percentage": 50,
                      },
                  ],
              })

              assert res is not None

              # Handle response
              print(res)
      - label: updateLink
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

          $requestBody = new Operations\UpdateLinkRequestBody(
              url: 'https://google.com',
              externalId: '123456',
              tagIds: [
                  'clux0rgak00011...',
              ],
              testVariants: [
                  new Operations\UpdateLinkTestVariants(
                      url: 'https://example.com/variant-1',
                      percentage: 50,
                  ),
                  new Operations\UpdateLinkTestVariants(
                      url: 'https://example.com/variant-2',
                      percentage: 50,
                  ),
              ],
          );

          $response = $sdk->links->update(
              linkId: '<id>',
              requestBody: $requestBody

          );

          if ($response->linkSchema !== null) {
              // handle response
          }
      - label: updateLink
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\tdubgo \"github.com/dubinc/dub-go\"\n\t\"github.com/dubinc/dub-go/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := dubgo.New(\n        dubgo.WithSecurity(\"DUB_API_KEY\"),\n    )\n\n    res, err := s.Links.Update(ctx, \"<id>\", &operations.UpdateLinkRequestBody{\n        URL: dubgo.Pointer(\"https://google.com\"),\n        ExternalID: dubgo.Pointer(\"123456\"),\n        TagIds: dubgo.Pointer(operations.CreateUpdateLinkTagIdsArrayOfStr(\n            []string{\n                \"clux0rgak00011...\",\n            },\n        )),\n        TestVariants: []operations.UpdateLinkTestVariants{\n            operations.UpdateLinkTestVariants{\n                URL: \"https://example.com/variant-1\",\n                Percentage: 50,\n            },\n            operations.UpdateLinkTestVariants{\n                URL: \"https://example.com/variant-2\",\n                Percentage: 50,\n            },\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: updateLink
        lang: ruby
        source: >-
          require 'dub'


          Models = ::OpenApiSDK::Models

          s = ::OpenApiSDK::Dub.new(
                security: Models::Shared::Security.new(
                  token: 'DUB_API_KEY',
                ),
              )

          res = s.links.update(link_id: '<id>', request_body:
          Models::Operations::UpdateLinkRequestBody.new(
            url: 'https://google.com',
            external_id: '123456',
            tag_ids: [
              'clux0rgak00011...',
            ],
            test_variants: [
              Models::Operations::UpdateLinkTestVariants.new(
                url: 'https://example.com/variant-1',
                percentage: 50.0,
              ),
              Models::Operations::UpdateLinkTestVariants.new(
                url: 'https://example.com/variant-2',
                percentage: 50.0,
              ),
            ],
          ))


          unless res.nil?
            # handle response
          end
      - label: updateLink
        lang: typescript
        source: |-
          import { Dub } from "dub";

          const dub = new Dub({
            token: "DUB_API_KEY",
          });

          async function run() {
            const result = await dub.links.update("<id>");

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
                    description: The unique ID of the short link.
              domain:
                allOf:
                  - type: string
                    description: >-
                      The domain of the short link. If not provided, the primary
                      domain for the workspace will be used (or `dub.sh` if the
                      workspace has no domains).
              key:
                allOf:
                  - type: string
                    description: >-
                      The short link slug. If not provided, a random 7-character
                      slug will be generated.
              url:
                allOf:
                  - type: string
                    format: uri
                    description: The destination URL of the short link.
              trackConversion:
                allOf:
                  - type: boolean
                    default: false
                    description: Whether to track conversions for the short link.
              externalId:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The ID of the link in your database. If set, it can be
                      used to identify the link in future API requests (must be
                      prefixed with 'ext_' when passed as a query parameter).
                      This key is unique across your workspace.
              tenantId:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The ID of the tenant that created the link inside your
                      system. If set, it can be used to fetch all links for a
                      tenant.
              programId:
                allOf:
                  - type: string
                    nullable: true
                    description: The ID of the program the short link is associated with.
              partnerId:
                allOf:
                  - type: string
                    nullable: true
                    description: The ID of the partner the short link is associated with.
              archived:
                allOf:
                  - type: boolean
                    default: false
                    description: Whether the short link is archived.
              expiresAt:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The date and time when the short link will expire in
                      ISO-8601 format.
              expiredUrl:
                allOf:
                  - type: string
                    nullable: true
                    format: uri
                    description: The URL to redirect to when the short link has expired.
              password:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The password required to access the destination URL of the
                      short link.
              proxy:
                allOf:
                  - type: boolean
                    default: false
                    description: Whether the short link uses Custom Link Previews feature.
              title:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The title of the short link. Will be used for Custom Link
                      Previews if `proxy` is true.
              description:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The description of the short link. Will be used for Custom
                      Link Previews if `proxy` is true.
              image:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The image of the short link. Will be used for Custom Link
                      Previews if `proxy` is true.
              video:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The custom link preview video (og:video). Will be used for
                      Custom Link Previews if `proxy` is true. Learn more:
                      https://d.to/og
              rewrite:
                allOf:
                  - type: boolean
                    default: false
                    description: Whether the short link uses link cloaking.
              doIndex:
                allOf:
                  - type: boolean
                    default: false
                    description: Whether to allow search engines to index the short link.
              ios:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The iOS destination URL for the short link for iOS device
                      targeting.
              android:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The Android destination URL for the short link for Android
                      device targeting.
              geo:
                allOf:
                  - type: object
                    nullable: true
                    additionalProperties:
                      type: string
                      format: uri
                    description: >-
                      Geo targeting information for the short link in JSON
                      format `{[COUNTRY]: https://example.com }`. See
                      https://d.to/geo for more information.
              publicStats:
                allOf:
                  - type: boolean
                    default: false
                    description: Whether the short link's stats are publicly accessible.
              tags:
                allOf:
                  - type: array
                    nullable: true
                    items:
                      $ref: '#/components/schemas/LinkTagSchema'
                    description: The tags assigned to the short link.
              folderId:
                allOf:
                  - type: string
                    nullable: true
                    description: The unique ID of the folder assigned to the short link.
              webhookIds:
                allOf:
                  - type: array
                    items:
                      type: string
                    description: >-
                      The IDs of the webhooks that the short link is associated
                      with.
              comments:
                allOf:
                  - type: string
                    nullable: true
                    description: The comments for the short link.
              shortLink:
                allOf:
                  - type: string
                    format: uri
                    description: >-
                      The full URL of the short link, including the https
                      protocol (e.g. `https://dub.sh/try`).
              qrCode:
                allOf:
                  - type: string
                    format: uri
                    description: >-
                      The full URL of the QR code for the short link (e.g.
                      `https://api.dub.co/qr?url=https://dub.sh/try`).
              utm_source:
                allOf:
                  - type: string
                    nullable: true
                    description: The UTM source of the short link.
              utm_medium:
                allOf:
                  - type: string
                    nullable: true
                    description: The UTM medium of the short link.
              utm_campaign:
                allOf:
                  - type: string
                    nullable: true
                    description: The UTM campaign of the short link.
              utm_term:
                allOf:
                  - type: string
                    nullable: true
                    description: The UTM term of the short link.
              utm_content:
                allOf:
                  - type: string
                    nullable: true
                    description: The UTM content of the short link.
              testVariants:
                allOf:
                  - type: array
                    nullable: true
                    items:
                      type: object
                      properties:
                        url:
                          type: string
                        percentage:
                          type: number
                          minimum: 10
                          maximum: 90
                      required:
                        - url
                        - percentage
                    minItems: 2
                    maxItems: 4
                    description: >-
                      An array of A/B test URLs and the percentage of traffic to
                      send to each URL.
                    example:
                      - url: https://example.com/variant-1
                        percentage: 50
                      - url: https://example.com/variant-2
                        percentage: 50
              testStartedAt:
                allOf:
                  - type: string
                    nullable: true
                    description: The date and time when the tests started.
              testCompletedAt:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      The date and time when the tests were or will be
                      completed.
              userId:
                allOf:
                  - type: string
                    nullable: true
                    description: The user ID of the creator of the short link.
              workspaceId:
                allOf:
                  - type: string
                    description: The workspace ID of the short link.
              clicks:
                allOf:
                  - type: number
                    default: 0
                    description: The number of clicks on the short link.
              leads:
                allOf:
                  - type: number
                    default: 0
                    description: The number of leads the short link has generated.
              conversions:
                allOf:
                  - type: number
                    default: 0
                    description: The number of leads that converted to paying customers.
              sales:
                allOf:
                  - type: number
                    default: 0
                    description: >-
                      The total number of sales (includes recurring sales)
                      generated by the short link.
              saleAmount:
                allOf:
                  - type: number
                    default: 0
                    description: >-
                      The total dollar value of sales (in cents) generated by
                      the short link.
              lastClicked:
                allOf:
                  - type: string
                    nullable: true
                    description: The date and time when the short link was last clicked.
              createdAt:
                allOf:
                  - type: string
                    description: The date and time when the short link was created.
              updatedAt:
                allOf:
                  - type: string
                    description: The date and time when the short link was last updated.
              tagId:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      Deprecated: Use `tags` instead. The unique ID of the tag
                      assigned to the short link.
                    deprecated: true
              projectId:
                allOf:
                  - type: string
                    description: >-
                      Deprecated: Use `workspaceId` instead. The project ID of
                      the short link.
                    deprecated: true
            title: Link
            refIdentifier: '#/components/schemas/LinkSchema'
            requiredProperties:
              - id
              - domain
              - key
              - url
              - trackConversion
              - externalId
              - tenantId
              - programId
              - partnerId
              - archived
              - expiresAt
              - expiredUrl
              - password
              - proxy
              - title
              - description
              - image
              - video
              - rewrite
              - doIndex
              - ios
              - android
              - geo
              - publicStats
              - tags
              - folderId
              - webhookIds
              - comments
              - shortLink
              - qrCode
              - utm_source
              - utm_medium
              - utm_campaign
              - utm_term
              - utm_content
              - userId
              - workspaceId
              - clicks
              - leads
              - conversions
              - sales
              - saleAmount
              - lastClicked
              - createdAt
              - updatedAt
              - tagId
              - projectId
        examples:
          example:
            value:
              id: <string>
              domain: <string>
              key: <string>
              url: <string>
              trackConversion: false
              externalId: <string>
              tenantId: <string>
              programId: <string>
              partnerId: <string>
              archived: false
              expiresAt: <string>
              expiredUrl: <string>
              password: <string>
              proxy: false
              title: <string>
              description: <string>
              image: <string>
              video: <string>
              rewrite: false
              doIndex: false
              ios: <string>
              android: <string>
              geo: {}
              publicStats: false
              tags:
                - id: <string>
                  name: <string>
                  color: red
              folderId: <string>
              webhookIds:
                - <string>
              comments: <string>
              shortLink: <string>
              qrCode: <string>
              utm_source: <string>
              utm_medium: <string>
              utm_campaign: <string>
              utm_term: <string>
              utm_content: <string>
              testVariants:
                - url: https://example.com/variant-1
                  percentage: 50
                - url: https://example.com/variant-2
                  percentage: 50
              testStartedAt: <string>
              testCompletedAt: <string>
              userId: <string>
              workspaceId: <string>
              clicks: 0
              leads: 0
              conversions: 0
              sales: 0
              saleAmount: 0
              lastClicked: <string>
              createdAt: <string>
              updatedAt: <string>
              tagId: <string>
              projectId: <string>
        description: The updated link
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
  schemas:
    LinkTagSchema:
      type: object
      properties:
        id:
          type: string
          description: The unique ID of the tag.
        name:
          type: string
          description: The name of the tag.
        color:
          type: string
          enum:
            - red
            - yellow
            - green
            - blue
            - purple
            - brown
            - pink
          description: The color of the tag.
      required:
        - id
        - name
        - color
      title: LinkTag
    linkGeoTargeting:
      type: object
      nullable: true
      additionalProperties:
        type: string
        maxLength: 32000
      description: >-
        Geo targeting information for the short link in JSON format `{[COUNTRY]:
        https://example.com }`. See https://d.to/geo for more information.

````