# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/update-firewall-configuration.md

# Update Firewall Configuration

> Process updates to modify the existing firewall config for a project

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/security/firewall/config
paths:
  path: /v1/security/firewall/config
  method: patch
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
      query:
        projectId:
          schema:
            - type: string
              required: true
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
              action:
                allOf:
                  - type: string
                    enum:
                      - firewallEnabled
              id:
                allOf:
                  - nullable: true
              value:
                allOf:
                  - type: boolean
            required: true
            description: Enable Firewall
            requiredProperties:
              - action
              - value
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - rules.insert
              id:
                allOf:
                  - nullable: true
              value:
                allOf:
                  - type: object
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
                                        type: array
                                        items:
                                          type: string
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
                                type: string
                                nullable: true
                              bypassSystem:
                                type: boolean
                                nullable: true
                            required:
                              - action
                            additionalProperties: false
                        additionalProperties: false
                    required:
                      - name
                      - active
                      - conditionGroup
                      - action
                    additionalProperties: false
            required: true
            description: Add a custom rule
            requiredProperties:
              - action
              - value
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - rules.update
              id:
                allOf:
                  - type: string
              value:
                allOf:
                  - type: object
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
                                        type: array
                                        items:
                                          type: string
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
                                type: string
                                nullable: true
                              bypassSystem:
                                type: boolean
                                nullable: true
                            required:
                              - action
                            additionalProperties: false
                        additionalProperties: false
                    required:
                      - name
                      - active
                      - conditionGroup
                      - action
                    additionalProperties: false
            required: true
            description: Update a custom rule
            requiredProperties:
              - action
              - id
              - value
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - rules.remove
              id:
                allOf:
                  - type: string
              value:
                allOf:
                  - nullable: true
            required: true
            description: Remove a custom rule
            requiredProperties:
              - action
              - id
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - rules.priority
              id:
                allOf:
                  - type: string
              value:
                allOf:
                  - type: number
            required: true
            description: Reorder a custom rule
            requiredProperties:
              - action
              - id
              - value
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - crs.update
              id:
                allOf:
                  - type: string
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
                allOf:
                  - type: object
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
            required: true
            description: Enable a managed rule
            requiredProperties:
              - action
              - id
              - value
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - crs.disable
              id:
                allOf:
                  - nullable: true
              value:
                allOf:
                  - nullable: true
            required: true
            description: Disable a managed rule
            requiredProperties:
              - action
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - ip.insert
              id:
                allOf:
                  - nullable: true
              value:
                allOf:
                  - type: object
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
            required: true
            description: Add an IP Blocking rule
            requiredProperties:
              - action
              - value
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - ip.update
              id:
                allOf:
                  - type: string
              value:
                allOf:
                  - type: object
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
            required: true
            description: Update an IP Blocking rule
            requiredProperties:
              - action
              - id
              - value
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - ip.remove
              id:
                allOf:
                  - type: string
              value:
                allOf:
                  - nullable: true
            required: true
            description: Remove an IP Blocking rule
            requiredProperties:
              - action
              - id
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - managedRules.update
              id:
                allOf:
                  - type: string
                    enum:
                      - ai_bots
                      - bot_filter
                      - bot_protection
                      - owasp
              value:
                allOf:
                  - type: object
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
            required: true
            description: Update a managed ruleset
            requiredProperties:
              - action
              - id
              - value
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
              id:
                allOf:
                  - type: string
                    enum:
                      - ai_bots
                      - bot_filter
                      - bot_protection
                      - owasp
              value:
                allOf:
                  - type: object
                    additionalProperties:
                      type: object
                      properties:
                        active:
                          type: boolean
                        action:
                          type: string
                          enum:
                            - log
                            - challenge
                            - deny
                      required:
                        - active
                      additionalProperties: false
            required: true
            description: Update a managed rule group
            requiredProperties:
              - action
              - id
              - value
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
              id:
                allOf:
                  - type: string
              value:
                allOf:
                  - type: boolean
            required: true
            description: Toggle bot ID
            requiredProperties:
              - action
              - value
            additionalProperties: false
        examples:
          example:
            value:
              action: firewallEnabled
              id: <any>
              value: true
    codeSamples:
      - label: updateFirewallConfig
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Security.UpdateFirewallConfig(ctx, \"<id>\", nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: updateFirewallConfig
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.security.updateFirewallConfig({
              projectId: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                action: "ip.remove",
                id: "<id>",
              },
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties: {}
        examples:
          example:
            value: {}
        description: ''
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
    '402': {}
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````