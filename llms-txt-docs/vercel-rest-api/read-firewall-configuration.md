# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/read-firewall-configuration.md

# Read Firewall Configuration

> Retrieve the specified firewall configuration for a project. The deployed configVersion will be `active`

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/security/firewall/config/{configVersion}
paths:
  path: /v1/security/firewall/config/{configVersion}
  method: get
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
        configVersion:
          schema:
            - type: string
              required: true
              description: The deployed configVersion for the firewall configuration
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
    body: {}
    codeSamples:
      - label: getFirewallConfig
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Security.GetFirewallConfig(ctx, \"<id>\", \"<value>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getFirewallConfig
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.security.getFirewallConfig({
              projectId: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              configVersion: "<value>",
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
              ownerId:
                allOf:
                  - type: string
              projectKey:
                allOf:
                  - type: string
              id:
                allOf:
                  - type: string
              version:
                allOf:
                  - type: number
              updatedAt:
                allOf:
                  - type: string
              firewallEnabled:
                allOf:
                  - type: boolean
              crs:
                allOf:
                  - properties:
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
                          Scanner Detection - Detect and prevent reconnaissance
                          activities from network scanning tools.
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
                          Multipart Attack - Block attempts to bypass security
                          controls using multipart/form-data encoding.
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
                          Remote File Inclusion Attack - Prohibit unauthorized
                          upload or execution of remote files.
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
                          PHP Attack - Safeguard against vulnerability exploits
                          in PHP-based applications.
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
                          Generic Attack - Provide broad protection from various
                          undefined or novel attack vectors.
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
                          XSS Attack - Prevent injection of malicious scripts
                          into trusted webpages.
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
                          SQL Injection Attack - Prohibit unauthorized use of
                          SQL commands to manipulate databases.
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
                          takeover of user sessions by enforcing unique session
                          IDs.
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
                          Java Attack - Mitigate risks of exploitation targeting
                          Java-based applications or components.
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
                allOf:
                  - items:
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
                                      description: >-
                                        [Parameter](https://vercel.com/docs/security/vercel-waf/rule-configuration#parameters)
                                        from the incoming traffic.
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
                allOf:
                  - items:
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
                allOf:
                  - items:
                      type: object
                    type: array
              managedRules:
                allOf:
                  - properties:
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
                allOf:
                  - type: boolean
            requiredProperties:
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
        examples:
          example:
            value:
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
        description: >-
          If the firewall configuration includes a [custom managed
          ruleset](https://vercel.com/docs/security/vercel-waf/managed-rulesets),
          it will include a `crs` item that has the following values: sd:
          Scanner Detection ma: Multipart Attack lfi: Local File Inclusion
          Attack rfi: Remote File Inclusion Attack rce: Remote Execution Attack
          php: PHP Attack gen: Generic Attack xss: XSS Attack sqli: SQL
          Injection Attack sf: Session Fixation Attack java: Java Attack
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
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
  deprecated: false
  type: path
components:
  schemas: {}

````