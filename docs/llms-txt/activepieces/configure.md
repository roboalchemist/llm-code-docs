# Source: https://www.activepieces.com/docs/endpoints/git-repos/configure.md

# Configure

> Upsert a git repository information for a project.

## OpenAPI

````yaml POST /v1/git-repos
paths:
  path: /v1/git-repos
  method: post
  servers:
    - url: https://cloud.activepieces.com/api
      description: Production Server
  request:
    security: []
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
              projectId:
                allOf:
                  - minLength: 1
                    type: string
              remoteUrl:
                allOf:
                  - pattern: ^git@
                    type: string
              branch:
                allOf:
                  - minLength: 1
                    type: string
              branchType:
                allOf:
                  - anyOf:
                      - type: string
                        enum:
                          - PRODUCTION
                      - type: string
                        enum:
                          - DEVELOPMENT
              sshPrivateKey:
                allOf:
                  - minLength: 1
                    type: string
              slug:
                allOf:
                  - minLength: 1
                    type: string
            required: true
            requiredProperties:
              - projectId
              - remoteUrl
              - branch
              - branchType
              - sshPrivateKey
              - slug
        examples:
          example:
            value:
              projectId: <string>
              remoteUrl: <string>
              branch: <string>
              branchType: PRODUCTION
              sshPrivateKey: <string>
              slug: <string>
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
              created:
                allOf:
                  - type: string
              updated:
                allOf:
                  - type: string
              remoteUrl:
                allOf:
                  - type: string
              branch:
                allOf:
                  - type: string
              branchType:
                allOf:
                  - anyOf:
                      - type: string
                        enum:
                          - PRODUCTION
                      - type: string
                        enum:
                          - DEVELOPMENT
              projectId:
                allOf:
                  - type: string
              slug:
                allOf:
                  - type: string
            requiredProperties:
              - id
              - created
              - updated
              - remoteUrl
              - branch
              - branchType
              - projectId
              - slug
        examples:
          example:
            value:
              id: <string>
              created: <string>
              updated: <string>
              remoteUrl: <string>
              branch: <string>
              branchType: PRODUCTION
              projectId: <string>
              slug: <string>
        description: Default Response
  deprecated: false
  type: path
components:
  schemas: {}

````