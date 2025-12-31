# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/accept-project-transfer-request.md

# Accept project transfer request

> Accept a project transfer request initated by another team. <br/> The `code` is generated using the `POST /projects/:idOrName/transfer-request` endpoint.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /projects/transfer-request/{code}
paths:
  path: /projects/transfer-request/{code}
  method: put
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
      path:
        code:
          schema:
            - type: string
              required: true
              description: The code of the project transfer request.
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              newProjectName:
                allOf:
                  - description: The desired name for the project
                    example: a-project-name
                    type: string
                    maxLength: 100
              paidFeatures:
                allOf:
                  - type: object
                    additionalProperties: false
                    properties:
                      concurrentBuilds:
                        type: integer
                        nullable: true
                      passwordProtection:
                        type: boolean
                        nullable: true
                      previewDeploymentSuffix:
                        type: boolean
                        nullable: true
              acceptedPolicies:
                allOf:
                  - type: object
                    additionalProperties:
                      type: object
                      additionalProperties:
                        type: string
                        format: date-time
                      required:
                        - eula
                        - privacy
                      properties:
                        eula:
                          type: string
                          format: date-time
                        privacy:
                          type: string
                          format: date-time
            additionalProperties: false
        examples:
          example:
            value:
              newProjectName: a-project-name
              paidFeatures:
                concurrentBuilds: 123
                passwordProtection: true
                previewDeploymentSuffix: true
              acceptedPolicies: {}
    codeSamples:
      - label: acceptProjectTransferRequest
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.acceptProjectTransferRequest({
              code: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                newProjectName: "a-project-name",
              },
            });

            console.log(result);
          }

          run();
  response:
    '202':
      application/json:
        schemaArray:
          - type: object
            properties:
              partnerCalls:
                allOf:
                  - items:
                      properties:
                        installationId:
                          type: string
                        resourceIds:
                          items:
                            type: string
                          type: array
                        result:
                          properties:
                            status:
                              type: string
                              enum:
                                - fulfilled
                                - errored
                            error:
                              type: object
                            code:
                              type: string
                          required:
                            - status
                          type: object
                      required:
                        - installationId
                        - resourceIds
                        - result
                      type: object
                    type: array
              resourceTransferErrors:
                allOf:
                  - items:
                      type: object
                    type: array
            requiredProperties:
              - partnerCalls
              - resourceTransferErrors
          - type: object
            properties: {}
        examples:
          example:
            value:
              partnerCalls:
                - installationId: <string>
                  resourceIds:
                    - <string>
                  result:
                    status: fulfilled
                    error: {}
                    code: <string>
              resourceTransferErrors:
                - {}
        description: The project has been transferred successfully.
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
    '422': {}
  deprecated: false
  type: path
components:
  schemas: {}

````