# Source: https://polar.sh/docs/api-reference/files/complete-upload.md

# Complete File Upload

> Complete a file upload.

**Scopes**: `files:write`

## OpenAPI

````yaml post /v1/files/{id}/uploaded
paths:
  path: /v1/files/{id}/uploaded
  method: post
  servers:
    - url: https://api.polar.sh
      description: Production environment
    - url: https://sandbox-api.polar.sh
      description: Sandbox environment
  request:
    security:
      - title: access token
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                You can generate an **Organization Access Token** from your
                organization's settings.
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              title: Id
              description: The file ID.
              format: uuid4
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    title: Id
              path:
                allOf:
                  - type: string
                    title: Path
              parts:
                allOf:
                  - items:
                      $ref: '#/components/schemas/S3FileUploadCompletedPart'
                    type: array
                    title: Parts
            required: true
            title: FileUploadCompleted
            refIdentifier: '#/components/schemas/FileUploadCompleted'
            requiredProperties:
              - id
              - path
              - parts
        examples:
          example:
            value:
              id: <string>
              path: <string>
              parts:
                - number: 123
                  checksum_etag: <string>
                  checksum_sha256_base64: <string>
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\t\"os\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"github.com/polarsource/polar-go/models/components\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New(\n        polargo.WithSecurity(os.Getenv(\"POLAR_ACCESS_TOKEN\")),\n    )\n\n    res, err := s.Files.Uploaded(ctx, \"<value>\", components.FileUploadCompleted{\n        ID: \"<id>\",\n        Path: \"/boot\",\n        Parts: []components.S3FileUploadCompletedPart{\n            components.S3FileUploadCompletedPart{\n                Number: 979613,\n                ChecksumEtag: \"<value>\",\n                ChecksumSha256Base64: polargo.Pointer(\"<value>\"),\n            },\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.ResponseFilesUploaded != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          from polar_sdk import Polar


          with Polar(
              access_token="<YOUR_BEARER_TOKEN_HERE>",
          ) as polar:

              res = polar.files.uploaded(id="<value>", file_upload_completed={
                  "id": "<id>",
                  "path": "/boot",
                  "parts": [
                      {
                          "number": 979613,
                          "checksum_etag": "<value>",
                          "checksum_sha256_base64": "<value>",
                      },
                  ],
              })

              # Handle response
              print(res)
      - label: Typescript (SDK)
        lang: typescript
        source: |-
          import { Polar } from "@polar-sh/sdk";

          const polar = new Polar({
            accessToken: process.env["POLAR_ACCESS_TOKEN"] ?? "",
          });

          async function run() {
            const result = await polar.files.uploaded({
              id: "<value>",
              fileUploadCompleted: {
                id: "<id>",
                path: "/boot",
                parts: [
                  {
                    number: 979613,
                    checksumEtag: "<value>",
                    checksumSha256Base64: "<value>",
                  },
                ],
              },
            });

            console.log(result);
          }

          run();
      - label: PHP (SDK)
        lang: php
        source: |-
          declare(strict_types=1);

          require 'vendor/autoload.php';

          use Polar;
          use Polar\Models\Components;

          $sdk = Polar\Polar::builder()
              ->setSecurity(
                  '<YOUR_BEARER_TOKEN_HERE>'
              )
              ->build();

          $fileUploadCompleted = new Components\FileUploadCompleted(
              id: '<id>',
              path: '/boot',
              parts: [
                  new Components\S3FileUploadCompletedPart(
                      number: 979613,
                      checksumEtag: '<value>',
                      checksumSha256Base64: '<value>',
                  ),
              ],
          );

          $response = $sdk->files->uploaded(
              id: '<value>',
              fileUploadCompleted: $fileUploadCompleted

          );

          if ($response->responseFilesUploaded !== null) {
              // handle response
          }
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Id
                    description: The ID of the object.
              organization_id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Organization Id
              name:
                allOf:
                  - type: string
                    title: Name
              path:
                allOf:
                  - type: string
                    title: Path
              mime_type:
                allOf:
                  - type: string
                    title: Mime Type
              size:
                allOf:
                  - type: integer
                    title: Size
              storage_version:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Storage Version
              checksum_etag:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Checksum Etag
              checksum_sha256_base64:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Checksum Sha256 Base64
              checksum_sha256_hex:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Checksum Sha256 Hex
              last_modified_at:
                allOf:
                  - anyOf:
                      - type: string
                        format: date-time
                      - type: 'null'
                    title: Last Modified At
              version:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Version
              service:
                allOf:
                  - type: string
                    const: downloadable
                    title: Service
              is_uploaded:
                allOf:
                  - type: boolean
                    title: Is Uploaded
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    title: Created At
              size_readable:
                allOf:
                  - type: string
                    title: Size Readable
            title: DownloadableFileRead
            description: File to be associated with the downloadables benefit.
            refIdentifier: '#/components/schemas/DownloadableFileRead'
            requiredProperties:
              - id
              - organization_id
              - name
              - path
              - mime_type
              - size
              - storage_version
              - checksum_etag
              - checksum_sha256_base64
              - checksum_sha256_hex
              - last_modified_at
              - version
              - service
              - is_uploaded
              - created_at
              - size_readable
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Id
                    description: The ID of the object.
              organization_id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Organization Id
              name:
                allOf:
                  - type: string
                    title: Name
              path:
                allOf:
                  - type: string
                    title: Path
              mime_type:
                allOf:
                  - type: string
                    title: Mime Type
              size:
                allOf:
                  - type: integer
                    title: Size
              storage_version:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Storage Version
              checksum_etag:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Checksum Etag
              checksum_sha256_base64:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Checksum Sha256 Base64
              checksum_sha256_hex:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Checksum Sha256 Hex
              last_modified_at:
                allOf:
                  - anyOf:
                      - type: string
                        format: date-time
                      - type: 'null'
                    title: Last Modified At
              version:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Version
              service:
                allOf:
                  - type: string
                    const: product_media
                    title: Service
              is_uploaded:
                allOf:
                  - type: boolean
                    title: Is Uploaded
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    title: Created At
              size_readable:
                allOf:
                  - type: string
                    title: Size Readable
              public_url:
                allOf:
                  - type: string
                    title: Public Url
            title: ProductMediaFileRead
            description: File to be used as a product media file.
            refIdentifier: '#/components/schemas/ProductMediaFileRead'
            requiredProperties:
              - id
              - organization_id
              - name
              - path
              - mime_type
              - size
              - storage_version
              - checksum_etag
              - checksum_sha256_base64
              - checksum_sha256_hex
              - last_modified_at
              - version
              - service
              - is_uploaded
              - created_at
              - size_readable
              - public_url
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Id
                    description: The ID of the object.
              organization_id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Organization Id
              name:
                allOf:
                  - type: string
                    title: Name
              path:
                allOf:
                  - type: string
                    title: Path
              mime_type:
                allOf:
                  - type: string
                    title: Mime Type
              size:
                allOf:
                  - type: integer
                    title: Size
              storage_version:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Storage Version
              checksum_etag:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Checksum Etag
              checksum_sha256_base64:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Checksum Sha256 Base64
              checksum_sha256_hex:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Checksum Sha256 Hex
              last_modified_at:
                allOf:
                  - anyOf:
                      - type: string
                        format: date-time
                      - type: 'null'
                    title: Last Modified At
              version:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Version
              service:
                allOf:
                  - type: string
                    const: organization_avatar
                    title: Service
              is_uploaded:
                allOf:
                  - type: boolean
                    title: Is Uploaded
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    title: Created At
              size_readable:
                allOf:
                  - type: string
                    title: Size Readable
              public_url:
                allOf:
                  - type: string
                    title: Public Url
            title: OrganizationAvatarFileRead
            description: File to be used as an organization avatar.
            refIdentifier: '#/components/schemas/OrganizationAvatarFileRead'
            requiredProperties:
              - id
              - organization_id
              - name
              - path
              - mime_type
              - size
              - storage_version
              - checksum_etag
              - checksum_sha256_base64
              - checksum_sha256_hex
              - last_modified_at
              - version
              - service
              - is_uploaded
              - created_at
              - size_readable
              - public_url
        examples:
          example:
            value:
              id: <string>
              organization_id: <string>
              name: <string>
              path: <string>
              mime_type: <string>
              size: 123
              storage_version: <string>
              checksum_etag: <string>
              checksum_sha256_base64: <string>
              checksum_sha256_hex: <string>
              last_modified_at: '2023-11-07T05:31:56Z'
              version: <string>
              service: <string>
              is_uploaded: true
              created_at: '2023-11-07T05:31:56Z'
              size_readable: <string>
        description: File upload completed.
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    const: NotPermitted
                    title: Error
                    examples:
                      - NotPermitted
              detail:
                allOf:
                  - type: string
                    title: Detail
            title: NotPermitted
            refIdentifier: '#/components/schemas/NotPermitted'
            requiredProperties:
              - error
              - detail
        examples:
          example:
            value:
              error: NotPermitted
              detail: <string>
        description: You don't have the permission to update this file.
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    const: ResourceNotFound
                    title: Error
                    examples:
                      - ResourceNotFound
              detail:
                allOf:
                  - type: string
                    title: Detail
            title: ResourceNotFound
            refIdentifier: '#/components/schemas/ResourceNotFound'
            requiredProperties:
              - error
              - detail
        examples:
          example:
            value:
              error: ResourceNotFound
              detail: <string>
        description: File not found.
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    type: array
                    title: Detail
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
    S3FileUploadCompletedPart:
      properties:
        number:
          type: integer
          title: Number
        checksum_etag:
          type: string
          title: Checksum Etag
        checksum_sha256_base64:
          anyOf:
            - type: string
            - type: 'null'
          title: Checksum Sha256 Base64
      type: object
      required:
        - number
        - checksum_etag
        - checksum_sha256_base64
      title: S3FileUploadCompletedPart
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````