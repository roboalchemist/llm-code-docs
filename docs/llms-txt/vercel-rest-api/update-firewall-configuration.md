# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/update-firewall-configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Firewall Configuration

> Process updates to modify the existing firewall config for a project



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/security/firewall/config
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
  /v1/security/firewall/config:
    patch:
      tags:
        - security
      summary: Update Firewall Configuration
      description: Process updates to modify the existing firewall config for a project
      operationId: updateFirewallConfig
      parameters:
        - name: projectId
          in: query
          required: true
          schema:
            type: string
        - description: The Team identifier to perform the request on behalf of.
          in: query
          name: teamId
          schema:
            type: string
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        - description: The Team slug to perform the request on behalf of.
          in: query
          name: slug
          schema:
            type: string
            example: my-team-url-slug
      requestBody:
        content:
          application/json:
            schema:
              oneOf:
                - description: Enable Firewall
                  type: object
                  properties:
                    action:
                      type: string
                      enum:
                        - firewallEnabled
                    id:
                      nullable: true
                    value:
                      type: boolean
                  required:
                    - action
                    - value
                  additionalProperties: false
                - description: Add a custom rule
                  type: object
                  properties:
                    action:
                      type: string
                      enum:
                        - rules.insert
                    id:
                      nullable: true
                    value:
                      type: object
                      properties:
                        name:
                          type: string
                          maxLength: 160
                        description:
                          type: string
                          maxLength: 256
                        active:
                          type: boolean
                        conditionGroup:
                          type: array
                          items:
                            type: object
                            properties:
                              conditions:
                                type: array
                                items:
                                  type: object
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - host
                                        - path
                                        - method
                                        - header
                                        - query
                                        - cookie
                                        - target_path
                                        - route
                                        - raw_path
                                        - ip_address
                                        - region
                                        - protocol
                                        - scheme
                                        - environment
                                        - user_agent
                                        - geo_continent
                                        - geo_country
                                        - geo_country_region
                                        - geo_city
                                        - geo_as_number
                                        - ja4_digest
                                        - ja3_digest
                                        - rate_limit_api_id
                                        - server_action
                                        - bot_name
                                        - bot_category
                                    op:
                                      type: string
                                      enum:
                                        - re
                                        - eq
                                        - neq
                                        - ex
                                        - nex
                                        - inc
                                        - ninc
                                        - pre
                                        - suf
                                        - sub
                                        - gt
                                        - gte
                                        - lt
                                        - lte
                                    neg:
                                      type: boolean
                                    key:
                                      type: string
                                    value:
                                      oneOf:
                                        - type: string
                                        - type: array
                                          items:
                                            type: string
                                          maxItems: 75
                                        - type: number
                                  required:
                                    - type
                                    - op
                                  additionalProperties: false
                                maxItems: 65
                            required:
                              - conditions
                            additionalProperties: false
                          maxItems: 25
                        action:
                          type: object
                          properties:
                            mitigate:
                              type: object
                              properties:
                                action:
                                  type: string
                                  enum:
                                    - log
                                    - challenge
                                    - deny
                                    - bypass
                                    - rate_limit
                                    - redirect
                                rateLimit:
                                  anyOf:
                                    - type: object
                                      properties:
                                        algo:
                                          type: string
                                          enum:
                                            - fixed_window
                                            - token_bucket
                                        window:
                                          type: number
                                        limit:
                                          type: number
                                        keys:
                                          items:
                                            type: string
                                          type: array
                                        action:
                                          anyOf:
                                            - type: string
                                              enum:
                                                - log
                                                - challenge
                                                - deny
                                                - rate_limit
                                            - {}
                                          nullable: true
                                      required:
                                        - algo
                                        - window
                                        - limit
                                        - keys
                                      additionalProperties: false
                                    - {}
                                  nullable: true
                                redirect:
                                  anyOf:
                                    - type: object
                                      properties:
                                        location:
                                          type: string
                                        permanent:
                                          type: boolean
                                      required:
                                        - location
                                        - permanent
                                      additionalProperties: false
                                    - {}
                                  nullable: true
                                actionDuration:
                                  nullable: true
                                  type: string
                                bypassSystem:
                                  type: boolean
                                  nullable: true
                              required:
                                - action
                              additionalProperties: false
                          additionalProperties: false
                        valid:
                          type: boolean
                        validationErrors:
                          anyOf:
                            - items:
                                type: string
                              type: array
                            - type: string
                      required:
                        - name
                        - active
                        - conditionGroup
                        - action
                      additionalProperties: false
                  required:
                    - action
                    - value
                  additionalProperties: false
                - description: Update a custom rule
                  type: object
                  properties:
                    action:
                      type: string
                      enum:
                        - rules.update
                    id:
                      type: string
                    value:
                      type: object
                      properties:
                        name:
                          type: string
                          maxLength: 160
                        description:
                          type: string
                          maxLength: 256
                        active:
                          type: boolean
                        conditionGroup:
                          type: array
                          items:
                            type: object
                            properties:
                              conditions:
                                type: array
                                items:
                                  type: object
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - host
                                        - path
                                        - method
                                        - header
                                        - query
                                        - cookie
                                        - target_path
                                        - route
                                        - raw_path
                                        - ip_address
                                        - region
                                        - protocol
                                        - scheme
                                        - environment
                                        - user_agent
                                        - geo_continent
                                        - geo_country
                                        - geo_country_region
                                        - geo_city
                                        - geo_as_number
                                        - ja4_digest
                                        - ja3_digest
                                        - rate_limit_api_id
                                        - server_action
                                        - bot_name
                                        - bot_category
                                    op:
                                      type: string
                                      enum:
                                        - re
                                        - eq
                                        - neq
                                        - ex
                                        - nex
                                        - inc
                                        - ninc
                                        - pre
                                        - suf
                                        - sub
                                        - gt
                                        - gte
                                        - lt
                                        - lte
                                    neg:
                                      type: boolean
                                    key:
                                      type: string
                                    value:
                                      anyOf:
                                        - type: string
                                        - type: array
                                          items:
                                            type: string
                                          maxItems: 75
                                        - type: number
                                  required:
                                    - type
                                    - op
                                  additionalProperties: false
                                maxItems: 65
                            required:
                              - conditions
                            additionalProperties: false
                          maxItems: 25
                        action:
                          type: object
                          properties:
                            mitigate:
                              type: object
                              properties:
                                action:
                                  type: string
                                  enum:
                                    - log
                                    - challenge
                                    - deny
                                    - bypass
                                    - rate_limit
                                    - redirect
                                rateLimit:
                                  anyOf:
                                    - type: object
                                      properties:
                                        algo:
                                          type: string
                                          enum:
                                            - fixed_window
                                            - token_bucket
                                        window:
                                          type: number
                                        limit:
                                          type: number
                                        keys:
                                          items:
                                            type: string
                                          type: array
                                        action:
                                          anyOf:
                                            - type: string
                                              enum:
                                                - log
                                                - challenge
                                                - deny
                                                - rate_limit
                                            - {}
                                          nullable: true
                                      required:
                                        - algo
                                        - window
                                        - limit
                                        - keys
                                      additionalProperties: false
                                    - {}
                                  nullable: true
                                redirect:
                                  anyOf:
                                    - type: object
                                      properties:
                                        location:
                                          type: string
                                        permanent:
                                          type: boolean
                                      required:
                                        - location
                                        - permanent
                                      additionalProperties: false
                                    - {}
                                  nullable: true
                                actionDuration:
                                  nullable: true
                                  type: string
                                bypassSystem:
                                  type: boolean
                                  nullable: true
                              required:
                                - action
                              additionalProperties: false
                          additionalProperties: false
                        valid:
                          type: boolean
                        validationErrors:
                          anyOf:
                            - items:
                                type: string
                              type: array
                            - type: string
                      required:
                        - name
                        - active
                        - conditionGroup
                        - action
                      additionalProperties: false
                  required:
                    - action
                    - id
                    - value
                  additionalProperties: false
                - description: Remove a custom rule
                  type: object
                  properties:
                    action:
                      type: string
                      enum:
                        - rules.remove
                    id:
                      type: string
                    value:
                      nullable: true
                  required:
                    - action
                    - id
                  additionalProperties: false
                - description: Reorder a custom rule
                  type: object
                  properties:
                    action:
                      type: string
                      enum:
                        - rules.priority
                    id:
                      type: string
                    value:
                      type: number
                  required:
                    - action
                    - id
                    - value
                  additionalProperties: false
                - description: Enable a managed rule
                  type: object
                  properties:
                    action:
                      type: string
                      enum:
                        - crs.update
                    id:
                      type: string
                      enum:
                        - sd
                        - ma
                        - lfi
                        - rfi
                        - rce
                        - php
                        - gen
                        - xss
                        - sqli
                        - sf
                        - java
                    value:
                      type: object
                      properties:
                        active:
                          type: boolean
                        action:
                          type: string
                          enum:
                            - deny
                            - log
                      required:
                        - active
                        - action
                      additionalProperties: false
                  required:
                    - action
                    - id
                    - value
                  additionalProperties: false
                - description: Disable a managed rule
                  type: object
                  properties:
                    action:
                      type: string
                      enum:
                        - crs.disable
                    id:
                      nullable: true
                    value:
                      nullable: true
                  required:
                    - action
                  additionalProperties: false
                - description: Add an IP Blocking rule
                  type: object
                  properties:
                    action:
                      type: string
                      enum:
                        - ip.insert
                    id:
                      nullable: true
                    value:
                      type: object
                      properties:
                        hostname:
                          type: string
                        ip:
                          type: string
                        notes:
                          type: string
                        action:
                          type: string
                          enum:
                            - deny
                            - challenge
                            - log
                            - bypass
                      required:
                        - hostname
                        - ip
                        - action
                      additionalProperties: false
                  required:
                    - action
                    - value
                  additionalProperties: false
                - description: Update an IP Blocking rule
                  type: object
                  properties:
                    action:
                      type: string
                      enum:
                        - ip.update
                    id:
                      type: string
                    value:
                      type: object
                      properties:
                        hostname:
                          type: string
                        ip:
                          type: string
                        notes:
                          type: string
                        action:
                          type: string
                          enum:
                            - deny
                            - challenge
                            - log
                            - bypass
                      required:
                        - hostname
                        - ip
                        - action
                      additionalProperties: false
                  required:
                    - action
                    - id
                    - value
                  additionalProperties: false
                - description: Remove an IP Blocking rule
                  type: object
                  properties:
                    action:
                      type: string
                      enum:
                        - ip.remove
                    id:
                      type: string
                    value:
                      nullable: true
                  required:
                    - action
                    - id
                  additionalProperties: false
                - description: Update a managed ruleset
                  type: object
                  properties:
                    action:
                      type: string
                      enum:
                        - managedRules.update
                    id:
                      type: string
                      enum:
                        - ai_bots
                        - bot_filter
                        - bot_protection
                        - vercel_ruleset
                        - owasp
                    value:
                      type: object
                      properties:
                        action:
                          type: string
                          enum:
                            - log
                            - challenge
                            - deny
                        active:
                          type: boolean
                      required:
                        - active
                      additionalProperties: false
                  required:
                    - action
                    - id
                    - value
                  additionalProperties: false
                - description: Update a managed rule group
                  type: object
                  properties:
                    action:
                      type: string
                    id:
                      type: string
                      enum:
                        - ai_bots
                        - bot_filter
                        - bot_protection
                        - vercel_ruleset
                        - owasp
                    value:
                      type: object
                      additionalProperties:
                        type: object
                        properties:
                          action:
                            type: string
                            enum:
                              - log
                              - challenge
                              - deny
                          active:
                            type: boolean
                        required:
                          - active
                        additionalProperties: false
                  required:
                    - action
                    - id
                    - value
                  additionalProperties: false
                - description: Toggle bot ID
                  type: object
                  properties:
                    action:
                      type: string
                    id:
                      type: string
                    value:
                      type: boolean
                  required:
                    - action
                    - value
                  additionalProperties: false
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '402':
          description: ''
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
        '500':
          description: ''
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````