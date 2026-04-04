# Source: https://www.activepieces.com/docs/endpoints/git-repos/configure.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure

> Upsert a git repository information for a project.



## OpenAPI

````yaml POST /v1/git-repos
openapi: 3.0.3
info:
  title: Activepieces Documentation
  version: 0.0.0
servers:
  - url: https://cloud.activepieces.com/api
    description: Production Server
security: []
externalDocs:
  url: https://www.activepieces.com/docs
  description: Find more info here
paths:
  /v1/git-repos:
    post:
      tags:
        - git-repos
      description: Upsert a git repository information for a project.
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                projectId:
                  minLength: 1
                  type: string
                remoteUrl:
                  pattern: ^git@
                  type: string
                branch:
                  minLength: 1
                  type: string
                branchType:
                  anyOf:
                    - type: string
                      enum:
                        - PRODUCTION
                    - type: string
                      enum:
                        - DEVELOPMENT
                sshPrivateKey:
                  minLength: 1
                  type: string
                slug:
                  minLength: 1
                  type: string
              required:
                - projectId
                - remoteUrl
                - branch
                - branchType
                - sshPrivateKey
                - slug
        required: true
      responses:
        '201':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                  created:
                    type: string
                  updated:
                    type: string
                  remoteUrl:
                    type: string
                  branch:
                    type: string
                  branchType:
                    anyOf:
                      - type: string
                        enum:
                          - PRODUCTION
                      - type: string
                        enum:
                          - DEVELOPMENT
                  projectId:
                    type: string
                  slug:
                    type: string
                required:
                  - id
                  - created
                  - updated
                  - remoteUrl
                  - branch
                  - branchType
                  - projectId
                  - slug

````