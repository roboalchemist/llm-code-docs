# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/put-firewall-configuration.md

# Put Firewall Configuration

> Set the firewall configuration to provided rules and settings. Creates or overwrite the existing firewall configuration.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v1/security/firewall/config
paths:
  path: /v1/security/firewall/config
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
              firewallEnabled:
                allOf:
                  - type: boolean
              managedRules:
                allOf:
                  - type: object
                    additionalProperties:
                      anyOf: []
              crs:
                allOf:
                  - type: object
                    properties:
                      sd:
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
                        description: >-
                          Scanner Detection - Detect and prevent reconnaissance
                          activities from network scanning tools.
                      ma:
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
                        description: >-
                          Multipart Attack - Block attempts to bypass security
                          controls using multipart/form-data encoding.
                      lfi:
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
                        description: >-
                          Local File Inclusion Attack - Prevent unauthorized
                          access to local files through web applications.
                      rfi:
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
                        description: >-
                          Remote File Inclusion Attack - Prohibit unauthorized
                          upload or execution of remote files.
                      rce:
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
                        description: >-
                          Remote Execution Attack - Prevent unauthorized
                          execution of remote scripts or commands.
                      php:
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
                        description: >-
                          PHP Attack - Safeguard against vulnerability exploits
                          in PHP-based applications.
                      gen:
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
                        description: >-
                          Generic Attack - Provide broad protection from various
                          undefined or novel attack vectors.
                      xss:
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
                        description: >-
                          XSS Attack - Prevent injection of malicious scripts
                          into trusted webpages.
                      sqli:
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
                        description: >-
                          SQL Injection Attack - Prohibit unauthorized use of
                          SQL commands to manipulate databases.
                      sf:
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
                        description: >-
                          Session Fixation Attack - Prevent unauthorized
                          takeover of user sessions by enforcing unique session
                          IDs.
                      java:
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
                        description: >-
                          Java Attack - Mitigate risks of exploitation targeting
                          Java-based applications or components.
                    additionalProperties: false
                    description: Custom Ruleset
              rules:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
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
                                      description: >-
                                        [Parameter](https://vercel.com/docs/security/vercel-waf/rule-configuration#parameters)
                                        from the incoming traffic.
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
              ips:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
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
              botIdEnabled:
                allOf:
                  - type: boolean
            required: true
            requiredProperties:
              - firewallEnabled
            additionalProperties: false
        examples:
          example:
            value:
              firewallEnabled: true
              managedRules: {}
              crs:
                sd:
                  active: true
                  action: deny
                ma:
                  active: true
                  action: deny
                lfi:
                  active: true
                  action: deny
                rfi:
                  active: true
                  action: deny
                rce:
                  active: true
                  action: deny
                php:
                  active: true
                  action: deny
                gen:
                  active: true
                  action: deny
                xss:
                  active: true
                  action: deny
                sqli:
                  active: true
                  action: deny
                sf:
                  active: true
                  action: deny
                java:
                  active: true
                  action: deny
              rules:
                - id: <string>
                  name: <string>
                  description: <string>
                  active: true
                  conditionGroup:
                    - conditions:
                        - type: host
                          op: re
                          neg: true
                          key: <string>
                          value: <string>
                  action:
                    mitigate:
                      action: log
                      rateLimit:
                        algo: fixed_window
                        window: 123
                        limit: 123
                        keys:
                          - <string>
                        action: log
                      redirect:
                        location: <string>
                        permanent: true
                      actionDuration: <string>
                      bypassSystem: true
              ips:
                - id: <string>
                  hostname: <string>
                  ip: <string>
                  notes: <string>
                  action: deny
              botIdEnabled: true
    codeSamples:
      - label: putFirewallConfig
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Security.PutFirewallConfig(ctx, \"<id>\", nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: putFirewallConfig
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.security.putFirewallConfig({
              projectId: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                firewallEnabled: true,
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
            properties:
              active:
                allOf:
                  - properties:
                      ownerId:
                        type: string
                      projectKey:
                        type: string
                      id:
                        type: string
                      version:
                        type: number
                      updatedAt:
                        type: string
                      firewallEnabled:
                        type: boolean
                      crs:
                        properties:
                          sd:
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
                            type: object
                            description: >-
                              Scanner Detection - Detect and prevent
                              reconnaissance activities from network scanning
                              tools.
                          ma:
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
                            type: object
                            description: >-
                              Multipart Attack - Block attempts to bypass
                              security controls using multipart/form-data
                              encoding.
                          lfi:
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
                            type: object
                            description: >-
                              Local File Inclusion Attack - Prevent unauthorized
                              access to local files through web applications.
                          rfi:
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
                            type: object
                            description: >-
                              Remote File Inclusion Attack - Prohibit
                              unauthorized upload or execution of remote files.
                          rce:
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
                            type: object
                            description: >-
                              Remote Execution Attack - Prevent unauthorized
                              execution of remote scripts or commands.
                          php:
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
                            type: object
                            description: >-
                              PHP Attack - Safeguard against vulnerability
                              exploits in PHP-based applications.
                          gen:
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
                            type: object
                            description: >-
                              Generic Attack - Provide broad protection from
                              various undefined or novel attack vectors.
                          xss:
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
                            type: object
                            description: >-
                              XSS Attack - Prevent injection of malicious
                              scripts into trusted webpages.
                          sqli:
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
                            type: object
                            description: >-
                              SQL Injection Attack - Prohibit unauthorized use
                              of SQL commands to manipulate databases.
                          sf:
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
                            type: object
                            description: >-
                              Session Fixation Attack - Prevent unauthorized
                              takeover of user sessions by enforcing unique
                              session IDs.
                          java:
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
                            type: object
                            description: >-
                              Java Attack - Mitigate risks of exploitation
                              targeting Java-based applications or components.
                        required:
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
                        type: object
                        description: Custom Ruleset
                      rules:
                        items:
                          properties:
                            id:
                              type: string
                            name:
                              type: string
                            description:
                              type: string
                            active:
                              type: boolean
                            conditionGroup:
                              items:
                                properties:
                                  conditions:
                                    items:
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
                                            - protocol
                                            - region
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
                                            - ex
                                            - inc
                                            - pre
                                            - suf
                                            - sub
                                            - gt
                                            - gte
                                            - lt
                                            - lte
                                            - nex
                                            - ninc
                                            - neq
                                        neg:
                                          type: boolean
                                        key:
                                          type: string
                                        value:
                                          oneOf:
                                            - type: string
                                            - type: number
                                            - items:
                                                type: string
                                              type: array
                                      required:
                                        - type
                                        - op
                                      type: object
                                    type: array
                                required:
                                  - conditions
                                type: object
                              type: array
                            action:
                              properties:
                                mitigate:
                                  properties:
                                    action:
                                      type: string
                                      enum:
                                        - deny
                                        - log
                                        - challenge
                                        - bypass
                                        - rate_limit
                                        - redirect
                                    rateLimit:
                                      nullable: true
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
                                          nullable: true
                                          type: string
                                          enum:
                                            - deny
                                            - log
                                            - challenge
                                            - rate_limit
                                      required:
                                        - algo
                                        - window
                                        - limit
                                        - keys
                                      type: object
                                    redirect:
                                      nullable: true
                                      properties:
                                        location:
                                          type: string
                                        permanent:
                                          type: boolean
                                      required:
                                        - location
                                        - permanent
                                      type: object
                                    actionDuration:
                                      nullable: true
                                      type: string
                                    bypassSystem:
                                      nullable: true
                                      type: boolean
                                  required:
                                    - action
                                  type: object
                              type: object
                          required:
                            - id
                            - name
                            - active
                            - conditionGroup
                            - action
                          type: object
                        type: array
                      ips:
                        items:
                          properties:
                            id:
                              type: string
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
                                - log
                                - challenge
                                - bypass
                          required:
                            - id
                            - hostname
                            - ip
                            - action
                          type: object
                        type: array
                      changes:
                        items:
                          type: object
                        type: array
                      managedRules:
                        properties:
                          bot_protection:
                            properties:
                              active:
                                type: boolean
                              action:
                                type: string
                                enum:
                                  - deny
                                  - log
                                  - challenge
                              updatedAt:
                                type: string
                              userId:
                                type: string
                              username:
                                type: string
                            required:
                              - active
                            type: object
                          ai_bots:
                            properties:
                              active:
                                type: boolean
                              action:
                                type: string
                                enum:
                                  - deny
                                  - log
                                  - challenge
                              updatedAt:
                                type: string
                              userId:
                                type: string
                              username:
                                type: string
                            required:
                              - active
                            type: object
                          owasp:
                            properties:
                              active:
                                type: boolean
                              action:
                                type: string
                                enum:
                                  - deny
                                  - log
                                  - challenge
                              updatedAt:
                                type: string
                              userId:
                                type: string
                              username:
                                type: string
                            required:
                              - active
                            type: object
                        type: object
                      botIdEnabled:
                        type: boolean
                    required:
                      - ownerId
                      - projectKey
                      - id
                      - version
                      - updatedAt
                      - firewallEnabled
                      - crs
                      - rules
                      - ips
                      - changes
                    type: object
            requiredProperties:
              - active
        examples:
          example:
            value:
              active:
                ownerId: <string>
                projectKey: <string>
                id: <string>
                version: 123
                updatedAt: <string>
                firewallEnabled: true
                crs:
                  sd:
                    active: true
                    action: deny
                  ma:
                    active: true
                    action: deny
                  lfi:
                    active: true
                    action: deny
                  rfi:
                    active: true
                    action: deny
                  rce:
                    active: true
                    action: deny
                  php:
                    active: true
                    action: deny
                  gen:
                    active: true
                    action: deny
                  xss:
                    active: true
                    action: deny
                  sqli:
                    active: true
                    action: deny
                  sf:
                    active: true
                    action: deny
                  java:
                    active: true
                    action: deny
                rules:
                  - id: <string>
                    name: <string>
                    description: <string>
                    active: true
                    conditionGroup:
                      - conditions:
                          - type: host
                            op: re
                            neg: true
                            key: <string>
                            value: <string>
                    action:
                      mitigate:
                        action: deny
                        rateLimit:
                          algo: fixed_window
                          window: 123
                          limit: 123
                          keys:
                            - <string>
                          action: deny
                        redirect:
                          location: <string>
                          permanent: true
                        actionDuration: <string>
                        bypassSystem: true
                ips:
                  - id: <string>
                    hostname: <string>
                    ip: <string>
                    notes: <string>
                    action: deny
                changes:
                  - {}
                managedRules:
                  bot_protection:
                    active: true
                    action: deny
                    updatedAt: <string>
                    userId: <string>
                    username: <string>
                  ai_bots:
                    active: true
                    action: deny
                    updatedAt: <string>
                    userId: <string>
                    username: <string>
                  owasp:
                    active: true
                    action: deny
                    updatedAt: <string>
                    userId: <string>
                    username: <string>
                botIdEnabled: true
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