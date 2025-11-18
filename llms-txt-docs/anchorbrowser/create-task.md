# Source: https://docs.anchorbrowser.io/api-reference/tasks/create-task.md

# Create Task

> Creates a new task or updates an existing task with the same name. Tasks are reusable code snippets 
that can be executed in browser sessions. Tasks support versioning with draft and published versions.


## OpenAPI

````yaml openapi-mintlify.yaml post /v1/task
paths:
  path: /v1/task
  method: post
  servers:
    - url: https://api.anchorbrowser.io
      description: API server
  request:
    security:
      - title: api key header
        parameters:
          query: {}
          header:
            anchor-api-key:
              type: apiKey
              description: API key passed in the header
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
              name:
                allOf:
                  - type: string
                    pattern: ^[a-zA-Z0-9_-]+$
                    minLength: 1
                    maxLength: 255
                    description: >-
                      Task name (letters, numbers, hyphens, and underscores
                      only)
              code:
                allOf:
                  - type: string
                    pattern: ^[A-Za-z0-9+/]*={0,2}$
                    description: Base64 encoded task code (optional)
              language:
                allOf:
                  - type: string
                    enum:
                      - typescript
                    description: Programming language for the task
              description:
                allOf:
                  - type: string
                    maxLength: 1000
                    description: Optional description of the task
              browserConfiguration:
                allOf:
                  - $ref: '#/components/schemas/SessionConfig'
                    description: Browser configuration for task execution
            required: true
            refIdentifier: '#/components/schemas/CreateTaskRequest'
            requiredProperties:
              - name
              - language
        examples:
          createTask:
            summary: Create a new task
            value:
              name: web-scraper
              language: typescript
              description: A task to scrape product information from e-commerce sites
              code: >-
                Y29uc3QgYW5jaG9yID0gcmVxdWlyZSgnYW5jaG9yYnJvd3NlcicpOwoKYXN5bmMgZnVuY3Rpb24gcnVuKCkgewogIGNvbnN0IHNlc3Npb24gPSBhd2FpdCBhbmNob3IuY3JlYXRlU2Vzc2lvbigpOwogIGF3YWl0IHNlc3Npb24uZ29UbygnaHR0cHM6Ly9leGFtcGxlLmNvbScpOwogIGNvbnN0IHRpdGxlID0gYXdhaXQgc2Vzc2lvbi5nZXRUaXRsZSgpOwogIGNvbnNvbGUubG9nKHRpdGxlKTsKICBhd2FpdCBzZXNzaW9uLmNsb3NlKCk7Cn0KcnVuKCk7
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - $ref: '#/components/schemas/Task'
            refIdentifier: '#/components/schemas/TaskResponse'
        examples:
          example:
            value:
              data:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                name: <string>
                teamId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                description: <string>
                latestVersion: <string>
                code: <string>
                language: typescript
                browserConfiguration:
                  initial_url: <string>
                  recording:
                    active: true
                  proxy:
                    active: true
                    type: anchor_proxy
                    country_code: af
                    region: <string>
                    city: <string>
                  timeout:
                    max_duration: 123
                    idle_timeout: 123
                  live_view:
                    read_only: true
                deleted: true
                createdAt: '2023-11-07T05:31:56Z'
                updatedAt: '2023-11-07T05:31:56Z'
        description: Task created or updated successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: object
                    properties:
                      code:
                        type: integer
                      message:
                        type: string
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Invalid request or validation failed
    '409':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Task name already exists
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Failed to create task
  deprecated: false
  type: path
components:
  schemas:
    ProxyConfig:
      description: |
        Proxy Documentation available at [Proxy Documentation](/advanced/proxy)
      type: object
      oneOf:
        - $ref: '#/components/schemas/AnchorProxy'
        - $ref: '#/components/schemas/CustomProxy'
    AnchorProxy:
      title: Anchor Proxy
      type: object
      properties:
        active:
          type: boolean
        type:
          type: string
          description: |
            **On change make sure to update the country_code.**
          oneOf:
            - enum:
                - anchor_proxy
                - anchor_residential
                - anchor_mobile
                - anchor_gov
              title: anchor_residential
              description: >-
                Create a session with a residential proxy to access websites as
                if you're browsing from a computer in that country.
            - enum:
                - anchor_proxy
                - anchor_residential
                - anchor_mobile
                - anchor_gov
              description: >-
                Create a session with a mobile proxy to access websites as if
                you're browsing from a mobile device in that country.
              title: anchor_mobile
            - enum:
                - anchor_proxy
                - anchor_residential
                - anchor_mobile
                - anchor_gov
              description: >-
                Create your session with a residential proxy to access websites
                as if you're browsing from a computer in that country. This
                option reduces the chance of being blocked by governmental
                websites.
              title: anchor_gov
            - enum:
                - anchor_proxy
                - anchor_residential
                - anchor_mobile
                - anchor_gov
              description: >-
                Create a session with a proxy to access websites as if you're
                browsing from a computer in that country.
              title: anchor_proxy
        country_code:
          oneOf:
            - $ref: '#/components/schemas/AnchorProxyCountryCode'
            - $ref: '#/components/schemas/ResidentialCountryCode'
            - $ref: '#/components/schemas/MobileCountryCode'
            - $ref: '#/components/schemas/GovCountryCode'
          description: |
            Supported country codes ISO 2 lowercase

            **On change make sure to update the Proxy type.**
        region:
          type: string
          description: |
            Region code for more specific geographic targeting.
            The city parameter can only be used when region is also provided.
        city:
          type: string
          description: >
            City name for precise geographic targeting. Supported for
            anchor_proxy only.

            Can only be used when region is also provided.
      required:
        - active
    CustomProxy:
      title: Custom Proxy
      type: object
      properties:
        type:
          type: string
          enum:
            - custom
        server:
          type: string
          description: Proxy server address
        username:
          type: string
          description: Proxy username
        password:
          type: string
          description: Proxy password
        active:
          type: boolean
      required:
        - type
        - server
        - username
        - password
        - active
    ResidentialCountryCode:
      type: string
      title: anchor_residential
      enum:
        - af
        - al
        - dz
        - ad
        - ao
        - ag
        - ar
        - am
        - aw
        - au
        - at
        - az
        - bs
        - bh
        - bd
        - bb
        - by
        - be
        - bz
        - bj
        - bm
        - bo
        - ba
        - bw
        - br
        - bn
        - bg
        - bf
        - bi
        - kh
        - cm
        - ca
        - cv
        - td
        - cl
        - cn
        - co
        - cg
        - cr
        - ci
        - hr
        - cu
        - cy
        - cz
        - dk
        - dj
        - dm
        - do
        - ec
        - eg
        - sv
        - gq
        - ee
        - sz
        - et
        - fj
        - fi
        - fr
        - pf
        - ga
        - gm
        - ge
        - de
        - gh
        - gr
        - gd
        - gt
        - gn
        - gy
        - ht
        - hn
        - hk
        - hu
        - is
        - in
        - id
        - ir
        - iq
        - ie
        - il
        - it
        - jm
        - jp
        - jo
        - kz
        - ke
        - kw
        - kg
        - la
        - lv
        - lb
        - ls
        - lr
        - ly
        - lt
        - lu
        - mk
        - mg
        - mw
        - my
        - mv
        - ml
        - mt
        - mr
        - mx
        - md
        - mn
        - me
        - ma
        - mz
        - mm
        - na
        - np
        - nl
        - nc
        - nz
        - ni
        - ne
        - ng
        - 'no'
        - om
        - pk
        - pa
        - pg
        - py
        - pe
        - ph
        - pl
        - pt
        - pr
        - qa
        - ro
        - ru
        - rw
        - lc
        - ws
        - sm
        - sa
        - sn
        - rs
        - sl
        - sg
        - sk
        - si
        - so
        - za
        - kr
        - ss
        - es
        - lk
        - sd
        - sr
        - se
        - ch
        - sy
        - st
        - tw
        - tj
        - tz
        - th
        - tl
        - tr
        - tg
        - tt
        - tn
        - tm
        - ug
        - ua
        - gb
        - us
        - uy
        - uz
        - vu
        - ve
        - vn
        - ye
        - zm
        - zw
      default: us
    MobileCountryCode:
      type: string
      title: anchor_mobile
      enum:
        - af
        - al
        - dz
        - ao
        - ag
        - ar
        - am
        - au
        - at
        - az
        - bs
        - bh
        - bd
        - bb
        - be
        - bz
        - bj
        - bt
        - bo
        - ba
        - bw
        - br
        - bg
        - bf
        - kh
        - cm
        - ca
        - cv
        - cl
        - cn
        - co
        - cg
        - ci
        - hr
        - cu
        - cy
        - cz
        - dk
        - do
        - ec
        - eg
        - sv
        - ee
        - et
        - fj
        - fi
        - fr
        - ga
        - gm
        - ge
        - de
        - gh
        - gr
        - gt
        - gw
        - gy
        - ht
        - hn
        - hu
        - is
        - in
        - id
        - iq
        - ie
        - il
        - it
        - jm
        - jp
        - jo
        - kz
        - ke
        - kw
        - kg
        - la
        - lv
        - lb
        - lr
        - ly
        - lt
        - mk
        - mw
        - my
        - mv
        - ml
        - mt
        - mu
        - mx
        - md
        - mn
        - me
        - ma
        - mz
        - np
        - nl
        - nc
        - nz
        - na
        - ni
        - ng
        - 'no'
        - om
        - pk
        - pa
        - py
        - pe
        - ph
        - pl
        - pt
        - qa
        - ro
        - ru
        - rw
        - sa
        - sn
        - rs
        - sl
        - sg
        - sk
        - si
        - za
        - kr
        - es
        - lk
        - sd
        - se
        - ch
        - sy
        - tw
        - tj
        - tz
        - th
        - tg
        - tt
        - tn
        - tr
        - ug
        - ua
        - ae
        - gb
        - us
        - uy
        - uz
        - ve
        - vn
        - ye
        - zm
        - zw
      default: us
    GovCountryCode:
      type: string
      title: anchor_gov
      enum:
        - af
        - al
        - dz
        - ad
        - ao
        - as
        - ag
        - ar
        - am
        - aw
        - au
        - at
        - az
        - bs
        - bh
        - bb
        - by
        - be
        - bz
        - bj
        - bm
        - bo
        - ba
        - br
        - bg
        - bf
        - cm
        - ca
        - cv
        - td
        - cl
        - co
        - cg
        - cr
        - ci
        - hr
        - cu
        - cy
        - cz
        - dk
        - dm
        - do
        - ec
        - eg
        - sv
        - ee
        - et
        - fo
        - fi
        - fr
        - gf
        - pf
        - ga
        - gm
        - ge
        - de
        - gh
        - gi
        - gr
        - gd
        - gp
        - gt
        - gg
        - gn
        - gw
        - gy
        - ht
        - hn
        - hu
        - is
        - in
        - ir
        - iq
        - ie
        - il
        - it
        - jm
        - jp
        - jo
        - kz
        - kw
        - kg
        - lv
        - lb
        - ly
        - li
        - lt
        - lu
        - mk
        - ml
        - mt
        - mq
        - mr
        - mx
        - md
        - mc
        - me
        - ma
        - nl
        - nz
        - ni
        - ng
        - 'no'
        - pk
        - pa
        - py
        - pe
        - ph
        - pl
        - pt
        - pr
        - qa
        - ro
        - lc
        - sm
        - sa
        - sn
        - rs
        - sc
        - sl
        - sk
        - si
        - so
        - za
        - kr
        - es
        - sr
        - se
        - ch
        - sy
        - st
        - tw
        - tj
        - tg
        - tt
        - tn
        - tr
        - tc
        - ua
        - ae
        - us
        - uy
        - uz
        - ve
        - ye
      default: us
    AnchorProxyCountryCode:
      type: string
      title: anchor_proxy
      enum:
        - af
        - al
        - dz
        - ad
        - ao
        - as
        - ag
        - ar
        - am
        - aw
        - au
        - at
        - az
        - bs
        - bh
        - bb
        - by
        - be
        - bz
        - bj
        - bm
        - bo
        - ba
        - br
        - bg
        - bf
        - cm
        - ca
        - cv
        - td
        - cl
        - co
        - cg
        - cr
        - ci
        - hr
        - cu
        - cy
        - cz
        - dk
        - dm
        - do
        - ec
        - eg
        - sv
        - ee
        - et
        - fo
        - fi
        - fr
        - gf
        - pf
        - ga
        - gm
        - ge
        - de
        - gh
        - gi
        - gr
        - gd
        - gp
        - gt
        - gg
        - gn
        - gw
        - gy
        - ht
        - hn
        - hu
        - is
        - in
        - ir
        - iq
        - ie
        - il
        - it
        - jm
        - jp
        - jo
        - kz
        - kw
        - kg
        - lv
        - lb
        - ly
        - li
        - lt
        - lu
        - mk
        - ml
        - mt
        - mq
        - mr
        - mx
        - md
        - mc
        - me
        - ma
        - nl
        - nz
        - ni
        - ng
        - 'no'
        - pk
        - pa
        - py
        - pe
        - ph
        - pl
        - pt
        - pr
        - qa
        - ro
        - lc
        - sm
        - sa
        - sn
        - rs
        - sc
        - sl
        - sk
        - si
        - so
        - za
        - kr
        - es
        - sr
        - se
        - ch
        - sy
        - st
        - tw
        - tj
        - tg
        - tt
        - tn
        - tr
        - tc
        - ua
        - ae
        - us
        - uy
        - uz
        - ve
        - ye
      default: us
    SessionConfig:
      type: object
      description: Session-related configurations.
      properties:
        initial_url:
          type: string
          format: uri
          description: >-
            The URL to navigate to when the browser session starts. If not
            provided, the browser will load an empty page.
        recording:
          type: object
          description: Configuration for session recording.
          properties:
            active:
              type: boolean
              description: >-
                Enable or disable video recording of the browser session.
                Defaults to `true`.
        proxy:
          $ref: '#/components/schemas/ProxyConfig'
        timeout:
          type: object
          description: Timeout configurations for the browser session.
          properties:
            max_duration:
              type: integer
              description: >-
                Maximum amount of time (in minutes) for the browser to run
                before terminating. Defaults to `20`.
            idle_timeout:
              type: integer
              description: >-
                The amount of time (in minutes) the browser session waits for
                new connections after all others are closed before stopping.
                Defaults to `5`.
        live_view:
          type: object
          description: Configuration for live viewing the browser session.
          properties:
            read_only:
              type: boolean
              description: >-
                Enable or disable read-only mode for live viewing. Defaults to
                `false`.
    Task:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the task
        name:
          type: string
          pattern: ^[a-zA-Z0-9_-]+$
          minLength: 1
          maxLength: 255
          description: Task name (letters, numbers, hyphens, and underscores only)
        teamId:
          type: string
          format: uuid
          description: Team identifier that owns this task
        description:
          type: string
          maxLength: 1000
          description: Optional description of the task
        latestVersion:
          type: string
          description: Latest version identifier (draft, latest, or version number)
        code:
          type: string
          description: Base64 encoded task code
        language:
          type: string
          enum:
            - typescript
          description: Programming language for the task
        browserConfiguration:
          $ref: '#/components/schemas/SessionConfig'
          description: Browser configuration for task execution
        deleted:
          type: boolean
          description: Whether the task is soft deleted
        createdAt:
          type: string
          format: date-time
          description: Task creation timestamp
        updatedAt:
          type: string
          format: date-time
          description: Task last update timestamp
      required:
        - id
        - name
        - teamId
        - latestVersion
        - code
        - language
        - deleted
        - createdAt
        - updatedAt

````