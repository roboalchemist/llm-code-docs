# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/read-firewall-actions-by-project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Firewall Actions by Project

> Retrieve firewall actions for a project



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/security/firewall/events
openapi: 3.0.3
info:
  title: Vercel REST API & SDK
  description: >-
    The [`@vercel/sdk`](https://www.npmjs.com/package/@vercel/sdk) is a
    type-safe Typescript SDK that allows you to access the resources and methods
    of the Vercel REST API. Learn how to [install
    it](https://vercel.com/docs/rest-api/sdk#installing-vercel-sdk) and
    [authenticate](https://vercel.com/docs/rest-api/sdk#authentication) with a
    Vercel access token.
  contact:
    email: support@vercel.com
    name: Vercel Support
    url: https://vercel.com/support
  version: 0.0.1
servers:
  - url: https://api.vercel.com
    description: Production API
security: []
paths:
  /v1/security/firewall/events:
    get:
      tags:
        - security
      summary: Read Firewall Actions by Project
      description: Retrieve firewall actions for a project
      parameters:
        - name: projectId
          in: query
          required: true
          schema:
            type: string
        - name: startTimestamp
          in: query
          required: false
          schema:
            type: number
        - name: endTimestamp
          in: query
          required: false
          schema:
            type: number
        - name: hosts
          in: query
          required: false
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  actions:
                    items:
                      properties:
                        startTime:
                          type: string
                        endTime:
                          type: string
                        isActive:
                          type: boolean
                          enum:
                            - false
                            - true
                        action_type:
                          type: string
                        host:
                          type: string
                        public_ip:
                          type: string
                        count:
                          type: number
                      required:
                        - action_type
                        - count
                        - endTime
                        - host
                        - isActive
                        - public_ip
                        - startTime
                      type: object
                    type: array
                required:
                  - actions
                type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
        '500':
          description: ''
      security: []

````