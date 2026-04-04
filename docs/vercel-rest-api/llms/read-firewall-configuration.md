# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/read-firewall-configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Firewall Configuration

> Retrieve the specified firewall configuration for a project. The deployed configVersion will be `active`



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/security/firewall/config/{configVersion}
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
  /v1/security/firewall/config/{configVersion}:
    get:
      tags:
        - security
      summary: Read Firewall Configuration
      description: >-
        Retrieve the specified firewall configuration for a project. The
        deployed configVersion will be `active`
      operationId: getFirewallConfig
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
        - description: The deployed configVersion for the firewall configuration
          in: path
          name: configVersion
          required: true
          schema:
            type: string
      responses:
        '200':
          description: >-
            If the firewall configuration includes a [custom managed
            ruleset](https://vercel.com/docs/security/vercel-waf/managed-rulesets),
            it will include a `crs` item that has the following values: sd:
            Scanner Detection ma: Multipart Attack lfi: Local File Inclusion
            Attack rfi: Remote File Inclusion Attack rce: Remote Execution
            Attack php: PHP Attack gen: Generic Attack xss: XSS Attack sqli: SQL
            Injection Attack sf: Session Fixation Attack java: Java Attack
          content:
            application/json:
              schema:
                properties:
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
                    enum:
                      - false
                      - true
                  crs:
                    properties:
                      sd:
                        properties:
                          active:
                            type: boolean
                            enum:
                              - false
                              - true
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - action
                          - active
                        type: object
                        description: >-
                          Scanner Detection - Detect and prevent reconnaissance
                          activities from network scanning tools.
                      ma:
                        properties:
                          active:
                            type: boolean
                            enum:
                              - false
                              - true
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - action
                          - active
                        type: object
                        description: >-
                          Multipart Attack - Block attempts to bypass security
                          controls using multipart/form-data encoding.
                      lfi:
                        properties:
                          active:
                            type: boolean
                            enum:
                              - false
                              - true
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - action
                          - active
                        type: object
                        description: >-
                          Local File Inclusion Attack - Prevent unauthorized
                          access to local files through web applications.
                      rfi:
                        properties:
                          active:
                            type: boolean
                            enum:
                              - false
                              - true
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - action
                          - active
                        type: object
                        description: >-
                          Remote File Inclusion Attack - Prohibit unauthorized
                          upload or execution of remote files.
                      rce:
                        properties:
                          active:
                            type: boolean
                            enum:
                              - false
                              - true
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - action
                          - active
                        type: object
                        description: >-
                          Remote Execution Attack - Prevent unauthorized
                          execution of remote scripts or commands.
                      php:
                        properties:
                          active:
                            type: boolean
                            enum:
                              - false
                              - true
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - action
                          - active
                        type: object
                        description: >-
                          PHP Attack - Safeguard against vulnerability exploits
                          in PHP-based applications.
                      gen:
                        properties:
                          active:
                            type: boolean
                            enum:
                              - false
                              - true
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - action
                          - active
                        type: object
                        description: >-
                          Generic Attack - Provide broad protection from various
                          undefined or novel attack vectors.
                      xss:
                        properties:
                          active:
                            type: boolean
                            enum:
                              - false
                              - true
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - action
                          - active
                        type: object
                        description: >-
                          XSS Attack - Prevent injection of malicious scripts
                          into trusted webpages.
                      sqli:
                        properties:
                          active:
                            type: boolean
                            enum:
                              - false
                              - true
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - action
                          - active
                        type: object
                        description: >-
                          SQL Injection Attack - Prohibit unauthorized use of
                          SQL commands to manipulate databases.
                      sf:
                        properties:
                          active:
                            type: boolean
                            enum:
                              - false
                              - true
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - action
                          - active
                        type: object
                        description: >-
                          Session Fixation Attack - Prevent unauthorized
                          takeover of user sessions by enforcing unique session
                          IDs.
                      java:
                        properties:
                          active:
                            type: boolean
                            enum:
                              - false
                              - true
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - action
                          - active
                        type: object
                        description: >-
                          Java Attack - Mitigate risks of exploitation targeting
                          Java-based applications or components.
                    required:
                      - gen
                      - java
                      - lfi
                      - ma
                      - php
                      - rce
                      - rfi
                      - sd
                      - sf
                      - sqli
                      - xss
                    type: object
                    description: Custom Ruleset
                  rules:
                    items:
                      oneOf:
                        - properties:
                            id:
                              type: string
                            name:
                              type: string
                            description:
                              type: string
                            active:
                              type: boolean
                              enum:
                                - false
                                - true
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
                                            - bot_name
                                            - bot_category
                                        op:
                                          type: string
                                          enum:
                                            - sub
                                            - re
                                            - eq
                                            - ex
                                            - inc
                                            - pre
                                            - suf
                                            - gt
                                            - gte
                                            - lt
                                            - lte
                                            - nex
                                            - ninc
                                            - neq
                                        neg:
                                          type: boolean
                                          enum:
                                            - false
                                            - true
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
                                        - op
                                        - type
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
                                        - keys
                                        - limit
                                        - window
                                      type: object
                                    redirect:
                                      nullable: true
                                      properties:
                                        location:
                                          type: string
                                        permanent:
                                          type: boolean
                                          enum:
                                            - false
                                            - true
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
                                      enum:
                                        - false
                                        - true
                                  required:
                                    - action
                                  type: object
                              type: object
                            valid:
                              type: boolean
                              enum:
                                - true
                            validationErrors:
                              nullable: true
                          required:
                            - action
                            - active
                            - conditionGroup
                            - id
                            - name
                            - valid
                            - validationErrors
                          type: object
                        - properties:
                            id:
                              type: string
                            name:
                              type: string
                            description:
                              type: string
                            active:
                              type: boolean
                              enum:
                                - false
                                - true
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
                                            - bot_name
                                            - bot_category
                                        op:
                                          type: string
                                          enum:
                                            - sub
                                            - re
                                            - eq
                                            - ex
                                            - inc
                                            - pre
                                            - suf
                                            - gt
                                            - gte
                                            - lt
                                            - lte
                                            - nex
                                            - ninc
                                            - neq
                                        neg:
                                          type: boolean
                                          enum:
                                            - false
                                            - true
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
                                        - op
                                        - type
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
                                        - keys
                                        - limit
                                        - window
                                      type: object
                                    redirect:
                                      nullable: true
                                      properties:
                                        location:
                                          type: string
                                        permanent:
                                          type: boolean
                                          enum:
                                            - false
                                            - true
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
                                      enum:
                                        - false
                                        - true
                                  required:
                                    - action
                                  type: object
                              type: object
                            valid:
                              type: boolean
                              enum:
                                - false
                            validationErrors:
                              items:
                                type: string
                              type: array
                          required:
                            - action
                            - active
                            - conditionGroup
                            - id
                            - name
                            - valid
                            - validationErrors
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
                        - action
                        - hostname
                        - id
                        - ip
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
                            enum:
                              - false
                              - true
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
                            enum:
                              - false
                              - true
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
                            enum:
                              - false
                              - true
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
                      vercel_ruleset:
                        properties:
                          active:
                            type: boolean
                            enum:
                              - false
                              - true
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
                    enum:
                      - false
                      - true
                required:
                  - changes
                  - crs
                  - firewallEnabled
                  - id
                  - ips
                  - ownerId
                  - projectKey
                  - rules
                  - updatedAt
                  - version
                type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
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