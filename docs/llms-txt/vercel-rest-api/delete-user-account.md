# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/user/delete-user-account.md

# Delete User Account

> Initiates the deletion process for the currently authenticated User, by sending a deletion confirmation email. The email contains a link that the user needs to visit in order to proceed with the deletion process.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/user
paths:
  path: /v1/user
  method: delete
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
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
              reasons:
                allOf:
                  - type: array
                    description: >-
                      Optional array of objects that describe the reason why the
                      User account is being deleted.
                    items:
                      type: object
                      description: >-
                        An object describing the reason why the User account is
                        being deleted.
                      required:
                        - slug
                        - description
                      additionalProperties: false
                      properties:
                        slug:
                          type: string
                          description: >-
                            Idenitifier slug of the reason why the User account
                            is being deleted.
                        description:
                          type: string
                          description: >-
                            Description of the reason why the User account is
                            being deleted.
            required: true
            additionalProperties: false
        examples:
          example:
            value:
              reasons:
                - slug: <string>
                  description: <string>
    codeSamples:
      - label: requestDelete
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.User.RequestDelete(ctx, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: requestDelete
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.user.requestDelete({});

            console.log(result);
          }

          run();
  response:
    '202':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: Unique identifier of the User who has initiated deletion.
              email:
                allOf:
                  - type: string
                    description: Email address of the User who has initiated deletion.
              message:
                allOf:
                  - type: string
                    description: User deletion progress status.
                    example: Verification email sent
            requiredProperties:
              - id
              - email
              - message
        examples:
          example:
            value:
              id: <string>
              email: <string>
              message: Verification email sent
        description: >-
          Response indicating that the User deletion process has been initiated,
          and a confirmation email has been sent.
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request body is invalid.
        examples: {}
        description: One of the provided values in the request body is invalid.
    '401': {}
    '402': {}
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````